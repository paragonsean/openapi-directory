# VerifyV2BucketApi

All URIs are relative to *https://verify.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBucket**](VerifyV2BucketApi.md#createBucket) | **POST** /v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets |  |
| [**deleteBucket**](VerifyV2BucketApi.md#deleteBucket) | **DELETE** /v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets/{Sid} |  |
| [**fetchBucket**](VerifyV2BucketApi.md#fetchBucket) | **GET** /v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets/{Sid} |  |
| [**listBucket**](VerifyV2BucketApi.md#listBucket) | **GET** /v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets |  |
| [**updateBucket**](VerifyV2BucketApi.md#updateBucket) | **POST** /v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets/{Sid} |  |


<a id="createBucket"></a>
# **createBucket**
> VerifyV2ServiceRateLimitBucket createBucket(serviceSid, rateLimitSid, interval, max)



Create a new Bucket for a Rate Limit

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2BucketApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2BucketApi apiInstance = new VerifyV2BucketApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    String rateLimitSid = "rateLimitSid_example"; // String | The Twilio-provided string that uniquely identifies the Rate Limit resource.
    Integer interval = 56; // Integer | Number of seconds that the rate limit will be enforced over.
    Integer max = 56; // Integer | Maximum number of requests permitted in during the interval.
    try {
      VerifyV2ServiceRateLimitBucket result = apiInstance.createBucket(serviceSid, rateLimitSid, interval, max);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2BucketApi#createBucket");
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
| **rateLimitSid** | **String**| The Twilio-provided string that uniquely identifies the Rate Limit resource. | |
| **interval** | **Integer**| Number of seconds that the rate limit will be enforced over. | |
| **max** | **Integer**| Maximum number of requests permitted in during the interval. | |

### Return type

[**VerifyV2ServiceRateLimitBucket**](VerifyV2ServiceRateLimitBucket.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteBucket"></a>
# **deleteBucket**
> deleteBucket(serviceSid, rateLimitSid, sid)



Delete a specific Bucket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2BucketApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2BucketApi apiInstance = new VerifyV2BucketApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    String rateLimitSid = "rateLimitSid_example"; // String | The Twilio-provided string that uniquely identifies the Rate Limit resource.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this Bucket.
    try {
      apiInstance.deleteBucket(serviceSid, rateLimitSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2BucketApi#deleteBucket");
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
| **rateLimitSid** | **String**| The Twilio-provided string that uniquely identifies the Rate Limit resource. | |
| **sid** | **String**| A 34 character string that uniquely identifies this Bucket. | |

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

<a id="fetchBucket"></a>
# **fetchBucket**
> VerifyV2ServiceRateLimitBucket fetchBucket(serviceSid, rateLimitSid, sid)



Fetch a specific Bucket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2BucketApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2BucketApi apiInstance = new VerifyV2BucketApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    String rateLimitSid = "rateLimitSid_example"; // String | The Twilio-provided string that uniquely identifies the Rate Limit resource.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this Bucket.
    try {
      VerifyV2ServiceRateLimitBucket result = apiInstance.fetchBucket(serviceSid, rateLimitSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2BucketApi#fetchBucket");
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
| **rateLimitSid** | **String**| The Twilio-provided string that uniquely identifies the Rate Limit resource. | |
| **sid** | **String**| A 34 character string that uniquely identifies this Bucket. | |

### Return type

[**VerifyV2ServiceRateLimitBucket**](VerifyV2ServiceRateLimitBucket.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listBucket"></a>
# **listBucket**
> ListBucketResponse listBucket(serviceSid, rateLimitSid, pageSize, page, pageToken)



Retrieve a list of all Buckets for a Rate Limit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2BucketApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2BucketApi apiInstance = new VerifyV2BucketApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    String rateLimitSid = "rateLimitSid_example"; // String | The Twilio-provided string that uniquely identifies the Rate Limit resource.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListBucketResponse result = apiInstance.listBucket(serviceSid, rateLimitSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2BucketApi#listBucket");
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
| **rateLimitSid** | **String**| The Twilio-provided string that uniquely identifies the Rate Limit resource. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListBucketResponse**](ListBucketResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateBucket"></a>
# **updateBucket**
> VerifyV2ServiceRateLimitBucket updateBucket(serviceSid, rateLimitSid, sid, interval, max)



Update a specific Bucket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2BucketApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2BucketApi apiInstance = new VerifyV2BucketApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    String rateLimitSid = "rateLimitSid_example"; // String | The Twilio-provided string that uniquely identifies the Rate Limit resource.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this Bucket.
    Integer interval = 56; // Integer | Number of seconds that the rate limit will be enforced over.
    Integer max = 56; // Integer | Maximum number of requests permitted in during the interval.
    try {
      VerifyV2ServiceRateLimitBucket result = apiInstance.updateBucket(serviceSid, rateLimitSid, sid, interval, max);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2BucketApi#updateBucket");
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
| **rateLimitSid** | **String**| The Twilio-provided string that uniquely identifies the Rate Limit resource. | |
| **sid** | **String**| A 34 character string that uniquely identifies this Bucket. | |
| **interval** | **Integer**| Number of seconds that the rate limit will be enforced over. | [optional] |
| **max** | **Integer**| Maximum number of requests permitted in during the interval. | [optional] |

### Return type

[**VerifyV2ServiceRateLimitBucket**](VerifyV2ServiceRateLimitBucket.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

