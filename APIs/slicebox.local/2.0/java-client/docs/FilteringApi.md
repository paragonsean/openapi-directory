# FilteringApi

All URIs are relative to *http://slicebox.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**filteringAssociationsGet**](FilteringApi.md#filteringAssociationsGet) | **GET** /filtering/associations |  |
| [**filteringAssociationsIdDelete**](FilteringApi.md#filteringAssociationsIdDelete) | **DELETE** /filtering/associations/{id} |  |
| [**filteringAssociationsPost**](FilteringApi.md#filteringAssociationsPost) | **POST** /filtering/associations |  |
| [**filteringFiltersGet**](FilteringApi.md#filteringFiltersGet) | **GET** /filtering/filters |  |
| [**filteringFiltersIdDelete**](FilteringApi.md#filteringFiltersIdDelete) | **DELETE** /filtering/filters/{id} |  |
| [**filteringFiltersIdTagpathsGet**](FilteringApi.md#filteringFiltersIdTagpathsGet) | **GET** /filtering/filters/{id}/tagpaths |  |
| [**filteringFiltersIdTagpathsPost**](FilteringApi.md#filteringFiltersIdTagpathsPost) | **POST** /filtering/filters/{id}/tagpaths |  |
| [**filteringFiltersIdTagpathsTagpathidDelete**](FilteringApi.md#filteringFiltersIdTagpathsTagpathidDelete) | **DELETE** /filtering/filters/{id}/tagpaths/{tagpathid} |  |
| [**filteringFiltersPost**](FilteringApi.md#filteringFiltersPost) | **POST** /filtering/filters |  |


<a id="filteringAssociationsGet"></a>
# **filteringAssociationsGet**
> List&lt;SourceTagFilter&gt; filteringAssociationsGet(startindex, count)



Get a list of source to filter associations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilteringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    FilteringApi apiInstance = new FilteringApi(defaultClient);
    Long startindex = 0L; // Long | start index of returned slice of source <-> filter associations
    Long count = 20L; // Long | size of returned slice of source <-> filter associations
    try {
      List<SourceTagFilter> result = apiInstance.filteringAssociationsGet(startindex, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilteringApi#filteringAssociationsGet");
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
| **startindex** | **Long**| start index of returned slice of source &lt;-&gt; filter associations | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of source &lt;-&gt; filter associations | [optional] [default to 20] |

### Return type

[**List&lt;SourceTagFilter&gt;**](SourceTagFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of source &lt;-&gt; filter associations |  -  |

<a id="filteringAssociationsIdDelete"></a>
# **filteringAssociationsIdDelete**
> filteringAssociationsIdDelete(id)



remove the source &lt;-&gt; filter association corresponding to the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilteringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    FilteringApi apiInstance = new FilteringApi(defaultClient);
    Long id = 56L; // Long | id of source <-> filter association to remove
    try {
      apiInstance.filteringAssociationsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilteringApi#filteringAssociationsIdDelete");
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
| **id** | **Long**| id of source &lt;-&gt; filter association to remove | |

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
| **204** | source &lt;-&gt; filter association removed |  -  |

<a id="filteringAssociationsPost"></a>
# **filteringAssociationsPost**
> filteringAssociationsPost(sourcetagfilter)



Inserts or updates a source &lt;-&gt; filter associations. If the specified Source already  has an association this is updated, otherwise a new is inserted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilteringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    FilteringApi apiInstance = new FilteringApi(defaultClient);
    SourceTagFilter sourcetagfilter = new SourceTagFilter(); // SourceTagFilter | Source to Filter association
    try {
      apiInstance.filteringAssociationsPost(sourcetagfilter);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilteringApi#filteringAssociationsPost");
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
| **sourcetagfilter** | [**SourceTagFilter**](SourceTagFilter.md)| Source to Filter association | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Upserted source &lt;-&gt; filter association |  -  |

<a id="filteringFiltersGet"></a>
# **filteringFiltersGet**
> List&lt;Filter&gt; filteringFiltersGet(startindex, count)



List defined filters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilteringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    FilteringApi apiInstance = new FilteringApi(defaultClient);
    Long startindex = 0L; // Long | start index of returned slice of filters
    Long count = 20L; // Long | size of returned slice of filters
    try {
      List<Filter> result = apiInstance.filteringFiltersGet(startindex, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilteringApi#filteringFiltersGet");
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
| **startindex** | **Long**| start index of returned slice of filters | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of filters | [optional] [default to 20] |

### Return type

[**List&lt;Filter&gt;**](Filter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of filters |  -  |

<a id="filteringFiltersIdDelete"></a>
# **filteringFiltersIdDelete**
> filteringFiltersIdDelete(id)



remove the filter corresponding to the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilteringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    FilteringApi apiInstance = new FilteringApi(defaultClient);
    Long id = 56L; // Long | id of filter to remove
    try {
      apiInstance.filteringFiltersIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilteringApi#filteringFiltersIdDelete");
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
| **id** | **Long**| id of filter to remove | |

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
| **204** | Filter removed |  -  |

<a id="filteringFiltersIdTagpathsGet"></a>
# **filteringFiltersIdTagpathsGet**
> List&lt;TagPathTag&gt; filteringFiltersIdTagpathsGet(id)



List tagpaths for the selected filter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilteringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    FilteringApi apiInstance = new FilteringApi(defaultClient);
    Long id = 56L; // Long | id of filter
    try {
      List<TagPathTag> result = apiInstance.filteringFiltersIdTagpathsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilteringApi#filteringFiltersIdTagpathsGet");
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
| **id** | **Long**| id of filter | |

### Return type

[**List&lt;TagPathTag&gt;**](TagPathTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of tagpaths |  -  |

<a id="filteringFiltersIdTagpathsPost"></a>
# **filteringFiltersIdTagpathsPost**
> filteringFiltersIdTagpathsPost(id, tagpath)



add a tagpath to a filter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilteringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    FilteringApi apiInstance = new FilteringApi(defaultClient);
    Long id = 56L; // Long | id of filter to remove
    TagPathTag tagpath = new TagPathTag(); // TagPathTag | id of filter to remove
    try {
      apiInstance.filteringFiltersIdTagpathsPost(id, tagpath);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilteringApi#filteringFiltersIdTagpathsPost");
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
| **id** | **Long**| id of filter to remove | |
| **tagpath** | [**TagPathTag**](TagPathTag.md)| id of filter to remove | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TagPath added |  -  |

<a id="filteringFiltersIdTagpathsTagpathidDelete"></a>
# **filteringFiltersIdTagpathsTagpathidDelete**
> filteringFiltersIdTagpathsTagpathidDelete(id, tagpathid)



remove the tagpath corresponding to the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilteringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    FilteringApi apiInstance = new FilteringApi(defaultClient);
    Long id = 56L; // Long | id of filter
    Long tagpathid = 56L; // Long | id of TagPath to remove
    try {
      apiInstance.filteringFiltersIdTagpathsTagpathidDelete(id, tagpathid);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilteringApi#filteringFiltersIdTagpathsTagpathidDelete");
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
| **id** | **Long**| id of filter | |
| **tagpathid** | **Long**| id of TagPath to remove | |

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
| **204** | TagPath removed |  -  |

<a id="filteringFiltersPost"></a>
# **filteringFiltersPost**
> filteringFiltersPost(tagFilter)



Inserts or updates a filter. If a filter with same name as supplied filter exists this filter is updated, otherwise a new filter is inserted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilteringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    FilteringApi apiInstance = new FilteringApi(defaultClient);
    Filter tagFilter = new Filter(); // Filter | Filter
    try {
      apiInstance.filteringFiltersPost(tagFilter);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilteringApi#filteringFiltersPost");
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
| **tagFilter** | [**Filter**](Filter.md)| Filter | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Filter upserted |  -  |

