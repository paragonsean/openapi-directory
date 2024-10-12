# EntriesApi

All URIs are relative to *https://datacatalog.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**datacatalogEntriesLookup**](EntriesApi.md#datacatalogEntriesLookup) | **GET** /v1/entries:lookup |  |


<a id="datacatalogEntriesLookup"></a>
# **datacatalogEntriesLookup**
> GoogleCloudDatacatalogV1Entry datacatalogEntriesLookup($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fullyQualifiedName, linkedResource, location, project, sqlResource)



Gets an entry by its target resource name. The resource name comes from the source Google Cloud Platform service.

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
    String fullyQualifiedName = "fullyQualifiedName_example"; // String | [Fully Qualified Name (FQN)](https://cloud.google.com//data-catalog/docs/fully-qualified-names) of the resource. FQNs take two forms: * For non-regionalized resources: `{SYSTEM}:{PROJECT}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}` * For regionalized resources: `{SYSTEM}:{PROJECT}.{LOCATION_ID}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}` Example for a DPMS table: `dataproc_metastore:{PROJECT_ID}.{LOCATION_ID}.{INSTANCE_ID}.{DATABASE_ID}.{TABLE_ID}`
    String linkedResource = "linkedResource_example"; // String | The full name of the Google Cloud Platform resource the Data Catalog entry represents. For more information, see [Full Resource Name] (https://cloud.google.com/apis/design/resource_names#full_resource_name). Full names are case-sensitive. For example: * `//bigquery.googleapis.com/projects/{PROJECT_ID}/datasets/{DATASET_ID}/tables/{TABLE_ID}` * `//pubsub.googleapis.com/projects/{PROJECT_ID}/topics/{TOPIC_ID}`
    String location = "location_example"; // String | Location where the lookup should be performed. Required to lookup entry that is not a part of `DPMS` or `DATAPLEX` `integrated_system` using its `fully_qualified_name`. Ignored in other cases.
    String project = "project_example"; // String | Project where the lookup should be performed. Required to lookup entry that is not a part of `DPMS` or `DATAPLEX` `integrated_system` using its `fully_qualified_name`. Ignored in other cases.
    String sqlResource = "sqlResource_example"; // String | The SQL name of the entry. SQL names are case-sensitive. Examples: * `pubsub.topic.{PROJECT_ID}.{TOPIC_ID}` * `pubsub.topic.{PROJECT_ID}.`\\``{TOPIC.ID.SEPARATED.WITH.DOTS}`\\` * `bigquery.table.{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}` * `bigquery.dataset.{PROJECT_ID}.{DATASET_ID}` * `datacatalog.entry.{PROJECT_ID}.{LOCATION_ID}.{ENTRY_GROUP_ID}.{ENTRY_ID}` Identifiers (`*_ID`) should comply with the [Lexical structure in Standard SQL] (https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical).
    try {
      GoogleCloudDatacatalogV1Entry result = apiInstance.datacatalogEntriesLookup($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, fullyQualifiedName, linkedResource, location, project, sqlResource);
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
| **fullyQualifiedName** | **String**| [Fully Qualified Name (FQN)](https://cloud.google.com//data-catalog/docs/fully-qualified-names) of the resource. FQNs take two forms: * For non-regionalized resources: &#x60;{SYSTEM}:{PROJECT}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}&#x60; * For regionalized resources: &#x60;{SYSTEM}:{PROJECT}.{LOCATION_ID}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}&#x60; Example for a DPMS table: &#x60;dataproc_metastore:{PROJECT_ID}.{LOCATION_ID}.{INSTANCE_ID}.{DATABASE_ID}.{TABLE_ID}&#x60; | [optional] |
| **linkedResource** | **String**| The full name of the Google Cloud Platform resource the Data Catalog entry represents. For more information, see [Full Resource Name] (https://cloud.google.com/apis/design/resource_names#full_resource_name). Full names are case-sensitive. For example: * &#x60;//bigquery.googleapis.com/projects/{PROJECT_ID}/datasets/{DATASET_ID}/tables/{TABLE_ID}&#x60; * &#x60;//pubsub.googleapis.com/projects/{PROJECT_ID}/topics/{TOPIC_ID}&#x60; | [optional] |
| **location** | **String**| Location where the lookup should be performed. Required to lookup entry that is not a part of &#x60;DPMS&#x60; or &#x60;DATAPLEX&#x60; &#x60;integrated_system&#x60; using its &#x60;fully_qualified_name&#x60;. Ignored in other cases. | [optional] |
| **project** | **String**| Project where the lookup should be performed. Required to lookup entry that is not a part of &#x60;DPMS&#x60; or &#x60;DATAPLEX&#x60; &#x60;integrated_system&#x60; using its &#x60;fully_qualified_name&#x60;. Ignored in other cases. | [optional] |
| **sqlResource** | **String**| The SQL name of the entry. SQL names are case-sensitive. Examples: * &#x60;pubsub.topic.{PROJECT_ID}.{TOPIC_ID}&#x60; * &#x60;pubsub.topic.{PROJECT_ID}.&#x60;\\&#x60;&#x60;{TOPIC.ID.SEPARATED.WITH.DOTS}&#x60;\\&#x60; * &#x60;bigquery.table.{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}&#x60; * &#x60;bigquery.dataset.{PROJECT_ID}.{DATASET_ID}&#x60; * &#x60;datacatalog.entry.{PROJECT_ID}.{LOCATION_ID}.{ENTRY_GROUP_ID}.{ENTRY_ID}&#x60; Identifiers (&#x60;*_ID&#x60;) should comply with the [Lexical structure in Standard SQL] (https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical). | [optional] |

### Return type

[**GoogleCloudDatacatalogV1Entry**](GoogleCloudDatacatalogV1Entry.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

