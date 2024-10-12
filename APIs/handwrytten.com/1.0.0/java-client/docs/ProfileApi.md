# ProfileApi

All URIs are relative to *https://api.handwrytten.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updateUserAddress**](ProfileApi.md#updateUserAddress) | **POST** /profile/updateAddress | update the user&#39;s return address information |
| [**userAddress**](ProfileApi.md#userAddress) | **POST** /profile/address | gets the user&#39;s return address information |


<a id="updateUserAddress"></a>
# **updateUserAddress**
> UserAddress200Response updateUserAddress(body)

update the user&#39;s return address information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    UpdateUserAddressRequest body = new UpdateUserAddressRequest(); // UpdateUserAddressRequest | additional parameters
    try {
      UserAddress200Response result = apiInstance.updateUserAddress(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#updateUserAddress");
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
| **body** | [**UpdateUserAddressRequest**](UpdateUserAddressRequest.md)| additional parameters | |

### Return type

[**UserAddress200Response**](UserAddress200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="userAddress"></a>
# **userAddress**
> UserAddress200Response userAddress(body)

gets the user&#39;s return address information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    UserAddressRequest body = new UserAddressRequest(); // UserAddressRequest | additional parameters
    try {
      UserAddress200Response result = apiInstance.userAddress(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#userAddress");
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
| **body** | [**UserAddressRequest**](UserAddressRequest.md)| additional parameters | [optional] |

### Return type

[**UserAddress200Response**](UserAddress200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

