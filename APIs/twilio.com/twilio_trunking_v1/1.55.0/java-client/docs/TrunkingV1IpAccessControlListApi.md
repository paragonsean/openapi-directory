# TrunkingV1IpAccessControlListApi

All URIs are relative to *https://trunking.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createIpAccessControlList**](TrunkingV1IpAccessControlListApi.md#createIpAccessControlList) | **POST** /v1/Trunks/{TrunkSid}/IpAccessControlLists |  |
| [**deleteIpAccessControlList**](TrunkingV1IpAccessControlListApi.md#deleteIpAccessControlList) | **DELETE** /v1/Trunks/{TrunkSid}/IpAccessControlLists/{Sid} |  |
| [**fetchIpAccessControlList**](TrunkingV1IpAccessControlListApi.md#fetchIpAccessControlList) | **GET** /v1/Trunks/{TrunkSid}/IpAccessControlLists/{Sid} |  |
| [**listIpAccessControlList**](TrunkingV1IpAccessControlListApi.md#listIpAccessControlList) | **GET** /v1/Trunks/{TrunkSid}/IpAccessControlLists |  |


<a id="createIpAccessControlList"></a>
# **createIpAccessControlList**
> TrunkingV1TrunkIpAccessControlList createIpAccessControlList(trunkSid, ipAccessControlListSid)



Associate an IP Access Control List with a Trunk

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1IpAccessControlListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1IpAccessControlListApi apiInstance = new TrunkingV1IpAccessControlListApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk to associate the IP Access Control List with.
    String ipAccessControlListSid = "ipAccessControlListSid_example"; // String | The SID of the [IP Access Control List](https://www.twilio.com/docs/voice/sip/api/sip-ipaccesscontrollist-resource) that you want to associate with the trunk.
    try {
      TrunkingV1TrunkIpAccessControlList result = apiInstance.createIpAccessControlList(trunkSid, ipAccessControlListSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1IpAccessControlListApi#createIpAccessControlList");
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
| **trunkSid** | **String**| The SID of the Trunk to associate the IP Access Control List with. | |
| **ipAccessControlListSid** | **String**| The SID of the [IP Access Control List](https://www.twilio.com/docs/voice/sip/api/sip-ipaccesscontrollist-resource) that you want to associate with the trunk. | |

### Return type

[**TrunkingV1TrunkIpAccessControlList**](TrunkingV1TrunkIpAccessControlList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteIpAccessControlList"></a>
# **deleteIpAccessControlList**
> deleteIpAccessControlList(trunkSid, sid)



Remove an associated IP Access Control List from a Trunk

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1IpAccessControlListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1IpAccessControlListApi apiInstance = new TrunkingV1IpAccessControlListApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to delete the IP Access Control List.
    String sid = "sid_example"; // String | The unique string that we created to identify the IpAccessControlList resource to delete.
    try {
      apiInstance.deleteIpAccessControlList(trunkSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1IpAccessControlListApi#deleteIpAccessControlList");
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
| **trunkSid** | **String**| The SID of the Trunk from which to delete the IP Access Control List. | |
| **sid** | **String**| The unique string that we created to identify the IpAccessControlList resource to delete. | |

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

<a id="fetchIpAccessControlList"></a>
# **fetchIpAccessControlList**
> TrunkingV1TrunkIpAccessControlList fetchIpAccessControlList(trunkSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1IpAccessControlListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1IpAccessControlListApi apiInstance = new TrunkingV1IpAccessControlListApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to fetch the IP Access Control List.
    String sid = "sid_example"; // String | The unique string that we created to identify the IpAccessControlList resource to fetch.
    try {
      TrunkingV1TrunkIpAccessControlList result = apiInstance.fetchIpAccessControlList(trunkSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1IpAccessControlListApi#fetchIpAccessControlList");
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
| **trunkSid** | **String**| The SID of the Trunk from which to fetch the IP Access Control List. | |
| **sid** | **String**| The unique string that we created to identify the IpAccessControlList resource to fetch. | |

### Return type

[**TrunkingV1TrunkIpAccessControlList**](TrunkingV1TrunkIpAccessControlList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listIpAccessControlList"></a>
# **listIpAccessControlList**
> ListIpAccessControlListResponse listIpAccessControlList(trunkSid, pageSize, page, pageToken)



List all IP Access Control Lists for a Trunk

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1IpAccessControlListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1IpAccessControlListApi apiInstance = new TrunkingV1IpAccessControlListApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to read the IP Access Control Lists.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListIpAccessControlListResponse result = apiInstance.listIpAccessControlList(trunkSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1IpAccessControlListApi#listIpAccessControlList");
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
| **trunkSid** | **String**| The SID of the Trunk from which to read the IP Access Control Lists. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListIpAccessControlListResponse**](ListIpAccessControlListResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

