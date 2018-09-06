import json

from flask import Blueprint, abort, g, redirect

from regex_converter import RegexConverter

shortener = Blueprint(
	'shortener',
	__name__,
)

def add_regex_converter(state):
	state.app.url_map.converters['regex'] = RegexConverter

shortener.record_once(add_regex_converter)

@shortener.route('/' + "<regex('([a-zA-Z0-9_\-\/]+)'):short>")
def check(short):
	if not hasattr(g, 'shortener_config') or short not in g.shortener_config:
		abort(404)
	return redirect(g.shortener_config[short], 302)
