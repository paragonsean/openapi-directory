# StreamChatApi.TruncateChannelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hardDelete** | **Boolean** | Permanently delete channel data (messages, reactions, etc.) | [optional] 
**message** | [**MessageRequest**](MessageRequest.md) |  | [optional] 
**skipPush** | **Boolean** | When &#x60;message&#x60; is set disables all push notifications for it | [optional] 
**truncatedAt** | **Date** | Truncate channel data up to &#x60;truncated_at&#x60;. The system message (if provided) creation time is always greater than &#x60;truncated_at&#x60; | [optional] 
**user** | [**UserObjectRequest**](UserObjectRequest.md) |  | [optional] 
**userId** | **String** |  | [optional] 


