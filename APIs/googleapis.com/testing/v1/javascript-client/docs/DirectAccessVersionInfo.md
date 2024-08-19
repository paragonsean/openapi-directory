# CloudTestingApi.DirectAccessVersionInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directAccessSupported** | **Boolean** | Whether direct access is supported at all. Clients are expected to filter down the device list to only android models and versions which support Direct Access when that is the user intent. | [optional] 
**minimumAndroidStudioVersion** | **String** | Output only. Indicates client-device compatibility, where a device is known to work only with certain workarounds implemented in the Android Studio client. Expected format \&quot;major.minor.micro.patch\&quot;, e.g. \&quot;5921.22.2211.8881706\&quot;. | [optional] 


