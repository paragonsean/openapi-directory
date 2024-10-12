# Shotstack.Edit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback** | **String** | An optional webhook callback URL used to receive status notifications when a render completes or fails. See [webhooks](https://shotstack.gitbook.io/docs/guides/architecting-an-application/webhooks) for  more details. | [optional] 
**disk** | **String** | The disk type to use for storing footage and assets for each render. See [disk types](https://shotstack.gitbook.io/docs/guides/architecting-an-application/disk-types) for more details. &lt;ul&gt;   &lt;li&gt;&#x60;local&#x60; - optimized for high speed rendering with up to 512MB storage&lt;/li&gt;   &lt;li&gt;&#x60;mount&#x60; - optimized for larger file sizes and longer videos with 5GB for source footage and 512MB for output render&lt;/li&gt; &lt;/ul&gt; | [optional] [default to &#39;local&#39;]
**output** | [**Output**](Output.md) |  | 
**timeline** | [**Timeline**](Timeline.md) |  | 



## Enum: DiskEnum


* `local` (value: `"local"`)

* `mount` (value: `"mount"`)




