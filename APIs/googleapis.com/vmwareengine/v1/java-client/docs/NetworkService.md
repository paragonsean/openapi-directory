

# NetworkService

Represents a network service that is managed by a `NetworkPolicy` resource. A network service provides a way to control an aspect of external access to VMware workloads. For example, whether the VMware workloads in the private clouds governed by a network policy can access or be accessed from the internet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | True if the service is enabled; false otherwise. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the service. New values may be added to this enum when appropriate. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| UNPROVISIONED | &quot;UNPROVISIONED&quot; |
| RECONCILING | &quot;RECONCILING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |



