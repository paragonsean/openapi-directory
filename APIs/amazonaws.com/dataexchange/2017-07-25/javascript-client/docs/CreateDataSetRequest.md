# AwsDataExchange.CreateDataSetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetType** | **String** | The type of asset that is added to a data set. | 
**description** | **String** | A description for the data set. This value can be up to 16,348 characters long. | 
**name** | **String** | The name of the data set. | 
**tags** | **{String: String}** | A data set tag is an optional label that you can assign to a data set when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to these data sets and revisions. | [optional] 



## Enum: AssetTypeEnum


* `S3_SNAPSHOT` (value: `"S3_SNAPSHOT"`)

* `REDSHIFT_DATA_SHARE` (value: `"REDSHIFT_DATA_SHARE"`)

* `API_GATEWAY_API` (value: `"API_GATEWAY_API"`)

* `S3_DATA_ACCESS` (value: `"S3_DATA_ACCESS"`)

* `LAKE_FORMATION_DATA_PERMISSION` (value: `"LAKE_FORMATION_DATA_PERMISSION"`)




