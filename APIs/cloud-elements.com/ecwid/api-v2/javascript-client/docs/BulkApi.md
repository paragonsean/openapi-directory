# Ecwid.BulkApi

All URIs are relative to *https://api.cloud-elements.com/elements/api-v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBulkByObjectName**](BulkApi.md#createBulkByObjectName) | **POST** /bulk/{objectName} | Upload a file of objects to be bulk uploaded to the provider.
[**createBulkDownload**](BulkApi.md#createBulkDownload) | **POST** /bulk/download | Create a new bulk download job (asynchronous)
[**createBulkQuery**](BulkApi.md#createBulkQuery) | **POST** /bulk/query | Create an asynchronous bulk query job.
[**getBulkByObjectName**](BulkApi.md#getBulkByObjectName) | **GET** /bulk/{id}/{objectName} | Retrieve the results of an asynchronous bulk query.
[**getBulkErrors**](BulkApi.md#getBulkErrors) | **GET** /bulk/{id}/errors | Retrieve the errors of a bulk job.
[**getBulkJobs**](BulkApi.md#getBulkJobs) | **GET** /bulk/jobs | Fetch all the bulk jobs for an instance
[**getBulkStatus**](BulkApi.md#getBulkStatus) | **GET** /bulk/{id}/status | Retrieve the status of a bulk job.
[**replaceBulkCancel**](BulkApi.md#replaceBulkCancel) | **PUT** /bulk/{id}/cancel | Cancel an asynchronous bulk query job.



## createBulkByObjectName

> BulkUploadResponse createBulkByObjectName(authorization, objectName, opts)

Upload a file of objects to be bulk uploaded to the provider.

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.BulkApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let objectName = "objectName_example"; // String | The name of the object for which data needs to be uploaded.
let opts = {
  'elementsAsyncCallbackUrl': "elementsAsyncCallbackUrl_example", // String | The Url to send the notification to when the Job is completed
  'metaData': "metaData_example", // String | Optional JSON MetaData that contains callback-payload, path or format, ex: {\\\"path\\\" :&lt;path for the sub resource&gt;, \\\"format\\\": &lt;json/csv&gt;, \\\"callback-payload\\\":&lt;json&gt;}. path - is passed to the endpoint for bulk loading the data into a nested object. Optional JSON Metadata that contains identifierFieldName, action, listId or campaignId. The identifierField name is used for upserts and the optional fields like listId or campaignId. Example: {\\\"listId\\\":\\\"1014\\\",\\\"action\\\":\\\"upsert\\\"}. If the Upload format is JSON pass metadata as {\\\"format\\\":\\\"json\\\"}. callback-payload - is passed back in bulk job notification 
  'file': "/path/to/file" // File | The file of objects to bulk load. If the JSON file upload, each JSON record should be in a single line
};
apiInstance.createBulkByObjectName(authorization, objectName, opts, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **objectName** | **String**| The name of the object for which data needs to be uploaded. | 
 **elementsAsyncCallbackUrl** | **String**| The Url to send the notification to when the Job is completed | [optional] 
 **metaData** | **String**| Optional JSON MetaData that contains callback-payload, path or format, ex: {\\\&quot;path\\\&quot; :&amp;lt;path for the sub resource&amp;gt;, \\\&quot;format\\\&quot;: &amp;lt;json/csv&amp;gt;, \\\&quot;callback-payload\\\&quot;:&amp;lt;json&amp;gt;}. path - is passed to the endpoint for bulk loading the data into a nested object. Optional JSON Metadata that contains identifierFieldName, action, listId or campaignId. The identifierField name is used for upserts and the optional fields like listId or campaignId. Example: {\\\&quot;listId\\\&quot;:\\\&quot;1014\\\&quot;,\\\&quot;action\\\&quot;:\\\&quot;upsert\\\&quot;}. If the Upload format is JSON pass metadata as {\\\&quot;format\\\&quot;:\\\&quot;json\\\&quot;}. callback-payload - is passed back in bulk job notification  | [optional] 
 **file** | **File**| The file of objects to bulk load. If the JSON file upload, each JSON record should be in a single line | [optional] 

### Return type

[**BulkUploadResponse**](BulkUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## createBulkDownload

> BulkQuery createBulkDownload(authorization, body)

Create a new bulk download job (asynchronous)

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.BulkApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let body = new Ecwid.BulkDownloadRequest(); // BulkDownloadRequest | The object body
apiInstance.createBulkDownload(authorization, body, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **body** | [**BulkDownloadRequest**](BulkDownloadRequest.md)| The object body | 

### Return type

[**BulkQuery**](BulkQuery.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## createBulkQuery

> BulkQuery createBulkQuery(authorization, opts)

Create an asynchronous bulk query job.

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.BulkApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let opts = {
  'elementsAsyncCallbackUrl': "elementsAsyncCallbackUrl_example", // String | The Url to send the notification to when the Job is completed
  'q': "q_example", // String | The CEQL query. When this parameter is omitted, all objects of the given type are returned via the bulk job. Endpoint limiters may still apply.
  'lastRunDate': "lastRunDate_example", // String | The last time this query was run. This is optional. You can also have this parameter in the query and leave this blank - optional eg. '2014-10-06T13:22:17-08:00'
  'from': "from_example", // String | The created/updated date of the object to filter on - optional eg. '2014-10-06T13:22:17-08:00'
  'to': "to_example", // String | The created/updated date of the object to filter on - optional eg. '2014-10-06T13:22:17-08:00'
  'metaData': "metaData_example" // String | Optional JSON MetaData that contains callback-payload and fileName, ex: {\\\"callback-payload\\\" : <Json> , \\\"fileName\\\" : \\\"{Date format}_Name of the file\\\"}. If the fileName is MyFile then pass metadata as {\\\"fileName\\\" : \\\"{yyyy-MM-dd HH:mm:ss}_MyFile\\\"}. The valid date formats are \\\"yyyy-MM-dd'T'HH:mm:ssXXX\\\", \\\"yyyy-MM-dd'T'HH:mm:ss'Z'\\\", \\\"yyyy-MM-dd'T'HH:mm:ss.SXXX\\\", \\\"yyyy-MM-dd'T'HH:mm:ss.SSSXXX\\\", \\\"yyyy-MM-dd'T'HH:mm:ss.SSSZ\\\", \\\"yyyy-MM-dd'T'HH:mm:ss.SSS'Z'\\\", \\\"yyyy-MM-dd HH:mm:ss\\\", \\\"yyyy.MM.dd G 'at' HH:mm:ss z\\\", \\\"h:mm a\\\", \\\"yyyyy.MMMMM.dd GGG hh:mm aaa\\\" and \\\"yyMMddHHmmssZ\\\". callback-payload - is passed back in bulk job notification 
};
apiInstance.createBulkQuery(authorization, opts, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **elementsAsyncCallbackUrl** | **String**| The Url to send the notification to when the Job is completed | [optional] 
 **q** | **String**| The CEQL query. When this parameter is omitted, all objects of the given type are returned via the bulk job. Endpoint limiters may still apply. | [optional] 
 **lastRunDate** | **String**| The last time this query was run. This is optional. You can also have this parameter in the query and leave this blank - optional eg. &#39;2014-10-06T13:22:17-08:00&#39; | [optional] 
 **from** | **String**| The created/updated date of the object to filter on - optional eg. &#39;2014-10-06T13:22:17-08:00&#39; | [optional] 
 **to** | **String**| The created/updated date of the object to filter on - optional eg. &#39;2014-10-06T13:22:17-08:00&#39; | [optional] 
 **metaData** | **String**| Optional JSON MetaData that contains callback-payload and fileName, ex: {\\\&quot;callback-payload\\\&quot; : &lt;Json&gt; , \\\&quot;fileName\\\&quot; : \\\&quot;{Date format}_Name of the file\\\&quot;}. If the fileName is MyFile then pass metadata as {\\\&quot;fileName\\\&quot; : \\\&quot;{yyyy-MM-dd HH:mm:ss}_MyFile\\\&quot;}. The valid date formats are \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssXXX\\\&quot;, \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;\\\&quot;, \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SXXX\\\&quot;, \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSXXX\\\&quot;, \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ\\\&quot;, \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;\\\&quot;, \\\&quot;yyyy-MM-dd HH:mm:ss\\\&quot;, \\\&quot;yyyy.MM.dd G &#39;at&#39; HH:mm:ss z\\\&quot;, \\\&quot;h:mm a\\\&quot;, \\\&quot;yyyyy.MMMMM.dd GGG hh:mm aaa\\\&quot; and \\\&quot;yyMMddHHmmssZ\\\&quot;. callback-payload - is passed back in bulk job notification  | [optional] 

### Return type

[**BulkQuery**](BulkQuery.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## getBulkByObjectName

> File getBulkByObjectName(authorization, id, objectName)

Retrieve the results of an asynchronous bulk query.

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.BulkApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let id = "id_example"; // String | The ID of the bulk job
let objectName = "objectName_example"; // String | The name of the object
apiInstance.getBulkByObjectName(authorization, id, objectName, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **id** | **String**| The ID of the bulk job | 
 **objectName** | **String**| The name of the object | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/csv, application/json, application/jsonl


## getBulkErrors

> [String] getBulkErrors(authorization, id, opts)

Retrieve the errors of a bulk job.

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.BulkApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let id = "id_example"; // String | The ID of the bulk job to retrieve its errors.
let opts = {
  'pageSize': 789, // Number | The page size for pagination, which defaults to 200 if not supplied
  'nextPage': "nextPage_example", // String | The next page cursor, taken from the response header: `elements-next-page-token`
  'fields': "fields_example" // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
};
apiInstance.getBulkErrors(authorization, id, opts, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **id** | **String**| The ID of the bulk job to retrieve its errors. | 
 **pageSize** | **Number**| The page size for pagination, which defaults to 200 if not supplied | [optional] 
 **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] 
 **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getBulkJobs

> BulkJobList getBulkJobs(authorization, opts)

Fetch all the bulk jobs for an instance

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.BulkApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let opts = {
  'where': "where_example", // String | The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query. For example to get all upload jobs the expression would be where=job_direction='UPLOAD'. The following fields are valid search fields 'object_name', 'job_status', 'job_direction', 'record_count'
  'nextPage': "nextPage_example", // String | The next page cursor, taken from the response header: `elements-next-page-token`
  'pageSize': 789, // Number | The page size for pagination, which defaults to 200 if not supplied
  'fields': "fields_example" // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
};
apiInstance.getBulkJobs(authorization, opts, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **where** | **String**| The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query. For example to get all upload jobs the expression would be where&#x3D;job_direction&#x3D;&#39;UPLOAD&#39;. The following fields are valid search fields &#39;object_name&#39;, &#39;job_status&#39;, &#39;job_direction&#39;, &#39;record_count&#39; | [optional] 
 **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] 
 **pageSize** | **Number**| The page size for pagination, which defaults to 200 if not supplied | [optional] 
 **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] 

### Return type

[**BulkJobList**](BulkJobList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getBulkStatus

> BulkStatus getBulkStatus(authorization, id)

Retrieve the status of a bulk job.

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.BulkApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let id = "id_example"; // String | The ID of the bulk job to retrieve its status.
apiInstance.getBulkStatus(authorization, id, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **id** | **String**| The ID of the bulk job to retrieve its status. | 

### Return type

[**BulkStatus**](BulkStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## replaceBulkCancel

> BulkStatus replaceBulkCancel(authorization, id)

Cancel an asynchronous bulk query job.

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.BulkApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let id = "id_example"; // String | The ID of the bulk job to cancel.
apiInstance.replaceBulkCancel(authorization, id, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **id** | **String**| The ID of the bulk job to cancel. | 

### Return type

[**BulkStatus**](BulkStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

