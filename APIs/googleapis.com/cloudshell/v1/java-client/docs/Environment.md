

# Environment

A Cloud Shell environment, which is defined as the combination of a Docker image specifying what is installed on the environment and a home directory containing the user's data that will remain across sessions. Each user has at least an environment with the ID \"default\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dockerImage** | **String** | Required. Immutable. Full path to the Docker image used to run this environment, e.g. \&quot;gcr.io/dev-con/cloud-devshell:latest\&quot;. |  [optional] |
|**id** | **String** | Output only. The environment&#39;s identifier, unique among the user&#39;s environments. |  [optional] [readonly] |
|**name** | **String** | Immutable. Full name of this resource, in the format &#x60;users/{owner_email}/environments/{environment_id}&#x60;. &#x60;{owner_email}&#x60; is the email address of the user to whom this environment belongs, and &#x60;{environment_id}&#x60; is the identifier of this environment. For example, &#x60;users/someone@example.com/environments/default&#x60;. |  [optional] |
|**publicKeys** | **List&lt;String&gt;** | Output only. Public keys associated with the environment. Clients can connect to this environment via SSH only if they possess a private key corresponding to at least one of these public keys. Keys can be added to or removed from the environment using the AddPublicKey and RemovePublicKey methods. |  [optional] [readonly] |
|**sshHost** | **String** | Output only. Host to which clients can connect to initiate SSH sessions with the environment. |  [optional] [readonly] |
|**sshPort** | **Integer** | Output only. Port to which clients can connect to initiate SSH sessions with the environment. |  [optional] [readonly] |
|**sshUsername** | **String** | Output only. Username that clients should use when initiating SSH sessions with the environment. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Current execution state of this environment. |  [optional] [readonly] |
|**webHost** | **String** | Output only. Host to which clients can connect to initiate HTTPS or WSS connections with the environment. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| DELETING | &quot;DELETING&quot; |



