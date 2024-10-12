# IpMessagingV1CredentialApi

All URIs are relative to *https://ip-messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCredential**](IpMessagingV1CredentialApi.md#createCredential) | **POST** /v1/Credentials |  |
| [**deleteCredential**](IpMessagingV1CredentialApi.md#deleteCredential) | **DELETE** /v1/Credentials/{Sid} |  |
| [**fetchCredential**](IpMessagingV1CredentialApi.md#fetchCredential) | **GET** /v1/Credentials/{Sid} |  |
| [**listCredential**](IpMessagingV1CredentialApi.md#listCredential) | **GET** /v1/Credentials |  |
| [**updateCredential**](IpMessagingV1CredentialApi.md#updateCredential) | **POST** /v1/Credentials/{Sid} |  |


<a id="createCredential"></a>
# **createCredential**
> IpMessagingV1Credential createCredential(type, apiKey, certificate, friendlyName, privateKey, sandbox, secret)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1CredentialApi apiInstance = new IpMessagingV1CredentialApi(defaultClient);
    CredentialEnumPushService type = CredentialEnumPushService.fromValue("gcm"); // CredentialEnumPushService | 
    String apiKey = "apiKey_example"; // String | 
    String certificate = "certificate_example"; // String | 
    String friendlyName = "friendlyName_example"; // String | 
    String privateKey = "privateKey_example"; // String | 
    Boolean sandbox = true; // Boolean | 
    String secret = "secret_example"; // String | 
    try {
      IpMessagingV1Credential result = apiInstance.createCredential(type, apiKey, certificate, friendlyName, privateKey, sandbox, secret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1CredentialApi#createCredential");
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
| **apiKey** | **String**|  | [optional] |
| **certificate** | **String**|  | [optional] |
| **friendlyName** | **String**|  | [optional] |
| **privateKey** | **String**|  | [optional] |
| **sandbox** | **Boolean**|  | [optional] |
| **secret** | **String**|  | [optional] |

### Return type

[**IpMessagingV1Credential**](IpMessagingV1Credential.md)

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
import org.openapitools.client.api.IpMessagingV1CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1CredentialApi apiInstance = new IpMessagingV1CredentialApi(defaultClient);
    String sid = "sid_example"; // String | 
    try {
      apiInstance.deleteCredential(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1CredentialApi#deleteCredential");
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
| **sid** | **String**|  | |

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
> IpMessagingV1Credential fetchCredential(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1CredentialApi apiInstance = new IpMessagingV1CredentialApi(defaultClient);
    String sid = "sid_example"; // String | 
    try {
      IpMessagingV1Credential result = apiInstance.fetchCredential(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1CredentialApi#fetchCredential");
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
| **sid** | **String**|  | |

### Return type

[**IpMessagingV1Credential**](IpMessagingV1Credential.md)

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
import org.openapitools.client.api.IpMessagingV1CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1CredentialApi apiInstance = new IpMessagingV1CredentialApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListCredentialResponse result = apiInstance.listCredential(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1CredentialApi#listCredential");
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
> IpMessagingV1Credential updateCredential(sid, apiKey, certificate, friendlyName, privateKey, sandbox, secret)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1CredentialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1CredentialApi apiInstance = new IpMessagingV1CredentialApi(defaultClient);
    String sid = "sid_example"; // String | 
    String apiKey = "apiKey_example"; // String | 
    String certificate = "certificate_example"; // String | 
    String friendlyName = "friendlyName_example"; // String | 
    String privateKey = "privateKey_example"; // String | 
    Boolean sandbox = true; // Boolean | 
    String secret = "secret_example"; // String | 
    try {
      IpMessagingV1Credential result = apiInstance.updateCredential(sid, apiKey, certificate, friendlyName, privateKey, sandbox, secret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1CredentialApi#updateCredential");
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
| **sid** | **String**|  | |
| **apiKey** | **String**|  | [optional] |
| **certificate** | **String**|  | [optional] |
| **friendlyName** | **String**|  | [optional] |
| **privateKey** | **String**|  | [optional] |
| **sandbox** | **Boolean**|  | [optional] |
| **secret** | **String**|  | [optional] |

### Return type

[**IpMessagingV1Credential**](IpMessagingV1Credential.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

