# DialogflowApi.GoogleCloudDialogflowCxV3beta1ImportTestCasesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **Blob** | Uncompressed raw byte content for test cases. | [optional] 
**gcsUri** | **String** | The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to import test cases from. The format of this URI must be &#x60;gs:///&#x60;. Dialogflow performs a read operation for the Cloud Storage object on the caller&#39;s behalf, so your request authentication must have read permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). | [optional] 


