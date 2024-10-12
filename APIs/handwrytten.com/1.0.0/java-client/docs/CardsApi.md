# CardsApi

All URIs are relative to *https://api.handwrytten.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**filterableCardDetails**](CardsApi.md#filterableCardDetails) | **POST** /cards/view | Provides full information on a specific card |
| [**listCards**](CardsApi.md#listCards) | **POST** /cards/list | Lists information on cards |
| [**simpleListCards**](CardsApi.md#simpleListCards) | **GET** /cards/list | Lists information on cards |


<a id="filterableCardDetails"></a>
# **filterableCardDetails**
> CardDetails filterableCardDetails(body)

Provides full information on a specific card

Full card details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    CardsApi apiInstance = new CardsApi(defaultClient);
    FilterableCardDetailsRequest body = new FilterableCardDetailsRequest(); // FilterableCardDetailsRequest | additional parameters
    try {
      CardDetails result = apiInstance.filterableCardDetails(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#filterableCardDetails");
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
| **body** | [**FilterableCardDetailsRequest**](FilterableCardDetailsRequest.md)| additional parameters | [optional] |

### Return type

[**CardDetails**](CardDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="listCards"></a>
# **listCards**
> List&lt;Card&gt; listCards(body)

Lists information on cards

Simple listing of cards.  No filters can be applied.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    CardsApi apiInstance = new CardsApi(defaultClient);
    ListCardsRequest body = new ListCardsRequest(); // ListCardsRequest | additional parameters
    try {
      List<Card> result = apiInstance.listCards(body);
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
| **body** | [**ListCardsRequest**](ListCardsRequest.md)| additional parameters | [optional] |

### Return type

[**List&lt;Card&gt;**](Card.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid status value |  -  |

<a id="simpleListCards"></a>
# **simpleListCards**
> List&lt;Card&gt; simpleListCards()

Lists information on cards

Filterable card list.  If called with UID will also provide user-specific cards.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CardsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    CardsApi apiInstance = new CardsApi(defaultClient);
    try {
      List<Card> result = apiInstance.simpleListCards();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#simpleListCards");
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

[**List&lt;Card&gt;**](Card.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid status value |  -  |

