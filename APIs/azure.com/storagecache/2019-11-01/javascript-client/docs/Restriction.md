# StorageCacheMgmtClient.Restriction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reasonCode** | **String** | The reason for the restriction. As of now this can be \&quot;QuotaId\&quot; or \&quot;NotAvailableForSubscription\&quot;. \&quot;QuotaId\&quot; is set when the SKU has requiredQuotas parameter as the subscription does not belong to that quota. \&quot;NotAvailableForSubscription\&quot; is related to capacity at the datacenter. | [optional] 
**type** | **String** | The type of restrictions. In this version, the only possible value for this is location. | [optional] [readonly] 
**values** | **[String]** | The value of restrictions. If the restriction type is set to location, then this would be the different locations where the SKU is restricted. | [optional] [readonly] 



## Enum: ReasonCodeEnum


* `QuotaId` (value: `"QuotaId"`)

* `NotAvailableForSubscription` (value: `"NotAvailableForSubscription"`)




