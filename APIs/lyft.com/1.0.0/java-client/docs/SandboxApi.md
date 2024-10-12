# SandboxApi

All URIs are relative to *https://api.lyft.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**setPrimeTime**](SandboxApi.md#setPrimeTime) | **PUT** /sandbox/primetime | Preset Prime Time percentage |
| [**setRideStatus**](SandboxApi.md#setRideStatus) | **PUT** /sandbox/rides/{id} | Propagate ride through ride status |
| [**setRideTypeAvailability**](SandboxApi.md#setRideTypeAvailability) | **PUT** /sandbox/ridetypes/{ride_type} | Driver availability for processing ride request |
| [**setRideTypes**](SandboxApi.md#setRideTypes) | **PUT** /sandbox/ridetypes | Preset types of rides for sandbox |


<a id="setPrimeTime"></a>
# **setPrimeTime**
> setPrimeTime(request)

Preset Prime Time percentage

Preset a Prime Time percentage in the region surrounding the specified location. This Prime Time percentage will be applied when requesting cost, or when requesting a ride in sandbox mode. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SandboxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lyft.com/v1");
    
    // Configure OAuth2 access token for authorization: Client Authentication
    OAuth Client Authentication = (OAuth) defaultClient.getAuthentication("Client Authentication");
    Client Authentication.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: User Authentication
    OAuth User Authentication = (OAuth) defaultClient.getAuthentication("User Authentication");
    User Authentication.setAccessToken("YOUR ACCESS TOKEN");

    SandboxApi apiInstance = new SandboxApi(defaultClient);
    SandboxPrimetime request = new SandboxPrimetime(); // SandboxPrimetime | Prime Time to be preset in the region surrounding the lat, lng
    try {
      apiInstance.setPrimeTime(request);
    } catch (ApiException e) {
      System.err.println("Exception when calling SandboxApi#setPrimeTime");
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
| **request** | [**SandboxPrimetime**](SandboxPrimetime.md)| Prime Time to be preset in the region surrounding the lat, lng | |

### Return type

null (empty response body)

### Authorization

[Client Authentication](../README.md#Client Authentication), [User Authentication](../README.md#User Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully applied Prime Time in sandbox |  -  |
| **400** | Validation error occurred |  -  |

<a id="setRideStatus"></a>
# **setRideStatus**
> SandboxRideUpdate setRideStatus(id, request)

Propagate ride through ride status

Propagate a sandbox-ride through various ride status 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SandboxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lyft.com/v1");
    
    // Configure OAuth2 access token for authorization: User Authentication
    OAuth User Authentication = (OAuth) defaultClient.getAuthentication("User Authentication");
    User Authentication.setAccessToken("YOUR ACCESS TOKEN");

    SandboxApi apiInstance = new SandboxApi(defaultClient);
    String id = "id_example"; // String | The ID of the ride
    SandboxRideStatus request = new SandboxRideStatus(); // SandboxRideStatus | status to propagate the ride into
    try {
      SandboxRideUpdate result = apiInstance.setRideStatus(id, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SandboxApi#setRideStatus");
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
| **id** | **String**| The ID of the ride | |
| **request** | [**SandboxRideStatus**](SandboxRideStatus.md)| status to propagate the ride into | |

### Return type

[**SandboxRideUpdate**](SandboxRideUpdate.md)

### Authorization

[User Authentication](../README.md#User Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An object with the Ride ID and the new status |  -  |
| **400** | Validation error occurred |  -  |
| **403** | User or client does not have permission to complete this request |  -  |

<a id="setRideTypeAvailability"></a>
# **setRideTypeAvailability**
> setRideTypeAvailability(rideType, request)

Driver availability for processing ride request

Set driver availability for the provided ride_type in the city/region surrounding the specified location 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SandboxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lyft.com/v1");
    
    // Configure OAuth2 access token for authorization: Client Authentication
    OAuth Client Authentication = (OAuth) defaultClient.getAuthentication("Client Authentication");
    Client Authentication.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: User Authentication
    OAuth User Authentication = (OAuth) defaultClient.getAuthentication("User Authentication");
    User Authentication.setAccessToken("YOUR ACCESS TOKEN");

    SandboxApi apiInstance = new SandboxApi(defaultClient);
    String rideType = "lyft"; // String | 
    SandboxDriverAvailability request = new SandboxDriverAvailability(); // SandboxDriverAvailability | Driver availability to be preset in the region surrounding the lat, lng
    try {
      apiInstance.setRideTypeAvailability(rideType, request);
    } catch (ApiException e) {
      System.err.println("Exception when calling SandboxApi#setRideTypeAvailability");
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
| **rideType** | **String**|  | [enum: lyft, lyft_line, lyft_plus, lyft_premier, lyft_lux, lyft_luxsuv] |
| **request** | [**SandboxDriverAvailability**](SandboxDriverAvailability.md)| Driver availability to be preset in the region surrounding the lat, lng | |

### Return type

null (empty response body)

### Authorization

[Client Authentication](../README.md#Client Authentication), [User Authentication](../README.md#User Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully set driver availability in sandbox |  -  |
| **400** | Validation error occurred |  -  |
| **404** | ride_type provided in the path is not supported in the current area |  -  |

<a id="setRideTypes"></a>
# **setRideTypes**
> SandboxRideType setRideTypes(request)

Preset types of rides for sandbox

The sandbox-ridetypes endpoint allows you to preset the ridetypes in the region surrounding the specified latitude and longitude to allow testing different scenarios 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SandboxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lyft.com/v1");
    
    // Configure OAuth2 access token for authorization: Client Authentication
    OAuth Client Authentication = (OAuth) defaultClient.getAuthentication("Client Authentication");
    Client Authentication.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: User Authentication
    OAuth User Authentication = (OAuth) defaultClient.getAuthentication("User Authentication");
    User Authentication.setAccessToken("YOUR ACCESS TOKEN");

    SandboxApi apiInstance = new SandboxApi(defaultClient);
    SandboxRideType request = new SandboxRideType(); // SandboxRideType | Ridetypes to be preset in the region surrounding the lat, lng
    try {
      SandboxRideType result = apiInstance.setRideTypes(request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SandboxApi#setRideTypes");
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
| **request** | [**SandboxRideType**](SandboxRideType.md)| Ridetypes to be preset in the region surrounding the lat, lng | |

### Return type

[**SandboxRideType**](SandboxRideType.md)

### Authorization

[Client Authentication](../README.md#Client Authentication), [User Authentication](../README.md#User Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An object listing the ridetypes at a given location |  -  |
| **400** | Validation error occurred |  -  |

