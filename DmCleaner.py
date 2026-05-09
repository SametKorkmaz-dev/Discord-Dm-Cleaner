import requests
import time
import os

# Konsolu temizleme fonksiyonu
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    # 
    print(r"""
  _____ ______ __     _______ _  __
 / ____|  ____|\ \   / /__   __\ \/ /
| |    | |__    \ \_/ /   | |   \  / 
| |    |  __|    \   /    | |    > <  
| |____| |____    | |     | |   /  \ 
 \_____|______|   |_|     |_|  /_/\_\
                                     
    """)
    print("="*60)
    print("                 CEYTX DM CLEANER                    ")
    print("="*60)
    print(" [!] UYARI: Kullanım riski size aittir.")
    print("="*60 + "\n")

def delete_messages():
    banner()
    
    # Giriş bilgileri
    token = input("[?] Discord Token'ını gir: ").strip()
    target_id = input("[?] Hedef Kullanıcı ID'sini gir: ").strip()
    
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    # Token Doğrulama
    try:
        me = requests.get('https://discord.com/api/v9/users/@me', headers=headers).json()
        my_id = me['id']
        print(f"\n[*] Giriş Başarılı: {me['username']}")
    except:
        print("\n[-] HATA: Token geçersiz!")
        input("\nÇıkmak için Enter'a bas..."); return

    # DM Kanal Tespiti
    response = requests.post(
        'https://discord.com/api/v9/users/@me/channels',
        headers=headers,
        json={'recipient_id': target_id}
    )
    
    if response.status_code != 200:
        print(f"[-] Kanal bulunamadı!")
        input("\nÇıkmak için Enter'a bas..."); return

    channel_id = response.json()['id']
    print(f"[+] Temizlik başlıyor...\n")

    last_message_id = None
    deleted_count = 0

    while True:
        url = f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=100'
        if last_message_id:
            url += f'&before={last_message_id}'

        res = requests.get(url, headers=headers)
        if res.status_code != 200: break
            
        messages = res.json()
        if not messages:
            print("\n[+] Silinecek mesaj kalmadı.")
            break

        for msg in messages:
            if msg['author']['id'] == my_id:
                del_res = requests.delete(
                    f'https://discord.com/api/v9/channels/{channel_id}/messages/{msg["id"]}',
                    headers=headers
                )
                
                if del_res.status_code == 204:
                    deleted_count += 1
                    print(f"   [Ceytx-Silindi] Mesaj: {deleted_count}")
                    time.sleep(1.5) 
                elif del_res.status_code == 429:
                    retry_after = del_res.json().get('retry_after', 5)
                    time.sleep(retry_after)
            
            last_message_id = msg['id']

    print(f"\n[OK] Toplam {deleted_count} mesaj temizlendi.")
    input("\nKapatmak için Enter'a bas...")

if __name__ == "__main__":
    delete_messages()
