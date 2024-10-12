

# ProductModel

Product Model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**numberOfFiles** | **Long** |  |  [optional] |
|**parentProduct** | [**ProductModel**](ProductModel.md) |  |  [optional] |
|**productDesc** | **String** |  |  [optional] |
|**productFiles** | [**List&lt;ProductFileModel&gt;**](ProductFileModel.md) |  |  [optional] |
|**productFrequency** | **String** |  |  [optional] |
|**productFromDate** | **String** |  |  [optional] |
|**productIdentifier** | **Integer** |  |  [optional] |
|**productLevel** | [**ProductLevelEnum**](#ProductLevelEnum) | Represents the Level in the Product hierarchy. |  [optional] |
|**productLinkPath** | **URI** |  |  [optional] |
|**productShortName** | **String** |  |  [optional] |
|**productTitle** | **String** |  |  [optional] |
|**productToDate** | **String** |  |  [optional] |



## Enum: ProductLevelEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;available&quot; |
| PENDING | &quot;pending&quot; |
| SOLD | &quot;sold&quot; |



