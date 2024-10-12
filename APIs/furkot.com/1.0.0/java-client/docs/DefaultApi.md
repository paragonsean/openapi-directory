# DefaultApi

All URIs are relative to *https://trips.furkot.com/pub/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tripGet**](DefaultApi.md#tripGet) | **GET** /trip |  |
| [**tripTripIdStopGet**](DefaultApi.md#tripTripIdStopGet) | **GET** /trip/{trip_id}/stop |  |


<a id="tripGet"></a>
# **tripGet**
> List&lt;Trip&gt; tripGet()



list user&#39;s trips

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trips.furkot.com/pub/api");
    
    // Configure OAuth2 access token for authorization: furkot_auth_access_code
    OAuth furkot_auth_access_code = (OAuth) defaultClient.getAuthentication("furkot_auth_access_code");
    furkot_auth_access_code.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: furkot_auth_implicit
    OAuth furkot_auth_implicit = (OAuth) defaultClient.getAuthentication("furkot_auth_implicit");
    furkot_auth_implicit.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<Trip> result = apiInstance.tripGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tripGet");
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

[**List&lt;Trip&gt;**](Trip.md)

### Authorization

[furkot_auth_access_code](../README.md#furkot_auth_access_code), [furkot_auth_implicit](../README.md#furkot_auth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="tripTripIdStopGet"></a>
# **tripTripIdStopGet**
> List&lt;Step&gt; tripTripIdStopGet(tripId)



list stops for a trip identified by {trip_id}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trips.furkot.com/pub/api");
    
    // Configure OAuth2 access token for authorization: furkot_auth_access_code
    OAuth furkot_auth_access_code = (OAuth) defaultClient.getAuthentication("furkot_auth_access_code");
    furkot_auth_access_code.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: furkot_auth_implicit
    OAuth furkot_auth_implicit = (OAuth) defaultClient.getAuthentication("furkot_auth_implicit");
    furkot_auth_implicit.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String tripId = "tripId_example"; // String | id of the trip
    try {
      List<Step> result = apiInstance.tripTripIdStopGet(tripId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tripTripIdStopGet");
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
| **tripId** | **String**| id of the trip | |

### Return type

[**List&lt;Step&gt;**](Step.md)

### Authorization

[furkot_auth_access_code](../README.md#furkot_auth_access_code), [furkot_auth_implicit](../README.md#furkot_auth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

