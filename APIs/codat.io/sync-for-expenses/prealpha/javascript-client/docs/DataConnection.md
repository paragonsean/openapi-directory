# CodatExpenseApi.DataConnection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalProperties** | **Object** |  | [optional] 
**connectionInfo** | **{String: String}** |  | [optional] 
**created** | **String** | In Codat&#39;s data model, dates and times are represented using the &lt;a class&#x3D;\&quot;external\&quot; href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 8601 standard&lt;/a&gt;. Date and time fields are formatted as strings; for example:  &#x60;&#x60;&#x60; 2020-10-08T22:40:50Z 2021-01-01T00:00:00 &#x60;&#x60;&#x60;    When syncing data that contains &#x60;DateTime&#x60; fields from Codat, make sure you support the following cases when reading time information:  - Coordinated Universal Time (UTC): &#x60;2021-11-15T06:00:00Z&#x60; - Unqualified local time: &#x60;2021-11-15T01:00:00&#x60; - UTC time offsets: &#x60;2021-11-15T01:00:00-05:00&#x60;  &gt; Time zones &gt;  &gt; Not all dates from Codat will contain information about time zones.   &gt; Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced. | 
**dataConnectionErrors** | [**[DataConnectionError]**](DataConnectionError.md) |  | [optional] 
**id** | **String** | Unique identifier for a company&#39;s data connection. | 
**integrationId** | **String** | A Codat ID representing the integration. | 
**integrationKey** | **String** | A unique four-character ID that identifies the platform of the company&#39;s data connection. This ensures continuity if the platform changes its name in the future. | 
**lastSync** | **String** | In Codat&#39;s data model, dates and times are represented using the &lt;a class&#x3D;\&quot;external\&quot; href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 8601 standard&lt;/a&gt;. Date and time fields are formatted as strings; for example:  &#x60;&#x60;&#x60; 2020-10-08T22:40:50Z 2021-01-01T00:00:00 &#x60;&#x60;&#x60;    When syncing data that contains &#x60;DateTime&#x60; fields from Codat, make sure you support the following cases when reading time information:  - Coordinated Universal Time (UTC): &#x60;2021-11-15T06:00:00Z&#x60; - Unqualified local time: &#x60;2021-11-15T01:00:00&#x60; - UTC time offsets: &#x60;2021-11-15T01:00:00-05:00&#x60;  &gt; Time zones &gt;  &gt; Not all dates from Codat will contain information about time zones.   &gt; Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced. | [optional] 
**linkUrl** | **String** |  | 
**platformName** | **String** |  | 
**sourceId** | **String** | A source-specific ID used to distinguish between different sources originating from the same data connection. In general, a data connection is a single data source. However, for TrueLayer, &#x60;sourceId&#x60; is associated with a specific bank and has a many-to-one relationship with the &#x60;integrationId&#x60;. | 
**sourceType** | **String** | The type of platform of the connection. | 
**status** | [**DataConnectionStatus**](DataConnectionStatus.md) |  | 



## Enum: SourceTypeEnum


* `Accounting` (value: `"Accounting"`)

* `Banking` (value: `"Banking"`)

* `Commerce` (value: `"Commerce"`)

* `Other` (value: `"Other"`)

* `Unknown` (value: `"Unknown"`)




