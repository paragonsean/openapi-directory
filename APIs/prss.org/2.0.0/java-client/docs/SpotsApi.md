# SpotsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2SpotsGet**](SpotsApi.md#apiV2SpotsGet) | **GET** /api/v2/spots | Returns the spots matching the query parameters. |
| [**apiV2SpotsIdDelete**](SpotsApi.md#apiV2SpotsIdDelete) | **DELETE** /api/v2/spots/{id} | Deletes the spot with the given ID. |
| [**apiV2SpotsIdGet**](SpotsApi.md#apiV2SpotsIdGet) | **GET** /api/v2/spots/{id} | Returns the spot matching the given ID. |
| [**apiV2SpotsPost**](SpotsApi.md#apiV2SpotsPost) | **POST** /api/v2/spots | Creates a new spot. |


<a id="apiV2SpotsGet"></a>
# **apiV2SpotsGet**
> List&lt;Spot&gt; apiV2SpotsGet(pageStart, pageSize, orderById)

Returns the spots matching the query parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpotsApi apiInstance = new SpotsApi(defaultClient);
    Integer pageStart = 0; // Integer | The start page of the spot to return. The first item is indexed at 0.
    Integer pageSize = 500; // Integer | The number of items to return. Must be between 0 and 500, inclusive.
    String orderById = "asc"; // String | The sort order of the list of spots, based on spot ID. If unspecified, the spots are returned in random order. If using paging to iterate through the results, sort order should be specified.
    try {
      List<Spot> result = apiInstance.apiV2SpotsGet(pageStart, pageSize, orderById);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpotsApi#apiV2SpotsGet");
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
| **pageStart** | **Integer**| The start page of the spot to return. The first item is indexed at 0. | [optional] [default to 0] |
| **pageSize** | **Integer**| The number of items to return. Must be between 0 and 500, inclusive. | [optional] [default to 500] |
| **orderById** | **String**| The sort order of the list of spots, based on spot ID. If unspecified, the spots are returned in random order. If using paging to iterate through the results, sort order should be specified. | [optional] [enum: asc, desc] |

### Return type

[**List&lt;Spot&gt;**](Spot.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The spots matching the query parameters |  -  |
| **403** | Authorization failed, or the user is not permitted to view these spots. |  -  |
| **404** | The spot cannot be found. |  -  |

<a id="apiV2SpotsIdDelete"></a>
# **apiV2SpotsIdDelete**
> apiV2SpotsIdDelete(id)

Deletes the spot with the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpotsApi apiInstance = new SpotsApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      apiInstance.apiV2SpotsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpotsApi#apiV2SpotsIdDelete");
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
| **id** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The spot was deleted. |  -  |
| **403** | Authorization failed, or the user is not permitted to delete the spot. |  -  |
| **404** | The spot cannot be found. |  -  |

<a id="apiV2SpotsIdGet"></a>
# **apiV2SpotsIdGet**
> Spot apiV2SpotsIdGet(id)

Returns the spot matching the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpotsApi apiInstance = new SpotsApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      Spot result = apiInstance.apiV2SpotsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpotsApi#apiV2SpotsIdGet");
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
| **id** | **Long**|  | |

### Return type

[**Spot**](Spot.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The spot with the given ID. |  -  |
| **403** | Authorization failed, or the user is not permitted to view the spot. |  -  |
| **404** | The spot information cannot be found. |  -  |

<a id="apiV2SpotsPost"></a>
# **apiV2SpotsPost**
> Spot apiV2SpotsPost(cdDriveUri, name, notes)

Creates a new spot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpotsApi apiInstance = new SpotsApi(defaultClient);
    String cdDriveUri = "cdDriveUri_example"; // String | The URI to the spot content in CD Drive. Format should be 'cddrive:id:{value}' or 'cddrive://{path}'.
    String name = "name_example"; // String | The name of the spot to create/update.
    String notes = "notes_example"; // String | Notes pertaining to the spot.
    try {
      Spot result = apiInstance.apiV2SpotsPost(cdDriveUri, name, notes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpotsApi#apiV2SpotsPost");
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
| **cdDriveUri** | **String**| The URI to the spot content in CD Drive. Format should be &#39;cddrive:id:{value}&#39; or &#39;cddrive://{path}&#39;. | |
| **name** | **String**| The name of the spot to create/update. | |
| **notes** | **String**| Notes pertaining to the spot. | |

### Return type

[**Spot**](Spot.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created spot with fields populated. |  -  |
| **400** | The request is missing required data or invalid. |  -  |
| **403** | Authorization failed, or the user is not permitted to create the spot. |  -  |
| **404** | The information for creating the spot cannot be found. |  -  |

