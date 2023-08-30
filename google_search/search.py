from googlesearch import search

def search_google(request, num_results=10):
    response = search(request, num_results=num_results, advanced=True)
    print('Google Request: ' + request + '\n')
    for result in list(response):
        print('URL: ' + result.url)
        print('Title: ' + result.title)
        print('Description: ' + result.description + '\n')