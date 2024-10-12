# TrusthubV1EndUserApi

All URIs are relative to *https://trusthub.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createEndUser**](TrusthubV1EndUserApi.md#createEndUser) | **POST** /v1/EndUsers |  |
| [**deleteEndUser**](TrusthubV1EndUserApi.md#deleteEndUser) | **DELETE** /v1/EndUsers/{Sid} |  |
| [**fetchEndUser**](TrusthubV1EndUserApi.md#fetchEndUser) | **GET** /v1/EndUsers/{Sid} |  |
| [**listEndUser**](TrusthubV1EndUserApi.md#listEndUser) | **GET** /v1/EndUsers |  |
| [**updateEndUser**](TrusthubV1EndUserApi.md#updateEndUser) | **POST** /v1/EndUsers/{Sid} |  |


<a id="createEndUser"></a>
# **createEndUser**
> TrusthubV1EndUser createEndUser(friendlyName, type, attributes)



Create a new End User.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1EndUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1EndUserApi apiInstance = new TrusthubV1EndUserApi(defaultClient);
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    String type = "type_example"; // String | The type of end user of the Bundle resource - can be `individual` or `business`.
    Object attributes = null; // Object | The set of parameters that are the attributes of the End User resource which are derived End User Types.
    try {
      TrusthubV1EndUser result = apiInstance.createEndUser(friendlyName, type, attributes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1EndUserApi#createEndUser");
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
| **friendlyName** | **String**| The string that you assigned to describe the resource. | |
| **type** | **String**| The type of end user of the Bundle resource - can be &#x60;individual&#x60; or &#x60;business&#x60;. | |
| **attributes** | [**Object**](Object.md)| The set of parameters that are the attributes of the End User resource which are derived End User Types. | [optional] |

### Return type

[**TrusthubV1EndUser**](TrusthubV1EndUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteEndUser"></a>
# **deleteEndUser**
> deleteEndUser(sid)



Delete a specific End User.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1EndUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1EndUserApi apiInstance = new TrusthubV1EndUserApi(defaultClient);
    String sid = "sid_example"; // String | The unique string created by Twilio to identify the End User resource.
    try {
      apiInstance.deleteEndUser(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1EndUserApi#deleteEndUser");
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
| **sid** | **String**| The unique string created by Twilio to identify the End User resource. | |

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

<a id="fetchEndUser"></a>
# **fetchEndUser**
> TrusthubV1EndUser fetchEndUser(sid)



Fetch specific End User Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1EndUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1EndUserApi apiInstance = new TrusthubV1EndUserApi(defaultClient);
    String sid = "sid_example"; // String | The unique string created by Twilio to identify the End User resource.
    try {
      TrusthubV1EndUser result = apiInstance.fetchEndUser(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1EndUserApi#fetchEndUser");
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
| **sid** | **String**| The unique string created by Twilio to identify the End User resource. | |

### Return type

[**TrusthubV1EndUser**](TrusthubV1EndUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listEndUser"></a>
# **listEndUser**
> ListEndUserResponse listEndUser(pageSize, page, pageToken)



Retrieve a list of all End User for an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1EndUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1EndUserApi apiInstance = new TrusthubV1EndUserApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListEndUserResponse result = apiInstance.listEndUser(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1EndUserApi#listEndUser");
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

[**ListEndUserResponse**](ListEndUserResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateEndUser"></a>
# **updateEndUser**
> TrusthubV1EndUser updateEndUser(sid, attributes, friendlyName)



Update an existing End User.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1EndUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1EndUserApi apiInstance = new TrusthubV1EndUserApi(defaultClient);
    String sid = "sid_example"; // String | The unique string created by Twilio to identify the End User resource.
    Object attributes = null; // Object | The set of parameters that are the attributes of the End User resource which are derived End User Types.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    try {
      TrusthubV1EndUser result = apiInstance.updateEndUser(sid, attributes, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1EndUserApi#updateEndUser");
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
| **sid** | **String**| The unique string created by Twilio to identify the End User resource. | |
| **attributes** | [**Object**](Object.md)| The set of parameters that are the attributes of the End User resource which are derived End User Types. | [optional] |
| **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] |

### Return type

[**TrusthubV1EndUser**](TrusthubV1EndUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

