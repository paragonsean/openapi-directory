# AssetApi

All URIs are relative to *https://api.xero.com/assets.xro/1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAsset**](AssetApi.md#createAsset) | **POST** /Assets | adds a fixed asset |
| [**createAssetType**](AssetApi.md#createAssetType) | **POST** /AssetTypes | adds a fixed asset type |
| [**getAssetById**](AssetApi.md#getAssetById) | **GET** /Assets/{id} | Retrieves fixed asset by id |
| [**getAssetSettings**](AssetApi.md#getAssetSettings) | **GET** /Settings | searches fixed asset settings |
| [**getAssetTypes**](AssetApi.md#getAssetTypes) | **GET** /AssetTypes | searches fixed asset types |
| [**getAssets**](AssetApi.md#getAssets) | **GET** /Assets | searches fixed asset |


<a id="createAsset"></a>
# **createAsset**
> Asset createAsset(xeroTenantId, asset)

adds a fixed asset

Adds an asset to the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/assets.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AssetApi apiInstance = new AssetApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Asset asset = new Asset(); // Asset | Fixed asset you are creating
    try {
      Asset result = apiInstance.createAsset(xeroTenantId, asset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetApi#createAsset");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **asset** | [**Asset**](Asset.md)| Fixed asset you are creating | |

### Return type

[**Asset**](Asset.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | return single object - create new asset |  -  |
| **400** | invalid input, object invalid |  -  |

<a id="createAssetType"></a>
# **createAssetType**
> AssetType createAssetType(xeroTenantId, assetType)

adds a fixed asset type

Adds an fixed asset type to the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/assets.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AssetApi apiInstance = new AssetApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    AssetType assetType = new AssetType(); // AssetType | Asset type to add
    try {
      AssetType result = apiInstance.createAssetType(xeroTenantId, assetType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetApi#createAssetType");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **assetType** | [**AssetType**](AssetType.md)| Asset type to add | [optional] |

### Return type

[**AssetType**](AssetType.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | results single object -  created fixed type |  -  |
| **400** | invalid input, object invalid |  -  |
| **409** | a type already exists |  -  |

<a id="getAssetById"></a>
# **getAssetById**
> Asset getAssetById(xeroTenantId, id)

Retrieves fixed asset by id

By passing in the appropriate asset id, you can search for a specific fixed asset in the system 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/assets.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AssetApi apiInstance = new AssetApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID id = UUID.fromString("4f7bcdcb-5ec1-4258-9558-19f662fccdfe"); // UUID | fixed asset id for single object
    try {
      Asset result = apiInstance.getAssetById(xeroTenantId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetApi#getAssetById");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **id** | **UUID**| fixed asset id for single object | |

### Return type

[**Asset**](Asset.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **400** | bad input parameter |  -  |

<a id="getAssetSettings"></a>
# **getAssetSettings**
> Setting getAssetSettings(xeroTenantId)

searches fixed asset settings

By passing in the appropriate options, you can search for available fixed asset types in the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/assets.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AssetApi apiInstance = new AssetApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    try {
      Setting result = apiInstance.getAssetSettings(xeroTenantId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetApi#getAssetSettings");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |

### Return type

[**Setting**](Setting.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **400** | bad input parameter |  -  |

<a id="getAssetTypes"></a>
# **getAssetTypes**
> List&lt;AssetType&gt; getAssetTypes(xeroTenantId)

searches fixed asset types

By passing in the appropriate options, you can search for available fixed asset types in the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/assets.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AssetApi apiInstance = new AssetApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    try {
      List<AssetType> result = apiInstance.getAssetTypes(xeroTenantId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetApi#getAssetTypes");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |

### Return type

[**List&lt;AssetType&gt;**](AssetType.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **400** | bad input parameter |  -  |

<a id="getAssets"></a>
# **getAssets**
> Assets getAssets(xeroTenantId, status, page, pageSize, orderBy, sortDirection, filterBy)

searches fixed asset

By passing in the appropriate options, you can search for available fixed asset in the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/assets.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AssetApi apiInstance = new AssetApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    AssetStatusQueryParam status = AssetStatusQueryParam.fromValue("DRAFT"); // AssetStatusQueryParam | Required when retrieving a collection of assets. See Asset Status Codes
    Integer page = 1; // Integer | Results are paged. This specifies which page of the results to return. The default page is 1.
    Integer pageSize = 5; // Integer | The number of records returned per page. By default the number of records returned is 10.
    String orderBy = "AssetType"; // String | Requests can be ordered by AssetType, AssetName, AssetNumber, PurchaseDate and PurchasePrice. If the asset status is DISPOSED it also allows DisposalDate and DisposalPrice.
    String sortDirection = "asc"; // String | ASC or DESC
    String filterBy = "Company Car"; // String | A string that can be used to filter the list to only return assets containing the text. Checks it against the AssetName, AssetNumber, Description and AssetTypeName fields.
    try {
      Assets result = apiInstance.getAssets(xeroTenantId, status, page, pageSize, orderBy, sortDirection, filterBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetApi#getAssets");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **status** | [**AssetStatusQueryParam**](.md)| Required when retrieving a collection of assets. See Asset Status Codes | [enum: DRAFT, REGISTERED, DISPOSED] |
| **page** | **Integer**| Results are paged. This specifies which page of the results to return. The default page is 1. | [optional] |
| **pageSize** | **Integer**| The number of records returned per page. By default the number of records returned is 10. | [optional] |
| **orderBy** | **String**| Requests can be ordered by AssetType, AssetName, AssetNumber, PurchaseDate and PurchasePrice. If the asset status is DISPOSED it also allows DisposalDate and DisposalPrice. | [optional] [enum: AssetType, AssetName, AssetNumber, PurchaseDate, PurchasePrice, DisposalDate, DisposalPrice] |
| **sortDirection** | **String**| ASC or DESC | [optional] [enum: asc, desc] |
| **filterBy** | **String**| A string that can be used to filter the list to only return assets containing the text. Checks it against the AssetName, AssetNumber, Description and AssetTypeName fields. | [optional] |

### Return type

[**Assets**](Assets.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **400** | bad input parameter |  -  |

