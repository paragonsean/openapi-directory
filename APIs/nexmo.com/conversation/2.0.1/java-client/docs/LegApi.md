# LegApi

All URIs are relative to *https://api.nexmo.com/v0.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteLeg**](LegApi.md#deleteLeg) | **DELETE** /legs/{leg_id} | Delete a leg |
| [**listLegs**](LegApi.md#listLegs) | **GET** /legs | List legs |


<a id="deleteLeg"></a>
# **deleteLeg**
> Object deleteLeg(legId)

Delete a leg

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.1");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    LegApi apiInstance = new LegApi(defaultClient);
    String legId = "legId_example"; // String | Leg ID
    try {
      Object result = apiInstance.deleteLeg(legId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegApi#deleteLeg");
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
| **legId** | **String**| Leg ID | |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success response with empty JSON |  -  |

<a id="listLegs"></a>
# **listLegs**
> ListLegs200Response listLegs()

List legs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.1");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    LegApi apiInstance = new LegApi(defaultClient);
    try {
      ListLegs200Response result = apiInstance.listLegs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegApi#listLegs");
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

[**ListLegs200Response**](ListLegs200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List Legs Successfully |  -  |

