# GooglePlayEmmApi.Device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**androidId** | **String** | The Google Play Services Android ID for the device encoded as a lowercase hex string. For example, \&quot;123456789abcdef0\&quot;. | [optional] 
**device** | **String** | The internal hardware codename of the device. This comes from android.os.Build.DEVICE. (field named \&quot;device\&quot; per logs/wireless/android/android_checkin.proto) | [optional] 
**latestBuildFingerprint** | **String** | The build fingerprint of the device if known. | [optional] 
**maker** | **String** | The manufacturer of the device. This comes from android.os.Build.MANUFACTURER. | [optional] 
**managementType** | **String** | Identifies the extent to which the device is controlled by a managed Google Play EMM in various deployment configurations. Possible values include: - \&quot;managedDevice\&quot;, a device that has the EMM&#39;s device policy controller (DPC) as the device owner. - \&quot;managedProfile\&quot;, a device that has a profile managed by the DPC (DPC is profile owner) in addition to a separate, personal profile that is unavailable to the DPC. - \&quot;containerApp\&quot;, no longer used (deprecated). - \&quot;unmanagedProfile\&quot;, a device that has been allowed (by the domain&#39;s admin, using the Admin Console to enable the privilege) to use managed Google Play, but the profile is itself not owned by a DPC.  | [optional] 
**model** | **String** | The model name of the device. This comes from android.os.Build.MODEL. | [optional] 
**policy** | [**Policy**](Policy.md) |  | [optional] 
**product** | **String** | The product name of the device. This comes from android.os.Build.PRODUCT. | [optional] 
**report** | [**DeviceReport**](DeviceReport.md) |  | [optional] 
**retailBrand** | **String** | Retail brand for the device, if set. See android.os.Build.BRAND | [optional] 
**sdkVersion** | **Number** | API compatibility version. | [optional] 



## Enum: ManagementTypeEnum


* `managedDevice` (value: `"managedDevice"`)

* `managedProfile` (value: `"managedProfile"`)

* `containerApp` (value: `"containerApp"`)

* `unmanagedProfile` (value: `"unmanagedProfile"`)




