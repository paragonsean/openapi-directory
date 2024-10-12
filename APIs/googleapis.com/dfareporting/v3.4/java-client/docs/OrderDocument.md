

# OrderDocument

Contains properties of a Planning order document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account ID of this order document. |  [optional] |
|**advertiserId** | **String** | Advertiser ID of this order document. |  [optional] |
|**amendedOrderDocumentId** | **String** | The amended order document ID of this order document. An order document can be created by optionally amending another order document so that the change history can be preserved. |  [optional] |
|**approvedByUserProfileIds** | **List&lt;String&gt;** | IDs of users who have approved this order document. |  [optional] |
|**cancelled** | **Boolean** | Whether this order document is cancelled. |  [optional] |
|**createdInfo** | [**LastModifiedInfo**](LastModifiedInfo.md) |  |  [optional] |
|**effectiveDate** | **LocalDate** |  |  [optional] |
|**id** | **String** | ID of this order document. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#orderDocument\&quot;. |  [optional] |
|**lastSentRecipients** | **List&lt;String&gt;** | List of email addresses that received the last sent document. |  [optional] |
|**lastSentTime** | **OffsetDateTime** |  |  [optional] |
|**orderId** | **String** | ID of the order from which this order document is created. |  [optional] |
|**projectId** | **String** | Project ID of this order document. |  [optional] |
|**signed** | **Boolean** | Whether this order document has been signed. |  [optional] |
|**subaccountId** | **String** | Subaccount ID of this order document. |  [optional] |
|**title** | **String** | Title of this order document. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of this order document |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INSERTION_ORDER | &quot;PLANNING_ORDER_TYPE_INSERTION_ORDER&quot; |
| CHANGE_ORDER | &quot;PLANNING_ORDER_TYPE_CHANGE_ORDER&quot; |



