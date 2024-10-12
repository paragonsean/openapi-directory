

# TrustedDevice

A trusted device object represents an active Remember Me session with <a target=\"_top\" href=\"https://login.linode.com\">login.linode.com</a>. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | When this Remember Me session was started.  This corresponds to the time of login with the \&quot;Remember Me\&quot; box checked.  |  [optional] [readonly] |
|**expiry** | **OffsetDateTime** | When this TrustedDevice session expires.  Sessions typically last 30 days.  |  [optional] [readonly] |
|**id** | **Integer** | The unique ID for this TrustedDevice |  [optional] [readonly] |
|**lastAuthenticated** | **OffsetDateTime** | The last time this TrustedDevice was successfully used to authenticate to &lt;a target&#x3D;\&quot;_top\&quot; href&#x3D;\&quot;https://login.linode.com\&quot;&gt;login.linode.com&lt;/a&gt;.  |  [optional] [readonly] |
|**lastRemoteAddr** | **String** | The last IP Address to successfully authenticate with this TrustedDevice.  |  [optional] [readonly] |
|**userAgent** | **String** | The User Agent of the browser that created this TrustedDevice session.  |  [optional] [readonly] |



