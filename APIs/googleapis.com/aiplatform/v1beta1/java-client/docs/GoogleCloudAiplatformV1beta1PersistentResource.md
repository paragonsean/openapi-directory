

# GoogleCloudAiplatformV1beta1PersistentResource

Represents long-lasting resources that are dedicated to users to runs custom workloads. A PersistentResource can have multiple node pools and each node pool can have its own machine spec.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Time when the PersistentResource was created. |  [optional] [readonly] |
|**displayName** | **String** | Optional. The display name of the PersistentResource. The name can be up to 128 characters long and can consist of any UTF-8 characters. |  [optional] |
|**encryptionSpec** | [**GoogleCloudAiplatformV1beta1EncryptionSpec**](GoogleCloudAiplatformV1beta1EncryptionSpec.md) |  |  [optional] |
|**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. The labels with user-defined metadata to organize PersistentResource. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |  [optional] |
|**name** | **String** | Immutable. Resource name of a PersistentResource. |  [optional] |
|**network** | **String** | Optional. The full name of the Compute Engine [network](/compute/docs/networks-and-firewalls#networks) to peered with Vertex AI to host the persistent resources. For example, &#x60;projects/12345/global/networks/myVPC&#x60;. [Format](/compute/docs/reference/rest/v1/networks/insert) is of the form &#x60;projects/{project}/global/networks/{network}&#x60;. Where {project} is a project number, as in &#x60;12345&#x60;, and {network} is a network name. To specify this field, you must have already [configured VPC Network Peering for Vertex AI](https://cloud.google.com/vertex-ai/docs/general/vpc-peering). If this field is left unspecified, the resources aren&#39;t peered with any network. |  [optional] |
|**reservedIpRanges** | **List&lt;String&gt;** | Optional. A list of names for the reserved IP ranges under the VPC network that can be used for this persistent resource. If set, we will deploy the persistent resource within the provided IP ranges. Otherwise, the persistent resource is deployed to any IP ranges under the provided VPC network. Example: [&#39;vertex-ai-ip-range&#39;]. |  [optional] |
|**resourcePools** | [**List&lt;GoogleCloudAiplatformV1beta1ResourcePool&gt;**](GoogleCloudAiplatformV1beta1ResourcePool.md) | Required. The spec of the pools of different resources. |  [optional] |
|**resourceRuntime** | [**GoogleCloudAiplatformV1beta1ResourceRuntime**](GoogleCloudAiplatformV1beta1ResourceRuntime.md) |  |  [optional] |
|**resourceRuntimeSpec** | [**GoogleCloudAiplatformV1beta1ResourceRuntimeSpec**](GoogleCloudAiplatformV1beta1ResourceRuntimeSpec.md) |  |  [optional] |
|**startTime** | **String** | Output only. Time when the PersistentResource for the first time entered the &#x60;RUNNING&#x60; state. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The detailed state of a Study. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Time when the PersistentResource was most recently updated. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PROVISIONING | &quot;PROVISIONING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| STOPPING | &quot;STOPPING&quot; |
| ERROR | &quot;ERROR&quot; |



