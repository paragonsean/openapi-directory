# BigQueryConnectionApi.CloudResourceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serviceAccountId** | **String** | Output only. The account ID of the service created for the purpose of this connection. The service account does not have any permissions associated with it when it is created. After creation, customers delegate permissions to the service account. When the connection is used in the context of an operation in BigQuery, the service account will be used to connect to the desired resources in GCP. The account ID is in the form of: @gcp-sa-bigquery-cloudresource.iam.gserviceaccount.com | [optional] [readonly] 


