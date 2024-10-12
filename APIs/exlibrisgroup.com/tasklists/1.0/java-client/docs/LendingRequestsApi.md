# LendingRequestsApi

All URIs are relative to *https://api-eu.hosted.exlibrisgroup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAlmawsV1TaskListsRsLendingRequests**](LendingRequestsApi.md#getAlmawsV1TaskListsRsLendingRequests) | **GET** /almaws/v1/task-lists/rs/lending-requests | Get Lending Requests |
| [**postAlmawsV1TaskListsRsLendingRequests**](LendingRequestsApi.md#postAlmawsV1TaskListsRsLendingRequests) | **POST** /almaws/v1/task-lists/rs/lending-requests | Act on Lending Requests |


<a id="getAlmawsV1TaskListsRsLendingRequests"></a>
# **getAlmawsV1TaskListsRsLendingRequests**
> GetAlmawsV1TaskListsRsLendingRequests200Response getAlmawsV1TaskListsRsLendingRequests(library, status, printed, reported, partner, requestedFormat, suppliedFormat)

Get Lending Requests

This API returns a list of lending requests in Alma

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LendingRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-eu.hosted.exlibrisgroup.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    LendingRequestsApi apiInstance = new LendingRequestsApi(defaultClient);
    String library = ""; // String | The resource sharing library for which lending requests should be retrieved. Mandatory. List of possible libraries can be retrieved using the [GET /almaws/v1/conf/libraries API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4Dp4I8TKv6CAxBlD4LyRaVE=/37088dc9-c685-4641-bc7f-60b5ca7cabed).
    String status = ""; // String | The status of lending requests to retrieve. Optional. List of possible statuses can be retrieved using the [GET almaws/v1/conf/code-tables/MandatoryLendingWorkflowSteps API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4K7cQ0vuYHLS4NSgDGmcRpRYqx5hIMRTng9SIKO5Vof+/37088dc9-c685-4641-bc7f-60b5ca7cabed) and the  [GET almaws/v1/conf/code-tables/OptionalLendingWorkflowSteps API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4K7cQ0vuYHLS4NSgDGmcRpRYqx5hIMRTng9SIKO5Vof+/37088dc9-c685-4641-bc7f-60b5ca7cabed).
    String printed = ""; // String | The 'printed' value of lending requests to retrieve. Optional. Possible values: Y, N.
    String reported = ""; // String | The 'reported' value of lending requests to retrieve. Optional. Possible values: Y, N.
    String partner = ""; // String | The partner value. Only lending requests from this partner should be retrieved. Optional. List of possible partners can be retrieved using the [GET almaws/v1/partners API](https://developers.exlibrisgroup.com/alma/apis/partners/GET/gwPcGly021piAVNPLaef7suP1zfa6Lui/8883ef41-c3b8-4792-9ff8-cb6b729d6e07).
    String requestedFormat = ""; // String | Requested format of the resource. Optional. List of possible formats can be retrieved using the [GET almaws/v1/conf/code-tables/RequestFormats API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4K7cQ0vuYHLS4NSgDGmcRpRYqx5hIMRTng9SIKO5Vof+/37088dc9-c685-4641-bc7f-60b5ca7cabed).
    String suppliedFormat = ""; // String | Supplied Format of the resource. Optional. List of possible formats can be retrieved using the [GET almaws/v1/conf/code-tables/RequestFormats API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4K7cQ0vuYHLS4NSgDGmcRpRYqx5hIMRTng9SIKO5Vof+/37088dc9-c685-4641-bc7f-60b5ca7cabed).
    try {
      GetAlmawsV1TaskListsRsLendingRequests200Response result = apiInstance.getAlmawsV1TaskListsRsLendingRequests(library, status, printed, reported, partner, requestedFormat, suppliedFormat);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LendingRequestsApi#getAlmawsV1TaskListsRsLendingRequests");
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
| **library** | **String**| The resource sharing library for which lending requests should be retrieved. Mandatory. List of possible libraries can be retrieved using the [GET /almaws/v1/conf/libraries API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4Dp4I8TKv6CAxBlD4LyRaVE&#x3D;/37088dc9-c685-4641-bc7f-60b5ca7cabed). | [optional] [default to ] |
| **status** | **String**| The status of lending requests to retrieve. Optional. List of possible statuses can be retrieved using the [GET almaws/v1/conf/code-tables/MandatoryLendingWorkflowSteps API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4K7cQ0vuYHLS4NSgDGmcRpRYqx5hIMRTng9SIKO5Vof+/37088dc9-c685-4641-bc7f-60b5ca7cabed) and the  [GET almaws/v1/conf/code-tables/OptionalLendingWorkflowSteps API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4K7cQ0vuYHLS4NSgDGmcRpRYqx5hIMRTng9SIKO5Vof+/37088dc9-c685-4641-bc7f-60b5ca7cabed). | [optional] [default to ] |
| **printed** | **String**| The &#39;printed&#39; value of lending requests to retrieve. Optional. Possible values: Y, N. | [optional] [default to ] |
| **reported** | **String**| The &#39;reported&#39; value of lending requests to retrieve. Optional. Possible values: Y, N. | [optional] [default to ] |
| **partner** | **String**| The partner value. Only lending requests from this partner should be retrieved. Optional. List of possible partners can be retrieved using the [GET almaws/v1/partners API](https://developers.exlibrisgroup.com/alma/apis/partners/GET/gwPcGly021piAVNPLaef7suP1zfa6Lui/8883ef41-c3b8-4792-9ff8-cb6b729d6e07). | [optional] [default to ] |
| **requestedFormat** | **String**| Requested format of the resource. Optional. List of possible formats can be retrieved using the [GET almaws/v1/conf/code-tables/RequestFormats API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4K7cQ0vuYHLS4NSgDGmcRpRYqx5hIMRTng9SIKO5Vof+/37088dc9-c685-4641-bc7f-60b5ca7cabed). | [optional] [default to ] |
| **suppliedFormat** | **String**| Supplied Format of the resource. Optional. List of possible formats can be retrieved using the [GET almaws/v1/conf/code-tables/RequestFormats API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4K7cQ0vuYHLS4NSgDGmcRpRYqx5hIMRTng9SIKO5Vof+/37088dc9-c685-4641-bc7f-60b5ca7cabed). | [optional] [default to ] |

### Return type

[**GetAlmawsV1TaskListsRsLendingRequests200Response**](GetAlmawsV1TaskListsRsLendingRequests200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - This method returns an object based on rest_user_resource_sharing_requests.xsd. See [here](/alma/apis/docs/xsd/rest_user_resource_sharing_requests.xsd) |  * X-Exl-Api-Remaining -  <br>  |
| **400** | Bad Request  402119 - &#39;General error.&#39;  401664 - &#39;Mandatory field is missing: X.&#39;  40166414 - &#39;The parameter &#39;X&#39; is mandatory. Valid options are: Y.&#39; |  -  |
| **500** | Internal Server Error |  -  |

<a id="postAlmawsV1TaskListsRsLendingRequests"></a>
# **postAlmawsV1TaskListsRsLendingRequests**
> Object postAlmawsV1TaskListsRsLendingRequests(library, op, status, printed, reported, partner, requestedFormat, suppliedFormat)

Act on Lending Requests

This API preforms the requested action on a list (specified by given filters) of lending requests in Alma

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LendingRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-eu.hosted.exlibrisgroup.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    LendingRequestsApi apiInstance = new LendingRequestsApi(defaultClient);
    String library = ""; // String | The resource sharing library from which lending requests should be retrieved. Mandatory. List of possible libraries can be retrieved using the [GET /almaws/v1/conf/libraries API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4Dp4I8TKv6CAxBlD4LyRaVE=/37088dc9-c685-4641-bc7f-60b5ca7cabed).
    String op = ""; // String | Operation to be preformed on the list of given requests. Currently the only supported action is 'mark_reported'. Mandatory.
    String status = ""; // String | The status of lending requests to retrieve. Optional. List of possible statuses can be retrieved using the [GET almaws/v1/conf/code-tables/MandatoryLendingWorkflowSteps API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4K7cQ0vuYHLS4NSgDGmcRpRYqx5hIMRTng9SIKO5Vof+/37088dc9-c685-4641-bc7f-60b5ca7cabed).and the  [GET almaws/v1/conf/code-tables/OptionalLendingWorkflowSteps API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4K7cQ0vuYHLS4NSgDGmcRpRYqx5hIMRTng9SIKO5Vof+/37088dc9-c685-4641-bc7f-60b5ca7cabed).
    String printed = ""; // String | The 'printed' value of lending requests to retrieve. Optional. Possible values: Y, N.
    String reported = ""; // String | The 'reported' value of lending requests to retrieve. Optional. Possible values: Y, N.
    String partner = ""; // String | The partner value. Only lending requests from this partner should be. Optional. List of possible partners can be retrieved using the [GET almaws/v1/partners API](https://developers.exlibrisgroup.com/alma/apis/partners/GET/gwPcGly021piAVNPLaef7suP1zfa6Lui/8883ef41-c3b8-4792-9ff8-cb6b729d6e07).
    String requestedFormat = ""; // String | Requested format of the resource. Optional. List of possible formats can be retrieved using the [GET almaws/v1/conf/code-tables/RequestFormats API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4K7cQ0vuYHLS4NSgDGmcRpRYqx5hIMRTng9SIKO5Vof+/37088dc9-c685-4641-bc7f-60b5ca7cabed).
    String suppliedFormat = ""; // String | Supplied Format of the resource. Optional. List of possible formats can be retrieved using the [GET almaws/v1/conf/code-tables/RequestFormats API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4K7cQ0vuYHLS4NSgDGmcRpRYqx5hIMRTng9SIKO5Vof+/37088dc9-c685-4641-bc7f-60b5ca7cabed).
    try {
      Object result = apiInstance.postAlmawsV1TaskListsRsLendingRequests(library, op, status, printed, reported, partner, requestedFormat, suppliedFormat);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LendingRequestsApi#postAlmawsV1TaskListsRsLendingRequests");
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
| **library** | **String**| The resource sharing library from which lending requests should be retrieved. Mandatory. List of possible libraries can be retrieved using the [GET /almaws/v1/conf/libraries API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4Dp4I8TKv6CAxBlD4LyRaVE&#x3D;/37088dc9-c685-4641-bc7f-60b5ca7cabed). | [optional] [default to ] |
| **op** | **String**| Operation to be preformed on the list of given requests. Currently the only supported action is &#39;mark_reported&#39;. Mandatory. | [optional] [default to ] |
| **status** | **String**| The status of lending requests to retrieve. Optional. List of possible statuses can be retrieved using the [GET almaws/v1/conf/code-tables/MandatoryLendingWorkflowSteps API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4K7cQ0vuYHLS4NSgDGmcRpRYqx5hIMRTng9SIKO5Vof+/37088dc9-c685-4641-bc7f-60b5ca7cabed).and the  [GET almaws/v1/conf/code-tables/OptionalLendingWorkflowSteps API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4K7cQ0vuYHLS4NSgDGmcRpRYqx5hIMRTng9SIKO5Vof+/37088dc9-c685-4641-bc7f-60b5ca7cabed). | [optional] [default to ] |
| **printed** | **String**| The &#39;printed&#39; value of lending requests to retrieve. Optional. Possible values: Y, N. | [optional] [default to ] |
| **reported** | **String**| The &#39;reported&#39; value of lending requests to retrieve. Optional. Possible values: Y, N. | [optional] [default to ] |
| **partner** | **String**| The partner value. Only lending requests from this partner should be. Optional. List of possible partners can be retrieved using the [GET almaws/v1/partners API](https://developers.exlibrisgroup.com/alma/apis/partners/GET/gwPcGly021piAVNPLaef7suP1zfa6Lui/8883ef41-c3b8-4792-9ff8-cb6b729d6e07). | [optional] [default to ] |
| **requestedFormat** | **String**| Requested format of the resource. Optional. List of possible formats can be retrieved using the [GET almaws/v1/conf/code-tables/RequestFormats API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4K7cQ0vuYHLS4NSgDGmcRpRYqx5hIMRTng9SIKO5Vof+/37088dc9-c685-4641-bc7f-60b5ca7cabed). | [optional] [default to ] |
| **suppliedFormat** | **String**| Supplied Format of the resource. Optional. List of possible formats can be retrieved using the [GET almaws/v1/conf/code-tables/RequestFormats API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4K7cQ0vuYHLS4NSgDGmcRpRYqx5hIMRTng9SIKO5Vof+/37088dc9-c685-4641-bc7f-60b5ca7cabed). | [optional] [default to ] |

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
| **200** | OK - This method returns an object based on rest_user_resource_sharing_request.xsd. See [here](/alma/apis/docs/xsd/rest_user_resource_sharing_request.xsd) |  * X-Exl-Api-Remaining -  <br>  |
| **400** | Bad Request  402119 - &#39;General error.&#39;  401666 - &#39;X parameter is not valid.&#39;  401664 - &#39;Mandatory field is missing: X.&#39;  40166414 - &#39;The parameter &#39;X&#39; is mandatory. Valid options are: Y.&#39; |  -  |
| **500** | Internal Server Error |  -  |

