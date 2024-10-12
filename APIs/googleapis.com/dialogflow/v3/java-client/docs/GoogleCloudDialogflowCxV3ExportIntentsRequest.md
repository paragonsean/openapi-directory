

# GoogleCloudDialogflowCxV3ExportIntentsRequest

The request message for Intents.ExportIntents.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataFormat** | [**DataFormatEnum**](#DataFormatEnum) | Optional. The data format of the exported intents. If not specified, &#x60;BLOB&#x60; is assumed. |  [optional] |
|**intents** | **List&lt;String&gt;** | Required. The name of the intents to export. Format: &#x60;projects//locations//agents//intents/&#x60;. |  [optional] |
|**intentsContentInline** | **Boolean** | Optional. The option to return the serialized intents inline. |  [optional] |
|**intentsUri** | **String** | Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the intents to. The format of this URI must be &#x60;gs:///&#x60;. Dialogflow performs a write operation for the Cloud Storage object on the caller&#39;s behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). |  [optional] |



## Enum: DataFormatEnum

| Name | Value |
|---- | -----|
| DATA_FORMAT_UNSPECIFIED | &quot;DATA_FORMAT_UNSPECIFIED&quot; |
| BLOB | &quot;BLOB&quot; |
| JSON | &quot;JSON&quot; |
| CSV | &quot;CSV&quot; |



