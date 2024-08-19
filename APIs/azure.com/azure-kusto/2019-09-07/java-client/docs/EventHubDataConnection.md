

# EventHubDataConnection

Class representing an event hub data connection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**EventHubConnectionProperties**](EventHubConnectionProperties.md) |  |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | Kind of the endpoint for the data connection |  |
|**location** | **String** | Resource location. |  [optional] |
|**id** | **String** | Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |  [optional] [readonly] |
|**name** | **String** | The name of the resource |  [optional] [readonly] |
|**type** | **String** | The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts. |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| EVENT_HUB | &quot;EventHub&quot; |
| EVENT_GRID | &quot;EventGrid&quot; |
| IOT_HUB | &quot;IotHub&quot; |



