# LocationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**locationsGet**](LocationsApi.md#locationsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation} |  |
| [**locationsList**](LocationsApi.md#locationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations |  |


<a id="locationsGet"></a>
# **locationsGet**
> AscLocation locationsGet(apiVersion, subscriptionId, ascLocation)



Details of a specific location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    try {
      AscLocation result = apiInstance.locationsGet(apiVersion, subscriptionId, ascLocation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#locationsGet");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |

### Return type

[**AscLocation**](AscLocation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="locationsList"></a>
# **locationsList**
> AscLocationList locationsList(apiVersion, subscriptionId)



The location of the responsible ASC of the specific subscription (home region). For each subscription there is only one responsible location. The location in the response should be used to read or write other resources in ASC according to their ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    try {
      AscLocationList result = apiInstance.locationsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#locationsList");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |

### Return type

[**AscLocationList**](AscLocationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

