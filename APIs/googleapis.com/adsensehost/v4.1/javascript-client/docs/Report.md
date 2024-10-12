# AdSenseHostApi.Report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**averages** | **[String]** | The averages of the report. This is the same length as any other row in the report; cells corresponding to dimension columns are empty. | [optional] 
**headers** | [**[ReportHeadersInner]**](ReportHeadersInner.md) | The header information of the columns requested in the report. This is a list of headers; one for each dimension in the request, followed by one for each metric in the request. | [optional] 
**kind** | **String** | Kind this is, in this case adsensehost#report. | [optional] [default to &#39;adsensehost#report&#39;]
**rows** | **[[String]]** | The output rows of the report. Each row is a list of cells; one for each dimension in the request, followed by one for each metric in the request. The dimension cells contain strings, and the metric cells contain numbers. | [optional] 
**totalMatchedRows** | **String** | The total number of rows matched by the report request. Fewer rows may be returned in the response due to being limited by the row count requested or the report row limit. | [optional] 
**totals** | **[String]** | The totals of the report. This is the same length as any other row in the report; cells corresponding to dimension columns are empty. | [optional] 
**warnings** | **[String]** | Any warnings associated with generation of the report. | [optional] 


