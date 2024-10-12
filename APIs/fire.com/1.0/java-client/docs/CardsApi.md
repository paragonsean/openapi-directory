# CardsApi

All URIs are relative to *https://api.fire.com/business*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**blockCard**](CardsApi.md#blockCard) | **POST** /v1/cards/{cardId}/block | Block a card |
| [**createNewCard**](CardsApi.md#createNewCard) | **POST** /v1/cards | Create a new debit card. |
| [**getListofCardTransactions**](CardsApi.md#getListofCardTransactions) | **GET** /v1/cards/{cardId}/transactions | List Card Transactions. |
| [**getListofCards**](CardsApi.md#getListofCards) | **GET** /v1/cards | View List of Cards. |
| [**unblockCard**](CardsApi.md#unblockCard) | **POST** /v1/cards/{cardId}/unblock | Unblock a card |


<a id="blockCard"></a>
# **blockCard**
> blockCard(cardId)

Block a card

Updates status of an existing card to block which prevents any transactions being carried out with that card.

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
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    CardsApi apiInstance = new CardsApi(defaultClient);
    Long cardId = 56L; // Long | 
    try {
      apiInstance.blockCard(cardId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#blockCard");
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
| **cardId** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No body is returned - “Status 204 No Content” signifies the call was successful. |  -  |

<a id="createNewCard"></a>
# **createNewCard**
> NewCardResponse createNewCard(newCard)

Create a new debit card.

You can create multiple debit cards which can be linked to your fire.com accounts.

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
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    CardsApi apiInstance = new CardsApi(defaultClient);
    NewCard newCard = new NewCard(); // NewCard | Details of the new card
    try {
      NewCardResponse result = apiInstance.createNewCard(newCard);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#createNewCard");
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
| **newCard** | [**NewCard**](NewCard.md)| Details of the new card | |

### Return type

[**NewCardResponse**](NewCardResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Card created successfully |  -  |

<a id="getListofCardTransactions"></a>
# **getListofCardTransactions**
> List&lt;CardTransactionsv1&gt; getListofCardTransactions(cardId, limit, offset)

List Card Transactions.

Returns a list of cards transactions related to your fire.com card.

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
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    CardsApi apiInstance = new CardsApi(defaultClient);
    Long cardId = 56L; // Long | 
    Long limit = 56L; // Long | 
    Long offset = 56L; // Long | 
    try {
      List<CardTransactionsv1> result = apiInstance.getListofCardTransactions(cardId, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#getListofCardTransactions");
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
| **cardId** | **Long**|  | |
| **limit** | **Long**|  | [optional] |
| **offset** | **Long**|  | [optional] |

### Return type

[**List&lt;CardTransactionsv1&gt;**](CardTransactionsv1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **401** | Access Token is Invalid or missing |  -  |
| **403** | Access Token is Invalid or missing |  -  |

<a id="getListofCards"></a>
# **getListofCards**
> Cards getListofCards()

View List of Cards.

Returns a list of cards related to your fire.com account.

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
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    CardsApi apiInstance = new CardsApi(defaultClient);
    try {
      Cards result = apiInstance.getListofCards();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#getListofCards");
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

[**Cards**](Cards.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **401** | Access Token is Invalid or missing |  -  |
| **403** | Access Token is Invalid or missing |  -  |

<a id="unblockCard"></a>
# **unblockCard**
> unblockCard(cardId)

Unblock a card

Updates status of an existing card to unblock which means that transactions can be carried out with that card.

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
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    CardsApi apiInstance = new CardsApi(defaultClient);
    Long cardId = 56L; // Long | 
    try {
      apiInstance.unblockCard(cardId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#unblockCard");
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
| **cardId** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No body is returned - “Status 204 No Content” signifies the call was successful. |  -  |

