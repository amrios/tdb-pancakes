#!/usr/bin/python3

# Indexer for OpenTDB

import lxml
import requests
import json
from html import unescape
from bs4 import BeautifulSoup

class tdb_index:
	def get_question_id(self, question):
		tdb_query = "https://opentdb.com/browse.php?query="
		query = requests.get(tdb_query + question + "&type=Question#")
		soup = BeautifulSoup(query.text, 'lxml')
		search_table = soup.find_all("table")[0].find_all('td')[0]

		return int(search_table.get_text())

	def get_api_sample(self, count, difficulty):
		# Note we can navigate through each element with get_api_sample(10, "hard")["results"][0]
		# Only part of the program that uses the API, documentation at https://opentdb.com/api_config.php
		API = "https://opentdb.com/api.php?amount={cnt}&difficulty={dflty}".format(cnt = count, dflty = difficulty)
		print(API)
		data = requests.get(API)
		return data.json()

	def get_questions_json(self, json_data):
		results = json_data["results"]
		ques = []
		for question in results:
			ques.append(question["question"])
		return unescape(ques)

	def get_correct_answer_json(self, json_data):
		results = json_data["results"]
		ques = []
		for question in results:
			ques.append(question["correct_answer"])
		return unescape(ques)
