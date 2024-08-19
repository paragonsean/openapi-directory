# SmartChargingApi

All URIs are relative to *http://api.edrv.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deletechargingschedule**](SmartChargingApi.md#deletechargingschedule) | **DELETE** /v1/commands/chargingschedule |  |
| [**setchargingschedule**](SmartChargingApi.md#setchargingschedule) | **POST** /v1/commands/chargingschedule |  |


<a id="deletechargingschedule"></a>
# **deletechargingschedule**
> Setchargingschedule201Response deletechargingschedule(deletechargingscheduleRequest)



Delete a smart charging schedule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmartChargingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SmartChargingApi apiInstance = new SmartChargingApi(defaultClient);
    DeletechargingscheduleRequest deletechargingscheduleRequest = new DeletechargingscheduleRequest(); // DeletechargingscheduleRequest | 
    try {
      Setchargingschedule201Response result = apiInstance.deletechargingschedule(deletechargingscheduleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmartChargingApi#deletechargingschedule");
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
| **deletechargingscheduleRequest** | [**DeletechargingscheduleRequest**](DeletechargingscheduleRequest.md)|  | |

### Return type

[**Setchargingschedule201Response**](Setchargingschedule201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A successful response |  -  |
| **400** | Schedule not found |  -  |

<a id="setchargingschedule"></a>
# **setchargingschedule**
> Setchargingschedule201Response setchargingschedule(setchargingscheduleRequest)



Set one of charging power or current of a specific chargestation connector

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmartChargingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SmartChargingApi apiInstance = new SmartChargingApi(defaultClient);
    SetchargingscheduleRequest setchargingscheduleRequest = new SetchargingscheduleRequest(); // SetchargingscheduleRequest | 
    try {
      Setchargingschedule201Response result = apiInstance.setchargingschedule(setchargingscheduleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmartChargingApi#setchargingschedule");
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
| **setchargingscheduleRequest** | [**SetchargingscheduleRequest**](SetchargingscheduleRequest.md)|  | |

### Return type

[**Setchargingschedule201Response**](Setchargingschedule201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A successful response |  -  |
| **400** | A failure response |  -  |

