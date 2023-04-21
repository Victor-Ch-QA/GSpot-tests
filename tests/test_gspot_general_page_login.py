from selene import browser, have


def test_signup():
    browser.open('/')

    browser.element('[class*=Header_login]').click()
    browser.element('[href="/signup"]').click()

    browser.element('[class*=Form_signInput][type=text]').set('Baracuda777999')
    browser.element('[class*=Form_signInput][type=email]').set('baracuda777999@gmail.com')
    browser.element('[class*=Form_signInput][type=password]').set('qwerty12345')

    browser.element('[class*=Form_signBtn]').click()


def test_login():
    browser.open('/')

    browser.element('[class*=Header_login]').click()

    browser.element('[class*=Form_signInput][type=text]').set('Baracuda777999')
    browser.element('[class*=Form_signInput][type=email]').set('baracuda777999@gmail.com')
    browser.element('[class*=Form_signInput][type=password]').set('qwerty12345')

    browser.element('[class*=Form_signBtn]').click()

    ...