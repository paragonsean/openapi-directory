

# AppBlock

<p>Describes an app block.</p> <p>App blocks are an Amazon AppStream 2.0 resource that stores the details about the virtual hard disk in an S3 bucket. It also stores the setup script with details about how to mount the virtual hard disk. The virtual hard disk includes the application binaries and other files necessary to launch your applications. Multiple applications can be assigned to a single app block.</p> <p>This is only supported for Elastic fleets.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  |
|**arn** | [**String**](String.md) |  |  |
|**description** | [**String**](String.md) |  |  [optional] |
|**displayName** | [**String**](String.md) |  |  [optional] |
|**sourceS3Location** | [**CreateAppBlockRequestSourceS3Location**](CreateAppBlockRequestSourceS3Location.md) |  |  [optional] |
|**setupScriptDetails** | [**AppBlockSetupScriptDetails**](AppBlockSetupScriptDetails.md) |  |  [optional] |
|**createdTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**postSetupScriptDetails** | [**AppBlockPostSetupScriptDetails**](AppBlockPostSetupScriptDetails.md) |  |  [optional] |
|**packagingType** | [**PackagingType**](PackagingType.md) |  |  [optional] |
|**state** | [**AppBlockState**](AppBlockState.md) |  |  [optional] |
|**appBlockErrors** | [**List**](List.md) |  |  [optional] |



