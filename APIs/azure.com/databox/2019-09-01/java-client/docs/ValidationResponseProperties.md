

# ValidationResponseProperties

Properties of pre job creation validation response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**individualResponseDetails** | [**List&lt;ValidationInputResponse&gt;**](ValidationInputResponse.md) | List of response details contain validationType and its response as key and value respectively. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Overall validation status. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ALL_VALID_TO_PROCEED | &quot;AllValidToProceed&quot; |
| INPUTS_REVISIT_REQUIRED | &quot;InputsRevisitRequired&quot; |
| CERTAIN_INPUT_VALIDATIONS_SKIPPED | &quot;CertainInputValidationsSkipped&quot; |



