

# AdminRecordingsStartPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**captureHeaders** | [**Map&lt;String, AdminRecordingsSnapshotPostRequestAllOfCaptureHeadersValue&gt;**](AdminRecordingsSnapshotPostRequestAllOfCaptureHeadersValue.md) | Headers from the request to include in the generated stub mappings, mapped to parameter objects. The only parameter available is \&quot;caseInsensitive\&quot;, which defaults to false |  [optional] |
|**extractBodyCriteria** | [**AdminRecordingsSnapshotPostRequestAllOfExtractBodyCriteria**](AdminRecordingsSnapshotPostRequestAllOfExtractBodyCriteria.md) |  |  [optional] |
|**persist** | **Boolean** | Whether to save stub mappings to the file system or just return them |  [optional] |
|**repeatsAsScenarios** | **Boolean** | When true, duplicate requests will be added to a Scenario. When false, duplicates are discarded |  [optional] |
|**requestBodyPattern** | [**AdminRecordingsSnapshotPostRequestAllOfRequestBodyPattern**](AdminRecordingsSnapshotPostRequestAllOfRequestBodyPattern.md) |  |  [optional] |
|**transformerParameters** | **Object** | List of names of stub mappings transformers to apply to generated stubs |  [optional] |
|**transformers** | **List&lt;String&gt;** | Parameters to pass to stub mapping transformers |  [optional] |
|**filters** | [**AdminRecordingsStartPostRequestAllOfFilters**](AdminRecordingsStartPostRequestAllOfFilters.md) |  |  [optional] |
|**targetBaseUrl** | **String** | Target URL when using the record and playback API |  [optional] |



