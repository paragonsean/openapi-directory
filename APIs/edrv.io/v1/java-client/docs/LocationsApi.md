# LocationsApi

All URIs are relative to *http://api.edrv.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteLocation**](LocationsApi.md#deleteLocation) | **DELETE** /v1/location/{id} |  |
| [**getLocation**](LocationsApi.md#getLocation) | **GET** /v1/location/{id} |  |
| [**getLocations**](LocationsApi.md#getLocations) | **GET** /v1/locations |  |
| [**patchLocation**](LocationsApi.md#patchLocation) | **PATCH** /v1/location/{id} |  |
| [**postLocations**](LocationsApi.md#postLocations) | **POST** /v1/locations |  |


<a id="deleteLocation"></a>
# **deleteLocation**
> deleteLocation(id)



Delete a location

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
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | The location id that needs to be deleted
    try {
      apiInstance.deleteLocation(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#deleteLocation");
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
| **id** | **String**| The location id that needs to be deleted | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the deleted location object |  -  |

<a id="getLocation"></a>
# **getLocation**
> getLocation(id, includeChargestations, includeOrganization)



Get a location&#39;s data

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
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | The location id that needs to be fetched
    Boolean includeChargestations = true; // Boolean | Populate chargestations
    Boolean includeOrganization = true; // Boolean | Populate organization
    try {
      apiInstance.getLocation(id, includeChargestations, includeOrganization);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#getLocation");
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
| **id** | **String**| The location id that needs to be fetched | |
| **includeChargestations** | **Boolean**| Populate chargestations | [optional] |
| **includeOrganization** | **Boolean**| Populate organization | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a location object |  -  |

<a id="getLocations"></a>
# **getLocations**
> getLocations(paginateLimit, paginatePage, paginateEnabled, sortBy, sortOrder, createdAt$gte, createdAt$lte, updatedAt$gte, updatedAt$lte, includeOrganization)



Get Locations data

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
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    Integer paginateLimit = 20; // Integer | Number of results per page
    String paginatePage = "paginatePage_example"; // String | The queried page index
    Boolean paginateEnabled = true; // Boolean | Enable pagination
    String sortBy = "createdAt"; // String | Sort data by this key
    String sortOrder = "desc"; // String | asc to sort ascending (default is desc - descending)
    OffsetDateTime createdAt$gte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime createdAt$lte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime updatedAt$gte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime updatedAt$lte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    Boolean includeOrganization = true; // Boolean | Populate organization
    try {
      apiInstance.getLocations(paginateLimit, paginatePage, paginateEnabled, sortBy, sortOrder, createdAt$gte, createdAt$lte, updatedAt$gte, updatedAt$lte, includeOrganization);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#getLocations");
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
| **paginateLimit** | **Integer**| Number of results per page | [optional] [default to 20] |
| **paginatePage** | **String**| The queried page index | [optional] |
| **paginateEnabled** | **Boolean**| Enable pagination | [optional] [default to true] |
| **sortBy** | **String**| Sort data by this key | [optional] [default to createdAt] |
| **sortOrder** | **String**| asc to sort ascending (default is desc - descending) | [optional] [default to desc] [enum: desc, asc] |
| **createdAt$gte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **createdAt$lte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **updatedAt$gte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **updatedAt$lte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **includeOrganization** | **Boolean**| Populate organization | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | A failure response |  -  |

<a id="patchLocation"></a>
# **patchLocation**
> GetDrivers200Response patchLocation(id, patchLocationRequest)



Update a location&#39;s data

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
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | ID of location that needs to be updated
    PatchLocationRequest patchLocationRequest = new PatchLocationRequest(); // PatchLocationRequest | Include location properties to create here
    try {
      GetDrivers200Response result = apiInstance.patchLocation(id, patchLocationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#patchLocation");
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
| **id** | **String**| ID of location that needs to be updated | |
| **patchLocationRequest** | [**PatchLocationRequest**](PatchLocationRequest.md)| Include location properties to create here | |

### Return type

[**GetDrivers200Response**](GetDrivers200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the updated location object |  -  |
| **400** | A failure response |  -  |

<a id="postLocations"></a>
# **postLocations**
> PatchChargeStation200Response postLocations(postLocationsRequest)



Create a new location

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
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    PostLocationsRequest postLocationsRequest = new PostLocationsRequest(); // PostLocationsRequest | Include location properties to create here
    try {
      PatchChargeStation200Response result = apiInstance.postLocations(postLocationsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#postLocations");
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
| **postLocationsRequest** | [**PostLocationsRequest**](PostLocationsRequest.md)| Include location properties to create here | |

### Return type

[**PatchChargeStation200Response**](PatchChargeStation200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the newly created location object |  -  |
| **400** | A failure response |  -  |

