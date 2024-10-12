# MeshServicesApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**meshServiceGet**](MeshServicesApi.md#meshServiceGet) | **GET** /Resources/Applications/{applicationResourceName}/Services/{serviceResourceName} | Gets the Service resource with the given name. |
| [**meshServiceList**](MeshServicesApi.md#meshServiceList) | **GET** /Resources/Applications/{applicationResourceName}/Services | Lists all the service resources. |


<a id="meshServiceGet"></a>
# **meshServiceGet**
> ServiceResourceDescription meshServiceGet(apiVersion, applicationResourceName, serviceResourceName)

Gets the Service resource with the given name.

Gets the information about the Service resource with the given name. The information include the description and other properties of the Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshServicesApi apiInstance = new MeshServicesApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
    String serviceResourceName = "serviceResourceName_example"; // String | The identity of the service.
    try {
      ServiceResourceDescription result = apiInstance.meshServiceGet(apiVersion, applicationResourceName, serviceResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshServicesApi#meshServiceGet");
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
| **serviceResourceName** | **String**| The identity of the service. | |

### Return type

[**ServiceResourceDescription**](ServiceResourceDescription.md)

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

<a id="meshServiceList"></a>
# **meshServiceList**
> PagedServiceResourceDescriptionList meshServiceList(apiVersion, applicationResourceName)

Lists all the service resources.

Gets the information about all services of an application resource. The information include the description and other properties of the Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeshServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    MeshServicesApi apiInstance = new MeshServicesApi(defaultClient);
    String apiVersion = "6.4-preview"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
    String applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
    try {
      PagedServiceResourceDescriptionList result = apiInstance.meshServiceList(apiVersion, applicationResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeshServicesApi#meshServiceList");
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

[**PagedServiceResourceDescriptionList**](PagedServiceResourceDescriptionList.md)

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

