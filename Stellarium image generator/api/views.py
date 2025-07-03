from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .run_stellarium import run_stellarium
import os
import time 
from .ssc_generator import generate_moon_ssc, generate_sky_ssc
from .run_stellarium import run_stellarium

class GenerateImageView(APIView):
    def post(self, request):
        # 1. Get date and time from request
        date = request.data.get("date")
        time = request.data.get("time", "20:00:00")  # Default to 8 PM

        if not date:
            return Response({"error": "Missing 'date' parameter (YYYY-MM-DD)"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # 2. Generate .ssc scripts
            moon_script = generate_moon_ssc(date, time)
            moon_image = run_stellarium(moon_script, "moon.png")
            sky_script = generate_sky_ssc(date, time)
            sky_image = run_stellarium(sky_script, "sky.png")

            # 3. Run Stellarium and generate screenshots
            

            # 4. Build response
            return Response({
                "moon_image": moon_image,
                "sky_image": sky_image
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
