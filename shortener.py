from flask import Blueprint, abort, redirect

shortener = Blueprint(
	'shortener',
	__name__,
	template_folder='templates',
	static_folder='static',
	static_url_path='/static'
)

from regex_converter import RegexConverter

@shortener.route('/' + "<regex('([a-zA-Z0-9_\-\/]+)'):short>")
def check(short):
	import json

	try:
		f = open('shortener_config.json', 'r')
	except FileNotFoundError:
		abort(500, {'message': 'missing_shortener_config_file'})

	try:
		shortener_config = json.load(f)
	except json.decoder.JSONDecodeError:
		abort(500, {'message': 'malformed_shortener_config'})

	if short not in shortener_config:
		abort(404)
	return redirect(shortener_config[short], 302)
