# MeshApplicationsApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**meshApplicationCreateOrUpdate**](MeshApplicationsApi.md#meshApplicationCreateOrUpdate) | **PUT** /Resources/Applications/{applicationResourceName} | Creates or updates a Application resource. |
| [**meshApplicationDelete**](MeshApplicationsApi.md#meshApplicationDelete) | **DELETE** /Resources/Applications/{applicationResourceName} | Deletes the Application resource. |
| [**meshApplicationGet**](MeshApplicationsApi.md#meshApplicationGet) | **GET** /Resources/Applications/{applicationResourceName} | Gets the Application resource with the given name. |
| [**meshApplicationGetUpgradeProgress**](MeshApplicationsApi.md#meshApplicationGetUpgradeProgress) | **GET** /Resources/Applications/{applicationResourceName}/$/GetUpgradeProgress | Gets the progress of the latest upgrade performed on this application resource. |
| [**meshApplicationList**](MeshApplicationsApi.md#meshApplicationList) | **GET** /Resources/Applications | Lists all the application resources. |


<a id="meshApplicationCreateOrUpdate"></a>
# **meshApplicationCreateOrUpdate**
> ApplicationResourceDescription meshApplicationCreateOrUpdate(apiVersion, applicationResourceName, applicationResourceDescription)

Creates or updates a Application resource.

Creates a Application resource with the specified name, description and properties. If Application resource with the same name exists, then it is updated with the specified description and properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshApplicationsApi apiInstance = new MeshApplicationsApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
    ApplicationResourceDescription applicationResourceDescription = new ApplicationResourceDescription(); // ApplicationResourceDescription | Description for creating a Application resource.
    try {
      ApplicationResourceDescription result = apiInstance.meshApplicationCreateOrUpdate(apiVersion, applicationResourceName, applicationResourceDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshApplicationsApi#meshApplicationCreateOrUpdate");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to 6.4-preview] [enum: 6.4-preview] |
| **applicationResourceName** | **String**| The identity of the application. | |
| **applicationResourceDescription** | [**ApplicationResourceDescription**](ApplicationResourceDescription.md)| Description for creating a Application resource. | |

### Return type

[**ApplicationResourceDescription**](ApplicationResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **202** | Accepted |  -  |
| **0** | Error |  -  |

<a id="meshApplicationDelete"></a>
# **meshApplicationDelete**
> meshApplicationDelete(apiVersion, applicationResourceName)

Deletes the Application resource.

Deletes the Application resource identified by the name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshApplicationsApi apiInstance = new MeshApplicationsApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
    try {
      apiInstance.meshApplicationDelete(apiVersion, applicationResourceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshApplicationsApi#meshApplicationDelete");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to 6.4-preview] [enum: 6.4-preview] |
| **applicationResourceName** | **String**| The identity of the application. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **204** | No Content - the specified application was not found. |  -  |
| **0** | Error |  -  |

<a id="meshApplicationGet"></a>
# **meshApplicationGet**
> ApplicationResourceDescription meshApplicationGet(apiVersion, applicationResourceName)

Gets the Application resource with the given name.

Gets the information about the Application resource with the given name. The information include the description and other properties of the Application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshApplicationsApi apiInstance = new MeshApplicationsApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
    try {
      ApplicationResourceDescription result = apiInstance.meshApplicationGet(apiVersion, applicationResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshApplicationsApi#meshApplicationGet");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to 6.4-preview] [enum: 6.4-preview] |
| **applicationResourceName** | **String**| The identity of the application. | |

### Return type

[**ApplicationResourceDescription**](ApplicationResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

<a id="meshApplicationGetUpgradeProgress"></a>
# **meshApplicationGetUpgradeProgress**
> ApplicationResourceUpgradeProgressInfo meshApplicationGetUpgradeProgress(apiVersion, applicationResourceName)

Gets the progress of the latest upgrade performed on this application resource.

Gets the upgrade progress information about the Application resource with the given name. The information include percentage of completion and other upgrade state information of the Application resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshApplicationsApi apiInstance = new MeshApplicationsApi(defaultClient);
    String apiVersion = "7.0"; // String | The version of the API. This parameter is required and its value must be '7.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
    try {
      ApplicationResourceUpgradeProgressInfo result = apiInstance.meshApplicationGetUpgradeProgress(apiVersion, applicationResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshApplicationsApi#meshApplicationGetUpgradeProgress");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;7.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This version is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accepts any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0 and the runtime is 6.1, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 7.0] [enum: 7.0] |
| **applicationResourceName** | **String**| The identity of the application. | |

### Return type

[**ApplicationResourceUpgradeProgressInfo**](ApplicationResourceUpgradeProgressInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

<a id="meshApplicationList"></a>
# **meshApplicationList**
> PagedApplicationResourceDescriptionList meshApplicationList(apiVersion)

Lists all the application resources.

Gets the information about all application resources in a given resource group. The information include the description and other properties of the Application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshApplicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshApplicationsApi apiInstance = new MeshApplicationsApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    try {
      PagedApplicationResourceDescriptionList result = apiInstance.meshApplicationList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshApplicationsApi#meshApplicationList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to 6.4-preview] [enum: 6.4-preview] |

### Return type

[**PagedApplicationResourceDescriptionList**](PagedApplicationResourceDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

