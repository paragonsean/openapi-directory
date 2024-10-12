# DialogflowApi.GoogleCloudDialogflowV2beta1IntentMessageRbmCardContentRbmMedia

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fileUri** | **String** | Required. Publicly reachable URI of the file. The RBM platform determines the MIME type of the file from the content-type field in the HTTP headers when the platform fetches the file. The content-type field must be present and accurate in the HTTP response from the URL. | [optional] 
**height** | **String** | Required for cards with vertical orientation. The height of the media within a rich card with a vertical layout. For a standalone card with horizontal layout, height is not customizable, and this field is ignored. | [optional] 
**thumbnailUri** | **String** | Optional. Publicly reachable URI of the thumbnail.If you don&#39;t provide a thumbnail URI, the RBM platform displays a blank placeholder thumbnail until the user&#39;s device downloads the file. Depending on the user&#39;s setting, the file may not download automatically and may require the user to tap a download button. | [optional] 



## Enum: HeightEnum


* `HEIGHT_UNSPECIFIED` (value: `"HEIGHT_UNSPECIFIED"`)

* `SHORT` (value: `"SHORT"`)

* `MEDIUM` (value: `"MEDIUM"`)

* `TALL` (value: `"TALL"`)




