# LinodeApi.TrustedDevice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** | When this Remember Me session was started.  This corresponds to the time of login with the \&quot;Remember Me\&quot; box checked.  | [optional] [readonly] 
**expiry** | **Date** | When this TrustedDevice session expires.  Sessions typically last 30 days.  | [optional] [readonly] 
**id** | **Number** | The unique ID for this TrustedDevice | [optional] [readonly] 
**lastAuthenticated** | **Date** | The last time this TrustedDevice was successfully used to authenticate to &lt;a target&#x3D;\&quot;_top\&quot; href&#x3D;\&quot;https://login.linode.com\&quot;&gt;login.linode.com&lt;/a&gt;.  | [optional] [readonly] 
**lastRemoteAddr** | **String** | The last IP Address to successfully authenticate with this TrustedDevice.  | [optional] [readonly] 
**userAgent** | **String** | The User Agent of the browser that created this TrustedDevice session.  | [optional] [readonly] 


