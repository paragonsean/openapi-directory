# DriversApi

All URIs are relative to *http://api.edrv.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteDriver**](DriversApi.md#deleteDriver) | **DELETE** /v1/drivers/{id} |  |
| [**getDriver**](DriversApi.md#getDriver) | **GET** /v1/drivers/{id} |  |
| [**getDrivers**](DriversApi.md#getDrivers) | **GET** /v1/drivers |  |
| [**patchDriver**](DriversApi.md#patchDriver) | **PATCH** /v1/drivers/{id} |  |
| [**postDrivers**](DriversApi.md#postDrivers) | **POST** /v1/drivers |  |


<a id="deleteDriver"></a>
# **deleteDriver**
> deleteDriver(id)



Delete a driver

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DriversApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DriversApi apiInstance = new DriversApi(defaultClient);
    String id = "id_example"; // String | The driver id that needs to be deleted
    try {
      apiInstance.deleteDriver(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DriversApi#deleteDriver");
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
| **id** | **String**| The driver id that needs to be deleted | |

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
| **200** | Returns the deleted driver object |  -  |

<a id="getDriver"></a>
# **getDriver**
> getDriver(id, includeTokens, includeGroup, includeOrganization)



Get a driver&#39;s data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DriversApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DriversApi apiInstance = new DriversApi(defaultClient);
    String id = "id_example"; // String | The driver id that needs to be fetched
    Boolean includeTokens = true; // Boolean | Populate tokens
    Boolean includeGroup = true; // Boolean | Populate group
    Boolean includeOrganization = true; // Boolean | Populate organization
    try {
      apiInstance.getDriver(id, includeTokens, includeGroup, includeOrganization);
    } catch (ApiException e) {
      System.err.println("Exception when calling DriversApi#getDriver");
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
| **id** | **String**| The driver id that needs to be fetched | |
| **includeTokens** | **Boolean**| Populate tokens | [optional] |
| **includeGroup** | **Boolean**| Populate group | [optional] |
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
| **200** | Returns a driver object |  -  |

<a id="getDrivers"></a>
# **getDrivers**
> GetDrivers200Response getDrivers(active, paginateLimit, paginatePage, paginateEnabled, sortBy, sortOrder, createdAt$gte, createdAt$lte, updatedAt$gte, updatedAt$lte, includeTokens, includeGroup, includeOrganization)



List all drivers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DriversApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DriversApi apiInstance = new DriversApi(defaultClient);
    Boolean active = true; // Boolean | Get a list of active drivers
    Integer paginateLimit = 20; // Integer | Number of results per page
    String paginatePage = "paginatePage_example"; // String | The queried page index
    Boolean paginateEnabled = true; // Boolean | Enable pagination
    String sortBy = "createdAt"; // String | Sort data by this key
    String sortOrder = "desc"; // String | asc to sort ascending (default is desc - descending)
    OffsetDateTime createdAt$gte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime createdAt$lte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime updatedAt$gte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime updatedAt$lte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    Boolean includeTokens = true; // Boolean | Populate tokens
    Boolean includeGroup = true; // Boolean | Populate group
    Boolean includeOrganization = true; // Boolean | Populate organization
    try {
      GetDrivers200Response result = apiInstance.getDrivers(active, paginateLimit, paginatePage, paginateEnabled, sortBy, sortOrder, createdAt$gte, createdAt$lte, updatedAt$gte, updatedAt$lte, includeTokens, includeGroup, includeOrganization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DriversApi#getDrivers");
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
| **active** | **Boolean**| Get a list of active drivers | [optional] |
| **paginateLimit** | **Integer**| Number of results per page | [optional] [default to 20] |
| **paginatePage** | **String**| The queried page index | [optional] |
| **paginateEnabled** | **Boolean**| Enable pagination | [optional] [default to true] |
| **sortBy** | **String**| Sort data by this key | [optional] [default to createdAt] |
| **sortOrder** | **String**| asc to sort ascending (default is desc - descending) | [optional] [default to desc] [enum: desc, asc] |
| **createdAt$gte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **createdAt$lte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **updatedAt$gte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **updatedAt$lte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **includeTokens** | **Boolean**| Populate tokens | [optional] |
| **includeGroup** | **Boolean**| Populate group | [optional] |
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
| **200** | Returns a list of driver objects |  -  |
| **400** | A failure response |  -  |

<a id="patchDriver"></a>
# **patchDriver**
> GetDrivers200Response patchDriver(id, patchDriverRequest)



Update a driver&#39;s data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DriversApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DriversApi apiInstance = new DriversApi(defaultClient);
    String id = "id_example"; // String | ID of driver that needs to be updated
    PatchDriverRequest patchDriverRequest = new PatchDriverRequest(); // PatchDriverRequest | Include driver properties to create here
    try {
      GetDrivers200Response result = apiInstance.patchDriver(id, patchDriverRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DriversApi#patchDriver");
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
| **id** | **String**| ID of driver that needs to be updated | |
| **patchDriverRequest** | [**PatchDriverRequest**](PatchDriverRequest.md)| Include driver properties to create here | |

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
| **200** | Returns the updated driver object |  -  |
| **400** | A failure response |  -  |

<a id="postDrivers"></a>
# **postDrivers**
> PatchChargeStation200Response postDrivers(postDriversRequest)



Create a new driver

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DriversApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DriversApi apiInstance = new DriversApi(defaultClient);
    PostDriversRequest postDriversRequest = new PostDriversRequest(); // PostDriversRequest | Include driver properties to create here
    try {
      PatchChargeStation200Response result = apiInstance.postDrivers(postDriversRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DriversApi#postDrivers");
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
| **postDriversRequest** | [**PostDriversRequest**](PostDriversRequest.md)| Include driver properties to create here | |

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
| **200** | Returns the newly created driver object |  -  |
| **400** | A failure response |  -  |

