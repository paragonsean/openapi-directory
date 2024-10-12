# FeatureApi

All URIs are relative to *https://tv.api.pressassociation.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFeature**](FeatureApi.md#getFeature) | **GET** /feature/{featureId} | Feature Detail |
| [**listFeatureTypes**](FeatureApi.md#listFeatureTypes) | **GET** /feature-type | Feature Type Collection |
| [**listFeatures**](FeatureApi.md#listFeatures) | **GET** /feature | Feature Collection |


<a id="getFeature"></a>
# **getFeature**
> Object getFeature(featureId)

Feature Detail

Return the content of the selected feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeatureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tv.api.pressassociation.io/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    FeatureApi apiInstance = new FeatureApi(defaultClient);
    String featureId = "featureId_example"; // String | The identifier for the selected feature.
    try {
      Object result = apiInstance.getFeature(featureId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeatureApi#getFeature");
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
| **featureId** | **String**| The identifier for the selected feature. | |

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="listFeatureTypes"></a>
# **listFeatureTypes**
> Object listFeatureTypes()

Feature Type Collection

Return a collection of Feature Types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeatureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tv.api.pressassociation.io/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    FeatureApi apiInstance = new FeatureApi(defaultClient);
    try {
      Object result = apiInstance.listFeatureTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeatureApi#listFeatureTypes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="listFeatures"></a>
# **listFeatures**
> Object listFeatures(type, date, start, end)

Feature Collection

Return a collection of Feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeatureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tv.api.pressassociation.io/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    FeatureApi apiInstance = new FeatureApi(defaultClient);
    String type = "netflix-monthly"; // String | The namespace of the feature type.
    String date = "2018-09-15"; // String | Date of the collection of feature items.
    String start = "2018-09-15"; // String | Start date for a range of features.
    String end = "2018-10-15"; // String | End date for a range of features.
    try {
      Object result = apiInstance.listFeatures(type, date, start, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeatureApi#listFeatures");
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
| **type** | **String**| The namespace of the feature type. | [optional] [default to netflix-monthly] |
| **date** | **String**| Date of the collection of feature items. | [optional] [default to 2018-09-15] |
| **start** | **String**| Start date for a range of features. | [optional] [default to 2018-09-15] |
| **end** | **String**| End date for a range of features. | [optional] [default to 2018-10-15] |

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

