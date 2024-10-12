# DialogflowApi.GoogleCloudDialogflowV2beta1ValidationError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | **[String]** | The names of the entries that the error is associated with. Format: - &#x60;projects//agent&#x60;, if the error is associated with the entire agent. - &#x60;projects//agent/intents/&#x60;, if the error is associated with certain intents. - &#x60;projects//agent/intents//trainingPhrases/&#x60;, if the error is associated with certain intent training phrases. - &#x60;projects//agent/intents//parameters/&#x60;, if the error is associated with certain intent parameters. - &#x60;projects//agent/entities/&#x60;, if the error is associated with certain entities. | [optional] 
**errorMessage** | **String** | The detailed error message. | [optional] 
**severity** | **String** | The severity of the error. | [optional] 



## Enum: SeverityEnum


* `SEVERITY_UNSPECIFIED` (value: `"SEVERITY_UNSPECIFIED"`)

* `INFO` (value: `"INFO"`)

* `WARNING` (value: `"WARNING"`)

* `ERROR` (value: `"ERROR"`)

* `CRITICAL` (value: `"CRITICAL"`)




