# AccountsV1PublicKeyApi

All URIs are relative to *https://accounts.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCredentialPublicKey**](AccountsV1PublicKeyApi.md#createCredentialPublicKey) | **POST** /v1/Credentials/PublicKeys |  |
| [**deleteCredentialPublicKey**](AccountsV1PublicKeyApi.md#deleteCredentialPublicKey) | **DELETE** /v1/Credentials/PublicKeys/{Sid} |  |
| [**fetchCredentialPublicKey**](AccountsV1PublicKeyApi.md#fetchCredentialPublicKey) | **GET** /v1/Credentials/PublicKeys/{Sid} |  |
| [**listCredentialPublicKey**](AccountsV1PublicKeyApi.md#listCredentialPublicKey) | **GET** /v1/Credentials/PublicKeys |  |
| [**updateCredentialPublicKey**](AccountsV1PublicKeyApi.md#updateCredentialPublicKey) | **POST** /v1/Credentials/PublicKeys/{Sid} |  |


<a id="createCredentialPublicKey"></a>
# **createCredentialPublicKey**
> AccountsV1CredentialCredentialPublicKey createCredentialPublicKey(publicKey, accountSid, friendlyName)



Create a new Public Key Credential

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsV1PublicKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accounts.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AccountsV1PublicKeyApi apiInstance = new AccountsV1PublicKeyApi(defaultClient);
    String publicKey = "publicKey_example"; // String | A URL encoded representation of the public key. For example, `-----BEGIN PUBLIC KEY-----MIIBIjANB.pa9xQIDAQAB-----END PUBLIC KEY-----`
    String accountSid = "accountSid_example"; // String | The SID of the Subaccount that this Credential should be associated with. Must be a valid Subaccount of the account issuing the request
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    try {
      AccountsV1CredentialCredentialPublicKey result = apiInstance.createCredentialPublicKey(publicKey, accountSid, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsV1PublicKeyApi#createCredentialPublicKey");
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
| **publicKey** | **String**| A URL encoded representation of the public key. For example, &#x60;-----BEGIN PUBLIC KEY-----MIIBIjANB.pa9xQIDAQAB-----END PUBLIC KEY-----&#x60; | |
| **accountSid** | **String**| The SID of the Subaccount that this Credential should be associated with. Must be a valid Subaccount of the account issuing the request | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] |

### Return type

[**AccountsV1CredentialCredentialPublicKey**](AccountsV1CredentialCredentialPublicKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteCredentialPublicKey"></a>
# **deleteCredentialPublicKey**
> deleteCredentialPublicKey(sid)



Delete a Credential from your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsV1PublicKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accounts.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AccountsV1PublicKeyApi apiInstance = new AccountsV1PublicKeyApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the PublicKey resource to delete.
    try {
      apiInstance.deleteCredentialPublicKey(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsV1PublicKeyApi#deleteCredentialPublicKey");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the PublicKey resource to delete. | |

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

<a id="fetchCredentialPublicKey"></a>
# **fetchCredentialPublicKey**
> AccountsV1CredentialCredentialPublicKey fetchCredentialPublicKey(sid)



Fetch the public key specified by the provided Credential Sid

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsV1PublicKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accounts.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AccountsV1PublicKeyApi apiInstance = new AccountsV1PublicKeyApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the PublicKey resource to fetch.
    try {
      AccountsV1CredentialCredentialPublicKey result = apiInstance.fetchCredentialPublicKey(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsV1PublicKeyApi#fetchCredentialPublicKey");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the PublicKey resource to fetch. | |

### Return type

[**AccountsV1CredentialCredentialPublicKey**](AccountsV1CredentialCredentialPublicKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listCredentialPublicKey"></a>
# **listCredentialPublicKey**
> ListCredentialPublicKeyResponse listCredentialPublicKey(pageSize, page, pageToken)



Retrieves a collection of Public Key Credentials belonging to the account used to make the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsV1PublicKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accounts.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AccountsV1PublicKeyApi apiInstance = new AccountsV1PublicKeyApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListCredentialPublicKeyResponse result = apiInstance.listCredentialPublicKey(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsV1PublicKeyApi#listCredentialPublicKey");
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

[**ListCredentialPublicKeyResponse**](ListCredentialPublicKeyResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateCredentialPublicKey"></a>
# **updateCredentialPublicKey**
> AccountsV1CredentialCredentialPublicKey updateCredentialPublicKey(sid, friendlyName)



Modify the properties of a given Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsV1PublicKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accounts.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AccountsV1PublicKeyApi apiInstance = new AccountsV1PublicKeyApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the PublicKey resource to update.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    try {
      AccountsV1CredentialCredentialPublicKey result = apiInstance.updateCredentialPublicKey(sid, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsV1PublicKeyApi#updateCredentialPublicKey");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the PublicKey resource to update. | |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] |

### Return type

[**AccountsV1CredentialCredentialPublicKey**](AccountsV1CredentialCredentialPublicKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

