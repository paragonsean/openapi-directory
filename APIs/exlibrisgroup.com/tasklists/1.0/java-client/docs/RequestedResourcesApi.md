# RequestedResourcesApi

All URIs are relative to *https://api-eu.hosted.exlibrisgroup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAlmawsV1TaskListsRequestedResources**](RequestedResourcesApi.md#getAlmawsV1TaskListsRequestedResources) | **GET** /almaws/v1/task-lists/requested-resources | Get Requested Resources |
| [**postAlmawsV1TaskListsRequestedResources**](RequestedResourcesApi.md#postAlmawsV1TaskListsRequestedResources) | **POST** /almaws/v1/task-lists/requested-resources | Act on Requested Resources |


<a id="getAlmawsV1TaskListsRequestedResources"></a>
# **getAlmawsV1TaskListsRequestedResources**
> GetAlmawsV1TaskListsRequestedResources200Response getAlmawsV1TaskListsRequestedResources(library, circDesk, location, orderBy, direction, pickupInst, reported, printed, limit, offset)

Get Requested Resources

This API returns a list of requested resources to be picked from the shelf in Alma

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestedResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-eu.hosted.exlibrisgroup.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    RequestedResourcesApi apiInstance = new RequestedResourcesApi(defaultClient);
    String library = "library_example"; // String | The library of the given circulation desk or department where the resources are located. Mandatory.
    String circDesk = "circDesk_example"; // String | The circulation desk where the action is being performed. Mandatory.
    String location = ""; // String | The location code. Optional.
    String orderBy = "call_number"; // String | The order in which to retrieve the results: location/call_number (default).
    String direction = "asc"; // String | The order direction in which to retrieve the results. Optional.
    String pickupInst = ""; // String | The pickup institution. Optional.
    String reported = ""; // String | Show reported results: Y/N. Optional.
    String printed = ""; // String | Show printed results: Y/N. Optional.
    Integer limit = 56; // Integer | Limits the number of results. Optional. Valid values are 0-100. Default value: 10.
    Integer offset = 56; // Integer | Offset of the results returned. Optional. Default value: 0, which means that the first results will be returned.
    try {
      GetAlmawsV1TaskListsRequestedResources200Response result = apiInstance.getAlmawsV1TaskListsRequestedResources(library, circDesk, location, orderBy, direction, pickupInst, reported, printed, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestedResourcesApi#getAlmawsV1TaskListsRequestedResources");
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
| **library** | **String**| The library of the given circulation desk or department where the resources are located. Mandatory. | |
| **circDesk** | **String**| The circulation desk where the action is being performed. Mandatory. | |
| **location** | **String**| The location code. Optional. | [optional] [default to ] |
| **orderBy** | **String**| The order in which to retrieve the results: location/call_number (default). | [optional] [default to call_number] |
| **direction** | **String**| The order direction in which to retrieve the results. Optional. | [optional] [default to asc] |
| **pickupInst** | **String**| The pickup institution. Optional. | [optional] [default to ] |
| **reported** | **String**| Show reported results: Y/N. Optional. | [optional] [default to ] |
| **printed** | **String**| Show printed results: Y/N. Optional. | [optional] [default to ] |
| **limit** | **Integer**| Limits the number of results. Optional. Valid values are 0-100. Default value: 10. | [optional] |
| **offset** | **Integer**| Offset of the results returned. Optional. Default value: 0, which means that the first results will be returned. | [optional] |

### Return type

[**GetAlmawsV1TaskListsRequestedResources200Response**](GetAlmawsV1TaskListsRequestedResources200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - This method returns an object based on rest_requested_resources.xsd. See [here](/alma/apis/docs/xsd/rest_requested_resources.xsd) |  * X-Exl-Api-Remaining -  <br>  |
| **400** | Bad Request  402119 - &#39;General error.&#39;  401664 - &#39;Mandatory field is missing: X.&#39;  40166414 - &#39;The parameter &#39;X&#39; is mandatory. Valid options are: Y.&#39; |  -  |
| **500** | Internal Server Error |  -  |

<a id="postAlmawsV1TaskListsRequestedResources"></a>
# **postAlmawsV1TaskListsRequestedResources**
> Object postAlmawsV1TaskListsRequestedResources(library, circDesk, op, location, pickupInst, reported, printed)

Act on Requested Resources

This API performs an action on requested resources that are on the shelf in Alma

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestedResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-eu.hosted.exlibrisgroup.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    RequestedResourcesApi apiInstance = new RequestedResourcesApi(defaultClient);
    String library = ""; // String | The library of the given circulation desk or department where the resources are located. Mandatory.
    String circDesk = ""; // String | The circulation desk where the action is being performed. Mandatory.
    String op = ""; // String | Operation to be preformed on the list of given requests. Currently the only supported action is 'mark_reported'. Mandatory.
    String location = ""; // String | The location code. Optional.
    String pickupInst = ""; // String | The pickup institution. Optional.
    String reported = ""; // String | Show reported results: Y/N. Optional.
    String printed = ""; // String | Show printed results: Y/N. Optional.
    try {
      Object result = apiInstance.postAlmawsV1TaskListsRequestedResources(library, circDesk, op, location, pickupInst, reported, printed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestedResourcesApi#postAlmawsV1TaskListsRequestedResources");
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
| **library** | **String**| The library of the given circulation desk or department where the resources are located. Mandatory. | [optional] [default to ] |
| **circDesk** | **String**| The circulation desk where the action is being performed. Mandatory. | [optional] [default to ] |
| **op** | **String**| Operation to be preformed on the list of given requests. Currently the only supported action is &#39;mark_reported&#39;. Mandatory. | [optional] [default to ] |
| **location** | **String**| The location code. Optional. | [optional] [default to ] |
| **pickupInst** | **String**| The pickup institution. Optional. | [optional] [default to ] |
| **reported** | **String**| Show reported results: Y/N. Optional. | [optional] [default to ] |
| **printed** | **String**| Show printed results: Y/N. Optional. | [optional] [default to ] |

### Return type

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - This method returns an object based on rest_requested_resources.xsd. See [here](/alma/apis/docs/xsd/rest_requested_resources.xsd) |  * X-Exl-Api-Remaining -  <br>  |
| **400** | Bad Request  402119 - &#39;General error.&#39;  401664 - &#39;Mandatory field is missing: X.&#39;  40166414 - &#39;The parameter &#39;X&#39; is mandatory. Valid options are: Y.&#39; |  -  |
| **500** | Internal Server Error |  -  |

