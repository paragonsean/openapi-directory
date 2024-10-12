# DisplayVideo360Api.ExitEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the click tag of the exit event. The name must be unique within one creative. Leave it empty or unset for creatives containing image assets only. | [optional] 
**reportingName** | **String** | The name used to identify this event in reports. Leave it empty or unset for creatives containing image assets only. | [optional] 
**type** | **String** | Required. The type of the exit event. | [optional] 
**url** | **String** | Required. The click through URL of the exit event. This is required when type is: * &#x60;EXIT_EVENT_TYPE_DEFAULT&#x60; * &#x60;EXIT_EVENT_TYPE_BACKUP&#x60; | [optional] 



## Enum: TypeEnum


* `UNSPECIFIED` (value: `"EXIT_EVENT_TYPE_UNSPECIFIED"`)

* `DEFAULT` (value: `"EXIT_EVENT_TYPE_DEFAULT"`)

* `BACKUP` (value: `"EXIT_EVENT_TYPE_BACKUP"`)




