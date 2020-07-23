from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils.safestring import mark_safe

class Post(models.Model):
	title = models.CharField('タイトル', max_length=255)
	main_text = MarkdownxField('本文')

	def convert_markdown_to_html(self):
		return mark_safe(markdownify(self.main_text))
