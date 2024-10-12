# LegalEntityManagementApi.SourceOfFunds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquiringBusinessLineId** | **String** | The unique identifier of the business line that will be the source of funds.This must be a business line for a **receivePayments** or **receiveFromPlatformPayments** capability. | [optional] 
**adyenProcessedFunds** | **Boolean** | Indicates whether the funds are coming from transactions processed by Adyen. If **false**, a &#x60;description&#x60; is required. | [optional] 
**description** | **String** | Text describing the source of funds. For example, for &#x60;type&#x60; **business**, provide a description of where the business transactions come from, such as payments through bank transfer. Required when &#x60;adyenProcessedFunds&#x60; is **false**. | [optional] 
**type** | **String** | The type of the source of funds. Possible value: **business**. | [optional] 



## Enum: TypeEnum


* `business` (value: `"business"`)




