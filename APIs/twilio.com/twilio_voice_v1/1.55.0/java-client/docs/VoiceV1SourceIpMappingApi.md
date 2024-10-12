# VoiceV1SourceIpMappingApi

All URIs are relative to *https://voice.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSourceIpMapping**](VoiceV1SourceIpMappingApi.md#createSourceIpMapping) | **POST** /v1/SourceIpMappings |  |
| [**deleteSourceIpMapping**](VoiceV1SourceIpMappingApi.md#deleteSourceIpMapping) | **DELETE** /v1/SourceIpMappings/{Sid} |  |
| [**fetchSourceIpMapping**](VoiceV1SourceIpMappingApi.md#fetchSourceIpMapping) | **GET** /v1/SourceIpMappings/{Sid} |  |
| [**listSourceIpMapping**](VoiceV1SourceIpMappingApi.md#listSourceIpMapping) | **GET** /v1/SourceIpMappings |  |
| [**updateSourceIpMapping**](VoiceV1SourceIpMappingApi.md#updateSourceIpMapping) | **POST** /v1/SourceIpMappings/{Sid} |  |


<a id="createSourceIpMapping"></a>
# **createSourceIpMapping**
> VoiceV1SourceIpMapping createSourceIpMapping(ipRecordSid, sipDomainSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1SourceIpMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1SourceIpMappingApi apiInstance = new VoiceV1SourceIpMappingApi(defaultClient);
    String ipRecordSid = "ipRecordSid_example"; // String | The Twilio-provided string that uniquely identifies the IP Record resource to map from.
    String sipDomainSid = "sipDomainSid_example"; // String | The SID of the SIP Domain that the IP Record should be mapped to.
    try {
      VoiceV1SourceIpMapping result = apiInstance.createSourceIpMapping(ipRecordSid, sipDomainSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1SourceIpMappingApi#createSourceIpMapping");
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
| **ipRecordSid** | **String**| The Twilio-provided string that uniquely identifies the IP Record resource to map from. | |
| **sipDomainSid** | **String**| The SID of the SIP Domain that the IP Record should be mapped to. | |

### Return type

[**VoiceV1SourceIpMapping**](VoiceV1SourceIpMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSourceIpMapping"></a>
# **deleteSourceIpMapping**
> deleteSourceIpMapping(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1SourceIpMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1SourceIpMappingApi apiInstance = new VoiceV1SourceIpMappingApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the IP Record resource to delete.
    try {
      apiInstance.deleteSourceIpMapping(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1SourceIpMappingApi#deleteSourceIpMapping");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the IP Record resource to delete. | |

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

<a id="fetchSourceIpMapping"></a>
# **fetchSourceIpMapping**
> VoiceV1SourceIpMapping fetchSourceIpMapping(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1SourceIpMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1SourceIpMappingApi apiInstance = new VoiceV1SourceIpMappingApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the IP Record resource to fetch.
    try {
      VoiceV1SourceIpMapping result = apiInstance.fetchSourceIpMapping(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1SourceIpMappingApi#fetchSourceIpMapping");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the IP Record resource to fetch. | |

### Return type

[**VoiceV1SourceIpMapping**](VoiceV1SourceIpMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSourceIpMapping"></a>
# **listSourceIpMapping**
> ListSourceIpMappingResponse listSourceIpMapping(pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1SourceIpMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1SourceIpMappingApi apiInstance = new VoiceV1SourceIpMappingApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSourceIpMappingResponse result = apiInstance.listSourceIpMapping(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1SourceIpMappingApi#listSourceIpMapping");
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

[**ListSourceIpMappingResponse**](ListSourceIpMappingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSourceIpMapping"></a>
# **updateSourceIpMapping**
> VoiceV1SourceIpMapping updateSourceIpMapping(sid, sipDomainSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1SourceIpMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1SourceIpMappingApi apiInstance = new VoiceV1SourceIpMappingApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the IP Record resource to update.
    String sipDomainSid = "sipDomainSid_example"; // String | The SID of the SIP Domain that the IP Record should be mapped to.
    try {
      VoiceV1SourceIpMapping result = apiInstance.updateSourceIpMapping(sid, sipDomainSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1SourceIpMappingApi#updateSourceIpMapping");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the IP Record resource to update. | |
| **sipDomainSid** | **String**| The SID of the SIP Domain that the IP Record should be mapped to. | |

### Return type

[**VoiceV1SourceIpMapping**](VoiceV1SourceIpMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

