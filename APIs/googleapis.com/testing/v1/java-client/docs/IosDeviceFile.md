

# IosDeviceFile

A file or directory to install on the device before the test starts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bundleId** | **String** | The bundle id of the app where this file lives. iOS apps sandbox their own filesystem, so app files must specify which app installed on the device. |  [optional] |
|**content** | [**FileReference**](FileReference.md) |  |  [optional] |
|**devicePath** | **String** | Location of the file on the device, inside the app&#39;s sandboxed filesystem |  [optional] |



