# DataApi

All URIs are relative to *https://api.consumerfinance.gov:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDataset**](DataApi.md#getDataset) | **GET** /data/{dataset} | Get metadata about a dataset. |
| [**getDatasets**](DataApi.md#getDatasets) | **GET** /data | Get a list of all datasets. |


<a id="getDataset"></a>
# **getDataset**
> getDataset(dataset)

Get metadata about a dataset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.consumerfinance.gov:443");

    DataApi apiInstance = new DataApi(defaultClient);
    String dataset = "dataset_example"; // String | Name of dataset
    try {
      apiInstance.getDataset(dataset);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#getDataset");
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
| **dataset** | **String**| Name of dataset | |

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
| **200** | No response was specified |  -  |

<a id="getDatasets"></a>
# **getDatasets**
> getDatasets()

Get a list of all datasets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.consumerfinance.gov:443");

    DataApi apiInstance = new DataApi(defaultClient);
    try {
      apiInstance.getDatasets();
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApi#getDatasets");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

