# Api20100401CredentialListApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSipCredentialList**](Api20100401CredentialListApi.md#createSipCredentialList) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists.json |  |
| [**deleteSipCredentialList**](Api20100401CredentialListApi.md#deleteSipCredentialList) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{Sid}.json |  |
| [**fetchSipCredentialList**](Api20100401CredentialListApi.md#fetchSipCredentialList) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{Sid}.json |  |
| [**listSipCredentialList**](Api20100401CredentialListApi.md#listSipCredentialList) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists.json |  |
| [**updateSipCredentialList**](Api20100401CredentialListApi.md#updateSipCredentialList) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{Sid}.json |  |


<a id="createSipCredentialList"></a>
# **createSipCredentialList**
> ApiV2010AccountSipSipCredentialList createSipCredentialList(accountSid, friendlyName)



Create a Credential List

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401CredentialListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401CredentialListApi apiInstance = new Api20100401CredentialListApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
    String friendlyName = "friendlyName_example"; // String | A human readable descriptive text that describes the CredentialList, up to 64 characters long.
    try {
      ApiV2010AccountSipSipCredentialList result = apiInstance.createSipCredentialList(accountSid, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401CredentialListApi#createSipCredentialList");
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
| **accountSid** | **String**| The unique id of the Account that is responsible for this resource. | |
| **friendlyName** | **String**| A human readable descriptive text that describes the CredentialList, up to 64 characters long. | |

### Return type

[**ApiV2010AccountSipSipCredentialList**](ApiV2010AccountSipSipCredentialList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSipCredentialList"></a>
# **deleteSipCredentialList**
> deleteSipCredentialList(accountSid, sid)



Delete a Credential List

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401CredentialListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401CredentialListApi apiInstance = new Api20100401CredentialListApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
    String sid = "sid_example"; // String | The credential list Sid that uniquely identifies this resource
    try {
      apiInstance.deleteSipCredentialList(accountSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401CredentialListApi#deleteSipCredentialList");
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
| **accountSid** | **String**| The unique id of the Account that is responsible for this resource. | |
| **sid** | **String**| The credential list Sid that uniquely identifies this resource | |

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

<a id="fetchSipCredentialList"></a>
# **fetchSipCredentialList**
> ApiV2010AccountSipSipCredentialList fetchSipCredentialList(accountSid, sid)



Get a Credential List

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401CredentialListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401CredentialListApi apiInstance = new Api20100401CredentialListApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
    String sid = "sid_example"; // String | The credential list Sid that uniquely identifies this resource
    try {
      ApiV2010AccountSipSipCredentialList result = apiInstance.fetchSipCredentialList(accountSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401CredentialListApi#fetchSipCredentialList");
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
| **accountSid** | **String**| The unique id of the Account that is responsible for this resource. | |
| **sid** | **String**| The credential list Sid that uniquely identifies this resource | |

### Return type

[**ApiV2010AccountSipSipCredentialList**](ApiV2010AccountSipSipCredentialList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSipCredentialList"></a>
# **listSipCredentialList**
> ListSipCredentialListResponse listSipCredentialList(accountSid, pageSize, page, pageToken)



Get All Credential Lists

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401CredentialListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401CredentialListApi apiInstance = new Api20100401CredentialListApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSipCredentialListResponse result = apiInstance.listSipCredentialList(accountSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401CredentialListApi#listSipCredentialList");
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
| **accountSid** | **String**| The unique id of the Account that is responsible for this resource. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSipCredentialListResponse**](ListSipCredentialListResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSipCredentialList"></a>
# **updateSipCredentialList**
> ApiV2010AccountSipSipCredentialList updateSipCredentialList(accountSid, sid, friendlyName)



Update a Credential List

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401CredentialListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401CredentialListApi apiInstance = new Api20100401CredentialListApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
    String sid = "sid_example"; // String | The credential list Sid that uniquely identifies this resource
    String friendlyName = "friendlyName_example"; // String | A human readable descriptive text for a CredentialList, up to 64 characters long.
    try {
      ApiV2010AccountSipSipCredentialList result = apiInstance.updateSipCredentialList(accountSid, sid, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401CredentialListApi#updateSipCredentialList");
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
| **accountSid** | **String**| The unique id of the Account that is responsible for this resource. | |
| **sid** | **String**| The credential list Sid that uniquely identifies this resource | |
| **friendlyName** | **String**| A human readable descriptive text for a CredentialList, up to 64 characters long. | |

### Return type

[**ApiV2010AccountSipSipCredentialList**](ApiV2010AccountSipSipCredentialList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

