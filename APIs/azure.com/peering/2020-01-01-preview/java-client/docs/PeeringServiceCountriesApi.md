# PeeringServiceCountriesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**peeringServiceCountriesList**](PeeringServiceCountriesApi.md#peeringServiceCountriesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/peeringServiceCountries |  |


<a id="peeringServiceCountriesList"></a>
# **peeringServiceCountriesList**
> PeeringServiceCountryListResult peeringServiceCountriesList(subscriptionId, apiVersion)



Lists all of the available countries for peering service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringServiceCountriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringServiceCountriesApi apiInstance = new PeeringServiceCountriesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      PeeringServiceCountryListResult result = apiInstance.peeringServiceCountriesList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringServiceCountriesApi#peeringServiceCountriesList");
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
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |

### Return type

[**PeeringServiceCountryListResult**](PeeringServiceCountryListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation has failed. |  -  |

