import json

from flask import Blueprint, abort, g, redirect

shortener = Blueprint(
	'shortener',
	__name__,
)

@shortener.route('/' + "<regex('([a-zA-Z0-9_\-\/]+)'):short>")
def check(short):
	if not hasattr(g, 'shortener_config') or short not in g.shortener_config:
		abort(404)
	return redirect(shortener_config[short], 302)
