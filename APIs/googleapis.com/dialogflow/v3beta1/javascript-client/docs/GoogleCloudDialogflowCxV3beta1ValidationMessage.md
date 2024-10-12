# DialogflowApi.GoogleCloudDialogflowCxV3beta1ValidationMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **String** | The message detail. | [optional] 
**resourceNames** | [**[GoogleCloudDialogflowCxV3beta1ResourceName]**](GoogleCloudDialogflowCxV3beta1ResourceName.md) | The resource names of the resources where the message is found. | [optional] 
**resourceType** | **String** | The type of the resources where the message is found. | [optional] 
**resources** | **[String]** | The names of the resources where the message is found. | [optional] 
**severity** | **String** | Indicates the severity of the message. | [optional] 



## Enum: ResourceTypeEnum


* `RESOURCE_TYPE_UNSPECIFIED` (value: `"RESOURCE_TYPE_UNSPECIFIED"`)

* `AGENT` (value: `"AGENT"`)

* `INTENT` (value: `"INTENT"`)

* `INTENT_TRAINING_PHRASE` (value: `"INTENT_TRAINING_PHRASE"`)

* `INTENT_PARAMETER` (value: `"INTENT_PARAMETER"`)

* `INTENTS` (value: `"INTENTS"`)

* `INTENT_TRAINING_PHRASES` (value: `"INTENT_TRAINING_PHRASES"`)

* `ENTITY_TYPE` (value: `"ENTITY_TYPE"`)

* `ENTITY_TYPES` (value: `"ENTITY_TYPES"`)

* `WEBHOOK` (value: `"WEBHOOK"`)

* `FLOW` (value: `"FLOW"`)

* `PAGE` (value: `"PAGE"`)

* `PAGES` (value: `"PAGES"`)

* `TRANSITION_ROUTE_GROUP` (value: `"TRANSITION_ROUTE_GROUP"`)

* `AGENT_TRANSITION_ROUTE_GROUP` (value: `"AGENT_TRANSITION_ROUTE_GROUP"`)





## Enum: SeverityEnum


* `SEVERITY_UNSPECIFIED` (value: `"SEVERITY_UNSPECIFIED"`)

* `INFO` (value: `"INFO"`)

* `WARNING` (value: `"WARNING"`)

* `ERROR` (value: `"ERROR"`)




