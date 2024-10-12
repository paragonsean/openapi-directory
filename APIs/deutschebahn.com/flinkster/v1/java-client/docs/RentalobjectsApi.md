# RentalobjectsApi

All URIs are relative to *https://api.deutschebahn.com/flinkster-api-ng/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRentalObject**](RentalobjectsApi.md#getRentalObject) | **GET** /providernetworks/{providernetworkUID}/rentalobjects/{rentalObjectUID} | Get information about the RentalObject. |


<a id="getRentalObject"></a>
# **getRentalObject**
> RentalObjectJO getRentalObject(rentalObjectUID, providernetworkUID, expand)

Get information about the RentalObject.

Get information about the Rental Object. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RentalobjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/flinkster-api-ng/v1");

    RentalobjectsApi apiInstance = new RentalobjectsApi(defaultClient);
    String rentalObjectUID = "rentalObjectUID_example"; // String | 
    String providernetworkUID = "providernetworkUID_example"; // String | 
    String expand = "expand_example"; // String | 
    try {
      RentalObjectJO result = apiInstance.getRentalObject(rentalObjectUID, providernetworkUID, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RentalobjectsApi#getRentalObject");
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
| **rentalObjectUID** | **String**|  | |
| **providernetworkUID** | **String**|  | |
| **expand** | **String**|  | [optional] |

### Return type

[**RentalObjectJO**](RentalObjectJO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request One or more parameters have invalid values. |  -  |
| **403** | Forbidden Provider is not allowed to use this interface. |  -  |

