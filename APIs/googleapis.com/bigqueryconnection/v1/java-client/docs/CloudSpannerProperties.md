

# CloudSpannerProperties

Connection properties specific to Cloud Spanner.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**database** | **String** | Cloud Spanner database in the form &#x60;project/instance/database&#39; |  [optional] |
|**databaseRole** | **String** | Optional. Cloud Spanner database role for fine-grained access control. The Cloud Spanner admin should have provisioned the database role with appropriate permissions, such as &#x60;SELECT&#x60; and &#x60;INSERT&#x60;. Other users should only use roles provided by their Cloud Spanner admins. For more details, see [About fine-grained access control] (https://cloud.google.com/spanner/docs/fgac-about). REQUIRES: The database role name must start with a letter, and can only contain letters, numbers, and underscores. |  [optional] |
|**maxParallelism** | **Integer** | Allows setting max parallelism per query when executing on Spanner independent compute resources. If unspecified, default values of parallelism are chosen that are dependent on the Cloud Spanner instance configuration. REQUIRES: &#x60;use_parallelism&#x60; must be set. REQUIRES: &#x60;use_data_boost&#x60; must be set. |  [optional] |
|**useDataBoost** | **Boolean** | If set, the request will be executed via Spanner independent compute resources. REQUIRES: &#x60;use_parallelism&#x60; must be set. |  [optional] |
|**useParallelism** | **Boolean** | If parallelism should be used when reading from Cloud Spanner |  [optional] |
|**useServerlessAnalytics** | **Boolean** | Deprecated: prefer use_data_boost instead. If the serverless analytics service should be used to read data from Cloud Spanner. Note: &#x60;use_parallelism&#x60; must be set when using serverless analytics. |  [optional] |



