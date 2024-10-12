# CloudVisionApi.GoogleCloudVisionV1p2beta1ImageSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcsImageUri** | **String** | **Use &#x60;image_uri&#x60; instead.** The Google Cloud Storage URI of the form &#x60;gs://bucket_name/object_name&#x60;. Object versioning is not supported. See [Google Cloud Storage Request URIs](https://cloud.google.com/storage/docs/reference-uris) for more info. | [optional] 
**imageUri** | **String** | The URI of the source image. Can be either: 1. A Google Cloud Storage URI of the form &#x60;gs://bucket_name/object_name&#x60;. Object versioning is not supported. See [Google Cloud Storage Request URIs](https://cloud.google.com/storage/docs/reference-uris) for more info. 2. A publicly-accessible image HTTP/HTTPS URL. When fetching images from HTTP/HTTPS URLs, Google cannot guarantee that the request will be completed. Your request may fail if the specified host denies the request (e.g. due to request throttling or DOS prevention), or if Google throttles requests to the site for abuse prevention. You should not depend on externally-hosted images for production applications. When both &#x60;gcs_image_uri&#x60; and &#x60;image_uri&#x60; are specified, &#x60;image_uri&#x60; takes precedence. | [optional] 


