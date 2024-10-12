

# DiscoveredWorkload

DiscoveredWorkload is a binary deployment (such as managed instance groups (MIGs) and GKE deployments) that performs the smallest logical subset of business functionality. A discovered workload can be registered to an App Hub Workload.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Identifier. The resource name of the discovered workload. Format: \&quot;projects/{host-project-id}/locations/{location}/discoveredWorkloads/{uuid}\&quot; |  [optional] |
|**workloadProperties** | [**WorkloadProperties**](WorkloadProperties.md) |  |  [optional] |
|**workloadReference** | [**WorkloadReference**](WorkloadReference.md) |  |  [optional] |



