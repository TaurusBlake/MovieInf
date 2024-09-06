from selenium import webdriver
from selenium.webdriver.common.by import By

# 初始化 WebDriver（确保你安装了相应的驱动程序，如 ChromeDriver）
driver = webdriver.Chrome()

# 打开目标页面
driver.get("https://www.vscinemas.com.tw/vsweb/film/detail.aspx?id=7223")

# 找到目标元素（比如通过 CSS 选择器）
element = driver.find_element(By.XPATH, "/html/body/article/section/div[2]/section/div[1]/span[1]")

# 使用 JavaScript 获取伪元素的内容
pseudo_element_content = driver.execute_script(
    "return window.getComputedStyle(arguments[0], '::before').getPropertyValue('content');",
    element
)

print(pseudo_element_content)

# 关闭浏览器
driver.quit()