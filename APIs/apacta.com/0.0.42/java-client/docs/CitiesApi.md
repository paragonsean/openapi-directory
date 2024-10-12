# CitiesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**citiesCityIdGet**](CitiesApi.md#citiesCityIdGet) | **GET** /cities/{city_id} | Get details about one city |
| [**citiesGet**](CitiesApi.md#citiesGet) | **GET** /cities | Get list of cities supported in Apacta |


<a id="citiesCityIdGet"></a>
# **citiesCityIdGet**
> CitiesCityIdGet200Response citiesCityIdGet(cityId)

Get details about one city

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CitiesApi apiInstance = new CitiesApi(defaultClient);
    String cityId = "cityId_example"; // String | 
    try {
      CitiesCityIdGet200Response result = apiInstance.citiesCityIdGet(cityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CitiesApi#citiesCityIdGet");
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
| **cityId** | **String**|  | |

### Return type

[**CitiesCityIdGet200Response**](CitiesCityIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="citiesGet"></a>
# **citiesGet**
> CitiesGet200Response citiesGet(zipCode, name, includeAll)

Get list of cities supported in Apacta

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CitiesApi apiInstance = new CitiesApi(defaultClient);
    String zipCode = "zipCode_example"; // String | Used to search for a city with specific zip code
    String name = "name_example"; // String | Used to search for a city by name
    Boolean includeAll = true; // Boolean | Used to search for a city without filtering by country
    try {
      CitiesGet200Response result = apiInstance.citiesGet(zipCode, name, includeAll);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CitiesApi#citiesGet");
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
| **zipCode** | **String**| Used to search for a city with specific zip code | [optional] |
| **name** | **String**| Used to search for a city by name | [optional] |
| **includeAll** | **Boolean**| Used to search for a city without filtering by country | [optional] |

### Return type

[**CitiesGet200Response**](CitiesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

