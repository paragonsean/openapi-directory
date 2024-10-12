# TrunkingV1CredentialListApi

All URIs are relative to *https://trunking.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCredentialList**](TrunkingV1CredentialListApi.md#createCredentialList) | **POST** /v1/Trunks/{TrunkSid}/CredentialLists |  |
| [**deleteCredentialList**](TrunkingV1CredentialListApi.md#deleteCredentialList) | **DELETE** /v1/Trunks/{TrunkSid}/CredentialLists/{Sid} |  |
| [**fetchCredentialList**](TrunkingV1CredentialListApi.md#fetchCredentialList) | **GET** /v1/Trunks/{TrunkSid}/CredentialLists/{Sid} |  |
| [**listCredentialList**](TrunkingV1CredentialListApi.md#listCredentialList) | **GET** /v1/Trunks/{TrunkSid}/CredentialLists |  |


<a id="createCredentialList"></a>
# **createCredentialList**
> TrunkingV1TrunkCredentialList createCredentialList(trunkSid, credentialListSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1CredentialListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1CredentialListApi apiInstance = new TrunkingV1CredentialListApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk to associate the credential list with.
    String credentialListSid = "credentialListSid_example"; // String | The SID of the [Credential List](https://www.twilio.com/docs/voice/sip/api/sip-credentiallist-resource) that you want to associate with the trunk. Once associated, we will authenticate access to the trunk against this list.
    try {
      TrunkingV1TrunkCredentialList result = apiInstance.createCredentialList(trunkSid, credentialListSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1CredentialListApi#createCredentialList");
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
| **trunkSid** | **String**| The SID of the Trunk to associate the credential list with. | |
| **credentialListSid** | **String**| The SID of the [Credential List](https://www.twilio.com/docs/voice/sip/api/sip-credentiallist-resource) that you want to associate with the trunk. Once associated, we will authenticate access to the trunk against this list. | |

### Return type

[**TrunkingV1TrunkCredentialList**](TrunkingV1TrunkCredentialList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteCredentialList"></a>
# **deleteCredentialList**
> deleteCredentialList(trunkSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1CredentialListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1CredentialListApi apiInstance = new TrunkingV1CredentialListApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to delete the credential list.
    String sid = "sid_example"; // String | The unique string that we created to identify the CredentialList resource to delete.
    try {
      apiInstance.deleteCredentialList(trunkSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1CredentialListApi#deleteCredentialList");
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
| **trunkSid** | **String**| The SID of the Trunk from which to delete the credential list. | |
| **sid** | **String**| The unique string that we created to identify the CredentialList resource to delete. | |

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

<a id="fetchCredentialList"></a>
# **fetchCredentialList**
> TrunkingV1TrunkCredentialList fetchCredentialList(trunkSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1CredentialListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1CredentialListApi apiInstance = new TrunkingV1CredentialListApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to fetch the credential list.
    String sid = "sid_example"; // String | The unique string that we created to identify the CredentialList resource to fetch.
    try {
      TrunkingV1TrunkCredentialList result = apiInstance.fetchCredentialList(trunkSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1CredentialListApi#fetchCredentialList");
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
| **trunkSid** | **String**| The SID of the Trunk from which to fetch the credential list. | |
| **sid** | **String**| The unique string that we created to identify the CredentialList resource to fetch. | |

### Return type

[**TrunkingV1TrunkCredentialList**](TrunkingV1TrunkCredentialList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listCredentialList"></a>
# **listCredentialList**
> ListCredentialListResponse listCredentialList(trunkSid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1CredentialListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1CredentialListApi apiInstance = new TrunkingV1CredentialListApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to read the credential lists.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListCredentialListResponse result = apiInstance.listCredentialList(trunkSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1CredentialListApi#listCredentialList");
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
| **trunkSid** | **String**| The SID of the Trunk from which to read the credential lists. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListCredentialListResponse**](ListCredentialListResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

