# PackageTypesApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2PackageTypesIDGet**](PackageTypesApi.md#apiV2PackageTypesIDGet) | **GET** /api/v2/PackageTypes/{ID} | Get a specific Package Type. |
| [**packageTypesAddPackageTypeUser**](PackageTypesApi.md#packageTypesAddPackageTypeUser) | **POST** /api/v2/PackageTypes/{id}/Users/{userID} | Add a package type that a user can see. |
| [**packageTypesDelete**](PackageTypesApi.md#packageTypesDelete) | **DELETE** /api/v2/PackageTypes/{ID} | Delete a Package Type. |
| [**packageTypesGet**](PackageTypesApi.md#packageTypesGet) | **GET** /api/v2/PackageTypes | Get all of the Package Types. |
| [**packageTypesPost**](PackageTypesApi.md#packageTypesPost) | **POST** /api/v2/PackageTypes | Add a Package Type. |
| [**packageTypesPut**](PackageTypesApi.md#packageTypesPut) | **PUT** /api/v2/PackageTypes/{ID} | Modify a Package Type. |
| [**packageTypesRemovePackageTypeUser**](PackageTypesApi.md#packageTypesRemovePackageTypeUser) | **DELETE** /api/v2/PackageTypes/{id}/Users/{userID} | Deletes a package type a user could see. |


<a id="apiV2PackageTypesIDGet"></a>
# **apiV2PackageTypesIDGet**
> UpdateSystemModelsPackageType apiV2PackageTypesIDGet(ID)

Get a specific Package Type.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackageTypesApi apiInstance = new PackageTypesApi(defaultClient);
    String ID = "ID_example"; // String | The Package Type ID
    try {
      UpdateSystemModelsPackageType result = apiInstance.apiV2PackageTypesIDGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageTypesApi#apiV2PackageTypesIDGet");
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
| **ID** | **String**| The Package Type ID | |

### Return type

[**UpdateSystemModelsPackageType**](UpdateSystemModelsPackageType.md)

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

<a id="packageTypesAddPackageTypeUser"></a>
# **packageTypesAddPackageTypeUser**
> packageTypesAddPackageTypeUser(id, userID)

Add a package type that a user can see.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackageTypesApi apiInstance = new PackageTypesApi(defaultClient);
    String id = "id_example"; // String | The ID of the Package Type
    Integer userID = 56; // Integer | The userID to link to the package type
    try {
      apiInstance.packageTypesAddPackageTypeUser(id, userID);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageTypesApi#packageTypesAddPackageTypeUser");
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
| **id** | **String**| The ID of the Package Type | |
| **userID** | **Integer**| The userID to link to the package type | |

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

<a id="packageTypesDelete"></a>
# **packageTypesDelete**
> packageTypesDelete(ID)

Delete a Package Type.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackageTypesApi apiInstance = new PackageTypesApi(defaultClient);
    String ID = "ID_example"; // String | The Package Type ID
    try {
      apiInstance.packageTypesDelete(ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageTypesApi#packageTypesDelete");
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
| **ID** | **String**| The Package Type ID | |

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

<a id="packageTypesGet"></a>
# **packageTypesGet**
> APIPagedResponseUpdateSystemModelsPackageType packageTypesGet(limit, offset, userID)

Get all of the Package Types.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackageTypesApi apiInstance = new PackageTypesApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    Integer userID = 56; // Integer | Optional. The user ID to sort packageTypes by the user's access
    try {
      APIPagedResponseUpdateSystemModelsPackageType result = apiInstance.packageTypesGet(limit, offset, userID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageTypesApi#packageTypesGet");
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
| **userID** | **Integer**| Optional. The user ID to sort packageTypes by the user&#39;s access | [optional] |

### Return type

[**APIPagedResponseUpdateSystemModelsPackageType**](APIPagedResponseUpdateSystemModelsPackageType.md)

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

<a id="packageTypesPost"></a>
# **packageTypesPost**
> String packageTypesPost(updateSystemModelsPackageType)

Add a Package Type.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackageTypesApi apiInstance = new PackageTypesApi(defaultClient);
    UpdateSystemModelsPackageType updateSystemModelsPackageType = new UpdateSystemModelsPackageType(); // UpdateSystemModelsPackageType | The Package Type to add
    try {
      String result = apiInstance.packageTypesPost(updateSystemModelsPackageType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageTypesApi#packageTypesPost");
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
| **updateSystemModelsPackageType** | [**UpdateSystemModelsPackageType**](UpdateSystemModelsPackageType.md)| The Package Type to add | |

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

<a id="packageTypesPut"></a>
# **packageTypesPut**
> packageTypesPut(ID, updateSystemModelsPackageType)

Modify a Package Type.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackageTypesApi apiInstance = new PackageTypesApi(defaultClient);
    String ID = "ID_example"; // String | The ID of the Package Type
    UpdateSystemModelsPackageType updateSystemModelsPackageType = new UpdateSystemModelsPackageType(); // UpdateSystemModelsPackageType | The Package Type to update
    try {
      apiInstance.packageTypesPut(ID, updateSystemModelsPackageType);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageTypesApi#packageTypesPut");
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
| **ID** | **String**| The ID of the Package Type | |
| **updateSystemModelsPackageType** | [**UpdateSystemModelsPackageType**](UpdateSystemModelsPackageType.md)| The Package Type to update | |

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

<a id="packageTypesRemovePackageTypeUser"></a>
# **packageTypesRemovePackageTypeUser**
> packageTypesRemovePackageTypeUser(id, userID)

Deletes a package type a user could see.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackageTypesApi apiInstance = new PackageTypesApi(defaultClient);
    String id = "id_example"; // String | The ID of the Package Type
    Integer userID = 56; // Integer | The userID to link to the package type
    try {
      apiInstance.packageTypesRemovePackageTypeUser(id, userID);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageTypesApi#packageTypesRemovePackageTypeUser");
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
| **id** | **String**| The ID of the Package Type | |
| **userID** | **Integer**| The userID to link to the package type | |

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

