# BigQueryConnectionApi.CloudSqlProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | [**CloudSqlCredential**](CloudSqlCredential.md) |  | [optional] 
**database** | **String** | Database name. | [optional] 
**instanceId** | **String** | Cloud SQL instance ID in the form &#x60;project:location:instance&#x60;. | [optional] 
**serviceAccountId** | **String** | Output only. The account ID of the service used for the purpose of this connection. When the connection is used in the context of an operation in BigQuery, this service account will serve as the identity being used for connecting to the CloudSQL instance specified in this connection. | [optional] [readonly] 
**type** | **String** | Type of the Cloud SQL database. | [optional] 



## Enum: TypeEnum


* `DATABASE_TYPE_UNSPECIFIED` (value: `"DATABASE_TYPE_UNSPECIFIED"`)

* `POSTGRES` (value: `"POSTGRES"`)

* `MYSQL` (value: `"MYSQL"`)




