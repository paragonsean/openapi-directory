

# QueryMembersRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAtAfter** | **OffsetDateTime** |  |  [optional] |
|**createdAtAfterOrEqual** | **OffsetDateTime** |  |  [optional] |
|**createdAtBefore** | **OffsetDateTime** |  |  [optional] |
|**createdAtBeforeOrEqual** | **OffsetDateTime** |  |  [optional] |
|**filterConditions** | **Map&lt;String, Object&gt;** | Filter to apply to members |  |
|**id** | **String** | Channel ID to interact with |  [optional] |
|**limit** | **Integer** | Number of records to return |  [optional] |
|**members** | [**List&lt;ChannelMember&gt;**](ChannelMember.md) | List of members to search in distinct channels |  [optional] |
|**offset** | **Integer** | Number of records to offset |  [optional] |
|**sort** | [**List&lt;SortParam&gt;**](SortParam.md) | Array of sort parameters |  [optional] |
|**type** | **String** | Channel type to interact with |  |
|**user** | **UserObject** |  |  [optional] |
|**userId** | **String** |  |  [optional] |
|**userIdGt** | **String** |  |  [optional] |
|**userIdGte** | **String** |  |  [optional] |
|**userIdLt** | **String** |  |  [optional] |
|**userIdLte** | **String** |  |  [optional] |



