

# ResourceStatus

Message describing resource status

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**rulesNewerVersions** | **List&lt;String&gt;** | Historical: Used before 2023-05-22 the new version of rule id if exists |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the resource |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETING | &quot;DELETING&quot; |



