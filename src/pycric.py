#!/usr/bin/env python
#
# The MIT License (MIT)
#
# Copyright (c) 2018 Yugantar Malhotra
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.


import requests


class CricApp:
    """
    The CricApp class contains all the functions to access API provided
    by cricapi.com
    """

    def __init__(self, apiKey=None):
        """

        :param apiKey: The key provided by cricapi.com to access their data

        Initialization of the user details
        """

        if apiKey:
            self.apiKey = apiKey
        else:
            raise Exception("API Key is required, please try again")

        self.api_url = "http://cricapi.com/api/"

    def response(self, url, params=None, method="get"):
        """

        :param url: The API url to be accessed
        :param params: The params required by the API to fetch data
        :param method: Request method type: get/post
        :return: json formatted data returned from the API
        """
        if params is None:
            params = {}
        if not isinstance(params, dict):
            raise Exception("Only dictionary value allowed for params")
        params.update(apikey=self.apiKey)

        if method == "post":
            resp = requests.post(url=url, params=params).json()
        else:
            resp = requests.get(url=url, params=params).json()

        if resp.get('error'):
            raise Exception(resp['error'])

        return resp

    def get_upcoming_matches(self):
        """
        The Upcoming matches API

        :return: json data
        """

        matches_url = self.api_url + "matches"
        resp = self.response(url=matches_url)
        return resp

    def get_old_matches(self):
        """
        The Old matches API

        :return: json data
        """

        matches_url = self.api_url + "cricket"
        resp = self.response(url=matches_url)
        return resp

    def get_match_calendar(self):
        """
        The Match Calendar API

        :return: json data
        """

        calendar_url = self.api_url + "matchCalendar"
        resp = self.response(url=calendar_url)
        return resp

    def get_cricket_score(self, match_id):
        """
        The Match Score API

        :param match_id: The unique id of the match
        :return: json data
        """

        score_url = self.api_url + "cricketScore"
        resp = self.response(url=score_url, params={'unique_id': match_id})
        return resp

    def get_player_stats(self, player_id):
        """
        The Player Stats API

        :param player_id: The unique id of the player
        :return: json data
        """

        player_url = self.api_url + "playerStats"
        resp = self.response(url=player_url, params={'pid': player_id})
        return resp

    def get_fantasy_summary(self, match_id):
        """
        The Fantasy Summary of a match API

        :param match_id: The unique id of the match
        :return: json data
        """

        fantasy_summary_url = self.api_url + "fantasySummary"
        resp = self.response(url=fantasy_summary_url, params={'unique_id': match_id})
        return resp

    def get_fantasy_squad(self, match_id):
        """
        The Fantasy Squad of a match API

        :param match_id: The unique id of the match
        :return: json data
        """

        fantasy_squad_url = self.api_url + "fantasySquad"
        resp = self.response(url=fantasy_squad_url, params={'unique_id': match_id})
        return resp

    def get_player_finder(self, player_name):
        """
        The Player Finder API

        :param player_name: The query string to be searched
        :return: json data
        """

        player_finder_url = self.api_url + "playerFinder"
        resp = self.response(url=player_finder_url, params={'name': player_name})
        return resp
