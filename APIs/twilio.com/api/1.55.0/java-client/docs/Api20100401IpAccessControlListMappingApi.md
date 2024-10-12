# Api20100401IpAccessControlListMappingApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSipIpAccessControlListMapping**](Api20100401IpAccessControlListMappingApi.md#createSipIpAccessControlListMapping) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings.json |  |
| [**deleteSipIpAccessControlListMapping**](Api20100401IpAccessControlListMappingApi.md#deleteSipIpAccessControlListMapping) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings/{Sid}.json |  |
| [**fetchSipIpAccessControlListMapping**](Api20100401IpAccessControlListMappingApi.md#fetchSipIpAccessControlListMapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings/{Sid}.json |  |
| [**listSipIpAccessControlListMapping**](Api20100401IpAccessControlListMappingApi.md#listSipIpAccessControlListMapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings.json |  |


<a id="createSipIpAccessControlListMapping"></a>
# **createSipIpAccessControlListMapping**
> ApiV2010AccountSipSipDomainSipIpAccessControlListMapping createSipIpAccessControlListMapping(accountSid, domainSid, ipAccessControlListSid)



Create a new IpAccessControlListMapping resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IpAccessControlListMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IpAccessControlListMappingApi apiInstance = new Api20100401IpAccessControlListMappingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
    String domainSid = "domainSid_example"; // String | A 34 character string that uniquely identifies the SIP domain.
    String ipAccessControlListSid = "ipAccessControlListSid_example"; // String | The unique id of the IP access control list to map to the SIP domain.
    try {
      ApiV2010AccountSipSipDomainSipIpAccessControlListMapping result = apiInstance.createSipIpAccessControlListMapping(accountSid, domainSid, ipAccessControlListSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IpAccessControlListMappingApi#createSipIpAccessControlListMapping");
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
| **domainSid** | **String**| A 34 character string that uniquely identifies the SIP domain. | |
| **ipAccessControlListSid** | **String**| The unique id of the IP access control list to map to the SIP domain. | |

### Return type

[**ApiV2010AccountSipSipDomainSipIpAccessControlListMapping**](ApiV2010AccountSipSipDomainSipIpAccessControlListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSipIpAccessControlListMapping"></a>
# **deleteSipIpAccessControlListMapping**
> deleteSipIpAccessControlListMapping(accountSid, domainSid, sid)



Delete an IpAccessControlListMapping resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IpAccessControlListMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IpAccessControlListMappingApi apiInstance = new Api20100401IpAccessControlListMappingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
    String domainSid = "domainSid_example"; // String | A 34 character string that uniquely identifies the SIP domain.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies the resource to delete.
    try {
      apiInstance.deleteSipIpAccessControlListMapping(accountSid, domainSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IpAccessControlListMappingApi#deleteSipIpAccessControlListMapping");
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
| **domainSid** | **String**| A 34 character string that uniquely identifies the SIP domain. | |
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

<a id="fetchSipIpAccessControlListMapping"></a>
# **fetchSipIpAccessControlListMapping**
> ApiV2010AccountSipSipDomainSipIpAccessControlListMapping fetchSipIpAccessControlListMapping(accountSid, domainSid, sid)



Fetch an IpAccessControlListMapping resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IpAccessControlListMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IpAccessControlListMappingApi apiInstance = new Api20100401IpAccessControlListMappingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
    String domainSid = "domainSid_example"; // String | A 34 character string that uniquely identifies the SIP domain.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies the resource to fetch.
    try {
      ApiV2010AccountSipSipDomainSipIpAccessControlListMapping result = apiInstance.fetchSipIpAccessControlListMapping(accountSid, domainSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IpAccessControlListMappingApi#fetchSipIpAccessControlListMapping");
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
| **domainSid** | **String**| A 34 character string that uniquely identifies the SIP domain. | |
| **sid** | **String**| A 34 character string that uniquely identifies the resource to fetch. | |

### Return type

[**ApiV2010AccountSipSipDomainSipIpAccessControlListMapping**](ApiV2010AccountSipSipDomainSipIpAccessControlListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSipIpAccessControlListMapping"></a>
# **listSipIpAccessControlListMapping**
> ListSipIpAccessControlListMappingResponse listSipIpAccessControlListMapping(accountSid, domainSid, pageSize, page, pageToken)



Retrieve a list of IpAccessControlListMapping resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401IpAccessControlListMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401IpAccessControlListMappingApi apiInstance = new Api20100401IpAccessControlListMappingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
    String domainSid = "domainSid_example"; // String | A 34 character string that uniquely identifies the SIP domain.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSipIpAccessControlListMappingResponse result = apiInstance.listSipIpAccessControlListMapping(accountSid, domainSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401IpAccessControlListMappingApi#listSipIpAccessControlListMapping");
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
| **domainSid** | **String**| A 34 character string that uniquely identifies the SIP domain. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSipIpAccessControlListMappingResponse**](ListSipIpAccessControlListMappingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

