

# AnalyzeIamPolicyLongrunningRequest

A request message for AssetService.AnalyzeIamPolicyLongrunning.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analysisQuery** | [**IamPolicyAnalysisQuery**](IamPolicyAnalysisQuery.md) |  |  [optional] |
|**outputConfig** | [**IamPolicyAnalysisOutputConfig**](IamPolicyAnalysisOutputConfig.md) |  |  [optional] |
|**savedAnalysisQuery** | **String** | Optional. The name of a saved query, which must be in the format of: * projects/project_number/savedQueries/saved_query_id * folders/folder_number/savedQueries/saved_query_id * organizations/organization_number/savedQueries/saved_query_id If both &#x60;analysis_query&#x60; and &#x60;saved_analysis_query&#x60; are provided, they will be merged together with the &#x60;saved_analysis_query&#x60; as base and the &#x60;analysis_query&#x60; as overrides. For more details of the merge behavior, refer to the [MergeFrom](https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.message#Message.MergeFrom.details) doc. Note that you cannot override primitive fields with default value, such as 0 or empty string, etc., because we use proto3, which doesn&#39;t support field presence yet. |  [optional] |



