

# Geoblock


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countries** | **List&lt;String&gt;** | Required when &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;allow&lt;/strong&gt; or &lt;strong&gt;deny&lt;/strong&gt;. The locations affected by the geo-blocking. Enter a comma-separated list (an array) of two-letter ISO 3166-1 country codes. For a list, see &lt;a href&#x3D;&#39;https://en.wikipedia.org/wiki/ISO_3166-1&#39; target&#x3D;&#39;_blank&#39;&gt;ISO 3166-1&lt;/a&gt; on wikipedia. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time that the geo-blocking rendition was created. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the geo-blocking. |  [optional] |
|**streamTargetId** | **String** | The unique alphanumeric string that identifies the stream target. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of geo-blocking to apply. The value &lt;strong&gt;allow&lt;/strong&gt; permits viewing only in the locations specified by the &lt;em&gt;countries&lt;/em&gt; parameter. The value &lt;strong&gt;deny&lt;/strong&gt; prohibits viewing in the locations specified by the &lt;em&gt;countries&lt;/em&gt; parameter. The value &lt;strong&gt;disabled&lt;/strong&gt; (the default) permits viewing everywhere. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time that the geo-blocking rendition was updated. |  [optional] |
|**whitelist** | **List&lt;String&gt;** | Whitelisted addresses can be viewed even if they&#39;re within a geo-blocked location. Enter a comma-separated list (an array) of IP addresses that always allow streaming. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| REQUESTED | &quot;requested&quot; |
| ACTIVATED | &quot;activated&quot; |
| UPDATE_REQUESTED | &quot;update_requested&quot; |
| DELETE_REQUESTED | &quot;delete_requested&quot; |
| FAILED | &quot;failed&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;disabled&quot; |
| ALLOW | &quot;allow&quot; |
| DENY | &quot;deny&quot; |



