

# CapabilitySetting


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedInstances** | [**AllowedInstancesEnum**](#AllowedInstancesEnum) |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**enabledByDefault** | **Boolean** |  |  [optional] |
|**key** | [**KeyEnum**](#KeyEnum) |  |  [optional] |
|**minInstances** | **Integer** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**options** | [**List&lt;CapabilityOption&gt;**](CapabilityOption.md) |  |  [optional] |
|**visible** | **Boolean** |  |  [optional] |



## Enum: AllowedInstancesEnum

| Name | Value |
|---- | -----|
| ENTRY | &quot;ENTRY&quot; |
| SINGLE | &quot;SINGLE&quot; |
| MULTIPLE | &quot;MULTIPLE&quot; |



## Enum: KeyEnum

| Name | Value |
|---- | -----|
| ICLOUD_VERSION | &quot;ICLOUD_VERSION&quot; |
| DATA_PROTECTION_PERMISSION_LEVEL | &quot;DATA_PROTECTION_PERMISSION_LEVEL&quot; |
| APPLE_ID_AUTH_APP_CONSENT | &quot;APPLE_ID_AUTH_APP_CONSENT&quot; |



