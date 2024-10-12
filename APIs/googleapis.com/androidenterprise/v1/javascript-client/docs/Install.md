# GooglePlayEmmApi.Install

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installState** | **String** | Install state. The state \&quot;installPending\&quot; means that an install request has recently been made and download to the device is in progress. The state \&quot;installed\&quot; means that the app has been installed. This field is read-only. | [optional] 
**productId** | **String** | The ID of the product that the install is for. For example, \&quot;app:com.google.android.gm\&quot;. | [optional] 
**versionCode** | **Number** | The version of the installed product. Guaranteed to be set only if the install state is \&quot;installed\&quot;. | [optional] 



## Enum: InstallStateEnum


* `installed` (value: `"installed"`)

* `installPending` (value: `"installPending"`)




