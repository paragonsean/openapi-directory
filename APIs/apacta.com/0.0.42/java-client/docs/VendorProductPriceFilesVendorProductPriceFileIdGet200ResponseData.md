

# VendorProductPriceFilesVendorProductPriceFileIdGet200ResponseData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**companiesVendorId** | **UUID** |  |  [optional] |
|**created** | **String** |  |  [optional] [readonly] |
|**createdById** | **UUID** |  |  [optional] |
|**deleted** | **String** | Only present if it&#39;s a deleted object |  [optional] [readonly] |
|**dir** | **String** |  |  [optional] |
|**_file** | **String** |  |  [optional] |
|**finished** | **Boolean** |  |  [optional] |
|**id** | **UUID** |  |  [optional] |
|**modified** | **String** |  |  [optional] [readonly] |
|**originalFileName** | **String** |  |  [optional] |
|**progress** | **Integer** |  |  [optional] |
|**size** | **Integer** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**type** | **String** |  |  [optional] |
|**vendorProductsCount** | **Integer** |  |  [optional] |
|**vendorProductsCountTotal** | **Integer** |  |  [optional] |
|**downloadLink** | **URI** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AWAITING | &quot;awaiting&quot; |
| FRESH | &quot;fresh&quot; |
| EXPIRED | &quot;expired&quot; |
| FAILED | &quot;failed&quot; |



