# AnalyticsReportingApi.GetReportsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reportRequests** | [**[ReportRequest]**](ReportRequest.md) | Requests, each request will have a separate response. There can be a maximum of 5 requests. All requests should have the same &#x60;dateRanges&#x60;, &#x60;viewId&#x60;, &#x60;segments&#x60;, &#x60;samplingLevel&#x60;, and &#x60;cohortGroup&#x60;. | [optional] 
**useResourceQuotas** | **Boolean** | Enables [resource based quotas](/analytics/devguides/reporting/core/v4/limits-quotas#analytics_reporting_api_v4), (defaults to &#x60;False&#x60;). If this field is set to &#x60;True&#x60; the per view (profile) quotas are governed by the computational cost of the request. Note that using cost based quotas will higher enable sampling rates. (10 Million for &#x60;SMALL&#x60;, 100M for &#x60;LARGE&#x60;. See the [limits and quotas documentation](/analytics/devguides/reporting/core/v4/limits-quotas#analytics_reporting_api_v4) for details. | [optional] 


