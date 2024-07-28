from booking.booking import Booking

try:
    with Booking() as bot:
        bot= Booking()
        bot.land_first_page()
        #bot.change_currency(currency='USD')
        bot.selecte_palce_to_go('NEW YORK')
        bot.selecte_date('2024-07-30','2024-08-28')
        bot.selecte_adualt(3)
        bot.click_serach()
        m= bot.report_result()
        #bot.booking_filtration()
        print('done')

except Exception as e:
    print('an error occure!',e)