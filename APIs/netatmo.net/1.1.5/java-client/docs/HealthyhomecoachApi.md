# HealthyhomecoachApi

All URIs are relative to *https://api.netatmo.net/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gethomecoachsdata**](HealthyhomecoachApi.md#gethomecoachsdata) | **GET** /gethomecoachsdata |  |


<a id="gethomecoachsdata"></a>
# **gethomecoachsdata**
> NAHealthyHomeCoachDataResponse gethomecoachsdata(deviceId)



The method gethomecoachsdata Returns data from a user Healthy Home Coach Station (measures and device specific data).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthyhomecoachApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    HealthyhomecoachApi apiInstance = new HealthyhomecoachApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Id of the device you want to retrieve information of
    try {
      NAHealthyHomeCoachDataResponse result = apiInstance.gethomecoachsdata(deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthyhomecoachApi#gethomecoachsdata");
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
| **deviceId** | **String**| Id of the device you want to retrieve information of | [optional] |

### Return type

[**NAHealthyHomeCoachDataResponse**](NAHealthyHomeCoachDataResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

