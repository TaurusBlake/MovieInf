from bf4 import Beautifulsoup
import requset
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


# 創建 Chrome 瀏覽器選項，不開啟畫面執行爬蟲
options = Options()
options.add_argument("--headless")  # 設定為無頭模式
options.add_argument("--disable-gpu")  # 禁用 GPU
#使用selenium開啟chrome driver
driver = webdriver.Chrome(options=options)

url = "https://www.vscinemas.com.tw/vsweb/film/detail.aspx?id=7258"
web = requset.get(url)
soup = Beautifulsoup(web, "lxml")

# 打开目标页面
driver.get(url)
# 找到目标元素（比如通过 CSS 选择器）
rating_url = driver.find_element(By.XPATH, "/html/body/article/section/div[2]/section/div[1]/span[1]")
# 使用 JavaScript 获取伪元素的内容(影片分級)
rating_text = driver.execute_script(
    "return window.getComputedStyle(arguments[0], '::before').getPropertyValue('content');",
    rating_url)

print(rating_text)

# 关闭浏览器
driver.quit()