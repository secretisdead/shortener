import json

from flask import Blueprint, abort, g, redirect

shortener = Blueprint(
	'shortener',
	__name__,
)

@shortener.route('/<short>')
def check(short):
	if not hasattr(g, 'shortener_config') or short not in g.shortener_config:
		abort(404)
	return redirect(g.shortener_config[short], 302)
