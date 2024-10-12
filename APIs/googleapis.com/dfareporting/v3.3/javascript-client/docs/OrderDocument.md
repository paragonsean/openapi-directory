# CampaignManager360Api.OrderDocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Account ID of this order document. | [optional] 
**advertiserId** | **String** | Advertiser ID of this order document. | [optional] 
**amendedOrderDocumentId** | **String** | The amended order document ID of this order document. An order document can be created by optionally amending another order document so that the change history can be preserved. | [optional] 
**approvedByUserProfileIds** | **[String]** | IDs of users who have approved this order document. | [optional] 
**cancelled** | **Boolean** | Whether this order document is cancelled. | [optional] 
**createdInfo** | [**LastModifiedInfo**](LastModifiedInfo.md) |  | [optional] 
**effectiveDate** | **Date** |  | [optional] 
**id** | **String** | ID of this order document. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#orderDocument\&quot;. | [optional] 
**lastSentRecipients** | **[String]** | List of email addresses that received the last sent document. | [optional] 
**lastSentTime** | **Date** |  | [optional] 
**orderId** | **String** | ID of the order from which this order document is created. | [optional] 
**projectId** | **String** | Project ID of this order document. | [optional] 
**signed** | **Boolean** | Whether this order document has been signed. | [optional] 
**subaccountId** | **String** | Subaccount ID of this order document. | [optional] 
**title** | **String** | Title of this order document. | [optional] 
**type** | **String** | Type of this order document | [optional] 



## Enum: TypeEnum


* `INSERTION_ORDER` (value: `"PLANNING_ORDER_TYPE_INSERTION_ORDER"`)

* `CHANGE_ORDER` (value: `"PLANNING_ORDER_TYPE_CHANGE_ORDER"`)




