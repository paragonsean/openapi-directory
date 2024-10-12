# OmInvoiceApiGenerationApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**generateBatchOrderInvoice**](OmInvoiceApiGenerationApi.md#generateBatchOrderInvoice) | **POST** /v2/user/marketplaces/orders/invoices/generate | Generate an Order Invoice batch |
| [**generateOrderInvoice**](OmInvoiceApiGenerationApi.md#generateOrderInvoice) | **POST** /v2/user/marketplaces/orders/invoices/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderUUID}/generate | Generate an Order Invoice |
| [**getOrderInvoicePdf**](OmInvoiceApiGenerationApi.md#getOrderInvoicePdf) | **POST** /v2/user/marketplaces/orders/invoices/getPdfInvoice | Returns the PDF version of the invoice |
| [**getOrderInvoicePreview**](OmInvoiceApiGenerationApi.md#getOrderInvoicePreview) | **POST** /v2/user/marketplaces/orders/invoices/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderUUID}/preview | View a preview an Order Invoice |


<a id="generateBatchOrderInvoice"></a>
# **generateBatchOrderInvoice**
> List&lt;GenerateOrderInvoiceResponse&gt; generateBatchOrderInvoice(userName, generateBatchOrderInvoiceRequestItem)

Generate an Order Invoice batch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OmInvoiceApiGenerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    OmInvoiceApiGenerationApi apiInstance = new OmInvoiceApiGenerationApi(defaultClient);
    String userName = "userName_example"; // String | Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application's user login.
    List<GenerateBatchOrderInvoiceRequestItem> generateBatchOrderInvoiceRequestItem = Arrays.asList(); // List<GenerateBatchOrderInvoiceRequestItem> | 
    try {
      List<GenerateOrderInvoiceResponse> result = apiInstance.generateBatchOrderInvoice(userName, generateBatchOrderInvoiceRequestItem);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OmInvoiceApiGenerationApi#generateBatchOrderInvoice");
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
| **userName** | **String**| Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application&#39;s user login. | |
| **generateBatchOrderInvoiceRequestItem** | [**List&lt;GenerateBatchOrderInvoiceRequestItem&gt;**](GenerateBatchOrderInvoiceRequestItem.md)|  | |

### Return type

[**List&lt;GenerateOrderInvoiceResponse&gt;**](GenerateOrderInvoiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The locations of the generated invoice. Might take a few seconds to be available |  -  |
| **400** | GenerateBatchOrderInvoiceErrorResponse |  -  |
| **403** | OwnerId not authorized The required order invoice settings have not been set BeezUPOrderStatus forbidden  |  -  |
| **404** | The order cannot be retrieved  |  -  |
| **409** | The InvoiceNumber is already used There is already an invoice for this order  |  -  |
| **429** | Too many Requests. Please retry in a few seconds  |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="generateOrderInvoice"></a>
# **generateOrderInvoice**
> generateOrderInvoice(marketplaceTechnicalCode, accountId, beezUPOrderUUID, userName, generateOrderInvoiceRequest)

Generate an Order Invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OmInvoiceApiGenerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    OmInvoiceApiGenerationApi apiInstance = new OmInvoiceApiGenerationApi(defaultClient);
    String marketplaceTechnicalCode = "marketplaceTechnicalCode_example"; // String | The Marketplace Technical Code
    String accountId = "accountId_example"; // String | The Account Identifier
    String beezUPOrderUUID = "beezUPOrderUUID_example"; // String | The BeezUP Order UUID
    String userName = "userName_example"; // String | Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application's user login.
    GenerateOrderInvoiceRequest generateOrderInvoiceRequest = new GenerateOrderInvoiceRequest(); // GenerateOrderInvoiceRequest | 
    try {
      apiInstance.generateOrderInvoice(marketplaceTechnicalCode, accountId, beezUPOrderUUID, userName, generateOrderInvoiceRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling OmInvoiceApiGenerationApi#generateOrderInvoice");
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
| **marketplaceTechnicalCode** | **String**| The Marketplace Technical Code | |
| **accountId** | **String**| The Account Identifier | |
| **beezUPOrderUUID** | **String**| The BeezUP Order UUID | |
| **userName** | **String**| Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application&#39;s user login. | |
| **generateOrderInvoiceRequest** | [**GenerateOrderInvoiceRequest**](GenerateOrderInvoiceRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Request Accepted. |  * Location - The location of the generated invoice. Might take a few seconds to be available <br>  |
| **403** | OwnerId not authorized The required order invoice settings have not been set BeezUPOrderStatus forbidden  |  -  |
| **404** | The order cannot be retrieved  |  -  |
| **409** | The InvoiceNumber is already used There is already an invoice for this order  |  -  |
| **429** | Too many Requests. Please retry in a few seconds  |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getOrderInvoicePdf"></a>
# **getOrderInvoicePdf**
> File getOrderInvoicePdf(getOrderInvoicePdfFromHtmlInvoiceUrlRequest)

Returns the PDF version of the invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OmInvoiceApiGenerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    OmInvoiceApiGenerationApi apiInstance = new OmInvoiceApiGenerationApi(defaultClient);
    GetOrderInvoicePdfFromHtmlInvoiceUrlRequest getOrderInvoicePdfFromHtmlInvoiceUrlRequest = new GetOrderInvoicePdfFromHtmlInvoiceUrlRequest(); // GetOrderInvoicePdfFromHtmlInvoiceUrlRequest | 
    try {
      File result = apiInstance.getOrderInvoicePdf(getOrderInvoicePdfFromHtmlInvoiceUrlRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OmInvoiceApiGenerationApi#getOrderInvoicePdf");
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
| **getOrderInvoicePdfFromHtmlInvoiceUrlRequest** | [**GetOrderInvoicePdfFromHtmlInvoiceUrlRequest**](GetOrderInvoicePdfFromHtmlInvoiceUrlRequest.md)|  | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The PDF version of the HTML invoice URL in the request |  -  |
| **403** | The ownerId is not found or not authorized |  -  |
| **404** | The order invoice does not exist  |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getOrderInvoicePreview"></a>
# **getOrderInvoicePreview**
> PreviewOrderInvoiceResponse getOrderInvoicePreview(marketplaceTechnicalCode, accountId, beezUPOrderUUID, acceptEncoding, previewOrderInvoiceRequest)

View a preview an Order Invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OmInvoiceApiGenerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    OmInvoiceApiGenerationApi apiInstance = new OmInvoiceApiGenerationApi(defaultClient);
    String marketplaceTechnicalCode = "marketplaceTechnicalCode_example"; // String | The Marketplace Technical Code
    String accountId = "accountId_example"; // String | The Account Identifier
    String beezUPOrderUUID = "beezUPOrderUUID_example"; // String | The BeezUP Order UUID
    List<String> acceptEncoding = Arrays.asList(); // List<String> | Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size
    PreviewOrderInvoiceRequest previewOrderInvoiceRequest = new PreviewOrderInvoiceRequest(); // PreviewOrderInvoiceRequest | 
    try {
      PreviewOrderInvoiceResponse result = apiInstance.getOrderInvoicePreview(marketplaceTechnicalCode, accountId, beezUPOrderUUID, acceptEncoding, previewOrderInvoiceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OmInvoiceApiGenerationApi#getOrderInvoicePreview");
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
| **marketplaceTechnicalCode** | **String**| The Marketplace Technical Code | |
| **accountId** | **String**| The Account Identifier | |
| **beezUPOrderUUID** | **String**| The BeezUP Order UUID | |
| **acceptEncoding** | [**List&lt;String&gt;**](String.md)| Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size | |
| **previewOrderInvoiceRequest** | [**PreviewOrderInvoiceRequest**](PreviewOrderInvoiceRequest.md)|  | |

### Return type

[**PreviewOrderInvoiceResponse**](PreviewOrderInvoiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Order Invoice preview successfully returned. |  -  |
| **403** | OwnerId not authorized The required order invoice settings have not been set BeezUPOrderStatus forbidden  |  -  |
| **404** | The order cannot be retrieved  |  -  |
| **409** | The InvoiceNumber is already used There is already an invoice for this order  |  -  |
| **0** | Occurs when something goes wrong |  -  |

