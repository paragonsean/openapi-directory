# FeedApi.ScheduleApi

All URIs are relative to *https://api.ebay.com/sell/feed/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSchedule**](ScheduleApi.md#createSchedule) | **POST** /schedule | 
[**deleteSchedule**](ScheduleApi.md#deleteSchedule) | **DELETE** /schedule/{schedule_id} | 
[**getLatestResultFile**](ScheduleApi.md#getLatestResultFile) | **GET** /schedule/{schedule_id}/download_result_file | 
[**getSchedule**](ScheduleApi.md#getSchedule) | **GET** /schedule/{schedule_id} | 
[**getScheduleTemplate**](ScheduleApi.md#getScheduleTemplate) | **GET** /schedule_template/{schedule_template_id} | 
[**getScheduleTemplates**](ScheduleApi.md#getScheduleTemplates) | **GET** /schedule_template | 
[**getSchedules**](ScheduleApi.md#getSchedules) | **GET** /schedule | 
[**updateSchedule**](ScheduleApi.md#updateSchedule) | **PUT** /schedule/{schedule_id} | 



## createSchedule

> Object createSchedule(createUserScheduleRequest)



This method creates a schedule, which is a subscription to the specified schedule template. A schedule periodically generates a report for the &lt;strong&gt;feedType&lt;/strong&gt; specified by the template. Specify the same &lt;strong&gt;feedType&lt;/strong&gt; as the &lt;strong&gt;feedType&lt;/strong&gt; of the associated schedule template. When creating the schedule, if available from the template, you can specify a preferred trigger hour, day of the week, or day of the month. These and other fields are conditionally available as specified by the template.&lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; Make sure to include all fields required by the schedule template (&lt;strong&gt;scheduleTemplateId&lt;/strong&gt;). Call the &lt;strong&gt;getScheduleTemplate&lt;/strong&gt; method (or the &lt;strong&gt;getScheduleTemplates&lt;/strong&gt; method), to find out which fields are required or optional. If a field is optional and a default value is provided by the template, the default value will be used if omitted from the payload.&lt;/span&gt;&lt;/p&gt;A successful call returns the location response header containing the &lt;strong&gt;getSchedule&lt;/strong&gt; call URI to retrieve the schedule you just created. The URL includes the eBay-assigned schedule ID, which you can use to reference the schedule task. &lt;br /&gt;&lt;br /&gt;To retrieve the details of the create schedule task, use the &lt;strong&gt;getSchedule&lt;/strong&gt; method for a single schedule ID or the &lt;strong&gt;getSchedules&lt;/strong&gt; method to retrieve all schedule details for the specified &lt;strong&gt;feed_type&lt;/strong&gt;. The number of schedules for each feedType is limited. Error code 160031 is returned when you have reached this maximum.&lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; Except for schedules with a HALF-HOUR frequency, all schedules will ideally run at the start of each hour (&#39;00&#39; minutes). Actual start time may vary time may vary due to load and other factors.&lt;/span&gt;&lt;/p&gt;

### Example

```javascript
import FeedApi from 'feed_api';
let defaultClient = FeedApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FeedApi.ScheduleApi();
let createUserScheduleRequest = new FeedApi.CreateUserScheduleRequest(); // CreateUserScheduleRequest | In the request payload: <strong>feedType</strong> and <strong>scheduleTemplateId</strong> are required; <strong>scheduleName</strong> is optional; <strong>preferredTriggerHour</strong>, <strong>preferredTriggerDayOfWeek</strong>, <strong>preferredTriggerDayOfMonth</strong>, <strong>scheduleStartDate</strong>, <strong>scheduleEndDate</strong>, and <strong>schemaVersion</strong> are conditional.
apiInstance.createSchedule(createUserScheduleRequest, (error, data, response) => {
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
 **createUserScheduleRequest** | [**CreateUserScheduleRequest**](CreateUserScheduleRequest.md)| In the request payload: &lt;strong&gt;feedType&lt;/strong&gt; and &lt;strong&gt;scheduleTemplateId&lt;/strong&gt; are required; &lt;strong&gt;scheduleName&lt;/strong&gt; is optional; &lt;strong&gt;preferredTriggerHour&lt;/strong&gt;, &lt;strong&gt;preferredTriggerDayOfWeek&lt;/strong&gt;, &lt;strong&gt;preferredTriggerDayOfMonth&lt;/strong&gt;, &lt;strong&gt;scheduleStartDate&lt;/strong&gt;, &lt;strong&gt;scheduleEndDate&lt;/strong&gt;, and &lt;strong&gt;schemaVersion&lt;/strong&gt; are conditional. | 

### Return type

**Object**

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSchedule

> deleteSchedule(scheduleId)



This method deletes an existing schedule. Specify the schedule to delete using the &lt;strong&gt;schedule_id&lt;/strong&gt; path parameter.

### Example

```javascript
import FeedApi from 'feed_api';
let defaultClient = FeedApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FeedApi.ScheduleApi();
let scheduleId = "scheduleId_example"; // String | The <strong>schedule_id</strong> of the schedule to delete. This ID was generated when the task was created. If you do not know the schedule_id, use the <strong>getSchedules</strong> method to return all schedules based on a specified feed_type and find the schedule_id of the schedule to delete.
apiInstance.deleteSchedule(scheduleId, (error, data, response) => {
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
 **scheduleId** | **String**| The &lt;strong&gt;schedule_id&lt;/strong&gt; of the schedule to delete. This ID was generated when the task was created. If you do not know the schedule_id, use the &lt;strong&gt;getSchedules&lt;/strong&gt; method to return all schedules based on a specified feed_type and find the schedule_id of the schedule to delete. | 

### Return type

null (empty response body)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getLatestResultFile

> Object getLatestResultFile(scheduleId)



This method downloads the latest result file generated by the schedule. The response of this call is a compressed or uncompressed CSV, XML, or JSON file, with the applicable file extension (for example: csv.gz). Specify the &lt;strong&gt;schedule_id&lt;/strong&gt; path parameter to download its last generated file.

### Example

```javascript
import FeedApi from 'feed_api';
let defaultClient = FeedApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FeedApi.ScheduleApi();
let scheduleId = "scheduleId_example"; // String | The ID of the schedule for which to retrieve the latest result file. This ID is generated when the schedule was created by the <strong>createSchedule</strong> method.
apiInstance.getLatestResultFile(scheduleId, (error, data, response) => {
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
 **scheduleId** | **String**| The ID of the schedule for which to retrieve the latest result file. This ID is generated when the schedule was created by the &lt;strong&gt;createSchedule&lt;/strong&gt; method. | 

### Return type

**Object**

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getSchedule

> UserScheduleResponse getSchedule(scheduleId)



This method retrieves schedule details and status of the specified schedule. Specify the schedule to retrieve using the &lt;strong&gt;schedule_id&lt;/strong&gt;. Use the &lt;strong&gt;getSchedules&lt;/strong&gt; method to find a schedule if you do not know the &lt;strong&gt;schedule_id&lt;/strong&gt;.

### Example

```javascript
import FeedApi from 'feed_api';
let defaultClient = FeedApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FeedApi.ScheduleApi();
let scheduleId = "scheduleId_example"; // String | The ID of the schedule for which to retrieve the details. This ID is generated when the schedule was created by the <strong>createSchedule</strong> method.
apiInstance.getSchedule(scheduleId, (error, data, response) => {
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
 **scheduleId** | **String**| The ID of the schedule for which to retrieve the details. This ID is generated when the schedule was created by the &lt;strong&gt;createSchedule&lt;/strong&gt; method. | 

### Return type

[**UserScheduleResponse**](UserScheduleResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getScheduleTemplate

> ScheduleTemplateResponse getScheduleTemplate(scheduleTemplateId)



This method retrieves the details of the specified template. Specify the template to retrieve using the &lt;strong&gt;schedule_template_id&lt;/strong&gt; path parameter. Use the &lt;strong&gt;getScheduleTemplates&lt;/strong&gt; method to find a schedule template if you do not know the &lt;strong&gt;schedule_template_id&lt;/strong&gt;.

### Example

```javascript
import FeedApi from 'feed_api';
let defaultClient = FeedApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FeedApi.ScheduleApi();
let scheduleTemplateId = "scheduleTemplateId_example"; // String | The ID of the template to retrieve. If you do not know the <strong>schedule_template_id</strong>, refer to the documentation or use the <strong>getScheduleTemplates</strong> method to find the available schedule templates.
apiInstance.getScheduleTemplate(scheduleTemplateId, (error, data, response) => {
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
 **scheduleTemplateId** | **String**| The ID of the template to retrieve. If you do not know the &lt;strong&gt;schedule_template_id&lt;/strong&gt;, refer to the documentation or use the &lt;strong&gt;getScheduleTemplates&lt;/strong&gt; method to find the available schedule templates. | 

### Return type

[**ScheduleTemplateResponse**](ScheduleTemplateResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getScheduleTemplates

> ScheduleTemplateCollection getScheduleTemplates(feedType, opts)



This method retrieves an array containing the details and status of all schedule templates based on the specified &lt;strong&gt;feed_type&lt;/strong&gt;. Use this method to find a schedule template if you do not know the &lt;strong&gt;schedule_template_id&lt;/strong&gt;.

### Example

```javascript
import FeedApi from 'feed_api';
let defaultClient = FeedApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FeedApi.ScheduleApi();
let feedType = "feedType_example"; // String | The feed type of the schedule templates to retrieve.
let opts = {
  'limit': "limit_example", // String | The maximum number of schedule templates that can be returned on each page of the paginated response. Use this parameter in conjunction with the <strong>offset</strong> parameter to control the pagination of the output. <p> <span class=\"tablenote\"><strong>Note:</strong> This feature employs a zero-based list, where the first item in the list has an offset of <code>0</code>.</span></p><p>For example, if <strong>offset</strong> is set to 10 and <strong>limit</strong> is set to 10, the call retrieves schedule templates 11 thru 20 from the result set.</p><p>If this parameter is omitted, the default value is used. <br /><br /><b>Default: </b> 10 <br /><br /><b>Maximum: </b>500
  'offset': "offset_example" // String | The number of schedule templates to skip in the result set before returning the first template in the paginated response. <p>Combine <strong>offset</strong> with the <strong>limit</strong> query parameter to control the items returned in the response. For example, if you supply an <strong>offset</strong> of <code>0</code> and a <strong>limit</strong> of <code>10</code>, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If <strong>offset</strong> is <code>10</code> and <strong>limit</strong> is <code>20</code>, the first page of the response contains items 11-30 from the complete result set. If this query parameter is not set, the default value is used and the first page of records is returned.<br /><br /><b>Default: </b>0
};
apiInstance.getScheduleTemplates(feedType, opts, (error, data, response) => {
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
 **feedType** | **String**| The feed type of the schedule templates to retrieve. | 
 **limit** | **String**| The maximum number of schedule templates that can be returned on each page of the paginated response. Use this parameter in conjunction with the &lt;strong&gt;offset&lt;/strong&gt; parameter to control the pagination of the output. &lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; This feature employs a zero-based list, where the first item in the list has an offset of &lt;code&gt;0&lt;/code&gt;.&lt;/span&gt;&lt;/p&gt;&lt;p&gt;For example, if &lt;strong&gt;offset&lt;/strong&gt; is set to 10 and &lt;strong&gt;limit&lt;/strong&gt; is set to 10, the call retrieves schedule templates 11 thru 20 from the result set.&lt;/p&gt;&lt;p&gt;If this parameter is omitted, the default value is used. &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default: &lt;/b&gt; 10 &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Maximum: &lt;/b&gt;500 | [optional] 
 **offset** | **String**| The number of schedule templates to skip in the result set before returning the first template in the paginated response. &lt;p&gt;Combine &lt;strong&gt;offset&lt;/strong&gt; with the &lt;strong&gt;limit&lt;/strong&gt; query parameter to control the items returned in the response. For example, if you supply an &lt;strong&gt;offset&lt;/strong&gt; of &lt;code&gt;0&lt;/code&gt; and a &lt;strong&gt;limit&lt;/strong&gt; of &lt;code&gt;10&lt;/code&gt;, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If &lt;strong&gt;offset&lt;/strong&gt; is &lt;code&gt;10&lt;/code&gt; and &lt;strong&gt;limit&lt;/strong&gt; is &lt;code&gt;20&lt;/code&gt;, the first page of the response contains items 11-30 from the complete result set. If this query parameter is not set, the default value is used and the first page of records is returned.&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default: &lt;/b&gt;0 | [optional] 

### Return type

[**ScheduleTemplateCollection**](ScheduleTemplateCollection.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSchedules

> UserScheduleCollection getSchedules(feedType, opts)



This method retrieves an array containing the details and status of all schedules based on the specified &lt;strong&gt;feed_type&lt;/strong&gt;. Use this method to find a schedule if you do not know the &lt;strong&gt;schedule_id&lt;/strong&gt;.

### Example

```javascript
import FeedApi from 'feed_api';
let defaultClient = FeedApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FeedApi.ScheduleApi();
let feedType = "feedType_example"; // String | The <strong>feedType</strong> associated with the schedule.
let opts = {
  'limit': "limit_example", // String | The maximum number of schedules that can be returned on each page of the paginated response. Use this parameter in conjunction with the <strong>offset</strong> parameter to control the pagination of the output. <p> <span class=\"tablenote\"><strong>Note:</strong> This feature employs a zero-based list, where the first item in the list has an offset of <code>0</code>.</span></p><p>For example, if <strong>offset</strong> is set to 10 and <strong>limit</strong> is set to 10, the call retrieves schedules 11 thru 20 from the result set.</p><p>If this parameter is omitted, the default value is used. <br /><br /><b>Default: </b> 10 <br /><br /><b>Maximum: </b>500
  'offset': "offset_example" // String | The number of schedules to skip in the result set before returning the first schedule in the paginated response. <p>Combine <strong>offset</strong> with the <strong>limit</strong> query parameter to control the items returned in the response. For example, if you supply an <strong>offset</strong> of <code>0</code> and a <strong>limit</strong> of <code>10</code>, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If <strong>offset</strong> is <code>10</code> and <strong>limit</strong> is <code>20</code>, the first page of the response contains items 11-30 from the complete result set. If this query parameter is not set, the default value is used and the first page of records is returned.<br /><br /><b>Default: </b>0
};
apiInstance.getSchedules(feedType, opts, (error, data, response) => {
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
 **feedType** | **String**| The &lt;strong&gt;feedType&lt;/strong&gt; associated with the schedule. | 
 **limit** | **String**| The maximum number of schedules that can be returned on each page of the paginated response. Use this parameter in conjunction with the &lt;strong&gt;offset&lt;/strong&gt; parameter to control the pagination of the output. &lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; This feature employs a zero-based list, where the first item in the list has an offset of &lt;code&gt;0&lt;/code&gt;.&lt;/span&gt;&lt;/p&gt;&lt;p&gt;For example, if &lt;strong&gt;offset&lt;/strong&gt; is set to 10 and &lt;strong&gt;limit&lt;/strong&gt; is set to 10, the call retrieves schedules 11 thru 20 from the result set.&lt;/p&gt;&lt;p&gt;If this parameter is omitted, the default value is used. &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default: &lt;/b&gt; 10 &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Maximum: &lt;/b&gt;500 | [optional] 
 **offset** | **String**| The number of schedules to skip in the result set before returning the first schedule in the paginated response. &lt;p&gt;Combine &lt;strong&gt;offset&lt;/strong&gt; with the &lt;strong&gt;limit&lt;/strong&gt; query parameter to control the items returned in the response. For example, if you supply an &lt;strong&gt;offset&lt;/strong&gt; of &lt;code&gt;0&lt;/code&gt; and a &lt;strong&gt;limit&lt;/strong&gt; of &lt;code&gt;10&lt;/code&gt;, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If &lt;strong&gt;offset&lt;/strong&gt; is &lt;code&gt;10&lt;/code&gt; and &lt;strong&gt;limit&lt;/strong&gt; is &lt;code&gt;20&lt;/code&gt;, the first page of the response contains items 11-30 from the complete result set. If this query parameter is not set, the default value is used and the first page of records is returned.&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default: &lt;/b&gt;0 | [optional] 

### Return type

[**UserScheduleCollection**](UserScheduleCollection.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSchedule

> updateSchedule(scheduleId, updateUserScheduleRequest)



This method updates an existing schedule. Specify the schedule to update using the &lt;strong&gt;schedule_id&lt;/strong&gt; path parameter. If the schedule template has changed after the schedule was created or updated, the input will be validated using the changed template.&lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; Make sure to include all fields required by the schedule template (&lt;strong&gt;scheduleTemplateId&lt;/strong&gt;). Call the &lt;strong&gt;getScheduleTemplate&lt;/strong&gt; method (or the &lt;strong&gt;getScheduleTemplates&lt;/strong&gt; method), to find out which fields are required or optional. If you do not know the &lt;strong&gt;scheduleTemplateId&lt;/strong&gt;, call the &lt;strong&gt;getSchedule&lt;/strong&gt; method to find out.&lt;/span&gt;&lt;/p&gt;

### Example

```javascript
import FeedApi from 'feed_api';
let defaultClient = FeedApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FeedApi.ScheduleApi();
let scheduleId = "scheduleId_example"; // String | The ID of the schedule to update. This ID is generated when the schedule was created by the <strong>createSchedule</strong> method.
let updateUserScheduleRequest = new FeedApi.UpdateUserScheduleRequest(); // UpdateUserScheduleRequest | In the request payload: <strong>scheduleName</strong> is optional; <strong>preferredTriggerHour</strong>, <strong>preferredTriggerDayOfWeek</strong>, <strong>preferredTriggerDayOfMonth</strong>, <strong>scheduleStartDate</strong>, <strong>scheduleEndDate</strong>, and <strong>schemaVersion</strong> are conditional.
apiInstance.updateSchedule(scheduleId, updateUserScheduleRequest, (error, data, response) => {
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
 **scheduleId** | **String**| The ID of the schedule to update. This ID is generated when the schedule was created by the &lt;strong&gt;createSchedule&lt;/strong&gt; method. | 
 **updateUserScheduleRequest** | [**UpdateUserScheduleRequest**](UpdateUserScheduleRequest.md)| In the request payload: &lt;strong&gt;scheduleName&lt;/strong&gt; is optional; &lt;strong&gt;preferredTriggerHour&lt;/strong&gt;, &lt;strong&gt;preferredTriggerDayOfWeek&lt;/strong&gt;, &lt;strong&gt;preferredTriggerDayOfMonth&lt;/strong&gt;, &lt;strong&gt;scheduleStartDate&lt;/strong&gt;, &lt;strong&gt;scheduleEndDate&lt;/strong&gt;, and &lt;strong&gt;schemaVersion&lt;/strong&gt; are conditional. | 

### Return type

null (empty response body)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

