

# GoogleCloudDialogflowCxV3ExportFlowRequest

The request message for Flows.ExportFlow.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**flowUri** | **String** | Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the flow to. The format of this URI must be &#x60;gs:///&#x60;. If left unspecified, the serialized flow is returned inline. Dialogflow performs a write operation for the Cloud Storage object on the caller&#39;s behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). |  [optional] |
|**includeReferencedFlows** | **Boolean** | Optional. Whether to export flows referenced by the specified flow. |  [optional] |



