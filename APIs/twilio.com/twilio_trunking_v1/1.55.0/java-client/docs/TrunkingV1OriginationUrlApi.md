# TrunkingV1OriginationUrlApi

All URIs are relative to *https://trunking.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOriginationUrl**](TrunkingV1OriginationUrlApi.md#createOriginationUrl) | **POST** /v1/Trunks/{TrunkSid}/OriginationUrls |  |
| [**deleteOriginationUrl**](TrunkingV1OriginationUrlApi.md#deleteOriginationUrl) | **DELETE** /v1/Trunks/{TrunkSid}/OriginationUrls/{Sid} |  |
| [**fetchOriginationUrl**](TrunkingV1OriginationUrlApi.md#fetchOriginationUrl) | **GET** /v1/Trunks/{TrunkSid}/OriginationUrls/{Sid} |  |
| [**listOriginationUrl**](TrunkingV1OriginationUrlApi.md#listOriginationUrl) | **GET** /v1/Trunks/{TrunkSid}/OriginationUrls |  |
| [**updateOriginationUrl**](TrunkingV1OriginationUrlApi.md#updateOriginationUrl) | **POST** /v1/Trunks/{TrunkSid}/OriginationUrls/{Sid} |  |


<a id="createOriginationUrl"></a>
# **createOriginationUrl**
> TrunkingV1TrunkOriginationUrl createOriginationUrl(trunkSid, enabled, friendlyName, priority, sipUrl, weight)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1OriginationUrlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1OriginationUrlApi apiInstance = new TrunkingV1OriginationUrlApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk to associate the resource with.
    Boolean enabled = true; // Boolean | Whether the URL is enabled. The default is `true`.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    Integer priority = 56; // Integer | The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
    URI sipUrl = new URI(); // URI | The SIP address you want Twilio to route your Origination calls to. This must be a `sip:` schema.
    Integer weight = 56; // Integer | The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
    try {
      TrunkingV1TrunkOriginationUrl result = apiInstance.createOriginationUrl(trunkSid, enabled, friendlyName, priority, sipUrl, weight);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1OriginationUrlApi#createOriginationUrl");
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
| **trunkSid** | **String**| The SID of the Trunk to associate the resource with. | |
| **enabled** | **Boolean**| Whether the URL is enabled. The default is &#x60;true&#x60;. | |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | |
| **priority** | **Integer**| The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI. | |
| **sipUrl** | **URI**| The SIP address you want Twilio to route your Origination calls to. This must be a &#x60;sip:&#x60; schema. | |
| **weight** | **Integer**| The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority. | |

### Return type

[**TrunkingV1TrunkOriginationUrl**](TrunkingV1TrunkOriginationUrl.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteOriginationUrl"></a>
# **deleteOriginationUrl**
> deleteOriginationUrl(trunkSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1OriginationUrlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1OriginationUrlApi apiInstance = new TrunkingV1OriginationUrlApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to delete the OriginationUrl.
    String sid = "sid_example"; // String | The unique string that we created to identify the OriginationUrl resource to delete.
    try {
      apiInstance.deleteOriginationUrl(trunkSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1OriginationUrlApi#deleteOriginationUrl");
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
| **trunkSid** | **String**| The SID of the Trunk from which to delete the OriginationUrl. | |
| **sid** | **String**| The unique string that we created to identify the OriginationUrl resource to delete. | |

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

<a id="fetchOriginationUrl"></a>
# **fetchOriginationUrl**
> TrunkingV1TrunkOriginationUrl fetchOriginationUrl(trunkSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1OriginationUrlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1OriginationUrlApi apiInstance = new TrunkingV1OriginationUrlApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to fetch the OriginationUrl.
    String sid = "sid_example"; // String | The unique string that we created to identify the OriginationUrl resource to fetch.
    try {
      TrunkingV1TrunkOriginationUrl result = apiInstance.fetchOriginationUrl(trunkSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1OriginationUrlApi#fetchOriginationUrl");
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
| **trunkSid** | **String**| The SID of the Trunk from which to fetch the OriginationUrl. | |
| **sid** | **String**| The unique string that we created to identify the OriginationUrl resource to fetch. | |

### Return type

[**TrunkingV1TrunkOriginationUrl**](TrunkingV1TrunkOriginationUrl.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listOriginationUrl"></a>
# **listOriginationUrl**
> ListOriginationUrlResponse listOriginationUrl(trunkSid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1OriginationUrlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1OriginationUrlApi apiInstance = new TrunkingV1OriginationUrlApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to read the OriginationUrl.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListOriginationUrlResponse result = apiInstance.listOriginationUrl(trunkSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1OriginationUrlApi#listOriginationUrl");
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
| **trunkSid** | **String**| The SID of the Trunk from which to read the OriginationUrl. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListOriginationUrlResponse**](ListOriginationUrlResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateOriginationUrl"></a>
# **updateOriginationUrl**
> TrunkingV1TrunkOriginationUrl updateOriginationUrl(trunkSid, sid, enabled, friendlyName, priority, sipUrl, weight)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1OriginationUrlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1OriginationUrlApi apiInstance = new TrunkingV1OriginationUrlApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to update the OriginationUrl.
    String sid = "sid_example"; // String | The unique string that we created to identify the OriginationUrl resource to update.
    Boolean enabled = true; // Boolean | Whether the URL is enabled. The default is `true`.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    Integer priority = 56; // Integer | The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
    URI sipUrl = new URI(); // URI | The SIP address you want Twilio to route your Origination calls to. This must be a `sip:` schema. `sips` is NOT supported.
    Integer weight = 56; // Integer | The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
    try {
      TrunkingV1TrunkOriginationUrl result = apiInstance.updateOriginationUrl(trunkSid, sid, enabled, friendlyName, priority, sipUrl, weight);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1OriginationUrlApi#updateOriginationUrl");
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
| **trunkSid** | **String**| The SID of the Trunk from which to update the OriginationUrl. | |
| **sid** | **String**| The unique string that we created to identify the OriginationUrl resource to update. | |
| **enabled** | **Boolean**| Whether the URL is enabled. The default is &#x60;true&#x60;. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] |
| **priority** | **Integer**| The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI. | [optional] |
| **sipUrl** | **URI**| The SIP address you want Twilio to route your Origination calls to. This must be a &#x60;sip:&#x60; schema. &#x60;sips&#x60; is NOT supported. | [optional] |
| **weight** | **Integer**| The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority. | [optional] |

### Return type

[**TrunkingV1TrunkOriginationUrl**](TrunkingV1TrunkOriginationUrl.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

