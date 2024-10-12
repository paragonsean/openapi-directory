# ChargingLocationsApi

All URIs are relative to *https://api.test.enode.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteCharginglocationsCharginglocationid**](ChargingLocationsApi.md#deleteCharginglocationsCharginglocationid) | **DELETE** /charging-locations/{chargingLocationId} | Delete Charging Location |
| [**getCharginglocations**](ChargingLocationsApi.md#getCharginglocations) | **GET** /charging-locations | List Charging Locations |
| [**getCharginglocationsCharginglocationid**](ChargingLocationsApi.md#getCharginglocationsCharginglocationid) | **GET** /charging-locations/{chargingLocationId} | Get Charging Location |
| [**postCharginglocations**](ChargingLocationsApi.md#postCharginglocations) | **POST** /charging-locations | Create Charging Location |
| [**putCharginglocationsCharginglocationid**](ChargingLocationsApi.md#putCharginglocationsCharginglocationid) | **PUT** /charging-locations/{chargingLocationId} | Update Charging Location |


<a id="deleteCharginglocationsCharginglocationid"></a>
# **deleteCharginglocationsCharginglocationid**
> deleteCharginglocationsCharginglocationid(chargingLocationId)

Delete Charging Location

Delete a Charging Location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargingLocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    ChargingLocationsApi apiInstance = new ChargingLocationsApi(defaultClient);
    String chargingLocationId = "chargingLocationId_example"; // String | ID of the Charging Location
    try {
      apiInstance.deleteCharginglocationsCharginglocationid(chargingLocationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargingLocationsApi#deleteCharginglocationsCharginglocationid");
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
| **chargingLocationId** | **String**| ID of the Charging Location | |

### Return type

null (empty response body)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="getCharginglocations"></a>
# **getCharginglocations**
> List&lt;Object&gt; getCharginglocations()

List Charging Locations

Returns a list of Charging Locations registered to the User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargingLocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    ChargingLocationsApi apiInstance = new ChargingLocationsApi(defaultClient);
    try {
      List<Object> result = apiInstance.getCharginglocations();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargingLocationsApi#getCharginglocations");
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

**List&lt;Object&gt;**

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |

<a id="getCharginglocationsCharginglocationid"></a>
# **getCharginglocationsCharginglocationid**
> Object getCharginglocationsCharginglocationid(chargingLocationId)

Get Charging Location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargingLocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    ChargingLocationsApi apiInstance = new ChargingLocationsApi(defaultClient);
    String chargingLocationId = "chargingLocationId_example"; // String | ID of the Charging Location
    try {
      Object result = apiInstance.getCharginglocationsCharginglocationid(chargingLocationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargingLocationsApi#getCharginglocationsCharginglocationid");
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
| **chargingLocationId** | **String**| ID of the Charging Location | |

### Return type

**Object**

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |

<a id="postCharginglocations"></a>
# **postCharginglocations**
> Object postCharginglocations(postCharginglocationsRequest)

Create Charging Location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargingLocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    ChargingLocationsApi apiInstance = new ChargingLocationsApi(defaultClient);
    PostCharginglocationsRequest postCharginglocationsRequest = new PostCharginglocationsRequest(); // PostCharginglocationsRequest | 
    try {
      Object result = apiInstance.postCharginglocations(postCharginglocationsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargingLocationsApi#postCharginglocations");
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
| **postCharginglocationsRequest** | [**PostCharginglocationsRequest**](PostCharginglocationsRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="putCharginglocationsCharginglocationid"></a>
# **putCharginglocationsCharginglocationid**
> Object putCharginglocationsCharginglocationid(chargingLocationId, body)

Update Charging Location

Updates a charging location with new configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargingLocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    ChargingLocationsApi apiInstance = new ChargingLocationsApi(defaultClient);
    String chargingLocationId = "chargingLocationId_example"; // String | ID of the Charging Location
    Object body = null; // Object | 
    try {
      Object result = apiInstance.putCharginglocationsCharginglocationid(chargingLocationId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargingLocationsApi#putCharginglocationsCharginglocationid");
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
| **chargingLocationId** | **String**| ID of the Charging Location | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |

