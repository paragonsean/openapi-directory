# FeatureApi

All URIs are relative to *https://apps.gov.bc.ca/pub/bcgnws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**featuresFeatureIdGet**](FeatureApi.md#featuresFeatureIdGet) | **GET** /features/{featureId} | Get a feature by its featureId |


<a id="featuresFeatureIdGet"></a>
# **featuresFeatureIdGet**
> featuresFeatureIdGet(featureId)

Get a feature by its featureId

Get information about the geographical feature with the specified featureId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeatureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.gov.bc.ca/pub/bcgnws");

    FeatureApi apiInstance = new FeatureApi(defaultClient);
    Integer featureId = 8879; // Integer | The unique identifier for a feature
    try {
      apiInstance.featuresFeatureIdGet(featureId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeatureApi#featuresFeatureIdGet");
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
| **featureId** | **Integer**| The unique identifier for a feature | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the feature with the specified featureId (XML format only) |  -  |
| **404** | The feature with the given featureId doesn&#39;t exist |  -  |

