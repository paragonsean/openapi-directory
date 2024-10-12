# CloudVisionApi.GoogleCloudVisionV1p2beta1BatchAnnotateFilesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **{String: String}** | Optional. The labels with user-defined metadata for the request. Label keys and values can be no longer than 63 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter. | [optional] 
**parent** | **String** | Optional. Target project and location to make a call. Format: &#x60;projects/{project-id}/locations/{location-id}&#x60;. If no parent is specified, a region will be chosen automatically. Supported location-ids: &#x60;us&#x60;: USA country only, &#x60;asia&#x60;: East asia areas, like Japan, Taiwan, &#x60;eu&#x60;: The European Union. Example: &#x60;projects/project-A/locations/eu&#x60;. | [optional] 
**requests** | [**[GoogleCloudVisionV1p2beta1AnnotateFileRequest]**](GoogleCloudVisionV1p2beta1AnnotateFileRequest.md) | Required. The list of file annotation requests. Right now we support only one AnnotateFileRequest in BatchAnnotateFilesRequest. | [optional] 


