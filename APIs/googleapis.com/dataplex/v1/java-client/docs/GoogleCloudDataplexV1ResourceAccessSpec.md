

# GoogleCloudDataplexV1ResourceAccessSpec

ResourceAccessSpec holds the access control configuration to be enforced on the resources, for example, Cloud Storage bucket, BigQuery dataset, BigQuery table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**owners** | **List&lt;String&gt;** | Optional. The set of principals to be granted owner role on the resource. |  [optional] |
|**readers** | **List&lt;String&gt;** | Optional. The format of strings follows the pattern followed by IAM in the bindings. user:{email}, serviceAccount:{email} group:{email}. The set of principals to be granted reader role on the resource. |  [optional] |
|**writers** | **List&lt;String&gt;** | Optional. The set of principals to be granted writer role on the resource. |  [optional] |



