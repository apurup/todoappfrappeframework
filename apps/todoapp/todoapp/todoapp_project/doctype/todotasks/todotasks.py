# Copyright (c) 2022, apurup and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class ToDoTasks(WebsiteGenerator):
	def before_save(self):
		self.route = "app/todotasks/"+self.id
	pass
