

# GoogleCloudDialogflowV2beta1ValidationError

Represents a single validation error.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entries** | **List&lt;String&gt;** | The names of the entries that the error is associated with. Format: - &#x60;projects//agent&#x60;, if the error is associated with the entire agent. - &#x60;projects//agent/intents/&#x60;, if the error is associated with certain intents. - &#x60;projects//agent/intents//trainingPhrases/&#x60;, if the error is associated with certain intent training phrases. - &#x60;projects//agent/intents//parameters/&#x60;, if the error is associated with certain intent parameters. - &#x60;projects//agent/entities/&#x60;, if the error is associated with certain entities. |  [optional] |
|**errorMessage** | **String** | The detailed error message. |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | The severity of the error. |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| SEVERITY_UNSPECIFIED | &quot;SEVERITY_UNSPECIFIED&quot; |
| INFO | &quot;INFO&quot; |
| WARNING | &quot;WARNING&quot; |
| ERROR | &quot;ERROR&quot; |
| CRITICAL | &quot;CRITICAL&quot; |



