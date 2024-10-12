# OrderDocumentsApi

All URIs are relative to *https://dfareporting.googleapis.com/dfareporting/v3.3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dfareportingOrderDocumentsGet**](OrderDocumentsApi.md#dfareportingOrderDocumentsGet) | **GET** /userprofiles/{profileId}/projects/{projectId}/orderDocuments/{id} |  |
| [**dfareportingOrderDocumentsList**](OrderDocumentsApi.md#dfareportingOrderDocumentsList) | **GET** /userprofiles/{profileId}/projects/{projectId}/orderDocuments |  |


<a id="dfareportingOrderDocumentsGet"></a>
# **dfareportingOrderDocumentsGet**
> OrderDocument dfareportingOrderDocumentsGet(profileId, projectId, id, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Gets one order document by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderDocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dfareporting.googleapis.com/dfareporting/v3.3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrderDocumentsApi apiInstance = new OrderDocumentsApi(defaultClient);
    String profileId = "profileId_example"; // String | User profile ID associated with this request.
    String projectId = "projectId_example"; // String | Project ID for order documents.
    String id = "id_example"; // String | Order document ID.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    try {
      OrderDocument result = apiInstance.dfareportingOrderDocumentsGet(profileId, projectId, id, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderDocumentsApi#dfareportingOrderDocumentsGet");
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
| **profileId** | **String**| User profile ID associated with this request. | |
| **projectId** | **String**| Project ID for order documents. | |
| **id** | **String**| Order document ID. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |

### Return type

[**OrderDocument**](OrderDocument.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dfareportingOrderDocumentsList"></a>
# **dfareportingOrderDocumentsList**
> OrderDocumentsListResponse dfareportingOrderDocumentsList(profileId, projectId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, approved, ids, maxResults, orderId, pageToken, searchString, siteId, sortField, sortOrder)



Retrieves a list of order documents, possibly filtered. This method supports paging.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderDocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dfareporting.googleapis.com/dfareporting/v3.3");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrderDocumentsApi apiInstance = new OrderDocumentsApi(defaultClient);
    String profileId = "profileId_example"; // String | User profile ID associated with this request.
    String projectId = "projectId_example"; // String | Project ID for order documents.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Boolean approved = true; // Boolean | Select only order documents that have been approved by at least one user.
    List<String> ids = Arrays.asList(); // List<String> | Select only order documents with these IDs.
    Integer maxResults = 56; // Integer | Maximum number of results to return.
    List<String> orderId = Arrays.asList(); // List<String> | Select only order documents for specified orders.
    String pageToken = "pageToken_example"; // String | Value of the nextPageToken from the previous result page.
    String searchString = "searchString_example"; // String | Allows searching for order documents by name or ID. Wildcards (*) are allowed. For example, \"orderdocument*2015\" will return order documents with names like \"orderdocument June 2015\", \"orderdocument April 2015\", or simply \"orderdocument 2015\". Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \"orderdocument\" will match order documents with name \"my orderdocument\", \"orderdocument 2015\", or simply \"orderdocument\".
    List<String> siteId = Arrays.asList(); // List<String> | Select only order documents that are associated with these sites.
    String sortField = "ID"; // String | Field by which to sort the list.
    String sortOrder = "ASCENDING"; // String | Order of sorted results.
    try {
      OrderDocumentsListResponse result = apiInstance.dfareportingOrderDocumentsList(profileId, projectId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, approved, ids, maxResults, orderId, pageToken, searchString, siteId, sortField, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderDocumentsApi#dfareportingOrderDocumentsList");
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
| **profileId** | **String**| User profile ID associated with this request. | |
| **projectId** | **String**| Project ID for order documents. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **approved** | **Boolean**| Select only order documents that have been approved by at least one user. | [optional] |
| **ids** | [**List&lt;String&gt;**](String.md)| Select only order documents with these IDs. | [optional] |
| **maxResults** | **Integer**| Maximum number of results to return. | [optional] |
| **orderId** | [**List&lt;String&gt;**](String.md)| Select only order documents for specified orders. | [optional] |
| **pageToken** | **String**| Value of the nextPageToken from the previous result page. | [optional] |
| **searchString** | **String**| Allows searching for order documents by name or ID. Wildcards (*) are allowed. For example, \&quot;orderdocument*2015\&quot; will return order documents with names like \&quot;orderdocument June 2015\&quot;, \&quot;orderdocument April 2015\&quot;, or simply \&quot;orderdocument 2015\&quot;. Most of the searches also add wildcards implicitly at the start and the end of the search string. For example, a search string of \&quot;orderdocument\&quot; will match order documents with name \&quot;my orderdocument\&quot;, \&quot;orderdocument 2015\&quot;, or simply \&quot;orderdocument\&quot;. | [optional] |
| **siteId** | [**List&lt;String&gt;**](String.md)| Select only order documents that are associated with these sites. | [optional] |
| **sortField** | **String**| Field by which to sort the list. | [optional] [enum: ID, NAME] |
| **sortOrder** | **String**| Order of sorted results. | [optional] [enum: ASCENDING, DESCENDING] |

### Return type

[**OrderDocumentsListResponse**](OrderDocumentsListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

