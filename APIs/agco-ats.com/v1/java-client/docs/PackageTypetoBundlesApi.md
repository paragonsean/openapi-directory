# PackageTypetoBundlesApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**packageTypetoBundlesDelete**](PackageTypetoBundlesApi.md#packageTypetoBundlesDelete) | **DELETE** /api/v2/PackageTypetoBundles | Delete a Package Type to Bundle Relationship. |
| [**packageTypetoBundlesGet**](PackageTypetoBundlesApi.md#packageTypetoBundlesGet) | **GET** /api/v2/PackageTypetoBundles | Get all of the Package Type to Bundle Relationships. |
| [**packageTypetoBundlesPost**](PackageTypetoBundlesApi.md#packageTypetoBundlesPost) | **POST** /api/v2/PackageTypetoBundles | Add a new Package Type ID to Bundle Relationship. |
| [**packageTypetoBundlesPut**](PackageTypetoBundlesApi.md#packageTypetoBundlesPut) | **PUT** /api/v2/PackageTypetoBundles | Update a Package Type ID to Bundle Relationship. |


<a id="packageTypetoBundlesDelete"></a>
# **packageTypetoBundlesDelete**
> packageTypetoBundlesDelete(bundleID, packageTypeID)

Delete a Package Type to Bundle Relationship.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageTypetoBundlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackageTypetoBundlesApi apiInstance = new PackageTypetoBundlesApi(defaultClient);
    String bundleID = "bundleID_example"; // String | The BundleID
    String packageTypeID = "packageTypeID_example"; // String | The PackageTypeID
    try {
      apiInstance.packageTypetoBundlesDelete(bundleID, packageTypeID);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageTypetoBundlesApi#packageTypetoBundlesDelete");
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
| **bundleID** | **String**| The BundleID | |
| **packageTypeID** | **String**| The PackageTypeID | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="packageTypetoBundlesGet"></a>
# **packageTypetoBundlesGet**
> APIPagedResponseUpdateSystemModelsPackageTypeIDtoBundle packageTypetoBundlesGet(bundleID, limit, offset)

Get all of the Package Type to Bundle Relationships.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageTypetoBundlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackageTypetoBundlesApi apiInstance = new PackageTypetoBundlesApi(defaultClient);
    String bundleID = "bundleID_example"; // String | Optional. Filter by BundleID.
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseUpdateSystemModelsPackageTypeIDtoBundle result = apiInstance.packageTypetoBundlesGet(bundleID, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageTypetoBundlesApi#packageTypetoBundlesGet");
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
| **bundleID** | **String**| Optional. Filter by BundleID. | [optional] |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseUpdateSystemModelsPackageTypeIDtoBundle**](APIPagedResponseUpdateSystemModelsPackageTypeIDtoBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="packageTypetoBundlesPost"></a>
# **packageTypetoBundlesPost**
> packageTypetoBundlesPost(updateSystemModelsPackageTypeIDtoBundle)

Add a new Package Type ID to Bundle Relationship.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageTypetoBundlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackageTypetoBundlesApi apiInstance = new PackageTypetoBundlesApi(defaultClient);
    UpdateSystemModelsPackageTypeIDtoBundle updateSystemModelsPackageTypeIDtoBundle = new UpdateSystemModelsPackageTypeIDtoBundle(); // UpdateSystemModelsPackageTypeIDtoBundle | The PackageTypeToBundle to add.
    try {
      apiInstance.packageTypetoBundlesPost(updateSystemModelsPackageTypeIDtoBundle);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageTypetoBundlesApi#packageTypetoBundlesPost");
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
| **updateSystemModelsPackageTypeIDtoBundle** | [**UpdateSystemModelsPackageTypeIDtoBundle**](UpdateSystemModelsPackageTypeIDtoBundle.md)| The PackageTypeToBundle to add. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="packageTypetoBundlesPut"></a>
# **packageTypetoBundlesPut**
> packageTypetoBundlesPut(updateSystemModelsPackageTypeIDtoBundle)

Update a Package Type ID to Bundle Relationship.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageTypetoBundlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackageTypetoBundlesApi apiInstance = new PackageTypetoBundlesApi(defaultClient);
    UpdateSystemModelsPackageTypeIDtoBundle updateSystemModelsPackageTypeIDtoBundle = new UpdateSystemModelsPackageTypeIDtoBundle(); // UpdateSystemModelsPackageTypeIDtoBundle | The PackageTypeToBundle to update.
    try {
      apiInstance.packageTypetoBundlesPut(updateSystemModelsPackageTypeIDtoBundle);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageTypetoBundlesApi#packageTypetoBundlesPut");
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
| **updateSystemModelsPackageTypeIDtoBundle** | [**UpdateSystemModelsPackageTypeIDtoBundle**](UpdateSystemModelsPackageTypeIDtoBundle.md)| The PackageTypeToBundle to update. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

