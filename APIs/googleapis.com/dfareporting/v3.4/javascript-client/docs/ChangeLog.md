# CampaignManager360Api.ChangeLog

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Account ID of the modified object. | [optional] 
**action** | **String** | Action which caused the change. | [optional] 
**changeTime** | **Date** |  | [optional] 
**fieldName** | **String** | Field name of the object which changed. | [optional] 
**id** | **String** | ID of this change log. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#changeLog\&quot;. | [optional] 
**newValue** | **String** | New value of the object field. | [optional] 
**objectId** | **String** | ID of the object of this change log. The object could be a campaign, placement, ad, or other type. | [optional] 
**objectType** | **String** | Object type of the change log. | [optional] 
**oldValue** | **String** | Old value of the object field. | [optional] 
**subaccountId** | **String** | Subaccount ID of the modified object. | [optional] 
**transactionId** | **String** | Transaction ID of this change log. When a single API call results in many changes, each change will have a separate ID in the change log but will share the same transactionId. | [optional] 
**userProfileId** | **String** | ID of the user who modified the object. | [optional] 
**userProfileName** | **String** | User profile name of the user who modified the object. | [optional] 


