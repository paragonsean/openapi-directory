# InappproductsApi

All URIs are relative to *https://www.googleapis.com/androidpublisher/v2/applications*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**androidpublisherInappproductsDelete**](InappproductsApi.md#androidpublisherInappproductsDelete) | **DELETE** /{packageName}/inappproducts/{sku} |  |
| [**androidpublisherInappproductsGet**](InappproductsApi.md#androidpublisherInappproductsGet) | **GET** /{packageName}/inappproducts/{sku} |  |
| [**androidpublisherInappproductsInsert**](InappproductsApi.md#androidpublisherInappproductsInsert) | **POST** /{packageName}/inappproducts |  |
| [**androidpublisherInappproductsList**](InappproductsApi.md#androidpublisherInappproductsList) | **GET** /{packageName}/inappproducts |  |
| [**androidpublisherInappproductsPatch**](InappproductsApi.md#androidpublisherInappproductsPatch) | **PATCH** /{packageName}/inappproducts/{sku} |  |
| [**androidpublisherInappproductsUpdate**](InappproductsApi.md#androidpublisherInappproductsUpdate) | **PUT** /{packageName}/inappproducts/{sku} |  |


<a id="androidpublisherInappproductsDelete"></a>
# **androidpublisherInappproductsDelete**
> androidpublisherInappproductsDelete(packageName, sku, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Delete an in-app product for an app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InappproductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InappproductsApi apiInstance = new InappproductsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app with the in-app product; for example, \"com.spiffygame\".
    String sku = "sku_example"; // String | Unique identifier for the in-app product.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      apiInstance.androidpublisherInappproductsDelete(packageName, sku, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
    } catch (ApiException e) {
      System.err.println("Exception when calling InappproductsApi#androidpublisherInappproductsDelete");
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
| **packageName** | **String**| Unique identifier for the Android app with the in-app product; for example, \&quot;com.spiffygame\&quot;. | |
| **sku** | **String**| Unique identifier for the in-app product. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherInappproductsGet"></a>
# **androidpublisherInappproductsGet**
> InAppProduct androidpublisherInappproductsGet(packageName, sku, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Returns information about the in-app product specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InappproductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InappproductsApi apiInstance = new InappproductsApi(defaultClient);
    String packageName = "packageName_example"; // String | 
    String sku = "sku_example"; // String | Unique identifier for the in-app product.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      InAppProduct result = apiInstance.androidpublisherInappproductsGet(packageName, sku, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InappproductsApi#androidpublisherInappproductsGet");
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
| **packageName** | **String**|  | |
| **sku** | **String**| Unique identifier for the in-app product. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**InAppProduct**](InAppProduct.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherInappproductsInsert"></a>
# **androidpublisherInappproductsInsert**
> InAppProduct androidpublisherInappproductsInsert(packageName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, autoConvertMissingPrices, inAppProduct)



Creates a new in-app product for an app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InappproductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InappproductsApi apiInstance = new InappproductsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app; for example, \"com.spiffygame\".
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean autoConvertMissingPrices = true; // Boolean | If true the prices for all regions targeted by the parent app that don't have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false.
    InAppProduct inAppProduct = new InAppProduct(); // InAppProduct | 
    try {
      InAppProduct result = apiInstance.androidpublisherInappproductsInsert(packageName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, autoConvertMissingPrices, inAppProduct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InappproductsApi#androidpublisherInappproductsInsert");
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
| **packageName** | **String**| Unique identifier for the Android app; for example, \&quot;com.spiffygame\&quot;. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **autoConvertMissingPrices** | **Boolean**| If true the prices for all regions targeted by the parent app that don&#39;t have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false. | [optional] |
| **inAppProduct** | [**InAppProduct**](InAppProduct.md)|  | [optional] |

### Return type

[**InAppProduct**](InAppProduct.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherInappproductsList"></a>
# **androidpublisherInappproductsList**
> InappproductsListResponse androidpublisherInappproductsList(packageName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, startIndex, token)



List all the in-app products for an Android app, both subscriptions and managed in-app products..

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InappproductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InappproductsApi apiInstance = new InappproductsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app with in-app products; for example, \"com.spiffygame\".
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer maxResults = 56; // Integer | 
    Integer startIndex = 56; // Integer | 
    String token = "token_example"; // String | 
    try {
      InappproductsListResponse result = apiInstance.androidpublisherInappproductsList(packageName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, startIndex, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InappproductsApi#androidpublisherInappproductsList");
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
| **packageName** | **String**| Unique identifier for the Android app with in-app products; for example, \&quot;com.spiffygame\&quot;. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **maxResults** | **Integer**|  | [optional] |
| **startIndex** | **Integer**|  | [optional] |
| **token** | **String**|  | [optional] |

### Return type

[**InappproductsListResponse**](InappproductsListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherInappproductsPatch"></a>
# **androidpublisherInappproductsPatch**
> InAppProduct androidpublisherInappproductsPatch(packageName, sku, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, autoConvertMissingPrices, inAppProduct)



Updates the details of an in-app product. This method supports patch semantics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InappproductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InappproductsApi apiInstance = new InappproductsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app with the in-app product; for example, \"com.spiffygame\".
    String sku = "sku_example"; // String | Unique identifier for the in-app product.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean autoConvertMissingPrices = true; // Boolean | If true the prices for all regions targeted by the parent app that don't have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false.
    InAppProduct inAppProduct = new InAppProduct(); // InAppProduct | 
    try {
      InAppProduct result = apiInstance.androidpublisherInappproductsPatch(packageName, sku, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, autoConvertMissingPrices, inAppProduct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InappproductsApi#androidpublisherInappproductsPatch");
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
| **packageName** | **String**| Unique identifier for the Android app with the in-app product; for example, \&quot;com.spiffygame\&quot;. | |
| **sku** | **String**| Unique identifier for the in-app product. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **autoConvertMissingPrices** | **Boolean**| If true the prices for all regions targeted by the parent app that don&#39;t have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false. | [optional] |
| **inAppProduct** | [**InAppProduct**](InAppProduct.md)|  | [optional] |

### Return type

[**InAppProduct**](InAppProduct.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherInappproductsUpdate"></a>
# **androidpublisherInappproductsUpdate**
> InAppProduct androidpublisherInappproductsUpdate(packageName, sku, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, autoConvertMissingPrices, inAppProduct)



Updates the details of an in-app product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InappproductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/androidpublisher/v2/applications");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InappproductsApi apiInstance = new InappproductsApi(defaultClient);
    String packageName = "packageName_example"; // String | Unique identifier for the Android app with the in-app product; for example, \"com.spiffygame\".
    String sku = "sku_example"; // String | Unique identifier for the in-app product.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Boolean autoConvertMissingPrices = true; // Boolean | If true the prices for all regions targeted by the parent app that don't have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false.
    InAppProduct inAppProduct = new InAppProduct(); // InAppProduct | 
    try {
      InAppProduct result = apiInstance.androidpublisherInappproductsUpdate(packageName, sku, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, autoConvertMissingPrices, inAppProduct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InappproductsApi#androidpublisherInappproductsUpdate");
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
| **packageName** | **String**| Unique identifier for the Android app with the in-app product; for example, \&quot;com.spiffygame\&quot;. | |
| **sku** | **String**| Unique identifier for the in-app product. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **autoConvertMissingPrices** | **Boolean**| If true the prices for all regions targeted by the parent app that don&#39;t have a price specified for this in-app product will be auto converted to the target currency based on the default price. Defaults to false. | [optional] |
| **inAppProduct** | [**InAppProduct**](InAppProduct.md)|  | [optional] |

### Return type

[**InAppProduct**](InAppProduct.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

