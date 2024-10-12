# MicrovisorV1AccountConfigApi

All URIs are relative to *https://microvisor.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAccountConfig**](MicrovisorV1AccountConfigApi.md#createAccountConfig) | **POST** /v1/Configs |  |
| [**deleteAccountConfig**](MicrovisorV1AccountConfigApi.md#deleteAccountConfig) | **DELETE** /v1/Configs/{Key} |  |
| [**fetchAccountConfig**](MicrovisorV1AccountConfigApi.md#fetchAccountConfig) | **GET** /v1/Configs/{Key} |  |
| [**listAccountConfig**](MicrovisorV1AccountConfigApi.md#listAccountConfig) | **GET** /v1/Configs |  |
| [**updateAccountConfig**](MicrovisorV1AccountConfigApi.md#updateAccountConfig) | **POST** /v1/Configs/{Key} |  |


<a id="createAccountConfig"></a>
# **createAccountConfig**
> MicrovisorV1AccountConfig createAccountConfig(key, value)



Create a config for an Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1AccountConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1AccountConfigApi apiInstance = new MicrovisorV1AccountConfigApi(defaultClient);
    String key = "key_example"; // String | The config key; up to 100 characters.
    String value = "value_example"; // String | The config value; up to 4096 characters.
    try {
      MicrovisorV1AccountConfig result = apiInstance.createAccountConfig(key, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1AccountConfigApi#createAccountConfig");
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
| **key** | **String**| The config key; up to 100 characters. | |
| **value** | **String**| The config value; up to 4096 characters. | |

### Return type

[**MicrovisorV1AccountConfig**](MicrovisorV1AccountConfig.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteAccountConfig"></a>
# **deleteAccountConfig**
> deleteAccountConfig(key)



Delete a config for an Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1AccountConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1AccountConfigApi apiInstance = new MicrovisorV1AccountConfigApi(defaultClient);
    String key = "key_example"; // String | The config key; up to 100 characters.
    try {
      apiInstance.deleteAccountConfig(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1AccountConfigApi#deleteAccountConfig");
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
| **key** | **String**| The config key; up to 100 characters. | |

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

<a id="fetchAccountConfig"></a>
# **fetchAccountConfig**
> MicrovisorV1AccountConfig fetchAccountConfig(key)



Retrieve a Config for an Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1AccountConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1AccountConfigApi apiInstance = new MicrovisorV1AccountConfigApi(defaultClient);
    String key = "key_example"; // String | The config key; up to 100 characters.
    try {
      MicrovisorV1AccountConfig result = apiInstance.fetchAccountConfig(key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1AccountConfigApi#fetchAccountConfig");
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
| **key** | **String**| The config key; up to 100 characters. | |

### Return type

[**MicrovisorV1AccountConfig**](MicrovisorV1AccountConfig.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAccountConfig"></a>
# **listAccountConfig**
> ListAccountConfigResponse listAccountConfig(pageSize, page, pageToken)



Retrieve a list of all Configs for an Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1AccountConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1AccountConfigApi apiInstance = new MicrovisorV1AccountConfigApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListAccountConfigResponse result = apiInstance.listAccountConfig(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1AccountConfigApi#listAccountConfig");
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

[**ListAccountConfigResponse**](ListAccountConfigResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateAccountConfig"></a>
# **updateAccountConfig**
> MicrovisorV1AccountConfig updateAccountConfig(key, value)



Update a config for an Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1AccountConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1AccountConfigApi apiInstance = new MicrovisorV1AccountConfigApi(defaultClient);
    String key = "key_example"; // String | The config key; up to 100 characters.
    String value = "value_example"; // String | The config value; up to 4096 characters.
    try {
      MicrovisorV1AccountConfig result = apiInstance.updateAccountConfig(key, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1AccountConfigApi#updateAccountConfig");
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
| **key** | **String**| The config key; up to 100 characters. | |
| **value** | **String**| The config value; up to 4096 characters. | |

### Return type

[**MicrovisorV1AccountConfig**](MicrovisorV1AccountConfig.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

