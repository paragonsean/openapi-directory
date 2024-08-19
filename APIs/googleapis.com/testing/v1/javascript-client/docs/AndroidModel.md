# CloudTestingApi.AndroidModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand** | **String** | The company that this device is branded with. Example: \&quot;Google\&quot;, \&quot;Samsung\&quot;. | [optional] 
**codename** | **String** | The name of the industrial design. This corresponds to android.os.Build.DEVICE. | [optional] 
**form** | **String** | Whether this device is virtual or physical. | [optional] 
**formFactor** | **String** | Whether this device is a phone, tablet, wearable, etc. | [optional] 
**id** | **String** | The unique opaque id for this model. Use this for invoking the TestExecutionService. | [optional] 
**lowFpsVideoRecording** | **Boolean** | True if and only if tests with this model are recorded by stitching together screenshots. See use_low_spec_video_recording in device config. | [optional] 
**manufacturer** | **String** | The manufacturer of this device. | [optional] 
**name** | **String** | The human-readable marketing name for this device model. Examples: \&quot;Nexus 5\&quot;, \&quot;Galaxy S5\&quot;. | [optional] 
**perVersionInfo** | [**[PerAndroidVersionInfo]**](PerAndroidVersionInfo.md) | Version-specific information of an Android model. | [optional] 
**screenDensity** | **Number** | Screen density in DPI. This corresponds to ro.sf.lcd_density | [optional] 
**screenX** | **Number** | Screen size in the horizontal (X) dimension measured in pixels. | [optional] 
**screenY** | **Number** | Screen size in the vertical (Y) dimension measured in pixels. | [optional] 
**supportedAbis** | **[String]** | The list of supported ABIs for this device. This corresponds to either android.os.Build.SUPPORTED_ABIS (for API level 21 and above) or android.os.Build.CPU_ABI/CPU_ABI2. The most preferred ABI is the first element in the list. Elements are optionally prefixed by \&quot;version_id:\&quot; (where version_id is the id of an AndroidVersion), denoting an ABI that is supported only on a particular version. | [optional] 
**supportedVersionIds** | **[String]** | The set of Android versions this device supports. | [optional] 
**tags** | **[String]** | Tags for this dimension. Examples: \&quot;default\&quot;, \&quot;preview\&quot;, \&quot;deprecated\&quot;. | [optional] 
**thumbnailUrl** | **String** | URL of a thumbnail image (photo) of the device. | [optional] 



## Enum: FormEnum


* `DEVICE_FORM_UNSPECIFIED` (value: `"DEVICE_FORM_UNSPECIFIED"`)

* `VIRTUAL` (value: `"VIRTUAL"`)

* `PHYSICAL` (value: `"PHYSICAL"`)

* `EMULATOR` (value: `"EMULATOR"`)





## Enum: FormFactorEnum


* `DEVICE_FORM_FACTOR_UNSPECIFIED` (value: `"DEVICE_FORM_FACTOR_UNSPECIFIED"`)

* `PHONE` (value: `"PHONE"`)

* `TABLET` (value: `"TABLET"`)

* `WEARABLE` (value: `"WEARABLE"`)




