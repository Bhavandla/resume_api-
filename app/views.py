# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from puzzles import puzzle_solver
import json

import logging
logger = logging.getLogger(__name__)


responses_dict = {'Ping': 'OK',
                  'Resume': 'https://1drv.ms/w/s!AqsCJCdtyQ7JhtU-Zgh43Z0I4H5GIQ?e=fkSOXK',
                  'Source': 'https://github.com/Bhavandla/resume_api-.git',
                  'Phone': '+1(302)268-2666',
                  'Years': '4+ years',
                  'Degree': 'Masters in Information Systems Management from Wilmington University (Aug 2016)',
                  'Status': 'https://1drv.ms/b/s!AqsCJCdtyQ7JhtVAiT3FiOZfl9wg0Q?e=91Vm3w',
                  'Position': 'https://careers-enginegroup.icims.com/jobs/2462/software-engineer-with-fullstack%2c-backend%2c-data-or-frontend-experience---new-york%2c-chicago%2c-or-san-francisco/job?hub=9',
                  'Referrer': 'Raven T. Hobson (via LinkedIn)',
                  'Email Address': 'manohar.bhavandla@outlook.com',
                  'Name': 'Saimanohar Bhavandla'
                  }


# Create your views here.:
def index(request):
    logger.debug(json.dumps(request.GET))
    q = request.GET['q']

    response = ''
    if q in responses_dict:
        response = responses_dict[q]
    elif q == 'Puzzle':
        response = puzzle_solver(request.GET['d'].decode('unicode_escape'))

    return HttpResponse(response)
