# ItemsApi

All URIs are relative to *http://1password.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createVaultItem**](ItemsApi.md#createVaultItem) | **POST** /vaults/{vaultUuid}/items | Create a new Item |
| [**deleteVaultItem**](ItemsApi.md#deleteVaultItem) | **DELETE** /vaults/{vaultUuid}/items/{itemUuid} | Delete an Item |
| [**getVaultItemById**](ItemsApi.md#getVaultItemById) | **GET** /vaults/{vaultUuid}/items/{itemUuid} | Get the details of an Item |
| [**getVaultItems**](ItemsApi.md#getVaultItems) | **GET** /vaults/{vaultUuid}/items | Get all items for inside a Vault |
| [**patchVaultItem**](ItemsApi.md#patchVaultItem) | **PATCH** /vaults/{vaultUuid}/items/{itemUuid} | Update a subset of Item attributes |
| [**updateVaultItem**](ItemsApi.md#updateVaultItem) | **PUT** /vaults/{vaultUuid}/items/{itemUuid} | Update an Item |


<a id="createVaultItem"></a>
# **createVaultItem**
> FullItem createVaultItem(vaultUuid, fullItem)

Create a new Item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://1password.local");
    
    // Configure HTTP bearer authorization: ConnectToken
    HttpBearerAuth ConnectToken = (HttpBearerAuth) defaultClient.getAuthentication("ConnectToken");
    ConnectToken.setBearerToken("BEARER TOKEN");

    ItemsApi apiInstance = new ItemsApi(defaultClient);
    String vaultUuid = "vaultUuid_example"; // String | The UUID of the Vault to create an Item in
    FullItem fullItem = new FullItem(); // FullItem | 
    try {
      FullItem result = apiInstance.createVaultItem(vaultUuid, fullItem);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItemsApi#createVaultItem");
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
| **vaultUuid** | **String**| The UUID of the Vault to create an Item in | |
| **fullItem** | [**FullItem**](FullItem.md)|  | [optional] |

### Return type

[**FullItem**](FullItem.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Unable to create item due to invalid input |  -  |
| **401** | Invalid or missing token |  -  |
| **403** | Unauthorized access |  -  |
| **404** | Item not found |  -  |

<a id="deleteVaultItem"></a>
# **deleteVaultItem**
> deleteVaultItem(vaultUuid, itemUuid)

Delete an Item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://1password.local");
    
    // Configure HTTP bearer authorization: ConnectToken
    HttpBearerAuth ConnectToken = (HttpBearerAuth) defaultClient.getAuthentication("ConnectToken");
    ConnectToken.setBearerToken("BEARER TOKEN");

    ItemsApi apiInstance = new ItemsApi(defaultClient);
    String vaultUuid = "vaultUuid_example"; // String | The UUID of the Vault the item is in
    String itemUuid = "itemUuid_example"; // String | The UUID of the Item to update
    try {
      apiInstance.deleteVaultItem(vaultUuid, itemUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItemsApi#deleteVaultItem");
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
| **vaultUuid** | **String**| The UUID of the Vault the item is in | |
| **itemUuid** | **String**| The UUID of the Item to update | |

### Return type

null (empty response body)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully deleted an item |  -  |
| **401** | Invalid or missing token |  -  |
| **403** | Unauthorized access |  -  |
| **404** | Item not found |  -  |

<a id="getVaultItemById"></a>
# **getVaultItemById**
> FullItem getVaultItemById(vaultUuid, itemUuid)

Get the details of an Item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://1password.local");
    
    // Configure HTTP bearer authorization: ConnectToken
    HttpBearerAuth ConnectToken = (HttpBearerAuth) defaultClient.getAuthentication("ConnectToken");
    ConnectToken.setBearerToken("BEARER TOKEN");

    ItemsApi apiInstance = new ItemsApi(defaultClient);
    String vaultUuid = "vaultUuid_example"; // String | The UUID of the Vault to fetch Item from
    String itemUuid = "itemUuid_example"; // String | The UUID of the Item to fetch
    try {
      FullItem result = apiInstance.getVaultItemById(vaultUuid, itemUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItemsApi#getVaultItemById");
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
| **vaultUuid** | **String**| The UUID of the Vault to fetch Item from | |
| **itemUuid** | **String**| The UUID of the Item to fetch | |

### Return type

[**FullItem**](FullItem.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Invalid or missing token |  -  |
| **403** | Unauthorized access |  -  |
| **404** | Item not found |  -  |

<a id="getVaultItems"></a>
# **getVaultItems**
> List&lt;Item&gt; getVaultItems(vaultUuid, filter)

Get all items for inside a Vault

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://1password.local");
    
    // Configure HTTP bearer authorization: ConnectToken
    HttpBearerAuth ConnectToken = (HttpBearerAuth) defaultClient.getAuthentication("ConnectToken");
    ConnectToken.setBearerToken("BEARER TOKEN");

    ItemsApi apiInstance = new ItemsApi(defaultClient);
    String vaultUuid = "vaultUuid_example"; // String | The UUID of the Vault to fetch Items from
    String filter = "title eq \"Some Item Name\""; // String | Filter the Item collection based on Item name using SCIM eq filter
    try {
      List<Item> result = apiInstance.getVaultItems(vaultUuid, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItemsApi#getVaultItems");
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
| **vaultUuid** | **String**| The UUID of the Vault to fetch Items from | |
| **filter** | **String**| Filter the Item collection based on Item name using SCIM eq filter | [optional] |

### Return type

[**List&lt;Item&gt;**](Item.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Invalid or missing token |  -  |
| **404** | Vault not found |  -  |

<a id="patchVaultItem"></a>
# **patchVaultItem**
> FullItem patchVaultItem(vaultUuid, itemUuid, patchInner)

Update a subset of Item attributes

Applies a modified [RFC6902 JSON Patch](https://tools.ietf.org/html/rfc6902) document to an Item or ItemField. This endpoint only supports &#x60;add&#x60;, &#x60;remove&#x60; and &#x60;replace&#x60; operations.  When modifying a specific ItemField, the ItemField&#39;s ID in the &#x60;path&#x60; attribute of the operation object: &#x60;/fields/{fieldId}&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://1password.local");
    
    // Configure HTTP bearer authorization: ConnectToken
    HttpBearerAuth ConnectToken = (HttpBearerAuth) defaultClient.getAuthentication("ConnectToken");
    ConnectToken.setBearerToken("BEARER TOKEN");

    ItemsApi apiInstance = new ItemsApi(defaultClient);
    String vaultUuid = "vaultUuid_example"; // String | The UUID of the Vault the item is in
    String itemUuid = "itemUuid_example"; // String | The UUID of the Item to update
    List<PatchInner> patchInner = Arrays.asList(); // List<PatchInner> | 
    try {
      FullItem result = apiInstance.patchVaultItem(vaultUuid, itemUuid, patchInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItemsApi#patchVaultItem");
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
| **vaultUuid** | **String**| The UUID of the Vault the item is in | |
| **itemUuid** | **String**| The UUID of the Item to update | |
| **patchInner** | [**List&lt;PatchInner&gt;**](PatchInner.md)|  | [optional] |

### Return type

[**FullItem**](FullItem.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Item updated. If no Patch operations were provided, Item is unmodified. |  -  |
| **401** | Invalid or missing token |  -  |
| **403** | Unauthorized access |  -  |
| **404** | Item not found |  -  |

<a id="updateVaultItem"></a>
# **updateVaultItem**
> FullItem updateVaultItem(vaultUuid, itemUuid, fullItem)

Update an Item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://1password.local");
    
    // Configure HTTP bearer authorization: ConnectToken
    HttpBearerAuth ConnectToken = (HttpBearerAuth) defaultClient.getAuthentication("ConnectToken");
    ConnectToken.setBearerToken("BEARER TOKEN");

    ItemsApi apiInstance = new ItemsApi(defaultClient);
    String vaultUuid = "vaultUuid_example"; // String | The UUID of the Item's Vault
    String itemUuid = "itemUuid_example"; // String | The UUID of the Item to update
    FullItem fullItem = new FullItem(); // FullItem | 
    try {
      FullItem result = apiInstance.updateVaultItem(vaultUuid, itemUuid, fullItem);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItemsApi#updateVaultItem");
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
| **vaultUuid** | **String**| The UUID of the Item&#39;s Vault | |
| **itemUuid** | **String**| The UUID of the Item to update | |
| **fullItem** | [**FullItem**](FullItem.md)|  | [optional] |

### Return type

[**FullItem**](FullItem.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Unable to create item due to invalid input |  -  |
| **401** | Invalid or missing token |  -  |
| **403** | Unauthorized access |  -  |
| **404** | Item not found |  -  |

