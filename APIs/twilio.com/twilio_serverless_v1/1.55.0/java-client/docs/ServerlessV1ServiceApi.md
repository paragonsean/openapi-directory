# ServerlessV1ServiceApi

All URIs are relative to *https://serverless.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createService**](ServerlessV1ServiceApi.md#createService) | **POST** /v1/Services |  |
| [**deleteService**](ServerlessV1ServiceApi.md#deleteService) | **DELETE** /v1/Services/{Sid} |  |
| [**fetchService**](ServerlessV1ServiceApi.md#fetchService) | **GET** /v1/Services/{Sid} |  |
| [**listService**](ServerlessV1ServiceApi.md#listService) | **GET** /v1/Services |  |
| [**updateService**](ServerlessV1ServiceApi.md#updateService) | **POST** /v1/Services/{Sid} |  |


<a id="createService"></a>
# **createService**
> ServerlessV1Service createService(friendlyName, uniqueName, includeCredentials, uiEditable)



Create a new Service resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1ServiceApi apiInstance = new ServerlessV1ServiceApi(defaultClient);
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Service resource. It can be a maximum of 255 characters.
    String uniqueName = "uniqueName_example"; // String | A user-defined string that uniquely identifies the Service resource. It can be used as an alternative to the `sid` in the URL path to address the Service resource. This value must be 50 characters or less in length and be unique.
    Boolean includeCredentials = true; // Boolean | Whether to inject Account credentials into a function invocation context. The default value is `true`.
    Boolean uiEditable = true; // Boolean | Whether the Service's properties and subresources can be edited via the UI. The default value is `false`.
    try {
      ServerlessV1Service result = apiInstance.createService(friendlyName, uniqueName, includeCredentials, uiEditable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1ServiceApi#createService");
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
| **friendlyName** | **String**| A descriptive string that you create to describe the Service resource. It can be a maximum of 255 characters. | |
| **uniqueName** | **String**| A user-defined string that uniquely identifies the Service resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the Service resource. This value must be 50 characters or less in length and be unique. | |
| **includeCredentials** | **Boolean**| Whether to inject Account credentials into a function invocation context. The default value is &#x60;true&#x60;. | [optional] |
| **uiEditable** | **Boolean**| Whether the Service&#39;s properties and subresources can be edited via the UI. The default value is &#x60;false&#x60;. | [optional] |

### Return type

[**ServerlessV1Service**](ServerlessV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteService"></a>
# **deleteService**
> deleteService(sid)



Delete a Service resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1ServiceApi apiInstance = new ServerlessV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The `sid` or `unique_name` of the Service resource to delete.
    try {
      apiInstance.deleteService(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1ServiceApi#deleteService");
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
| **sid** | **String**| The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the Service resource to delete. | |

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

<a id="fetchService"></a>
# **fetchService**
> ServerlessV1Service fetchService(sid)



Retrieve a specific Service resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1ServiceApi apiInstance = new ServerlessV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The `sid` or `unique_name` of the Service resource to fetch.
    try {
      ServerlessV1Service result = apiInstance.fetchService(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1ServiceApi#fetchService");
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
| **sid** | **String**| The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the Service resource to fetch. | |

### Return type

[**ServerlessV1Service**](ServerlessV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listService"></a>
# **listService**
> ListServiceResponse listService(pageSize, page, pageToken)



Retrieve a list of all Services.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1ServiceApi apiInstance = new ServerlessV1ServiceApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListServiceResponse result = apiInstance.listService(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1ServiceApi#listService");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListServiceResponse**](ListServiceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateService"></a>
# **updateService**
> ServerlessV1Service updateService(sid, friendlyName, includeCredentials, uiEditable)



Update a specific Service resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1ServiceApi apiInstance = new ServerlessV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The `sid` or `unique_name` of the Service resource to update.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Service resource. It can be a maximum of 255 characters.
    Boolean includeCredentials = true; // Boolean | Whether to inject Account credentials into a function invocation context.
    Boolean uiEditable = true; // Boolean | Whether the Service resource's properties and subresources can be edited via the UI. The default value is `false`.
    try {
      ServerlessV1Service result = apiInstance.updateService(sid, friendlyName, includeCredentials, uiEditable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1ServiceApi#updateService");
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
| **sid** | **String**| The &#x60;sid&#x60; or &#x60;unique_name&#x60; of the Service resource to update. | |
| **friendlyName** | **String**| A descriptive string that you create to describe the Service resource. It can be a maximum of 255 characters. | [optional] |
| **includeCredentials** | **Boolean**| Whether to inject Account credentials into a function invocation context. | [optional] |
| **uiEditable** | **Boolean**| Whether the Service resource&#39;s properties and subresources can be edited via the UI. The default value is &#x60;false&#x60;. | [optional] |

### Return type

[**ServerlessV1Service**](ServerlessV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

