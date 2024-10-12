# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "openapi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.14.1",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="Adafruit IO REST API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Adafruit IO REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    ### The Internet of Things for Everyone  The Adafruit IO HTTP API provides access to your Adafruit IO data from any programming language or hardware environment that can speak HTTP. The easiest way to get started is with [an Adafruit IO learn guide](https://learn.adafruit.com/series/adafruit-io-basics) and [a simple Internet of Things capable device like the Feather Huzzah](https://www.adafruit.com/product/2821).  This API documentation is hosted on GitHub Pages and is available at [https://github.com/adafruit/io-api](https://github.com/adafruit/io-api). For questions or comments visit the [Adafruit IO Forums](https://forums.adafruit.com/viewforum.php?f&#x3D;56) or the [adafruit-io channel on the Adafruit Discord server](https://discord.gg/adafruit).  #### Authentication  Authentication for every API request happens through the &#x60;X-AIO-Key&#x60; header or query parameter and your IO API key. A simple cURL request to get all available feeds for a user with the username \&quot;io_username\&quot; and the key \&quot;io_key_12345\&quot; could look like this:      $ curl -H \&quot;X-AIO-Key: io_key_12345\&quot; https://io.adafruit.com/api/v2/io_username/feeds  Or like this:      $ curl \&quot;https://io.adafruit.com/api/v2/io_username/feeds?X-AIO-Key&#x3D;io_key_12345  Using the node.js [request](https://github.com/request/request) library, IO HTTP requests are as easy as:  &#x60;&#x60;&#x60;js var request &#x3D; require(&#39;request&#39;);  var options &#x3D; {   url: &#39;https://io.adafruit.com/api/v2/io_username/feeds&#39;,   headers: {     &#39;X-AIO-Key&#39;: &#39;io_key_12345&#39;,     &#39;Content-Type&#39;: &#39;application/json&#39;   } };  function callback(error, response, body) {   if (!error &amp;&amp; response.statusCode &#x3D;&#x3D; 200) {     var feeds &#x3D; JSON.parse(body);     console.log(feeds.length + \&quot; FEEDS AVAILABLE\&quot;);      feeds.forEach(function (feed) {       console.log(feed.name, feed.key);     })   } }  request(options, callback); &#x60;&#x60;&#x60;  Using the ESP8266 Arduino HTTPClient library, an HTTPS GET request would look like this (replacing &#x60;---&#x60; with your own values in the appropriate locations):  &#x60;&#x60;&#x60;arduino /// based on /// https://github.com/esp8266/Arduino/blob/master/libraries/ESP8266HTTPClient/examples/Authorization/Authorization.ino  #include &lt;Arduino.h&gt; #include &lt;ESP8266WiFi.h&gt; #include &lt;ESP8266WiFiMulti.h&gt; #include &lt;ESP8266HTTPClient.h&gt;  ESP8266WiFiMulti WiFiMulti;  const char* ssid &#x3D; \&quot;---\&quot;; const char* password &#x3D; \&quot;---\&quot;;  const char* host &#x3D; \&quot;io.adafruit.com\&quot;;  const char* io_key &#x3D; \&quot;---\&quot;; const char* path_with_username &#x3D; \&quot;/api/v2/---/dashboards\&quot;;  // Use web browser to view and copy // SHA1 fingerprint of the certificate const char* fingerprint &#x3D; \&quot;77 00 54 2D DA E7 D8 03 27 31 23 99 EB 27 DB CB A5 4C 57 18\&quot;;  void setup() {   Serial.begin(115200);    for(uint8_t t &#x3D; 4; t &gt; 0; t--) {     Serial.printf(\&quot;[SETUP] WAIT %d...\\n\&quot;, t);     Serial.flush();     delay(1000);   }    WiFi.mode(WIFI_STA);   WiFiMulti.addAP(ssid, password);    // wait for WiFi connection   while(WiFiMulti.run() !&#x3D; WL_CONNECTED) {     Serial.print(&#39;.&#39;);     delay(1000);   }    Serial.println(\&quot;[WIFI] connected!\&quot;);    HTTPClient http;    // start request with URL and TLS cert fingerprint for verification   http.begin(\&quot;https://\&quot; + String(host) + String(path_with_username), fingerprint);    // IO API authentication   http.addHeader(\&quot;X-AIO-Key\&quot;, io_key);    // start connection and send HTTP header   int httpCode &#x3D; http.GET();    // httpCode will be negative on error   if(httpCode &gt; 0) {     // HTTP header has been send and Server response header has been handled     Serial.printf(\&quot;[HTTP] GET response: %d\\n\&quot;, httpCode);      // HTTP 200 OK     if(httpCode &#x3D;&#x3D; HTTP_CODE_OK) {       String payload &#x3D; http.getString();       Serial.println(payload);     }      http.end();   } }  void loop() {} &#x60;&#x60;&#x60;  #### Client Libraries  We have client libraries to help you get started with your project: [Python](https://github.com/adafruit/io-client-python), [Ruby](https://github.com/adafruit/io-client-ruby), [Arduino C++](https://github.com/adafruit/Adafruit_IO_Arduino), [Javascript](https://github.com/adafruit/adafruit-io-node), and [Go](https://github.com/adafruit/io-client-go) are available. They&#39;re all open source, so if they don&#39;t already do what you want, you can fork and add any feature you&#39;d like.  
    """
)

