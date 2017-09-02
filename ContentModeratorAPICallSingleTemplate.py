########### Python 3.2 #############
import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64

headers = {
    # Request headers
    'Content-Type': 'text/plain',
    'Ocp-Apim-Subscription-Key': '{ENTER HERE}',
}

params = urllib.parse.urlencode({
    # Request parameters
    'autocorrect': 'false',
    'PII': 'true',
    'listId': 'false',
    'classify': 'true'
})

try:
    conn = http.client.HTTPSConnection('eastus2.api.cognitive.microsoft.com')
    conn.request(
        "POST", "/contentmoderator/moderate/v1.0/ProcessText/Screen/?language=eng&%s" % params, "this is dog test", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
