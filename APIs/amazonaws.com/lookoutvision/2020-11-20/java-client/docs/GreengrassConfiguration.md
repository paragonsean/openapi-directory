

# GreengrassConfiguration

<p>Configuration information for the AWS IoT Greengrass component created in a model packaging job. For more information, see <a>StartModelPackagingJob</a>. </p> <note> <p>You can't specify a component with the same <code>ComponentName</code> and <code>Componentversion</code> as an existing component with the same component name and component version.</p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**compilerOptions** | [**String**](String.md) |  |  [optional] |
|**targetDevice** | [**TargetDevice**](TargetDevice.md) |  |  [optional] |
|**targetPlatform** | [**GreengrassConfigurationTargetPlatform**](GreengrassConfigurationTargetPlatform.md) |  |  [optional] |
|**s3OutputLocation** | [**GreengrassConfigurationS3OutputLocation**](GreengrassConfigurationS3OutputLocation.md) |  |  |
|**componentName** | [**String**](String.md) |  |  |
|**componentVersion** | [**String**](String.md) |  |  [optional] |
|**componentDescription** | [**String**](String.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |



