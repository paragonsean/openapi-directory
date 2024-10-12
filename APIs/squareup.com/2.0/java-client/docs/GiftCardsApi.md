# GiftCardsApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createGiftCard**](GiftCardsApi.md#createGiftCard) | **POST** /v2/gift-cards | CreateGiftCard |
| [**linkCustomerToGiftCard**](GiftCardsApi.md#linkCustomerToGiftCard) | **POST** /v2/gift-cards/{gift_card_id}/link-customer | LinkCustomerToGiftCard |
| [**listGiftCards**](GiftCardsApi.md#listGiftCards) | **GET** /v2/gift-cards | ListGiftCards |
| [**retrieveGiftCard**](GiftCardsApi.md#retrieveGiftCard) | **GET** /v2/gift-cards/{id} | RetrieveGiftCard |
| [**retrieveGiftCardFromGAN**](GiftCardsApi.md#retrieveGiftCardFromGAN) | **POST** /v2/gift-cards/from-gan | RetrieveGiftCardFromGAN |
| [**retrieveGiftCardFromNonce**](GiftCardsApi.md#retrieveGiftCardFromNonce) | **POST** /v2/gift-cards/from-nonce | RetrieveGiftCardFromNonce |
| [**unlinkCustomerFromGiftCard**](GiftCardsApi.md#unlinkCustomerFromGiftCard) | **POST** /v2/gift-cards/{gift_card_id}/unlink-customer | UnlinkCustomerFromGiftCard |


<a id="createGiftCard"></a>
# **createGiftCard**
> CreateGiftCardResponse createGiftCard(createGiftCardRequest)

CreateGiftCard

Creates a digital gift card or registers a physical (plastic) gift card. You must activate the gift card before  it can be used for payment. For more information, see  [Selling gift cards](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#selling-square-gift-cards).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftCardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GiftCardsApi apiInstance = new GiftCardsApi(defaultClient);
    CreateGiftCardRequest createGiftCardRequest = new CreateGiftCardRequest(); // CreateGiftCardRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CreateGiftCardResponse result = apiInstance.createGiftCard(createGiftCardRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftCardsApi#createGiftCard");
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
| **createGiftCardRequest** | [**CreateGiftCardRequest**](CreateGiftCardRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CreateGiftCardResponse**](CreateGiftCardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="linkCustomerToGiftCard"></a>
# **linkCustomerToGiftCard**
> LinkCustomerToGiftCardResponse linkCustomerToGiftCard(giftCardId, linkCustomerToGiftCardRequest)

LinkCustomerToGiftCard

Links a customer to a gift card

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftCardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GiftCardsApi apiInstance = new GiftCardsApi(defaultClient);
    String giftCardId = "giftCardId_example"; // String | The ID of the gift card to link.
    LinkCustomerToGiftCardRequest linkCustomerToGiftCardRequest = new LinkCustomerToGiftCardRequest(); // LinkCustomerToGiftCardRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      LinkCustomerToGiftCardResponse result = apiInstance.linkCustomerToGiftCard(giftCardId, linkCustomerToGiftCardRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftCardsApi#linkCustomerToGiftCard");
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
| **giftCardId** | **String**| The ID of the gift card to link. | |
| **linkCustomerToGiftCardRequest** | [**LinkCustomerToGiftCardRequest**](LinkCustomerToGiftCardRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**LinkCustomerToGiftCardResponse**](LinkCustomerToGiftCardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listGiftCards"></a>
# **listGiftCards**
> ListGiftCardsResponse listGiftCards(type, state, limit, cursor, customerId)

ListGiftCards

Lists all gift cards. You can specify optional filters to retrieve  a subset of the gift cards.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftCardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GiftCardsApi apiInstance = new GiftCardsApi(defaultClient);
    String type = "type_example"; // String | If a type is provided, gift cards of this type are returned  (see [GiftCardType](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardType)). If no type is provided, it returns gift cards of all types.
    String state = "state_example"; // String | If the state is provided, it returns the gift cards in the specified state  (see [GiftCardStatus](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardStatus)). Otherwise, it returns the gift cards of all states.
    Integer limit = 56; // Integer | If a value is provided, it returns only that number of results per page. The maximum number of results allowed per page is 50. The default value is 30.
    String cursor = "cursor_example"; // String | A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. If a cursor is not provided, it returns the first page of the results.  For more information, see [Pagination](https://developer.squareup.com/docs/docs/working-with-apis/pagination).
    String customerId = "customerId_example"; // String | If a value is provided, returns only the gift cards linked to the specified customer
    try {
      ListGiftCardsResponse result = apiInstance.listGiftCards(type, state, limit, cursor, customerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftCardsApi#listGiftCards");
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
| **type** | **String**| If a type is provided, gift cards of this type are returned  (see [GiftCardType](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardType)). If no type is provided, it returns gift cards of all types. | [optional] |
| **state** | **String**| If the state is provided, it returns the gift cards in the specified state  (see [GiftCardStatus](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardStatus)). Otherwise, it returns the gift cards of all states. | [optional] |
| **limit** | **Integer**| If a value is provided, it returns only that number of results per page. The maximum number of results allowed per page is 50. The default value is 30. | [optional] |
| **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. If a cursor is not provided, it returns the first page of the results.  For more information, see [Pagination](https://developer.squareup.com/docs/docs/working-with-apis/pagination). | [optional] |
| **customerId** | **String**| If a value is provided, returns only the gift cards linked to the specified customer | [optional] |

### Return type

[**ListGiftCardsResponse**](ListGiftCardsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveGiftCard"></a>
# **retrieveGiftCard**
> RetrieveGiftCardResponse retrieveGiftCard(id)

RetrieveGiftCard

Retrieves a gift card using its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftCardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GiftCardsApi apiInstance = new GiftCardsApi(defaultClient);
    String id = "id_example"; // String | The ID of the gift card to retrieve.
    try {
      RetrieveGiftCardResponse result = apiInstance.retrieveGiftCard(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftCardsApi#retrieveGiftCard");
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
| **id** | **String**| The ID of the gift card to retrieve. | |

### Return type

[**RetrieveGiftCardResponse**](RetrieveGiftCardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveGiftCardFromGAN"></a>
# **retrieveGiftCardFromGAN**
> RetrieveGiftCardFromGANResponse retrieveGiftCardFromGAN(retrieveGiftCardFromGANRequest)

RetrieveGiftCardFromGAN

Retrieves a gift card using the gift card account number (GAN).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftCardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GiftCardsApi apiInstance = new GiftCardsApi(defaultClient);
    RetrieveGiftCardFromGANRequest retrieveGiftCardFromGANRequest = new RetrieveGiftCardFromGANRequest(); // RetrieveGiftCardFromGANRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      RetrieveGiftCardFromGANResponse result = apiInstance.retrieveGiftCardFromGAN(retrieveGiftCardFromGANRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftCardsApi#retrieveGiftCardFromGAN");
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
| **retrieveGiftCardFromGANRequest** | [**RetrieveGiftCardFromGANRequest**](RetrieveGiftCardFromGANRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**RetrieveGiftCardFromGANResponse**](RetrieveGiftCardFromGANResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveGiftCardFromNonce"></a>
# **retrieveGiftCardFromNonce**
> RetrieveGiftCardFromNonceResponse retrieveGiftCardFromNonce(retrieveGiftCardFromNonceRequest)

RetrieveGiftCardFromNonce

Retrieves a gift card using a nonce (a secure token) that represents the gift card.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftCardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GiftCardsApi apiInstance = new GiftCardsApi(defaultClient);
    RetrieveGiftCardFromNonceRequest retrieveGiftCardFromNonceRequest = new RetrieveGiftCardFromNonceRequest(); // RetrieveGiftCardFromNonceRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      RetrieveGiftCardFromNonceResponse result = apiInstance.retrieveGiftCardFromNonce(retrieveGiftCardFromNonceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftCardsApi#retrieveGiftCardFromNonce");
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
| **retrieveGiftCardFromNonceRequest** | [**RetrieveGiftCardFromNonceRequest**](RetrieveGiftCardFromNonceRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**RetrieveGiftCardFromNonceResponse**](RetrieveGiftCardFromNonceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="unlinkCustomerFromGiftCard"></a>
# **unlinkCustomerFromGiftCard**
> UnlinkCustomerFromGiftCardResponse unlinkCustomerFromGiftCard(giftCardId, unlinkCustomerFromGiftCardRequest)

UnlinkCustomerFromGiftCard

Unlinks a customer from a gift card

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftCardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    GiftCardsApi apiInstance = new GiftCardsApi(defaultClient);
    String giftCardId = "giftCardId_example"; // String | 
    UnlinkCustomerFromGiftCardRequest unlinkCustomerFromGiftCardRequest = new UnlinkCustomerFromGiftCardRequest(); // UnlinkCustomerFromGiftCardRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      UnlinkCustomerFromGiftCardResponse result = apiInstance.unlinkCustomerFromGiftCard(giftCardId, unlinkCustomerFromGiftCardRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftCardsApi#unlinkCustomerFromGiftCard");
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
| **giftCardId** | **String**|  | |
| **unlinkCustomerFromGiftCardRequest** | [**UnlinkCustomerFromGiftCardRequest**](UnlinkCustomerFromGiftCardRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**UnlinkCustomerFromGiftCardResponse**](UnlinkCustomerFromGiftCardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

