# AmazonKinesisVideoStreams.GetDataEndpointRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**streamName** | **String** | The name of the stream that you want to get the endpoint for. You must specify either this parameter or a &lt;code&gt;StreamARN&lt;/code&gt; in the request. | [optional] 
**streamARN** | **String** | The Amazon Resource Name (ARN) of the stream that you want to get the endpoint for. You must specify either this parameter or a &lt;code&gt;StreamName&lt;/code&gt; in the request.  | [optional] 
**aPIName** | **String** | The name of the API action for which to get an endpoint. | 



## Enum: APINameEnum


* `PUT_MEDIA` (value: `"PUT_MEDIA"`)

* `GET_MEDIA` (value: `"GET_MEDIA"`)

* `LIST_FRAGMENTS` (value: `"LIST_FRAGMENTS"`)

* `GET_MEDIA_FOR_FRAGMENT_LIST` (value: `"GET_MEDIA_FOR_FRAGMENT_LIST"`)

* `GET_HLS_STREAMING_SESSION_URL` (value: `"GET_HLS_STREAMING_SESSION_URL"`)

* `GET_DASH_STREAMING_SESSION_URL` (value: `"GET_DASH_STREAMING_SESSION_URL"`)

* `GET_CLIP` (value: `"GET_CLIP"`)

* `GET_IMAGES` (value: `"GET_IMAGES"`)




