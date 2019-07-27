from time import sleep

class ShoppingSite:
    def __init__(self):
        self.DEFAULT_WAIT = 2

        self.login()

    def login(self):
        # jump to login page

        # enter account

        # enter password

        # click login button
        sleep(self.DEFAULT_WAIT)

    def jumpToItemPage(self):
        sleep(self.DEFAULT_WAIT)

    def addItemToCart(self):
        sleep(self.DEFAULT_WAIT)

    def jumpToPaymentPage(self):
        sleep(self.DEFAULT_WAIT)

    def enterOrdererInfo(self):
        sleep(self.DEFAULT_WAIT)

    def waitConfirmation(self):
        sleep(65535)
