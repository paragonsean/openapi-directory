

# GetProductInfo200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**barcodeUrl** | **URI** | The URL to the scannable barcode image. |  [optional] |
|**codeType** | [**CodeTypeEnum**](#CodeTypeEnum) | The type of product code (UPC/EAN/ISBN). |  [optional] |
|**product** | [**GetProductInfo200ResponseProduct**](GetProductInfo200ResponseProduct.md) |  |  [optional] |



## Enum: CodeTypeEnum

| Name | Value |
|---- | -----|
| UPC | &quot;UPC&quot; |
| EAN | &quot;EAN&quot; |
| ISBN | &quot;ISBN&quot; |



