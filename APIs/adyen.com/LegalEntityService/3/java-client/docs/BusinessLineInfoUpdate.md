

# BusinessLineInfoUpdate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capability** | [**CapabilityEnum**](#CapabilityEnum) | The capability for which you are creating the business line. For example, **receivePayments**. |  [optional] |
|**industryCode** | **String** | A code that represents the industry of your legal entity. For example, **4431A** for computer software stores. |  [optional] |
|**legalEntityId** | **String** | Unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities__resParam_id) that owns the business line. |  [optional] |
|**salesChannels** | **List&lt;String&gt;** | A list of channels where goods or services are sold.  Possible values: **pos**, **posMoto**, **eCommerce**, **ecomMoto**, **payByLink**.  Required only in combination with the &#x60;service&#x60; **paymentProcessing**. |  [optional] |
|**service** | [**ServiceEnum**](#ServiceEnum) | The service for which you are creating the business line.    Possible values: *  **paymentProcessing** *  **banking**   |  [optional] |
|**sourceOfFunds** | [**SourceOfFunds**](SourceOfFunds.md) | Contains information about the source of your user&#39;s funds. Required only for the &#x60;service&#x60; **banking**. |  [optional] |
|**webData** | [**List&lt;WebData&gt;**](WebData.md) | List of website URLs where your user&#39;s goods or services are sold. When this is required for a service but your user does not have an online presence, provide the reason in the &#x60;webDataExemption&#x60; object. |  [optional] |
|**webDataExemption** | [**WebDataExemption**](WebDataExemption.md) | The reason why the web data is not provided. |  [optional] |



## Enum: CapabilityEnum

| Name | Value |
|---- | -----|
| RECEIVE_PAYMENTS | &quot;receivePayments&quot; |
| RECEIVE_FROM_PLATFORM_PAYMENTS | &quot;receiveFromPlatformPayments&quot; |
| ISSUE_BANK_ACCOUNT | &quot;issueBankAccount&quot; |



## Enum: ServiceEnum

| Name | Value |
|---- | -----|
| PAYMENT_PROCESSING | &quot;paymentProcessing&quot; |
| BANKING | &quot;banking&quot; |



