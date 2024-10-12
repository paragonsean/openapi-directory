# ApigeeApi.GoogleCloudApigeeV1SecurityReportResultView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **Number** | Error code when there is a failure. | [optional] 
**error** | **String** | Error message when there is a failure. | [optional] 
**metadata** | [**GoogleCloudApigeeV1SecurityReportMetadata**](GoogleCloudApigeeV1SecurityReportMetadata.md) |  | [optional] 
**rows** | **[Object]** | Rows of security report result. Each row is a JSON object. Example: {sum(message_count): 1, developer_app: \&quot;(not set)\&quot;,…} | [optional] 
**state** | **String** | State of retrieving ResultView. | [optional] 


