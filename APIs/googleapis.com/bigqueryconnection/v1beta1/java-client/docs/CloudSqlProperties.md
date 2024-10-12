

# CloudSqlProperties

Connection properties specific to the Cloud SQL.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**credential** | [**CloudSqlCredential**](CloudSqlCredential.md) |  |  [optional] |
|**database** | **String** | Database name. |  [optional] |
|**instanceId** | **String** | Cloud SQL instance ID in the form &#x60;project:location:instance&#x60;. |  [optional] |
|**serviceAccountId** | **String** | Output only. The account ID of the service used for the purpose of this connection. When the connection is used in the context of an operation in BigQuery, this service account will serve as the identity being used for connecting to the CloudSQL instance specified in this connection. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the Cloud SQL database. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DATABASE_TYPE_UNSPECIFIED | &quot;DATABASE_TYPE_UNSPECIFIED&quot; |
| POSTGRES | &quot;POSTGRES&quot; |
| MYSQL | &quot;MYSQL&quot; |



