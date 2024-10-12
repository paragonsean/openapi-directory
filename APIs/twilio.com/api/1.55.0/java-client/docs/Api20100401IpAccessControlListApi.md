# Api20100401IpAccessControlListApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSipIpAccessControlList**](Api20100401IpAccessControlListApi.md#createSipIpAccessControlList) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists.json |  |
| [**deleteSipIpAccessControlList**](Api20100401IpAccessControlListApi.md#deleteSipIpAccessControlList) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{Sid}.json |  |
| [**fetchSipIpAccessControlList**](Api20100401IpAccessControlListApi.md#fetchSipIpAccessControlList) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{Sid}.json |  |
| [**listSipIpAccessControlList**](Api20100401IpAccessControlListApi.md#listSipIpAccessControlList) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists.json |  |
| [**updateSipIpAccessControlList**](Api20100401IpAccessControlListApi.md#updateSipIpAccessControlList) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{Sid}.json |  |


<a id="createSipIpAccessControlList"></a>
# **createSipIpAccessControlList**
> ApiV2010AccountSipSipIpAccessControlList createSipIpAccessControlList(accountSid, friendlyName)



Create a new IpAccessControlList resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IpAccessControlListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IpAccessControlListApi apiInstance = new Api20100401IpAccessControlListApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    String friendlyName = "friendlyName_example"; // String | A human readable descriptive text that describes the IpAccessControlList, up to 255 characters long.
    try {
      ApiV2010AccountSipSipIpAccessControlList result = apiInstance.createSipIpAccessControlList(accountSid, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IpAccessControlListApi#createSipIpAccessControlList");
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
| **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | |
| **friendlyName** | **String**| A human readable descriptive text that describes the IpAccessControlList, up to 255 characters long. | |

### Return type

[**ApiV2010AccountSipSipIpAccessControlList**](ApiV2010AccountSipSipIpAccessControlList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSipIpAccessControlList"></a>
# **deleteSipIpAccessControlList**
> deleteSipIpAccessControlList(accountSid, sid)



Delete an IpAccessControlList from the requested account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IpAccessControlListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IpAccessControlListApi apiInstance = new Api20100401IpAccessControlListApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies the resource to delete.
    try {
      apiInstance.deleteSipIpAccessControlList(accountSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IpAccessControlListApi#deleteSipIpAccessControlList");
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
| **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | |
| **sid** | **String**| A 34 character string that uniquely identifies the resource to delete. | |

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

<a id="fetchSipIpAccessControlList"></a>
# **fetchSipIpAccessControlList**
> ApiV2010AccountSipSipIpAccessControlList fetchSipIpAccessControlList(accountSid, sid)



Fetch a specific instance of an IpAccessControlList

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IpAccessControlListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IpAccessControlListApi apiInstance = new Api20100401IpAccessControlListApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies the resource to fetch.
    try {
      ApiV2010AccountSipSipIpAccessControlList result = apiInstance.fetchSipIpAccessControlList(accountSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IpAccessControlListApi#fetchSipIpAccessControlList");
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
| **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | |
| **sid** | **String**| A 34 character string that uniquely identifies the resource to fetch. | |

### Return type

[**ApiV2010AccountSipSipIpAccessControlList**](ApiV2010AccountSipSipIpAccessControlList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSipIpAccessControlList"></a>
# **listSipIpAccessControlList**
> ListSipIpAccessControlListResponse listSipIpAccessControlList(accountSid, pageSize, page, pageToken)



Retrieve a list of IpAccessControlLists that belong to the account used to make the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IpAccessControlListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IpAccessControlListApi apiInstance = new Api20100401IpAccessControlListApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSipIpAccessControlListResponse result = apiInstance.listSipIpAccessControlList(accountSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IpAccessControlListApi#listSipIpAccessControlList");
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
| **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSipIpAccessControlListResponse**](ListSipIpAccessControlListResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSipIpAccessControlList"></a>
# **updateSipIpAccessControlList**
> ApiV2010AccountSipSipIpAccessControlList updateSipIpAccessControlList(accountSid, sid, friendlyName)



Rename an IpAccessControlList

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IpAccessControlListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IpAccessControlListApi apiInstance = new Api20100401IpAccessControlListApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies the resource to udpate.
    String friendlyName = "friendlyName_example"; // String | A human readable descriptive text, up to 255 characters long.
    try {
      ApiV2010AccountSipSipIpAccessControlList result = apiInstance.updateSipIpAccessControlList(accountSid, sid, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IpAccessControlListApi#updateSipIpAccessControlList");
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
| **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | |
| **sid** | **String**| A 34 character string that uniquely identifies the resource to udpate. | |
| **friendlyName** | **String**| A human readable descriptive text, up to 255 characters long. | |

### Return type

[**ApiV2010AccountSipSipIpAccessControlList**](ApiV2010AccountSipSipIpAccessControlList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

