

# CustomImageProperties

Properties of a custom image.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**author** | **String** | The author of the custom image. |  [optional] |
|**creationDate** | **OffsetDateTime** | The creation date of the custom image. |  [optional] |
|**description** | **String** | The description of the custom image. |  [optional] |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | The OS type of the custom image. |  [optional] |
|**provisioningState** | **String** | The provisioning status of the resource. |  [optional] |
|**vhd** | [**CustomImagePropertiesCustom**](CustomImagePropertiesCustom.md) |  |  [optional] |
|**vm** | [**CustomImagePropertiesFromVm**](CustomImagePropertiesFromVm.md) |  |  [optional] |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |
| NONE | &quot;None&quot; |



