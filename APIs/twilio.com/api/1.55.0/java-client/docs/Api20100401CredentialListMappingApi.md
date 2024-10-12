# Api20100401CredentialListMappingApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSipCredentialListMapping**](Api20100401CredentialListMappingApi.md#createSipCredentialListMapping) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings.json |  |
| [**deleteSipCredentialListMapping**](Api20100401CredentialListMappingApi.md#deleteSipCredentialListMapping) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings/{Sid}.json |  |
| [**fetchSipCredentialListMapping**](Api20100401CredentialListMappingApi.md#fetchSipCredentialListMapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings/{Sid}.json |  |
| [**listSipCredentialListMapping**](Api20100401CredentialListMappingApi.md#listSipCredentialListMapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings.json |  |


<a id="createSipCredentialListMapping"></a>
# **createSipCredentialListMapping**
> ApiV2010AccountSipSipDomainSipCredentialListMapping createSipCredentialListMapping(accountSid, domainSid, credentialListSid)



Create a CredentialListMapping resource for an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401CredentialListMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401CredentialListMappingApi apiInstance = new Api20100401CredentialListMappingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    String domainSid = "domainSid_example"; // String | A 34 character string that uniquely identifies the SIP Domain for which the CredentialList resource will be mapped.
    String credentialListSid = "credentialListSid_example"; // String | A 34 character string that uniquely identifies the CredentialList resource to map to the SIP domain.
    try {
      ApiV2010AccountSipSipDomainSipCredentialListMapping result = apiInstance.createSipCredentialListMapping(accountSid, domainSid, credentialListSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401CredentialListMappingApi#createSipCredentialListMapping");
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
| **domainSid** | **String**| A 34 character string that uniquely identifies the SIP Domain for which the CredentialList resource will be mapped. | |
| **credentialListSid** | **String**| A 34 character string that uniquely identifies the CredentialList resource to map to the SIP domain. | |

### Return type

[**ApiV2010AccountSipSipDomainSipCredentialListMapping**](ApiV2010AccountSipSipDomainSipCredentialListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSipCredentialListMapping"></a>
# **deleteSipCredentialListMapping**
> deleteSipCredentialListMapping(accountSid, domainSid, sid)



Delete a CredentialListMapping resource from an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401CredentialListMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401CredentialListMappingApi apiInstance = new Api20100401CredentialListMappingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    String domainSid = "domainSid_example"; // String | A 34 character string that uniquely identifies the SIP Domain that includes the resource to delete.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies the resource to delete.
    try {
      apiInstance.deleteSipCredentialListMapping(accountSid, domainSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401CredentialListMappingApi#deleteSipCredentialListMapping");
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
| **domainSid** | **String**| A 34 character string that uniquely identifies the SIP Domain that includes the resource to delete. | |
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

<a id="fetchSipCredentialListMapping"></a>
# **fetchSipCredentialListMapping**
> ApiV2010AccountSipSipDomainSipCredentialListMapping fetchSipCredentialListMapping(accountSid, domainSid, sid)



Fetch a single CredentialListMapping resource from an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401CredentialListMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401CredentialListMappingApi apiInstance = new Api20100401CredentialListMappingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    String domainSid = "domainSid_example"; // String | A 34 character string that uniquely identifies the SIP Domain that includes the resource to fetch.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies the resource to fetch.
    try {
      ApiV2010AccountSipSipDomainSipCredentialListMapping result = apiInstance.fetchSipCredentialListMapping(accountSid, domainSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401CredentialListMappingApi#fetchSipCredentialListMapping");
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
| **domainSid** | **String**| A 34 character string that uniquely identifies the SIP Domain that includes the resource to fetch. | |
| **sid** | **String**| A 34 character string that uniquely identifies the resource to fetch. | |

### Return type

[**ApiV2010AccountSipSipDomainSipCredentialListMapping**](ApiV2010AccountSipSipDomainSipCredentialListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSipCredentialListMapping"></a>
# **listSipCredentialListMapping**
> ListSipCredentialListMappingResponse listSipCredentialListMapping(accountSid, domainSid, pageSize, page, pageToken)



Read multiple CredentialListMapping resources from an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401CredentialListMappingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401CredentialListMappingApi apiInstance = new Api20100401CredentialListMappingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    String domainSid = "domainSid_example"; // String | A 34 character string that uniquely identifies the SIP Domain that includes the resource to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSipCredentialListMappingResponse result = apiInstance.listSipCredentialListMapping(accountSid, domainSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401CredentialListMappingApi#listSipCredentialListMapping");
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
| **domainSid** | **String**| A 34 character string that uniquely identifies the SIP Domain that includes the resource to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSipCredentialListMappingResponse**](ListSipCredentialListMappingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

