# LicenseAssignmentsApi

All URIs are relative to *https://licensing.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**licensingLicenseAssignmentsDelete**](LicenseAssignmentsApi.md#licensingLicenseAssignmentsDelete) | **DELETE** /apps/licensing/v1/product/{productId}/sku/{skuId}/user/{userId} |  |
| [**licensingLicenseAssignmentsGet**](LicenseAssignmentsApi.md#licensingLicenseAssignmentsGet) | **GET** /apps/licensing/v1/product/{productId}/sku/{skuId}/user/{userId} |  |
| [**licensingLicenseAssignmentsInsert**](LicenseAssignmentsApi.md#licensingLicenseAssignmentsInsert) | **POST** /apps/licensing/v1/product/{productId}/sku/{skuId}/user |  |
| [**licensingLicenseAssignmentsListForProduct**](LicenseAssignmentsApi.md#licensingLicenseAssignmentsListForProduct) | **GET** /apps/licensing/v1/product/{productId}/users |  |
| [**licensingLicenseAssignmentsListForProductAndSku**](LicenseAssignmentsApi.md#licensingLicenseAssignmentsListForProductAndSku) | **GET** /apps/licensing/v1/product/{productId}/sku/{skuId}/users |  |
| [**licensingLicenseAssignmentsPatch**](LicenseAssignmentsApi.md#licensingLicenseAssignmentsPatch) | **PATCH** /apps/licensing/v1/product/{productId}/sku/{skuId}/user/{userId} |  |
| [**licensingLicenseAssignmentsUpdate**](LicenseAssignmentsApi.md#licensingLicenseAssignmentsUpdate) | **PUT** /apps/licensing/v1/product/{productId}/sku/{skuId}/user/{userId} |  |


<a id="licensingLicenseAssignmentsDelete"></a>
# **licensingLicenseAssignmentsDelete**
> Object licensingLicenseAssignmentsDelete(productId, skuId, userId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Revoke a license.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://licensing.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LicenseAssignmentsApi apiInstance = new LicenseAssignmentsApi(defaultClient);
    String productId = "productId_example"; // String | A product's unique identifier. For more information about products in this version of the API, see Products and SKUs.
    String skuId = "skuId_example"; // String | A product SKU's unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
    String userId = "userId_example"; // String | The user's current primary email address. If the user's email address changes, use the new email address in your API requests. Since a `userId` is subject to change, do not use a `userId` value as a key for persistent data. This key could break if the current user's email address changes. If the `userId` is suspended, the license status changes.
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
      Object result = apiInstance.licensingLicenseAssignmentsDelete(productId, skuId, userId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseAssignmentsApi#licensingLicenseAssignmentsDelete");
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
| **productId** | **String**| A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs. | |
| **skuId** | **String**| A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs. | |
| **userId** | **String**| The user&#39;s current primary email address. If the user&#39;s email address changes, use the new email address in your API requests. Since a &#x60;userId&#x60; is subject to change, do not use a &#x60;userId&#x60; value as a key for persistent data. This key could break if the current user&#39;s email address changes. If the &#x60;userId&#x60; is suspended, the license status changes. | |
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

<a id="licensingLicenseAssignmentsGet"></a>
# **licensingLicenseAssignmentsGet**
> LicenseAssignment licensingLicenseAssignmentsGet(productId, skuId, userId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Get a specific user&#39;s license by product SKU.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://licensing.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LicenseAssignmentsApi apiInstance = new LicenseAssignmentsApi(defaultClient);
    String productId = "productId_example"; // String | A product's unique identifier. For more information about products in this version of the API, see Products and SKUs.
    String skuId = "skuId_example"; // String | A product SKU's unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
    String userId = "userId_example"; // String | The user's current primary email address. If the user's email address changes, use the new email address in your API requests. Since a `userId` is subject to change, do not use a `userId` value as a key for persistent data. This key could break if the current user's email address changes. If the `userId` is suspended, the license status changes.
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
      LicenseAssignment result = apiInstance.licensingLicenseAssignmentsGet(productId, skuId, userId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseAssignmentsApi#licensingLicenseAssignmentsGet");
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
| **productId** | **String**| A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs. | |
| **skuId** | **String**| A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs. | |
| **userId** | **String**| The user&#39;s current primary email address. If the user&#39;s email address changes, use the new email address in your API requests. Since a &#x60;userId&#x60; is subject to change, do not use a &#x60;userId&#x60; value as a key for persistent data. This key could break if the current user&#39;s email address changes. If the &#x60;userId&#x60; is suspended, the license status changes. | |
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

[**LicenseAssignment**](LicenseAssignment.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="licensingLicenseAssignmentsInsert"></a>
# **licensingLicenseAssignmentsInsert**
> LicenseAssignment licensingLicenseAssignmentsInsert(productId, skuId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, licenseAssignmentInsert)



Assign a license.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://licensing.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LicenseAssignmentsApi apiInstance = new LicenseAssignmentsApi(defaultClient);
    String productId = "productId_example"; // String | A product's unique identifier. For more information about products in this version of the API, see Products and SKUs.
    String skuId = "skuId_example"; // String | A product SKU's unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
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
    LicenseAssignmentInsert licenseAssignmentInsert = new LicenseAssignmentInsert(); // LicenseAssignmentInsert | 
    try {
      LicenseAssignment result = apiInstance.licensingLicenseAssignmentsInsert(productId, skuId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, licenseAssignmentInsert);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseAssignmentsApi#licensingLicenseAssignmentsInsert");
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
| **productId** | **String**| A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs. | |
| **skuId** | **String**| A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs. | |
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
| **licenseAssignmentInsert** | [**LicenseAssignmentInsert**](LicenseAssignmentInsert.md)|  | [optional] |

### Return type

[**LicenseAssignment**](LicenseAssignment.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="licensingLicenseAssignmentsListForProduct"></a>
# **licensingLicenseAssignmentsListForProduct**
> LicenseAssignmentList licensingLicenseAssignmentsListForProduct(productId, customerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, maxResults, pageToken)



List all users assigned licenses for a specific product SKU.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://licensing.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LicenseAssignmentsApi apiInstance = new LicenseAssignmentsApi(defaultClient);
    String productId = "productId_example"; // String | A product's unique identifier. For more information about products in this version of the API, see Products and SKUs.
    String customerId = "customerId_example"; // String | The customer's unique ID as defined in the Admin console, such as `C00000000`. If the customer is suspended, the server returns an error.
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
    Integer maxResults = 56; // Integer | The `maxResults` query string determines how many entries are returned on each page of a large response. This is an optional parameter. The value must be a positive number.
    String pageToken = "pageToken_example"; // String | Token to fetch the next page of data. The `maxResults` query string is related to the `pageToken` since `maxResults` determines how many entries are returned on each page. This is an optional query string. If not specified, the server returns the first page.
    try {
      LicenseAssignmentList result = apiInstance.licensingLicenseAssignmentsListForProduct(productId, customerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, maxResults, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseAssignmentsApi#licensingLicenseAssignmentsListForProduct");
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
| **productId** | **String**| A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs. | |
| **customerId** | **String**| The customer&#39;s unique ID as defined in the Admin console, such as &#x60;C00000000&#x60;. If the customer is suspended, the server returns an error. | |
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
| **maxResults** | **Integer**| The &#x60;maxResults&#x60; query string determines how many entries are returned on each page of a large response. This is an optional parameter. The value must be a positive number. | [optional] |
| **pageToken** | **String**| Token to fetch the next page of data. The &#x60;maxResults&#x60; query string is related to the &#x60;pageToken&#x60; since &#x60;maxResults&#x60; determines how many entries are returned on each page. This is an optional query string. If not specified, the server returns the first page. | [optional] |

### Return type

[**LicenseAssignmentList**](LicenseAssignmentList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="licensingLicenseAssignmentsListForProductAndSku"></a>
# **licensingLicenseAssignmentsListForProductAndSku**
> LicenseAssignmentList licensingLicenseAssignmentsListForProductAndSku(productId, skuId, customerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, maxResults, pageToken)



List all users assigned licenses for a specific product SKU.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://licensing.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LicenseAssignmentsApi apiInstance = new LicenseAssignmentsApi(defaultClient);
    String productId = "productId_example"; // String | A product's unique identifier. For more information about products in this version of the API, see Products and SKUs.
    String skuId = "skuId_example"; // String | A product SKU's unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
    String customerId = "customerId_example"; // String | The customer's unique ID as defined in the Admin console, such as `C00000000`. If the customer is suspended, the server returns an error.
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
    Integer maxResults = 56; // Integer | The `maxResults` query string determines how many entries are returned on each page of a large response. This is an optional parameter. The value must be a positive number.
    String pageToken = "pageToken_example"; // String | Token to fetch the next page of data. The `maxResults` query string is related to the `pageToken` since `maxResults` determines how many entries are returned on each page. This is an optional query string. If not specified, the server returns the first page.
    try {
      LicenseAssignmentList result = apiInstance.licensingLicenseAssignmentsListForProductAndSku(productId, skuId, customerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, maxResults, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseAssignmentsApi#licensingLicenseAssignmentsListForProductAndSku");
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
| **productId** | **String**| A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs. | |
| **skuId** | **String**| A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs. | |
| **customerId** | **String**| The customer&#39;s unique ID as defined in the Admin console, such as &#x60;C00000000&#x60;. If the customer is suspended, the server returns an error. | |
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
| **maxResults** | **Integer**| The &#x60;maxResults&#x60; query string determines how many entries are returned on each page of a large response. This is an optional parameter. The value must be a positive number. | [optional] |
| **pageToken** | **String**| Token to fetch the next page of data. The &#x60;maxResults&#x60; query string is related to the &#x60;pageToken&#x60; since &#x60;maxResults&#x60; determines how many entries are returned on each page. This is an optional query string. If not specified, the server returns the first page. | [optional] |

### Return type

[**LicenseAssignmentList**](LicenseAssignmentList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="licensingLicenseAssignmentsPatch"></a>
# **licensingLicenseAssignmentsPatch**
> LicenseAssignment licensingLicenseAssignmentsPatch(productId, skuId, userId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, licenseAssignment)



Reassign a user&#39;s product SKU with a different SKU in the same product. This method supports patch semantics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://licensing.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LicenseAssignmentsApi apiInstance = new LicenseAssignmentsApi(defaultClient);
    String productId = "productId_example"; // String | A product's unique identifier. For more information about products in this version of the API, see Products and SKUs.
    String skuId = "skuId_example"; // String | A product SKU's unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
    String userId = "userId_example"; // String | The user's current primary email address. If the user's email address changes, use the new email address in your API requests. Since a `userId` is subject to change, do not use a `userId` value as a key for persistent data. This key could break if the current user's email address changes. If the `userId` is suspended, the license status changes.
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
    LicenseAssignment licenseAssignment = new LicenseAssignment(); // LicenseAssignment | 
    try {
      LicenseAssignment result = apiInstance.licensingLicenseAssignmentsPatch(productId, skuId, userId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, licenseAssignment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseAssignmentsApi#licensingLicenseAssignmentsPatch");
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
| **productId** | **String**| A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs. | |
| **skuId** | **String**| A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs. | |
| **userId** | **String**| The user&#39;s current primary email address. If the user&#39;s email address changes, use the new email address in your API requests. Since a &#x60;userId&#x60; is subject to change, do not use a &#x60;userId&#x60; value as a key for persistent data. This key could break if the current user&#39;s email address changes. If the &#x60;userId&#x60; is suspended, the license status changes. | |
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
| **licenseAssignment** | [**LicenseAssignment**](LicenseAssignment.md)|  | [optional] |

### Return type

[**LicenseAssignment**](LicenseAssignment.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="licensingLicenseAssignmentsUpdate"></a>
# **licensingLicenseAssignmentsUpdate**
> LicenseAssignment licensingLicenseAssignmentsUpdate(productId, skuId, userId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, licenseAssignment)



Reassign a user&#39;s product SKU with a different SKU in the same product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicenseAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://licensing.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LicenseAssignmentsApi apiInstance = new LicenseAssignmentsApi(defaultClient);
    String productId = "productId_example"; // String | A product's unique identifier. For more information about products in this version of the API, see Products and SKUs.
    String skuId = "skuId_example"; // String | A product SKU's unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
    String userId = "userId_example"; // String | The user's current primary email address. If the user's email address changes, use the new email address in your API requests. Since a `userId` is subject to change, do not use a `userId` value as a key for persistent data. This key could break if the current user's email address changes. If the `userId` is suspended, the license status changes.
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
    LicenseAssignment licenseAssignment = new LicenseAssignment(); // LicenseAssignment | 
    try {
      LicenseAssignment result = apiInstance.licensingLicenseAssignmentsUpdate(productId, skuId, userId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, licenseAssignment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicenseAssignmentsApi#licensingLicenseAssignmentsUpdate");
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
| **productId** | **String**| A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs. | |
| **skuId** | **String**| A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs. | |
| **userId** | **String**| The user&#39;s current primary email address. If the user&#39;s email address changes, use the new email address in your API requests. Since a &#x60;userId&#x60; is subject to change, do not use a &#x60;userId&#x60; value as a key for persistent data. This key could break if the current user&#39;s email address changes. If the &#x60;userId&#x60; is suspended, the license status changes. | |
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
| **licenseAssignment** | [**LicenseAssignment**](LicenseAssignment.md)|  | [optional] |

### Return type

[**LicenseAssignment**](LicenseAssignment.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

