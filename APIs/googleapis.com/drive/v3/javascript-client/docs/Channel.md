# GoogleDriveApi.Channel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | The address where notifications are delivered for this channel. | [optional] 
**expiration** | **String** | Date and time of notification channel expiration, expressed as a Unix timestamp, in milliseconds. Optional. | [optional] 
**id** | **String** | A UUID or similar unique string that identifies this channel. | [optional] 
**kind** | **String** | Identifies this as a notification channel used to watch for changes to a resource, which is &#x60;api#channel&#x60;. | [optional] [default to &#39;api#channel&#39;]
**params** | **{String: String}** | Additional parameters controlling delivery channel behavior. Optional. | [optional] 
**payload** | **Boolean** | A Boolean value to indicate whether payload is wanted. Optional. | [optional] 
**resourceId** | **String** | An opaque ID that identifies the resource being watched on this channel. Stable across different API versions. | [optional] 
**resourceUri** | **String** | A version-specific identifier for the watched resource. | [optional] 
**token** | **String** | An arbitrary string delivered to the target address with each notification delivered over this channel. Optional. | [optional] 
**type** | **String** | The type of delivery mechanism used for this channel. Valid values are \&quot;web_hook\&quot; or \&quot;webhook\&quot;. | [optional] 


