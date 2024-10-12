

# CreateAnnotationStoreRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reference** | [**CreateAnnotationStoreRequestReference**](CreateAnnotationStoreRequestReference.md) |  |  [optional] |
|**name** | **String** | A name for the store. |  [optional] |
|**description** | **String** | A description for the store. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Tags for the store. |  [optional] |
|**sseConfig** | [**CreateAnnotationStoreRequestSseConfig**](CreateAnnotationStoreRequestSseConfig.md) |  |  [optional] |
|**storeFormat** | [**StoreFormatEnum**](#StoreFormatEnum) | The annotation file format of the store. |  |
|**storeOptions** | [**CreateAnnotationStoreRequestStoreOptions**](CreateAnnotationStoreRequestStoreOptions.md) |  |  [optional] |



## Enum: StoreFormatEnum

| Name | Value |
|---- | -----|
| GFF | &quot;GFF&quot; |
| TSV | &quot;TSV&quot; |
| VCF | &quot;VCF&quot; |



