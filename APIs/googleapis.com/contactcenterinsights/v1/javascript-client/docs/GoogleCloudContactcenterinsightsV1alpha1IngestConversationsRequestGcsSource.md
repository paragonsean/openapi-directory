# ContactCenterAiInsightsApi.GoogleCloudContactcenterinsightsV1alpha1IngestConversationsRequestGcsSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucketObjectType** | **String** | Optional. Specifies the type of the objects in &#x60;bucket_uri&#x60;. | [optional] 
**bucketUri** | **String** | Required. The Cloud Storage bucket containing source objects. | [optional] 
**customMetadataKeys** | **[String]** | Optional. Custom keys to extract as conversation labels from metadata files in &#x60;metadata_bucket_uri&#x60;. Keys not included in this field will be ignored. Note that there is a limit of 20 labels per conversation. | [optional] 
**metadataBucketUri** | **String** | Optional. The Cloud Storage path to the source object metadata. Note that: [1] metadata files are expected to be in JSON format [2] metadata and source objects must be in separate buckets [3] a source object&#39;s metadata object must share the same name to be properly ingested | [optional] 



## Enum: BucketObjectTypeEnum


* `BUCKET_OBJECT_TYPE_UNSPECIFIED` (value: `"BUCKET_OBJECT_TYPE_UNSPECIFIED"`)

* `TRANSCRIPT` (value: `"TRANSCRIPT"`)

* `AUDIO` (value: `"AUDIO"`)




