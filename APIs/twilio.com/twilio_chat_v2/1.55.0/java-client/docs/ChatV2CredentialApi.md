# ChatV2CredentialApi

All URIs are relative to *https://chat.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCredential**](ChatV2CredentialApi.md#createCredential) | **POST** /v2/Credentials |  |
| [**deleteCredential**](ChatV2CredentialApi.md#deleteCredential) | **DELETE** /v2/Credentials/{Sid} |  |
| [**fetchCredential**](ChatV2CredentialApi.md#fetchCredential) | **GET** /v2/Credentials/{Sid} |  |
| [**listCredential**](ChatV2CredentialApi.md#listCredential) | **GET** /v2/Credentials |  |
| [**updateCredential**](ChatV2CredentialApi.md#updateCredential) | **POST** /v2/Credentials/{Sid} |  |


<a id="createCredential"></a>
# **createCredential**
> ChatV2Credential createCredential(type, apiKey, certificate, friendlyName, privateKey, sandbox, secret)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2CredentialApi apiInstance = new ChatV2CredentialApi(defaultClient);
    CredentialEnumPushService type = CredentialEnumPushService.fromValue("gcm"); // CredentialEnumPushService | 
    String apiKey = "apiKey_example"; // String | [GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential.
    String certificate = "certificate_example"; // String | [APN only] The URL encoded representation of the certificate. For example,  `-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A== -----END CERTIFICATE-----`
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
    String privateKey = "privateKey_example"; // String | [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----`
    Boolean sandbox = true; // Boolean | [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
    String secret = "secret_example"; // String | [FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging.
    try {
      ChatV2Credential result = apiInstance.createCredential(type, apiKey, certificate, friendlyName, privateKey, sandbox, secret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2CredentialApi#createCredential");
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
| **type** | **CredentialEnumPushService**|  | [enum: gcm, apn, fcm] |
| **apiKey** | **String**| [GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential. | [optional] |
| **certificate** | **String**| [APN only] The URL encoded representation of the certificate. For example,  &#x60;-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A&#x3D;&#x3D; -----END CERTIFICATE-----&#x60; | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the new resource. It can be up to 64 characters long. | [optional] |
| **privateKey** | **String**| [APN only] The URL encoded representation of the private key. For example, &#x60;-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----&#x60; | [optional] |
| **sandbox** | **Boolean**| [APN only] Whether to send the credential to sandbox APNs. Can be &#x60;true&#x60; to send to sandbox APNs or &#x60;false&#x60; to send to production. | [optional] |
| **secret** | **String**| [FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging. | [optional] |

### Return type

[**ChatV2Credential**](ChatV2Credential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteCredential"></a>
# **deleteCredential**
> deleteCredential(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2CredentialApi apiInstance = new ChatV2CredentialApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Credential resource to delete.
    try {
      apiInstance.deleteCredential(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2CredentialApi#deleteCredential");
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
| **sid** | **String**| The SID of the Credential resource to delete. | |

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

<a id="fetchCredential"></a>
# **fetchCredential**
> ChatV2Credential fetchCredential(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2CredentialApi apiInstance = new ChatV2CredentialApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Credential resource to fetch.
    try {
      ChatV2Credential result = apiInstance.fetchCredential(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2CredentialApi#fetchCredential");
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
| **sid** | **String**| The SID of the Credential resource to fetch. | |

### Return type

[**ChatV2Credential**](ChatV2Credential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listCredential"></a>
# **listCredential**
> ListCredentialResponse listCredential(pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2CredentialApi apiInstance = new ChatV2CredentialApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListCredentialResponse result = apiInstance.listCredential(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2CredentialApi#listCredential");
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

[**ListCredentialResponse**](ListCredentialResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateCredential"></a>
# **updateCredential**
> ChatV2Credential updateCredential(sid, apiKey, certificate, friendlyName, privateKey, sandbox, secret)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2CredentialApi apiInstance = new ChatV2CredentialApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Credential resource to update.
    String apiKey = "apiKey_example"; // String | [GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential.
    String certificate = "certificate_example"; // String | [APN only] The URL encoded representation of the certificate. For example,  `-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A== -----END CERTIFICATE-----`
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    String privateKey = "privateKey_example"; // String | [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----`
    Boolean sandbox = true; // Boolean | [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
    String secret = "secret_example"; // String | [FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging.
    try {
      ChatV2Credential result = apiInstance.updateCredential(sid, apiKey, certificate, friendlyName, privateKey, sandbox, secret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2CredentialApi#updateCredential");
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
| **sid** | **String**| The SID of the Credential resource to update. | |
| **apiKey** | **String**| [GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential. | [optional] |
| **certificate** | **String**| [APN only] The URL encoded representation of the certificate. For example,  &#x60;-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A&#x3D;&#x3D; -----END CERTIFICATE-----&#x60; | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] |
| **privateKey** | **String**| [APN only] The URL encoded representation of the private key. For example, &#x60;-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----&#x60; | [optional] |
| **sandbox** | **Boolean**| [APN only] Whether to send the credential to sandbox APNs. Can be &#x60;true&#x60; to send to sandbox APNs or &#x60;false&#x60; to send to production. | [optional] |
| **secret** | **String**| [FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging. | [optional] |

### Return type

[**ChatV2Credential**](ChatV2Credential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

