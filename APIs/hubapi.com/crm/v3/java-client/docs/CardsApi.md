# CardsApi

All URIs are relative to *https://api.hubapi.com/crm/v3/extensions/cards*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteCrmV3ExtensionsCardsAppIdCardId**](CardsApi.md#deleteCrmV3ExtensionsCardsAppIdCardId) | **DELETE** /{appId}/{cardId} | Delete a card |
| [**getCrmV3ExtensionsCardsAppId**](CardsApi.md#getCrmV3ExtensionsCardsAppId) | **GET** /{appId} | Get all cards |
| [**getCrmV3ExtensionsCardsAppIdCardId**](CardsApi.md#getCrmV3ExtensionsCardsAppIdCardId) | **GET** /{appId}/{cardId} | Get a card. |
| [**patchCrmV3ExtensionsCardsAppIdCardId**](CardsApi.md#patchCrmV3ExtensionsCardsAppIdCardId) | **PATCH** /{appId}/{cardId} | Update a card |
| [**postCrmV3ExtensionsCardsAppId**](CardsApi.md#postCrmV3ExtensionsCardsAppId) | **POST** /{appId} | Create a new card |


<a id="deleteCrmV3ExtensionsCardsAppIdCardId"></a>
# **deleteCrmV3ExtensionsCardsAppIdCardId**
> deleteCrmV3ExtensionsCardsAppIdCardId(appId, cardId)

Delete a card

Permanently deletes a card definition with the given ID. Once deleted, data fetch requests for this card will no longer be sent to your service. This can&#39;t be undone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com/crm/v3/extensions/cards");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    CardsApi apiInstance = new CardsApi(defaultClient);
    Integer appId = 56; // Integer | The ID of the target app.
    String cardId = "cardId_example"; // String | The ID of the card to delete.
    try {
      apiInstance.deleteCrmV3ExtensionsCardsAppIdCardId(appId, cardId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#deleteCrmV3ExtensionsCardsAppIdCardId");
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
| **appId** | **Integer**| The ID of the target app. | |
| **cardId** | **String**| The ID of the card to delete. | |

### Return type

null (empty response body)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |
| **0** | An error occurred. |  -  |

<a id="getCrmV3ExtensionsCardsAppId"></a>
# **getCrmV3ExtensionsCardsAppId**
> CardListResponse getCrmV3ExtensionsCardsAppId(appId)

Get all cards

Returns a list of cards for a given app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com/crm/v3/extensions/cards");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    CardsApi apiInstance = new CardsApi(defaultClient);
    Integer appId = 56; // Integer | The ID of the target app.
    try {
      CardListResponse result = apiInstance.getCrmV3ExtensionsCardsAppId(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#getCrmV3ExtensionsCardsAppId");
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
| **appId** | **Integer**| The ID of the target app. | |

### Return type

[**CardListResponse**](CardListResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="getCrmV3ExtensionsCardsAppIdCardId"></a>
# **getCrmV3ExtensionsCardsAppIdCardId**
> CardResponse getCrmV3ExtensionsCardsAppIdCardId(appId, cardId)

Get a card.

Returns the definition for a card with the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com/crm/v3/extensions/cards");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    CardsApi apiInstance = new CardsApi(defaultClient);
    Integer appId = 56; // Integer | The ID of the target app.
    String cardId = "cardId_example"; // String | The ID of the target card.
    try {
      CardResponse result = apiInstance.getCrmV3ExtensionsCardsAppIdCardId(appId, cardId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#getCrmV3ExtensionsCardsAppIdCardId");
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
| **appId** | **Integer**| The ID of the target app. | |
| **cardId** | **String**| The ID of the target card. | |

### Return type

[**CardResponse**](CardResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="patchCrmV3ExtensionsCardsAppIdCardId"></a>
# **patchCrmV3ExtensionsCardsAppIdCardId**
> CardResponse patchCrmV3ExtensionsCardsAppIdCardId(appId, cardId, cardPatchRequest)

Update a card

Update a card definition with new details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com/crm/v3/extensions/cards");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    CardsApi apiInstance = new CardsApi(defaultClient);
    Integer appId = 56; // Integer | The ID of the target app.
    String cardId = "cardId_example"; // String | The ID of the card to update.
    CardPatchRequest cardPatchRequest = new CardPatchRequest(); // CardPatchRequest | Card definition fields to be updated.
    try {
      CardResponse result = apiInstance.patchCrmV3ExtensionsCardsAppIdCardId(appId, cardId, cardPatchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#patchCrmV3ExtensionsCardsAppIdCardId");
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
| **appId** | **Integer**| The ID of the target app. | |
| **cardId** | **String**| The ID of the card to update. | |
| **cardPatchRequest** | [**CardPatchRequest**](CardPatchRequest.md)| Card definition fields to be updated. | |

### Return type

[**CardResponse**](CardResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="postCrmV3ExtensionsCardsAppId"></a>
# **postCrmV3ExtensionsCardsAppId**
> CardResponse postCrmV3ExtensionsCardsAppId(appId, cardCreateRequest)

Create a new card

Defines a new card that will become active on an account when this app is installed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com/crm/v3/extensions/cards");
    
    // Configure API key authorization: developer_hapikey
    ApiKeyAuth developer_hapikey = (ApiKeyAuth) defaultClient.getAuthentication("developer_hapikey");
    developer_hapikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developer_hapikey.setApiKeyPrefix("Token");

    CardsApi apiInstance = new CardsApi(defaultClient);
    Integer appId = 56; // Integer | The ID of the target app.
    CardCreateRequest cardCreateRequest = new CardCreateRequest(); // CardCreateRequest | The new card definition.
    try {
      CardResponse result = apiInstance.postCrmV3ExtensionsCardsAppId(appId, cardCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#postCrmV3ExtensionsCardsAppId");
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
| **appId** | **Integer**| The ID of the target app. | |
| **cardCreateRequest** | [**CardCreateRequest**](CardCreateRequest.md)| The new card definition. | |

### Return type

[**CardResponse**](CardResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | successful operation |  -  |
| **0** | An error occurred. |  -  |

