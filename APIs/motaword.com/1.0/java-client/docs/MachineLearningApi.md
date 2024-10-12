# MachineLearningApi

All URIs are relative to *https://api.motaword.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeliveryPrediction**](MachineLearningApi.md#getDeliveryPrediction) | **POST** /ml/delivery-prediction | Get a delivery prediction for a project |


<a id="getDeliveryPrediction"></a>
# **getDeliveryPrediction**
> DeliveryPredictionResponse getDeliveryPrediction(deliveryPredictionPayload)

Get a delivery prediction for a project

Get a delivery prediction for a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MachineLearningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    MachineLearningApi apiInstance = new MachineLearningApi(defaultClient);
    DeliveryPredictionPayload deliveryPredictionPayload = new DeliveryPredictionPayload(); // DeliveryPredictionPayload | 
    try {
      DeliveryPredictionResponse result = apiInstance.getDeliveryPrediction(deliveryPredictionPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MachineLearningApi#getDeliveryPrediction");
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
| **deliveryPredictionPayload** | [**DeliveryPredictionPayload**](DeliveryPredictionPayload.md)|  | [optional] |

### Return type

[**DeliveryPredictionResponse**](DeliveryPredictionResponse.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Prediction and its probability |  -  |
| **400** | MissingParameter |  -  |
| **404** | ProjectNotFound |  -  |

