# ConversationsV1CredentialApi

All URIs are relative to *https://conversations.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCredential**](ConversationsV1CredentialApi.md#createCredential) | **POST** /v1/Credentials |  |
| [**deleteCredential**](ConversationsV1CredentialApi.md#deleteCredential) | **DELETE** /v1/Credentials/{Sid} |  |
| [**fetchCredential**](ConversationsV1CredentialApi.md#fetchCredential) | **GET** /v1/Credentials/{Sid} |  |
| [**listCredential**](ConversationsV1CredentialApi.md#listCredential) | **GET** /v1/Credentials |  |
| [**updateCredential**](ConversationsV1CredentialApi.md#updateCredential) | **POST** /v1/Credentials/{Sid} |  |


<a id="createCredential"></a>
# **createCredential**
> ConversationsV1Credential createCredential(type, apiKey, certificate, friendlyName, privateKey, sandbox, secret)



Add a new push notification credential to your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1CredentialApi apiInstance = new ConversationsV1CredentialApi(defaultClient);
    CredentialEnumPushType type = CredentialEnumPushType.fromValue("apn"); // CredentialEnumPushType | 
    String apiKey = "apiKey_example"; // String | [GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential.
    String certificate = "certificate_example"; // String | [APN only] The URL encoded representation of the certificate. For example,  `-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A== -----END CERTIFICATE-----`.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
    String privateKey = "privateKey_example"; // String | [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----`.
    Boolean sandbox = true; // Boolean | [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
    String secret = "secret_example"; // String | [FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging.
    try {
      ConversationsV1Credential result = apiInstance.createCredential(type, apiKey, certificate, friendlyName, privateKey, sandbox, secret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1CredentialApi#createCredential");
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
| **type** | **CredentialEnumPushType**|  | [enum: apn, gcm, fcm] |
| **apiKey** | **String**| [GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential. | [optional] |
| **certificate** | **String**| [APN only] The URL encoded representation of the certificate. For example,  &#x60;-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A&#x3D;&#x3D; -----END CERTIFICATE-----&#x60;. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the new resource. It can be up to 64 characters long. | [optional] |
| **privateKey** | **String**| [APN only] The URL encoded representation of the private key. For example, &#x60;-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----&#x60;. | [optional] |
| **sandbox** | **Boolean**| [APN only] Whether to send the credential to sandbox APNs. Can be &#x60;true&#x60; to send to sandbox APNs or &#x60;false&#x60; to send to production. | [optional] |
| **secret** | **String**| [FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging. | [optional] |

### Return type

[**ConversationsV1Credential**](ConversationsV1Credential.md)

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



Remove a push notification credential from your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1CredentialApi apiInstance = new ConversationsV1CredentialApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    try {
      apiInstance.deleteCredential(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1CredentialApi#deleteCredential");
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
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |

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
> ConversationsV1Credential fetchCredential(sid)



Fetch a push notification credential from your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1CredentialApi apiInstance = new ConversationsV1CredentialApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    try {
      ConversationsV1Credential result = apiInstance.fetchCredential(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1CredentialApi#fetchCredential");
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
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |

### Return type

[**ConversationsV1Credential**](ConversationsV1Credential.md)

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



Retrieve a list of all push notification credentials on your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1CredentialApi apiInstance = new ConversationsV1CredentialApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListCredentialResponse result = apiInstance.listCredential(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1CredentialApi#listCredential");
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
> ConversationsV1Credential updateCredential(sid, apiKey, certificate, friendlyName, privateKey, sandbox, secret, type)



Update an existing push notification credential on your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1CredentialApi apiInstance = new ConversationsV1CredentialApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    String apiKey = "apiKey_example"; // String | [GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential.
    String certificate = "certificate_example"; // String | [APN only] The URL encoded representation of the certificate. For example,  `-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A== -----END CERTIFICATE-----`.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
    String privateKey = "privateKey_example"; // String | [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----`.
    Boolean sandbox = true; // Boolean | [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
    String secret = "secret_example"; // String | [FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging.
    CredentialEnumPushType type = CredentialEnumPushType.fromValue("apn"); // CredentialEnumPushType | 
    try {
      ConversationsV1Credential result = apiInstance.updateCredential(sid, apiKey, certificate, friendlyName, privateKey, sandbox, secret, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1CredentialApi#updateCredential");
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
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |
| **apiKey** | **String**| [GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential. | [optional] |
| **certificate** | **String**| [APN only] The URL encoded representation of the certificate. For example,  &#x60;-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEF.....A&#x3D;&#x3D; -----END CERTIFICATE-----&#x60;. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the new resource. It can be up to 64 characters long. | [optional] |
| **privateKey** | **String**| [APN only] The URL encoded representation of the private key. For example, &#x60;-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fG... -----END RSA PRIVATE KEY-----&#x60;. | [optional] |
| **sandbox** | **Boolean**| [APN only] Whether to send the credential to sandbox APNs. Can be &#x60;true&#x60; to send to sandbox APNs or &#x60;false&#x60; to send to production. | [optional] |
| **secret** | **String**| [FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging. | [optional] |
| **type** | **CredentialEnumPushType**|  | [optional] [enum: apn, gcm, fcm] |

### Return type

[**ConversationsV1Credential**](ConversationsV1Credential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

