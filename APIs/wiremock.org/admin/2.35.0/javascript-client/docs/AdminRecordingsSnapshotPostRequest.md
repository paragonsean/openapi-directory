# WireMock.AdminRecordingsSnapshotPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captureHeaders** | [**{String: AdminRecordingsSnapshotPostRequestAllOfCaptureHeadersValue}**](AdminRecordingsSnapshotPostRequestAllOfCaptureHeadersValue.md) | Headers from the request to include in the generated stub mappings, mapped to parameter objects. The only parameter available is \&quot;caseInsensitive\&quot;, which defaults to false | [optional] 
**extractBodyCriteria** | [**AdminRecordingsSnapshotPostRequestAllOfExtractBodyCriteria**](AdminRecordingsSnapshotPostRequestAllOfExtractBodyCriteria.md) |  | [optional] 
**persist** | **Boolean** | Whether to save stub mappings to the file system or just return them | [optional] [default to true]
**repeatsAsScenarios** | **Boolean** | When true, duplicate requests will be added to a Scenario. When false, duplicates are discarded | [optional] [default to true]
**requestBodyPattern** | [**AdminRecordingsSnapshotPostRequestAllOfRequestBodyPattern**](AdminRecordingsSnapshotPostRequestAllOfRequestBodyPattern.md) |  | [optional] 
**transformerParameters** | **Object** | List of names of stub mappings transformers to apply to generated stubs | [optional] 
**transformers** | **[String]** | Parameters to pass to stub mapping transformers | [optional] 
**filters** | [**AdminRecordingsSnapshotPostRequestAllOfFilters**](AdminRecordingsSnapshotPostRequestAllOfFilters.md) |  | [optional] 


