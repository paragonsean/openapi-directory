

# GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequest

Request message for the TrainProcessorVersion method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseProcessorVersion** | **String** | Optional. The processor version to use as a base for training. This processor version must be a child of &#x60;parent&#x60;. Format: &#x60;projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}&#x60;. |  [optional] |
|**customDocumentExtractionOptions** | [**GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestCustomDocumentExtractionOptions**](GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestCustomDocumentExtractionOptions.md) |  |  [optional] |
|**documentSchema** | [**GoogleCloudDocumentaiV1beta3DocumentSchema**](GoogleCloudDocumentaiV1beta3DocumentSchema.md) |  |  [optional] |
|**foundationModelTuningOptions** | [**GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestFoundationModelTuningOptions**](GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestFoundationModelTuningOptions.md) |  |  [optional] |
|**inputData** | [**GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestInputData**](GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequestInputData.md) |  |  [optional] |
|**processorVersion** | [**GoogleCloudDocumentaiV1beta3ProcessorVersion**](GoogleCloudDocumentaiV1beta3ProcessorVersion.md) |  |  [optional] |



