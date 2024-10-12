

# GoogleCloudDiscoveryengineV1betaDocumentInfo

Detailed document information associated with a user event.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The Document resource ID. |  [optional] |
|**name** | **String** | The Document resource full name, of the form: &#x60;projects/{project_id}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}/branches/{branch_id}/documents/{document_id}&#x60; |  [optional] |
|**promotionIds** | **List&lt;String&gt;** | The promotion IDs associated with this Document. Currently, this field is restricted to at most one ID. |  [optional] |
|**quantity** | **Integer** | Quantity of the Document associated with the user event. Defaults to 1. For example, this field will be 2 if two quantities of the same Document are involved in a &#x60;add-to-cart&#x60; event. Required for events of the following event types: * &#x60;add-to-cart&#x60; * &#x60;purchase&#x60; |  [optional] |
|**uri** | **String** | The Document URI - only allowed for website data stores. |  [optional] |



