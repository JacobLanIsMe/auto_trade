from urllib import request
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from api_service.service.mongodb_service import get_candidate_data
from api_service.model.Candidate import Candidate
import logging

class CandidateListView(View):
    def get(self, request):
        logging.info("Get candidate from MongoDb")
        data = get_candidate_data()
        candidates = []
        for item in data:
            candidate = Candidate(
                id=str(item.get('id', '')),
                stockCode=item.get('stockCode', ''),
                companyName=item.get('companyName', ''),
                isHolding=item.get('isHolding', False),
                gapUpHigh=item.get('gapUpHigh', 0),
                gapUpLow=item.get('gapUpLow', 0),
                techData=item.get('techData', '')
            )
            candidates.append(candidate)
        # Sort candidates by numeric value of stockCode
        candidates.sort(key=lambda c: int(''.join(filter(str.isdigit, c.stockCode))) if c.stockCode.isdigit() else float('inf'))
        return render(request, 'candidates.html', {'candidates': candidates})

def popup_chart(request: HttpRequest):
    # Renders the popup.html template for candlestick chart
    return render(request, 'popup.html')