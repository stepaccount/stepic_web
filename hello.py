
def app(env, start_response):
    url_param_str = env['QUERY_STRING'].replace("&","\n")
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [url_param_str]
