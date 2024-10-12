# DataBoxManagementClient.ValidationResponseProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**individualResponseDetails** | [**[ValidationInputResponse]**](ValidationInputResponse.md) | List of response details contain validationType and its response as key and value respectively. | [optional] [readonly] 
**status** | **String** | Overall validation status. | [optional] [readonly] 



## Enum: StatusEnum


* `AllValidToProceed` (value: `"AllValidToProceed"`)

* `InputsRevisitRequired` (value: `"InputsRevisitRequired"`)

* `CertainInputValidationsSkipped` (value: `"CertainInputValidationsSkipped"`)




