
def app(env, start_response):
    url_param_str = env['QUERY_STRING'].replace("&","\n")
    if url_param_str != "":
        url_param_str += "\n"
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [url_param_str]
