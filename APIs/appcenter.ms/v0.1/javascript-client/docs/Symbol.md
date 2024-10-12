# AppCenterClient.Symbol

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternateSymbolIds** | **[String]** | The other symbols in the same file | 
**appId** | **String** | The application that this symbol belongs to | 
**build** | **String** | The build number. Optional for Apple. Required for Android. | [optional] 
**origin** | **String** | The origin of the symbol file | 
**platform** | **String** | The platform that this symbol is associated with | 
**status** | **String** | Whether the symbol is ignored. | 
**symbolId** | **String** | The unique id for this symbol (uuid) | 
**symbolUploadId** | **String** | The id of the symbol upload this symbol belongs to. | 
**type** | **String** | The type of the symbol for the current symbol upload | 
**url** | **String** | The path name of the symbol file in blob storage | 
**version** | **String** | The version number. Optional for Apple. Required for Android. | [optional] 



## Enum: OriginEnum


* `System` (value: `"System"`)

* `User` (value: `"User"`)





## Enum: StatusEnum


* `available` (value: `"available"`)

* `ignored` (value: `"ignored"`)





## Enum: TypeEnum


* `Apple` (value: `"Apple"`)

* `JavaScript` (value: `"JavaScript"`)

* `Breakpad` (value: `"Breakpad"`)

* `AndroidProguard` (value: `"AndroidProguard"`)

* `UWP` (value: `"UWP"`)




