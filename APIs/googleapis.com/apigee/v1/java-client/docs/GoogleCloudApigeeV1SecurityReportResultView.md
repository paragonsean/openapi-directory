

# GoogleCloudApigeeV1SecurityReportResultView

The response for security report result view APIs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **Integer** | Error code when there is a failure. |  [optional] |
|**error** | **String** | Error message when there is a failure. |  [optional] |
|**metadata** | [**GoogleCloudApigeeV1SecurityReportMetadata**](GoogleCloudApigeeV1SecurityReportMetadata.md) |  |  [optional] |
|**rows** | **List&lt;Object&gt;** | Rows of security report result. Each row is a JSON object. Example: {sum(message_count): 1, developer_app: \&quot;(not set)\&quot;,…} |  [optional] |
|**state** | **String** | State of retrieving ResultView. |  [optional] |



