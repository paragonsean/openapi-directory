# BulkApi

All URIs are relative to *https://api.cloud-elements.com/elements/api-v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBulkByObjectName**](BulkApi.md#createBulkByObjectName) | **POST** /bulk/{objectName} | Upload a file of objects to be bulk uploaded to the provider. |
| [**createBulkDownload**](BulkApi.md#createBulkDownload) | **POST** /bulk/download | Create a new bulk download job (asynchronous) |
| [**createBulkQuery**](BulkApi.md#createBulkQuery) | **POST** /bulk/query | Create an asynchronous bulk query job. |
| [**getBulkByObjectName**](BulkApi.md#getBulkByObjectName) | **GET** /bulk/{id}/{objectName} | Retrieve the results of an asynchronous bulk query. |
| [**getBulkErrors**](BulkApi.md#getBulkErrors) | **GET** /bulk/{id}/errors | Retrieve the errors of a bulk job. |
| [**getBulkJobs**](BulkApi.md#getBulkJobs) | **GET** /bulk/jobs | Fetch all the bulk jobs for an instance |
| [**getBulkStatus**](BulkApi.md#getBulkStatus) | **GET** /bulk/{id}/status | Retrieve the status of a bulk job. |
| [**replaceBulkCancel**](BulkApi.md#replaceBulkCancel) | **PUT** /bulk/{id}/cancel | Cancel an asynchronous bulk query job. |


<a id="createBulkByObjectName"></a>
# **createBulkByObjectName**
> BulkUploadResponse createBulkByObjectName(authorization, objectName, elementsAsyncCallbackUrl, metaData, _file)

Upload a file of objects to be bulk uploaded to the provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    BulkApi apiInstance = new BulkApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String objectName = "objectName_example"; // String | The name of the object for which data needs to be uploaded.
    String elementsAsyncCallbackUrl = "elementsAsyncCallbackUrl_example"; // String | The Url to send the notification to when the Job is completed
    String metaData = "metaData_example"; // String | Optional JSON MetaData that contains callback-payload, path or format, ex: {\\\"path\\\" :&lt;path for the sub resource&gt;, \\\"format\\\": &lt;json/csv&gt;, \\\"callback-payload\\\":&lt;json&gt;}. path - is passed to the endpoint for bulk loading the data into a nested object. Optional JSON Metadata that contains identifierFieldName, action, listId or campaignId. The identifierField name is used for upserts and the optional fields like listId or campaignId. Example: {\\\"listId\\\":\\\"1014\\\",\\\"action\\\":\\\"upsert\\\"}. If the Upload format is JSON pass metadata as {\\\"format\\\":\\\"json\\\"}. callback-payload - is passed back in bulk job notification 
    File _file = new File("/path/to/file"); // File | The file of objects to bulk load. If the JSON file upload, each JSON record should be in a single line
    try {
      BulkUploadResponse result = apiInstance.createBulkByObjectName(authorization, objectName, elementsAsyncCallbackUrl, metaData, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkApi#createBulkByObjectName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **objectName** | **String**| The name of the object for which data needs to be uploaded. | |
| **elementsAsyncCallbackUrl** | **String**| The Url to send the notification to when the Job is completed | [optional] |
| **metaData** | **String**| Optional JSON MetaData that contains callback-payload, path or format, ex: {\\\&quot;path\\\&quot; :&amp;lt;path for the sub resource&amp;gt;, \\\&quot;format\\\&quot;: &amp;lt;json/csv&amp;gt;, \\\&quot;callback-payload\\\&quot;:&amp;lt;json&amp;gt;}. path - is passed to the endpoint for bulk loading the data into a nested object. Optional JSON Metadata that contains identifierFieldName, action, listId or campaignId. The identifierField name is used for upserts and the optional fields like listId or campaignId. Example: {\\\&quot;listId\\\&quot;:\\\&quot;1014\\\&quot;,\\\&quot;action\\\&quot;:\\\&quot;upsert\\\&quot;}. If the Upload format is JSON pass metadata as {\\\&quot;format\\\&quot;:\\\&quot;json\\\&quot;}. callback-payload - is passed back in bulk job notification  | [optional] |
| **_file** | **File**| The file of objects to bulk load. If the JSON file upload, each JSON record should be in a single line | [optional] |

### Return type

[**BulkUploadResponse**](BulkUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="createBulkDownload"></a>
# **createBulkDownload**
> BulkQuery createBulkDownload(authorization, body)

Create a new bulk download job (asynchronous)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    BulkApi apiInstance = new BulkApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    BulkDownloadRequest body = new BulkDownloadRequest(); // BulkDownloadRequest | The object body
    try {
      BulkQuery result = apiInstance.createBulkDownload(authorization, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkApi#createBulkDownload");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **body** | [**BulkDownloadRequest**](BulkDownloadRequest.md)| The object body | |

### Return type

[**BulkQuery**](BulkQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="createBulkQuery"></a>
# **createBulkQuery**
> BulkQuery createBulkQuery(authorization, elementsAsyncCallbackUrl, q, lastRunDate, from, to, metaData)

Create an asynchronous bulk query job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    BulkApi apiInstance = new BulkApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String elementsAsyncCallbackUrl = "elementsAsyncCallbackUrl_example"; // String | The Url to send the notification to when the Job is completed
    String q = "q_example"; // String | The CEQL query. When this parameter is omitted, all objects of the given type are returned via the bulk job. Endpoint limiters may still apply.
    String lastRunDate = "lastRunDate_example"; // String | The last time this query was run. This is optional. You can also have this parameter in the query and leave this blank - optional eg. '2014-10-06T13:22:17-08:00'
    String from = "from_example"; // String | The created/updated date of the object to filter on - optional eg. '2014-10-06T13:22:17-08:00'
    String to = "to_example"; // String | The created/updated date of the object to filter on - optional eg. '2014-10-06T13:22:17-08:00'
    String metaData = "metaData_example"; // String | Optional JSON MetaData that contains callback-payload and fileName, ex: {\\\"callback-payload\\\" : <Json> , \\\"fileName\\\" : \\\"{Date format}_Name of the file\\\"}. If the fileName is MyFile then pass metadata as {\\\"fileName\\\" : \\\"{yyyy-MM-dd HH:mm:ss}_MyFile\\\"}. The valid date formats are \\\"yyyy-MM-dd'T'HH:mm:ssXXX\\\", \\\"yyyy-MM-dd'T'HH:mm:ss'Z'\\\", \\\"yyyy-MM-dd'T'HH:mm:ss.SXXX\\\", \\\"yyyy-MM-dd'T'HH:mm:ss.SSSXXX\\\", \\\"yyyy-MM-dd'T'HH:mm:ss.SSSZ\\\", \\\"yyyy-MM-dd'T'HH:mm:ss.SSS'Z'\\\", \\\"yyyy-MM-dd HH:mm:ss\\\", \\\"yyyy.MM.dd G 'at' HH:mm:ss z\\\", \\\"h:mm a\\\", \\\"yyyyy.MMMMM.dd GGG hh:mm aaa\\\" and \\\"yyMMddHHmmssZ\\\". callback-payload - is passed back in bulk job notification 
    try {
      BulkQuery result = apiInstance.createBulkQuery(authorization, elementsAsyncCallbackUrl, q, lastRunDate, from, to, metaData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkApi#createBulkQuery");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **elementsAsyncCallbackUrl** | **String**| The Url to send the notification to when the Job is completed | [optional] |
| **q** | **String**| The CEQL query. When this parameter is omitted, all objects of the given type are returned via the bulk job. Endpoint limiters may still apply. | [optional] |
| **lastRunDate** | **String**| The last time this query was run. This is optional. You can also have this parameter in the query and leave this blank - optional eg. &#39;2014-10-06T13:22:17-08:00&#39; | [optional] |
| **from** | **String**| The created/updated date of the object to filter on - optional eg. &#39;2014-10-06T13:22:17-08:00&#39; | [optional] |
| **to** | **String**| The created/updated date of the object to filter on - optional eg. &#39;2014-10-06T13:22:17-08:00&#39; | [optional] |
| **metaData** | **String**| Optional JSON MetaData that contains callback-payload and fileName, ex: {\\\&quot;callback-payload\\\&quot; : &lt;Json&gt; , \\\&quot;fileName\\\&quot; : \\\&quot;{Date format}_Name of the file\\\&quot;}. If the fileName is MyFile then pass metadata as {\\\&quot;fileName\\\&quot; : \\\&quot;{yyyy-MM-dd HH:mm:ss}_MyFile\\\&quot;}. The valid date formats are \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssXXX\\\&quot;, \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;\\\&quot;, \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SXXX\\\&quot;, \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSXXX\\\&quot;, \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ\\\&quot;, \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;\\\&quot;, \\\&quot;yyyy-MM-dd HH:mm:ss\\\&quot;, \\\&quot;yyyy.MM.dd G &#39;at&#39; HH:mm:ss z\\\&quot;, \\\&quot;h:mm a\\\&quot;, \\\&quot;yyyyy.MMMMM.dd GGG hh:mm aaa\\\&quot; and \\\&quot;yyMMddHHmmssZ\\\&quot;. callback-payload - is passed back in bulk job notification  | [optional] |

### Return type

[**BulkQuery**](BulkQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getBulkByObjectName"></a>
# **getBulkByObjectName**
> File getBulkByObjectName(authorization, id, objectName)

Retrieve the results of an asynchronous bulk query.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    BulkApi apiInstance = new BulkApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String id = "id_example"; // String | The ID of the bulk job
    String objectName = "objectName_example"; // String | The name of the object
    try {
      File result = apiInstance.getBulkByObjectName(authorization, id, objectName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkApi#getBulkByObjectName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **id** | **String**| The ID of the bulk job | |
| **objectName** | **String**| The name of the object | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json, application/jsonl

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getBulkErrors"></a>
# **getBulkErrors**
> List&lt;String&gt; getBulkErrors(authorization, id, pageSize, nextPage, fields)

Retrieve the errors of a bulk job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    BulkApi apiInstance = new BulkApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String id = "id_example"; // String | The ID of the bulk job to retrieve its errors.
    Long pageSize = 56L; // Long | The page size for pagination, which defaults to 200 if not supplied
    String nextPage = "nextPage_example"; // String | The next page cursor, taken from the response header: `elements-next-page-token`
    String fields = "fields_example"; // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
    try {
      List<String> result = apiInstance.getBulkErrors(authorization, id, pageSize, nextPage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkApi#getBulkErrors");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **id** | **String**| The ID of the bulk job to retrieve its errors. | |
| **pageSize** | **Long**| The page size for pagination, which defaults to 200 if not supplied | [optional] |
| **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] |
| **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getBulkJobs"></a>
# **getBulkJobs**
> BulkJobList getBulkJobs(authorization, where, nextPage, pageSize, fields)

Fetch all the bulk jobs for an instance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    BulkApi apiInstance = new BulkApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String where = "where_example"; // String | The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query. For example to get all upload jobs the expression would be where=job_direction='UPLOAD'. The following fields are valid search fields 'object_name', 'job_status', 'job_direction', 'record_count'
    String nextPage = "nextPage_example"; // String | The next page cursor, taken from the response header: `elements-next-page-token`
    Long pageSize = 56L; // Long | The page size for pagination, which defaults to 200 if not supplied
    String fields = "fields_example"; // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
    try {
      BulkJobList result = apiInstance.getBulkJobs(authorization, where, nextPage, pageSize, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkApi#getBulkJobs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **where** | **String**| The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query. For example to get all upload jobs the expression would be where&#x3D;job_direction&#x3D;&#39;UPLOAD&#39;. The following fields are valid search fields &#39;object_name&#39;, &#39;job_status&#39;, &#39;job_direction&#39;, &#39;record_count&#39; | [optional] |
| **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] |
| **pageSize** | **Long**| The page size for pagination, which defaults to 200 if not supplied | [optional] |
| **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] |

### Return type

[**BulkJobList**](BulkJobList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getBulkStatus"></a>
# **getBulkStatus**
> BulkStatus getBulkStatus(authorization, id)

Retrieve the status of a bulk job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    BulkApi apiInstance = new BulkApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String id = "id_example"; // String | The ID of the bulk job to retrieve its status.
    try {
      BulkStatus result = apiInstance.getBulkStatus(authorization, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkApi#getBulkStatus");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **id** | **String**| The ID of the bulk job to retrieve its status. | |

### Return type

[**BulkStatus**](BulkStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="replaceBulkCancel"></a>
# **replaceBulkCancel**
> BulkStatus replaceBulkCancel(authorization, id)

Cancel an asynchronous bulk query job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    BulkApi apiInstance = new BulkApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String id = "id_example"; // String | The ID of the bulk job to cancel.
    try {
      BulkStatus result = apiInstance.replaceBulkCancel(authorization, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkApi#replaceBulkCancel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **id** | **String**| The ID of the bulk job to cancel. | |

### Return type

[**BulkStatus**](BulkStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

