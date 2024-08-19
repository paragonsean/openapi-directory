

# UserSettings

<p>A collection of settings that apply to users of Amazon SageMaker Studio. These settings are specified when the <code>CreateUserProfile</code> API is called, and as <code>DefaultUserSettings</code> when the <code>CreateDomain</code> API is called.</p> <p> <code>SecurityGroups</code> is aggregated when specified in both calls. For all other settings in <code>UserSettings</code>, the values specified in <code>CreateUserProfile</code> take precedence over those specified in <code>CreateDomain</code>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**executionRole** | [**String**](String.md) |  |  [optional] |
|**securityGroups** | [**List**](List.md) |  |  [optional] |
|**sharingSettings** | [**UserSettingsSharingSettings**](UserSettingsSharingSettings.md) |  |  [optional] |
|**jupyterServerAppSettings** | [**UserSettingsJupyterServerAppSettings**](UserSettingsJupyterServerAppSettings.md) |  |  [optional] |
|**kernelGatewayAppSettings** | [**UserSettingsKernelGatewayAppSettings**](UserSettingsKernelGatewayAppSettings.md) |  |  [optional] |
|**tensorBoardAppSettings** | [**UserSettingsTensorBoardAppSettings**](UserSettingsTensorBoardAppSettings.md) |  |  [optional] |
|**rstudioServerProAppSettings** | [**UserSettingsRStudioServerProAppSettings**](UserSettingsRStudioServerProAppSettings.md) |  |  [optional] |
|**rsessionAppSettings** | [**UserSettingsRSessionAppSettings**](UserSettingsRSessionAppSettings.md) |  |  [optional] |
|**canvasAppSettings** | [**UserSettingsCanvasAppSettings**](UserSettingsCanvasAppSettings.md) |  |  [optional] |



