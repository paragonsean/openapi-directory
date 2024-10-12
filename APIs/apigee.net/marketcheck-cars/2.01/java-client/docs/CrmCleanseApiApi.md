# CrmCleanseApiApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**crmCheck**](CrmCleanseApiApi.md#crmCheck) | **GET** /crm_check/car/{vin} | CRM check of a particular vin |


<a id="crmCheck"></a>
# **crmCheck**
> CRMResponse crmCheck(vin, saleDate, apiKey)

CRM check of a particular vin

Check whether particular vin has had a listing after stipulated date or not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrmCleanseApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CrmCleanseApiApi apiInstance = new CrmCleanseApiApi(defaultClient);
    String vin = "vin_example"; // String | The VIN to identify the car. Must be a valid 17 char VIN
    String saleDate = "saleDate_example"; // String | sale date to check whether after this listing has appeared or not. Must be 8 character long, with YYYYMMDD format
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    try {
      CRMResponse result = apiInstance.crmCheck(vin, saleDate, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrmCleanseApiApi#crmCheck");
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
| **vin** | **String**| The VIN to identify the car. Must be a valid 17 char VIN | |
| **saleDate** | **String**| sale date to check whether after this listing has appeared or not. Must be 8 character long, with YYYYMMDD format | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |

### Return type

[**CRMResponse**](CRMResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CRM check for given vin |  -  |
| **0** | Error |  -  |

