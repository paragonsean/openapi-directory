# ServerlessV1FunctionApi

All URIs are relative to *https://serverless.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createFunction**](ServerlessV1FunctionApi.md#createFunction) | **POST** /v1/Services/{ServiceSid}/Functions |  |
| [**deleteFunction**](ServerlessV1FunctionApi.md#deleteFunction) | **DELETE** /v1/Services/{ServiceSid}/Functions/{Sid} |  |
| [**fetchFunction**](ServerlessV1FunctionApi.md#fetchFunction) | **GET** /v1/Services/{ServiceSid}/Functions/{Sid} |  |
| [**listFunction**](ServerlessV1FunctionApi.md#listFunction) | **GET** /v1/Services/{ServiceSid}/Functions |  |
| [**updateFunction**](ServerlessV1FunctionApi.md#updateFunction) | **POST** /v1/Services/{ServiceSid}/Functions/{Sid} |  |


<a id="createFunction"></a>
# **createFunction**
> ServerlessV1ServiceFunction createFunction(serviceSid, friendlyName)



Create a new Function resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1FunctionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1FunctionApi apiInstance = new ServerlessV1FunctionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to create the Function resource under.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters.
    try {
      ServerlessV1ServiceFunction result = apiInstance.createFunction(serviceSid, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1FunctionApi#createFunction");
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
| **serviceSid** | **String**| The SID of the Service to create the Function resource under. | |
| **friendlyName** | **String**| A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters. | |

### Return type

[**ServerlessV1ServiceFunction**](ServerlessV1ServiceFunction.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteFunction"></a>
# **deleteFunction**
> deleteFunction(serviceSid, sid)



Delete a Function resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1FunctionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1FunctionApi apiInstance = new ServerlessV1FunctionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to delete the Function resource from.
    String sid = "sid_example"; // String | The SID of the Function resource to delete.
    try {
      apiInstance.deleteFunction(serviceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1FunctionApi#deleteFunction");
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
| **serviceSid** | **String**| The SID of the Service to delete the Function resource from. | |
| **sid** | **String**| The SID of the Function resource to delete. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchFunction"></a>
# **fetchFunction**
> ServerlessV1ServiceFunction fetchFunction(serviceSid, sid)



Retrieve a specific Function resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1FunctionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1FunctionApi apiInstance = new ServerlessV1FunctionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Function resource from.
    String sid = "sid_example"; // String | The SID of the Function resource to fetch.
    try {
      ServerlessV1ServiceFunction result = apiInstance.fetchFunction(serviceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1FunctionApi#fetchFunction");
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
| **serviceSid** | **String**| The SID of the Service to fetch the Function resource from. | |
| **sid** | **String**| The SID of the Function resource to fetch. | |

### Return type

[**ServerlessV1ServiceFunction**](ServerlessV1ServiceFunction.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listFunction"></a>
# **listFunction**
> ListFunctionResponse listFunction(serviceSid, pageSize, page, pageToken)



Retrieve a list of all Functions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1FunctionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1FunctionApi apiInstance = new ServerlessV1FunctionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Function resources from.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListFunctionResponse result = apiInstance.listFunction(serviceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1FunctionApi#listFunction");
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
| **serviceSid** | **String**| The SID of the Service to read the Function resources from. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListFunctionResponse**](ListFunctionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateFunction"></a>
# **updateFunction**
> ServerlessV1ServiceFunction updateFunction(serviceSid, sid, friendlyName)



Update a specific Function resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1FunctionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1FunctionApi apiInstance = new ServerlessV1FunctionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to update the Function resource from.
    String sid = "sid_example"; // String | The SID of the Function resource to update.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters.
    try {
      ServerlessV1ServiceFunction result = apiInstance.updateFunction(serviceSid, sid, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1FunctionApi#updateFunction");
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
| **serviceSid** | **String**| The SID of the Service to update the Function resource from. | |
| **sid** | **String**| The SID of the Function resource to update. | |
| **friendlyName** | **String**| A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters. | |

### Return type

[**ServerlessV1ServiceFunction**](ServerlessV1ServiceFunction.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

