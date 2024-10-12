

# GoogleCloudApigeeV1ApiSecurityRuntimeConfig

Response for GetApiSecurityRuntimeConfig[EnvironmentService.GetApiSecurityRuntimeConfig].

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**location** | **List&lt;String&gt;** | A list of up to 5 Cloud Storage Blobs that contain SecurityActions. |  [optional] |
|**name** | **String** | Name of the environment API Security Runtime configuration resource. Format: &#x60;organizations/{org}/environments/{env}/apiSecurityRuntimeConfig&#x60; |  [optional] |
|**revisionId** | **String** | Revision ID of the API Security Runtime configuration. The higher the value, the more recently the configuration was deployed. |  [optional] |
|**uid** | **String** | Unique ID for the API Security Runtime configuration. The ID will only change if the environment is deleted and recreated. |  [optional] |
|**updateTime** | **String** | Time that the API Security Runtime configuration was updated. |  [optional] |



