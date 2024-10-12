# SupersimV1NetworkAccessProfileApi

All URIs are relative to *https://supersim.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkAccessProfile**](SupersimV1NetworkAccessProfileApi.md#createNetworkAccessProfile) | **POST** /v1/NetworkAccessProfiles |  |
| [**fetchNetworkAccessProfile**](SupersimV1NetworkAccessProfileApi.md#fetchNetworkAccessProfile) | **GET** /v1/NetworkAccessProfiles/{Sid} |  |
| [**listNetworkAccessProfile**](SupersimV1NetworkAccessProfileApi.md#listNetworkAccessProfile) | **GET** /v1/NetworkAccessProfiles |  |
| [**updateNetworkAccessProfile**](SupersimV1NetworkAccessProfileApi.md#updateNetworkAccessProfile) | **POST** /v1/NetworkAccessProfiles/{Sid} |  |


<a id="createNetworkAccessProfile"></a>
# **createNetworkAccessProfile**
> SupersimV1NetworkAccessProfile createNetworkAccessProfile(networks, uniqueName)



Create a new Network Access Profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1NetworkAccessProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1NetworkAccessProfileApi apiInstance = new SupersimV1NetworkAccessProfileApi(defaultClient);
    List<String> networks = Arrays.asList(); // List<String> | List of Network SIDs that this Network Access Profile will allow connections to.
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
    try {
      SupersimV1NetworkAccessProfile result = apiInstance.createNetworkAccessProfile(networks, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1NetworkAccessProfileApi#createNetworkAccessProfile");
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
| **networks** | [**List&lt;String&gt;**](String.md)| List of Network SIDs that this Network Access Profile will allow connections to. | [optional] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource. | [optional] |

### Return type

[**SupersimV1NetworkAccessProfile**](SupersimV1NetworkAccessProfile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchNetworkAccessProfile"></a>
# **fetchNetworkAccessProfile**
> SupersimV1NetworkAccessProfile fetchNetworkAccessProfile(sid)



Fetch a Network Access Profile instance from your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1NetworkAccessProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1NetworkAccessProfileApi apiInstance = new SupersimV1NetworkAccessProfileApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Network Access Profile resource to fetch.
    try {
      SupersimV1NetworkAccessProfile result = apiInstance.fetchNetworkAccessProfile(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1NetworkAccessProfileApi#fetchNetworkAccessProfile");
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
| **sid** | **String**| The SID of the Network Access Profile resource to fetch. | |

### Return type

[**SupersimV1NetworkAccessProfile**](SupersimV1NetworkAccessProfile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listNetworkAccessProfile"></a>
# **listNetworkAccessProfile**
> ListNetworkAccessProfileResponse listNetworkAccessProfile(pageSize, page, pageToken)



Retrieve a list of Network Access Profiles from your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1NetworkAccessProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1NetworkAccessProfileApi apiInstance = new SupersimV1NetworkAccessProfileApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListNetworkAccessProfileResponse result = apiInstance.listNetworkAccessProfile(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1NetworkAccessProfileApi#listNetworkAccessProfile");
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

[**ListNetworkAccessProfileResponse**](ListNetworkAccessProfileResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateNetworkAccessProfile"></a>
# **updateNetworkAccessProfile**
> SupersimV1NetworkAccessProfile updateNetworkAccessProfile(sid, uniqueName)



Updates the given properties of a Network Access Profile in your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1NetworkAccessProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1NetworkAccessProfileApi apiInstance = new SupersimV1NetworkAccessProfileApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Network Access Profile to update.
    String uniqueName = "uniqueName_example"; // String | The new unique name of the Network Access Profile.
    try {
      SupersimV1NetworkAccessProfile result = apiInstance.updateNetworkAccessProfile(sid, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1NetworkAccessProfileApi#updateNetworkAccessProfile");
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
| **sid** | **String**| The SID of the Network Access Profile to update. | |
| **uniqueName** | **String**| The new unique name of the Network Access Profile. | [optional] |

### Return type

[**SupersimV1NetworkAccessProfile**](SupersimV1NetworkAccessProfile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

