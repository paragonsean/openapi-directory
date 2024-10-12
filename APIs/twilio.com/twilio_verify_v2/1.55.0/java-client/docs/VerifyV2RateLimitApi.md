# VerifyV2RateLimitApi

All URIs are relative to *https://verify.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRateLimit**](VerifyV2RateLimitApi.md#createRateLimit) | **POST** /v2/Services/{ServiceSid}/RateLimits |  |
| [**deleteRateLimit**](VerifyV2RateLimitApi.md#deleteRateLimit) | **DELETE** /v2/Services/{ServiceSid}/RateLimits/{Sid} |  |
| [**fetchRateLimit**](VerifyV2RateLimitApi.md#fetchRateLimit) | **GET** /v2/Services/{ServiceSid}/RateLimits/{Sid} |  |
| [**listRateLimit**](VerifyV2RateLimitApi.md#listRateLimit) | **GET** /v2/Services/{ServiceSid}/RateLimits |  |
| [**updateRateLimit**](VerifyV2RateLimitApi.md#updateRateLimit) | **POST** /v2/Services/{ServiceSid}/RateLimits/{Sid} |  |


<a id="createRateLimit"></a>
# **createRateLimit**
> VerifyV2ServiceRateLimit createRateLimit(serviceSid, uniqueName, description)



Create a new Rate Limit for a Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2RateLimitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2RateLimitApi apiInstance = new VerifyV2RateLimitApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    String uniqueName = "uniqueName_example"; // String | Provides a unique and addressable name to be assigned to this Rate Limit, assigned by the developer, to be optionally used in addition to SID. **This value should not contain PII.**
    String description = "description_example"; // String | Description of this Rate Limit
    try {
      VerifyV2ServiceRateLimit result = apiInstance.createRateLimit(serviceSid, uniqueName, description);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2RateLimitApi#createRateLimit");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with. | |
| **uniqueName** | **String**| Provides a unique and addressable name to be assigned to this Rate Limit, assigned by the developer, to be optionally used in addition to SID. **This value should not contain PII.** | |
| **description** | **String**| Description of this Rate Limit | [optional] |

### Return type

[**VerifyV2ServiceRateLimit**](VerifyV2ServiceRateLimit.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteRateLimit"></a>
# **deleteRateLimit**
> deleteRateLimit(serviceSid, sid)



Delete a specific Rate Limit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2RateLimitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2RateLimitApi apiInstance = new VerifyV2RateLimitApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
    try {
      apiInstance.deleteRateLimit(serviceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2RateLimitApi#deleteRateLimit");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch. | |

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

<a id="fetchRateLimit"></a>
# **fetchRateLimit**
> VerifyV2ServiceRateLimit fetchRateLimit(serviceSid, sid)



Fetch a specific Rate Limit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2RateLimitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2RateLimitApi apiInstance = new VerifyV2RateLimitApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
    try {
      VerifyV2ServiceRateLimit result = apiInstance.fetchRateLimit(serviceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2RateLimitApi#fetchRateLimit");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch. | |

### Return type

[**VerifyV2ServiceRateLimit**](VerifyV2ServiceRateLimit.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listRateLimit"></a>
# **listRateLimit**
> ListRateLimitResponse listRateLimit(serviceSid, pageSize, page, pageToken)



Retrieve a list of all Rate Limits for a service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2RateLimitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2RateLimitApi apiInstance = new VerifyV2RateLimitApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListRateLimitResponse result = apiInstance.listRateLimit(serviceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2RateLimitApi#listRateLimit");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListRateLimitResponse**](ListRateLimitResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateRateLimit"></a>
# **updateRateLimit**
> VerifyV2ServiceRateLimit updateRateLimit(serviceSid, sid, description)



Update a specific Rate Limit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2RateLimitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2RateLimitApi apiInstance = new VerifyV2RateLimitApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
    String description = "description_example"; // String | Description of this Rate Limit
    try {
      VerifyV2ServiceRateLimit result = apiInstance.updateRateLimit(serviceSid, sid, description);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2RateLimitApi#updateRateLimit");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch. | |
| **description** | **String**| Description of this Rate Limit | [optional] |

### Return type

[**VerifyV2ServiceRateLimit**](VerifyV2ServiceRateLimit.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

