# PayorsPrivateApi

All URIs are relative to *https://api.sandbox.velopayments.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPayorLinks**](PayorsPrivateApi.md#createPayorLinks) | **POST** /v1/payorLinks | Create a Payor Link |


<a id="createPayorLinks"></a>
# **createPayorLinks**
> createPayorLinks(createPayorLinkRequest)

Create a Payor Link

This endpoint allows you to create a payor link.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayorsPrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: oAuthVeloBackOffice
    OAuth oAuthVeloBackOffice = (OAuth) defaultClient.getAuthentication("oAuthVeloBackOffice");
    oAuthVeloBackOffice.setAccessToken("YOUR ACCESS TOKEN");

    PayorsPrivateApi apiInstance = new PayorsPrivateApi(defaultClient);
    CreatePayorLinkRequest createPayorLinkRequest = new CreatePayorLinkRequest(); // CreatePayorLinkRequest | Request to create a payor link
    try {
      apiInstance.createPayorLinks(createPayorLinkRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayorsPrivateApi#createPayorLinks");
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
| **createPayorLinkRequest** | [**CreatePayorLinkRequest**](CreatePayorLinkRequest.md)| Request to create a payor link | |

### Return type

null (empty response body)

### Authorization

[oAuthVeloBackOffice](../README.md#oAuthVeloBackOffice)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | HTTP Creeated |  * Location - URI to location of created resource <br>  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

