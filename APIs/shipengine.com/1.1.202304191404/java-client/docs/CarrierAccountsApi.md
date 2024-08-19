# CarrierAccountsApi

All URIs are relative to *https://api.shipengine.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**connectCarrier**](CarrierAccountsApi.md#connectCarrier) | **POST** /v1/connections/carriers/{carrier_name} | Connect a carrier account |
| [**disconnectCarrier**](CarrierAccountsApi.md#disconnectCarrier) | **DELETE** /v1/connections/carriers/{carrier_name}/{carrier_id} | Disconnect a carrier |
| [**getCarrierSettings**](CarrierAccountsApi.md#getCarrierSettings) | **GET** /v1/connections/carriers/{carrier_name}/{carrier_id}/settings | Get carrier settings |
| [**updateCarrierSettings**](CarrierAccountsApi.md#updateCarrierSettings) | **PUT** /v1/connections/carriers/{carrier_name}/{carrier_id}/settings | Update carrier settings |


<a id="connectCarrier"></a>
# **connectCarrier**
> ConnectCarrierResponseBody connectCarrier(carrierName, connectCarrierRequestBody)

Connect a carrier account

Connect a carrier account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarrierAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CarrierAccountsApi apiInstance = new CarrierAccountsApi(defaultClient);
    CarrierName carrierName = CarrierName.fromValue("access_worldwide"); // CarrierName | The carrier name, such as `stamps_com`, `ups`, `fedex`, or `dhl_express`.
    ConnectCarrierRequestBody connectCarrierRequestBody = new ConnectCarrierRequestBody(); // ConnectCarrierRequestBody | 
    try {
      ConnectCarrierResponseBody result = apiInstance.connectCarrier(carrierName, connectCarrierRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarrierAccountsApi#connectCarrier");
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
| **carrierName** | [**CarrierName**](.md)| The carrier name, such as &#x60;stamps_com&#x60;, &#x60;ups&#x60;, &#x60;fedex&#x60;, or &#x60;dhl_express&#x60;. | [enum: access_worldwide, amazon_buy_shipping, amazon_shipping_uk, apc, asendia, australia_post, canada_post, dhl_ecommerce, dhl_express, dhl_express_au, dhl_express_ca, dhl_express_uk, dpd, endicia, fedex, fedex_uk, firstmile, imex, newgistics, ontrac, purolator_canada, royal_mail, rr_donnelley, seko, sendle, stamps_com, ups] |
| **connectCarrierRequestBody** | [**ConnectCarrierRequestBody**](ConnectCarrierRequestBody.md)|  | |

### Return type

[**ConnectCarrierResponseBody**](ConnectCarrierResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="disconnectCarrier"></a>
# **disconnectCarrier**
> String disconnectCarrier(carrierName, carrierId)

Disconnect a carrier

Disconnect a carrier

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarrierAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CarrierAccountsApi apiInstance = new CarrierAccountsApi(defaultClient);
    CarrierName carrierName = CarrierName.fromValue("access_worldwide"); // CarrierName | The carrier name, such as `stamps_com`, `ups`, `fedex`, or `dhl_express`.
    String carrierId = "se-28529731"; // String | Carrier ID
    try {
      String result = apiInstance.disconnectCarrier(carrierName, carrierId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarrierAccountsApi#disconnectCarrier");
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
| **carrierName** | [**CarrierName**](.md)| The carrier name, such as &#x60;stamps_com&#x60;, &#x60;ups&#x60;, &#x60;fedex&#x60;, or &#x60;dhl_express&#x60;. | [enum: access_worldwide, amazon_buy_shipping, amazon_shipping_uk, apc, asendia, australia_post, canada_post, dhl_ecommerce, dhl_express, dhl_express_au, dhl_express_ca, dhl_express_uk, dpd, endicia, fedex, fedex_uk, firstmile, imex, newgistics, ontrac, purolator_canada, royal_mail, rr_donnelley, seko, sendle, stamps_com, ups] |
| **carrierId** | **String**| Carrier ID | |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The request was successful. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="getCarrierSettings"></a>
# **getCarrierSettings**
> GetCarrierSettingsResponseBody getCarrierSettings(carrierName, carrierId)

Get carrier settings

Get carrier settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarrierAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CarrierAccountsApi apiInstance = new CarrierAccountsApi(defaultClient);
    CarrierNameWithSettings carrierName = CarrierNameWithSettings.fromValue("dhl_express"); // CarrierNameWithSettings | The carrier name, such as `ups`, `fedex`, or `dhl_express`.
    String carrierId = "se-28529731"; // String | Carrier ID
    try {
      GetCarrierSettingsResponseBody result = apiInstance.getCarrierSettings(carrierName, carrierId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarrierAccountsApi#getCarrierSettings");
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
| **carrierName** | [**CarrierNameWithSettings**](.md)| The carrier name, such as &#x60;ups&#x60;, &#x60;fedex&#x60;, or &#x60;dhl_express&#x60;. | [enum: dhl_express, fedex, newgistics, ups] |
| **carrierId** | **String**| Carrier ID | |

### Return type

[**GetCarrierSettingsResponseBody**](GetCarrierSettingsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="updateCarrierSettings"></a>
# **updateCarrierSettings**
> String updateCarrierSettings(carrierName, carrierId, updateCarrierSettingsRequestBody)

Update carrier settings

Update carrier settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarrierAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CarrierAccountsApi apiInstance = new CarrierAccountsApi(defaultClient);
    CarrierNameWithSettings carrierName = CarrierNameWithSettings.fromValue("dhl_express"); // CarrierNameWithSettings | The carrier name, such as `ups`, `fedex`, or `dhl_express`.
    String carrierId = "se-28529731"; // String | Carrier ID
    UpdateCarrierSettingsRequestBody updateCarrierSettingsRequestBody = new UpdateCarrierSettingsRequestBody(); // UpdateCarrierSettingsRequestBody | 
    try {
      String result = apiInstance.updateCarrierSettings(carrierName, carrierId, updateCarrierSettingsRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarrierAccountsApi#updateCarrierSettings");
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
| **carrierName** | [**CarrierNameWithSettings**](.md)| The carrier name, such as &#x60;ups&#x60;, &#x60;fedex&#x60;, or &#x60;dhl_express&#x60;. | [enum: dhl_express, fedex, newgistics, ups] |
| **carrierId** | **String**| Carrier ID | |
| **updateCarrierSettingsRequestBody** | [**UpdateCarrierSettingsRequestBody**](UpdateCarrierSettingsRequestBody.md)|  | |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The request was successful. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

