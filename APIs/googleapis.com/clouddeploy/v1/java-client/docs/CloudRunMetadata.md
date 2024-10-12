

# CloudRunMetadata

CloudRunMetadata contains information from a Cloud Run deployment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**job** | **String** | Output only. The name of the Cloud Run job that is associated with a &#x60;Rollout&#x60;. Format is &#x60;projects/{project}/locations/{location}/jobs/{job_name}&#x60;. |  [optional] [readonly] |
|**revision** | **String** | Output only. The Cloud Run Revision id associated with a &#x60;Rollout&#x60;. |  [optional] [readonly] |
|**service** | **String** | Output only. The name of the Cloud Run Service that is associated with a &#x60;Rollout&#x60;. Format is &#x60;projects/{project}/locations/{location}/services/{service}&#x60;. |  [optional] [readonly] |
|**serviceUrls** | **List&lt;String&gt;** | Output only. The Cloud Run Service urls that are associated with a &#x60;Rollout&#x60;. |  [optional] [readonly] |



