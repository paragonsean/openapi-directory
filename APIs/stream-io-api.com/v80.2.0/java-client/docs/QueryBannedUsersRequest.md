

# QueryBannedUsersRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAtAfter** | **OffsetDateTime** |  |  [optional] |
|**createdAtAfterOrEqual** | **OffsetDateTime** |  |  [optional] |
|**createdAtBefore** | **OffsetDateTime** |  |  [optional] |
|**createdAtBeforeOrEqual** | **OffsetDateTime** |  |  [optional] |
|**filterConditions** | **Map&lt;String, Object&gt;** |  |  |
|**limit** | **Integer** |  |  [optional] |
|**offset** | **Integer** |  |  [optional] |
|**sort** | [**List&lt;SortParam&gt;**](SortParam.md) |  |  [optional] |
|**user** | **UserObject** |  |  [optional] |
|**userId** | **String** | **Server-side only**. User ID which server acts upon |  [optional] |



