

# ServersIdActionsEnableRescuePostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sshKeys** | **List&lt;Integer&gt;** | Array of SSH key IDs which should be injected into the rescue system. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of rescue system to boot (default: &#x60;linux64&#x60;) |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| LINUX64 | &quot;linux64&quot; |
| LINUX32 | &quot;linux32&quot; |



