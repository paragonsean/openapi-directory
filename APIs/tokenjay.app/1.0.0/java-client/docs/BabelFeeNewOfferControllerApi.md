# BabelFeeNewOfferControllerApi

All URIs are relative to *https://api.tokenjay.app*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**doCreateBabelBox**](BabelFeeNewOfferControllerApi.md#doCreateBabelBox) | **POST** /mosaik/babelfee/newoffer/doit |  |
| [**ergoPayCreateBabelBox**](BabelFeeNewOfferControllerApi.md#ergoPayCreateBabelBox) | **GET** /createbabel/{address} |  |
| [**getBabelFeeNewOffer**](BabelFeeNewOfferControllerApi.md#getBabelFeeNewOffer) | **GET** /mosaik/babelfee/newoffer |  |
| [**replaceTokenAmountInputFields**](BabelFeeNewOfferControllerApi.md#replaceTokenAmountInputFields) | **POST** /mosaik/babelfee/newoffer/new-input |  |


<a id="doCreateBabelBox"></a>
# **doCreateBabelBox**
> FetchActionResponse doCreateBabelBox(requestBody)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BabelFeeNewOfferControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    BabelFeeNewOfferControllerApi apiInstance = new BabelFeeNewOfferControllerApi(defaultClient);
    Map<String, Object> requestBody = null; // Map<String, Object> | 
    try {
      FetchActionResponse result = apiInstance.doCreateBabelBox(requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BabelFeeNewOfferControllerApi#doCreateBabelBox");
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
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)|  | |

### Return type

[**FetchActionResponse**](FetchActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

<a id="ergoPayCreateBabelBox"></a>
# **ergoPayCreateBabelBox**
> ErgoPayResponse ergoPayCreateBabelBox(address, tokenId, ergAmount, tokenAmount)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BabelFeeNewOfferControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    BabelFeeNewOfferControllerApi apiInstance = new BabelFeeNewOfferControllerApi(defaultClient);
    String address = "address_example"; // String | 
    String tokenId = "tokenId_example"; // String | 
    Long ergAmount = 56L; // Long | 
    Long tokenAmount = 56L; // Long | 
    try {
      ErgoPayResponse result = apiInstance.ergoPayCreateBabelBox(address, tokenId, ergAmount, tokenAmount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BabelFeeNewOfferControllerApi#ergoPayCreateBabelBox");
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
| **address** | **String**|  | |
| **tokenId** | **String**|  | |
| **ergAmount** | **Long**|  | |
| **tokenAmount** | **Long**|  | |

### Return type

[**ErgoPayResponse**](ErgoPayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

<a id="getBabelFeeNewOffer"></a>
# **getBabelFeeNewOffer**
> MosaikApp getBabelFeeNewOffer()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BabelFeeNewOfferControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    BabelFeeNewOfferControllerApi apiInstance = new BabelFeeNewOfferControllerApi(defaultClient);
    try {
      MosaikApp result = apiInstance.getBabelFeeNewOffer();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BabelFeeNewOfferControllerApi#getBabelFeeNewOffer");
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

[**MosaikApp**](MosaikApp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

<a id="replaceTokenAmountInputFields"></a>
# **replaceTokenAmountInputFields**
> FetchActionResponse replaceTokenAmountInputFields(requestBody)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BabelFeeNewOfferControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    BabelFeeNewOfferControllerApi apiInstance = new BabelFeeNewOfferControllerApi(defaultClient);
    Map<String, Object> requestBody = null; // Map<String, Object> | 
    try {
      FetchActionResponse result = apiInstance.replaceTokenAmountInputFields(requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BabelFeeNewOfferControllerApi#replaceTokenAmountInputFields");
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
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)|  | |

### Return type

[**FetchActionResponse**](FetchActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

