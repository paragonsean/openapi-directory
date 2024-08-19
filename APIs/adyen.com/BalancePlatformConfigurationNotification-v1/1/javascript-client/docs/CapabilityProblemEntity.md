# ConfigurationWebhooks.CapabilityProblemEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | **[String]** | List of document IDs to which the verification errors related to the capabilities correspond to. | [optional] 
**id** | **String** | The ID of the entity. | [optional] 
**owner** | [**CapabilityProblemEntityRecursive**](CapabilityProblemEntityRecursive.md) | Contains details about the owner of the entity that has an error. | [optional] 
**type** | **String** | Type of entity.   Possible values: **LegalEntity**, **BankAccount**, **Document**. | [optional] 



## Enum: TypeEnum


* `BankAccount` (value: `"BankAccount"`)

* `Document` (value: `"Document"`)

* `LegalEntity` (value: `"LegalEntity"`)




