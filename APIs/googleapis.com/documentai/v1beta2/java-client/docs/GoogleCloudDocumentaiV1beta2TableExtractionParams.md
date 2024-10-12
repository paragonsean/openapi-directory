

# GoogleCloudDocumentaiV1beta2TableExtractionParams

Parameters to control table extraction behavior.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether to enable table extraction. |  [optional] |
|**headerHints** | **List&lt;String&gt;** | Optional. Reserved for future use. |  [optional] |
|**modelVersion** | **String** | Model version of the table extraction system. Default is \&quot;builtin/stable\&quot;. Specify \&quot;builtin/latest\&quot; for the latest model. |  [optional] |
|**tableBoundHints** | [**List&lt;GoogleCloudDocumentaiV1beta2TableBoundHint&gt;**](GoogleCloudDocumentaiV1beta2TableBoundHint.md) | Optional. Table bounding box hints that can be provided to complex cases which our algorithm cannot locate the table(s) in. |  [optional] |



