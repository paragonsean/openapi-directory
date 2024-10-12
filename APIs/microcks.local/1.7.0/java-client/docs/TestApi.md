# TestApi

All URIs are relative to *http://microcks.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTest**](TestApi.md#createTest) | **POST** /tests | Create a new Test |
| [**getEventsByTestCase**](TestApi.md#getEventsByTestCase) | **GET** /tests/{id}/events/{testCaseId} | Get events for TestCase |
| [**getMessagesByTestCase**](TestApi.md#getMessagesByTestCase) | **GET** /tests/{id}/messages/{testCaseId} | Get messages for TestCase |
| [**getTestResult**](TestApi.md#getTestResult) | **GET** /tests/{id} | Get TestResult |
| [**getTestResultsByService**](TestApi.md#getTestResultsByService) | **GET** /tests/service/{serviceId} | Get TestResults by Service |
| [**getTestResultsByServiceCounter**](TestApi.md#getTestResultsByServiceCounter) | **GET** /tests/service/{serviceId}/count | Get the TestResults for Service counter |
| [**reportTestCaseResult**](TestApi.md#reportTestCaseResult) | **POST** /tests/{id}/testCaseResult | Report and create a new TestCaseResult |


<a id="createTest"></a>
# **createTest**
> TestResult createTest(testRequest)

Create a new Test

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    TestApi apiInstance = new TestApi(defaultClient);
    TestRequest testRequest = new TestRequest(); // TestRequest | 
    try {
      TestResult result = apiInstance.createTest(testRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#createTest");
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
| **testRequest** | [**TestRequest**](TestRequest.md)|  | |

### Return type

[**TestResult**](TestResult.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created TestResult (empty shell cause tests are executed asynchronously) |  -  |

<a id="getEventsByTestCase"></a>
# **getEventsByTestCase**
> List&lt;UnidirectionalEvent&gt; getEventsByTestCase(id, testCaseId)

Get events for TestCase

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    TestApi apiInstance = new TestApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of TestResult to manage
    String testCaseId = "testCaseId_example"; // String | Unique identifier of TetsCaseResult to manage
    try {
      List<UnidirectionalEvent> result = apiInstance.getEventsByTestCase(id, testCaseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#getEventsByTestCase");
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
| **id** | **String**| Unique identifier of TestResult to manage | |
| **testCaseId** | **String**| Unique identifier of TetsCaseResult to manage | |

### Return type

[**List&lt;UnidirectionalEvent&gt;**](UnidirectionalEvent.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of event messages for this TestCase |  -  |

<a id="getMessagesByTestCase"></a>
# **getMessagesByTestCase**
> List&lt;RequestResponsePair&gt; getMessagesByTestCase(id, testCaseId)

Get messages for TestCase

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    TestApi apiInstance = new TestApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of TestResult to manage
    String testCaseId = "testCaseId_example"; // String | Unique identifier of TetsCaseResult to manage
    try {
      List<RequestResponsePair> result = apiInstance.getMessagesByTestCase(id, testCaseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#getMessagesByTestCase");
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
| **id** | **String**| Unique identifier of TestResult to manage | |
| **testCaseId** | **String**| Unique identifier of TetsCaseResult to manage | |

### Return type

[**List&lt;RequestResponsePair&gt;**](RequestResponsePair.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of request and response messages for this TestCase |  -  |

<a id="getTestResult"></a>
# **getTestResult**
> TestResult getTestResult(id)

Get TestResult



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    TestApi apiInstance = new TestApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of TestResult to manage
    try {
      TestResult result = apiInstance.getTestResult(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#getTestResult");
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
| **id** | **String**| Unique identifier of TestResult to manage | |

### Return type

[**TestResult**](TestResult.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Requested TestResult |  -  |

<a id="getTestResultsByService"></a>
# **getTestResultsByService**
> List&lt;TestResult&gt; getTestResultsByService(serviceId)

Get TestResults by Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    TestApi apiInstance = new TestApi(defaultClient);
    String serviceId = "serviceId_example"; // String | Unique identifier of Service to manage TestResults for
    try {
      List<TestResult> result = apiInstance.getTestResultsByService(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#getTestResultsByService");
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
| **serviceId** | **String**| Unique identifier of Service to manage TestResults for | |

### Return type

[**List&lt;TestResult&gt;**](TestResult.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of TestResults for the Service having the requested id |  -  |

<a id="getTestResultsByServiceCounter"></a>
# **getTestResultsByServiceCounter**
> Counter getTestResultsByServiceCounter(serviceId)

Get the TestResults for Service counter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    TestApi apiInstance = new TestApi(defaultClient);
    String serviceId = "serviceId_example"; // String | Unique identifier of Service to manage TestResults for
    try {
      Counter result = apiInstance.getTestResultsByServiceCounter(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#getTestResultsByServiceCounter");
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
| **serviceId** | **String**| Unique identifier of Service to manage TestResults for | |

### Return type

[**Counter**](Counter.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number of TestResults for this Service in datastore |  -  |

<a id="reportTestCaseResult"></a>
# **reportTestCaseResult**
> TestCaseResult reportTestCaseResult(id, testCaseReturnDTO)

Report and create a new TestCaseResult

Report a TestCaseResult (typically used by a Test runner)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    TestApi apiInstance = new TestApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of TestResult to manage
    TestCaseReturnDTO testCaseReturnDTO = new TestCaseReturnDTO(); // TestCaseReturnDTO | TestCase return wrapper object
    try {
      TestCaseResult result = apiInstance.reportTestCaseResult(id, testCaseReturnDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#reportTestCaseResult");
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
| **id** | **String**| Unique identifier of TestResult to manage | |
| **testCaseReturnDTO** | [**TestCaseReturnDTO**](TestCaseReturnDTO.md)| TestCase return wrapper object | |

### Return type

[**TestCaseResult**](TestCaseResult.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TestCaseResult is reported |  -  |

