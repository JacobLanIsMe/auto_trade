from django.shortcuts import render
from django.views import View
import sys
import os

# Add the root directory to sys.path to import service modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from service.mongodb_service import get_candidate_data
from model.Candidate import Candidate

class CandidateListView(View):
    def get(self, request):
        data = get_candidate_data()
        candidates = []
        for item in data:
            candidate = Candidate(
                id=str(item.get('id', '')),
                stockCode=item.get('stockCode', ''),
                companyName=item.get('companyName', ''),
                isHolding=item.get('isHolding', False)
            )
            candidates.append(candidate)
        return render(request, 'candidates.html', {'candidates': candidates})
