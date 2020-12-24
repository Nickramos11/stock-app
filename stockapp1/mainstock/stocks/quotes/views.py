from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

# browser request, render home, pass dict
def home(request):
   import requests
   import json

   if request.method == 'POST':
      ticker = request.POST['ticker']

      api_requeststock = requests.get(url="https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_13a4e33ce0804011ac1723df2b58a0af")

      try:
         apistock = json.loads(api_requeststock.content)
      except Exception as e:
         apistock = "Error..."
      return render(request, 'home.html', {'api': apistock})

   else:
      return render(request, 'home.html', {'ticker': "Enter a ticker symbol in the search bar"})


# for about sect
def about(request):
   return render(request, 'about.html', {})

def add_stock(request):
   import requests
   import json
   if request.method == 'POST':
      form = StockForm(request.POST or None)

      if form.is_valid():
         form.save()
         messages.success(request,("Stock Has Been Added"))
         return redirect('add_stock')

   else:
      ticker = Stock.objects.all()
      output = []
      for ticker_item in ticker: 
         api_requeststock = requests.get(url="https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_13a4e33ce0804011ac1723df2b58a0af")
         try:
            apistock = json.loads(api_requeststock.content)
            output.append(apistock)
         except Exception as e:
            apistock = "Error..."

      return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})

def delete(request, stock_id):
   item = Stock.objects.get(pk=stock_id)
   item.delete()
   messages.success(request, ("Stock Has Been Deleted!"))

   return redirect(delete_stock)

def delete_stock(request):
   ticker = Stock.objects.all()
   return render(request, 'delete_stock.html', {'ticker': ticker})
