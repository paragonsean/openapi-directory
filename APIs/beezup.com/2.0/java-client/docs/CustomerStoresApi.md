# CustomerStoresApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createStore**](CustomerStoresApi.md#createStore) | **POST** /v2/user/customer/stores | Create a new store |
| [**deleteStore**](CustomerStoresApi.md#deleteStore) | **DELETE** /v2/user/customer/stores/{storeId} | Delete a store |
| [**getStore**](CustomerStoresApi.md#getStore) | **GET** /v2/user/customer/stores/{storeId} | Get store&#39;s information |
| [**getStores**](CustomerStoresApi.md#getStores) | **GET** /v2/user/customer/stores | Get store list |
| [**updateStore**](CustomerStoresApi.md#updateStore) | **PATCH** /v2/user/customer/stores/{storeId} | Update some store&#39;s information. |


<a id="createStore"></a>
# **createStore**
> LinksGetStoreLink createStore(createStoreRequest)

Create a new store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerStoresApi apiInstance = new CustomerStoresApi(defaultClient);
    CreateStoreRequest createStoreRequest = new CreateStoreRequest(); // CreateStoreRequest | 
    try {
      LinksGetStoreLink result = apiInstance.createStore(createStoreRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerStoresApi#createStore");
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
| **createStoreRequest** | [**CreateStoreRequest**](CreateStoreRequest.md)|  | |

### Return type

[**LinksGetStoreLink**](LinksGetStoreLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The store has been created successfully. The http header Location contains the new resource url. The body contains the link to the new resource. |  -  |
| **402** | The maximum amount of store has been reached. Please upgrade your contract. |  -  |
| **409** | The customer has a store with the same name |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="deleteStore"></a>
# **deleteStore**
> deleteStore(storeId)

Delete a store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerStoresApi apiInstance = new CustomerStoresApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      apiInstance.deleteStore(storeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerStoresApi#deleteStore");
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
| **storeId** | **String**| Your store identifier | |

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
| **204** | Store deleted |  -  |
| **404** | Store not found or customer not the owner |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getStore"></a>
# **getStore**
> Store getStore(storeId, ifNoneMatch)

Get store&#39;s information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerStoresApi apiInstance = new CustomerStoresApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    try {
      Store result = apiInstance.getStore(storeId, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerStoresApi#getStore");
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
| **storeId** | **String**| Your store identifier | |
| **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] |

### Return type

[**Store**](Store.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The store information |  -  |
| **304** | The ETag sent in the http header If-None-Match did not change. So you are up to date ! |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  * Last-Modified - Last modification UTC date of the resource\\ For more details go to this link: https://tools.ietf.org/html/rfc7232#section-2.2  <br>  |
| **404** | Store not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getStores"></a>
# **getStores**
> StoreList getStores(ifNoneMatch)

Get store list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerStoresApi apiInstance = new CustomerStoresApi(defaultClient);
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    try {
      StoreList result = apiInstance.getStores(ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerStoresApi#getStores");
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
| **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] |

### Return type

[**StoreList**](StoreList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Store list |  -  |
| **304** | The ETag sent in the http header If-None-Match did not change. So you are up to date ! |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  * Last-Modified - Last modification UTC date of the resource\\ For more details go to this link: https://tools.ietf.org/html/rfc7232#section-2.2  <br>  |
| **0** | Occurs when something goes wrong |  -  |

<a id="updateStore"></a>
# **updateStore**
> updateStore(storeId, updateStoreRequest)

Update some store&#39;s information.

Update some store&#39;s information. FYI, you cannot change the country. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerStoresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerStoresApi apiInstance = new CustomerStoresApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    UpdateStoreRequest updateStoreRequest = new UpdateStoreRequest(); // UpdateStoreRequest | 
    try {
      apiInstance.updateStore(storeId, updateStoreRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerStoresApi#updateStore");
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
| **storeId** | **String**| Your store identifier | |
| **updateStoreRequest** | [**UpdateStoreRequest**](UpdateStoreRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Store updated |  -  |
| **404** | Store not found or customer not the owner |  -  |
| **409** | The store name already used |  -  |
| **0** | Occurs when something goes wrong |  -  |

