# NotifyV1CredentialApi

All URIs are relative to *https://notify.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCredential**](NotifyV1CredentialApi.md#createCredential) | **POST** /v1/Credentials |  |
| [**deleteCredential**](NotifyV1CredentialApi.md#deleteCredential) | **DELETE** /v1/Credentials/{Sid} |  |
| [**fetchCredential**](NotifyV1CredentialApi.md#fetchCredential) | **GET** /v1/Credentials/{Sid} |  |
| [**listCredential**](NotifyV1CredentialApi.md#listCredential) | **GET** /v1/Credentials |  |
| [**updateCredential**](NotifyV1CredentialApi.md#updateCredential) | **POST** /v1/Credentials/{Sid} |  |


<a id="createCredential"></a>
# **createCredential**
> NotifyV1Credential createCredential(type, apiKey, certificate, friendlyName, privateKey, sandbox, secret)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotifyV1CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://notify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NotifyV1CredentialApi apiInstance = new NotifyV1CredentialApi(defaultClient);
    CredentialEnumPushService type = CredentialEnumPushService.fromValue("gcm"); // CredentialEnumPushService | 
    String apiKey = "apiKey_example"; // String | [GCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.
    String certificate = "certificate_example"; // String | [APN only] The URL-encoded representation of the certificate. Strip everything outside of the headers, e.g. `-----BEGIN CERTIFICATE-----MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A==-----END CERTIFICATE-----`
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    String privateKey = "privateKey_example"; // String | [APN only] The URL-encoded representation of the private key. Strip everything outside of the headers, e.g. `-----BEGIN RSA PRIVATE KEY-----MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR\\\\n.-----END RSA PRIVATE KEY-----`
    Boolean sandbox = true; // Boolean | [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
    String secret = "secret_example"; // String | [FCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.
    try {
      NotifyV1Credential result = apiInstance.createCredential(type, apiKey, certificate, friendlyName, privateKey, sandbox, secret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotifyV1CredentialApi#createCredential");
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
| **apiKey** | **String**| [GCM only] The &#x60;Server key&#x60; of your project from Firebase console under Settings / Cloud messaging. | [optional] |
| **certificate** | **String**| [APN only] The URL-encoded representation of the certificate. Strip everything outside of the headers, e.g. &#x60;-----BEGIN CERTIFICATE-----MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A&#x3D;&#x3D;-----END CERTIFICATE-----&#x60; | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] |
| **privateKey** | **String**| [APN only] The URL-encoded representation of the private key. Strip everything outside of the headers, e.g. &#x60;-----BEGIN RSA PRIVATE KEY-----MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR\\\\n.-----END RSA PRIVATE KEY-----&#x60; | [optional] |
| **sandbox** | **Boolean**| [APN only] Whether to send the credential to sandbox APNs. Can be &#x60;true&#x60; to send to sandbox APNs or &#x60;false&#x60; to send to production. | [optional] |
| **secret** | **String**| [FCM only] The &#x60;Server key&#x60; of your project from Firebase console under Settings / Cloud messaging. | [optional] |

### Return type

[**NotifyV1Credential**](NotifyV1Credential.md)

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
import org.openapitools.client.api.NotifyV1CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://notify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NotifyV1CredentialApi apiInstance = new NotifyV1CredentialApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Credential resource to delete.
    try {
      apiInstance.deleteCredential(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotifyV1CredentialApi#deleteCredential");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Credential resource to delete. | |

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
> NotifyV1Credential fetchCredential(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotifyV1CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://notify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NotifyV1CredentialApi apiInstance = new NotifyV1CredentialApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Credential resource to fetch.
    try {
      NotifyV1Credential result = apiInstance.fetchCredential(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotifyV1CredentialApi#fetchCredential");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Credential resource to fetch. | |

### Return type

[**NotifyV1Credential**](NotifyV1Credential.md)

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
import org.openapitools.client.api.NotifyV1CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://notify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NotifyV1CredentialApi apiInstance = new NotifyV1CredentialApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListCredentialResponse result = apiInstance.listCredential(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotifyV1CredentialApi#listCredential");
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
> NotifyV1Credential updateCredential(sid, apiKey, certificate, friendlyName, privateKey, sandbox, secret)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotifyV1CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://notify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NotifyV1CredentialApi apiInstance = new NotifyV1CredentialApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Credential resource to update.
    String apiKey = "apiKey_example"; // String | [GCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.
    String certificate = "certificate_example"; // String | [APN only] The URL-encoded representation of the certificate. Strip everything outside of the headers, e.g. `-----BEGIN CERTIFICATE-----MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A==-----END CERTIFICATE-----`
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    String privateKey = "privateKey_example"; // String | [APN only] The URL-encoded representation of the private key. Strip everything outside of the headers, e.g. `-----BEGIN RSA PRIVATE KEY-----MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR\\\\n.-----END RSA PRIVATE KEY-----`
    Boolean sandbox = true; // Boolean | [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
    String secret = "secret_example"; // String | [FCM only] The `Server key` of your project from Firebase console under Settings / Cloud messaging.
    try {
      NotifyV1Credential result = apiInstance.updateCredential(sid, apiKey, certificate, friendlyName, privateKey, sandbox, secret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotifyV1CredentialApi#updateCredential");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Credential resource to update. | |
| **apiKey** | **String**| [GCM only] The &#x60;Server key&#x60; of your project from Firebase console under Settings / Cloud messaging. | [optional] |
| **certificate** | **String**| [APN only] The URL-encoded representation of the certificate. Strip everything outside of the headers, e.g. &#x60;-----BEGIN CERTIFICATE-----MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A&#x3D;&#x3D;-----END CERTIFICATE-----&#x60; | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] |
| **privateKey** | **String**| [APN only] The URL-encoded representation of the private key. Strip everything outside of the headers, e.g. &#x60;-----BEGIN RSA PRIVATE KEY-----MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR\\\\n.-----END RSA PRIVATE KEY-----&#x60; | [optional] |
| **sandbox** | **Boolean**| [APN only] Whether to send the credential to sandbox APNs. Can be &#x60;true&#x60; to send to sandbox APNs or &#x60;false&#x60; to send to production. | [optional] |
| **secret** | **String**| [FCM only] The &#x60;Server key&#x60; of your project from Firebase console under Settings / Cloud messaging. | [optional] |

### Return type

[**NotifyV1Credential**](NotifyV1Credential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

