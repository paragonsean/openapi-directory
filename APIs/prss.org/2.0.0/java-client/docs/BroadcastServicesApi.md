# BroadcastServicesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2BroadcastservicesGet**](BroadcastServicesApi.md#apiV2BroadcastservicesGet) | **GET** /api/v2/broadcastservices | Gets broadcast services matching the given criteria. |
| [**apiV2BroadcastservicesIdGet**](BroadcastServicesApi.md#apiV2BroadcastservicesIdGet) | **GET** /api/v2/broadcastservices/{id} | Returns the broadcast service matching the given ID. |


<a id="apiV2BroadcastservicesGet"></a>
# **apiV2BroadcastservicesGet**
> List&lt;Episode&gt; apiV2BroadcastservicesGet(pageStart, pageSize, orderById)

Gets broadcast services matching the given criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BroadcastServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BroadcastServicesApi apiInstance = new BroadcastServicesApi(defaultClient);
    Integer pageStart = 0; // Integer | The start page of the results to return. The first item is indexed at 0.
    Integer pageSize = 500; // Integer | The number of items to return. Must be between 0 and 500, inclusive.
    String orderById = "asc"; // String | The sort order of the list of broadcast services, based on broadcast service ID. If unspecified, the broadcast services are returned in random order. If using paging to iterate through the results, sort order should be specified.
    try {
      List<Episode> result = apiInstance.apiV2BroadcastservicesGet(pageStart, pageSize, orderById);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BroadcastServicesApi#apiV2BroadcastservicesGet");
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
| **pageStart** | **Integer**| The start page of the results to return. The first item is indexed at 0. | [optional] [default to 0] |
| **pageSize** | **Integer**| The number of items to return. Must be between 0 and 500, inclusive. | [optional] [default to 500] |
| **orderById** | **String**| The sort order of the list of broadcast services, based on broadcast service ID. If unspecified, the broadcast services are returned in random order. If using paging to iterate through the results, sort order should be specified. | [optional] [enum: asc, desc] |

### Return type

[**List&lt;Episode&gt;**](Episode.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The matching broadcast services. |  -  |
| **400** | The request is missing required data or invalid. |  -  |
| **403** | Authorization failed, username or password not found or incorrect. |  -  |

<a id="apiV2BroadcastservicesIdGet"></a>
# **apiV2BroadcastservicesIdGet**
> BroadcastService apiV2BroadcastservicesIdGet(id)

Returns the broadcast service matching the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BroadcastServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: cd_oauth2
    OAuth cd_oauth2 = (OAuth) defaultClient.getAuthentication("cd_oauth2");
    cd_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BroadcastServicesApi apiInstance = new BroadcastServicesApi(defaultClient);
    Long id = 56L; // Long | The ID of the broadcast service to find.
    try {
      BroadcastService result = apiInstance.apiV2BroadcastservicesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BroadcastServicesApi#apiV2BroadcastservicesIdGet");
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
| **id** | **Long**| The ID of the broadcast service to find. | |

### Return type

[**BroadcastService**](BroadcastService.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The matching broadcast service. |  -  |
| **403** | Authorization failed, or the user is not permitted to view this broadcast service. |  -  |
| **404** | The broadcast service cannot be found. |  -  |

