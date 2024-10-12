# LegalEntityManagementApi.TransferInstrument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bankAccount** | [**BankAccountInfo**](BankAccountInfo.md) | Contains information about the legal entity&#39;s bank account. | 
**documents** | [**[EntityReference]**](EntityReference.md) | List of documents uploaded for the transfer instrument. | [optional] 
**id** | **String** | The unique identifier of the transfer instrument. | [readonly] 
**legalEntityId** | **String** | The unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id) that owns the transfer instrument. | 
**type** | **String** | The type of transfer instrument.  Possible value: **bankAccount**. | 



## Enum: TypeEnum


* `bankAccount` (value: `"bankAccount"`)

* `recurringDetail` (value: `"recurringDetail"`)




