

# CreateDataSetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetType** | [**AssetTypeEnum**](#AssetTypeEnum) | The type of asset that is added to a data set. |  |
|**description** | **String** | A description for the data set. This value can be up to 16,348 characters long. |  |
|**name** | **String** | The name of the data set. |  |
|**tags** | **Map&lt;String, String&gt;** | A data set tag is an optional label that you can assign to a data set when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to these data sets and revisions. |  [optional] |



## Enum: AssetTypeEnum

| Name | Value |
|---- | -----|
| S3_SNAPSHOT | &quot;S3_SNAPSHOT&quot; |
| REDSHIFT_DATA_SHARE | &quot;REDSHIFT_DATA_SHARE&quot; |
| API_GATEWAY_API | &quot;API_GATEWAY_API&quot; |
| S3_DATA_ACCESS | &quot;S3_DATA_ACCESS&quot; |
| LAKE_FORMATION_DATA_PERMISSION | &quot;LAKE_FORMATION_DATA_PERMISSION&quot; |



