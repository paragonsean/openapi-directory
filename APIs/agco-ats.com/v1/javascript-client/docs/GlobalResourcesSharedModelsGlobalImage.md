# AgcoApi.GlobalResourcesSharedModelsGlobalImage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CRC** | **String** | The Hash of the file (SHA256, HEX-encoded). | 
**categories** | [**[GlobalResourcesSharedModelsGlobalImageCategory]**](GlobalResourcesSharedModelsGlobalImageCategory.md) | The category of the file. | [optional] 
**date** | **Date** | The date of the file. | [optional] 
**description** | **String** | The description of the file. | 
**height** | **Number** | The height of the file. | 
**id** | **String** | The Id of the GlobalImage Metadata. | [optional] 
**name** | **String** | The name of the file when downloaded. | 
**publisher** | **String** | The Publisher of the file. | [optional] 
**size** | **Number** | The size of the file in bytes. Null until assigned by server when marked as &#39;Available&#39;. Read Only | [optional] 
**state** | **String** | Indicates the state of this file. Must be &#39;Created&#39; when created. Read Only. | 
**thumbnailCRC** | **String** | The Hash of the thumbnail file (SHA256, HEX-encoded). | 
**thumbnailSize** | **Number** | The size of the thumbnail file in bytes. Null until assigned by server when marked as &#39;Available&#39;. Read Only | [optional] 
**width** | **Number** | The width of the file. | 



## Enum: StateEnum


* `Created` (value: `"Created"`)

* `Available` (value: `"Available"`)

* `Removed` (value: `"Removed"`)




