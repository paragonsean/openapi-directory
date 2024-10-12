# SkuAttachmentApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtSkuattachmentDelete**](SkuAttachmentApi.md#apiCatalogPvtSkuattachmentDelete) | **DELETE** /api/catalog/pvt/skuattachment | Dissociate attachments and SKUs |
| [**apiCatalogPvtSkuattachmentPost**](SkuAttachmentApi.md#apiCatalogPvtSkuattachmentPost) | **POST** /api/catalog/pvt/skuattachment | Associate SKU Attachment |
| [**apiCatalogPvtSkuattachmentSkuAttachmentAssociationIdDelete**](SkuAttachmentApi.md#apiCatalogPvtSkuattachmentSkuAttachmentAssociationIdDelete) | **DELETE** /api/catalog/pvt/skuattachment/{skuAttachmentAssociationId} | Delete SKU Attachment by Attachment Association ID |
| [**apiCatalogPvtStockkeepingunitSkuIdAttachmentGet**](SkuAttachmentApi.md#apiCatalogPvtStockkeepingunitSkuIdAttachmentGet) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/attachment | Get SKU Attachments by SKU ID |
| [**associateattachmentstoSKU**](SkuAttachmentApi.md#associateattachmentstoSKU) | **POST** /api/catalog_system/pvt/sku/associateattachments | Associate attachments to an SKU |


<a id="apiCatalogPvtSkuattachmentDelete"></a>
# **apiCatalogPvtSkuattachmentDelete**
> apiCatalogPvtSkuattachmentDelete(contentType, accept, skuId, attachmentId)

Dissociate attachments and SKUs

Dissociates attachments and SKUs based on an SKU ID or an attachment ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuAttachmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SkuAttachmentApi apiInstance = new SkuAttachmentApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 1; // Integer | SKU ID. By using this query param, you can dissociate all the attachments from an SKU based on its SKU ID.
    Integer attachmentId = 1; // Integer | Attachment ID. By using this query param, you can dissociate the given attachment from all previously associated SKUs.
    try {
      apiInstance.apiCatalogPvtSkuattachmentDelete(contentType, accept, skuId, attachmentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuAttachmentApi#apiCatalogPvtSkuattachmentDelete");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **skuId** | **Integer**| SKU ID. By using this query param, you can dissociate all the attachments from an SKU based on its SKU ID. | [optional] |
| **attachmentId** | **Integer**| Attachment ID. By using this query param, you can dissociate the given attachment from all previously associated SKUs. | [optional] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSkuattachmentPost"></a>
# **apiCatalogPvtSkuattachmentPost**
> ApiCatalogPvtSkuattachmentPost200Response apiCatalogPvtSkuattachmentPost(contentType, accept, requestBody1)

Associate SKU Attachment

Associates an existing SKU to an existing Attachment.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;AttachmentId\&quot;: 1,      \&quot;SkuId\&quot;: 7  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 31,      \&quot;AttachmentId\&quot;: 1,      \&quot;SkuId\&quot;: 7  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuAttachmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SkuAttachmentApi apiInstance = new SkuAttachmentApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    RequestBody1 requestBody1 = new RequestBody1(); // RequestBody1 | 
    try {
      ApiCatalogPvtSkuattachmentPost200Response result = apiInstance.apiCatalogPvtSkuattachmentPost(contentType, accept, requestBody1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuAttachmentApi#apiCatalogPvtSkuattachmentPost");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **requestBody1** | [**RequestBody1**](RequestBody1.md)|  | [optional] |

### Return type

[**ApiCatalogPvtSkuattachmentPost200Response**](ApiCatalogPvtSkuattachmentPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSkuattachmentSkuAttachmentAssociationIdDelete"></a>
# **apiCatalogPvtSkuattachmentSkuAttachmentAssociationIdDelete**
> apiCatalogPvtSkuattachmentSkuAttachmentAssociationIdDelete(contentType, accept, skuAttachmentAssociationId)

Delete SKU Attachment by Attachment Association ID

Deletes the association of an SKU to an Attachment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuAttachmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SkuAttachmentApi apiInstance = new SkuAttachmentApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuAttachmentAssociationId = 1; // Integer | ID of the association between the attachment and the SKU, which corresponds to the `Id` in the response body of the [Associate SKU Attachment](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-sku-attachment) and the [Get SKU Attachment by SKU ID](https://developers.vtex.com/vtex-rest-api/reference/get_api-catalog-pvt-stockkeepingunit-skuid-attachment) endpoints.
    try {
      apiInstance.apiCatalogPvtSkuattachmentSkuAttachmentAssociationIdDelete(contentType, accept, skuAttachmentAssociationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuAttachmentApi#apiCatalogPvtSkuattachmentSkuAttachmentAssociationIdDelete");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **skuAttachmentAssociationId** | **Integer**| ID of the association between the attachment and the SKU, which corresponds to the &#x60;Id&#x60; in the response body of the [Associate SKU Attachment](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-sku-attachment) and the [Get SKU Attachment by SKU ID](https://developers.vtex.com/vtex-rest-api/reference/get_api-catalog-pvt-stockkeepingunit-skuid-attachment) endpoints. | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtStockkeepingunitSkuIdAttachmentGet"></a>
# **apiCatalogPvtStockkeepingunitSkuIdAttachmentGet**
> List&lt;ApiCatalogPvtSkuattachmentPost200Response&gt; apiCatalogPvtStockkeepingunitSkuIdAttachmentGet(contentType, accept, skuId)

Get SKU Attachments by SKU ID

Retrieves existing SKU Attachments by SKU ID.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 97,          \&quot;AttachmentId\&quot;: 1,          \&quot;SkuId\&quot;: 1      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuAttachmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SkuAttachmentApi apiInstance = new SkuAttachmentApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 1; // Integer | SKU unique identifier.
    try {
      List<ApiCatalogPvtSkuattachmentPost200Response> result = apiInstance.apiCatalogPvtStockkeepingunitSkuIdAttachmentGet(contentType, accept, skuId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuAttachmentApi#apiCatalogPvtStockkeepingunitSkuIdAttachmentGet");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **skuId** | **Integer**| SKU unique identifier. | |

### Return type

[**List&lt;ApiCatalogPvtSkuattachmentPost200Response&gt;**](ApiCatalogPvtSkuattachmentPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="associateattachmentstoSKU"></a>
# **associateattachmentstoSKU**
> associateattachmentstoSKU(contentType, accept, associateattachmentstoSKURequest)

Associate attachments to an SKU

Associates attachments to an SKU based on a given SKU ID and attachment names.  This request removes existing SKU attachment associations and recreates the associations with the attachments being sent.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuId\&quot;: 1,      \&quot;AttachmentNames\&quot;: [          \&quot;T-Shirt Customization\&quot;      ]  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuAttachmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SkuAttachmentApi apiInstance = new SkuAttachmentApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    AssociateattachmentstoSKURequest associateattachmentstoSKURequest = new AssociateattachmentstoSKURequest(); // AssociateattachmentstoSKURequest | 
    try {
      apiInstance.associateattachmentstoSKU(contentType, accept, associateattachmentstoSKURequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuAttachmentApi#associateattachmentstoSKU");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **associateattachmentstoSKURequest** | [**AssociateattachmentstoSKURequest**](AssociateattachmentstoSKURequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

