def get_vat(price, vat_rate):
    price = int(price)
    vat_rate = int(price)
    if price>=0 and vat_rate>=0:
        vat = price / 100 * vat_rate
        price_no_vat = price - vat
        print(price_no_vat)