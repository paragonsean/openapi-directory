# ProjectsApi

All URIs are relative to *https://datacatalog.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**datacatalogProjectsLocationsEntryGroupsCreate**](ProjectsApi.md#datacatalogProjectsLocationsEntryGroupsCreate) | **POST** /v1beta1/{parent}/entryGroups |  |
| [**datacatalogProjectsLocationsEntryGroupsEntriesCreate**](ProjectsApi.md#datacatalogProjectsLocationsEntryGroupsEntriesCreate) | **POST** /v1beta1/{parent}/entries |  |
| [**datacatalogProjectsLocationsEntryGroupsEntriesList**](ProjectsApi.md#datacatalogProjectsLocationsEntryGroupsEntriesList) | **GET** /v1beta1/{parent}/entries |  |
| [**datacatalogProjectsLocationsEntryGroupsList**](ProjectsApi.md#datacatalogProjectsLocationsEntryGroupsList) | **GET** /v1beta1/{parent}/entryGroups |  |
| [**datacatalogProjectsLocationsEntryGroupsTagsCreate**](ProjectsApi.md#datacatalogProjectsLocationsEntryGroupsTagsCreate) | **POST** /v1beta1/{parent}/tags |  |
| [**datacatalogProjectsLocationsEntryGroupsTagsList**](ProjectsApi.md#datacatalogProjectsLocationsEntryGroupsTagsList) | **GET** /v1beta1/{parent}/tags |  |
| [**datacatalogProjectsLocationsTagTemplatesCreate**](ProjectsApi.md#datacatalogProjectsLocationsTagTemplatesCreate) | **POST** /v1beta1/{parent}/tagTemplates |  |
| [**datacatalogProjectsLocationsTagTemplatesFieldsCreate**](ProjectsApi.md#datacatalogProjectsLocationsTagTemplatesFieldsCreate) | **POST** /v1beta1/{parent}/fields |  |
| [**datacatalogProjectsLocationsTagTemplatesFieldsEnumValuesRename**](ProjectsApi.md#datacatalogProjectsLocationsTagTemplatesFieldsEnumValuesRename) | **POST** /v1beta1/{name}:rename |  |
| [**datacatalogProjectsLocationsTaxonomiesCreate**](ProjectsApi.md#datacatalogProjectsLocationsTaxonomiesCreate) | **POST** /v1beta1/{parent}/taxonomies |  |
| [**datacatalogProjectsLocationsTaxonomiesExport**](ProjectsApi.md#datacatalogProjectsLocationsTaxonomiesExport) | **GET** /v1beta1/{parent}/taxonomies:export |  |
| [**datacatalogProjectsLocationsTaxonomiesImport**](ProjectsApi.md#datacatalogProjectsLocationsTaxonomiesImport) | **POST** /v1beta1/{parent}/taxonomies:import |  |
| [**datacatalogProjectsLocationsTaxonomiesList**](ProjectsApi.md#datacatalogProjectsLocationsTaxonomiesList) | **GET** /v1beta1/{parent}/taxonomies |  |
| [**datacatalogProjectsLocationsTaxonomiesPolicyTagsCreate**](ProjectsApi.md#datacatalogProjectsLocationsTaxonomiesPolicyTagsCreate) | **POST** /v1beta1/{parent}/policyTags |  |
| [**datacatalogProjectsLocationsTaxonomiesPolicyTagsDelete**](ProjectsApi.md#datacatalogProjectsLocationsTaxonomiesPolicyTagsDelete) | **DELETE** /v1beta1/{name} |  |
| [**datacatalogProjectsLocationsTaxonomiesPolicyTagsGet**](ProjectsApi.md#datacatalogProjectsLocationsTaxonomiesPolicyTagsGet) | **GET** /v1beta1/{name} |  |
| [**datacatalogProjectsLocationsTaxonomiesPolicyTagsGetIamPolicy**](ProjectsApi.md#datacatalogProjectsLocationsTaxonomiesPolicyTagsGetIamPolicy) | **POST** /v1beta1/{resource}:getIamPolicy |  |
| [**datacatalogProjectsLocationsTaxonomiesPolicyTagsList**](ProjectsApi.md#datacatalogProjectsLocationsTaxonomiesPolicyTagsList) | **GET** /v1beta1/{parent}/policyTags |  |
| [**datacatalogProjectsLocationsTaxonomiesPolicyTagsPatch**](ProjectsApi.md#datacatalogProjectsLocationsTaxonomiesPolicyTagsPatch) | **PATCH** /v1beta1/{name} |  |
| [**datacatalogProjectsLocationsTaxonomiesPolicyTagsSetIamPolicy**](ProjectsApi.md#datacatalogProjectsLocationsTaxonomiesPolicyTagsSetIamPolicy) | **POST** /v1beta1/{resource}:setIamPolicy |  |
| [**datacatalogProjectsLocationsTaxonomiesPolicyTagsTestIamPermissions**](ProjectsApi.md#datacatalogProjectsLocationsTaxonomiesPolicyTagsTestIamPermissions) | **POST** /v1beta1/{resource}:testIamPermissions |  |


<a id="datacatalogProjectsLocationsEntryGroupsCreate"></a>
# **datacatalogProjectsLocationsEntryGroupsCreate**
> GoogleCloudDatacatalogV1beta1EntryGroup datacatalogProjectsLocationsEntryGroupsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, entryGroupId, googleCloudDatacatalogV1beta1EntryGroup)



A maximum of 10,000 entry groups may be created per organization across all locations. Users should enable the Data Catalog API in the project identified by the &#x60;parent&#x60; parameter (see [Data Catalog Resource Project] (https://cloud.google.com/data-catalog/docs/concepts/resource-project) for more information).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The name of the project this entry group is in. Example: * projects/{project_id}/locations/{location} Note that this EntryGroup and its child resources may not actually be stored in the location in this name.
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
    String entryGroupId = "entryGroupId_example"; // String | Required. The id of the entry group to create. The id must begin with a letter or underscore, contain only English letters, numbers and underscores, and be at most 64 characters.
    GoogleCloudDatacatalogV1beta1EntryGroup googleCloudDatacatalogV1beta1EntryGroup = new GoogleCloudDatacatalogV1beta1EntryGroup(); // GoogleCloudDatacatalogV1beta1EntryGroup | 
    try {
      GoogleCloudDatacatalogV1beta1EntryGroup result = apiInstance.datacatalogProjectsLocationsEntryGroupsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, entryGroupId, googleCloudDatacatalogV1beta1EntryGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsEntryGroupsCreate");
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
| **parent** | **String**| Required. The name of the project this entry group is in. Example: * projects/{project_id}/locations/{location} Note that this EntryGroup and its child resources may not actually be stored in the location in this name. | |
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
| **entryGroupId** | **String**| Required. The id of the entry group to create. The id must begin with a letter or underscore, contain only English letters, numbers and underscores, and be at most 64 characters. | [optional] |
| **googleCloudDatacatalogV1beta1EntryGroup** | [**GoogleCloudDatacatalogV1beta1EntryGroup**](GoogleCloudDatacatalogV1beta1EntryGroup.md)|  | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1EntryGroup**](GoogleCloudDatacatalogV1beta1EntryGroup.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsEntryGroupsEntriesCreate"></a>
# **datacatalogProjectsLocationsEntryGroupsEntriesCreate**
> GoogleCloudDatacatalogV1beta1Entry datacatalogProjectsLocationsEntryGroupsEntriesCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, entryId, googleCloudDatacatalogV1beta1Entry)



Creates an entry. Only entries of &#39;FILESET&#39; type or user-specified type can be created. Users should enable the Data Catalog API in the project identified by the &#x60;parent&#x60; parameter (see [Data Catalog Resource Project] (https://cloud.google.com/data-catalog/docs/concepts/resource-project) for more information). A maximum of 100,000 entries may be created per entry group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The name of the entry group this entry is in. Example: * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id} Note that this Entry and its child resources may not actually be stored in the location in this name.
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
    String entryId = "entryId_example"; // String | Required. The id of the entry to create.
    GoogleCloudDatacatalogV1beta1Entry googleCloudDatacatalogV1beta1Entry = new GoogleCloudDatacatalogV1beta1Entry(); // GoogleCloudDatacatalogV1beta1Entry | 
    try {
      GoogleCloudDatacatalogV1beta1Entry result = apiInstance.datacatalogProjectsLocationsEntryGroupsEntriesCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, entryId, googleCloudDatacatalogV1beta1Entry);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsEntryGroupsEntriesCreate");
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
| **parent** | **String**| Required. The name of the entry group this entry is in. Example: * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id} Note that this Entry and its child resources may not actually be stored in the location in this name. | |
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
| **entryId** | **String**| Required. The id of the entry to create. | [optional] |
| **googleCloudDatacatalogV1beta1Entry** | [**GoogleCloudDatacatalogV1beta1Entry**](GoogleCloudDatacatalogV1beta1Entry.md)|  | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1Entry**](GoogleCloudDatacatalogV1beta1Entry.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsEntryGroupsEntriesList"></a>
# **datacatalogProjectsLocationsEntryGroupsEntriesList**
> GoogleCloudDatacatalogV1beta1ListEntriesResponse datacatalogProjectsLocationsEntryGroupsEntriesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, readMask)



Lists entries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The name of the entry group that contains the entries, which can be provided in URL format. Example: * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}
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
    Integer pageSize = 56; // Integer | The maximum number of items to return. Default is 10. Max limit is 1000. Throws an invalid argument for `page_size > 1000`.
    String pageToken = "pageToken_example"; // String | Token that specifies which page is requested. If empty, the first page is returned.
    String readMask = "readMask_example"; // String | The fields to return for each Entry. If not set or empty, all fields are returned. For example, setting read_mask to contain only one path \"name\" will cause ListEntries to return a list of Entries with only \"name\" field.
    try {
      GoogleCloudDatacatalogV1beta1ListEntriesResponse result = apiInstance.datacatalogProjectsLocationsEntryGroupsEntriesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, readMask);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsEntryGroupsEntriesList");
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
| **parent** | **String**| Required. The name of the entry group that contains the entries, which can be provided in URL format. Example: * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id} | |
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
| **pageSize** | **Integer**| The maximum number of items to return. Default is 10. Max limit is 1000. Throws an invalid argument for &#x60;page_size &gt; 1000&#x60;. | [optional] |
| **pageToken** | **String**| Token that specifies which page is requested. If empty, the first page is returned. | [optional] |
| **readMask** | **String**| The fields to return for each Entry. If not set or empty, all fields are returned. For example, setting read_mask to contain only one path \&quot;name\&quot; will cause ListEntries to return a list of Entries with only \&quot;name\&quot; field. | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1ListEntriesResponse**](GoogleCloudDatacatalogV1beta1ListEntriesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsEntryGroupsList"></a>
# **datacatalogProjectsLocationsEntryGroupsList**
> GoogleCloudDatacatalogV1beta1ListEntryGroupsResponse datacatalogProjectsLocationsEntryGroupsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Lists entry groups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The name of the location that contains the entry groups, which can be provided in URL format. Example: * projects/{project_id}/locations/{location}
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
    Integer pageSize = 56; // Integer | Optional. The maximum number of items to return. Default is 10. Max limit is 1000. Throws an invalid argument for `page_size > 1000`.
    String pageToken = "pageToken_example"; // String | Optional. Token that specifies which page is requested. If empty, the first page is returned.
    try {
      GoogleCloudDatacatalogV1beta1ListEntryGroupsResponse result = apiInstance.datacatalogProjectsLocationsEntryGroupsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsEntryGroupsList");
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
| **parent** | **String**| Required. The name of the location that contains the entry groups, which can be provided in URL format. Example: * projects/{project_id}/locations/{location} | |
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
| **pageSize** | **Integer**| Optional. The maximum number of items to return. Default is 10. Max limit is 1000. Throws an invalid argument for &#x60;page_size &gt; 1000&#x60;. | [optional] |
| **pageToken** | **String**| Optional. Token that specifies which page is requested. If empty, the first page is returned. | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1ListEntryGroupsResponse**](GoogleCloudDatacatalogV1beta1ListEntryGroupsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsEntryGroupsTagsCreate"></a>
# **datacatalogProjectsLocationsEntryGroupsTagsCreate**
> GoogleCloudDatacatalogV1beta1Tag datacatalogProjectsLocationsEntryGroupsTagsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDatacatalogV1beta1Tag)



Creates a tag on an Entry. Note: The project identified by the &#x60;parent&#x60; parameter for the [tag](https://cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.entryGroups.entries.tags/create#path-parameters) and the [tag template](https://cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.tagTemplates/create#path-parameters) used to create the tag must be from the same organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The name of the resource to attach this tag to. Tags can be attached to Entries. Example: * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id} Note that this Tag and its child resources may not actually be stored in the location in this name.
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
    GoogleCloudDatacatalogV1beta1Tag googleCloudDatacatalogV1beta1Tag = new GoogleCloudDatacatalogV1beta1Tag(); // GoogleCloudDatacatalogV1beta1Tag | 
    try {
      GoogleCloudDatacatalogV1beta1Tag result = apiInstance.datacatalogProjectsLocationsEntryGroupsTagsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDatacatalogV1beta1Tag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsEntryGroupsTagsCreate");
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
| **parent** | **String**| Required. The name of the resource to attach this tag to. Tags can be attached to Entries. Example: * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id} Note that this Tag and its child resources may not actually be stored in the location in this name. | |
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
| **googleCloudDatacatalogV1beta1Tag** | [**GoogleCloudDatacatalogV1beta1Tag**](GoogleCloudDatacatalogV1beta1Tag.md)|  | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1Tag**](GoogleCloudDatacatalogV1beta1Tag.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsEntryGroupsTagsList"></a>
# **datacatalogProjectsLocationsEntryGroupsTagsList**
> GoogleCloudDatacatalogV1beta1ListTagsResponse datacatalogProjectsLocationsEntryGroupsTagsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Lists tags assigned to an Entry. The columns in the response are lowercased.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The name of the Data Catalog resource to list the tags of. The resource could be an Entry or an EntryGroup. Examples: * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id} * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}
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
    Integer pageSize = 56; // Integer | The maximum number of tags to return. Default is 10. Max limit is 1000.
    String pageToken = "pageToken_example"; // String | Token that specifies which page is requested. If empty, the first page is returned.
    try {
      GoogleCloudDatacatalogV1beta1ListTagsResponse result = apiInstance.datacatalogProjectsLocationsEntryGroupsTagsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsEntryGroupsTagsList");
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
| **parent** | **String**| Required. The name of the Data Catalog resource to list the tags of. The resource could be an Entry or an EntryGroup. Examples: * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id} * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id} | |
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
| **pageSize** | **Integer**| The maximum number of tags to return. Default is 10. Max limit is 1000. | [optional] |
| **pageToken** | **String**| Token that specifies which page is requested. If empty, the first page is returned. | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1ListTagsResponse**](GoogleCloudDatacatalogV1beta1ListTagsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsTagTemplatesCreate"></a>
# **datacatalogProjectsLocationsTagTemplatesCreate**
> GoogleCloudDatacatalogV1beta1TagTemplate datacatalogProjectsLocationsTagTemplatesCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, tagTemplateId, googleCloudDatacatalogV1beta1TagTemplate)



Creates a tag template. The user should enable the Data Catalog API in the project identified by the &#x60;parent&#x60; parameter (see [Data Catalog Resource Project](https://cloud.google.com/data-catalog/docs/concepts/resource-project) for more information).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The name of the project and the template location [region](https://cloud.google.com/data-catalog/docs/concepts/regions. Example: * projects/{project_id}/locations/us-central1
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
    String tagTemplateId = "tagTemplateId_example"; // String | Required. The id of the tag template to create.
    GoogleCloudDatacatalogV1beta1TagTemplate googleCloudDatacatalogV1beta1TagTemplate = new GoogleCloudDatacatalogV1beta1TagTemplate(); // GoogleCloudDatacatalogV1beta1TagTemplate | 
    try {
      GoogleCloudDatacatalogV1beta1TagTemplate result = apiInstance.datacatalogProjectsLocationsTagTemplatesCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, tagTemplateId, googleCloudDatacatalogV1beta1TagTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsTagTemplatesCreate");
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
| **parent** | **String**| Required. The name of the project and the template location [region](https://cloud.google.com/data-catalog/docs/concepts/regions. Example: * projects/{project_id}/locations/us-central1 | |
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
| **tagTemplateId** | **String**| Required. The id of the tag template to create. | [optional] |
| **googleCloudDatacatalogV1beta1TagTemplate** | [**GoogleCloudDatacatalogV1beta1TagTemplate**](GoogleCloudDatacatalogV1beta1TagTemplate.md)|  | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1TagTemplate**](GoogleCloudDatacatalogV1beta1TagTemplate.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsTagTemplatesFieldsCreate"></a>
# **datacatalogProjectsLocationsTagTemplatesFieldsCreate**
> GoogleCloudDatacatalogV1beta1TagTemplateField datacatalogProjectsLocationsTagTemplatesFieldsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, tagTemplateFieldId, googleCloudDatacatalogV1beta1TagTemplateField)



Creates a field in a tag template. The user should enable the Data Catalog API in the project identified by the &#x60;parent&#x60; parameter (see [Data Catalog Resource Project](https://cloud.google.com/data-catalog/docs/concepts/resource-project) for more information).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The name of the project and the template location [region](https://cloud.google.com/data-catalog/docs/concepts/regions). Example: * projects/{project_id}/locations/us-central1/tagTemplates/{tag_template_id}
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
    String tagTemplateFieldId = "tagTemplateFieldId_example"; // String | Required. The ID of the tag template field to create. Field ids can contain letters (both uppercase and lowercase), numbers (0-9), underscores (_) and dashes (-). Field IDs must be at least 1 character long and at most 128 characters long. Field IDs must also be unique within their template.
    GoogleCloudDatacatalogV1beta1TagTemplateField googleCloudDatacatalogV1beta1TagTemplateField = new GoogleCloudDatacatalogV1beta1TagTemplateField(); // GoogleCloudDatacatalogV1beta1TagTemplateField | 
    try {
      GoogleCloudDatacatalogV1beta1TagTemplateField result = apiInstance.datacatalogProjectsLocationsTagTemplatesFieldsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, tagTemplateFieldId, googleCloudDatacatalogV1beta1TagTemplateField);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsTagTemplatesFieldsCreate");
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
| **parent** | **String**| Required. The name of the project and the template location [region](https://cloud.google.com/data-catalog/docs/concepts/regions). Example: * projects/{project_id}/locations/us-central1/tagTemplates/{tag_template_id} | |
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
| **tagTemplateFieldId** | **String**| Required. The ID of the tag template field to create. Field ids can contain letters (both uppercase and lowercase), numbers (0-9), underscores (_) and dashes (-). Field IDs must be at least 1 character long and at most 128 characters long. Field IDs must also be unique within their template. | [optional] |
| **googleCloudDatacatalogV1beta1TagTemplateField** | [**GoogleCloudDatacatalogV1beta1TagTemplateField**](GoogleCloudDatacatalogV1beta1TagTemplateField.md)|  | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1TagTemplateField**](GoogleCloudDatacatalogV1beta1TagTemplateField.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsTagTemplatesFieldsEnumValuesRename"></a>
# **datacatalogProjectsLocationsTagTemplatesFieldsEnumValuesRename**
> GoogleCloudDatacatalogV1beta1TagTemplateField datacatalogProjectsLocationsTagTemplatesFieldsEnumValuesRename(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDatacatalogV1beta1RenameTagTemplateFieldEnumValueRequest)



Renames an enum value in a tag template. The enum values have to be unique within one enum field. Thus, an enum value cannot be renamed with a name used in any other enum value within the same enum field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Required. The name of the enum field value. Example: * projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}/fields/{tag_template_field_id}/enumValues/{enum_value_display_name}
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
    GoogleCloudDatacatalogV1beta1RenameTagTemplateFieldEnumValueRequest googleCloudDatacatalogV1beta1RenameTagTemplateFieldEnumValueRequest = new GoogleCloudDatacatalogV1beta1RenameTagTemplateFieldEnumValueRequest(); // GoogleCloudDatacatalogV1beta1RenameTagTemplateFieldEnumValueRequest | 
    try {
      GoogleCloudDatacatalogV1beta1TagTemplateField result = apiInstance.datacatalogProjectsLocationsTagTemplatesFieldsEnumValuesRename(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDatacatalogV1beta1RenameTagTemplateFieldEnumValueRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsTagTemplatesFieldsEnumValuesRename");
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
| **name** | **String**| Required. The name of the enum field value. Example: * projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}/fields/{tag_template_field_id}/enumValues/{enum_value_display_name} | |
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
| **googleCloudDatacatalogV1beta1RenameTagTemplateFieldEnumValueRequest** | [**GoogleCloudDatacatalogV1beta1RenameTagTemplateFieldEnumValueRequest**](GoogleCloudDatacatalogV1beta1RenameTagTemplateFieldEnumValueRequest.md)|  | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1TagTemplateField**](GoogleCloudDatacatalogV1beta1TagTemplateField.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsTaxonomiesCreate"></a>
# **datacatalogProjectsLocationsTaxonomiesCreate**
> GoogleCloudDatacatalogV1beta1Taxonomy datacatalogProjectsLocationsTaxonomiesCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDatacatalogV1beta1Taxonomy)



Creates a taxonomy in the specified project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. Resource name of the project that the taxonomy will belong to.
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
    GoogleCloudDatacatalogV1beta1Taxonomy googleCloudDatacatalogV1beta1Taxonomy = new GoogleCloudDatacatalogV1beta1Taxonomy(); // GoogleCloudDatacatalogV1beta1Taxonomy | 
    try {
      GoogleCloudDatacatalogV1beta1Taxonomy result = apiInstance.datacatalogProjectsLocationsTaxonomiesCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDatacatalogV1beta1Taxonomy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsTaxonomiesCreate");
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
| **parent** | **String**| Required. Resource name of the project that the taxonomy will belong to. | |
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
| **googleCloudDatacatalogV1beta1Taxonomy** | [**GoogleCloudDatacatalogV1beta1Taxonomy**](GoogleCloudDatacatalogV1beta1Taxonomy.md)|  | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1Taxonomy**](GoogleCloudDatacatalogV1beta1Taxonomy.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsTaxonomiesExport"></a>
# **datacatalogProjectsLocationsTaxonomiesExport**
> GoogleCloudDatacatalogV1beta1ExportTaxonomiesResponse datacatalogProjectsLocationsTaxonomiesExport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, serializedTaxonomies, taxonomies)



Exports all taxonomies and their policy tags in a project. This method generates SerializedTaxonomy protos with nested policy tags that can be used as an input for future ImportTaxonomies calls.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. Resource name of the project that taxonomies to be exported will share.
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
    Boolean serializedTaxonomies = true; // Boolean | Export taxonomies as serialized taxonomies.
    List<String> taxonomies = Arrays.asList(); // List<String> | Required. Resource names of the taxonomies to be exported.
    try {
      GoogleCloudDatacatalogV1beta1ExportTaxonomiesResponse result = apiInstance.datacatalogProjectsLocationsTaxonomiesExport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, serializedTaxonomies, taxonomies);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsTaxonomiesExport");
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
| **parent** | **String**| Required. Resource name of the project that taxonomies to be exported will share. | |
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
| **serializedTaxonomies** | **Boolean**| Export taxonomies as serialized taxonomies. | [optional] |
| **taxonomies** | [**List&lt;String&gt;**](String.md)| Required. Resource names of the taxonomies to be exported. | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1ExportTaxonomiesResponse**](GoogleCloudDatacatalogV1beta1ExportTaxonomiesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsTaxonomiesImport"></a>
# **datacatalogProjectsLocationsTaxonomiesImport**
> GoogleCloudDatacatalogV1beta1ImportTaxonomiesResponse datacatalogProjectsLocationsTaxonomiesImport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDatacatalogV1beta1ImportTaxonomiesRequest)



Imports all taxonomies and their policy tags to a project as new taxonomies. This method provides a bulk taxonomy / policy tag creation using nested proto structure.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. Resource name of project that the imported taxonomies will belong to.
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
    GoogleCloudDatacatalogV1beta1ImportTaxonomiesRequest googleCloudDatacatalogV1beta1ImportTaxonomiesRequest = new GoogleCloudDatacatalogV1beta1ImportTaxonomiesRequest(); // GoogleCloudDatacatalogV1beta1ImportTaxonomiesRequest | 
    try {
      GoogleCloudDatacatalogV1beta1ImportTaxonomiesResponse result = apiInstance.datacatalogProjectsLocationsTaxonomiesImport(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDatacatalogV1beta1ImportTaxonomiesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsTaxonomiesImport");
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
| **parent** | **String**| Required. Resource name of project that the imported taxonomies will belong to. | |
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
| **googleCloudDatacatalogV1beta1ImportTaxonomiesRequest** | [**GoogleCloudDatacatalogV1beta1ImportTaxonomiesRequest**](GoogleCloudDatacatalogV1beta1ImportTaxonomiesRequest.md)|  | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1ImportTaxonomiesResponse**](GoogleCloudDatacatalogV1beta1ImportTaxonomiesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsTaxonomiesList"></a>
# **datacatalogProjectsLocationsTaxonomiesList**
> GoogleCloudDatacatalogV1beta1ListTaxonomiesResponse datacatalogProjectsLocationsTaxonomiesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken)



Lists all taxonomies in a project in a particular location that the caller has permission to view.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. Resource name of the project to list the taxonomies of.
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
    String filter = "filter_example"; // String | Supported field for filter is 'service' and value is 'dataplex'. Eg: service=dataplex.
    Integer pageSize = 56; // Integer | The maximum number of items to return. Must be a value between 1 and 1000. If not set, defaults to 50.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous list request, if any. If not set, defaults to an empty string.
    try {
      GoogleCloudDatacatalogV1beta1ListTaxonomiesResponse result = apiInstance.datacatalogProjectsLocationsTaxonomiesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsTaxonomiesList");
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
| **parent** | **String**| Required. Resource name of the project to list the taxonomies of. | |
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
| **filter** | **String**| Supported field for filter is &#39;service&#39; and value is &#39;dataplex&#39;. Eg: service&#x3D;dataplex. | [optional] |
| **pageSize** | **Integer**| The maximum number of items to return. Must be a value between 1 and 1000. If not set, defaults to 50. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous list request, if any. If not set, defaults to an empty string. | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1ListTaxonomiesResponse**](GoogleCloudDatacatalogV1beta1ListTaxonomiesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsTaxonomiesPolicyTagsCreate"></a>
# **datacatalogProjectsLocationsTaxonomiesPolicyTagsCreate**
> GoogleCloudDatacatalogV1beta1PolicyTag datacatalogProjectsLocationsTaxonomiesPolicyTagsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDatacatalogV1beta1PolicyTag)



Creates a policy tag in the specified taxonomy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. Resource name of the taxonomy that the policy tag will belong to.
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
    GoogleCloudDatacatalogV1beta1PolicyTag googleCloudDatacatalogV1beta1PolicyTag = new GoogleCloudDatacatalogV1beta1PolicyTag(); // GoogleCloudDatacatalogV1beta1PolicyTag | 
    try {
      GoogleCloudDatacatalogV1beta1PolicyTag result = apiInstance.datacatalogProjectsLocationsTaxonomiesPolicyTagsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDatacatalogV1beta1PolicyTag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsTaxonomiesPolicyTagsCreate");
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
| **parent** | **String**| Required. Resource name of the taxonomy that the policy tag will belong to. | |
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
| **googleCloudDatacatalogV1beta1PolicyTag** | [**GoogleCloudDatacatalogV1beta1PolicyTag**](GoogleCloudDatacatalogV1beta1PolicyTag.md)|  | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1PolicyTag**](GoogleCloudDatacatalogV1beta1PolicyTag.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsTaxonomiesPolicyTagsDelete"></a>
# **datacatalogProjectsLocationsTaxonomiesPolicyTagsDelete**
> Object datacatalogProjectsLocationsTaxonomiesPolicyTagsDelete(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, force)



Deletes a policy tag. Also deletes all of its descendant policy tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Required. Resource name of the policy tag to be deleted. All of its descendant policy tags will also be deleted.
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
    Boolean force = true; // Boolean | Required. Currently, this field must always be set to `true`. This confirms the deletion of this field from any tags using this field. `force = false` will be supported in the future.
    try {
      Object result = apiInstance.datacatalogProjectsLocationsTaxonomiesPolicyTagsDelete(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, force);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsTaxonomiesPolicyTagsDelete");
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
| **name** | **String**| Required. Resource name of the policy tag to be deleted. All of its descendant policy tags will also be deleted. | |
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
| **force** | **Boolean**| Required. Currently, this field must always be set to &#x60;true&#x60;. This confirms the deletion of this field from any tags using this field. &#x60;force &#x3D; false&#x60; will be supported in the future. | [optional] |

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsTaxonomiesPolicyTagsGet"></a>
# **datacatalogProjectsLocationsTaxonomiesPolicyTagsGet**
> GoogleCloudDatacatalogV1beta1PolicyTag datacatalogProjectsLocationsTaxonomiesPolicyTagsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, readMask)



Gets a policy tag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Required. Resource name of the requested policy tag.
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
    String readMask = "readMask_example"; // String | The fields to return. If not set or empty, all fields are returned.
    try {
      GoogleCloudDatacatalogV1beta1PolicyTag result = apiInstance.datacatalogProjectsLocationsTaxonomiesPolicyTagsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, readMask);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsTaxonomiesPolicyTagsGet");
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
| **name** | **String**| Required. Resource name of the requested policy tag. | |
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
| **readMask** | **String**| The fields to return. If not set or empty, all fields are returned. | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1PolicyTag**](GoogleCloudDatacatalogV1beta1PolicyTag.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsTaxonomiesPolicyTagsGetIamPolicy"></a>
# **datacatalogProjectsLocationsTaxonomiesPolicyTagsGetIamPolicy**
> Policy datacatalogProjectsLocationsTaxonomiesPolicyTagsGetIamPolicy(resource, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, getIamPolicyRequest)



Gets the IAM policy for a taxonomy or a policy tag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String resource = "resource_example"; // String | REQUIRED: The resource for which the policy is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
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
    GetIamPolicyRequest getIamPolicyRequest = new GetIamPolicyRequest(); // GetIamPolicyRequest | 
    try {
      Policy result = apiInstance.datacatalogProjectsLocationsTaxonomiesPolicyTagsGetIamPolicy(resource, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, getIamPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsTaxonomiesPolicyTagsGetIamPolicy");
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
| **resource** | **String**| REQUIRED: The resource for which the policy is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field. | |
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
| **getIamPolicyRequest** | [**GetIamPolicyRequest**](GetIamPolicyRequest.md)|  | [optional] |

### Return type

[**Policy**](Policy.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsTaxonomiesPolicyTagsList"></a>
# **datacatalogProjectsLocationsTaxonomiesPolicyTagsList**
> GoogleCloudDatacatalogV1beta1ListPolicyTagsResponse datacatalogProjectsLocationsTaxonomiesPolicyTagsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Lists all policy tags in a taxonomy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Required. Resource name of the taxonomy to list the policy tags of.
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
    Integer pageSize = 56; // Integer | The maximum number of items to return. Must be a value between 1 and 1000. If not set, defaults to 50.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous List request, if any. If not set, defaults to an empty string.
    try {
      GoogleCloudDatacatalogV1beta1ListPolicyTagsResponse result = apiInstance.datacatalogProjectsLocationsTaxonomiesPolicyTagsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsTaxonomiesPolicyTagsList");
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
| **parent** | **String**| Required. Resource name of the taxonomy to list the policy tags of. | |
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
| **pageSize** | **Integer**| The maximum number of items to return. Must be a value between 1 and 1000. If not set, defaults to 50. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous List request, if any. If not set, defaults to an empty string. | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1ListPolicyTagsResponse**](GoogleCloudDatacatalogV1beta1ListPolicyTagsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsTaxonomiesPolicyTagsPatch"></a>
# **datacatalogProjectsLocationsTaxonomiesPolicyTagsPatch**
> GoogleCloudDatacatalogV1beta1PolicyTag datacatalogProjectsLocationsTaxonomiesPolicyTagsPatch(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, updateMask, googleCloudDatacatalogV1beta1PolicyTag)



Updates a policy tag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Identifier. Resource name of this policy tag, whose format is: \"projects/{project_number}/locations/{location_id}/taxonomies/{taxonomy_id}/policyTags/{id}\".
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
    String updateMask = "updateMask_example"; // String | The update mask applies to the resource. Only display_name, description and parent_policy_tag can be updated and thus can be listed in the mask. If update_mask is not provided, all allowed fields (i.e. display_name, description and parent) will be updated. For more information including the `FieldMask` definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask If not set, defaults to all of the fields that are allowed to update.
    GoogleCloudDatacatalogV1beta1PolicyTag googleCloudDatacatalogV1beta1PolicyTag = new GoogleCloudDatacatalogV1beta1PolicyTag(); // GoogleCloudDatacatalogV1beta1PolicyTag | 
    try {
      GoogleCloudDatacatalogV1beta1PolicyTag result = apiInstance.datacatalogProjectsLocationsTaxonomiesPolicyTagsPatch(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, updateMask, googleCloudDatacatalogV1beta1PolicyTag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsTaxonomiesPolicyTagsPatch");
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
| **name** | **String**| Identifier. Resource name of this policy tag, whose format is: \&quot;projects/{project_number}/locations/{location_id}/taxonomies/{taxonomy_id}/policyTags/{id}\&quot;. | |
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
| **updateMask** | **String**| The update mask applies to the resource. Only display_name, description and parent_policy_tag can be updated and thus can be listed in the mask. If update_mask is not provided, all allowed fields (i.e. display_name, description and parent) will be updated. For more information including the &#x60;FieldMask&#x60; definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask If not set, defaults to all of the fields that are allowed to update. | [optional] |
| **googleCloudDatacatalogV1beta1PolicyTag** | [**GoogleCloudDatacatalogV1beta1PolicyTag**](GoogleCloudDatacatalogV1beta1PolicyTag.md)|  | [optional] |

### Return type

[**GoogleCloudDatacatalogV1beta1PolicyTag**](GoogleCloudDatacatalogV1beta1PolicyTag.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsTaxonomiesPolicyTagsSetIamPolicy"></a>
# **datacatalogProjectsLocationsTaxonomiesPolicyTagsSetIamPolicy**
> Policy datacatalogProjectsLocationsTaxonomiesPolicyTagsSetIamPolicy(resource, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, setIamPolicyRequest)



Sets the IAM policy for a taxonomy or a policy tag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String resource = "resource_example"; // String | REQUIRED: The resource for which the policy is being specified. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
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
    SetIamPolicyRequest setIamPolicyRequest = new SetIamPolicyRequest(); // SetIamPolicyRequest | 
    try {
      Policy result = apiInstance.datacatalogProjectsLocationsTaxonomiesPolicyTagsSetIamPolicy(resource, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, setIamPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsTaxonomiesPolicyTagsSetIamPolicy");
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
| **resource** | **String**| REQUIRED: The resource for which the policy is being specified. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field. | |
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
| **setIamPolicyRequest** | [**SetIamPolicyRequest**](SetIamPolicyRequest.md)|  | [optional] |

### Return type

[**Policy**](Policy.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="datacatalogProjectsLocationsTaxonomiesPolicyTagsTestIamPermissions"></a>
# **datacatalogProjectsLocationsTaxonomiesPolicyTagsTestIamPermissions**
> TestIamPermissionsResponse datacatalogProjectsLocationsTaxonomiesPolicyTagsTestIamPermissions(resource, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, testIamPermissionsRequest)



Returns the permissions that a caller has on the specified taxonomy or policy tag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String resource = "resource_example"; // String | REQUIRED: The resource for which the policy detail is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
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
    TestIamPermissionsRequest testIamPermissionsRequest = new TestIamPermissionsRequest(); // TestIamPermissionsRequest | 
    try {
      TestIamPermissionsResponse result = apiInstance.datacatalogProjectsLocationsTaxonomiesPolicyTagsTestIamPermissions(resource, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, testIamPermissionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#datacatalogProjectsLocationsTaxonomiesPolicyTagsTestIamPermissions");
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
| **resource** | **String**| REQUIRED: The resource for which the policy detail is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field. | |
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
| **testIamPermissionsRequest** | [**TestIamPermissionsRequest**](TestIamPermissionsRequest.md)|  | [optional] |

### Return type

[**TestIamPermissionsResponse**](TestIamPermissionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

