# Api20100401CredentialApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSipCredential**](Api20100401CredentialApi.md#createSipCredential) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials.json |  |
| [**deleteSipCredential**](Api20100401CredentialApi.md#deleteSipCredential) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json |  |
| [**fetchSipCredential**](Api20100401CredentialApi.md#fetchSipCredential) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json |  |
| [**listSipCredential**](Api20100401CredentialApi.md#listSipCredential) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials.json |  |
| [**updateSipCredential**](Api20100401CredentialApi.md#updateSipCredential) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json |  |


<a id="createSipCredential"></a>
# **createSipCredential**
> ApiV2010AccountSipSipCredentialListSipCredential createSipCredential(accountSid, credentialListSid, password, username)



Create a new credential resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401CredentialApi apiInstance = new Api20100401CredentialApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
    String credentialListSid = "credentialListSid_example"; // String | The unique id that identifies the credential list to include the created credential.
    String password = "password_example"; // String | The password that the username will use when authenticating SIP requests. The password must be a minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg `IWasAtSignal2018`)
    String username = "username_example"; // String | The username that will be passed when authenticating SIP requests. The username should be sent in response to Twilio's challenge of the initial INVITE. It can be up to 32 characters long.
    try {
      ApiV2010AccountSipSipCredentialListSipCredential result = apiInstance.createSipCredential(accountSid, credentialListSid, password, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401CredentialApi#createSipCredential");
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
| **credentialListSid** | **String**| The unique id that identifies the credential list to include the created credential. | |
| **password** | **String**| The password that the username will use when authenticating SIP requests. The password must be a minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg &#x60;IWasAtSignal2018&#x60;) | |
| **username** | **String**| The username that will be passed when authenticating SIP requests. The username should be sent in response to Twilio&#39;s challenge of the initial INVITE. It can be up to 32 characters long. | |

### Return type

[**ApiV2010AccountSipSipCredentialListSipCredential**](ApiV2010AccountSipSipCredentialListSipCredential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSipCredential"></a>
# **deleteSipCredential**
> deleteSipCredential(accountSid, credentialListSid, sid)



Delete a credential resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401CredentialApi apiInstance = new Api20100401CredentialApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
    String credentialListSid = "credentialListSid_example"; // String | The unique id that identifies the credential list that contains the desired credentials.
    String sid = "sid_example"; // String | The unique id that identifies the resource to delete.
    try {
      apiInstance.deleteSipCredential(accountSid, credentialListSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401CredentialApi#deleteSipCredential");
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
| **credentialListSid** | **String**| The unique id that identifies the credential list that contains the desired credentials. | |
| **sid** | **String**| The unique id that identifies the resource to delete. | |

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

<a id="fetchSipCredential"></a>
# **fetchSipCredential**
> ApiV2010AccountSipSipCredentialListSipCredential fetchSipCredential(accountSid, credentialListSid, sid)



Fetch a single credential.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401CredentialApi apiInstance = new Api20100401CredentialApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
    String credentialListSid = "credentialListSid_example"; // String | The unique id that identifies the credential list that contains the desired credential.
    String sid = "sid_example"; // String | The unique id that identifies the resource to fetch.
    try {
      ApiV2010AccountSipSipCredentialListSipCredential result = apiInstance.fetchSipCredential(accountSid, credentialListSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401CredentialApi#fetchSipCredential");
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
| **credentialListSid** | **String**| The unique id that identifies the credential list that contains the desired credential. | |
| **sid** | **String**| The unique id that identifies the resource to fetch. | |

### Return type

[**ApiV2010AccountSipSipCredentialListSipCredential**](ApiV2010AccountSipSipCredentialListSipCredential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSipCredential"></a>
# **listSipCredential**
> ListSipCredentialResponse listSipCredential(accountSid, credentialListSid, pageSize, page, pageToken)



Retrieve a list of credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401CredentialApi apiInstance = new Api20100401CredentialApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
    String credentialListSid = "credentialListSid_example"; // String | The unique id that identifies the credential list that contains the desired credentials.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSipCredentialResponse result = apiInstance.listSipCredential(accountSid, credentialListSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401CredentialApi#listSipCredential");
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
| **credentialListSid** | **String**| The unique id that identifies the credential list that contains the desired credentials. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSipCredentialResponse**](ListSipCredentialResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSipCredential"></a>
# **updateSipCredential**
> ApiV2010AccountSipSipCredentialListSipCredential updateSipCredential(accountSid, credentialListSid, sid, password)



Update a credential resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401CredentialApi apiInstance = new Api20100401CredentialApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
    String credentialListSid = "credentialListSid_example"; // String | The unique id that identifies the credential list that includes this credential.
    String sid = "sid_example"; // String | The unique id that identifies the resource to update.
    String password = "password_example"; // String | The password that the username will use when authenticating SIP requests. The password must be a minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg `IWasAtSignal2018`)
    try {
      ApiV2010AccountSipSipCredentialListSipCredential result = apiInstance.updateSipCredential(accountSid, credentialListSid, sid, password);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401CredentialApi#updateSipCredential");
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
| **credentialListSid** | **String**| The unique id that identifies the credential list that includes this credential. | |
| **sid** | **String**| The unique id that identifies the resource to update. | |
| **password** | **String**| The password that the username will use when authenticating SIP requests. The password must be a minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg &#x60;IWasAtSignal2018&#x60;) | [optional] |

### Return type

[**ApiV2010AccountSipSipCredentialListSipCredential**](ApiV2010AccountSipSipCredentialListSipCredential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

