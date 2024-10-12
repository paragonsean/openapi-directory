# AmazonOmics.CreateAnnotationStoreRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | [**CreateAnnotationStoreRequestReference**](CreateAnnotationStoreRequestReference.md) |  | [optional] 
**name** | **String** | A name for the store. | [optional] 
**description** | **String** | A description for the store. | [optional] 
**tags** | **{String: String}** | Tags for the store. | [optional] 
**sseConfig** | [**CreateAnnotationStoreRequestSseConfig**](CreateAnnotationStoreRequestSseConfig.md) |  | [optional] 
**storeFormat** | **String** | The annotation file format of the store. | 
**storeOptions** | [**CreateAnnotationStoreRequestStoreOptions**](CreateAnnotationStoreRequestStoreOptions.md) |  | [optional] 



## Enum: StoreFormatEnum


* `GFF` (value: `"GFF"`)

* `TSV` (value: `"TSV"`)

* `VCF` (value: `"VCF"`)




