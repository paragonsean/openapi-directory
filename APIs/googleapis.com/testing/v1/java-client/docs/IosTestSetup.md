

# IosTestSetup

A description of how to set up an iOS device prior to running the test.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalIpas** | [**List&lt;FileReference&gt;**](FileReference.md) | iOS apps to install in addition to those being directly tested. |  [optional] |
|**networkProfile** | **String** | The network traffic profile used for running the test. Available network profiles can be queried by using the NETWORK_CONFIGURATION environment type when calling TestEnvironmentDiscoveryService.GetTestEnvironmentCatalog. |  [optional] |
|**pullDirectories** | [**List&lt;IosDeviceFile&gt;**](IosDeviceFile.md) | List of directories on the device to upload to Cloud Storage at the end of the test. Directories should either be in a shared directory (such as /private/var/mobile/Media) or within an accessible directory inside the app&#39;s filesystem (such as /Documents) by specifying the bundle ID. |  [optional] |
|**pushFiles** | [**List&lt;IosDeviceFile&gt;**](IosDeviceFile.md) | List of files to push to the device before starting the test. |  [optional] |



