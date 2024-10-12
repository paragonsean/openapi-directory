

# GoogleCloudDialogflowCxV3KnowledgeConnectorSettings

The Knowledge Connector settings for this page or flow. This includes information such as the attached Knowledge Bases, and the way to execute fulfillment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataStoreConnections** | [**List&lt;GoogleCloudDialogflowCxV3DataStoreConnection&gt;**](GoogleCloudDialogflowCxV3DataStoreConnection.md) | Optional. List of related data store connections. |  [optional] |
|**enabled** | **Boolean** | Whether Knowledge Connector is enabled or not. |  [optional] |
|**targetFlow** | **String** | The target flow to transition to. Format: &#x60;projects//locations//agents//flows/&#x60;. |  [optional] |
|**targetPage** | **String** | The target page to transition to. Format: &#x60;projects//locations//agents//flows//pages/&#x60;. |  [optional] |
|**triggerFulfillment** | [**GoogleCloudDialogflowCxV3Fulfillment**](GoogleCloudDialogflowCxV3Fulfillment.md) |  |  [optional] |



