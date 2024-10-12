

# GoogleCloudApigeeV1SecurityReport

SecurityReport saves all the information about the created security report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **String** | Creation time of the query. |  [optional] |
|**displayName** | **String** | Display Name specified by the user. |  [optional] |
|**envgroupHostname** | **String** | Hostname is available only when query is executed at host level. |  [optional] |
|**error** | **String** | Error is set when query fails. |  [optional] |
|**executionTime** | **String** | ExecutionTime is available only after the query is completed. |  [optional] |
|**queryParams** | [**GoogleCloudApigeeV1SecurityReportMetadata**](GoogleCloudApigeeV1SecurityReportMetadata.md) |  |  [optional] |
|**reportDefinitionId** | **String** | Report Definition ID. |  [optional] |
|**result** | [**GoogleCloudApigeeV1SecurityReportResultMetadata**](GoogleCloudApigeeV1SecurityReportResultMetadata.md) |  |  [optional] |
|**resultFileSize** | **String** | ResultFileSize is available only after the query is completed. |  [optional] |
|**resultRows** | **String** | ResultRows is available only after the query is completed. |  [optional] |
|**self** | **String** | Self link of the query. Example: &#x60;/organizations/myorg/environments/myenv/securityReports/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd&#x60; or following format if query is running at host level: &#x60;/organizations/myorg/hostSecurityReports/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd&#x60; |  [optional] |
|**state** | **String** | Query state could be \&quot;enqueued\&quot;, \&quot;running\&quot;, \&quot;completed\&quot;, \&quot;expired\&quot; and \&quot;failed\&quot;. |  [optional] |
|**updated** | **String** | Output only. Last updated timestamp for the query. |  [optional] [readonly] |



