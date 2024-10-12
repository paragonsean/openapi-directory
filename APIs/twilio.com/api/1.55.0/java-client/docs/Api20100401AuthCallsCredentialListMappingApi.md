# Api20100401AuthCallsCredentialListMappingApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSipAuthCallsCredentialListMapping**](Api20100401AuthCallsCredentialListMappingApi.md#createSipAuthCallsCredentialListMapping) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/CredentialListMappings.json |  |
| [**deleteSipAuthCallsCredentialListMapping**](Api20100401AuthCallsCredentialListMappingApi.md#deleteSipAuthCallsCredentialListMapping) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/CredentialListMappings/{Sid}.json |  |
| [**fetchSipAuthCallsCredentialListMapping**](Api20100401AuthCallsCredentialListMappingApi.md#fetchSipAuthCallsCredentialListMapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/CredentialListMappings/{Sid}.json |  |
| [**listSipAuthCallsCredentialListMapping**](Api20100401AuthCallsCredentialListMappingApi.md#listSipAuthCallsCredentialListMapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/CredentialListMappings.json |  |


<a id="createSipAuthCallsCredentialListMapping"></a>
# **createSipAuthCallsCredentialListMapping**
> ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsCredentialListMapping createSipAuthCallsCredentialListMapping(accountSid, domainSid, credentialListSid)



Create a new credential list mapping resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AuthCallsCredentialListMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AuthCallsCredentialListMappingApi apiInstance = new Api20100401AuthCallsCredentialListMappingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    String domainSid = "domainSid_example"; // String | The SID of the SIP domain that will contain the new resource.
    String credentialListSid = "credentialListSid_example"; // String | The SID of the CredentialList resource to map to the SIP domain.
    try {
      ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsCredentialListMapping result = apiInstance.createSipAuthCallsCredentialListMapping(accountSid, domainSid, credentialListSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AuthCallsCredentialListMappingApi#createSipAuthCallsCredentialListMapping");
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
| **credentialListSid** | **String**| The SID of the CredentialList resource to map to the SIP domain. | |

### Return type

[**ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsCredentialListMapping**](ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsCredentialListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSipAuthCallsCredentialListMapping"></a>
# **deleteSipAuthCallsCredentialListMapping**
> deleteSipAuthCallsCredentialListMapping(accountSid, domainSid, sid)



Delete a credential list mapping from the requested domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AuthCallsCredentialListMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AuthCallsCredentialListMappingApi apiInstance = new Api20100401AuthCallsCredentialListMappingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to delete.
    String domainSid = "domainSid_example"; // String | The SID of the SIP domain that contains the resource to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the CredentialListMapping resource to delete.
    try {
      apiInstance.deleteSipAuthCallsCredentialListMapping(accountSid, domainSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AuthCallsCredentialListMappingApi#deleteSipAuthCallsCredentialListMapping");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to delete. | |
| **domainSid** | **String**| The SID of the SIP domain that contains the resource to delete. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the CredentialListMapping resource to delete. | |

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

<a id="fetchSipAuthCallsCredentialListMapping"></a>
# **fetchSipAuthCallsCredentialListMapping**
> ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsCredentialListMapping fetchSipAuthCallsCredentialListMapping(accountSid, domainSid, sid)



Fetch a specific instance of a credential list mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AuthCallsCredentialListMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AuthCallsCredentialListMappingApi apiInstance = new Api20100401AuthCallsCredentialListMappingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resource to fetch.
    String domainSid = "domainSid_example"; // String | The SID of the SIP domain that contains the resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch.
    try {
      ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsCredentialListMapping result = apiInstance.fetchSipAuthCallsCredentialListMapping(accountSid, domainSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AuthCallsCredentialListMappingApi#fetchSipAuthCallsCredentialListMapping");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resource to fetch. | |
| **domainSid** | **String**| The SID of the SIP domain that contains the resource to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch. | |

### Return type

[**ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsCredentialListMapping**](ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsCredentialListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSipAuthCallsCredentialListMapping"></a>
# **listSipAuthCallsCredentialListMapping**
> ListSipAuthCallsCredentialListMappingResponse listSipAuthCallsCredentialListMapping(accountSid, domainSid, pageSize, page, pageToken)



Retrieve a list of credential list mappings belonging to the domain used in the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401AuthCallsCredentialListMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401AuthCallsCredentialListMappingApi apiInstance = new Api20100401AuthCallsCredentialListMappingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to read.
    String domainSid = "domainSid_example"; // String | The SID of the SIP domain that contains the resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSipAuthCallsCredentialListMappingResponse result = apiInstance.listSipAuthCallsCredentialListMapping(accountSid, domainSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401AuthCallsCredentialListMappingApi#listSipAuthCallsCredentialListMapping");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to read. | |
| **domainSid** | **String**| The SID of the SIP domain that contains the resources to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSipAuthCallsCredentialListMappingResponse**](ListSipAuthCallsCredentialListMappingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

