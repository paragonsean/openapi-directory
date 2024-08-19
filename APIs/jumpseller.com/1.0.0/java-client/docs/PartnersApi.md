# PartnersApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**partnersStoresJsonGet**](PartnersApi.md#partnersStoresJsonGet) | **GET** /partners/stores.json | Retrieve statistics. |
| [**storeCheckStatusJsonGet**](PartnersApi.md#storeCheckStatusJsonGet) | **GET** /store/check_status.json | Retrive store creation status. |
| [**storeCreateJsonPost**](PartnersApi.md#storeCreateJsonPost) | **POST** /store/create.json | Create a Partnered Store |


<a id="partnersStoresJsonGet"></a>
# **partnersStoresJsonGet**
> List&lt;Type&gt; partnersStoresJsonGet(partnerCode, authToken, from, to, page)

Retrieve statistics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String partnerCode = "partnerCode_example"; // String | Partner code.
    String authToken = "authToken_example"; // String | Partner authentication token.
    String from = "from_example"; // String | Statistics start date. Should be in format 'Y-m-d'.
    String to = "to_example"; // String | Statistics end date. Should be in format 'Y-m-d'.
    Integer page = 1; // Integer | List page
    try {
      List<Type> result = apiInstance.partnersStoresJsonGet(partnerCode, authToken, from, to, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#partnersStoresJsonGet");
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
| **partnerCode** | **String**| Partner code. | |
| **authToken** | **String**| Partner authentication token. | |
| **from** | **String**| Statistics start date. Should be in format &#39;Y-m-d&#39;. | |
| **to** | **String**| Statistics end date. Should be in format &#39;Y-m-d&#39;. | |
| **page** | **Integer**| List page | [optional] [default to 1] |

### Return type

[**List&lt;Type&gt;**](Type.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of partner stores statistics. |  -  |
| **400** | Bad Request. |  -  |

<a id="storeCheckStatusJsonGet"></a>
# **storeCheckStatusJsonGet**
> StoreCheckStatusJsonGet200Response storeCheckStatusJsonGet(partnerCode, authToken, storeCode, locale)

Retrive store creation status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String partnerCode = "partnerCode_example"; // String | Partner code.
    String authToken = "authToken_example"; // String | Partner authentication token.
    String storeCode = "storeCode_example"; // String | Store Code
    String locale = "en"; // String | ISO 3166-2 code of the language used in the response messages.
    try {
      StoreCheckStatusJsonGet200Response result = apiInstance.storeCheckStatusJsonGet(partnerCode, authToken, storeCode, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#storeCheckStatusJsonGet");
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
| **partnerCode** | **String**| Partner code. | |
| **authToken** | **String**| Partner authentication token. | |
| **storeCode** | **String**| Store Code | |
| **locale** | **String**| ISO 3166-2 code of the language used in the response messages. | [optional] [default to en] |

### Return type

[**StoreCheckStatusJsonGet200Response**](StoreCheckStatusJsonGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Store status object if creation is still in progress. A new Partner Store object when creation is done. |  -  |
| **400** | Bad Request. |  -  |

<a id="storeCreateJsonPost"></a>
# **storeCreateJsonPost**
> PartnerStoreCode storeCreateJsonPost(partnerCode, authToken, partnerStoreCreate)

Create a Partnered Store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String partnerCode = "partnerCode_example"; // String | Partner code.
    String authToken = "authToken_example"; // String | Partner authentication token.
    PartnerStoreCreate partnerStoreCreate = new PartnerStoreCreate(); // PartnerStoreCreate | New partnered Store parameters.
    try {
      PartnerStoreCode result = apiInstance.storeCreateJsonPost(partnerCode, authToken, partnerStoreCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#storeCreateJsonPost");
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
| **partnerCode** | **String**| Partner code. | |
| **authToken** | **String**| Partner authentication token. | |
| **partnerStoreCreate** | [**PartnerStoreCreate**](PartnerStoreCreate.md)| New partnered Store parameters. | |

### Return type

[**PartnerStoreCode**](PartnerStoreCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Partner Store object. |  -  |
| **400** | Bad Request. |  -  |

