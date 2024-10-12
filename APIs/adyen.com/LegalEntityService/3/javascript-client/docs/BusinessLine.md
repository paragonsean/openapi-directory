# LegalEntityManagementApi.BusinessLine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capability** | **String** | The capability for which you are creating the business line.  Possible values: **receivePayments**, **receiveFromPlatformPayments**, **issueBankAccount** | [optional] 
**id** | **String** | The unique identifier of the business line. | [readonly] 
**industryCode** | **String** | A code that represents the [industry of the legal entity](https://docs.adyen.com/marketplaces-and-platforms/verification-requirements/reference-additional-products/#list-industry-codes). For example, **4431A** for computer software stores. | 
**legalEntityId** | **String** | Unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities__resParam_id) that owns the business line. | 
**problems** | [**[CapabilityProblem]**](CapabilityProblem.md) | The verification errors related to capabilities for this supporting entity. | [optional] 
**salesChannels** | **[String]** | A list of channels where goods or services are sold.  Possible values: **pos**, **posMoto**, **eCommerce**, **ecomMoto**, **payByLink**.  Required only in combination with the &#x60;service&#x60; **paymentProcessing**. | [optional] 
**service** | **String** | The service for which you are creating the business line.    Possible values: *  **paymentProcessing** *  **banking**   | 
**sourceOfFunds** | [**SourceOfFunds**](SourceOfFunds.md) | Contains information about the source of your user&#39;s funds. Required only for the &#x60;service&#x60; **banking**. | [optional] 
**webData** | [**[WebData]**](WebData.md) | List of website URLs where your user&#39;s goods or services are sold. When this is required for a service but your user does not have an online presence, provide the reason in the &#x60;webDataExemption&#x60; object. | [optional] 
**webDataExemption** | [**WebDataExemption**](WebDataExemption.md) | The reason why the web data is not provided. | [optional] 



## Enum: CapabilityEnum


* `receivePayments` (value: `"receivePayments"`)

* `receiveFromPlatformPayments` (value: `"receiveFromPlatformPayments"`)

* `issueBankAccount` (value: `"issueBankAccount"`)





## Enum: ServiceEnum


* `paymentProcessing` (value: `"paymentProcessing"`)

* `banking` (value: `"banking"`)




