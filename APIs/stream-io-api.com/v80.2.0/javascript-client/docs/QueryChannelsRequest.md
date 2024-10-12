# StreamChatApi.QueryChannelsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** |  | [optional] 
**connectionId** | **String** |  | [optional] 
**filterConditions** | **{String: Object}** |  | [optional] 
**limit** | **Number** | Number of channels to limit | [optional] 
**memberLimit** | **Number** | Number of members to limit | [optional] 
**messageLimit** | **Number** | Number of messages to limit | [optional] 
**offset** | **Number** | Channel pagination offset | [optional] 
**presence** | **Boolean** |  | [optional] 
**sort** | [**[SortParamRequest]**](SortParamRequest.md) | List of sort parameters | 
**state** | **Boolean** | Whether to update channel state or not | [optional] 
**user** | [**UserObjectRequest**](UserObjectRequest.md) |  | [optional] 
**userId** | **String** |  | [optional] 
**watch** | **Boolean** | Whether to start watching found channels or not | [optional] 


