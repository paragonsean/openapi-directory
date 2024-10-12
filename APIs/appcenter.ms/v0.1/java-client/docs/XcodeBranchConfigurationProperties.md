

# XcodeBranchConfigurationProperties

Build configuration when Xcode is part of the build steps

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appExtensionProvisioningProfileFiles** | [**List&lt;BranchConfigurationsGet200ResponseAllOfToolsetsXcodeAppExtensionProvisioningProfileFilesInner&gt;**](BranchConfigurationsGet200ResponseAllOfToolsetsXcodeAppExtensionProvisioningProfileFilesInner.md) |  |  [optional] |
|**archiveConfiguration** | **String** | The build configuration of the target to archive |  [optional] |
|**automaticSigning** | **Boolean** |  |  [optional] |
|**cartfilePath** | **String** | Path to Carthage file, if present |  [optional] |
|**certificateEncoded** | **String** |  |  [optional] |
|**certificateFileId** | **String** |  |  [optional] |
|**certificateFilename** | **String** |  |  [optional] |
|**certificatePassword** | **String** |  |  [optional] |
|**certificateUploadId** | **String** |  |  [optional] |
|**forceLegacyBuildSystem** | **Boolean** | Setting this to true forces the build to use Xcode legacy build system. Otherwise, the setting from workspace settings is used. By default new build system is used if workspace setting is not committed to the repository. Only used for iOS React Native app, with Xcode 10.  |  [optional] |
|**podfilePath** | **String** | Path to CococaPods file, if present |  [optional] |
|**projectOrWorkspacePath** | **String** | Xcode project/workspace path |  [optional] |
|**provisioningProfileEncoded** | **String** |  |  [optional] |
|**provisioningProfileFileId** | **String** |  |  [optional] |
|**provisioningProfileFilename** | **String** |  |  [optional] |
|**provisioningProfileUploadId** | **String** |  |  [optional] |
|**scheme** | **String** |  |  [optional] |
|**targetToArchive** | **String** | The target id of the selected scheme to archive |  [optional] |
|**teamId** | **String** |  |  [optional] |
|**xcodeProjectSha** | **String** | The selected pbxproject hash to the repositroy |  [optional] |
|**xcodeVersion** | **String** | Xcode version used to build. Available versions can be found in \&quot;/xcode_versions\&quot; API. Default is latest stable version, at the time when the configuration is set. |  [optional] |



