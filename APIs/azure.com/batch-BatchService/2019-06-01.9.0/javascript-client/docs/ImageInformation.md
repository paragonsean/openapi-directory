# BatchService.ImageInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batchSupportEndOfLife** | **Date** |  | [optional] 
**capabilities** | **[String]** | Not every capability of the Image is listed. Capabilities in this list are considered of special interest and are generally related to integration with other features in the Azure Batch service. | [optional] 
**imageReference** | [**ImageReference**](ImageReference.md) |  | 
**nodeAgentSKUId** | **String** |  | 
**osType** | **String** |  | 
**verificationType** | **String** |  | 



## Enum: OsTypeEnum


* `linux` (value: `"linux"`)

* `windows` (value: `"windows"`)





## Enum: VerificationTypeEnum


* `verified` (value: `"verified"`)

* `unverified` (value: `"unverified"`)




