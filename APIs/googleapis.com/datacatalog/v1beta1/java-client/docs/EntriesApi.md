# EntriesApi

All URIs are relative to *https://datacatalog.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**datacatalogEntriesLookup**](EntriesApi.md#datacatalogEntriesLookup) | **GET** /v1beta1/entries:lookup |  |


<a id="datacatalogEntriesLookup"></a>
# **datacatalogEntriesLookup**
> GoogleCloudDatacatalogV1beta1Entry datacatalogEntriesLookup($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, linkedResource, sqlResource)



Get an entry by target resource name. This method allows clients to use the resource name from the source Google Cloud Platform service to get the Data Catalog Entry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://datacatalog.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EntriesApi apiInstance = new EntriesApi(defaultClient);
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
    String linkedResource = "linkedResource_example"; // String | The full name of the Google Cloud Platform resource the Data Catalog entry represents. See: https://cloud.google.com/apis/design/resource_names#full_resource_name. Full names are case-sensitive. Examples: * //bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId * //pubsub.googleapis.com/projects/projectId/topics/topicId
    String sqlResource = "sqlResource_example"; // String | The SQL name of the entry. SQL names are case-sensitive. Examples: * `pubsub.project_id.topic_id` * ``pubsub.project_id.`topic.id.with.dots` `` * `bigquery.table.project_id.dataset_id.table_id` * `bigquery.dataset.project_id.dataset_id` * `datacatalog.entry.project_id.location_id.entry_group_id.entry_id` `*_id`s should satisfy the standard SQL rules for identifiers. https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical.
    try {
      GoogleCloudDatacatalogV1beta1Entry result = apiInstance.datacatalogEntriesLookup($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, linkedResource, sqlResource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntriesApi#datacatalogEntriesLookup");
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
| **linkedResource** | **String**| The full name of the Google Cloud Platform resource the Data Catalog entry represents. See: https://cloud.google.com/apis/design/resource_names#full_resource_name. Full names are case-sensitive. Examples: * //bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId * //pubsub.googleapis.com/projects/projectId/topics/topicId | [optional] |
| **sqlResource** | **String**| The SQL name of the entry. SQL names are case-sensitive. Examples: * &#x60;pubsub.project_id.topic_id&#x60; * &#x60;&#x60;pubsub.project_id.&#x60;topic.id.with.dots&#x60; &#x60;&#x60; * &#x60;bigquery.table.project_id.dataset_id.table_id&#x60; * &#x60;bigquery.dataset.project_id.dataset_id&#x60; * &#x60;datacatalog.entry.project_id.location_id.entry_group_id.entry_id&#x60; &#x60;*_id&#x60;s should satisfy the standard SQL rules for identifiers. https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical. | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1Entry**](GoogleCloudDatacatalogV1beta1Entry.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

