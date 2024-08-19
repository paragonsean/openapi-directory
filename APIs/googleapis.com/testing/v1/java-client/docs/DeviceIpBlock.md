

# DeviceIpBlock

A single device IP block

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addedDate** | [**Date**](Date.md) |  |  [optional] |
|**block** | **String** | An IP address block in CIDR notation eg: 34.68.194.64/29 |  [optional] |
|**form** | [**FormEnum**](#FormEnum) | Whether this block is used by physical or virtual devices |  [optional] |



## Enum: FormEnum

| Name | Value |
|---- | -----|
| DEVICE_FORM_UNSPECIFIED | &quot;DEVICE_FORM_UNSPECIFIED&quot; |
| VIRTUAL | &quot;VIRTUAL&quot; |
| PHYSICAL | &quot;PHYSICAL&quot; |
| EMULATOR | &quot;EMULATOR&quot; |



