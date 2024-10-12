# PrivateStoresApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateStoreCreateOrUpdate**](PrivateStoresApi.md#privateStoreCreateOrUpdate) | **PUT** /providers/Microsoft.Marketplace/privateStores/{PrivateStoreId} |  |
| [**privateStoreDelete**](PrivateStoresApi.md#privateStoreDelete) | **DELETE** /providers/Microsoft.Marketplace/privateStores/{PrivateStoreId} |  |
| [**privateStoreGet**](PrivateStoresApi.md#privateStoreGet) | **GET** /providers/Microsoft.Marketplace/privateStores/{PrivateStoreId} |  |
| [**privateStoreList**](PrivateStoresApi.md#privateStoreList) | **GET** /providers/Microsoft.Marketplace/privateStores |  |
| [**privateStoreOfferCreateOrUpdate**](PrivateStoresApi.md#privateStoreOfferCreateOrUpdate) | **PUT** /providers/Microsoft.Marketplace/privateStores/{PrivateStoreId}/offers/{OfferId} |  |
| [**privateStoreOfferDelete**](PrivateStoresApi.md#privateStoreOfferDelete) | **DELETE** /providers/Microsoft.Marketplace/privateStores/{PrivateStoreId}/offers/{OfferId} |  |
| [**privateStoreOfferGet**](PrivateStoresApi.md#privateStoreOfferGet) | **GET** /providers/Microsoft.Marketplace/privateStores/{PrivateStoreId}/offers/{OfferId} |  |
| [**privateStoreOffersList**](PrivateStoresApi.md#privateStoreOffersList) | **GET** /providers/Microsoft.Marketplace/privateStores/{PrivateStoreId}/offers |  |


<a id="privateStoreCreateOrUpdate"></a>
# **privateStoreCreateOrUpdate**
> PrivateStoreProperties privateStoreCreateOrUpdate(privateStoreId, apiVersion, payload)



Changes private store properties

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateStoresApi apiInstance = new PrivateStoresApi(defaultClient);
    String privateStoreId = "privateStoreId_example"; // String | The store ID - must use the tenant ID
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    PrivateStoreProperties payload = new PrivateStoreProperties(); // PrivateStoreProperties | 
    try {
      PrivateStoreProperties result = apiInstance.privateStoreCreateOrUpdate(privateStoreId, apiVersion, payload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateStoresApi#privateStoreCreateOrUpdate");
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
| **privateStoreId** | **String**| The store ID - must use the tenant ID | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **payload** | [**PrivateStoreProperties**](PrivateStoreProperties.md)|  | [optional] |

### Return type

[**PrivateStoreProperties**](PrivateStoreProperties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Change successful |  -  |
| **0** | Microsoft.Marketplace error response describing why the operation failed. |  -  |

<a id="privateStoreDelete"></a>
# **privateStoreDelete**
> privateStoreDelete(privateStoreId, apiVersion)



Deletes the private store. All that is not saved will be lost.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateStoresApi apiInstance = new PrivateStoresApi(defaultClient);
    String privateStoreId = "privateStoreId_example"; // String | The store ID - must use the tenant ID
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.privateStoreDelete(privateStoreId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateStoresApi#privateStoreDelete");
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
| **privateStoreId** | **String**| The store ID - must use the tenant ID | |
| **apiVersion** | **String**| The API version to use for the request. | |

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
| **200** | Private store was deleted successfully . |  -  |
| **0** | Microsoft.Marketplace error response describing why the operation failed. |  -  |

<a id="privateStoreGet"></a>
# **privateStoreGet**
> PrivateStoreProperties privateStoreGet(privateStoreId, apiVersion)



Get information about the private store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateStoresApi apiInstance = new PrivateStoresApi(defaultClient);
    String privateStoreId = "privateStoreId_example"; // String | The store ID - must use the tenant ID
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      PrivateStoreProperties result = apiInstance.privateStoreGet(privateStoreId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateStoresApi#privateStoreGet");
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
| **privateStoreId** | **String**| The store ID - must use the tenant ID | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**PrivateStoreProperties**](PrivateStoreProperties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Microsoft.Marketplace error response describing why the operation failed. |  -  |

<a id="privateStoreList"></a>
# **privateStoreList**
> PrivateStoreList privateStoreList(apiVersion)



Gets the list of available private stores

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateStoresApi apiInstance = new PrivateStoresApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      PrivateStoreList result = apiInstance.privateStoreList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateStoresApi#privateStoreList");
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
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**PrivateStoreList**](PrivateStoreList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |

<a id="privateStoreOfferCreateOrUpdate"></a>
# **privateStoreOfferCreateOrUpdate**
> Offer privateStoreOfferCreateOrUpdate(offerId, privateStoreId, apiVersion, payload)



Update or add an offer to the default collection of the private store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateStoresApi apiInstance = new PrivateStoresApi(defaultClient);
    String offerId = "offerId_example"; // String | The offer ID to update or delete
    String privateStoreId = "privateStoreId_example"; // String | The store ID - must use the tenant ID
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    Offer payload = new Offer(); // Offer | 
    try {
      Offer result = apiInstance.privateStoreOfferCreateOrUpdate(offerId, privateStoreId, apiVersion, payload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateStoresApi#privateStoreOfferCreateOrUpdate");
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
| **offerId** | **String**| The offer ID to update or delete | |
| **privateStoreId** | **String**| The store ID - must use the tenant ID | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **payload** | [**Offer**](Offer.md)|  | [optional] |

### Return type

[**Offer**](Offer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Microsoft.Marketplace error response describing why the operation failed. |  -  |

<a id="privateStoreOfferDelete"></a>
# **privateStoreOfferDelete**
> privateStoreOfferDelete(offerId, privateStoreId, apiVersion)



Deletes an offer from the given private store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateStoresApi apiInstance = new PrivateStoresApi(defaultClient);
    String offerId = "offerId_example"; // String | The offer ID to update or delete
    String privateStoreId = "privateStoreId_example"; // String | The store ID - must use the tenant ID
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.privateStoreOfferDelete(offerId, privateStoreId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateStoresApi#privateStoreOfferDelete");
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
| **offerId** | **String**| The offer ID to update or delete | |
| **privateStoreId** | **String**| The store ID - must use the tenant ID | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Offer was deleted successfully |  -  |
| **0** | Microsoft.Marketplace error response describing why the operation failed. |  -  |

<a id="privateStoreOfferGet"></a>
# **privateStoreOfferGet**
> Offer privateStoreOfferGet(offerId, privateStoreId, apiVersion)



Gets information about a specific offer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateStoresApi apiInstance = new PrivateStoresApi(defaultClient);
    String offerId = "offerId_example"; // String | The offer ID to update or delete
    String privateStoreId = "privateStoreId_example"; // String | The store ID - must use the tenant ID
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      Offer result = apiInstance.privateStoreOfferGet(offerId, privateStoreId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateStoresApi#privateStoreOfferGet");
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
| **offerId** | **String**| The offer ID to update or delete | |
| **privateStoreId** | **String**| The store ID - must use the tenant ID | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**Offer**](Offer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Offer information retrieved |  -  |
| **0** | Microsoft.Marketplace error response describing why the operation failed. |  -  |

<a id="privateStoreOffersList"></a>
# **privateStoreOffersList**
> OfferListResponse privateStoreOffersList(privateStoreId, apiVersion)



Get a list of all private offers in the given private store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateStoresApi apiInstance = new PrivateStoresApi(defaultClient);
    String privateStoreId = "privateStoreId_example"; // String | The store ID - must use the tenant ID
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      OfferListResponse result = apiInstance.privateStoreOffersList(privateStoreId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateStoresApi#privateStoreOffersList");
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
| **privateStoreId** | **String**| The store ID - must use the tenant ID | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**OfferListResponse**](OfferListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Microsoft.Marketplace error response describing why the operation failed. |  -  |

