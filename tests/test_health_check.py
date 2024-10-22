import requests
                    
## Verify that app_under_construction returns correct under constuction page
def test_app_health_check():
    url = "https://vrubleuski.me"
    response = requests.get(url, timeout=10)
    ## Verify response code is 200
    assert 200 == response.status_code
    content = str(response.content)
    ## Verify the page contains correct welcome message
    assert 'Hello, This Page is Under Construction' in content
    ## verify there is single <h2> element on the page
    assert 1 == content.count('<h2>')