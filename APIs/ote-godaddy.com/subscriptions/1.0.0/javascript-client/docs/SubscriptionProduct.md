# OpenapiJsClient.SubscriptionProduct

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **String** | A human readable description of the Product that is subscribed | 
**namespace** | **String** | Grouping of related Subscriptions | 
**pfid** | **Number** | Unique identifier of the Product that is subscribed | 
**productGroupKey** | **String** | Primary key of a grouping of related Subscriptions | 
**renewalPeriod** | **Number** | The number of &#x60;renewalPeriodUnits&#x60; that will be added by the &#x60;renewalPfid&#x60; | 
**renewalPeriodUnit** | **String** | The unit of time that &#x60;renewalPeriod&#x60; is measured in | 
**renewalPfid** | **Number** | Unique identifier of the renewal Product | 
**supportBillOn** | **Boolean** | Whether the product supports the &#x60;billOn&#x60; option on the renewal endpoint | 



## Enum: RenewalPeriodUnitEnum


* `MONTH` (value: `"MONTH"`)

* `QUARTER` (value: `"QUARTER"`)

* `SEMI_ANNUAL` (value: `"SEMI_ANNUAL"`)

* `YEAR` (value: `"YEAR"`)




