

# Key

Automation key which is used to register a DSC Node

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyName** | [**KeyNameEnum**](#KeyNameEnum) | Automation key name. |  [optional] [readonly] |
|**permissions** | [**PermissionsEnum**](#PermissionsEnum) | Automation key permissions. |  [optional] [readonly] |
|**value** | **String** | Value of the Automation Key used for registration. |  [optional] [readonly] |



## Enum: KeyNameEnum

| Name | Value |
|---- | -----|
| PRIMARY | &quot;Primary&quot; |
| SECONDARY | &quot;Secondary&quot; |



## Enum: PermissionsEnum

| Name | Value |
|---- | -----|
| READ | &quot;Read&quot; |
| FULL | &quot;Full&quot; |



