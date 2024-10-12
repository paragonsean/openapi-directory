# ZoneApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**zoneGet**](ZoneApi.md#zoneGet) | **GET** /zone | get a list of zones |
| [**zonePost**](ZoneApi.md#zonePost) | **POST** /zone | create zone |
| [**zoneZoneKeyDelete**](ZoneApi.md#zoneZoneKeyDelete) | **DELETE** /zone/{zoneKey} | delete zone |
| [**zoneZoneKeyGet**](ZoneApi.md#zoneZoneKeyGet) | **GET** /zone/{zoneKey} | get zone |


<a id="zoneGet"></a>
# **zoneGet**
> MultiZoneResult zoneGet(filters)

get a list of zones

Get all zones. possibly with filters 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ZoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ZoneApi apiInstance = new ZoneApi(defaultClient);
    String filters = "filters_example"; // String | A JSON encoded array of ZoneFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ZoneFilter will be included. 
    try {
      MultiZoneResult result = apiInstance.zoneGet(filters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ZoneApi#zoneGet");
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
| **filters** | **String**| A JSON encoded array of ZoneFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ZoneFilter will be included.  | [optional] |

### Return type

[**MultiZoneResult**](MultiZoneResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A result containing an array of zones |  -  |
| **0** | Unexpected error |  -  |

<a id="zonePost"></a>
# **zonePost**
> ZoneResult zonePost(zone)

create zone

Create a new zone. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ZoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ZoneApi apiInstance = new ZoneApi(defaultClient);
    ZoneCreate zone = new ZoneCreate(); // ZoneCreate | the zone to create
    try {
      ZoneResult result = apiInstance.zonePost(zone);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ZoneApi#zonePost");
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
| **zone** | [**ZoneCreate**](ZoneCreate.md)| the zone to create | |

### Return type

[**ZoneResult**](ZoneResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A result containing the newly created zone |  -  |
| **0** | Unexpected error |  -  |

<a id="zoneZoneKeyDelete"></a>
# **zoneZoneKeyDelete**
> Object zoneZoneKeyDelete(zoneKey, checksum)

delete zone

Delete a zone. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ZoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ZoneApi apiInstance = new ZoneApi(defaultClient);
    String zoneKey = "9cd24183-f848-48f8-6f55-0f0724070000"; // String | the zone key
    String checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the zone to be deleted
    try {
      Object result = apiInstance.zoneZoneKeyDelete(zoneKey, checksum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ZoneApi#zoneZoneKeyDelete");
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
| **zoneKey** | **String**| the zone key | |
| **checksum** | **String**| the current checksum of the zone to be deleted | |

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | an empty result |  -  |
| **0** | Unexpected error |  -  |

<a id="zoneZoneKeyGet"></a>
# **zoneZoneKeyGet**
> ZoneResult zoneZoneKeyGet(zoneKey)

get zone

Get details for a single zone 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ZoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ZoneApi apiInstance = new ZoneApi(defaultClient);
    String zoneKey = "9cd24183-f848-48f8-6f55-0f0724070000"; // String | the zone key
    try {
      ZoneResult result = apiInstance.zoneZoneKeyGet(zoneKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ZoneApi#zoneZoneKeyGet");
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
| **zoneKey** | **String**| the zone key | |

### Return type

[**ZoneResult**](ZoneResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a result containing a single zone |  -  |
| **0** | Unexpected error |  -  |

