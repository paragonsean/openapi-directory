

# KeyResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | The Ably application ID which this key is associated with. |  [optional] |
|**capability** | [**Map&lt;String, List&lt;String&gt;&gt;**](#Map&lt;String, List&lt;String&gt;&gt;) | The capabilities that this key has. More information on capabilities can be found in the &lt;a href&#x3D;\&quot;https://ably.com/documentation/core-features/authentication#capabilities-explained\&quot;&gt;Ably documentation&lt;/a&gt;. |  [optional] |
|**created** | **Integer** | Unix timestamp representing the date and time of creation of the key. |  [optional] |
|**id** | **String** | The key ID. |  [optional] |
|**key** | **String** | The complete API key including API secret. |  [optional] |
|**modified** | **Integer** | Unix timestamp representing the date and time of the last modification of the key. |  [optional] |
|**name** | **String** | The name of the application this key is associated with. |  [optional] |



## Enum: Map&lt;String, List&lt;String&gt;&gt;

| Name | Value |
|---- | -----|
| PUBLISH | &quot;publish&quot; |
| SUBSCRIBE | &quot;subscribe&quot; |
| HISTORY | &quot;history&quot; |
| PRESENCE | &quot;presence&quot; |
| CHANNEL_METADATA | &quot;channel-metadata&quot; |
| PUSH_ADMIN | &quot;push-admin&quot; |
| PUSH_SUBSCRIBE | &quot;push-subscribe&quot; |
| STATISTICS | &quot;statistics&quot; |



