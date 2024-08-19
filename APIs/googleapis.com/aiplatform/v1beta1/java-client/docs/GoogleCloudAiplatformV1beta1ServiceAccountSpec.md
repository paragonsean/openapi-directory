

# GoogleCloudAiplatformV1beta1ServiceAccountSpec

Configuration for the use of custom service account to run the workloads.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableCustomServiceAccount** | **Boolean** | Required. If true, custom user-managed service account is enforced to run any workloads (for example, Vertex Jobs) on the resource. Otherwise, uses the [Vertex AI Custom Code Service Agent](https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents). |  [optional] |
|**serviceAccount** | **String** | Optional. Default service account that this PersistentResource&#39;s workloads run as. The workloads include: * Any runtime specified via &#x60;ResourceRuntimeSpec&#x60; on creation time, for example, Ray. * Jobs submitted to PersistentResource, if no other service account specified in the job specs. Only works when custom service account is enabled and users have the &#x60;iam.serviceAccounts.actAs&#x60; permission on this service account. Required if any containers are specified in &#x60;ResourceRuntimeSpec&#x60;. |  [optional] |



