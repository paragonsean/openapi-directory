# NamespacesApi

All URIs are relative to *https://hub.docker.com/api/publisher/analytics/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNamespaceDataByTimespan**](NamespacesApi.md#getNamespaceDataByTimespan) | **GET** /namespaces/{namespace}/pulls/exports/years/{year}/{timespantype}/{timespan}/{dataview} | Get namespace data for timespan |
| [**getNamespaceTimespanMetadata**](NamespacesApi.md#getNamespaceTimespanMetadata) | **GET** /namespaces/{namespace}/pulls/exports/years/{year}/{timespantype}/{timespan} | Get namespace metadata for timespan |
| [**getNamespaceTimespans**](NamespacesApi.md#getNamespaceTimespans) | **GET** /namespaces/{namespace}/pulls/exports/years/{year}/{timespantype} | Get timespans with data |
| [**getNamespaceYears**](NamespacesApi.md#getNamespaceYears) | **GET** /namespaces/{namespace}/pulls/exports/years | Get years with data |


<a id="getNamespaceDataByTimespan"></a>
# **getNamespaceDataByTimespan**
> ResponseData getNamespaceDataByTimespan(namespace, year, timespantype, timespan, dataview)

Get namespace data for timespan

Gets a list of URLs that can be used to download the pull data for the given namespace and timespan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com/api/publisher/analytics/v1");
    
    // Configure HTTP bearer authorization: HubAuth
    HttpBearerAuth HubAuth = (HttpBearerAuth) defaultClient.getAuthentication("HubAuth");
    HubAuth.setBearerToken("BEARER TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String namespace = "namespace_example"; // String | Namespace to fetch data for
    Integer year = 56; // Integer | Year to fetch data for
    TimespanType timespantype = TimespanType.fromValue("months"); // TimespanType | Type of timespan to fetch data for
    Integer timespan = 56; // Integer | Timespan to fetch data for
    DataviewType dataview = DataviewType.fromValue("raw"); // DataviewType | Type of data to fetch
    try {
      ResponseData result = apiInstance.getNamespaceDataByTimespan(namespace, year, timespantype, timespan, dataview);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#getNamespaceDataByTimespan");
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
| **namespace** | **String**| Namespace to fetch data for | |
| **year** | **Integer**| Year to fetch data for | |
| **timespantype** | [**TimespanType**](.md)| Type of timespan to fetch data for | [enum: months, weeks] |
| **timespan** | **Integer**| Timespan to fetch data for | |
| **dataview** | [**DataviewType**](.md)| Type of data to fetch | [enum: raw, summary, repo-summary] |

### Return type

[**ResponseData**](ResponseData.md)

### Authorization

[HubAuth](../README.md#HubAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getNamespaceTimespanMetadata"></a>
# **getNamespaceTimespanMetadata**
> TimespanModel getNamespaceTimespanMetadata(namespace, year, timespantype, timespan)

Get namespace metadata for timespan

Gets info about data for the given namespace and timespan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com/api/publisher/analytics/v1");
    
    // Configure HTTP bearer authorization: HubAuth
    HttpBearerAuth HubAuth = (HttpBearerAuth) defaultClient.getAuthentication("HubAuth");
    HubAuth.setBearerToken("BEARER TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String namespace = "namespace_example"; // String | Namespace to fetch data for
    Integer year = 56; // Integer | Year to fetch data for
    TimespanType timespantype = TimespanType.fromValue("months"); // TimespanType | Type of timespan to fetch data for
    Integer timespan = 56; // Integer | Timespan to fetch data for
    try {
      TimespanModel result = apiInstance.getNamespaceTimespanMetadata(namespace, year, timespantype, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#getNamespaceTimespanMetadata");
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
| **namespace** | **String**| Namespace to fetch data for | |
| **year** | **Integer**| Year to fetch data for | |
| **timespantype** | [**TimespanType**](.md)| Type of timespan to fetch data for | [enum: months, weeks] |
| **timespan** | **Integer**| Timespan to fetch data for | |

### Return type

[**TimespanModel**](TimespanModel.md)

### Authorization

[HubAuth](../README.md#HubAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="getNamespaceTimespans"></a>
# **getNamespaceTimespans**
> TimespanData getNamespaceTimespans(namespace, year, timespantype)

Get timespans with data

Gets a list of timespans of the given type that have data for the given namespace and year

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com/api/publisher/analytics/v1");
    
    // Configure HTTP bearer authorization: HubAuth
    HttpBearerAuth HubAuth = (HttpBearerAuth) defaultClient.getAuthentication("HubAuth");
    HubAuth.setBearerToken("BEARER TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String namespace = "namespace_example"; // String | Namespace to fetch data for
    Integer year = 56; // Integer | Year to fetch data for
    TimespanType timespantype = TimespanType.fromValue("months"); // TimespanType | Type of timespan to fetch data for
    try {
      TimespanData result = apiInstance.getNamespaceTimespans(namespace, year, timespantype);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#getNamespaceTimespans");
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
| **namespace** | **String**| Namespace to fetch data for | |
| **year** | **Integer**| Year to fetch data for | |
| **timespantype** | [**TimespanType**](.md)| Type of timespan to fetch data for | [enum: months, weeks] |

### Return type

[**TimespanData**](TimespanData.md)

### Authorization

[HubAuth](../README.md#HubAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getNamespaceYears"></a>
# **getNamespaceYears**
> YearData getNamespaceYears(namespace)

Get years with data

Gets a list of years that have data for the given namespace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com/api/publisher/analytics/v1");
    
    // Configure HTTP bearer authorization: HubAuth
    HttpBearerAuth HubAuth = (HttpBearerAuth) defaultClient.getAuthentication("HubAuth");
    HubAuth.setBearerToken("BEARER TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String namespace = "namespace_example"; // String | Namespace to fetch data for
    try {
      YearData result = apiInstance.getNamespaceYears(namespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#getNamespaceYears");
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
| **namespace** | **String**| Namespace to fetch data for | |

### Return type

[**YearData**](YearData.md)

### Authorization

[HubAuth](../README.md#HubAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

