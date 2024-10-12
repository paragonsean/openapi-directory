

# Config


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | Baskets capacity, defines maximum number of requests to store |  [optional] |
|**expandPath** | **Boolean** | If set to &#x60;true&#x60; the forward URL path will be expanded when original HTTP request contains compound path. |  [optional] |
|**forwardUrl** | **String** | URL to forward all incoming requests of the basket, &#x60;empty&#x60; value disables forwarding |  [optional] |
|**insecureTls** | **Boolean** | If set to &#x60;true&#x60; the certificate verification will be disabled if forward URL indicates HTTPS scheme. **Warning:** enabling this feature has known security implications.  |  [optional] |
|**proxyResponse** | **Boolean** | If set to &#x60;true&#x60; this basket behaves as a full proxy: responses from underlying service configured in &#x60;forward_url&#x60; are passed back to clients of original requests. The configuration of basket responses is ignored in this case.  |  [optional] |



