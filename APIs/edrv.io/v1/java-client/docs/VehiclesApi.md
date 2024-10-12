# VehiclesApi

All URIs are relative to *http://api.edrv.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVehicle**](VehiclesApi.md#getVehicle) | **GET** /v1/vehicles/{id} |  |
| [**getVehicleBattery**](VehiclesApi.md#getVehicleBattery) | **GET** /v1/vehicles/{id}/battery |  |
| [**getVehicleCharge**](VehiclesApi.md#getVehicleCharge) | **GET** /v1/vehicles/{id}/charge |  |
| [**getVehicleLocation**](VehiclesApi.md#getVehicleLocation) | **GET** /v1/vehicles/{id}/location |  |
| [**getVehicleOdometer**](VehiclesApi.md#getVehicleOdometer) | **GET** /v1/vehicles/{id}/odometer |  |
| [**getVehicles**](VehiclesApi.md#getVehicles) | **GET** /v1/vehicles |  |
| [**postCharge**](VehiclesApi.md#postCharge) | **POST** /v1/vehicles/{id}/charge |  |


<a id="getVehicle"></a>
# **getVehicle**
> getVehicle(id, includeDriver, includeToken, includeOrganization)



Get a vehicle&#39;s data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    String id = "id_example"; // String | The vehicule id that needs to be fetched
    Boolean includeDriver = true; // Boolean | Populate driver
    Boolean includeToken = true; // Boolean | Populate token
    Boolean includeOrganization = true; // Boolean | Populate organization
    try {
      apiInstance.getVehicle(id, includeDriver, includeToken, includeOrganization);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#getVehicle");
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
| **id** | **String**| The vehicule id that needs to be fetched | |
| **includeDriver** | **Boolean**| Populate driver | [optional] |
| **includeToken** | **Boolean**| Populate token | [optional] |
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
| **200** | Returns a vehicle object |  -  |

<a id="getVehicleBattery"></a>
# **getVehicleBattery**
> getVehicleBattery(id)



Get a vehicle&#39;s battery

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    String id = "id_example"; // String | The vehicle id that needs to be fetched
    try {
      apiInstance.getVehicleBattery(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#getVehicleBattery");
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
| **id** | **String**| The vehicle id that needs to be fetched | |

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
| **200** | Returns a vehicle object |  -  |

<a id="getVehicleCharge"></a>
# **getVehicleCharge**
> getVehicleCharge(id)



Get a vehicle&#39;s charge

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    String id = "id_example"; // String | The vehicle id that needs to be fetched
    try {
      apiInstance.getVehicleCharge(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#getVehicleCharge");
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
| **id** | **String**| The vehicle id that needs to be fetched | |

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
| **200** | Returns a vehicle object |  -  |

<a id="getVehicleLocation"></a>
# **getVehicleLocation**
> getVehicleLocation(id)



Get a vehicle&#39;s location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    String id = "id_example"; // String | The vehicle id that needs to be fetched
    try {
      apiInstance.getVehicleLocation(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#getVehicleLocation");
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
| **id** | **String**| The vehicle id that needs to be fetched | |

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
| **200** | Returns a vehicle object |  -  |

<a id="getVehicleOdometer"></a>
# **getVehicleOdometer**
> getVehicleOdometer(id)



Get a vehicle&#39;s odometer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    String id = "id_example"; // String | The vehicle id that needs to be fetched
    try {
      apiInstance.getVehicleOdometer(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#getVehicleOdometer");
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
| **id** | **String**| The vehicle id that needs to be fetched | |

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
| **200** | Returns a vehicle object |  -  |

<a id="getVehicles"></a>
# **getVehicles**
> GetDrivers200Response getVehicles(active, paginateLimit, paginatePage, paginateEnabled, sortBy, sortOrder, createdAt$gte, createdAt$lte, updatedAt$gte, updatedAt$lte, includeDriver, includeToken, includeOrganization)



List all vehicles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    Boolean active = true; // Boolean | Get a list of active vehicles
    Integer paginateLimit = 20; // Integer | Number of results per page
    String paginatePage = "paginatePage_example"; // String | The queried page index
    Boolean paginateEnabled = true; // Boolean | Enable pagination
    String sortBy = "createdAt"; // String | Sort data by this key
    String sortOrder = "desc"; // String | asc to sort ascending (default is desc - descending)
    OffsetDateTime createdAt$gte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime createdAt$lte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime updatedAt$gte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime updatedAt$lte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    Boolean includeDriver = true; // Boolean | Populate driver
    Boolean includeToken = true; // Boolean | Populate token
    Boolean includeOrganization = true; // Boolean | Populate organization
    try {
      GetDrivers200Response result = apiInstance.getVehicles(active, paginateLimit, paginatePage, paginateEnabled, sortBy, sortOrder, createdAt$gte, createdAt$lte, updatedAt$gte, updatedAt$lte, includeDriver, includeToken, includeOrganization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#getVehicles");
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
| **active** | **Boolean**| Get a list of active vehicles | [optional] |
| **paginateLimit** | **Integer**| Number of results per page | [optional] [default to 20] |
| **paginatePage** | **String**| The queried page index | [optional] |
| **paginateEnabled** | **Boolean**| Enable pagination | [optional] [default to true] |
| **sortBy** | **String**| Sort data by this key | [optional] [default to createdAt] |
| **sortOrder** | **String**| asc to sort ascending (default is desc - descending) | [optional] [default to desc] [enum: desc, asc] |
| **createdAt$gte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **createdAt$lte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **updatedAt$gte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **updatedAt$lte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **includeDriver** | **Boolean**| Populate driver | [optional] |
| **includeToken** | **Boolean**| Populate token | [optional] |
| **includeOrganization** | **Boolean**| Populate organization | [optional] |

### Return type

[**GetDrivers200Response**](GetDrivers200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of vehicle objects |  -  |
| **400** | A failure response |  -  |

<a id="postCharge"></a>
# **postCharge**
> PatchChargeStation200Response postCharge(id, postChargeRequest)



Change charge

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    String id = "id_example"; // String | The vehicle id that needs to be fetched
    PostChargeRequest postChargeRequest = new PostChargeRequest(); // PostChargeRequest | Include command properties to send here
    try {
      PatchChargeStation200Response result = apiInstance.postCharge(id, postChargeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#postCharge");
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
| **id** | **String**| The vehicle id that needs to be fetched | |
| **postChargeRequest** | [**PostChargeRequest**](PostChargeRequest.md)| Include command properties to send here | |

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
| **200** | Returns the status of the command |  -  |
| **400** | A failure response |  -  |

