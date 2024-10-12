# PackagesApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**packagesDeletePackage**](PackagesApi.md#packagesDeletePackage) | **DELETE** /api/v2/Packages/{ID} | Delete a Package. |
| [**packagesGetPackage**](PackagesApi.md#packagesGetPackage) | **GET** /api/v2/Packages/{ID} | Find a Package. |
| [**packagesGetPackages**](PackagesApi.md#packagesGetPackages) | **GET** /api/v2/Packages | List Packages. |
| [**packagesPostPackage**](PackagesApi.md#packagesPostPackage) | **POST** /api/v2/Packages | Add a Package to the Update System. |
| [**packagesPutPackage**](PackagesApi.md#packagesPutPackage) | **PUT** /api/v2/Packages/{ID} | Modify a Packge to the Update System. |


<a id="packagesDeletePackage"></a>
# **packagesDeletePackage**
> packagesDeletePackage(ID)

Delete a Package.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackagesApi apiInstance = new PackagesApi(defaultClient);
    String ID = "ID_example"; // String | The Package ID to Delete
    try {
      apiInstance.packagesDeletePackage(ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackagesApi#packagesDeletePackage");
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
| **ID** | **String**| The Package ID to Delete | |

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

<a id="packagesGetPackage"></a>
# **packagesGetPackage**
> UpdateSystemModelsPackage packagesGetPackage(ID)

Find a Package.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackagesApi apiInstance = new PackagesApi(defaultClient);
    String ID = "ID_example"; // String | The Package ID to Search for
    try {
      UpdateSystemModelsPackage result = apiInstance.packagesGetPackage(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackagesApi#packagesGetPackage");
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
| **ID** | **String**| The Package ID to Search for | |

### Return type

[**UpdateSystemModelsPackage**](UpdateSystemModelsPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="packagesGetPackages"></a>
# **packagesGetPackages**
> APIPagedResponseUpdateSystemModelsPackage packagesGetPackages(limit, offset, packageTypeID, version, released)

List Packages.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackagesApi apiInstance = new PackagesApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    String packageTypeID = "packageTypeID_example"; // String | Optional. If provided, filters by PackageTypeID.
    Integer version = 56; // Integer | Optional. If provided, filters by Version.
    Boolean released = true; // Boolean | Optional. If provided, filters by Released.
    try {
      APIPagedResponseUpdateSystemModelsPackage result = apiInstance.packagesGetPackages(limit, offset, packageTypeID, version, released);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackagesApi#packagesGetPackages");
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
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |
| **packageTypeID** | **String**| Optional. If provided, filters by PackageTypeID. | [optional] |
| **version** | **Integer**| Optional. If provided, filters by Version. | [optional] |
| **released** | **Boolean**| Optional. If provided, filters by Released. | [optional] |

### Return type

[**APIPagedResponseUpdateSystemModelsPackage**](APIPagedResponseUpdateSystemModelsPackage.md)

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

<a id="packagesPostPackage"></a>
# **packagesPostPackage**
> String packagesPostPackage(updateSystemModelsPackage)

Add a Package to the Update System.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackagesApi apiInstance = new PackagesApi(defaultClient);
    UpdateSystemModelsPackage updateSystemModelsPackage = new UpdateSystemModelsPackage(); // UpdateSystemModelsPackage | The package to add.
    try {
      String result = apiInstance.packagesPostPackage(updateSystemModelsPackage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackagesApi#packagesPostPackage");
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
| **updateSystemModelsPackage** | [**UpdateSystemModelsPackage**](UpdateSystemModelsPackage.md)| The package to add. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="packagesPutPackage"></a>
# **packagesPutPackage**
> packagesPutPackage(ID, updateSystemModelsPackage)

Modify a Packge to the Update System.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackagesApi apiInstance = new PackagesApi(defaultClient);
    String ID = "ID_example"; // String | The unique ID of the Package
    UpdateSystemModelsPackage updateSystemModelsPackage = new UpdateSystemModelsPackage(); // UpdateSystemModelsPackage | The package to update.
    try {
      apiInstance.packagesPutPackage(ID, updateSystemModelsPackage);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackagesApi#packagesPutPackage");
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
| **ID** | **String**| The unique ID of the Package | |
| **updateSystemModelsPackage** | [**UpdateSystemModelsPackage**](UpdateSystemModelsPackage.md)| The package to update. | |

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

