# HmdaApi

All URIs are relative to *https://api.consumerfinance.gov:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getConceptHmda**](HmdaApi.md#getConceptHmda) | **GET** /data/hmda/concept/{concept} | Get information about a particular concept in this dataset. |
| [**getDatasetHmda**](HmdaApi.md#getDatasetHmda) | **GET** /data/hmda | Get metadata for this dataset. |
| [**getSliceMetadataHmda**](HmdaApi.md#getSliceMetadataHmda) | **GET** /data/hmda/slice/{slice}/metadata | Get the metadata for a slice in this dataset. |
| [**querySliceHmda**](HmdaApi.md#querySliceHmda) | **GET** /data/hmda/slice/{slice} | Query a slice in this dataset. |


<a id="getConceptHmda"></a>
# **getConceptHmda**
> getConceptHmda(concept)

Get information about a particular concept in this dataset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HmdaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.consumerfinance.gov:443");

    HmdaApi apiInstance = new HmdaApi(defaultClient);
    String concept = "concept_example"; // String | Name of concept
    try {
      apiInstance.getConceptHmda(concept);
    } catch (ApiException e) {
      System.err.println("Exception when calling HmdaApi#getConceptHmda");
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
| **concept** | **String**| Name of concept | |

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

<a id="getDatasetHmda"></a>
# **getDatasetHmda**
> getDatasetHmda()

Get metadata for this dataset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HmdaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.consumerfinance.gov:443");

    HmdaApi apiInstance = new HmdaApi(defaultClient);
    try {
      apiInstance.getDatasetHmda();
    } catch (ApiException e) {
      System.err.println("Exception when calling HmdaApi#getDatasetHmda");
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

<a id="getSliceMetadataHmda"></a>
# **getSliceMetadataHmda**
> getSliceMetadataHmda(slice)

Get the metadata for a slice in this dataset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HmdaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.consumerfinance.gov:443");

    HmdaApi apiInstance = new HmdaApi(defaultClient);
    String slice = "slice_example"; // String | Name of slice
    try {
      apiInstance.getSliceMetadataHmda(slice);
    } catch (ApiException e) {
      System.err.println("Exception when calling HmdaApi#getSliceMetadataHmda");
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
| **slice** | **String**| Name of slice | |

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

<a id="querySliceHmda"></a>
# **querySliceHmda**
> QueryResponse querySliceHmda(slice, $select, $where, $group, $limit, $offset, $orderBy, $callback)

Query a slice in this dataset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HmdaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.consumerfinance.gov:443");

    HmdaApi apiInstance = new HmdaApi(defaultClient);
    String slice = "slice_example"; // String | Name of slice
    String $select = "$select_example"; // String | Fields to return, separated by commas.
    String $where = "$where_example"; // String | Conditions to search for in the slice, in SQL WHERE style.
    String $group = "$group_example"; // String | Fields to group by, summarizing the data, separated by commas.
    Integer $limit = 56; // Integer | Number of records to return, 100 by default. Enter 0 for no limit.
    Integer $offset = 56; // Integer | Number of records to skip.
    String $orderBy = "$orderBy_example"; // String | Fields to order by, separated by commas. ASC and DESC can be used to modify the order.
    String $callback = "$callback_example"; // String | JavaScript callback to invoke. Only useful with JSONP requests.
    try {
      QueryResponse result = apiInstance.querySliceHmda(slice, $select, $where, $group, $limit, $offset, $orderBy, $callback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HmdaApi#querySliceHmda");
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
| **slice** | **String**| Name of slice | |
| **$select** | **String**| Fields to return, separated by commas. | [optional] |
| **$where** | **String**| Conditions to search for in the slice, in SQL WHERE style. | [optional] |
| **$group** | **String**| Fields to group by, summarizing the data, separated by commas. | [optional] |
| **$limit** | **Integer**| Number of records to return, 100 by default. Enter 0 for no limit. | [optional] |
| **$offset** | **Integer**| Number of records to skip. | [optional] |
| **$orderBy** | **String**| Fields to order by, separated by commas. ASC and DESC can be used to modify the order. | [optional] |
| **$callback** | **String**| JavaScript callback to invoke. Only useful with JSONP requests. | [optional] |

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/javascript, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

