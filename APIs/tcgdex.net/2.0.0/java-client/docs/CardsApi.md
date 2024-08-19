# CardsApi

All URIs are relative to *https://api.tcgdex.net/v2/en*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cards**](CardsApi.md#cards) | **GET** /cards | fetch the list of cards |
| [**findPetsByTags**](CardsApi.md#findPetsByTags) | **GET** /cards/{cardId} | Finds Card by Global ID |
| [**setsSetCardLocalIdGet**](CardsApi.md#setsSetCardLocalIdGet) | **GET** /sets/{set}/{cardLocalId} |  |


<a id="cards"></a>
# **cards**
> List&lt;CardResume&gt; cards()

fetch the list of cards

desc

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
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    CardsApi apiInstance = new CardsApi(defaultClient);
    try {
      List<CardResume> result = apiInstance.cards();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#cards");
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

[**List&lt;CardResume&gt;**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="findPetsByTags"></a>
# **findPetsByTags**
> Card findPetsByTags(cardId)

Finds Card by Global ID

Find a defined card thatusing its global id

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
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    CardsApi apiInstance = new CardsApi(defaultClient);
    String cardId = "cardId_example"; // String | Tags to filter by
    try {
      Card result = apiInstance.findPetsByTags(cardId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#findPetsByTags");
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
| **cardId** | **String**| Tags to filter by | |

### Return type

[**Card**](Card.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **404** | The Card doesn&#39;t exist |  -  |

<a id="setsSetCardLocalIdGet"></a>
# **setsSetCardLocalIdGet**
> Card setsSetCardLocalIdGet(set, cardLocalId)



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
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    CardsApi apiInstance = new CardsApi(defaultClient);
    String set = "set_example"; // String | 
    String cardLocalId = "cardLocalId_example"; // String | 
    try {
      Card result = apiInstance.setsSetCardLocalIdGet(set, cardLocalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CardsApi#setsSetCardLocalIdGet");
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
| **set** | **String**|  | |
| **cardLocalId** | **String**|  | |

### Return type

[**Card**](Card.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | the Set or cardLocalId are incorrect |  -  |

