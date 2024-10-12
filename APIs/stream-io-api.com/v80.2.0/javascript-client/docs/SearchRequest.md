# StreamChatApi.SearchRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filterConditions** | **{String: Object}** | Channel filter conditions | 
**limit** | **Number** | Number of messages to return | [optional] 
**messageFilterConditions** | **{String: Object}** | Message filter conditions | [optional] 
**next** | **String** | Pagination parameter. Cannot be used with non-zero offset. | [optional] 
**offset** | **Number** | Pagination offset. Cannot be used with sort or next. | [optional] 
**query** | **String** | Search phrase | [optional] 
**sort** | [**[SortParam]**](SortParam.md) | Sort parameters. Cannot be used with non-zero offset | [optional] 


