

# GoogleCloudVisionV1p1beta1OutputConfig

The desired output location and metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batchSize** | **Integer** | The max number of response protos to put into each output JSON file on Google Cloud Storage. The valid range is [1, 100]. If not specified, the default value is 20. For example, for one pdf file with 100 pages, 100 response protos will be generated. If &#x60;batch_size&#x60; &#x3D; 20, then 5 json files each containing 20 response protos will be written under the prefix &#x60;gcs_destination&#x60;.&#x60;uri&#x60;. Currently, batch_size only applies to GcsDestination, with potential future support for other output configurations. |  [optional] |
|**gcsDestination** | [**GoogleCloudVisionV1p1beta1GcsDestination**](GoogleCloudVisionV1p1beta1GcsDestination.md) |  |  [optional] |



