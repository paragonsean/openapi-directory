# DefaultApi

All URIs are relative to *https://api.vonage.com/t/vbc.prod/provisioning*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountCtrlGetAccountServicesByAccountID**](DefaultApi.md#accountCtrlGetAccountServicesByAccountID) | **GET** /api/accounts/{account_id} | Get account data by ID |
| [**accountCtrlGetLocationByID**](DefaultApi.md#accountCtrlGetLocationByID) | **GET** /api/accounts/{account_id}/locations/{location_id} | Get location data by account ID and location ID |
| [**accountCtrlGetLocationsByAccountID**](DefaultApi.md#accountCtrlGetLocationsByAccountID) | **GET** /api/accounts/{account_id}/locations | Get account locations data by account ID |


<a id="accountCtrlGetAccountServicesByAccountID"></a>
# **accountCtrlGetAccountServicesByAccountID**
> AccountHalResponse accountCtrlGetAccountServicesByAccountID(accountId)

Get account data by ID

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
    BigDecimal accountId = new BigDecimal("571700"); // BigDecimal | The Vonage Business Cloud account ID
    try {
      AccountHalResponse result = apiInstance.accountCtrlGetAccountServicesByAccountID(accountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#accountCtrlGetAccountServicesByAccountID");
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
| **accountId** | **BigDecimal**| The Vonage Business Cloud account ID | |

### Return type

[**AccountHalResponse**](AccountHalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Account not found |  -  |

<a id="accountCtrlGetLocationByID"></a>
# **accountCtrlGetLocationByID**
> LocationHalResponse accountCtrlGetLocationByID(accountId, locationId)

Get location data by account ID and location ID

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
    BigDecimal accountId = new BigDecimal("571700"); // BigDecimal | The Vonage Business Cloud account ID
    BigDecimal locationId = new BigDecimal("327910"); // BigDecimal | The Vonage Business Cloud location ID
    try {
      LocationHalResponse result = apiInstance.accountCtrlGetLocationByID(accountId, locationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#accountCtrlGetLocationByID");
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
| **accountId** | **BigDecimal**| The Vonage Business Cloud account ID | |
| **locationId** | **BigDecimal**| The Vonage Business Cloud location ID | |

### Return type

[**LocationHalResponse**](LocationHalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Location not found |  -  |

<a id="accountCtrlGetLocationsByAccountID"></a>
# **accountCtrlGetLocationsByAccountID**
> LocationsHalResponse accountCtrlGetLocationsByAccountID(accountId)

Get account locations data by account ID

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
    BigDecimal accountId = new BigDecimal("571700"); // BigDecimal | The Vonage Business Cloud account ID
    try {
      LocationsHalResponse result = apiInstance.accountCtrlGetLocationsByAccountID(accountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#accountCtrlGetLocationsByAccountID");
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
| **accountId** | **BigDecimal**| The Vonage Business Cloud account ID | |

### Return type

[**LocationsHalResponse**](LocationsHalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

