

# SparkStatistics

Statistics for a BigSpark query. Populated as part of JobStatistics2

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpoints** | **Map&lt;String, String&gt;** | Output only. Endpoints returned from Dataproc. Key list: - history_server_endpoint: A link to Spark job UI. |  [optional] [readonly] |
|**gcsStagingBucket** | **String** | Output only. The Google Cloud Storage bucket that is used as the default filesystem by the Spark application. This fields is only filled when the Spark procedure uses the INVOKER security mode. It is inferred from the system variable @@spark_proc_properties.staging_bucket if it is provided. Otherwise, BigQuery creates a default staging bucket for the job and returns the bucket name in this field. Example: * &#x60;gs://[bucket_name]&#x60; |  [optional] [readonly] |
|**kmsKeyName** | **String** | Output only. The Cloud KMS encryption key that is used to protect the resources created by the Spark job. If the Spark procedure uses DEFINER security mode, the Cloud KMS key is inferred from the Spark connection associated with the procedure if it is provided. Otherwise the key is inferred from the default key of the Spark connection&#39;s project if the CMEK organization policy is enforced. If the Spark procedure uses INVOKER security mode, the Cloud KMS encryption key is inferred from the system variable @@spark_proc_properties.kms_key_name if it is provided. Otherwise, the key is inferred fromt he default key of the BigQuery job&#39;s project if the CMEK organization policy is enforced. Example: * &#x60;projects/[kms_project_id]/locations/[region]/keyRings/[key_region]/cryptoKeys/[key]&#x60; |  [optional] [readonly] |
|**loggingInfo** | [**SparkLoggingInfo**](SparkLoggingInfo.md) |  |  [optional] |
|**sparkJobId** | **String** | Output only. Spark job ID if a Spark job is created successfully. |  [optional] [readonly] |
|**sparkJobLocation** | **String** | Output only. Location where the Spark job is executed. A location is selected by BigQueury for jobs configured to run in a multi-region. |  [optional] [readonly] |



