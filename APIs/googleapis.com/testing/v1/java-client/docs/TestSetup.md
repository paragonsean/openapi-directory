

# TestSetup

A description of how to set up the Android device prior to running the test.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | [**Account**](Account.md) |  |  [optional] |
|**additionalApks** | [**List&lt;Apk&gt;**](Apk.md) | APKs to install in addition to those being directly tested. These will be installed after the app under test. Currently capped at 100. |  [optional] |
|**directoriesToPull** | **List&lt;String&gt;** | List of directories on the device to upload to GCS at the end of the test; they must be absolute paths under /sdcard, /storage or /data/local/tmp. Path names are restricted to characters a-z A-Z 0-9 _ - . + and / Note: The paths /sdcard and /data will be made available and treated as implicit path substitutions. E.g. if /sdcard on a particular device does not map to external storage, the system will replace it with the external storage path prefix for that device. |  [optional] |
|**dontAutograntPermissions** | **Boolean** | Whether to prevent all runtime permissions to be granted at app install |  [optional] |
|**environmentVariables** | [**List&lt;EnvironmentVariable&gt;**](EnvironmentVariable.md) | Environment variables to set for the test (only applicable for instrumentation tests). |  [optional] |
|**filesToPush** | [**List&lt;DeviceFile&gt;**](DeviceFile.md) | List of files to push to the device before starting the test. |  [optional] |
|**initialSetupApks** | [**List&lt;Apk&gt;**](Apk.md) | Optional. Initial setup APKs to install before the app under test is installed. Currently capped at 100. |  [optional] |
|**networkProfile** | **String** | The network traffic profile used for running the test. Available network profiles can be queried by using the NETWORK_CONFIGURATION environment type when calling TestEnvironmentDiscoveryService.GetTestEnvironmentCatalog. |  [optional] |
|**systrace** | [**SystraceSetup**](SystraceSetup.md) |  |  [optional] |



