# PrivateCloudsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateCloudsGet**](PrivateCloudsApi.md#privateCloudsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName} | Implements private cloud GET method |
| [**privateCloudsList**](PrivateCloudsApi.md#privateCloudsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds | Implements private cloud list GET method |


<a id="privateCloudsGet"></a>
# **privateCloudsGet**
> PrivateCloud privateCloudsGet(subscriptionId, pcName, regionId, apiVersion)

Implements private cloud GET method

Returns private cloud by its name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateCloudsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateCloudsApi apiInstance = new PrivateCloudsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String pcName = "pcName_example"; // String | The private cloud name
    String regionId = "regionId_example"; // String | The region Id (westus, eastus)
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      PrivateCloud result = apiInstance.privateCloudsGet(subscriptionId, pcName, regionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateCloudsApi#privateCloudsGet");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **pcName** | **String**| The private cloud name | |
| **regionId** | **String**| The region Id (westus, eastus) | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**PrivateCloud**](PrivateCloud.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

<a id="privateCloudsList"></a>
# **privateCloudsList**
> PrivateCloudList privateCloudsList(subscriptionId, regionId, apiVersion)

Implements private cloud list GET method

Returns list of private clouds in particular region

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateCloudsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateCloudsApi apiInstance = new PrivateCloudsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String regionId = "regionId_example"; // String | The region Id (westus, eastus)
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      PrivateCloudList result = apiInstance.privateCloudsList(subscriptionId, regionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateCloudsApi#privateCloudsList");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **regionId** | **String**| The region Id (westus, eastus) | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**PrivateCloudList**](PrivateCloudList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

