

# GoogleCloudApigeeV1RuntimeConfig

Runtime configuration for the organization. Response for GetRuntimeConfig.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analyticsBucket** | **String** | Cloud Storage bucket used for uploading Analytics records. |  [optional] |
|**name** | **String** | Name of the resource in the following format: &#x60;organizations/{org}/runtimeConfig&#x60;. |  [optional] |
|**tenantProjectId** | **String** | Output only. Tenant project ID associated with the Apigee organization. The tenant project is used to host Google-managed resources that are dedicated to this Apigee organization. Clients have limited access to resources within the tenant project used to support Apigee runtime instances. Access to the tenant project is managed using SetSyncAuthorization. It can be empty if the tenant project hasn&#39;t been created yet. |  [optional] [readonly] |
|**traceBucket** | **String** | Cloud Storage bucket used for uploading Trace records. |  [optional] |



