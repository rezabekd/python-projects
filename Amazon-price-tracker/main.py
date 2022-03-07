import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

PRODUCT = "Instant Pot Max 6 Quart Multi-use Electric Pressure Cooker"

FROM = "example@example.com"
TO = "example@example.com"
PASSWORD = "example_password"

URL = "https://www.amazon.com/Instant-Pot-60-Max-Electric/dp/B077T9YGRM/ref=ex_alt_wg_d?_encoding=UTF8&pd_rd_i=" \
      "B077T9YGRM&psc=1&pd_rd_w=OZDdt&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pf_rd_r=PAQ800V96H3CWQ5H48DH&" \
      "pd_rd_r=7655fedc-f80a-4a8b-b459-4af7d0d242a8&pd_rd_wg=8W4lG"

ACCEPT_LANGUAGE = "cs-CZ,cs;q=0.9"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)" \
             " Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.27"

headers = {
    "Accept-Language": ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT,
}

response = requests.get(url=URL, headers=headers)
amazon_page = response.text

soup = BeautifulSoup(amazon_page, "lxml")
price_tag_span = soup.find("span", class_="a-offscreen").getText()

price_tag = price_tag_span.split("$")[1]
price = float(price_tag)

if price < 200:
    message = f"{PRODUCT} is now ${price}!"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM, password=PASSWORD)
        connection.sendmail(from_addr=FROM,
                            to_addrs=TO,
                            msg=f"Subject:Amazon Price Alert!\n\n{message}")
