# AppCenterClient.BillingPlan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **{String: Object}** | Collection of attribute values. | [optional] 
**id** | **String** | The Billing Plan ID | [optional] 
**limits** | **{String: Number}** | A collection of named numeric values | [optional] 
**parentId** | **String** |  | [optional] 
**paymentSource** | **String** | Service that receives payments for this billing plan. | [optional] 
**price** | **Number** | Price of the Billing Plan | [optional] 
**service** | **String** | Name of the service that the plan applies to. | [optional] 
**version** | **String** | Version of the Billing Plan schema | [optional] 



## Enum: PaymentSourceEnum


* `None` (value: `"None"`)

* `AppCenter` (value: `"AppCenter"`)

* `GitHub` (value: `"GitHub"`)

* `Xtc` (value: `"Xtc"`)





## Enum: ServiceEnum


* `Build` (value: `"Build"`)

* `Test` (value: `"Test"`)




