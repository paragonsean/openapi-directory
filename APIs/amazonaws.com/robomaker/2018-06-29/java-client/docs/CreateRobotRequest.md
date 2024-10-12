

# CreateRobotRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name for the robot. |  |
|**architecture** | [**ArchitectureEnum**](#ArchitectureEnum) | The target architecture of the robot. |  |
|**greengrassGroupId** | **String** | The Greengrass group id. |  |
|**tags** | **Map&lt;String, String&gt;** | A map that contains tag keys and tag values that are attached to the robot. |  [optional] |



## Enum: ArchitectureEnum

| Name | Value |
|---- | -----|
| X86_64 | &quot;X86_64&quot; |
| ARM64 | &quot;ARM64&quot; |
| ARMHF | &quot;ARMHF&quot; |



