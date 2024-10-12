

# GoogleCloudApigeeV1SecurityReportResultMetadata

Contains informations about the security report results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expires** | **String** | Output only. Expire_time is set to 7 days after report creation. Query result will be unaccessable after this time. Example: \&quot;2021-05-04T13:38:52-07:00\&quot; |  [optional] [readonly] |
|**self** | **String** | Self link of the query results. Example: &#x60;/organizations/myorg/environments/myenv/securityReports/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd/result&#x60; or following format if query is running at host level: &#x60;/organizations/myorg/hostSecurityReports/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd/result&#x60; |  [optional] |



