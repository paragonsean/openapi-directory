# BigQueryConnectionApi.SparkProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metastoreServiceConfig** | [**MetastoreServiceConfig**](MetastoreServiceConfig.md) |  | [optional] 
**serviceAccountId** | **String** | Output only. The account ID of the service created for the purpose of this connection. The service account does not have any permissions associated with it when it is created. After creation, customers delegate permissions to the service account. When the connection is used in the context of a stored procedure for Apache Spark in BigQuery, the service account is used to connect to the desired resources in Google Cloud. The account ID is in the form of: bqcx--@gcp-sa-bigquery-consp.iam.gserviceaccount.com | [optional] [readonly] 
**sparkHistoryServerConfig** | [**SparkHistoryServerConfig**](SparkHistoryServerConfig.md) |  | [optional] 


