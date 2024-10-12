# AuthorizationApiApi

All URIs are relative to *https://betaapi.digitallocker.gov.in/public*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceCodeId**](AuthorizationApiApi.md#getDeviceCodeId) | **POST** /oauth2/1/code | Get Device Code |


<a id="getDeviceCodeId"></a>
# **getDeviceCodeId**
> DeviceAuthorizationCodeResponse getDeviceCodeId(deviceAuthorizationCode)

Get Device Code

The client device calls the DigiLocker API to get the device code by providing the client_id issued to the device OEM and either the username or the mobile number of the user. DigiLocker responds with a device code and then sends an OTP on the mobile number and email address associated with the user’s account. The masked mobile number and email address is also sent in response. The device should use these values to notify the users about the mobile and email address on which the OTP has been sent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure OAuth2 access token for authorization: oauthsecurity
    OAuth oauthsecurity = (OAuth) defaultClient.getAuthentication("oauthsecurity");
    oauthsecurity.setAccessToken("YOUR ACCESS TOKEN");

    AuthorizationApiApi apiInstance = new AuthorizationApiApi(defaultClient);
    DeviceAuthorizationCode deviceAuthorizationCode = new DeviceAuthorizationCode(); // DeviceAuthorizationCode | 
    try {
      DeviceAuthorizationCodeResponse result = apiInstance.getDeviceCodeId(deviceAuthorizationCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationApiApi#getDeviceCodeId");
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
| **deviceAuthorizationCode** | [**DeviceAuthorizationCode**](DeviceAuthorizationCode.md)|  | [optional] |

### Return type

[**DeviceAuthorizationCodeResponse**](DeviceAuthorizationCodeResponse.md)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad Request |  -  |
| **401** | The client_id parameter is invalid. |  -  |
| **500** | Internal Error |  -  |

