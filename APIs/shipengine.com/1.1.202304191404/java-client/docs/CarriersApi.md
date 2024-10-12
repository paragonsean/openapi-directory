# CarriersApi

All URIs are relative to *https://api.shipengine.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addFundsToCarrier**](CarriersApi.md#addFundsToCarrier) | **PUT** /v1/carriers/{carrier_id}/add_funds | Add Funds To Carrier |
| [**getCarrierById**](CarriersApi.md#getCarrierById) | **GET** /v1/carriers/{carrier_id} | Get Carrier By ID |
| [**getCarrierOptions**](CarriersApi.md#getCarrierOptions) | **GET** /v1/carriers/{carrier_id}/options | Get Carrier Options |
| [**listCarrierPackageTypes**](CarriersApi.md#listCarrierPackageTypes) | **GET** /v1/carriers/{carrier_id}/packages | List Carrier Package Types |
| [**listCarrierServices**](CarriersApi.md#listCarrierServices) | **GET** /v1/carriers/{carrier_id}/services | List Carrier Services |
| [**listCarriers**](CarriersApi.md#listCarriers) | **GET** /v1/carriers | List Carriers |


<a id="addFundsToCarrier"></a>
# **addFundsToCarrier**
> AddFundsToCarrierResponseBody addFundsToCarrier(carrierId, addFundsToCarrierRequestBody)

Add Funds To Carrier

Add Funds To A Carrier

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarriersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CarriersApi apiInstance = new CarriersApi(defaultClient);
    String carrierId = "se-28529731"; // String | Carrier ID
    AddFundsToCarrierRequestBody addFundsToCarrierRequestBody = new AddFundsToCarrierRequestBody(); // AddFundsToCarrierRequestBody | 
    try {
      AddFundsToCarrierResponseBody result = apiInstance.addFundsToCarrier(carrierId, addFundsToCarrierRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarriersApi#addFundsToCarrier");
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
| **carrierId** | **String**| Carrier ID | |
| **addFundsToCarrierRequestBody** | [**AddFundsToCarrierRequestBody**](AddFundsToCarrierRequestBody.md)|  | |

### Return type

[**AddFundsToCarrierResponseBody**](AddFundsToCarrierResponseBody.md)

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

<a id="getCarrierById"></a>
# **getCarrierById**
> GetCarrierByIdResponseBody getCarrierById(carrierId)

Get Carrier By ID

Retrive carrier info by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarriersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CarriersApi apiInstance = new CarriersApi(defaultClient);
    String carrierId = "se-28529731"; // String | Carrier ID
    try {
      GetCarrierByIdResponseBody result = apiInstance.getCarrierById(carrierId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarriersApi#getCarrierById");
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
| **carrierId** | **String**| Carrier ID | |

### Return type

[**GetCarrierByIdResponseBody**](GetCarrierByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="getCarrierOptions"></a>
# **getCarrierOptions**
> GetCarrierOptionsResponseBody getCarrierOptions(carrierId)

Get Carrier Options

Get a list of the options available for the carrier

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarriersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CarriersApi apiInstance = new CarriersApi(defaultClient);
    String carrierId = "se-28529731"; // String | Carrier ID
    try {
      GetCarrierOptionsResponseBody result = apiInstance.getCarrierOptions(carrierId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarriersApi#getCarrierOptions");
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
| **carrierId** | **String**| Carrier ID | |

### Return type

[**GetCarrierOptionsResponseBody**](GetCarrierOptionsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="listCarrierPackageTypes"></a>
# **listCarrierPackageTypes**
> ListCarrierPackageTypesResponseBody listCarrierPackageTypes(carrierId)

List Carrier Package Types

List the package types associated with the carrier

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarriersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CarriersApi apiInstance = new CarriersApi(defaultClient);
    String carrierId = "se-28529731"; // String | Carrier ID
    try {
      ListCarrierPackageTypesResponseBody result = apiInstance.listCarrierPackageTypes(carrierId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarriersApi#listCarrierPackageTypes");
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
| **carrierId** | **String**| Carrier ID | |

### Return type

[**ListCarrierPackageTypesResponseBody**](ListCarrierPackageTypesResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="listCarrierServices"></a>
# **listCarrierServices**
> ListCarrierServicesResponseBody listCarrierServices(carrierId)

List Carrier Services

List the services associated with the carrier ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarriersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CarriersApi apiInstance = new CarriersApi(defaultClient);
    String carrierId = "se-28529731"; // String | Carrier ID
    try {
      ListCarrierServicesResponseBody result = apiInstance.listCarrierServices(carrierId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarriersApi#listCarrierServices");
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
| **carrierId** | **String**| Carrier ID | |

### Return type

[**ListCarrierServicesResponseBody**](ListCarrierServicesResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="listCarriers"></a>
# **listCarriers**
> GetCarriersResponseBody listCarriers()

List Carriers

List all carriers that have been added to this account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarriersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CarriersApi apiInstance = new CarriersApi(defaultClient);
    try {
      GetCarriersResponseBody result = apiInstance.listCarriers();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarriersApi#listCarriers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetCarriersResponseBody**](GetCarriersResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **207** | The request was a partial success. It contains results, as well as errors. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

