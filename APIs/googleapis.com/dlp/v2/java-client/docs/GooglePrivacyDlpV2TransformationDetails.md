

# GooglePrivacyDlpV2TransformationDetails

Details about a single transformation. This object contains a description of the transformation, information about whether the transformation was successfully applied, and the precise location where the transformation occurred. These details are stored in a user-specified BigQuery table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerName** | **String** | The top level name of the container where the transformation is located (this will be the source file name or table name). |  [optional] |
|**resourceName** | **String** | The name of the job that completed the transformation. |  [optional] |
|**statusDetails** | [**GooglePrivacyDlpV2TransformationResultStatus**](GooglePrivacyDlpV2TransformationResultStatus.md) |  |  [optional] |
|**transformation** | [**List&lt;GooglePrivacyDlpV2TransformationDescription&gt;**](GooglePrivacyDlpV2TransformationDescription.md) | Description of transformation. This would only contain more than one element if there were multiple matching transformations and which one to apply was ambiguous. Not set for states that contain no transformation, currently only state that contains no transformation is TransformationResultStateType.METADATA_UNRETRIEVABLE. |  [optional] |
|**transformationLocation** | [**GooglePrivacyDlpV2TransformationLocation**](GooglePrivacyDlpV2TransformationLocation.md) |  |  [optional] |
|**transformedBytes** | **String** | The number of bytes that were transformed. If transformation was unsuccessful or did not take place because there was no content to transform, this will be zero. |  [optional] |



