# AppCenterClient.SymbolUploadsCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build** | **String** | The build number. Optional for Apple. Required for Android. | [optional] 
**clientCallback** | **String** | The callback URL that the client can optionally provide to get status updates for the current symbol upload | [optional] 
**fileName** | **String** | The file name for the symbol upload | [optional] 
**symbolType** | **String** | The type of the symbol for the current symbol upload | 
**version** | **String** | The version number. Optional for Apple. Required for Android. | [optional] 



## Enum: SymbolTypeEnum


* `Apple` (value: `"Apple"`)

* `JavaScript` (value: `"JavaScript"`)

* `Breakpad` (value: `"Breakpad"`)

* `AndroidProguard` (value: `"AndroidProguard"`)

* `UWP` (value: `"UWP"`)




