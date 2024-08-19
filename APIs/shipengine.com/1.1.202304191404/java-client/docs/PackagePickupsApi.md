# PackagePickupsApi

All URIs are relative to *https://api.shipengine.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteScheduledPickup**](PackagePickupsApi.md#deleteScheduledPickup) | **DELETE** /v1/pickups/{pickup_id} | Delete a Scheduled Pickup |
| [**getPickupById**](PackagePickupsApi.md#getPickupById) | **GET** /v1/pickups/{pickup_id} | Get Pickup By ID |
| [**listScheduledPickups**](PackagePickupsApi.md#listScheduledPickups) | **GET** /v1/pickups | List Scheduled Pickups |
| [**schedulePickup**](PackagePickupsApi.md#schedulePickup) | **POST** /v1/pickups | Schedule a Pickup |


<a id="deleteScheduledPickup"></a>
# **deleteScheduledPickup**
> DeletePickupByIdResponseBody deleteScheduledPickup(pickupId)

Delete a Scheduled Pickup

Delete a previously-scheduled pickup by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackagePickupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    PackagePickupsApi apiInstance = new PackagePickupsApi(defaultClient);
    String pickupId = "pickupId_example"; // String | 
    try {
      DeletePickupByIdResponseBody result = apiInstance.deleteScheduledPickup(pickupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackagePickupsApi#deleteScheduledPickup");
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
| **pickupId** | **String**|  | |

### Return type

[**DeletePickupByIdResponseBody**](DeletePickupByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the &#x60;pickup_id&#x60; of the scheduled pickup that was successfully deleted  |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="getPickupById"></a>
# **getPickupById**
> GetPickupByIdResponseBody getPickupById(pickupId)

Get Pickup By ID

Get Pickup By ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackagePickupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    PackagePickupsApi apiInstance = new PackagePickupsApi(defaultClient);
    String pickupId = "pickupId_example"; // String | 
    try {
      GetPickupByIdResponseBody result = apiInstance.getPickupById(pickupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackagePickupsApi#getPickupById");
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
| **pickupId** | **String**|  | |

### Return type

[**GetPickupByIdResponseBody**](GetPickupByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="listScheduledPickups"></a>
# **listScheduledPickups**
> GetPickupsResponseBody listScheduledPickups(carrierId, warehouseId, createdAtStart, createdAtEnd, page, pageSize)

List Scheduled Pickups

List all pickups that have been scheduled for this carrier

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackagePickupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    PackagePickupsApi apiInstance = new PackagePickupsApi(defaultClient);
    String carrierId = "carrierId_example"; // String | Carrier ID
    String warehouseId = "warehouseId_example"; // String | Warehouse ID
    OffsetDateTime createdAtStart = OffsetDateTime.parse("2019-03-12T19:24:13.657Z"); // OffsetDateTime | Only return scheduled pickups that were created on or after a specific date/time
    OffsetDateTime createdAtEnd = OffsetDateTime.parse("2019-03-12T19:24:13.657Z"); // OffsetDateTime | Only return scheduled pickups that were created on or before a specific date/time
    Integer page = 1; // Integer | Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 
    Integer pageSize = 25; // Integer | The number of results to return per response.
    try {
      GetPickupsResponseBody result = apiInstance.listScheduledPickups(carrierId, warehouseId, createdAtStart, createdAtEnd, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackagePickupsApi#listScheduledPickups");
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
| **carrierId** | **String**| Carrier ID | [optional] |
| **warehouseId** | **String**| Warehouse ID | [optional] |
| **createdAtStart** | **OffsetDateTime**| Only return scheduled pickups that were created on or after a specific date/time | [optional] |
| **createdAtEnd** | **OffsetDateTime**| Only return scheduled pickups that were created on or before a specific date/time | [optional] |
| **page** | **Integer**| Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned.  | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return per response. | [optional] [default to 25] |

### Return type

[**GetPickupsResponseBody**](GetPickupsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="schedulePickup"></a>
# **schedulePickup**
> SchedulePickupResponseBody schedulePickup(schedulePickupRequestBody)

Schedule a Pickup

Schedule a package pickup with a carrier

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackagePickupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    PackagePickupsApi apiInstance = new PackagePickupsApi(defaultClient);
    SchedulePickupRequestBody schedulePickupRequestBody = new SchedulePickupRequestBody(); // SchedulePickupRequestBody | 
    try {
      SchedulePickupResponseBody result = apiInstance.schedulePickup(schedulePickupRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackagePickupsApi#schedulePickup");
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
| **schedulePickupRequestBody** | [**SchedulePickupRequestBody**](SchedulePickupRequestBody.md)|  | |

### Return type

[**SchedulePickupResponseBody**](SchedulePickupResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

