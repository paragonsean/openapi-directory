

# GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**model** | **String** | The power supply unit model. |  [optional] |
|**number** | [**NumberEnum**](#NumberEnum) | Which slot the AC power supply occupies. Possible values are: 0, 1, 2. |  [optional] |
|**serial** | **String** | The power supply unit serial number. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the power supply unit. Possible values are: connected, not connected, powering. |  [optional] |



## Enum: NumberEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CONNECTED | &quot;connected&quot; |
| NOT_CONNECTED | &quot;not connected&quot; |
| POWERING | &quot;powering&quot; |



