# LocationsApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createLocation**](LocationsApi.md#createLocation) | **POST** /v2/locations | CreateLocation |
| [**listLocations**](LocationsApi.md#listLocations) | **GET** /v2/locations | ListLocations |
| [**retrieveLocation**](LocationsApi.md#retrieveLocation) | **GET** /v2/locations/{location_id} | RetrieveLocation |
| [**updateLocation**](LocationsApi.md#updateLocation) | **PUT** /v2/locations/{location_id} | UpdateLocation |


<a id="createLocation"></a>
# **createLocation**
> CreateLocationResponse createLocation(createLocationRequest)

CreateLocation

Creates a location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    CreateLocationRequest createLocationRequest = new CreateLocationRequest(); // CreateLocationRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CreateLocationResponse result = apiInstance.createLocation(createLocationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#createLocation");
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
| **createLocationRequest** | [**CreateLocationRequest**](CreateLocationRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CreateLocationResponse**](CreateLocationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listLocations"></a>
# **listLocations**
> ListLocationsResponse listLocations()

ListLocations

Provides information of all locations of a business.  Many Square API endpoints require a &#x60;location_id&#x60; parameter. The &#x60;id&#x60; field of the [&#x60;Location&#x60;](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) objects returned by this endpoint correspond to that &#x60;location_id&#x60; parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    try {
      ListLocationsResponse result = apiInstance.listLocations();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#listLocations");
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

[**ListLocationsResponse**](ListLocationsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveLocation"></a>
# **retrieveLocation**
> RetrieveLocationResponse retrieveLocation(locationId)

RetrieveLocation

Retrieves details of a location. You can specify \&quot;main\&quot;  as the location ID to retrieve details of the  main location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String locationId = "locationId_example"; // String | The ID of the location to retrieve. If you specify the string \"main\", then the endpoint returns the main location.
    try {
      RetrieveLocationResponse result = apiInstance.retrieveLocation(locationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#retrieveLocation");
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
| **locationId** | **String**| The ID of the location to retrieve. If you specify the string \&quot;main\&quot;, then the endpoint returns the main location. | |

### Return type

[**RetrieveLocationResponse**](RetrieveLocationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="updateLocation"></a>
# **updateLocation**
> UpdateLocationResponse updateLocation(locationId, updateLocationRequest)

UpdateLocation

Updates a location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String locationId = "locationId_example"; // String | The ID of the location to update.
    UpdateLocationRequest updateLocationRequest = new UpdateLocationRequest(); // UpdateLocationRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      UpdateLocationResponse result = apiInstance.updateLocation(locationId, updateLocationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#updateLocation");
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
| **locationId** | **String**| The ID of the location to update. | |
| **updateLocationRequest** | [**UpdateLocationRequest**](UpdateLocationRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**UpdateLocationResponse**](UpdateLocationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

