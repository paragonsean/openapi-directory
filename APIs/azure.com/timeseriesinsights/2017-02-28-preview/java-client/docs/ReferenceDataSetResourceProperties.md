

# ReferenceDataSetResourceProperties

Properties of the reference data set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyProperties** | [**List&lt;ReferenceDataSetKeyProperty&gt;**](ReferenceDataSetKeyProperty.md) | The list of key properties for the reference data set. |  |
|**creationTime** | **OffsetDateTime** | The time the resource was created. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the resource. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;Accepted&quot; |
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| DELETING | &quot;Deleting&quot; |



