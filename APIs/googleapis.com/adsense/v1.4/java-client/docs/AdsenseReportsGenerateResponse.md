

# AdsenseReportsGenerateResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**averages** | **List&lt;String&gt;** | The averages of the report. This is the same length as any other row in the report; cells corresponding to dimension columns are empty. |  [optional] |
|**endDate** | **String** | The requested end date in yyyy-mm-dd format. |  [optional] |
|**headers** | [**List&lt;AdsenseReportsGenerateResponseHeadersInner&gt;**](AdsenseReportsGenerateResponseHeadersInner.md) | The header information of the columns requested in the report. This is a list of headers; one for each dimension in the request, followed by one for each metric in the request. |  [optional] |
|**kind** | **String** | Kind this is, in this case adsense#report. |  [optional] |
|**rows** | **List&lt;List&lt;String&gt;&gt;** | The output rows of the report. Each row is a list of cells; one for each dimension in the request, followed by one for each metric in the request. The dimension cells contain strings, and the metric cells contain numbers. |  [optional] |
|**startDate** | **String** | The requested start date in yyyy-mm-dd format. |  [optional] |
|**totalMatchedRows** | **String** | The total number of rows matched by the report request. Fewer rows may be returned in the response due to being limited by the row count requested or the report row limit. |  [optional] |
|**totals** | **List&lt;String&gt;** | The totals of the report. This is the same length as any other row in the report; cells corresponding to dimension columns are empty. |  [optional] |
|**warnings** | **List&lt;String&gt;** | Any warnings associated with generation of the report. |  [optional] |



