# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assetFiltersCreateOrUpdate**](DefaultApi.md#assetFiltersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName}/assetFilters/{filterName} | Create or update an Asset Filter |
| [**assetFiltersDelete**](DefaultApi.md#assetFiltersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName}/assetFilters/{filterName} | Delete an Asset Filter. |
| [**assetFiltersGet**](DefaultApi.md#assetFiltersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName}/assetFilters/{filterName} | Get an Asset Filter. |
| [**assetFiltersList**](DefaultApi.md#assetFiltersList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName}/assetFilters | List Asset Filters |
| [**assetFiltersUpdate**](DefaultApi.md#assetFiltersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName}/assetFilters/{filterName} | Update an Asset Filter |
| [**assetsCreateOrUpdate**](DefaultApi.md#assetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName} | Create or update an Asset |
| [**assetsDelete**](DefaultApi.md#assetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName} | Delete an Asset. |
| [**assetsGet**](DefaultApi.md#assetsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName} | Get an Asset |
| [**assetsGetEncryptionKey**](DefaultApi.md#assetsGetEncryptionKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName}/getEncryptionKey | Gets the Asset storage key |
| [**assetsList**](DefaultApi.md#assetsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets | List Assets |
| [**assetsListContainerSas**](DefaultApi.md#assetsListContainerSas) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName}/listContainerSas | List the Asset URLs |
| [**assetsListStreamingLocators**](DefaultApi.md#assetsListStreamingLocators) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName}/listStreamingLocators | List Streaming Locators |
| [**assetsUpdate**](DefaultApi.md#assetsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/assets/{assetName} | Update an Asset |


<a id="assetFiltersCreateOrUpdate"></a>
# **assetFiltersCreateOrUpdate**
> AssetFilter assetFiltersCreateOrUpdate(subscriptionId, resourceGroupName, accountName, assetName, filterName, apiVersion, parameters)

Create or update an Asset Filter

Creates or updates an Asset Filter associated with the specified Asset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String assetName = "assetName_example"; // String | The Asset name.
    String filterName = "filterName_example"; // String | The Asset Filter name
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    AssetFilter parameters = new AssetFilter(); // AssetFilter | The request parameters
    try {
      AssetFilter result = apiInstance.assetFiltersCreateOrUpdate(subscriptionId, resourceGroupName, accountName, assetName, filterName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assetFiltersCreateOrUpdate");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **assetName** | **String**| The Asset name. | |
| **filterName** | **String**| The Asset Filter name | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**AssetFilter**](AssetFilter.md)| The request parameters | |

### Return type

[**AssetFilter**](AssetFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | Detailed error information. |  -  |

<a id="assetFiltersDelete"></a>
# **assetFiltersDelete**
> assetFiltersDelete(subscriptionId, resourceGroupName, accountName, assetName, filterName, apiVersion)

Delete an Asset Filter.

Deletes an Asset Filter associated with the specified Asset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String assetName = "assetName_example"; // String | The Asset name.
    String filterName = "filterName_example"; // String | The Asset Filter name
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.assetFiltersDelete(subscriptionId, resourceGroupName, accountName, assetName, filterName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assetFiltersDelete");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **assetName** | **String**| The Asset name. | |
| **filterName** | **String**| The Asset Filter name | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | NoContent |  -  |
| **0** | Detailed error information. |  -  |

<a id="assetFiltersGet"></a>
# **assetFiltersGet**
> AssetFilter assetFiltersGet(subscriptionId, resourceGroupName, accountName, assetName, filterName, apiVersion)

Get an Asset Filter.

Get the details of an Asset Filter associated with the specified Asset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String assetName = "assetName_example"; // String | The Asset name.
    String filterName = "filterName_example"; // String | The Asset Filter name
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      AssetFilter result = apiInstance.assetFiltersGet(subscriptionId, resourceGroupName, accountName, assetName, filterName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assetFiltersGet");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **assetName** | **String**| The Asset name. | |
| **filterName** | **String**| The Asset Filter name | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**AssetFilter**](AssetFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NotFound |  -  |
| **0** | Detailed error information. |  -  |

<a id="assetFiltersList"></a>
# **assetFiltersList**
> AssetFilterCollection assetFiltersList(subscriptionId, resourceGroupName, accountName, assetName, apiVersion)

List Asset Filters

List Asset Filters associated with the specified Asset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String assetName = "assetName_example"; // String | The Asset name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      AssetFilterCollection result = apiInstance.assetFiltersList(subscriptionId, resourceGroupName, accountName, assetName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assetFiltersList");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **assetName** | **String**| The Asset name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**AssetFilterCollection**](AssetFilterCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

<a id="assetFiltersUpdate"></a>
# **assetFiltersUpdate**
> AssetFilter assetFiltersUpdate(subscriptionId, resourceGroupName, accountName, assetName, filterName, apiVersion, parameters)

Update an Asset Filter

Updates an existing Asset Filter associated with the specified Asset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String assetName = "assetName_example"; // String | The Asset name.
    String filterName = "filterName_example"; // String | The Asset Filter name
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    AssetFilter parameters = new AssetFilter(); // AssetFilter | The request parameters
    try {
      AssetFilter result = apiInstance.assetFiltersUpdate(subscriptionId, resourceGroupName, accountName, assetName, filterName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assetFiltersUpdate");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **assetName** | **String**| The Asset name. | |
| **filterName** | **String**| The Asset Filter name | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**AssetFilter**](AssetFilter.md)| The request parameters | |

### Return type

[**AssetFilter**](AssetFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

<a id="assetsCreateOrUpdate"></a>
# **assetsCreateOrUpdate**
> Asset assetsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, assetName, apiVersion, parameters)

Create or update an Asset

Creates or updates an Asset in the Media Services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String assetName = "assetName_example"; // String | The Asset name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    Asset parameters = new Asset(); // Asset | The request parameters
    try {
      Asset result = apiInstance.assetsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, assetName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assetsCreateOrUpdate");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **assetName** | **String**| The Asset name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**Asset**](Asset.md)| The request parameters | |

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | Detailed error information. |  -  |

<a id="assetsDelete"></a>
# **assetsDelete**
> assetsDelete(subscriptionId, resourceGroupName, accountName, assetName, apiVersion)

Delete an Asset.

Deletes an Asset in the Media Services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String assetName = "assetName_example"; // String | The Asset name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.assetsDelete(subscriptionId, resourceGroupName, accountName, assetName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assetsDelete");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **assetName** | **String**| The Asset name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | NoContent |  -  |
| **0** | Detailed error information. |  -  |

<a id="assetsGet"></a>
# **assetsGet**
> Asset assetsGet(subscriptionId, resourceGroupName, accountName, assetName, apiVersion)

Get an Asset

Get the details of an Asset in the Media Services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String assetName = "assetName_example"; // String | The Asset name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      Asset result = apiInstance.assetsGet(subscriptionId, resourceGroupName, accountName, assetName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assetsGet");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **assetName** | **String**| The Asset name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NotFound |  -  |
| **0** | Detailed error information. |  -  |

<a id="assetsGetEncryptionKey"></a>
# **assetsGetEncryptionKey**
> StorageEncryptedAssetDecryptionData assetsGetEncryptionKey(subscriptionId, resourceGroupName, accountName, assetName, apiVersion)

Gets the Asset storage key

Gets the Asset storage encryption keys used to decrypt content created by version 2 of the Media Services API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String assetName = "assetName_example"; // String | The Asset name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      StorageEncryptedAssetDecryptionData result = apiInstance.assetsGetEncryptionKey(subscriptionId, resourceGroupName, accountName, assetName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assetsGetEncryptionKey");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **assetName** | **String**| The Asset name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**StorageEncryptedAssetDecryptionData**](StorageEncryptedAssetDecryptionData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

<a id="assetsList"></a>
# **assetsList**
> AssetCollection assetsList(subscriptionId, resourceGroupName, accountName, apiVersion, $filter, $top, $orderby)

List Assets

List Assets in the Media Services account with optional filtering and ordering

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | Restricts the set of items returned.
    Integer $top = 56; // Integer | Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
    String $orderby = "$orderby_example"; // String | Specifies the key by which the result collection should be ordered.
    try {
      AssetCollection result = apiInstance.assetsList(subscriptionId, resourceGroupName, accountName, apiVersion, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assetsList");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **$filter** | **String**| Restricts the set of items returned. | [optional] |
| **$top** | **Integer**| Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n. | [optional] |
| **$orderby** | **String**| Specifies the key by which the result collection should be ordered. | [optional] |

### Return type

[**AssetCollection**](AssetCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

<a id="assetsListContainerSas"></a>
# **assetsListContainerSas**
> AssetContainerSas assetsListContainerSas(subscriptionId, resourceGroupName, accountName, assetName, apiVersion, parameters)

List the Asset URLs

Lists storage container URLs with shared access signatures (SAS) for uploading and downloading Asset content. The signatures are derived from the storage account keys.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String assetName = "assetName_example"; // String | The Asset name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    ListContainerSasInput parameters = new ListContainerSasInput(); // ListContainerSasInput | The request parameters
    try {
      AssetContainerSas result = apiInstance.assetsListContainerSas(subscriptionId, resourceGroupName, accountName, assetName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assetsListContainerSas");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **assetName** | **String**| The Asset name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**ListContainerSasInput**](ListContainerSasInput.md)| The request parameters | |

### Return type

[**AssetContainerSas**](AssetContainerSas.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

<a id="assetsListStreamingLocators"></a>
# **assetsListStreamingLocators**
> ListStreamingLocatorsResponse assetsListStreamingLocators(subscriptionId, resourceGroupName, accountName, assetName, apiVersion)

List Streaming Locators

Lists Streaming Locators which are associated with this asset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String assetName = "assetName_example"; // String | The Asset name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      ListStreamingLocatorsResponse result = apiInstance.assetsListStreamingLocators(subscriptionId, resourceGroupName, accountName, assetName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assetsListStreamingLocators");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **assetName** | **String**| The Asset name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**ListStreamingLocatorsResponse**](ListStreamingLocatorsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

<a id="assetsUpdate"></a>
# **assetsUpdate**
> Asset assetsUpdate(subscriptionId, resourceGroupName, accountName, assetName, apiVersion, parameters)

Update an Asset

Updates an existing Asset in the Media Services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String assetName = "assetName_example"; // String | The Asset name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    Asset parameters = new Asset(); // Asset | The request parameters
    try {
      Asset result = apiInstance.assetsUpdate(subscriptionId, resourceGroupName, accountName, assetName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assetsUpdate");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **assetName** | **String**| The Asset name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**Asset**](Asset.md)| The request parameters | |

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

