# Api20100401AuthCallsIpAccessControlListMappingApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSipAuthCallsIpAccessControlListMapping**](Api20100401AuthCallsIpAccessControlListMappingApi.md#createSipAuthCallsIpAccessControlListMapping) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/IpAccessControlListMappings.json |  |
| [**deleteSipAuthCallsIpAccessControlListMapping**](Api20100401AuthCallsIpAccessControlListMappingApi.md#deleteSipAuthCallsIpAccessControlListMapping) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/IpAccessControlListMappings/{Sid}.json |  |
| [**fetchSipAuthCallsIpAccessControlListMapping**](Api20100401AuthCallsIpAccessControlListMappingApi.md#fetchSipAuthCallsIpAccessControlListMapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/IpAccessControlListMappings/{Sid}.json |  |
| [**listSipAuthCallsIpAccessControlListMapping**](Api20100401AuthCallsIpAccessControlListMappingApi.md#listSipAuthCallsIpAccessControlListMapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/IpAccessControlListMappings.json |  |


<a id="createSipAuthCallsIpAccessControlListMapping"></a>
# **createSipAuthCallsIpAccessControlListMapping**
> ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping createSipAuthCallsIpAccessControlListMapping(accountSid, domainSid, ipAccessControlListSid)



Create a new IP Access Control List mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AuthCallsIpAccessControlListMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AuthCallsIpAccessControlListMappingApi apiInstance = new Api20100401AuthCallsIpAccessControlListMappingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    String domainSid = "domainSid_example"; // String | The SID of the SIP domain that will contain the new resource.
    String ipAccessControlListSid = "ipAccessControlListSid_example"; // String | The SID of the IpAccessControlList resource to map to the SIP domain.
    try {
      ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping result = apiInstance.createSipAuthCallsIpAccessControlListMapping(accountSid, domainSid, ipAccessControlListSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AuthCallsIpAccessControlListMappingApi#createSipAuthCallsIpAccessControlListMapping");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. | |
| **domainSid** | **String**| The SID of the SIP domain that will contain the new resource. | |
| **ipAccessControlListSid** | **String**| The SID of the IpAccessControlList resource to map to the SIP domain. | |

### Return type

[**ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping**](ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSipAuthCallsIpAccessControlListMapping"></a>
# **deleteSipAuthCallsIpAccessControlListMapping**
> deleteSipAuthCallsIpAccessControlListMapping(accountSid, domainSid, sid)



Delete an IP Access Control List mapping from the requested domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AuthCallsIpAccessControlListMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AuthCallsIpAccessControlListMappingApi apiInstance = new Api20100401AuthCallsIpAccessControlListMappingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resources to delete.
    String domainSid = "domainSid_example"; // String | The SID of the SIP domain that contains the resources to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the IpAccessControlListMapping resource to delete.
    try {
      apiInstance.deleteSipAuthCallsIpAccessControlListMapping(accountSid, domainSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AuthCallsIpAccessControlListMappingApi#deleteSipAuthCallsIpAccessControlListMapping");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resources to delete. | |
| **domainSid** | **String**| The SID of the SIP domain that contains the resources to delete. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the IpAccessControlListMapping resource to delete. | |

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

<a id="fetchSipAuthCallsIpAccessControlListMapping"></a>
# **fetchSipAuthCallsIpAccessControlListMapping**
> ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping fetchSipAuthCallsIpAccessControlListMapping(accountSid, domainSid, sid)



Fetch a specific instance of an IP Access Control List mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AuthCallsIpAccessControlListMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AuthCallsIpAccessControlListMappingApi apiInstance = new Api20100401AuthCallsIpAccessControlListMappingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resource to fetch.
    String domainSid = "domainSid_example"; // String | The SID of the SIP domain that contains the resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the IpAccessControlListMapping resource to fetch.
    try {
      ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping result = apiInstance.fetchSipAuthCallsIpAccessControlListMapping(accountSid, domainSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AuthCallsIpAccessControlListMappingApi#fetchSipAuthCallsIpAccessControlListMapping");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resource to fetch. | |
| **domainSid** | **String**| The SID of the SIP domain that contains the resource to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the IpAccessControlListMapping resource to fetch. | |

### Return type

[**ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping**](ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSipAuthCallsIpAccessControlListMapping"></a>
# **listSipAuthCallsIpAccessControlListMapping**
> ListSipAuthCallsIpAccessControlListMappingResponse listSipAuthCallsIpAccessControlListMapping(accountSid, domainSid, pageSize, page, pageToken)



Retrieve a list of IP Access Control List mappings belonging to the domain used in the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AuthCallsIpAccessControlListMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AuthCallsIpAccessControlListMappingApi apiInstance = new Api20100401AuthCallsIpAccessControlListMappingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resources to read.
    String domainSid = "domainSid_example"; // String | The SID of the SIP domain that contains the resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSipAuthCallsIpAccessControlListMappingResponse result = apiInstance.listSipAuthCallsIpAccessControlListMapping(accountSid, domainSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AuthCallsIpAccessControlListMappingApi#listSipAuthCallsIpAccessControlListMapping");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resources to read. | |
| **domainSid** | **String**| The SID of the SIP domain that contains the resources to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSipAuthCallsIpAccessControlListMappingResponse**](ListSipAuthCallsIpAccessControlListMappingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

