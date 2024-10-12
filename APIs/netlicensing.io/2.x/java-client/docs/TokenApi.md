# TokenApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createToken**](TokenApi.md#createToken) | **POST** /token | Create token |
| [**deleteToken**](TokenApi.md#deleteToken) | **DELETE** /token/{tokenNumber} | Delete token |
| [**getToken**](TokenApi.md#getToken) | **GET** /token/{tokenNumber} | Get token |
| [**listTokens**](TokenApi.md#listTokens) | **GET** /token | List Tokens |


<a id="createToken"></a>
# **createToken**
> Netlicensing createToken(tokenType, action, apiKeyRole, cancelURL, cancelURLTitle, licenseTemplateNumber, licenseeNumber, predefinedShoppingItem, privateKey, productNumber, successURL, successURLTitle, type)

Create token

Create token by &#39;tokenType&#39; and additional token parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TokenApi apiInstance = new TokenApi(defaultClient);
    String tokenType = "DEFAULT"; // String | Token type to be generated
    String action = "licenseeLogin"; // String | For <i>type=ACTION</i> only; defines token action to be perfromed
    String apiKeyRole = "ROLE_APIKEY_LICENSEE"; // String | For <i>tokenType=APIKEY</i> only (default: ROLE_APIKEY_LICENSEE); defines token RoleID
    String cancelURL = "cancelURL_example"; // String | For <i>tokenType=SHOP</i> only; take customers to this URL when they cancel their checkout
    String cancelURLTitle = "cancelURLTitle_example"; // String | For <i>tokenType=SHOP</i> only; shop link title for cancel checkout process
    String licenseTemplateNumber = "licenseTemplateNumber_example"; // String | For <i>tokenType=SHOP</i> only; identifies LicenseTemplate that will be assigned to the shop token
    String licenseeNumber = "licenseeNumber_example"; // String | For <i>tokenType=SHOP</i> or <i>type=ACTION</i> only (mandatory); identifies Licensee that will be assigned to the shop token
    String predefinedShoppingItem = "predefinedShoppingItem_example"; // String | For <i>tokenType=SHOP</i> only; identifies Shopping Item name that will be shown to the customer
    String privateKey = "privateKey_example"; // String | For <i>tokenType=APIKEY</i> only (optional); defines PrivateKey to be used with the validate method<br/><strong>Please Note:</strong> PrivateKey need to be provided as one line without spaces
    String productNumber = "productNumber_example"; // String | For <i>tokenType=SHOP</i> only (mandatory); identifies Product that will be assigned to the shop token
    String successURL = "successURL_example"; // String | For <i>tokenType=SHOP</i> only; take customers to this URL when they finish checkout
    String successURLTitle = "successURLTitle_example"; // String | For <i>tokenType=SHOP</i> only; shop link title for successful checkout process
    String type = "ACTION"; // String | For <i>tokenType=DEFAULT</i> only; action type to be set
    try {
      Netlicensing result = apiInstance.createToken(tokenType, action, apiKeyRole, cancelURL, cancelURLTitle, licenseTemplateNumber, licenseeNumber, predefinedShoppingItem, privateKey, productNumber, successURL, successURLTitle, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenApi#createToken");
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
| **tokenType** | **String**| Token type to be generated | [enum: DEFAULT, SHOP, APIKEY] |
| **action** | **String**| For &lt;i&gt;type&#x3D;ACTION&lt;/i&gt; only; defines token action to be perfromed | [optional] [enum: licenseeLogin] |
| **apiKeyRole** | **String**| For &lt;i&gt;tokenType&#x3D;APIKEY&lt;/i&gt; only (default: ROLE_APIKEY_LICENSEE); defines token RoleID | [optional] [enum: ROLE_APIKEY_LICENSEE, ROLE_APIKEY_ANALYTICS, ROLE_APIKEY_OPERATION, ROLE_APIKEY_MAINTENANCE, ROLE_APIKEY_ADMIN] |
| **cancelURL** | **String**| For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; take customers to this URL when they cancel their checkout | [optional] |
| **cancelURLTitle** | **String**| For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; shop link title for cancel checkout process | [optional] |
| **licenseTemplateNumber** | **String**| For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; identifies LicenseTemplate that will be assigned to the shop token | [optional] |
| **licenseeNumber** | **String**| For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; or &lt;i&gt;type&#x3D;ACTION&lt;/i&gt; only (mandatory); identifies Licensee that will be assigned to the shop token | [optional] |
| **predefinedShoppingItem** | **String**| For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; identifies Shopping Item name that will be shown to the customer | [optional] |
| **privateKey** | **String**| For &lt;i&gt;tokenType&#x3D;APIKEY&lt;/i&gt; only (optional); defines PrivateKey to be used with the validate method&lt;br/&gt;&lt;strong&gt;Please Note:&lt;/strong&gt; PrivateKey need to be provided as one line without spaces | [optional] |
| **productNumber** | **String**| For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only (mandatory); identifies Product that will be assigned to the shop token | [optional] |
| **successURL** | **String**| For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; take customers to this URL when they finish checkout | [optional] |
| **successURLTitle** | **String**| For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; shop link title for successful checkout process | [optional] |
| **type** | **String**| For &lt;i&gt;tokenType&#x3D;DEFAULT&lt;/i&gt; only; action type to be set | [optional] [enum: ACTION] |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="deleteToken"></a>
# **deleteToken**
> Netlicensing deleteToken(tokenNumber)

Delete token

Delete a token by &#39;number&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TokenApi apiInstance = new TokenApi(defaultClient);
    String tokenNumber = "tokenNumber_example"; // String | Token number
    try {
      Netlicensing result = apiInstance.deleteToken(tokenNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenApi#deleteToken");
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
| **tokenNumber** | **String**| Token number | |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="getToken"></a>
# **getToken**
> Netlicensing getToken(tokenNumber)

Get token

Return a token by &#39;tokenNumber&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TokenApi apiInstance = new TokenApi(defaultClient);
    String tokenNumber = "tokenNumber_example"; // String | Token number
    try {
      Netlicensing result = apiInstance.getToken(tokenNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenApi#getToken");
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
| **tokenNumber** | **String**| Token number | |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="listTokens"></a>
# **listTokens**
> List&lt;Netlicensing&gt; listTokens()

List Tokens

Return a list of all tokens for the current Vendor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TokenApi apiInstance = new TokenApi(defaultClient);
    try {
      List<Netlicensing> result = apiInstance.listTokens();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenApi#listTokens");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Netlicensing&gt;**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

