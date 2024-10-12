# RegisterForRealtimeApiApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**registerForRealtimeApiDelete**](RegisterForRealtimeApiApi.md#registerForRealtimeApiDelete) | **DELETE** /api/RegisterForRealtimeApi/{id} | Deletes a realtime API registration. |
| [**registerForRealtimeApiGet**](RegisterForRealtimeApiApi.md#registerForRealtimeApiGet) | **GET** /api/RegisterForRealtimeApi | Gets all registrations for the Realtime API. |
| [**registerForRealtimeApiPost**](RegisterForRealtimeApiApi.md#registerForRealtimeApiPost) | **POST** /api/RegisterForRealtimeApi | Creates a new registration for the realtime API. The Realtime API sends you the data of the registred devices as soon as we have them on the cloud.               More Information about the realtime API: https://www.smart-me.com/Description/api/realtimeapi.aspx |


<a id="registerForRealtimeApiDelete"></a>
# **registerForRealtimeApiDelete**
> registerForRealtimeApiDelete(id)

Deletes a realtime API registration.

Deletes a realtime API registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisterForRealtimeApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    RegisterForRealtimeApiApi apiInstance = new RegisterForRealtimeApiApi(defaultClient);
    String id = "id_example"; // String | The ID of the realtime API registration
    try {
      apiInstance.registerForRealtimeApiDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisterForRealtimeApiApi#registerForRealtimeApiDelete");
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
| **id** | **String**| The ID of the realtime API registration | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="registerForRealtimeApiGet"></a>
# **registerForRealtimeApiGet**
> List&lt;RegisterRealtimeApiData&gt; registerForRealtimeApiGet()

Gets all registrations for the Realtime API.

Gets all registrations for the Realtime API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisterForRealtimeApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    RegisterForRealtimeApiApi apiInstance = new RegisterForRealtimeApiApi(defaultClient);
    try {
      List<RegisterRealtimeApiData> result = apiInstance.registerForRealtimeApiGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisterForRealtimeApiApi#registerForRealtimeApiGet");
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

[**List&lt;RegisterRealtimeApiData&gt;**](RegisterRealtimeApiData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="registerForRealtimeApiPost"></a>
# **registerForRealtimeApiPost**
> registerForRealtimeApiPost(registerRealtimeApiData)

Creates a new registration for the realtime API. The Realtime API sends you the data of the registred devices as soon as we have them on the cloud.               More Information about the realtime API: https://www.smart-me.com/Description/api/realtimeapi.aspx

Creates a new registration for the realtime API. The Realtime API sends you the data of the registred devices as soon as we have them on the cloud. More Information about the realtime API: https://www.smart-me.com/Description/api/realtimeapi.aspx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisterForRealtimeApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    RegisterForRealtimeApiApi apiInstance = new RegisterForRealtimeApiApi(defaultClient);
    RegisterRealtimeApiData registerRealtimeApiData = new RegisterRealtimeApiData(); // RegisterRealtimeApiData | 
    try {
      apiInstance.registerForRealtimeApiPost(registerRealtimeApiData);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisterForRealtimeApiApi#registerForRealtimeApiPost");
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
| **registerRealtimeApiData** | [**RegisterRealtimeApiData**](RegisterRealtimeApiData.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

