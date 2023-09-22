#kredi hesaplama
anapara=float(input("Anapara(₺):"))
faiz_oranı=float(input("yıllık faiz oranı (%):"))/100
vade=int(input("vade(ay):"))

aylık_faiz_oranı=faiz_oranı/12
aylik_taksit=(anapara*aylık_faiz_oranı*(1+aylık_faiz_oranı)**vade)/((1+aylık_faiz_oranı)**vade-1)
toplam_geri_ödeme=aylik_taksit*vade

print("Aylık taksit:",round(aylik_taksit,2),"₺")
print("Toplam geri ödeme:",round(toplam_geri_ödeme,2),"₺")