# OrganizationsApi

All URIs are relative to *https://cloudprivatecatalog.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cloudprivatecatalogOrganizationsCatalogsSearch**](OrganizationsApi.md#cloudprivatecatalogOrganizationsCatalogsSearch) | **GET** /v1beta1/{resource}/catalogs:search |  |
| [**cloudprivatecatalogOrganizationsProductsSearch**](OrganizationsApi.md#cloudprivatecatalogOrganizationsProductsSearch) | **GET** /v1beta1/{resource}/products:search |  |
| [**cloudprivatecatalogOrganizationsVersionsSearch**](OrganizationsApi.md#cloudprivatecatalogOrganizationsVersionsSearch) | **GET** /v1beta1/{resource}/versions:search |  |


<a id="cloudprivatecatalogOrganizationsCatalogsSearch"></a>
# **cloudprivatecatalogOrganizationsCatalogsSearch**
> GoogleCloudPrivatecatalogV1beta1SearchCatalogsResponse cloudprivatecatalogOrganizationsCatalogsSearch(resource, $xgafv, oauthToken, paramCallback, alt, key, accessToken, uploadProtocol, prettyPrint, quotaUser, fields, uploadType, pageSize, pageToken, query)



Search Catalog resources that consumers have access to, within the scope of the consumer cloud resource hierarchy context.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudprivatecatalog.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String resource = "resource_example"; // String | Required. The name of the resource context. It can be in following formats:  * `projects/{project_id}` * `folders/{folder_id}` * `organizations/{organization_id}`
    String $xgafv = "1"; // String | V1 error format.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String alt = "json"; // String | Data format for response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of entries that are requested.
    String pageToken = "pageToken_example"; // String | A pagination token returned from a previous call to SearchCatalogs that indicates where this listing should continue from. This field is optional.
    String query = "query_example"; // String | The query to filter the catalogs. The supported queries are:  * Get a single catalog: `name=catalogs/{catalog_id}`
    try {
      GoogleCloudPrivatecatalogV1beta1SearchCatalogsResponse result = apiInstance.cloudprivatecatalogOrganizationsCatalogsSearch(resource, $xgafv, oauthToken, paramCallback, alt, key, accessToken, uploadProtocol, prettyPrint, quotaUser, fields, uploadType, pageSize, pageToken, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#cloudprivatecatalogOrganizationsCatalogsSearch");
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
| **resource** | **String**| Required. The name of the resource context. It can be in following formats:  * &#x60;projects/{project_id}&#x60; * &#x60;folders/{folder_id}&#x60; * &#x60;organizations/{organization_id}&#x60; | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **paramCallback** | **String**| JSONP | [optional] |
| **alt** | **String**| Data format for response. | [optional] [default to json] [enum: json, media, proto] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of entries that are requested. | [optional] |
| **pageToken** | **String**| A pagination token returned from a previous call to SearchCatalogs that indicates where this listing should continue from. This field is optional. | [optional] |
| **query** | **String**| The query to filter the catalogs. The supported queries are:  * Get a single catalog: &#x60;name&#x3D;catalogs/{catalog_id}&#x60; | [optional] |

### Return type

[**GoogleCloudPrivatecatalogV1beta1SearchCatalogsResponse**](GoogleCloudPrivatecatalogV1beta1SearchCatalogsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudprivatecatalogOrganizationsProductsSearch"></a>
# **cloudprivatecatalogOrganizationsProductsSearch**
> GoogleCloudPrivatecatalogV1beta1SearchProductsResponse cloudprivatecatalogOrganizationsProductsSearch(resource, $xgafv, oauthToken, paramCallback, alt, key, accessToken, uploadProtocol, prettyPrint, quotaUser, fields, uploadType, pageSize, pageToken, query)



Search Product resources that consumers have access to, within the scope of the consumer cloud resource hierarchy context.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudprivatecatalog.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String resource = "resource_example"; // String | Required. The name of the resource context. See SearchCatalogsRequest.resource for details.
    String $xgafv = "1"; // String | V1 error format.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String alt = "json"; // String | Data format for response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of entries that are requested.
    String pageToken = "pageToken_example"; // String | A pagination token returned from a previous call to SearchProducts that indicates where this listing should continue from. This field is optional.
    String query = "query_example"; // String | The query to filter the products.  The supported queries are: * List products of all catalogs: empty * List products under a catalog: `parent=catalogs/{catalog_id}` * Get a product by name: `name=catalogs/{catalog_id}/products/{product_id}`
    try {
      GoogleCloudPrivatecatalogV1beta1SearchProductsResponse result = apiInstance.cloudprivatecatalogOrganizationsProductsSearch(resource, $xgafv, oauthToken, paramCallback, alt, key, accessToken, uploadProtocol, prettyPrint, quotaUser, fields, uploadType, pageSize, pageToken, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#cloudprivatecatalogOrganizationsProductsSearch");
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
| **resource** | **String**| Required. The name of the resource context. See SearchCatalogsRequest.resource for details. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **paramCallback** | **String**| JSONP | [optional] |
| **alt** | **String**| Data format for response. | [optional] [default to json] [enum: json, media, proto] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of entries that are requested. | [optional] |
| **pageToken** | **String**| A pagination token returned from a previous call to SearchProducts that indicates where this listing should continue from. This field is optional. | [optional] |
| **query** | **String**| The query to filter the products.  The supported queries are: * List products of all catalogs: empty * List products under a catalog: &#x60;parent&#x3D;catalogs/{catalog_id}&#x60; * Get a product by name: &#x60;name&#x3D;catalogs/{catalog_id}/products/{product_id}&#x60; | [optional] |

### Return type

[**GoogleCloudPrivatecatalogV1beta1SearchProductsResponse**](GoogleCloudPrivatecatalogV1beta1SearchProductsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudprivatecatalogOrganizationsVersionsSearch"></a>
# **cloudprivatecatalogOrganizationsVersionsSearch**
> GoogleCloudPrivatecatalogV1beta1SearchVersionsResponse cloudprivatecatalogOrganizationsVersionsSearch(resource, $xgafv, oauthToken, paramCallback, alt, key, accessToken, uploadProtocol, prettyPrint, quotaUser, fields, uploadType, pageSize, pageToken, query)



Search Version resources that consumers have access to, within the scope of the consumer cloud resource hierarchy context.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudprivatecatalog.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String resource = "resource_example"; // String | Required. The name of the resource context. See SearchCatalogsRequest.resource for details.
    String $xgafv = "1"; // String | V1 error format.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String alt = "json"; // String | Data format for response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of entries that are requested.
    String pageToken = "pageToken_example"; // String | A pagination token returned from a previous call to SearchVersions that indicates where this listing should continue from. This field is optional.
    String query = "query_example"; // String | The query to filter the versions. Required.  The supported queries are: * List versions under a product: `parent=catalogs/{catalog_id}/products/{product_id}` * Get a version by name: `name=catalogs/{catalog_id}/products/{product_id}/versions/{version_id}`
    try {
      GoogleCloudPrivatecatalogV1beta1SearchVersionsResponse result = apiInstance.cloudprivatecatalogOrganizationsVersionsSearch(resource, $xgafv, oauthToken, paramCallback, alt, key, accessToken, uploadProtocol, prettyPrint, quotaUser, fields, uploadType, pageSize, pageToken, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#cloudprivatecatalogOrganizationsVersionsSearch");
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
| **resource** | **String**| Required. The name of the resource context. See SearchCatalogsRequest.resource for details. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **paramCallback** | **String**| JSONP | [optional] |
| **alt** | **String**| Data format for response. | [optional] [default to json] [enum: json, media, proto] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of entries that are requested. | [optional] |
| **pageToken** | **String**| A pagination token returned from a previous call to SearchVersions that indicates where this listing should continue from. This field is optional. | [optional] |
| **query** | **String**| The query to filter the versions. Required.  The supported queries are: * List versions under a product: &#x60;parent&#x3D;catalogs/{catalog_id}/products/{product_id}&#x60; * Get a version by name: &#x60;name&#x3D;catalogs/{catalog_id}/products/{product_id}/versions/{version_id}&#x60; | [optional] |

### Return type

[**GoogleCloudPrivatecatalogV1beta1SearchVersionsResponse**](GoogleCloudPrivatecatalogV1beta1SearchVersionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

