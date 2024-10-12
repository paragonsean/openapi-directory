

# Database

Class representing a Kusto database.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) | Kind of the database |  [optional] |
|**location** | **String** | Resource location. |  [optional] |
|**id** | **String** | Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |  [optional] [readonly] |
|**name** | **String** | The name of the resource |  [optional] [readonly] |
|**type** | **String** | The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts. |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| READ_WRITE | &quot;ReadWrite&quot; |
| READ_ONLY_FOLLOWING | &quot;ReadOnlyFollowing&quot; |



