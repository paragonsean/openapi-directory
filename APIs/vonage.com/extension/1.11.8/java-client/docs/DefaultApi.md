# DefaultApi

All URIs are relative to *https://api.vonage.com/t/vbc.prod/provisioning*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**extensionCtrlGetAccountExtensionByID**](DefaultApi.md#extensionCtrlGetAccountExtensionByID) | **GET** /api/accounts/{account_id}/extensions/{extension_number} | Get extension data by account ID and extension number |
| [**extensionCtrlGetAccountExtensions**](DefaultApi.md#extensionCtrlGetAccountExtensions) | **GET** /api/accounts/{account_id}/extensions | Get account extensions data by account ID |


<a id="extensionCtrlGetAccountExtensionByID"></a>
# **extensionCtrlGetAccountExtensionByID**
> EndUserRouteHalResponse extensionCtrlGetAccountExtensionByID(accountId, extensionNumber)

Get extension data by account ID and extension number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/provisioning");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Vonage Business Cloud account ID
    BigDecimal extensionNumber = new BigDecimal("789"); // BigDecimal | The extension number
    try {
      EndUserRouteHalResponse result = apiInstance.extensionCtrlGetAccountExtensionByID(accountId, extensionNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#extensionCtrlGetAccountExtensionByID");
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
| **accountId** | **String**| The Vonage Business Cloud account ID | |
| **extensionNumber** | **BigDecimal**| The extension number | |

### Return type

[**EndUserRouteHalResponse**](EndUserRouteHalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Extension not found |  -  |

<a id="extensionCtrlGetAccountExtensions"></a>
# **extensionCtrlGetAccountExtensions**
> EndUserRouteHalResponse extensionCtrlGetAccountExtensions(accountId, pageSize, page, locationId, phoneNumber, loginName, email)

Get account extensions data by account ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/provisioning");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Vonage Business Cloud account ID
    BigDecimal pageSize = new BigDecimal("10"); // BigDecimal | Number of records per page
    BigDecimal page = new BigDecimal("10"); // BigDecimal | Current page number
    BigDecimal locationId = new BigDecimal("145214"); // BigDecimal | Filter by location id
    String phoneNumber = "14155550100"; // String | Filter by phone number
    String loginName = "jsmith"; // String | Filter by login name
    String email = "john.smith@example.com"; // String | Filter by email address
    try {
      EndUserRouteHalResponse result = apiInstance.extensionCtrlGetAccountExtensions(accountId, pageSize, page, locationId, phoneNumber, loginName, email);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#extensionCtrlGetAccountExtensions");
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
| **accountId** | **String**| The Vonage Business Cloud account ID | |
| **pageSize** | **BigDecimal**| Number of records per page | [optional] |
| **page** | **BigDecimal**| Current page number | [optional] |
| **locationId** | **BigDecimal**| Filter by location id | [optional] |
| **phoneNumber** | **String**| Filter by phone number | [optional] |
| **loginName** | **String**| Filter by login name | [optional] |
| **email** | **String**| Filter by email address | [optional] |

### Return type

[**EndUserRouteHalResponse**](EndUserRouteHalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Invalid parameters given |  -  |

