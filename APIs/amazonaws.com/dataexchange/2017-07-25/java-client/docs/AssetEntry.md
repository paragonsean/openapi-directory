

# AssetEntry

An asset in AWS Data Exchange is a piece of data (Amazon S3 object) or a means of fulfilling data (Amazon Redshift datashare or Amazon API Gateway API, AWS Lake Formation data permission, or Amazon S3 data access). The asset can be a structured data file, an image file, or some other data file that can be stored as an Amazon S3 object, an Amazon API Gateway API, or an Amazon Redshift datashare, an AWS Lake Formation data permission, or an Amazon S3 data access. When you create an import job for your files, API Gateway APIs, Amazon Redshift datashares, AWS Lake Formation data permission, or Amazon S3 data access, you create an asset in AWS Data Exchange.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | [**String**](String.md) |  |  |
|**assetDetails** | [**GetAssetResponseAssetDetails**](GetAssetResponseAssetDetails.md) |  |  |
|**assetType** | [**AssetType**](AssetType.md) |  |  |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**dataSetId** | [**String**](String.md) |  |  |
|**id** | [**String**](String.md) |  |  |
|**name** | [**String**](String.md) |  |  |
|**revisionId** | [**String**](String.md) |  |  |
|**sourceId** | [**String**](String.md) |  |  [optional] |
|**updatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |



