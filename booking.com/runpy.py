from booking.booking import Booking
from time import sleep

bot= Booking()
bot.land_first_page()
# bot.change_currency(currency='USD')
bot.selecte_palce_to_go('NEW YORK')
sleep(3)
bot.selecte_date('2024-07-27','2024-08-28')
sleep(3)
bot.selecte_adualt(6)
sleep(3)
bot.click_serach()
sleep(3)
bot.booking_filtration()


sleep(10)
