

# Workload

Workload is an App Hub data model that contains a discovered workload, which represents a binary deployment (such as managed instance groups (MIGs) and GKE deployments) that performs the smallest logical subset of business functionality.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**Attributes**](Attributes.md) |  |  [optional] |
|**createTime** | **String** | Output only. Create time. |  [optional] [readonly] |
|**description** | **String** | Optional. User-defined description of a Workload. Can have a maximum length of 2048 characters. |  [optional] |
|**discoveredWorkload** | **String** | Required. Immutable. The resource name of the original discovered workload. |  [optional] |
|**displayName** | **String** | Optional. User-defined name for the Workload. Can have a maximum length of 63 characters. |  [optional] |
|**name** | **String** | Identifier. The resource name of the Workload. Format: \&quot;projects/{host-project-id}/locations/{location}/applications/{application-id}/workloads/{workload-id}\&quot; |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Workload state. |  [optional] [readonly] |
|**uid** | **String** | Output only. A universally unique identifier (UUID) for the &#x60;Workload&#x60; in the UUID4 format. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Update time. |  [optional] [readonly] |
|**workloadProperties** | [**WorkloadProperties**](WorkloadProperties.md) |  |  [optional] |
|**workloadReference** | [**WorkloadReference**](WorkloadReference.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETING | &quot;DELETING&quot; |
| DETACHED | &quot;DETACHED&quot; |



