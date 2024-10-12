# RowAccessPoliciesApi

All URIs are relative to *https://bigquery.googleapis.com/bigquery/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bigqueryRowAccessPoliciesList**](RowAccessPoliciesApi.md#bigqueryRowAccessPoliciesList) | **GET** /projects/{projectId}/datasets/{datasetId}/tables/{tableId}/rowAccessPolicies |  |


<a id="bigqueryRowAccessPoliciesList"></a>
# **bigqueryRowAccessPoliciesList**
> ListRowAccessPoliciesResponse bigqueryRowAccessPoliciesList(projectId, datasetId, tableId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Lists all row access policies on the specified table.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RowAccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bigquery.googleapis.com/bigquery/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RowAccessPoliciesApi apiInstance = new RowAccessPoliciesApi(defaultClient);
    String projectId = "projectId_example"; // String | Required. Project ID of the row access policies to list.
    String datasetId = "datasetId_example"; // String | Required. Dataset ID of row access policies to list.
    String tableId = "tableId_example"; // String | Required. Table ID of the table to list row access policies.
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
    Integer pageSize = 56; // Integer | The maximum number of results to return in a single response page. Leverage the page tokens to iterate through the entire collection.
    String pageToken = "pageToken_example"; // String | Page token, returned by a previous call, to request the next page of results.
    try {
      ListRowAccessPoliciesResponse result = apiInstance.bigqueryRowAccessPoliciesList(projectId, datasetId, tableId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RowAccessPoliciesApi#bigqueryRowAccessPoliciesList");
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
| **projectId** | **String**| Required. Project ID of the row access policies to list. | |
| **datasetId** | **String**| Required. Dataset ID of row access policies to list. | |
| **tableId** | **String**| Required. Table ID of the table to list row access policies. | |
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
| **pageSize** | **Integer**| The maximum number of results to return in a single response page. Leverage the page tokens to iterate through the entire collection. | [optional] |
| **pageToken** | **String**| Page token, returned by a previous call, to request the next page of results. | [optional] |

### Return type

[**ListRowAccessPoliciesResponse**](ListRowAccessPoliciesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

