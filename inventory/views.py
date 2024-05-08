from django.shortcuts import render, redirect
from .models import Product

def buy_product(request):
    if request.method == 'POST':
        selected_product_ids = request.POST.getlist('selected_products')
        selected_products = Product.objects.filter(id__in=selected_product_ids)

        # ส่งรายการสินค้าที่ผู้ใช้เลือกไปยังหน้า Checkout
        return render(request, 'checkout.html', {'selected_products': selected_products})

    else:
        products = Product.objects.all()
        return render(request, 'buy_product.html', {'products': products})


def checkout(request):
    if request.method == 'POST':
        selected_product_ids = request.POST.getlist('selected_products')
        selected_products = Product.objects.filter(id__in=selected_product_ids)

        # คำนวณราคารวมตามจำนวนสินค้าที่เลือกและบันทึกการเปลี่ยนแปลงในฐานข้อมูล
        total_price = 0
        for product in selected_products:
            total_price += product.price * product.qty
            product.qty -= 1
            product.save()

        # แสดงหน้า Checkout พร้อมรายการสินค้าและราคารวม
        return render(request, 'checkout.html',
                      {'selected_products': selected_products,
                       'total_price': total_price})
    return redirect('product_list')

def order_confirmation(request):
    # แสดงหน้ายืนยันการสั่งซื้อหรือหน้าขอบคุณ
    return render(request, 'order_confirmation.html')
