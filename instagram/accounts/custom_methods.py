from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.utils.text import slugify

import re, datetime, random
import threading, random

class EmailThread(threading.Thread):
	def __init__(self, subject, body, from_email, recipient_list, fail_silently, html):
		self.subject = subject
		self.body = body
		self.from_email = from_email
		self.recipient_list = recipient_list
		self.fail_silently = fail_silently
		self.html = html
		threading.Thread.__init__(self)

	def run(self):
		msg = EmailMultiAlternatives(self.subject, self.body, self.from_email, self.recipient_list)
		if self.html:
			msg.attach_alternative(self.html, "text/html")
		msg.send(self.fail_silently)

def send_mail(subject, recipient_list, body='', from_email=settings.EMAIL_HOST_USER, fail_silently=False, html=None, *args, **kwargs):
	EmailThread(subject, body, from_email, recipient_list, fail_silently, html).start()

def email_verification_code():
	code = random.randrange(0, 1000000)
	code_with_zero = f'{code:06}'
	return code_with_zero

def customSlugify(author, title):
	random_int = ''.join([str(x) for x in random.sample(range(10), 3, counts=None)])
	now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	slug = str(author) + '-' + slugify(title, allow_unicode=True) + '-' + now + '-' + random_int
	return slug