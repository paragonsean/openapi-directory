# AppCenterClient.SymbolUpload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appId** | **String** | The application that this symbol upload belongs to | 
**fileName** | **String** | The file name for the symbol upload | [optional] 
**fileSize** | **Number** | The size of the file in Mebibytes. This may be 0 until the status is indexed | [optional] 
**origin** | **String** | The origin of the symbol upload | [optional] 
**status** | **String** | The current status for the symbol upload | 
**symbolType** | **String** | The type of the symbol for the current symbol upload | 
**symbolUploadId** | **String** | The id for the current symbol upload | 
**symbolsUploaded** | [**[SymbolUploadsList200ResponseInnerSymbolsUploadedInner]**](SymbolUploadsList200ResponseInnerSymbolsUploadedInner.md) | The symbols found in the upload. This may be empty until the status is indexed | [optional] 
**timestamp** | **Date** | When the symbol upload was committed, or last transaction time if not committed | [optional] 
**user** | [**SymbolUploadsList200ResponseInnerUser**](SymbolUploadsList200ResponseInnerUser.md) |  | [optional] 



## Enum: OriginEnum


* `User` (value: `"User"`)

* `System` (value: `"System"`)





## Enum: StatusEnum


* `created` (value: `"created"`)

* `committed` (value: `"committed"`)

* `aborted` (value: `"aborted"`)

* `processing` (value: `"processing"`)

* `indexed` (value: `"indexed"`)

* `failed` (value: `"failed"`)





## Enum: SymbolTypeEnum


* `Apple` (value: `"Apple"`)

* `JavaScript` (value: `"JavaScript"`)

* `Breakpad` (value: `"Breakpad"`)

* `AndroidProguard` (value: `"AndroidProguard"`)

* `UWP` (value: `"UWP"`)




