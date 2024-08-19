# ApplicationApi

All URIs are relative to *https://api-2445581398133.apicast.io:443/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createApplicationEntity**](ApplicationApi.md#createApplicationEntity) | **POST** /application | POST for application |
| [**deleteApplicationEntity**](ApplicationApi.md#deleteApplicationEntity) | **DELETE** /application/{key} | DELETE for application |
| [**getApplicationCollection**](ApplicationApi.md#getApplicationCollection) | **GET** /application/list | GET for application |
| [**getApplicationCountCollection**](ApplicationApi.md#getApplicationCountCollection) | **GET** /application/count | COUNT for application |
| [**getApplicationEntity**](ApplicationApi.md#getApplicationEntity) | **GET** /application/{key} | GET for application |
| [**updateApplicationEntity**](ApplicationApi.md#updateApplicationEntity) | **PUT** /application/{key} | PUT for application |


<a id="createApplicationEntity"></a>
# **createApplicationEntity**
> ApplicationEntityRelation createApplicationEntity(X_API2CRM_USER_KEY, body)

POST for application

Add application into the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | API2CRM user key
    ApplicationEntityWrite body = new ApplicationEntityWrite(); // ApplicationEntityWrite | Add application into the system
    try {
      ApplicationEntityRelation result = apiInstance.createApplicationEntity(X_API2CRM_USER_KEY, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#createApplicationEntity");
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
| **X_API2CRM_USER_KEY** | **String**| API2CRM user key | [default to e2a6379ab878ae7e58119d4ec842bf9c] |
| **body** | [**ApplicationEntityWrite**](ApplicationEntityWrite.md)| Add application into the system | |

### Return type

[**ApplicationEntityRelation**](ApplicationEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Client Error |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="deleteApplicationEntity"></a>
# **deleteApplicationEntity**
> deleteApplicationEntity(X_API2CRM_USER_KEY, key)

DELETE for application

Delete application information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | API2CRM user key
    String key = "key_example"; // String | Application key
    try {
      apiInstance.deleteApplicationEntity(X_API2CRM_USER_KEY, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#deleteApplicationEntity");
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
| **X_API2CRM_USER_KEY** | **String**| API2CRM user key | [default to e2a6379ab878ae7e58119d4ec842bf9c] |
| **key** | **String**| Application key | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **404** | Not Found |  -  |

<a id="getApplicationCollection"></a>
# **getApplicationCollection**
> List&lt;ApplicationEntityList&gt; getApplicationCollection(X_API2CRM_USER_KEY, pageSize, page, filter, fields, sort)

GET for application

Returns all applications from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | API2CRM user key
    Integer pageSize = 56; // Integer | Amount of results (default: 25)
    Integer page = 56; // Integer | Page to show (default: 1)
    String filter = "filter_example"; // String | Filter
    String fields = "fields_example"; // String | Comma-separated list of fields to include in the response
    String sort = "sort_example"; // String | Specifies ascending or descending sort on existing fields
    try {
      List<ApplicationEntityList> result = apiInstance.getApplicationCollection(X_API2CRM_USER_KEY, pageSize, page, filter, fields, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#getApplicationCollection");
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
| **X_API2CRM_USER_KEY** | **String**| API2CRM user key | [default to e2a6379ab878ae7e58119d4ec842bf9c] |
| **pageSize** | **Integer**| Amount of results (default: 25) | [optional] |
| **page** | **Integer**| Page to show (default: 1) | [optional] |
| **filter** | **String**| Filter | [optional] |
| **fields** | **String**| Comma-separated list of fields to include in the response | [optional] |
| **sort** | **String**| Specifies ascending or descending sort on existing fields | [optional] |

### Return type

[**List&lt;ApplicationEntityList&gt;**](ApplicationEntityList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

<a id="getApplicationCountCollection"></a>
# **getApplicationCountCollection**
> Count getApplicationCountCollection(X_API2CRM_USER_KEY, filter)

COUNT for application

Count all applications from the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | API2CRM user key
    String filter = "filter_example"; // String | Filter
    try {
      Count result = apiInstance.getApplicationCountCollection(X_API2CRM_USER_KEY, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#getApplicationCountCollection");
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
| **X_API2CRM_USER_KEY** | **String**| API2CRM user key | [default to e2a6379ab878ae7e58119d4ec842bf9c] |
| **filter** | **String**| Filter | [optional] |

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

<a id="getApplicationEntity"></a>
# **getApplicationEntity**
> ApplicationEntity getApplicationEntity(X_API2CRM_USER_KEY, key, fields)

GET for application

Return application information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | API2CRM user key
    String key = "key_example"; // String | Application key
    String fields = "fields_example"; // String | Comma-separated list of fields to include in the response
    try {
      ApplicationEntity result = apiInstance.getApplicationEntity(X_API2CRM_USER_KEY, key, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#getApplicationEntity");
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
| **X_API2CRM_USER_KEY** | **String**| API2CRM user key | [default to e2a6379ab878ae7e58119d4ec842bf9c] |
| **key** | **String**| Application key | |
| **fields** | **String**| Comma-separated list of fields to include in the response | [optional] |

### Return type

[**ApplicationEntity**](ApplicationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

<a id="updateApplicationEntity"></a>
# **updateApplicationEntity**
> ApplicationEntityRelation updateApplicationEntity(X_API2CRM_USER_KEY, key, body)

PUT for application

Update application information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-2445581398133.apicast.io:443/v1");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String X_API2CRM_USER_KEY = "e2a6379ab878ae7e58119d4ec842bf9c"; // String | API2CRM user key
    String key = "key_example"; // String | Application key
    ApplicationEntityWrite body = new ApplicationEntityWrite(); // ApplicationEntityWrite | Update application information
    try {
      ApplicationEntityRelation result = apiInstance.updateApplicationEntity(X_API2CRM_USER_KEY, key, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#updateApplicationEntity");
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
| **X_API2CRM_USER_KEY** | **String**| API2CRM user key | [default to e2a6379ab878ae7e58119d4ec842bf9c] |
| **key** | **String**| Application key | |
| **body** | [**ApplicationEntityWrite**](ApplicationEntityWrite.md)| Update application information | |

### Return type

[**ApplicationEntityRelation**](ApplicationEntityRelation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Client Error |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |

