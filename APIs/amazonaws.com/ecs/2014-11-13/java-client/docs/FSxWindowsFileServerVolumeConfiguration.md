

# FSxWindowsFileServerVolumeConfiguration

<p>This parameter is specified when you're using <a href=\"https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html\">Amazon FSx for Windows File Server</a> file system for task storage.</p> <p>For more information and the input format, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/wfsx-volumes.html\">Amazon FSx for Windows File Server volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileSystemId** | [**String**](String.md) |  |  |
|**rootDirectory** | [**String**](String.md) |  |  |
|**authorizationConfig** | [**FSxWindowsFileServerVolumeConfigurationAuthorizationConfig**](FSxWindowsFileServerVolumeConfigurationAuthorizationConfig.md) |  |  |



