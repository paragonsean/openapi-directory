# MessagingV1BrandVettingApi

All URIs are relative to *https://messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBrandVetting**](MessagingV1BrandVettingApi.md#createBrandVetting) | **POST** /v1/a2p/BrandRegistrations/{BrandSid}/Vettings |  |
| [**fetchBrandVetting**](MessagingV1BrandVettingApi.md#fetchBrandVetting) | **GET** /v1/a2p/BrandRegistrations/{BrandSid}/Vettings/{BrandVettingSid} |  |
| [**listBrandVetting**](MessagingV1BrandVettingApi.md#listBrandVetting) | **GET** /v1/a2p/BrandRegistrations/{BrandSid}/Vettings |  |


<a id="createBrandVetting"></a>
# **createBrandVetting**
> MessagingV1BrandRegistrationsBrandVetting createBrandVetting(brandSid, vettingProvider, vettingId)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1BrandVettingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1BrandVettingApi apiInstance = new MessagingV1BrandVettingApi(defaultClient);
    String brandSid = "brandSid_example"; // String | The SID of the Brand Registration resource of the vettings to create .
    BrandVettingEnumVettingProvider vettingProvider = BrandVettingEnumVettingProvider.fromValue("campaign-verify"); // BrandVettingEnumVettingProvider | 
    String vettingId = "vettingId_example"; // String | The unique ID of the vetting
    try {
      MessagingV1BrandRegistrationsBrandVetting result = apiInstance.createBrandVetting(brandSid, vettingProvider, vettingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1BrandVettingApi#createBrandVetting");
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
| **brandSid** | **String**| The SID of the Brand Registration resource of the vettings to create . | |
| **vettingProvider** | **BrandVettingEnumVettingProvider**|  | [enum: campaign-verify] |
| **vettingId** | **String**| The unique ID of the vetting | [optional] |

### Return type

[**MessagingV1BrandRegistrationsBrandVetting**](MessagingV1BrandRegistrationsBrandVetting.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchBrandVetting"></a>
# **fetchBrandVetting**
> MessagingV1BrandRegistrationsBrandVetting fetchBrandVetting(brandSid, brandVettingSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1BrandVettingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1BrandVettingApi apiInstance = new MessagingV1BrandVettingApi(defaultClient);
    String brandSid = "brandSid_example"; // String | The SID of the Brand Registration resource of the vettings to read .
    String brandVettingSid = "brandVettingSid_example"; // String | The Twilio SID of the third-party vetting record.
    try {
      MessagingV1BrandRegistrationsBrandVetting result = apiInstance.fetchBrandVetting(brandSid, brandVettingSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1BrandVettingApi#fetchBrandVetting");
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
| **brandSid** | **String**| The SID of the Brand Registration resource of the vettings to read . | |
| **brandVettingSid** | **String**| The Twilio SID of the third-party vetting record. | |

### Return type

[**MessagingV1BrandRegistrationsBrandVetting**](MessagingV1BrandRegistrationsBrandVetting.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listBrandVetting"></a>
# **listBrandVetting**
> ListBrandVettingResponse listBrandVetting(brandSid, vettingProvider, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1BrandVettingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1BrandVettingApi apiInstance = new MessagingV1BrandVettingApi(defaultClient);
    String brandSid = "brandSid_example"; // String | The SID of the Brand Registration resource of the vettings to read .
    BrandVettingEnumVettingProvider vettingProvider = BrandVettingEnumVettingProvider.fromValue("campaign-verify"); // BrandVettingEnumVettingProvider | The third-party provider of the vettings to read
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListBrandVettingResponse result = apiInstance.listBrandVetting(brandSid, vettingProvider, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1BrandVettingApi#listBrandVetting");
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
| **brandSid** | **String**| The SID of the Brand Registration resource of the vettings to read . | |
| **vettingProvider** | **BrandVettingEnumVettingProvider**| The third-party provider of the vettings to read | [optional] [enum: campaign-verify] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListBrandVettingResponse**](ListBrandVettingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

