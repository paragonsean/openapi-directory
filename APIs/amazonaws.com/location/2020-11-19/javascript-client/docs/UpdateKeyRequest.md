# AmazonLocationService.UpdateKeyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Updates the description for the API key resource. | [optional] 
**expireTime** | **Date** | Updates the timestamp for when the API key resource will expire in &lt;a href&#x3D;\&quot;https://www.iso.org/iso-8601-date-and-time-format.html\&quot;&gt; ISO 8601&lt;/a&gt; format: &lt;code&gt;YYYY-MM-DDThh:mm:ss.sssZ&lt;/code&gt;.  | [optional] 
**forceUpdate** | **Boolean** | &lt;p&gt;The boolean flag to be included for updating &lt;code&gt;ExpireTime&lt;/code&gt; or &lt;code&gt;Restrictions&lt;/code&gt; details.&lt;/p&gt; &lt;p&gt;Must be set to &lt;code&gt;true&lt;/code&gt; to update an API key resource that has been used in the past 7 days.&lt;/p&gt; &lt;p&gt; &lt;code&gt;False&lt;/code&gt; if force update is not preferred&lt;/p&gt; &lt;p&gt;Default value: &lt;code&gt;False&lt;/code&gt; &lt;/p&gt; | [optional] 
**noExpiry** | **Boolean** | Whether the API key should expire. Set to &lt;code&gt;true&lt;/code&gt; to set the API key to have no expiration time. | [optional] 
**restrictions** | [**CreateKeyRequestRestrictions**](CreateKeyRequestRestrictions.md) |  | [optional] 


