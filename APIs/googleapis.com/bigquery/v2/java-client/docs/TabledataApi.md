# TabledataApi

All URIs are relative to *https://bigquery.googleapis.com/bigquery/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bigqueryTabledataInsertAll**](TabledataApi.md#bigqueryTabledataInsertAll) | **POST** /projects/{projectId}/datasets/{datasetId}/tables/{tableId}/insertAll |  |
| [**bigqueryTabledataList**](TabledataApi.md#bigqueryTabledataList) | **GET** /projects/{projectId}/datasets/{datasetId}/tables/{tableId}/data |  |


<a id="bigqueryTabledataInsertAll"></a>
# **bigqueryTabledataInsertAll**
> TableDataInsertAllResponse bigqueryTabledataInsertAll(projectId, datasetId, tableId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, tableDataInsertAllRequest)



Streams data into BigQuery one record at a time without needing to run a load job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TabledataApi;

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

    TabledataApi apiInstance = new TabledataApi(defaultClient);
    String projectId = "projectId_example"; // String | Required. Project ID of the destination.
    String datasetId = "datasetId_example"; // String | Required. Dataset ID of the destination.
    String tableId = "tableId_example"; // String | Required. Table ID of the destination.
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
    TableDataInsertAllRequest tableDataInsertAllRequest = new TableDataInsertAllRequest(); // TableDataInsertAllRequest | 
    try {
      TableDataInsertAllResponse result = apiInstance.bigqueryTabledataInsertAll(projectId, datasetId, tableId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, tableDataInsertAllRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TabledataApi#bigqueryTabledataInsertAll");
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
| **projectId** | **String**| Required. Project ID of the destination. | |
| **datasetId** | **String**| Required. Dataset ID of the destination. | |
| **tableId** | **String**| Required. Table ID of the destination. | |
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
| **tableDataInsertAllRequest** | [**TableDataInsertAllRequest**](TableDataInsertAllRequest.md)|  | [optional] |

### Return type

[**TableDataInsertAllResponse**](TableDataInsertAllResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="bigqueryTabledataList"></a>
# **bigqueryTabledataList**
> TableDataList bigqueryTabledataList(projectId, datasetId, tableId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, formatOptionsUseInt64Timestamp, maxResults, pageToken, selectedFields, startIndex)



List the content of a table in rows.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TabledataApi;

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

    TabledataApi apiInstance = new TabledataApi(defaultClient);
    String projectId = "projectId_example"; // String | Required. Project id of the table to list.
    String datasetId = "datasetId_example"; // String | Required. Dataset id of the table to list.
    String tableId = "tableId_example"; // String | Required. Table id of the table to list.
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
    Boolean formatOptionsUseInt64Timestamp = true; // Boolean | Optional. Output timestamp as usec int64. Default is false.
    Integer maxResults = 56; // Integer | Row limit of the table.
    String pageToken = "pageToken_example"; // String | To retrieve the next page of table data, set this field to the string provided in the pageToken field of the response body from your previous call to tabledata.list.
    String selectedFields = "selectedFields_example"; // String | Subset of fields to return, supports select into sub fields. Example: selected_fields = \"a,e.d.f\";
    String startIndex = "startIndex_example"; // String | Start row index of the table.
    try {
      TableDataList result = apiInstance.bigqueryTabledataList(projectId, datasetId, tableId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, formatOptionsUseInt64Timestamp, maxResults, pageToken, selectedFields, startIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TabledataApi#bigqueryTabledataList");
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
| **projectId** | **String**| Required. Project id of the table to list. | |
| **datasetId** | **String**| Required. Dataset id of the table to list. | |
| **tableId** | **String**| Required. Table id of the table to list. | |
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
| **formatOptionsUseInt64Timestamp** | **Boolean**| Optional. Output timestamp as usec int64. Default is false. | [optional] |
| **maxResults** | **Integer**| Row limit of the table. | [optional] |
| **pageToken** | **String**| To retrieve the next page of table data, set this field to the string provided in the pageToken field of the response body from your previous call to tabledata.list. | [optional] |
| **selectedFields** | **String**| Subset of fields to return, supports select into sub fields. Example: selected_fields &#x3D; \&quot;a,e.d.f\&quot;; | [optional] |
| **startIndex** | **String**| Start row index of the table. | [optional] |

### Return type

[**TableDataList**](TableDataList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

