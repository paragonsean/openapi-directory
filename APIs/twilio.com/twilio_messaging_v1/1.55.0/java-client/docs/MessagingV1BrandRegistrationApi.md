# MessagingV1BrandRegistrationApi

All URIs are relative to *https://messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBrandRegistrations**](MessagingV1BrandRegistrationApi.md#createBrandRegistrations) | **POST** /v1/a2p/BrandRegistrations |  |
| [**fetchBrandRegistrations**](MessagingV1BrandRegistrationApi.md#fetchBrandRegistrations) | **GET** /v1/a2p/BrandRegistrations/{Sid} |  |
| [**listBrandRegistrations**](MessagingV1BrandRegistrationApi.md#listBrandRegistrations) | **GET** /v1/a2p/BrandRegistrations |  |
| [**updateBrandRegistrations**](MessagingV1BrandRegistrationApi.md#updateBrandRegistrations) | **POST** /v1/a2p/BrandRegistrations/{Sid} |  |


<a id="createBrandRegistrations"></a>
# **createBrandRegistrations**
> MessagingV1BrandRegistrations createBrandRegistrations(a2PProfileBundleSid, customerProfileBundleSid, brandType, mock, skipAutomaticSecVet)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1BrandRegistrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1BrandRegistrationApi apiInstance = new MessagingV1BrandRegistrationApi(defaultClient);
    String a2PProfileBundleSid = "a2PProfileBundleSid_example"; // String | A2P Messaging Profile Bundle Sid.
    String customerProfileBundleSid = "customerProfileBundleSid_example"; // String | Customer Profile Bundle Sid.
    String brandType = "brandType_example"; // String | Type of brand being created. One of: \\\"STANDARD\\\", \\\"SOLE_PROPRIETOR\\\". SOLE_PROPRIETOR is for low volume, SOLE_PROPRIETOR use cases. STANDARD is for all other use cases.
    Boolean mock = true; // Boolean | A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided.
    Boolean skipAutomaticSecVet = true; // Boolean | A flag to disable automatic secondary vetting for brands which it would otherwise be done.
    try {
      MessagingV1BrandRegistrations result = apiInstance.createBrandRegistrations(a2PProfileBundleSid, customerProfileBundleSid, brandType, mock, skipAutomaticSecVet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1BrandRegistrationApi#createBrandRegistrations");
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
| **a2PProfileBundleSid** | **String**| A2P Messaging Profile Bundle Sid. | |
| **customerProfileBundleSid** | **String**| Customer Profile Bundle Sid. | |
| **brandType** | **String**| Type of brand being created. One of: \\\&quot;STANDARD\\\&quot;, \\\&quot;SOLE_PROPRIETOR\\\&quot;. SOLE_PROPRIETOR is for low volume, SOLE_PROPRIETOR use cases. STANDARD is for all other use cases. | [optional] |
| **mock** | **Boolean**| A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided. | [optional] |
| **skipAutomaticSecVet** | **Boolean**| A flag to disable automatic secondary vetting for brands which it would otherwise be done. | [optional] |

### Return type

[**MessagingV1BrandRegistrations**](MessagingV1BrandRegistrations.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchBrandRegistrations"></a>
# **fetchBrandRegistrations**
> MessagingV1BrandRegistrations fetchBrandRegistrations(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1BrandRegistrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1BrandRegistrationApi apiInstance = new MessagingV1BrandRegistrationApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Brand Registration resource to fetch.
    try {
      MessagingV1BrandRegistrations result = apiInstance.fetchBrandRegistrations(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1BrandRegistrationApi#fetchBrandRegistrations");
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
| **sid** | **String**| The SID of the Brand Registration resource to fetch. | |

### Return type

[**MessagingV1BrandRegistrations**](MessagingV1BrandRegistrations.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listBrandRegistrations"></a>
# **listBrandRegistrations**
> ListBrandRegistrationsResponse listBrandRegistrations(pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1BrandRegistrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1BrandRegistrationApi apiInstance = new MessagingV1BrandRegistrationApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListBrandRegistrationsResponse result = apiInstance.listBrandRegistrations(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1BrandRegistrationApi#listBrandRegistrations");
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

[**ListBrandRegistrationsResponse**](ListBrandRegistrationsResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateBrandRegistrations"></a>
# **updateBrandRegistrations**
> MessagingV1BrandRegistrations updateBrandRegistrations(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1BrandRegistrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1BrandRegistrationApi apiInstance = new MessagingV1BrandRegistrationApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Brand Registration resource to update.
    try {
      MessagingV1BrandRegistrations result = apiInstance.updateBrandRegistrations(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1BrandRegistrationApi#updateBrandRegistrations");
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
| **sid** | **String**| The SID of the Brand Registration resource to update. | |

### Return type

[**MessagingV1BrandRegistrations**](MessagingV1BrandRegistrations.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |

