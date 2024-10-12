# QueryApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queryImagesByPackage**](QueryApi.md#queryImagesByPackage) | **GET** /query/images/by_package | List of images containing given package |
| [**queryImagesByVulnerability**](QueryApi.md#queryImagesByVulnerability) | **GET** /query/images/by_vulnerability | List images vulnerable to the specific vulnerability ID. |
| [**queryVulnerabilities**](QueryApi.md#queryVulnerabilities) | **GET** /query/vulnerabilities | Listing information about given vulnerability |


<a id="queryImagesByPackage"></a>
# **queryImagesByPackage**
> PaginatedImageList queryImagesByPackage(name, packageType, version, page, limit, xAnchoreAccount)

List of images containing given package

Filterable query interface to search for images containing specified package

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    QueryApi apiInstance = new QueryApi(defaultClient);
    String name = "name_example"; // String | Name of package to search for (e.g. sed)
    String packageType = "packageType_example"; // String | Type of package to filter on (e.g. dpkg)
    String version = "version_example"; // String | Version of named package to filter on (e.g. 4.4-1)
    String page = "page_example"; // String | The page of results to fetch. Pages start at 1
    Integer limit = 56; // Integer | Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      PaginatedImageList result = apiInstance.queryImagesByPackage(name, packageType, version, page, limit, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#queryImagesByPackage");
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
| **name** | **String**| Name of package to search for (e.g. sed) | |
| **packageType** | **String**| Type of package to filter on (e.g. dpkg) | [optional] |
| **version** | **String**| Version of named package to filter on (e.g. 4.4-1) | [optional] |
| **page** | **String**| The page of results to fetch. Pages start at 1 | [optional] |
| **limit** | **Integer**| Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page | [optional] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**PaginatedImageList**](PaginatedImageList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image listing |  -  |
| **400** | Bad filter parameters |  -  |

<a id="queryImagesByVulnerability"></a>
# **queryImagesByVulnerability**
> PaginatedVulnerableImageList queryImagesByVulnerability(vulnerabilityId, namespace, affectedPackage, severity, vendorOnly, page, limit, xAnchoreAccount)

List images vulnerable to the specific vulnerability ID.

Returns a listing of images and their respective packages vulnerable to the given vulnerability ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    QueryApi apiInstance = new QueryApi(defaultClient);
    String vulnerabilityId = "vulnerabilityId_example"; // String | The ID of the vulnerability to search for within all images stored in anchore-engine (e.g. CVE-1999-0001)
    String namespace = "namespace_example"; // String | Filter results to images within the given vulnerability namespace (e.g. debian:8, ubuntu:14.04)
    String affectedPackage = "affectedPackage_example"; // String | Filter results to images with vulnable packages with the given package name (e.g. libssl)
    String severity = "Unknown"; // String | Filter results to vulnerable package/vulnerability with the given severity
    Boolean vendorOnly = true; // Boolean | Filter results to include only vulnerabilities that are not marked as invalid by upstream OS vendor data
    Integer page = 56; // Integer | The page of results to fetch. Pages start at 1
    Integer limit = 56; // Integer | Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      PaginatedVulnerableImageList result = apiInstance.queryImagesByVulnerability(vulnerabilityId, namespace, affectedPackage, severity, vendorOnly, page, limit, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#queryImagesByVulnerability");
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
| **vulnerabilityId** | **String**| The ID of the vulnerability to search for within all images stored in anchore-engine (e.g. CVE-1999-0001) | |
| **namespace** | **String**| Filter results to images within the given vulnerability namespace (e.g. debian:8, ubuntu:14.04) | [optional] |
| **affectedPackage** | **String**| Filter results to images with vulnable packages with the given package name (e.g. libssl) | [optional] |
| **severity** | **String**| Filter results to vulnerable package/vulnerability with the given severity | [optional] [enum: Unknown, Negligible, Low, Medium, High, Critical] |
| **vendorOnly** | **Boolean**| Filter results to include only vulnerabilities that are not marked as invalid by upstream OS vendor data | [optional] [default to true] |
| **page** | **Integer**| The page of results to fetch. Pages start at 1 | [optional] |
| **limit** | **Integer**| Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page | [optional] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**PaginatedVulnerableImageList**](PaginatedVulnerableImageList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image lookup success |  -  |
| **400** | Invalid filter parameters |  -  |

<a id="queryVulnerabilities"></a>
# **queryVulnerabilities**
> PaginatedVulnerabilityList queryVulnerabilities(id, affectedPackage, affectedPackageVersion, page, limit, namespace)

Listing information about given vulnerability

List (w/filters) vulnerability records known by the system, with affected packages information if present

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    QueryApi apiInstance = new QueryApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | The ID of the vulnerability (e.g. CVE-1999-0001)
    String affectedPackage = "affectedPackage_example"; // String | Filter results by specified package name (e.g. sed)
    String affectedPackageVersion = "affectedPackageVersion_example"; // String | Filter results by specified package version (e.g. 4.4-1)
    String page = "1"; // String | The page of results to fetch. Pages start at 1
    Integer limit = 56; // Integer | Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page
    List<String> namespace = Arrays.asList(); // List<String> | Namespace(s) to filter vulnerability records by
    try {
      PaginatedVulnerabilityList result = apiInstance.queryVulnerabilities(id, affectedPackage, affectedPackageVersion, page, limit, namespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#queryVulnerabilities");
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
| **id** | [**List&lt;String&gt;**](String.md)| The ID of the vulnerability (e.g. CVE-1999-0001) | |
| **affectedPackage** | **String**| Filter results by specified package name (e.g. sed) | [optional] |
| **affectedPackageVersion** | **String**| Filter results by specified package version (e.g. 4.4-1) | [optional] |
| **page** | **String**| The page of results to fetch. Pages start at 1 | [optional] [default to 1] |
| **limit** | **Integer**| Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page | [optional] |
| **namespace** | [**List&lt;String&gt;**](String.md)| Namespace(s) to filter vulnerability records by | [optional] |

### Return type

[**PaginatedVulnerabilityList**](PaginatedVulnerabilityList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Vulnerability listing paginated |  -  |
| **400** | Invalid filter parameters |  -  |

