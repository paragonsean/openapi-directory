# StreamChatApi.QueryMembersRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAtAfter** | **Date** |  | [optional] 
**createdAtAfterOrEqual** | **Date** |  | [optional] 
**createdAtBefore** | **Date** |  | [optional] 
**createdAtBeforeOrEqual** | **Date** |  | [optional] 
**filterConditions** | **{String: Object}** | Filter to apply to members | 
**id** | **String** | Channel ID to interact with | [optional] 
**limit** | **Number** | Number of records to return | [optional] 
**members** | [**[ChannelMember]**](ChannelMember.md) | List of members to search in distinct channels | [optional] 
**offset** | **Number** | Number of records to offset | [optional] 
**sort** | [**[SortParam]**](SortParam.md) | Array of sort parameters | [optional] 
**type** | **String** | Channel type to interact with | 
**user** | [**UserObject**](UserObject.md) |  | [optional] 
**userId** | **String** |  | [optional] 
**userIdGt** | **String** |  | [optional] 
**userIdGte** | **String** |  | [optional] 
**userIdLt** | **String** |  | [optional] 
**userIdLte** | **String** |  | [optional] 


