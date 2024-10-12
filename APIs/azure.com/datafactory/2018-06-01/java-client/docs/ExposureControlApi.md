# ExposureControlApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**exposureControlGetFeatureValue**](ExposureControlApi.md#exposureControlGetFeatureValue) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DataFactory/locations/{locationId}/getFeatureValue |  |
| [**exposureControlGetFeatureValueByFactory**](ExposureControlApi.md#exposureControlGetFeatureValueByFactory) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/getFeatureValue |  |


<a id="exposureControlGetFeatureValue"></a>
# **exposureControlGetFeatureValue**
> ExposureControlResponse exposureControlGetFeatureValue(subscriptionId, locationId, apiVersion, exposureControlRequest)



Get exposure control feature for specific location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExposureControlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExposureControlApi apiInstance = new ExposureControlApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String locationId = "locationId_example"; // String | The location identifier.
    String apiVersion = "apiVersion_example"; // String | The API version.
    ExposureControlRequest exposureControlRequest = new ExposureControlRequest(); // ExposureControlRequest | The exposure control request.
    try {
      ExposureControlResponse result = apiInstance.exposureControlGetFeatureValue(subscriptionId, locationId, apiVersion, exposureControlRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExposureControlApi#exposureControlGetFeatureValue");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **locationId** | **String**| The location identifier. | |
| **apiVersion** | **String**| The API version. | |
| **exposureControlRequest** | [**ExposureControlRequest**](ExposureControlRequest.md)| The exposure control request. | |

### Return type

[**ExposureControlResponse**](ExposureControlResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="exposureControlGetFeatureValueByFactory"></a>
# **exposureControlGetFeatureValueByFactory**
> ExposureControlResponse exposureControlGetFeatureValueByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion, exposureControlRequest)



Get exposure control feature for specific factory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExposureControlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExposureControlApi apiInstance = new ExposureControlApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    ExposureControlRequest exposureControlRequest = new ExposureControlRequest(); // ExposureControlRequest | The exposure control request.
    try {
      ExposureControlResponse result = apiInstance.exposureControlGetFeatureValueByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion, exposureControlRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExposureControlApi#exposureControlGetFeatureValueByFactory");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **apiVersion** | **String**| The API version. | |
| **exposureControlRequest** | [**ExposureControlRequest**](ExposureControlRequest.md)| The exposure control request. | |

### Return type

[**ExposureControlResponse**](ExposureControlResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

