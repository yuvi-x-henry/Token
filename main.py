import requests
import json
from urllib.parse import urlparse, parse_qs

def get_facebook_eaad_token(session_cookies):
    """
    Facebook panel script jo EAAD6V7 token extract karta hai.
    WARNING: Ye sirf educational/pentesting purpose ke liye hai.
    Apne account pe test karo aur production mein mat use karo.
    """
    
    # Facebook login page ya graph API endpoint
    url = "https://www.facebook.com/ajax/pagelet/generic.php/PageletHomePage"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Cookie': session_cookies  # Yahan apne Facebook cookies paste karo
    }
    
    try:
        response = requests.get(url, headers=headers)
        print("Status Code:", response.status_code)
        
        # EAAD6V7 token dhundne ke liye regex/pattern
        import re
        ead_token = re.search(r'EAAD6V7["\']?\s*[:=]\s*["\']([^"\']+)["\']', response.text)
        
        if ead_token:
            print(f"\n✅ EAAD6V7 Token Found!")
            print(f"Token: {ead_token.group(1)}")
            return ead_token.group(1)
        else:
            print("❌ EAAD6V7 token nahi mila. Different endpoint try karo.")
            print("Response preview:", response.text[:500])
            
    except Exception as e:
        print(f"Error: {e}")
    
    return None

# Usage example
if __name__ == "__main__":
    print("=== Facebook EAAD6V7 Token Extractor Panel ===\n")
    
    # Yahan apne Facebook session cookies paste karo (F12 > Application > Cookies)
    cookies_str = input("Apne Facebook cookies paste karo (c_user, xs, fr etc.): ")
    
    token = get_facebook_eaad_token(cookies_str)
    
    if token:
        print(f"\n💾 Token saved to token.txt")
        with open("token.txt", "w") as f:
            f.write(token)
        print("Done! ✅")
