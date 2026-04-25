from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd

# Home route (fixes 404 on /)
@api_view(['GET'])
def home(request):
    return Response({"message": "API is running 🚀"})

# Main API
@api_view(['POST'])
def optimize_route(request):
    start = request.data.get("start")
    end = request.data.get("end")

    # Load fuel data
    df = pd.read_csv("fuel_prices.csv")

    # Find cheapest fuel city
    cheapest = df.loc[df['price'].idxmin()]

    return Response({
        "start": start,
        "end": end,
        "cheapest_fuel_stop": cheapest['city'],
        "price": cheapest['price'],
        "message": "Route optimized (basic logic)"
    })