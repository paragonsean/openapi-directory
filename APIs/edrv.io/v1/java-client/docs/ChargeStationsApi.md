# ChargeStationsApi

All URIs are relative to *http://api.edrv.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteChargeStation**](ChargeStationsApi.md#deleteChargeStation) | **DELETE** /v1/chargestations/{id} |  |
| [**getChargeStation**](ChargeStationsApi.md#getChargeStation) | **GET** /v1/chargestations/{id} |  |
| [**getChargeStationConnectors**](ChargeStationsApi.md#getChargeStationConnectors) | **GET** /v1/chargestations/{id}/connectors |  |
| [**getChargeStations**](ChargeStationsApi.md#getChargeStations) | **GET** /v1/chargestations |  |
| [**patchChargeStation**](ChargeStationsApi.md#patchChargeStation) | **PATCH** /v1/chargestations/{id} |  |
| [**postChargeStations**](ChargeStationsApi.md#postChargeStations) | **POST** /v1/chargestations |  |


<a id="deleteChargeStation"></a>
# **deleteChargeStation**
> deleteChargeStation(id)



Use to delete a charge station

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargeStationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ChargeStationsApi apiInstance = new ChargeStationsApi(defaultClient);
    String id = "id_example"; // String | The charge station id that needs to be deleted
    try {
      apiInstance.deleteChargeStation(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargeStationsApi#deleteChargeStation");
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
| **id** | **String**| The charge station id that needs to be deleted | |

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
| **200** | Returns the deleted chargestion object |  -  |
| **400** | Request Error |  -  |

<a id="getChargeStation"></a>
# **getChargeStation**
> getChargeStation(id, includeLocation, includeEvses, includeOrganization)



Get a single charge station&#39;s data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargeStationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ChargeStationsApi apiInstance = new ChargeStationsApi(defaultClient);
    String id = "id_example"; // String | The charge station id that needs to be fetched
    Boolean includeLocation = true; // Boolean | Populate location
    Boolean includeEvses = true; // Boolean | Populate evses
    Boolean includeOrganization = true; // Boolean | Populate organization
    try {
      apiInstance.getChargeStation(id, includeLocation, includeEvses, includeOrganization);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargeStationsApi#getChargeStation");
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
| **id** | **String**| The charge station id that needs to be fetched | |
| **includeLocation** | **Boolean**| Populate location | [optional] |
| **includeEvses** | **Boolean**| Populate evses | [optional] |
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
| **200** | Returns a chargestion object |  -  |

<a id="getChargeStationConnectors"></a>
# **getChargeStationConnectors**
> getChargeStationConnectors(id, includeEvse, includeOrganization)



List connectors for a chargestation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargeStationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ChargeStationsApi apiInstance = new ChargeStationsApi(defaultClient);
    String id = "id_example"; // String | chargeStation id
    Boolean includeEvse = true; // Boolean | Populate evse
    Boolean includeOrganization = true; // Boolean | Populate organization
    try {
      apiInstance.getChargeStationConnectors(id, includeEvse, includeOrganization);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargeStationsApi#getChargeStationConnectors");
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
| **id** | **String**| chargeStation id | |
| **includeEvse** | **Boolean**| Populate evse | [optional] |
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
| **200** | Returns an array of connector objects |  -  |
| **400** | A failure response |  -  |

<a id="getChargeStations"></a>
# **getChargeStations**
> getChargeStations(organization, location, online, active, _public, paginateLimit, paginatePage, paginateEnabled, sortBy, sortOrder, createdAt$gte, createdAt$lte, updatedAt$gte, updatedAt$lte, includeLocation, includeEvses, includeOrganization)



List all Chargestations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargeStationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ChargeStationsApi apiInstance = new ChargeStationsApi(defaultClient);
    String organization = "organization_example"; // String | Filter by Org. Id
    String location = "location_example"; // String | Filter by Location Id
    Boolean online = true; // Boolean | Filter by Online Status
    Boolean active = true; // Boolean | Chargestations that have been activated/deactivated by the admin
    Boolean _public = true; // Boolean | Chargestations that are public
    Integer paginateLimit = 20; // Integer | Number of results per page
    String paginatePage = "paginatePage_example"; // String | The queried page index
    Boolean paginateEnabled = true; // Boolean | Enable pagination
    String sortBy = "createdAt"; // String | Sort data by this key
    String sortOrder = "desc"; // String | asc to sort ascending (default is desc - descending)
    OffsetDateTime createdAt$gte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime createdAt$lte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime updatedAt$gte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime updatedAt$lte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    Boolean includeLocation = true; // Boolean | Populate location
    Boolean includeEvses = true; // Boolean | Populate evses
    Boolean includeOrganization = true; // Boolean | Populate organization
    try {
      apiInstance.getChargeStations(organization, location, online, active, _public, paginateLimit, paginatePage, paginateEnabled, sortBy, sortOrder, createdAt$gte, createdAt$lte, updatedAt$gte, updatedAt$lte, includeLocation, includeEvses, includeOrganization);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargeStationsApi#getChargeStations");
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
| **organization** | **String**| Filter by Org. Id | [optional] |
| **location** | **String**| Filter by Location Id | [optional] |
| **online** | **Boolean**| Filter by Online Status | [optional] |
| **active** | **Boolean**| Chargestations that have been activated/deactivated by the admin | [optional] |
| **_public** | **Boolean**| Chargestations that are public | [optional] |
| **paginateLimit** | **Integer**| Number of results per page | [optional] [default to 20] |
| **paginatePage** | **String**| The queried page index | [optional] |
| **paginateEnabled** | **Boolean**| Enable pagination | [optional] [default to true] |
| **sortBy** | **String**| Sort data by this key | [optional] [default to createdAt] |
| **sortOrder** | **String**| asc to sort ascending (default is desc - descending) | [optional] [default to desc] [enum: desc, asc] |
| **createdAt$gte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **createdAt$lte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **updatedAt$gte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **updatedAt$lte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **includeLocation** | **Boolean**| Populate location | [optional] |
| **includeEvses** | **Boolean**| Populate evses | [optional] |
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
| **200** | An array of chargestation objects |  -  |

<a id="patchChargeStation"></a>
# **patchChargeStation**
> PatchChargeStation200Response patchChargeStation(id, schema1)



Update a charge station&#39;s data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargeStationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ChargeStationsApi apiInstance = new ChargeStationsApi(defaultClient);
    String id = "id_example"; // String | ID of charge station that needs to be updated
    Schema1 schema1 = new Schema1(); // Schema1 | Include charge station properties to update here
    try {
      PatchChargeStation200Response result = apiInstance.patchChargeStation(id, schema1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargeStationsApi#patchChargeStation");
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
| **id** | **String**| ID of charge station that needs to be updated | |
| **schema1** | [**Schema1**](Schema1.md)| Include charge station properties to update here | |

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
| **200** | Returns the updated chargestion object |  -  |
| **400** | A failure response |  -  |

<a id="postChargeStations"></a>
# **postChargeStations**
> PostChargeStations201Response postChargeStations(schema1)



Create a new charge station

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargeStationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ChargeStationsApi apiInstance = new ChargeStationsApi(defaultClient);
    Schema1 schema1 = new Schema1(); // Schema1 | Include charge station properties to create here
    try {
      PostChargeStations201Response result = apiInstance.postChargeStations(schema1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargeStationsApi#postChargeStations");
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
| **schema1** | [**Schema1**](Schema1.md)| Include charge station properties to create here | |

### Return type

[**PostChargeStations201Response**](PostChargeStations201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Returns the newly created chargestion object |  -  |
| **400** | A failure response |  -  |

