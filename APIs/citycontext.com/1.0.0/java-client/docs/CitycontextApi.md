# CitycontextApi

All URIs are relative to *http://api.citycontext.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**byPoint**](CitycontextApi.md#byPoint) | **GET** /@{lat},{lon} | Query by coordinates (SRID 4326 - decimal degrees) |
| [**byPostcode**](CitycontextApi.md#byPostcode) | **GET** /postcodes/{postcode} | Query by postcode |
| [**usage**](CitycontextApi.md#usage) | **GET** /usage | Get usage in current month |


<a id="byPoint"></a>
# **byPoint**
> PointInfo byPoint(lat, lon, schoolSearchRadius, parkSearchRadius)

Query by coordinates (SRID 4326 - decimal degrees)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CitycontextApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.citycontext.com/v1");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    CitycontextApi apiInstance = new CitycontextApi(defaultClient);
    Float lat = 3.4F; // Float | Latitude
    Float lon = 3.4F; // Float | Longitude
    Integer schoolSearchRadius = 56; // Integer | Search radius for schools, in metres, between 100 and 4000
    Integer parkSearchRadius = 56; // Integer | Search radius for parks, in metres, between 100 and 2000
    try {
      PointInfo result = apiInstance.byPoint(lat, lon, schoolSearchRadius, parkSearchRadius);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CitycontextApi#byPoint");
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
| **lat** | **Float**| Latitude | |
| **lon** | **Float**| Longitude | |
| **schoolSearchRadius** | **Integer**| Search radius for schools, in metres, between 100 and 4000 | [optional] |
| **parkSearchRadius** | **Integer**| Search radius for parks, in metres, between 100 and 2000 | [optional] |

### Return type

[**PointInfo**](PointInfo.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="byPostcode"></a>
# **byPostcode**
> PointInfo byPostcode(postcode, schoolSearchRadius, parkSearchRadius)

Query by postcode

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CitycontextApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.citycontext.com/v1");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    CitycontextApi apiInstance = new CitycontextApi(defaultClient);
    String postcode = "postcode_example"; // String | Postcode
    Integer schoolSearchRadius = 56; // Integer | Search radius for schools, in metres, between 100 and 4000
    Integer parkSearchRadius = 56; // Integer | Search radius for parks, in metres, between 100 and 2000
    try {
      PointInfo result = apiInstance.byPostcode(postcode, schoolSearchRadius, parkSearchRadius);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CitycontextApi#byPostcode");
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
| **postcode** | **String**| Postcode | |
| **schoolSearchRadius** | **Integer**| Search radius for schools, in metres, between 100 and 4000 | [optional] |
| **parkSearchRadius** | **Integer**| Search radius for parks, in metres, between 100 and 2000 | [optional] |

### Return type

[**PointInfo**](PointInfo.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="usage"></a>
# **usage**
> Usage usage()

Get usage in current month

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CitycontextApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.citycontext.com/v1");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    CitycontextApi apiInstance = new CitycontextApi(defaultClient);
    try {
      Usage result = apiInstance.usage();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CitycontextApi#usage");
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

[**Usage**](Usage.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

