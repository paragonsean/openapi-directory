# CardsApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCard**](CardsApi.md#createCard) | **POST** /v2/cards | CreateCard |
| [**disableCard**](CardsApi.md#disableCard) | **POST** /v2/cards/{card_id}/disable | DisableCard |
| [**listCards**](CardsApi.md#listCards) | **GET** /v2/cards | ListCards |
| [**retrieveCard**](CardsApi.md#retrieveCard) | **GET** /v2/cards/{card_id} | RetrieveCard |


<a id="createCard"></a>
# **createCard**
> CreateCardResponse createCard(createCardRequest)

CreateCard

Adds a card on file to an existing merchant.

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
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CardsApi apiInstance = new CardsApi(defaultClient);
    CreateCardRequest createCardRequest = new CreateCardRequest(); // CreateCardRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CreateCardResponse result = apiInstance.createCard(createCardRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#createCard");
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
| **createCardRequest** | [**CreateCardRequest**](CreateCardRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CreateCardResponse**](CreateCardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="disableCard"></a>
# **disableCard**
> DisableCardResponse disableCard(cardId)

DisableCard

Disables the card, preventing any further updates or charges. Disabling an already disabled card is allowed but has no effect.

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
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CardsApi apiInstance = new CardsApi(defaultClient);
    String cardId = "cardId_example"; // String | Unique ID for the desired Card.
    try {
      DisableCardResponse result = apiInstance.disableCard(cardId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#disableCard");
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
| **cardId** | **String**| Unique ID for the desired Card. | |

### Return type

[**DisableCardResponse**](DisableCardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listCards"></a>
# **listCards**
> ListCardsResponse listCards(cursor, customerId, includeDisabled, referenceId, sortOrder)

ListCards

Retrieves a list of cards owned by the account making the request. A max of 25 cards will be returned.

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
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CardsApi apiInstance = new CardsApi(defaultClient);
    String cursor = "cursor_example"; // String | A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query.  See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.
    String customerId = "customerId_example"; // String | Limit results to cards associated with the customer supplied. By default, all cards owned by the merchant are returned.
    Boolean includeDisabled = true; // Boolean | Includes disabled cards. By default, all enabled cards owned by the merchant are returned.
    String referenceId = "referenceId_example"; // String | Limit results to cards associated with the reference_id supplied.
    String sortOrder = "sortOrder_example"; // String | Sorts the returned list by when the card was created with the specified order. This field defaults to ASC.
    try {
      ListCardsResponse result = apiInstance.listCards(cursor, customerId, includeDisabled, referenceId, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#listCards");
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
| **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query.  See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. | [optional] |
| **customerId** | **String**| Limit results to cards associated with the customer supplied. By default, all cards owned by the merchant are returned. | [optional] |
| **includeDisabled** | **Boolean**| Includes disabled cards. By default, all enabled cards owned by the merchant are returned. | [optional] |
| **referenceId** | **String**| Limit results to cards associated with the reference_id supplied. | [optional] |
| **sortOrder** | **String**| Sorts the returned list by when the card was created with the specified order. This field defaults to ASC. | [optional] |

### Return type

[**ListCardsResponse**](ListCardsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveCard"></a>
# **retrieveCard**
> RetrieveCardResponse retrieveCard(cardId)

RetrieveCard

Retrieves details for a specific Card.

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
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CardsApi apiInstance = new CardsApi(defaultClient);
    String cardId = "cardId_example"; // String | Unique ID for the desired Card.
    try {
      RetrieveCardResponse result = apiInstance.retrieveCard(cardId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#retrieveCard");
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
| **cardId** | **String**| Unique ID for the desired Card. | |

### Return type

[**RetrieveCardResponse**](RetrieveCardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

