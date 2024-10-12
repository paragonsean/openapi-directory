

# GetDataEndpointRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**streamName** | **String** | The name of the stream that you want to get the endpoint for. You must specify either this parameter or a &lt;code&gt;StreamARN&lt;/code&gt; in the request. |  [optional] |
|**streamARN** | **String** | The Amazon Resource Name (ARN) of the stream that you want to get the endpoint for. You must specify either this parameter or a &lt;code&gt;StreamName&lt;/code&gt; in the request.  |  [optional] |
|**apIName** | [**ApINameEnum**](#ApINameEnum) | The name of the API action for which to get an endpoint. |  |



## Enum: ApINameEnum

| Name | Value |
|---- | -----|
| PUT_MEDIA | &quot;PUT_MEDIA&quot; |
| GET_MEDIA | &quot;GET_MEDIA&quot; |
| LIST_FRAGMENTS | &quot;LIST_FRAGMENTS&quot; |
| GET_MEDIA_FOR_FRAGMENT_LIST | &quot;GET_MEDIA_FOR_FRAGMENT_LIST&quot; |
| GET_HLS_STREAMING_SESSION_URL | &quot;GET_HLS_STREAMING_SESSION_URL&quot; |
| GET_DASH_STREAMING_SESSION_URL | &quot;GET_DASH_STREAMING_SESSION_URL&quot; |
| GET_CLIP | &quot;GET_CLIP&quot; |
| GET_IMAGES | &quot;GET_IMAGES&quot; |



