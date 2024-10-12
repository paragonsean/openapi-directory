

# Criticality

Criticality of the Application, Service, or Workload

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**level** | **String** | Optional. Criticality level. Can contain only lowercase letters, numeric characters, underscores, and dashes. Can have a maximum length of 63 characters. |  [optional] |
|**missionCritical** | **Boolean** | Optional. Indicates mission-critical Application, Service, or Workload. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. Criticality Type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| MISSION_CRITICAL | &quot;MISSION_CRITICAL&quot; |
| HIGH | &quot;HIGH&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| LOW | &quot;LOW&quot; |



