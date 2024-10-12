

# DscNodeReport

Definition of the dsc node report type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configurationVersion** | **String** | Gets or sets the configurationVersion of the node report. |  [optional] |
|**endTime** | **OffsetDateTime** | Gets or sets the end time of the node report. |  [optional] |
|**errors** | [**List&lt;DscReportError&gt;**](DscReportError.md) | Gets or sets the errors for the node report. |  [optional] |
|**hostName** | **String** | Gets or sets the hostname of the node that sent the report. |  [optional] |
|**iPV4Addresses** | **List&lt;String&gt;** | Gets or sets the IPv4 address of the node that sent the report. |  [optional] |
|**iPV6Addresses** | **List&lt;String&gt;** | Gets or sets the IPv6 address of the node that sent the report. |  [optional] |
|**id** | **String** | Gets or sets the id. |  [optional] |
|**lastModifiedTime** | **OffsetDateTime** | Gets or sets the lastModifiedTime of the node report. |  [optional] |
|**metaConfiguration** | [**DscMetaConfiguration**](DscMetaConfiguration.md) |  |  [optional] |
|**numberOfResources** | **Integer** | Gets or sets the number of resource in the node report. |  [optional] |
|**rawErrors** | **String** | Gets or sets the unparsed errors for the node report. |  [optional] |
|**rebootRequested** | **String** | Gets or sets the rebootRequested of the node report. |  [optional] |
|**refreshMode** | **String** | Gets or sets the refreshMode of the node report. |  [optional] |
|**reportFormatVersion** | **String** | Gets or sets the reportFormatVersion of the node report. |  [optional] |
|**reportId** | **String** | Gets or sets the id of the node report. |  [optional] |
|**resources** | [**List&lt;DscReportResource&gt;**](DscReportResource.md) | Gets or sets the resource for the node report. |  [optional] |
|**startTime** | **OffsetDateTime** | Gets or sets the start time of the node report. |  [optional] |
|**status** | **String** | Gets or sets the status of the node report. |  [optional] |
|**type** | **String** | Gets or sets the type of the node report. |  [optional] |



