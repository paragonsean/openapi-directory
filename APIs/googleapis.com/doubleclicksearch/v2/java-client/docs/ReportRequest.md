

# ReportRequest

A request object used to create a DoubleClick Search report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columns** | [**List&lt;ReportApiColumnSpec&gt;**](ReportApiColumnSpec.md) | The columns to include in the report. This includes both DoubleClick Search columns and saved columns. For DoubleClick Search columns, only the &#x60;columnName&#x60; parameter is required. For saved columns only the &#x60;savedColumnName&#x60; parameter is required. Both &#x60;columnName&#x60; and &#x60;savedColumnName&#x60; cannot be set in the same stanza.\\ The maximum number of columns per request is 300. |  [optional] |
|**downloadFormat** | **String** | Format that the report should be returned in. Currently &#x60;csv&#x60; or &#x60;tsv&#x60; is supported. |  [optional] |
|**filters** | [**List&lt;ReportRequestFiltersInner&gt;**](ReportRequestFiltersInner.md) | A list of filters to be applied to the report.\\ The maximum number of filters per request is 300. |  [optional] |
|**includeDeletedEntities** | **Boolean** | Determines if removed entities should be included in the report. Defaults to &#x60;false&#x60;. Deprecated, please use &#x60;includeRemovedEntities&#x60; instead. |  [optional] |
|**includeRemovedEntities** | **Boolean** | Determines if removed entities should be included in the report. Defaults to &#x60;false&#x60;. |  [optional] |
|**maxRowsPerFile** | **Integer** | Asynchronous report only. The maximum number of rows per report file. A large report is split into many files based on this field. Acceptable values are &#x60;1000000&#x60; to &#x60;100000000&#x60;, inclusive. |  [optional] |
|**orderBy** | [**List&lt;ReportRequestOrderByInner&gt;**](ReportRequestOrderByInner.md) | Synchronous report only. A list of columns and directions defining sorting to be performed on the report rows.\\ The maximum number of orderings per request is 300. |  [optional] |
|**reportScope** | [**ReportRequestReportScope**](ReportRequestReportScope.md) |  |  [optional] |
|**reportType** | **String** | Determines the type of rows that are returned in the report. For example, if you specify &#x60;reportType: keyword&#x60;, each row in the report will contain data about a keyword. See the [Types of Reports](/search-ads/v2/report-types/) reference for the columns that are available for each type. |  [optional] |
|**rowCount** | **Integer** | Synchronous report only. The maximum number of rows to return; additional rows are dropped. Acceptable values are &#x60;0&#x60; to &#x60;10000&#x60;, inclusive. Defaults to &#x60;10000&#x60;. |  [optional] |
|**startRow** | **Integer** | Synchronous report only. Zero-based index of the first row to return. Acceptable values are &#x60;0&#x60; to &#x60;50000&#x60;, inclusive. Defaults to &#x60;0&#x60;. |  [optional] |
|**statisticsCurrency** | **String** | Specifies the currency in which monetary will be returned. Possible values are: &#x60;usd&#x60;, &#x60;agency&#x60; (valid if the report is scoped to agency or lower), &#x60;advertiser&#x60; (valid if the report is scoped to * advertiser or lower), or &#x60;account&#x60; (valid if the report is scoped to engine account or lower). |  [optional] |
|**timeRange** | [**ReportRequestTimeRange**](ReportRequestTimeRange.md) |  |  [optional] |
|**verifySingleTimeZone** | **Boolean** | If &#x60;true&#x60;, the report would only be created if all the requested stat data are sourced from a single timezone. Defaults to &#x60;false&#x60;. |  [optional] |



