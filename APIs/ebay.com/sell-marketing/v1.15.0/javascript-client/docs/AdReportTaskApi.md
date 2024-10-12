# MarketingApi.AdReportTaskApi

All URIs are relative to *https://api.ebay.com/sell/marketing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createReportTask**](AdReportTaskApi.md#createReportTask) | **POST** /ad_report_task | 
[**deleteReportTask**](AdReportTaskApi.md#deleteReportTask) | **DELETE** /ad_report_task/{report_task_id} | 
[**getReportTask**](AdReportTaskApi.md#getReportTask) | **GET** /ad_report_task/{report_task_id} | 
[**getReportTasks**](AdReportTaskApi.md#getReportTasks) | **GET** /ad_report_task | 



## createReportTask

> createReportTask(createReportTask)



&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; Using multiple funding models in one report is deprecated. If multiple funding models are used, a Warning will be returned in a header. This functionality will be decommissioned on April 3, 2023. See &lt;a href&#x3D;\&quot;/develop/apis/api-deprecation-status\&quot;&gt;API Deprecation Status&lt;/a&gt; for details.&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;This method creates a &lt;i&gt;report task&lt;/i&gt;, which generates a Promoted Listings report based on the values specified in the call.&lt;br /&gt;&lt;br /&gt;The report is generated based on the criteria you specify, including the report type, the report&#39;s dimensions and metrics, the report&#39;s start and end dates, the listings to include in the report, and more. &lt;i&gt;Metrics &lt;/i&gt;are the quantitative measurements in the report while &lt;i&gt;dimensions&lt;/i&gt; specify the attributes of the data included in the reports.&lt;br /&gt;&lt;br /&gt;When creating a report task, you can specify the items you want included in the report. The items you specify, using either &lt;b&gt;listingId&lt;/b&gt; or &lt;b&gt;inventoryReference&lt;/b&gt; values, must be in a Promoted Listings campaign for them to be included in the report.&lt;br /&gt;&lt;br /&gt;For details on the required and optional fields for each report type, see &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-reports.html\&quot;&gt;Promoted Listings reporting&lt;/a&gt;.&lt;br /&gt;&lt;br /&gt;This call returns the URL to the report task in the &lt;b&gt;Location&lt;/b&gt; response header, and the URL includes the report-task ID.&lt;br /&gt;&lt;br /&gt;Reports often take time to generate and it&#39;s common for this call to return an HTTP status of &lt;code&gt;202&lt;/code&gt;, which indicates the report is being generated. Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad_report_task/methods/getReportTasks\&quot;&gt;getReportTasks&lt;/a&gt; (or &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad_report_task/methods/getReportTask\&quot;&gt;getReportTask&lt;/a&gt; with the report-task ID) to determine the status of a Promoted Listings report. When a report is complete, eBay sets its status to &lt;b&gt;SUCCESS&lt;/b&gt; and you can download it using the URL returned in the &lt;b&gt;reportHref&lt;/b&gt; field of the &lt;b&gt;getReportTask&lt;/b&gt; call. Report files are tab-separated value gzip files with a file extension of &lt;code&gt;.tsv.gz&lt;/code&gt;.&lt;br/&gt;&lt;br/&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; The reporting of some data related to sales and ad-fees may require a 72-hour (&lt;b&gt;maximum&lt;/b&gt;) adjustment period which is often referred to as the &lt;i&gt;Reconciliation Period&lt;/i&gt;. Such adjustment periods should, on average, be minimal. However, at any given time, the &lt;b&gt;payments&lt;/b&gt; tab may be used to view those amounts that have actually been charged.&lt;/span&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#004680\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt;&lt;/span&gt; This call fails if you don&#39;t submit all the required fields for the specified report type. Fields not supported by the specified report type are ignored. Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad_report_metadata/methods/getReportMetadata\&quot;&gt;getReportMetadata&lt;/a&gt; to retrieve a list of the fields you need to configure for each Promoted Listings report type.&lt;/span&gt;&lt;br/&gt;&lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt;For &lt;b&gt;ad_report&lt;/b&gt; and &lt;b&gt;ad_report_task&lt;/b&gt; methods, the API call limit is subject to a per user quota. These API calls can &lt;b&gt;only&lt;/b&gt; be executed a maximum of 200 times per hour for each seller/user. If the number of calls per hour exceeds this limit, any new calls will be blocked for the next hour.&lt;/p&gt;&lt;/div&gt;

### Example

```javascript
import MarketingApi from 'marketing_api';
let defaultClient = MarketingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MarketingApi.AdReportTaskApi();
let createReportTask = new MarketingApi.CreateReportTask(); // CreateReportTask | The container for the fields that define the report task.
apiInstance.createReportTask(createReportTask, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createReportTask** | [**CreateReportTask**](CreateReportTask.md)| The container for the fields that define the report task. | 

### Return type

null (empty response body)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteReportTask

> deleteReportTask(reportTaskId)



This call deletes the report task specified by the &lt;b&gt;report_task_id&lt;/b&gt; path parameter. This method also deletes any reports generated by the report task.  &lt;p&gt;Report task IDs are generated by eBay when you call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad_report_task/methods/createReportTask\&quot;&gt;createReportTask&lt;/a&gt;. Get a complete list of a seller&#39;s report-task IDs by calling &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad_report_task/methods/getReportTasks\&quot;&gt;getReportTasks&lt;/a&gt;.&lt;/p&gt;&lt;br/&gt;&lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt;For &lt;b&gt;ad_report&lt;/b&gt; and &lt;b&gt;ad_report_task&lt;/b&gt; methods, the API call limit is subject to a per user quota. These API calls can &lt;b&gt;only&lt;/b&gt; be executed a maximum of 200 times per hour for each seller/user. If the number of calls per hour exceeds this limit, any new calls will be blocked for the next hour.&lt;/p&gt;&lt;/div&gt;

### Example

```javascript
import MarketingApi from 'marketing_api';
let defaultClient = MarketingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MarketingApi.AdReportTaskApi();
let reportTaskId = "reportTaskId_example"; // String | A unique eBay-assigned ID for the report task that's generated when the report task is created by a call to <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/createReportTask\">createReportTask</a>.
apiInstance.deleteReportTask(reportTaskId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reportTaskId** | **String**| A unique eBay-assigned ID for the report task that&#39;s generated when the report task is created by a call to &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad_report_task/methods/createReportTask\&quot;&gt;createReportTask&lt;/a&gt;. | 

### Return type

null (empty response body)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getReportTask

> ReportTask getReportTask(reportTaskId)



This call returns the details of a specific Promoted Listings report task, as specified by the &lt;b&gt;report_task_id&lt;/b&gt; path parameter. &lt;p&gt;The report task includes the report criteria (such as the report dimensions, metrics, and included listing) and the report-generation rules (such as starting and ending dates for the specified report task).&lt;/p&gt;  &lt;p&gt;Report-task IDs are generated by eBay when you call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad_report_task/methods/createReportTask\&quot;&gt;createReportTask&lt;/a&gt;. Get a complete list of a seller&#39;s report-task IDs by calling &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad_report_task/methods/getReportTasks\&quot;&gt;getReportTasks&lt;/a&gt;.&lt;/p&gt;&lt;br/&gt;&lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt;For &lt;b&gt;ad_report&lt;/b&gt; and &lt;b&gt;ad_report_task&lt;/b&gt; methods, the API call limit is subject to a per user quota. These API calls can &lt;b&gt;only&lt;/b&gt; be executed a maximum of 200 times per hour for each seller/user. If the number of calls per hour exceeds this limit, any new calls will be blocked for the next hour.&lt;/p&gt;&lt;/div&gt;

### Example

```javascript
import MarketingApi from 'marketing_api';
let defaultClient = MarketingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MarketingApi.AdReportTaskApi();
let reportTaskId = "reportTaskId_example"; // String | A unique eBay-assigned ID for the report task that's generated when the report task is created by a call to <a href=\"/api-docs/sell/marketing/resources/ad_report_task/methods/createReportTask\">createReportTask</a>.
apiInstance.getReportTask(reportTaskId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reportTaskId** | **String**| A unique eBay-assigned ID for the report task that&#39;s generated when the report task is created by a call to &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad_report_task/methods/createReportTask\&quot;&gt;createReportTask&lt;/a&gt;. | 

### Return type

[**ReportTask**](ReportTask.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportTasks

> ReportTaskPagedCollection getReportTasks(opts)



This method returns information on all the existing report tasks related to a seller. &lt;p&gt;Use the &lt;b&gt;report_task_statuses&lt;/b&gt; query parameter to control which reports to return. You can paginate the result set by specifying a &lt;b&gt;limit&lt;/b&gt;, which dictates how many report tasks to return on each page of the response. Use the &lt;b&gt;offset&lt;/b&gt; parameter to specify how many reports to skip in the result set before returning the first result.&lt;/p&gt;&lt;br/&gt;&lt;div class&#x3D;\&quot;msgbox_important\&quot;&gt;&lt;p class&#x3D;\&quot;msgbox_importantInDiv\&quot; data-mc-autonum&#x3D;\&quot;&amp;lt;b&amp;gt;&amp;lt;span style&#x3D;&amp;quot;color: #dd1e31;&amp;quot; class&#x3D;&amp;quot;mcFormatColor&amp;quot;&amp;gt;Important! &amp;lt;/span&amp;gt;&amp;lt;/b&amp;gt;\&quot;&gt;&lt;span class&#x3D;\&quot;autonumber\&quot;&gt;&lt;span&gt;&lt;b&gt;&lt;span style&#x3D;\&quot;color: #dd1e31;\&quot; class&#x3D;\&quot;mcFormatColor\&quot;&gt;Important!&lt;/span&gt;&lt;/b&gt;&lt;/span&gt;&lt;/span&gt;For &lt;b&gt;ad_report&lt;/b&gt; and &lt;b&gt;ad_report_task&lt;/b&gt; methods, the API call limit is subject to a per user quota. These API calls can &lt;b&gt;only&lt;/b&gt; be executed a maximum of 200 times per hour for each seller/user. If the number of calls per hour exceeds this limit, any new calls will be blocked for the next hour.&lt;/p&gt;&lt;/div&gt;

### Example

```javascript
import MarketingApi from 'marketing_api';
let defaultClient = MarketingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MarketingApi.AdReportTaskApi();
let opts = {
  'limit': "limit_example", // String | Specifies the maximum number of report tasks to return on a page in the paginated response.  <p><b>Default:</b> 10<br><b>Maximum:</b> 500</p>
  'offset': "offset_example", // String | Specifies the number of report tasks to skip in the result set before returning the first report in the paginated response.  <p>Combine <b>offset</b> with the <b>limit</b> query parameter to control the reports returned in the response. For example, if you supply an <b>offset</b> of <code>0</code> and a <b>limit</b> of <code>10</code>, the response contains the first 10 reports from the complete list of report tasks retrieved by the call. If <b>offset</b> is <code>10</code> and <b>limit</b> is <code>10</code>, the first page of the response contains reports 11-20 from the complete result set.</p> <b>Default:</b> 0
  'reportTaskStatuses': "reportTaskStatuses_example" // String | This parameter filters the returned report tasks by their status. Supply a comma-separated list of the report statuses you want returned. The results are filtered to include only the report statuses you specify.<br /><br /><span class=\"tablenote\"><span style=\"color:#004680\"><strong>Note:</strong></span> The results might not include some report tasks if other search conditions exclude them.</span><br /><br /><b>Valid values: </b> <br>&nbsp;&nbsp;&nbsp;<code>PENDING</code> <br>&nbsp;&nbsp;&nbsp;<code>SUCCESS</code> <br>&nbsp;&nbsp;&nbsp;<code>FAILED</code>
};
apiInstance.getReportTasks(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **String**| Specifies the maximum number of report tasks to return on a page in the paginated response.  &lt;p&gt;&lt;b&gt;Default:&lt;/b&gt; 10&lt;br&gt;&lt;b&gt;Maximum:&lt;/b&gt; 500&lt;/p&gt; | [optional] 
 **offset** | **String**| Specifies the number of report tasks to skip in the result set before returning the first report in the paginated response.  &lt;p&gt;Combine &lt;b&gt;offset&lt;/b&gt; with the &lt;b&gt;limit&lt;/b&gt; query parameter to control the reports returned in the response. For example, if you supply an &lt;b&gt;offset&lt;/b&gt; of &lt;code&gt;0&lt;/code&gt; and a &lt;b&gt;limit&lt;/b&gt; of &lt;code&gt;10&lt;/code&gt;, the response contains the first 10 reports from the complete list of report tasks retrieved by the call. If &lt;b&gt;offset&lt;/b&gt; is &lt;code&gt;10&lt;/code&gt; and &lt;b&gt;limit&lt;/b&gt; is &lt;code&gt;10&lt;/code&gt;, the first page of the response contains reports 11-20 from the complete result set.&lt;/p&gt; &lt;b&gt;Default:&lt;/b&gt; 0 | [optional] 
 **reportTaskStatuses** | **String**| This parameter filters the returned report tasks by their status. Supply a comma-separated list of the report statuses you want returned. The results are filtered to include only the report statuses you specify.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#004680\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt;&lt;/span&gt; The results might not include some report tasks if other search conditions exclude them.&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Valid values: &lt;/b&gt; &lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;code&gt;PENDING&lt;/code&gt; &lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;code&gt;SUCCESS&lt;/code&gt; &lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;code&gt;FAILED&lt;/code&gt; | [optional] 

### Return type

[**ReportTaskPagedCollection**](ReportTaskPagedCollection.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

