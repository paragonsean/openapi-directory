# SupersimV1NetworkAccessProfileNetworkApi

All URIs are relative to *https://supersim.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkAccessProfileNetwork**](SupersimV1NetworkAccessProfileNetworkApi.md#createNetworkAccessProfileNetwork) | **POST** /v1/NetworkAccessProfiles/{NetworkAccessProfileSid}/Networks |  |
| [**deleteNetworkAccessProfileNetwork**](SupersimV1NetworkAccessProfileNetworkApi.md#deleteNetworkAccessProfileNetwork) | **DELETE** /v1/NetworkAccessProfiles/{NetworkAccessProfileSid}/Networks/{Sid} |  |
| [**fetchNetworkAccessProfileNetwork**](SupersimV1NetworkAccessProfileNetworkApi.md#fetchNetworkAccessProfileNetwork) | **GET** /v1/NetworkAccessProfiles/{NetworkAccessProfileSid}/Networks/{Sid} |  |
| [**listNetworkAccessProfileNetwork**](SupersimV1NetworkAccessProfileNetworkApi.md#listNetworkAccessProfileNetwork) | **GET** /v1/NetworkAccessProfiles/{NetworkAccessProfileSid}/Networks |  |


<a id="createNetworkAccessProfileNetwork"></a>
# **createNetworkAccessProfileNetwork**
> SupersimV1NetworkAccessProfileNetworkAccessProfileNetwork createNetworkAccessProfileNetwork(networkAccessProfileSid, network)



Add a Network resource to the Network Access Profile resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1NetworkAccessProfileNetworkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1NetworkAccessProfileNetworkApi apiInstance = new SupersimV1NetworkAccessProfileNetworkApi(defaultClient);
    String networkAccessProfileSid = "networkAccessProfileSid_example"; // String | The unique string that identifies the Network Access Profile resource.
    String network = "network_example"; // String | The SID of the Network resource to be added to the Network Access Profile resource.
    try {
      SupersimV1NetworkAccessProfileNetworkAccessProfileNetwork result = apiInstance.createNetworkAccessProfileNetwork(networkAccessProfileSid, network);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1NetworkAccessProfileNetworkApi#createNetworkAccessProfileNetwork");
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
| **networkAccessProfileSid** | **String**| The unique string that identifies the Network Access Profile resource. | |
| **network** | **String**| The SID of the Network resource to be added to the Network Access Profile resource. | |

### Return type

[**SupersimV1NetworkAccessProfileNetworkAccessProfileNetwork**](SupersimV1NetworkAccessProfileNetworkAccessProfileNetwork.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteNetworkAccessProfileNetwork"></a>
# **deleteNetworkAccessProfileNetwork**
> deleteNetworkAccessProfileNetwork(networkAccessProfileSid, sid)



Remove a Network resource from the Network Access Profile resource&#39;s.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1NetworkAccessProfileNetworkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1NetworkAccessProfileNetworkApi apiInstance = new SupersimV1NetworkAccessProfileNetworkApi(defaultClient);
    String networkAccessProfileSid = "networkAccessProfileSid_example"; // String | The unique string that identifies the Network Access Profile resource.
    String sid = "sid_example"; // String | The SID of the Network resource to be removed from the Network Access Profile resource.
    try {
      apiInstance.deleteNetworkAccessProfileNetwork(networkAccessProfileSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1NetworkAccessProfileNetworkApi#deleteNetworkAccessProfileNetwork");
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
| **networkAccessProfileSid** | **String**| The unique string that identifies the Network Access Profile resource. | |
| **sid** | **String**| The SID of the Network resource to be removed from the Network Access Profile resource. | |

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

<a id="fetchNetworkAccessProfileNetwork"></a>
# **fetchNetworkAccessProfileNetwork**
> SupersimV1NetworkAccessProfileNetworkAccessProfileNetwork fetchNetworkAccessProfileNetwork(networkAccessProfileSid, sid)



Fetch a Network Access Profile resource&#39;s Network resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1NetworkAccessProfileNetworkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1NetworkAccessProfileNetworkApi apiInstance = new SupersimV1NetworkAccessProfileNetworkApi(defaultClient);
    String networkAccessProfileSid = "networkAccessProfileSid_example"; // String | The unique string that identifies the Network Access Profile resource.
    String sid = "sid_example"; // String | The SID of the Network resource to fetch.
    try {
      SupersimV1NetworkAccessProfileNetworkAccessProfileNetwork result = apiInstance.fetchNetworkAccessProfileNetwork(networkAccessProfileSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1NetworkAccessProfileNetworkApi#fetchNetworkAccessProfileNetwork");
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
| **networkAccessProfileSid** | **String**| The unique string that identifies the Network Access Profile resource. | |
| **sid** | **String**| The SID of the Network resource to fetch. | |

### Return type

[**SupersimV1NetworkAccessProfileNetworkAccessProfileNetwork**](SupersimV1NetworkAccessProfileNetworkAccessProfileNetwork.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listNetworkAccessProfileNetwork"></a>
# **listNetworkAccessProfileNetwork**
> ListNetworkAccessProfileNetworkResponse listNetworkAccessProfileNetwork(networkAccessProfileSid, pageSize, page, pageToken)



Retrieve a list of Network Access Profile resource&#39;s Network resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1NetworkAccessProfileNetworkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1NetworkAccessProfileNetworkApi apiInstance = new SupersimV1NetworkAccessProfileNetworkApi(defaultClient);
    String networkAccessProfileSid = "networkAccessProfileSid_example"; // String | The unique string that identifies the Network Access Profile resource.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListNetworkAccessProfileNetworkResponse result = apiInstance.listNetworkAccessProfileNetwork(networkAccessProfileSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1NetworkAccessProfileNetworkApi#listNetworkAccessProfileNetwork");
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
| **networkAccessProfileSid** | **String**| The unique string that identifies the Network Access Profile resource. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListNetworkAccessProfileNetworkResponse**](ListNetworkAccessProfileNetworkResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

