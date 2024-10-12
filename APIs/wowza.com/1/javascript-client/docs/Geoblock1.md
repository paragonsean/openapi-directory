# WowzaStreamingCloudRestApiReferenceDocumentation.Geoblock1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | **[String]** | Required when &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;allow&lt;/strong&gt; or &lt;strong&gt;deny&lt;/strong&gt;. The locations affected by the geo-blocking. Enter a comma-separated list (an array) of two-letter ISO 3166-1 country codes. For a list, see &lt;a href&#x3D;&#39;https://en.wikipedia.org/wiki/ISO_3166-1&#39; target&#x3D;&#39;_blank&#39;&gt;ISO 3166-1&lt;/a&gt; on wikipedia. | [optional] 
**type** | **String** | The type of geo-blocking to apply. The value &lt;strong&gt;allow&lt;/strong&gt; permits viewing only in the locations specified by the &lt;em&gt;countries&lt;/em&gt; parameter. The value &lt;strong&gt;deny&lt;/strong&gt; prohibits viewing in the locations specified by the &lt;em&gt;countries&lt;/em&gt; parameter. The value &lt;strong&gt;disabled&lt;/strong&gt; (the default) permits viewing everywhere. | 
**whitelist** | **[String]** | Whitelisted addresses can be viewed even if they&#39;re within a geo-blocked location. Enter a comma-separated list (an array) of IP addresses that always allow streaming. | [optional] 



## Enum: TypeEnum


* `disabled` (value: `"disabled"`)

* `allow` (value: `"allow"`)

* `deny` (value: `"deny"`)




