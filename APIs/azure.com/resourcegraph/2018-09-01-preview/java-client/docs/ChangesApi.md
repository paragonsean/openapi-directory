# ChangesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourceChangeDetails**](ChangesApi.md#resourceChangeDetails) | **POST** /providers/Microsoft.ResourceGraph/resourceChangeDetails |  |
| [**resourceChanges**](ChangesApi.md#resourceChanges) | **POST** /providers/Microsoft.ResourceGraph/resourceChanges |  |


<a id="resourceChangeDetails"></a>
# **resourceChangeDetails**
> ResourceChangeData resourceChangeDetails(apiVersion, parameters)



Get resource change details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ChangesApi apiInstance = new ChangesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    ResourceChangeDetailsRequestParameters parameters = new ResourceChangeDetailsRequestParameters(); // ResourceChangeDetailsRequestParameters | The parameters for this request for resource change details.
    try {
      ResourceChangeData result = apiInstance.resourceChangeDetails(apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangesApi#resourceChangeDetails");
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
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**ResourceChangeDetailsRequestParameters**](ResourceChangeDetailsRequestParameters.md)| The parameters for this request for resource change details. | |

### Return type

[**ResourceChangeData**](ResourceChangeData.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Resource change details. |  -  |
| **0** | A response indicating an error. |  -  |

<a id="resourceChanges"></a>
# **resourceChanges**
> ResourceChangeList resourceChanges(apiVersion, parameters)



List changes to a resource for a given time interval.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ChangesApi apiInstance = new ChangesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    ResourceChangesRequestParameters parameters = new ResourceChangesRequestParameters(); // ResourceChangesRequestParameters | the parameters for this request for changes.
    try {
      ResourceChangeList result = apiInstance.resourceChanges(apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangesApi#resourceChanges");
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
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**ResourceChangesRequestParameters**](ResourceChangesRequestParameters.md)| the parameters for this request for changes. | |

### Return type

[**ResourceChangeList**](ResourceChangeList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of changes associated with a resource over a specific time interval. |  -  |
| **0** | A response indicating an error. |  -  |

