

# BranchConfigurationsGet200ResponseAllOfToolsetsXamarin

Build configuration for Xamarin projects

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**args** | **String** |  |  [optional] |
|**_configuration** | **String** |  |  [optional] |
|**isSimBuild** | **Boolean** |  |  [optional] |
|**monoVersion** | **String** |  |  [optional] |
|**p12File** | **String** |  |  [optional] |
|**p12Pwd** | **String** |  |  [optional] |
|**provProfile** | **String** |  |  [optional] |
|**sdkBundle** | **String** |  |  [optional] |
|**slnPath** | **String** |  |  [optional] |
|**symlink** | **String** | Symlink of the SDK Bundle and Mono installation. The build will use the associated Mono bundled with related Xamarin SDK. If both symlink and monoVersion or sdkBundle are passed, the symlink is taking precedence. If non-existing symlink is passed, the current stable Mono version will be configured for building.  |  [optional] |



