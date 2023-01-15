import time
from selenium.webdriver.common.by import By
from config import email, password, password1, numb, log, nev_log, nev_numb, nev_email, unvaild_password, fam1, fam50, famili, nam1, nam50, nam_lat, pas_7, pass_21, kirill, pass_bez_zag


# Проверка наличия табов
def test_clic_tab_1(driver):
    mail = driver.find_element(By.ID, "t-btn-tab-mail")
    mail.click()
    time.sleep(1)
    log = driver.find_element(By.ID, "t-btn-tab-login")
    log.click()
    time.sleep(1)
    lic_chet = driver.find_element(By.ID, "t-btn-tab-ls")
    lic_chet.click()
    time.sleep(1)
    assert mail is not None and log is not None and lic_chet is not None

# Авторизация по номеру телефона.
def test_auth_po_number_2(driver):
    author = driver.find_element(By.ID, "username")
    author.send_keys(numb)
    time.sleep(1)
    passw = driver.find_element(By.ID, "password")
    passw.send_keys(password)
    time.sleep(1)
    enter = driver.find_element(By.XPATH, "//*[@id=\"kc-login\"]")
    enter.click()
    time.sleep(2)
    uch_dann = driver.find_element(By.XPATH, "//*[@id=\"app\"]/main[1]/div[1]/div[2]/div[1]/h3[1]")
    assert uch_dann is not None


# Авторизация с неверным паролем.
def test_unvalid_passw_3(driver):
    author = driver.find_element(By.ID, "username")
    author.send_keys(numb)
    time.sleep(1)
    unv_pass = driver.find_element(By.ID, "password")
    unv_pass.send_keys(unvaild_password)
    time.sleep(1)
    enter = driver.find_element(By.XPATH, "//*[@id=\"kc-login\"]")
    enter.click()
    time.sleep(2)
    eror_mess = driver.find_element(By.ID, "form-error-message")
    assert eror_mess is not None


# Авторизация по электронной почте
def test_auth_po_email_4(driver):
    tab = driver.find_element(By.ID, "t-btn-tab-mail")
    tab.click()
    time.sleep(1)
    aut_em = driver.find_element(By.ID, "username")
    aut_em.send_keys(email)
    time.sleep(1)
    passw = driver.find_element(By.ID, "password")
    passw.send_keys(password1)
    time.sleep(1)
    enter = driver.find_element(By.XPATH, "//*[@id=\"kc-login\"]")
    enter.click()
    time.sleep(2)
    uch_dan = driver.find_element(By.XPATH, "//*[@id=\"app\"]/main[1]/div[1]/div[2]/div[1]/h3[1]")
    assert uch_dan is not None

# Авторизация по логину
def test_auth_po_log_5(driver):
    tab = driver.find_element(By.ID, "t-btn-tab-login")
    tab.click()
    time.sleep(3)
    login = driver.find_element(By.ID, "username")
    login.send_keys(log)
    time.sleep(3)
    passw = driver.find_element(By.ID,"password")
    passw.send_keys(password)
    enter = driver.find_element(By.XPATH, "//*[@id=\"kc-login\"]")
    enter.click()
    time.sleep(3)
    uch_dan = driver.find_element(By.XPATH, "//*[@id=\"app\"]/main[1]/div[1]/div[2]/div[1]/h3[1]")
    assert uch_dan is not None


# Авторизация по неверному номеру телефона
def test_autch_nev_numb_6(driver):
    new_numb = driver.find_element(By.ID, "username")
    new_numb.send_keys(nev_numb)
    time.sleep(3)
    passw = driver.find_element(By.ID, "password")
    passw.send_keys(password)
    time.sleep(3)
    enter = driver.find_element(By.XPATH, "//*[@id=\"kc-login\"]")
    enter.click()
    time.sleep(3)
    eror_mess = driver.find_element(By.ID, "form-error-message")
    assert eror_mess is not None


# Авторизация по неверной электронной почте
def test_autch_nev_mail_7(driver):
    tab = driver.find_element(By.ID, "t-btn-tab-mail")
    tab.click()
    time.sleep(3)
    new_mail = driver.find_element(By.ID, "username")
    new_mail.send_keys(nev_email)
    passw = driver.find_element(By.ID, "password")
    passw.send_keys(password1)
    time.sleep(3)
    enter = driver.find_element(By.XPATH, "//*[@id=\"kc-login\"]")
    enter.click()
    time.sleep(3)
    eror_mess = driver.find_element(By.ID, "form-error-message")
    assert eror_mess is not None


# Авторизация по неверному логину
def test_autch_nev_log_8(driver):
    tab = driver.find_element(By.ID, "t-btn-tab-login")
    tab.click()
    time.sleep(3)
    new_log = driver.find_element(By.ID, "username")
    new_log.send_keys(nev_log)
    passw = driver.find_element(By.ID, "password")
    passw.send_keys(password1)
    time.sleep(3)
    enter = driver.find_element(By.XPATH, "//*[@id=\"kc-login\"]")
    enter.click()
    time.sleep(3)
    eror_mess = driver.find_element(By.ID, "form-error-message")
    assert eror_mess is not None



# Эквивалентное знаечение.Создание фамилии из 1 символа.
def test_ekviv_znach_fam1_simv_9(driver):
    clic = driver.find_element(By.ID, "kc-register")
    clic.click()
    time.sleep(2)
    fam = driver.find_element(By.NAME, "lastName")
    fam.send_keys(fam1)
    meil = driver.find_element(By.ID, "address")
    meil.click()
    time.sleep(2)
    red_erorr = driver.find_element(By.CSS_SELECTOR, "section#page-right > div > div > div > form > div > div:nth-of-type(2) > span")
    assert red_erorr is not None


# Эквивалентное знаечение.Создание фамилии из 50 символов.
def test_ekviv_znach_fam50_simv_10(driver):
    clic = driver.find_element(By.ID, "kc-register")
    clic.click()
    time.sleep(2)
    fam = driver.find_element(By.NAME, "lastName")
    fam.send_keys(fam50)
    meil = driver.find_element(By.ID, "address")
    meil.click()
    time.sleep(2)
    red_erorr = driver.find_element(By.CSS_SELECTOR, "section#page-right > div > div > div > form > div > div:nth-of-type(2) > span")
    assert red_erorr is not None


# Создание фамилии из латинских символов
def test_fam_lat_simv11(driver):
    clic = driver.find_element(By.ID, "kc-register")
    clic.click()
    time.sleep(2)
    fam = driver.find_element(By.NAME, "lastName")
    fam.send_keys(famili)
    meil = driver.find_element(By.ID, "address")
    meil.click()
    time.sleep(2)
    red_erorr = driver.find_element(By.CSS_SELECTOR, "section#page-right > div > div > div > form > div > div:nth-of-type(2) > span")
    assert red_erorr is not None


# Создание имени из 1 символа
def test_name1_simv_12(driver):
    clic = driver.find_element(By.ID, "kc-register")
    clic.click()
    time.sleep(2)
    nam = driver.find_element(By.NAME, "firstName")
    nam.send_keys(nam1)
    meil = driver.find_element(By.ID, "address")
    meil.click()
    time.sleep(2)
    red_erorr = driver.find_element(By.CSS_SELECTOR, "section#page-right > div > div > div > form > div > div > span")
    assert red_erorr is not None


# Создание имени из 50 символов
def test_name50_simv_13(driver):
    clic = driver.find_element(By.ID, "kc-register")
    clic.click()
    time.sleep(2)
    nam = driver.find_element(By.NAME, "firstName")
    nam.send_keys(nam50)
    meil = driver.find_element(By.ID, "address")
    meil.click()
    time.sleep(2)
    red_erorr = driver.find_element(By.CSS_SELECTOR, "section#page-right > div > div > div > form > div > div > span")
    assert red_erorr is not None



# Ввод латинские символе в поле "Имя"
def test_name_lat_simv_14(driver):
    clic = driver.find_element(By.ID, "kc-register")
    clic.click()
    time.sleep(2)
    namelt = driver.find_element(By.NAME, "firstName")
    namelt.send_keys(nam_lat)
    meil = driver.find_element(By.ID, "address")
    meil.click()
    time.sleep(2)
    red_erorr = driver.find_element(By.CSS_SELECTOR, "section#page-right > div > div > div > form > div > div > span")
    assert red_erorr is not None


# Создание пароля из 7 символов
def test_passw_7simvl_15(driver):
    clic = driver.find_element(By.ID, "kc-register")
    clic.click()
    time.sleep(2)
    pass7 = driver.find_element(By.ID, "password")
    pass7.send_keys(pas_7)
    time.sleep(2)
    clic_pass = driver.find_element(By.ID, "password-confirm")
    clic_pass.click()
    time.sleep(2)
    red_erorr = driver.find_element(By.CSS_SELECTOR, "section#page-right > div > div > div > form > div > div > span")
    assert red_erorr is not None


# Создание пароля из 21 символа
def test_pass_21_simv_16(driver):
    clic = driver.find_element(By.ID, "kc-register")
    clic.click()
    time.sleep(2)
    pass21 = driver.find_element(By.ID, "password")
    pass21.send_keys(pass_21)
    time.sleep(2)
    clic_pass = driver.find_element(By.ID, "password-confirm")
    clic_pass.click()
    time.sleep(2)
    red_erorr = driver.find_element(By.CSS_SELECTOR, "section#page-right > div > div > div > form > div > div > span")
    assert red_erorr is not None


# Ввод в поле "Пароль" кириллические символы
def test_pass_kirill_17(driver):
    clic = driver.find_element(By.ID, "kc-register")
    clic.click()
    time.sleep(2)
    kirill_pass = driver.find_element(By.ID, "password")
    kirill_pass.send_keys(kirill)
    time.sleep(2)
    clic_pass = driver.find_element(By.ID, "password-confirm")
    clic_pass.click()
    time.sleep(2)
    red_erorr = driver.find_element(By.CSS_SELECTOR, "section#page-right > div > div > div > form > div > div > span")
    assert red_erorr is not None


# Ввод пароля без заглавной буквы.
def test_pass_bez_zagl_18(driver):
    clic = driver.find_element(By.ID, "kc-register")
    clic.click()
    time.sleep(2)
    pass_b_zag = driver.find_element(By.ID, "password")
    pass_b_zag.send_keys(pass_bez_zag)
    time.sleep(2)
    clic_pass = driver.find_element(By.ID, "password-confirm")
    clic_pass.click()
    time.sleep(2)
    red_erorr = driver.find_element(By.CSS_SELECTOR, "section#page-right > div > div > div > form > div > div > span")
    assert red_erorr is not None























