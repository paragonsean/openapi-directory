

# GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpec

Specification for the BigQuery connection to a Cloud SQL instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**database** | **String** | Database name. |  [optional] |
|**instanceId** | **String** | Cloud SQL instance ID in the format of &#x60;project:location:instance&#x60;. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the Cloud SQL database. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DATABASE_TYPE_UNSPECIFIED | &quot;DATABASE_TYPE_UNSPECIFIED&quot; |
| POSTGRES | &quot;POSTGRES&quot; |
| MYSQL | &quot;MYSQL&quot; |



