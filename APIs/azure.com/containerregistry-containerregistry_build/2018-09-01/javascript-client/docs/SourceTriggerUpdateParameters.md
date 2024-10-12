# ContainerRegistryManagementClient.SourceTriggerUpdateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the trigger. | 
**sourceRepository** | [**SourceUpdateParameters**](SourceUpdateParameters.md) |  | [optional] 
**sourceTriggerEvents** | **[String]** | The source event corresponding to the trigger. | [optional] 
**status** | **String** | The current status of trigger. | [optional] [default to &#39;Enabled&#39;]



## Enum: [SourceTriggerEventsEnum]


* `commit` (value: `"commit"`)

* `pullrequest` (value: `"pullrequest"`)





## Enum: StatusEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)




