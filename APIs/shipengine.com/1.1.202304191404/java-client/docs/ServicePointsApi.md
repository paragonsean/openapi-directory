# ServicePointsApi

All URIs are relative to *https://api.shipengine.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicePointsGetById**](ServicePointsApi.md#servicePointsGetById) | **GET** /v1/service_points/{carrier_code}/{country_code}/{service_point_id} | Get Service Point By ID |
| [**servicePointsList**](ServicePointsApi.md#servicePointsList) | **POST** /v1/service_points/list | List Service Points |


<a id="servicePointsGetById"></a>
# **servicePointsGetById**
> GetServicePointByIdResponseBody servicePointsGetById(carrierCode, countryCode, servicePointId)

Get Service Point By ID

Returns a carrier service point by using the service_point_id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ServicePointsApi apiInstance = new ServicePointsApi(defaultClient);
    String carrierCode = "stamps_com"; // String | Carrier code
    String countryCode = "CA"; // String | A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1) 
    String servicePointId = "614940"; // String | 
    try {
      GetServicePointByIdResponseBody result = apiInstance.servicePointsGetById(carrierCode, countryCode, servicePointId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePointsApi#servicePointsGetById");
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
| **carrierCode** | **String**| Carrier code | |
| **countryCode** | **String**| A two-letter [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1)  | |
| **servicePointId** | **String**|  | |

### Return type

[**GetServicePointByIdResponseBody**](GetServicePointByIdResponseBody.md)

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

<a id="servicePointsList"></a>
# **servicePointsList**
> ListServicePointsResponseBody servicePointsList(getServicePointsRequest)

List Service Points

List carrier service points by location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicePointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ServicePointsApi apiInstance = new ServicePointsApi(defaultClient);
    GetServicePointsRequest getServicePointsRequest = new GetServicePointsRequest(); // GetServicePointsRequest | 
    try {
      ListServicePointsResponseBody result = apiInstance.servicePointsList(getServicePointsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicePointsApi#servicePointsList");
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
| **getServicePointsRequest** | [**GetServicePointsRequest**](GetServicePointsRequest.md)|  | |

### Return type

[**ListServicePointsResponseBody**](ListServicePointsResponseBody.md)

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

