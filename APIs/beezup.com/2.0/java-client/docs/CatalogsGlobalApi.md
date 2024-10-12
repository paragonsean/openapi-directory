# CatalogsGlobalApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogGetBeezUPColumns**](CatalogsGlobalApi.md#catalogGetBeezUPColumns) | **GET** /v2/user/catalogs/beezupColumns | Get the BeezUP columns |
| [**catalogIndex**](CatalogsGlobalApi.md#catalogIndex) | **GET** /v2/user/catalogs/ | Get the index of the catalog API |


<a id="catalogGetBeezUPColumns"></a>
# **catalogGetBeezUPColumns**
> List&lt;BeezUPColumnConfiguration&gt; catalogGetBeezUPColumns()

Get the BeezUP columns

Get the BeezUP columns, this columns are used for mapping during the manual catalog importation process.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsGlobalApi apiInstance = new CatalogsGlobalApi(defaultClient);
    try {
      List<BeezUPColumnConfiguration> result = apiInstance.catalogGetBeezUPColumns();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsGlobalApi#catalogGetBeezUPColumns");
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

[**List&lt;BeezUPColumnConfiguration&gt;**](BeezUPColumnConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The catalog API index |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="catalogIndex"></a>
# **catalogIndex**
> CatalogIndex catalogIndex()

Get the index of the catalog API

The operation will give you all the operations you will be able to do and all the LOV used in this API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsGlobalApi apiInstance = new CatalogsGlobalApi(defaultClient);
    try {
      CatalogIndex result = apiInstance.catalogIndex();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsGlobalApi#catalogIndex");
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

[**CatalogIndex**](CatalogIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Occurs when something goes wrong |  -  |

