

# ProfileProperties

The JSON object that contains the properties required to create a profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | **String** | Provisioning status of the profile. |  [optional] [readonly] |
|**resourceState** | [**ResourceStateEnum**](#ResourceStateEnum) | Resource status of the profile. |  [optional] [readonly] |



## Enum: ResourceStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| ACTIVE | &quot;Active&quot; |
| DELETING | &quot;Deleting&quot; |
| DISABLED | &quot;Disabled&quot; |



