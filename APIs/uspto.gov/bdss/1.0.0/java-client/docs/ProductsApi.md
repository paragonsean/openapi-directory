# ProductsApi

All URIs are relative to *http://localhost/BDSS-API*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLatestProductFilesByProductIdAndTime**](ProductsApi.md#getLatestProductFilesByProductIdAndTime) | **GET** /products/{shortName}/latest | Returns products along with their latest files by short names. |
| [**getPopulartProducts**](ProductsApi.md#getPopulartProducts) | **GET** /products/popular | Returns popular products along with latest files. |
| [**getProductSubTree**](ProductsApi.md#getProductSubTree) | **GET** /products/tree/{shortName} | Returns products&#39; hierarchical subtree. |
| [**getProductsByName**](ProductsApi.md#getProductsByName) | **GET** /products/byname/{productName} | Returns files associated with products (of level PRODUCT) based on their full or partial names. |
| [**getProductsByShortName**](ProductsApi.md#getProductsByShortName) | **GET** /products/{shortName} | Returns products along with their associated files by short names. |
| [**getProductsTree**](ProductsApi.md#getProductsTree) | **GET** /products/tree | Returns products&#39; hierarchical tree. |
| [**getProductsWithLatestProductFiles**](ProductsApi.md#getProductsWithLatestProductFiles) | **GET** /products/all/latest | Returns all products with Latest Files. |


<a id="getLatestProductFilesByProductIdAndTime"></a>
# **getLatestProductFilesByProductIdAndTime**
> getLatestProductFilesByProductIdAndTime(shortName, year, hierarchy)

Returns products along with their latest files by short names.

Use this GET to search for latest released bulk data products by their short names and release year. The return response will include the latest files within the year specified.  An error message will be returned if product(s) cannot be found for the year specified

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/BDSS-API");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String shortName = "shortName_example"; // String | Short name of the product, for example, \"PTGRSP\"
    Integer year = 56; // Integer | Year of the product files  needed, for example, 2001.
    String hierarchy = "false"; // String | Boolean flag (possible values: true and false) to indicate if product hierarchy needs to be return in the response. By default it doesn't return the hierarchy in the response.
    try {
      apiInstance.getLatestProductFilesByProductIdAndTime(shortName, year, hierarchy);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getLatestProductFilesByProductIdAndTime");
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
| **shortName** | **String**| Short name of the product, for example, \&quot;PTGRSP\&quot; | |
| **year** | **Integer**| Year of the product files  needed, for example, 2001. | [optional] |
| **hierarchy** | **String**| Boolean flag (possible values: true and false) to indicate if product hierarchy needs to be return in the response. By default it doesn&#39;t return the hierarchy in the response. | [optional] [default to false] |

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
| **200** | Successful operation. |  -  |
| **404** | Product not found. |  -  |
| **500** | Internal server error. |  -  |

<a id="getPopulartProducts"></a>
# **getPopulartProducts**
> getPopulartProducts()

Returns popular products along with latest files.

Use this GET to retrieve these bulk data files by their popularity. The response includes product fields such as title, description, frequency, and level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/BDSS-API");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    try {
      apiInstance.getPopulartProducts();
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getPopulartProducts");
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
| **200** | Successful operation. |  -  |
| **404** | Unexpected error accessing metadata. |  -  |
| **500** | Internal server error. |  -  |

<a id="getProductSubTree"></a>
# **getProductSubTree**
> getProductSubTree(shortName)

Returns products&#39; hierarchical subtree.

Use this GET to search for bulk data products by their short names. This works almost like products/tree GET, the difference is that it returns subtree data starting from a particular tree node (i.e. the GET returns all children if parent short name is entered). If a product cannot be found by its short name (has to be exact match and is not case sensitive), then an error message will appear in response body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/BDSS-API");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String shortName = "shortName_example"; // String | Short name of the product, for example, \"PTISSD\"
    try {
      apiInstance.getProductSubTree(shortName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProductSubTree");
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
| **shortName** | **String**| Short name of the product, for example, \&quot;PTISSD\&quot; | |

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
| **200** | Successful operation. |  -  |
| **404** | Product not found. |  -  |
| **500** | Internal server error. |  -  |

<a id="getProductsByName"></a>
# **getProductsByName**
> getProductsByName(productName, fromYear, toYear, fromMonth, toMonth, fromDay, toDay, hierarchy, maxFiles)

Returns files associated with products (of level PRODUCT) based on their full or partial names.

Use this GET to search for bulk data services by product name or description. An error message will be returned if the product cannot be found by name. Note that product name is not case sensitive. You can enter full or partial name of an existing product to receive bulk data services. Default values for field names are as follows - if both years are not defined, toYear will be set equal to current year, fromYear will be set equal to previous year - if fromYear is defined, toYear will be set equal to fromYear+1 - if fromMonth not defined, current month will be used - if toMonth not defined, it will be set equal to fromMonth - if fromDay is not defined, it will be set equal to current day (today) - if toDay is not defined, it will be set to the last day of toMonth/toYear

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/BDSS-API");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String productName = "productName_example"; // String | Name of the product, for example, \"Trademark\"
    Integer fromYear = 56; // Integer | Year from when the product files are needed, for example, 1999.
    Integer toYear = 56; // Integer | Year until when the product files are needed, for example, 2000.
    Integer fromMonth = 56; // Integer | Month from when the product files are needed, for example, 01.
    Integer toMonth = 56; // Integer | Month until when the product files are needed, for example, 12.
    Integer fromDay = 56; // Integer | Day from when the product files are needed, for example, 01.
    Integer toDay = 56; // Integer | Day until when the product files are needed, for example, 31.
    String hierarchy = "false"; // String | Boolean flag to indicate if product hierarchy needs to be return in the response. By default it doesn't return the hierarchy in the response.
    Integer maxFiles = 20; // Integer | Max. number of files to retrieve, per product. Set value to -1 to get all files
    try {
      apiInstance.getProductsByName(productName, fromYear, toYear, fromMonth, toMonth, fromDay, toDay, hierarchy, maxFiles);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProductsByName");
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
| **productName** | **String**| Name of the product, for example, \&quot;Trademark\&quot; | |
| **fromYear** | **Integer**| Year from when the product files are needed, for example, 1999. | [optional] |
| **toYear** | **Integer**| Year until when the product files are needed, for example, 2000. | [optional] |
| **fromMonth** | **Integer**| Month from when the product files are needed, for example, 01. | [optional] |
| **toMonth** | **Integer**| Month until when the product files are needed, for example, 12. | [optional] |
| **fromDay** | **Integer**| Day from when the product files are needed, for example, 01. | [optional] |
| **toDay** | **Integer**| Day until when the product files are needed, for example, 31. | [optional] |
| **hierarchy** | **String**| Boolean flag to indicate if product hierarchy needs to be return in the response. By default it doesn&#39;t return the hierarchy in the response. | [optional] [default to false] |
| **maxFiles** | **Integer**| Max. number of files to retrieve, per product. Set value to -1 to get all files | [optional] [default to 20] |

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
| **200** | Successful operation. |  -  |
| **404** | Unexpected error accessing metadata. |  -  |
| **500** | Internal server error. |  -  |

<a id="getProductsByShortName"></a>
# **getProductsByShortName**
> getProductsByShortName(shortName, fromYear, toYear, fromMonth, toMonth, fromDay, toDay, fromDate, toDate, hierarchy)

Returns products along with their associated files by short names.

Use this GET to search for bulk data products by their short names and description. Note that \&quot;From\&quot; and \&quot;To\&quot; dates can be inputted separately as year/month/day values or as a single date string in format \&quot;YYYY-MM-DD\&quot;. If all values are entered, single date strings have a higher priority For the list of default values rules, see GET /products/byname/{productName} above

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/BDSS-API");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String shortName = "shortName_example"; // String | Short name  of the product, for example, \"PTGRSP\"
    Integer fromYear = 56; // Integer | Year from when the product files are needed, for example, 1999.
    Integer toYear = 56; // Integer | Year until when the product files are needed, for example, 2000.
    Integer fromMonth = 56; // Integer | Month from when the product files are needed, for example, 01.
    Integer toMonth = 56; // Integer | Month until when the product files are needed, for example, 12.
    Integer fromDay = 56; // Integer | Day from when the product files are needed, for example, 01.
    Integer toDay = 56; // Integer | Day until when the product files are needed, for example, 31.
    String fromDate = "fromDate_example"; // String | Year from when the product files are needed, for example, 1999-01-01.
    String toDate = "toDate_example"; // String | Year until when the product files are needed, for example, 2001-12-31.
    String hierarchy = "false"; // String | Boolean flag (possible values: true and false) to indicate if product hierarchy needs to be return in the response. By default it doesn't return the hierarchy in the response.
    try {
      apiInstance.getProductsByShortName(shortName, fromYear, toYear, fromMonth, toMonth, fromDay, toDay, fromDate, toDate, hierarchy);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProductsByShortName");
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
| **shortName** | **String**| Short name  of the product, for example, \&quot;PTGRSP\&quot; | |
| **fromYear** | **Integer**| Year from when the product files are needed, for example, 1999. | [optional] |
| **toYear** | **Integer**| Year until when the product files are needed, for example, 2000. | [optional] |
| **fromMonth** | **Integer**| Month from when the product files are needed, for example, 01. | [optional] |
| **toMonth** | **Integer**| Month until when the product files are needed, for example, 12. | [optional] |
| **fromDay** | **Integer**| Day from when the product files are needed, for example, 01. | [optional] |
| **toDay** | **Integer**| Day until when the product files are needed, for example, 31. | [optional] |
| **fromDate** | **String**| Year from when the product files are needed, for example, 1999-01-01. | [optional] |
| **toDate** | **String**| Year until when the product files are needed, for example, 2001-12-31. | [optional] |
| **hierarchy** | **String**| Boolean flag (possible values: true and false) to indicate if product hierarchy needs to be return in the response. By default it doesn&#39;t return the hierarchy in the response. | [optional] [default to false] |

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
| **200** | Successful operation. |  -  |
| **404** | Product not found. |  -  |
| **500** | Internal server error. |  -  |

<a id="getProductsTree"></a>
# **getProductsTree**
> getProductsTree()

Returns products&#39; hierarchical tree.

Use this GET to retrieve short name and parent/child relationships for bulk data products. Short names are unique IDs of the products and should be used in other GETs where {shortName} parameter is required Use this GET to perform initial exploration of the existing products hierarchy Short names are unique IDs of the products and should be used in other GETs where {shortName} parameter is required

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/BDSS-API");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    try {
      apiInstance.getProductsTree();
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProductsTree");
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
| **200** | Successful operation. |  -  |
| **404** | Unexpected error accessing metadata. |  -  |
| **500** | Internal server error. |  -  |

<a id="getProductsWithLatestProductFiles"></a>
# **getProductsWithLatestProductFiles**
> getProductsWithLatestProductFiles()

Returns all products with Latest Files.

Use this GET to retrieve latest released bulk data products. Note that there is one file per product. The response includes product fields such as title, description, frequency, and level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/BDSS-API");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    try {
      apiInstance.getProductsWithLatestProductFiles();
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProductsWithLatestProductFiles");
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
| **200** | Successful operation. |  -  |
| **404** | Unexpected error accessing metadata. |  -  |
| **500** | Internal server error. |  -  |

