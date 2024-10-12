

# KustoDatabaseDataSetProperties

Properties of the kusto database data set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSetId** | **String** | Unique id for identifying a data set resource |  [optional] [readonly] |
|**kustoDatabaseResourceId** | **String** | Resource id of the kusto database. |  |
|**location** | **String** | Location of the kusto cluster. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the kusto database data set. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| MOVING | &quot;Moving&quot; |
| FAILED | &quot;Failed&quot; |



