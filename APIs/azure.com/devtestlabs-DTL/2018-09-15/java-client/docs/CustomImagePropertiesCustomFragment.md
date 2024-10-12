

# CustomImagePropertiesCustomFragment

Properties for creating a custom image from a VHD.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**imageName** | **String** | The image name. |  [optional] |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | The OS type of the custom image (i.e. Windows, Linux) |  [optional] |
|**sysPrep** | **Boolean** | Indicates whether sysprep has been run on the VHD. |  [optional] |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |
| NONE | &quot;None&quot; |



