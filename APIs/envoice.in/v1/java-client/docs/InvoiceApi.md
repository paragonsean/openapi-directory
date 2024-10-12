# InvoiceApi

All URIs are relative to *https://www.envoice.in*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiInvoiceAllcategoriesGet**](InvoiceApi.md#apiInvoiceAllcategoriesGet) | **GET** /api/invoice/allcategories | Return all invoice categories for the account |
| [**apiInvoiceDeletecategoryPost**](InvoiceApi.md#apiInvoiceDeletecategoryPost) | **POST** /api/invoice/deletecategory | Delete an existing invoice category |
| [**apiInvoiceNewcategoryPost**](InvoiceApi.md#apiInvoiceNewcategoryPost) | **POST** /api/invoice/newcategory | Create an invoice category |
| [**apiInvoiceUpdatecategoryPost**](InvoiceApi.md#apiInvoiceUpdatecategoryPost) | **POST** /api/invoice/updatecategory | Update an existing invoice category |
| [**invoiceApiAll**](InvoiceApi.md#invoiceApiAll) | **GET** /api/invoice/all | Return all invoices for the account |
| [**invoiceApiChangeStatus**](InvoiceApi.md#invoiceApiChangeStatus) | **POST** /api/invoice/changestatus | Change invoice status |
| [**invoiceApiDelete**](InvoiceApi.md#invoiceApiDelete) | **POST** /api/invoice/delete | Delete an existing invoice |
| [**invoiceApiDetails**](InvoiceApi.md#invoiceApiDetails) | **GET** /api/invoice/details | Return invoice data |
| [**invoiceApiNew**](InvoiceApi.md#invoiceApiNew) | **POST** /api/invoice/new | Create an invoice |
| [**invoiceApiPdf**](InvoiceApi.md#invoiceApiPdf) | **GET** /api/invoice/pdf | Return the PDF for the invoice |
| [**invoiceApiSendToAccountant**](InvoiceApi.md#invoiceApiSendToAccountant) | **POST** /api/invoice/sendtoaccountant | Send the provided invoice to the accountant |
| [**invoiceApiSendToClient**](InvoiceApi.md#invoiceApiSendToClient) | **POST** /api/invoice/sendtoclient | Send the provided invoice to the client |
| [**invoiceApiStatus**](InvoiceApi.md#invoiceApiStatus) | **GET** /api/invoice/status | Retrieve the status of the invoice |
| [**invoiceApiUpdate**](InvoiceApi.md#invoiceApiUpdate) | **POST** /api/invoice/update | Update an existing invoice |
| [**invoiceApiUri**](InvoiceApi.md#invoiceApiUri) | **GET** /api/invoice/uri | Return the unique url to the client&#39;s invoice |


<a id="apiInvoiceAllcategoriesGet"></a>
# **apiInvoiceAllcategoriesGet**
> ListResultInvoiceCategoryApiModel apiInvoiceAllcategoriesGet(xAuthKey, xAuthSecret, query)

Return all invoice categories for the account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    String query = "query_example"; // String | 
    try {
      ListResultInvoiceCategoryApiModel result = apiInstance.apiInvoiceAllcategoriesGet(xAuthKey, xAuthSecret, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#apiInvoiceAllcategoriesGet");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **query** | **String**|  | [optional] |

### Return type

[**ListResultInvoiceCategoryApiModel**](ListResultInvoiceCategoryApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiInvoiceDeletecategoryPost"></a>
# **apiInvoiceDeletecategoryPost**
> Integer apiInvoiceDeletecategoryPost(xAuthKey, xAuthSecret, invoiceCategoryDeleteApiModel)

Delete an existing invoice category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    InvoiceCategoryDeleteApiModel invoiceCategoryDeleteApiModel = new InvoiceCategoryDeleteApiModel(); // InvoiceCategoryDeleteApiModel | 
    try {
      Integer result = apiInstance.apiInvoiceDeletecategoryPost(xAuthKey, xAuthSecret, invoiceCategoryDeleteApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#apiInvoiceDeletecategoryPost");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **invoiceCategoryDeleteApiModel** | [**InvoiceCategoryDeleteApiModel**](InvoiceCategoryDeleteApiModel.md)|  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiInvoiceNewcategoryPost"></a>
# **apiInvoiceNewcategoryPost**
> InvoiceCategoryApiModel apiInvoiceNewcategoryPost(xAuthKey, xAuthSecret, invoiceCategoryCreateApiModel)

Create an invoice category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    InvoiceCategoryCreateApiModel invoiceCategoryCreateApiModel = new InvoiceCategoryCreateApiModel(); // InvoiceCategoryCreateApiModel | 
    try {
      InvoiceCategoryApiModel result = apiInstance.apiInvoiceNewcategoryPost(xAuthKey, xAuthSecret, invoiceCategoryCreateApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#apiInvoiceNewcategoryPost");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **invoiceCategoryCreateApiModel** | [**InvoiceCategoryCreateApiModel**](InvoiceCategoryCreateApiModel.md)|  | |

### Return type

[**InvoiceCategoryApiModel**](InvoiceCategoryApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiInvoiceUpdatecategoryPost"></a>
# **apiInvoiceUpdatecategoryPost**
> InvoiceCategoryApiModel apiInvoiceUpdatecategoryPost(xAuthKey, xAuthSecret, invoiceCategoryUpdateApiModel)

Update an existing invoice category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    InvoiceCategoryUpdateApiModel invoiceCategoryUpdateApiModel = new InvoiceCategoryUpdateApiModel(); // InvoiceCategoryUpdateApiModel | 
    try {
      InvoiceCategoryApiModel result = apiInstance.apiInvoiceUpdatecategoryPost(xAuthKey, xAuthSecret, invoiceCategoryUpdateApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#apiInvoiceUpdatecategoryPost");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **invoiceCategoryUpdateApiModel** | [**InvoiceCategoryUpdateApiModel**](InvoiceCategoryUpdateApiModel.md)|  | |

### Return type

[**InvoiceCategoryApiModel**](InvoiceCategoryApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoiceApiAll"></a>
# **invoiceApiAll**
> ListResultInvoiceDetailsApiModel invoiceApiAll(xAuthKey, xAuthSecret, queryOptionsPage, queryOptionsPageSize)

Return all invoices for the account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    Integer queryOptionsPage = 56; // Integer | 
    Integer queryOptionsPageSize = 56; // Integer | 
    try {
      ListResultInvoiceDetailsApiModel result = apiInstance.invoiceApiAll(xAuthKey, xAuthSecret, queryOptionsPage, queryOptionsPageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#invoiceApiAll");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **queryOptionsPage** | **Integer**|  | [optional] |
| **queryOptionsPageSize** | **Integer**|  | [optional] |

### Return type

[**ListResultInvoiceDetailsApiModel**](ListResultInvoiceDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoiceApiChangeStatus"></a>
# **invoiceApiChangeStatus**
> Boolean invoiceApiChangeStatus(xAuthKey, xAuthSecret, changeStatusApiModel)

Change invoice status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    ChangeStatusApiModel changeStatusApiModel = new ChangeStatusApiModel(); // ChangeStatusApiModel | 
    try {
      Boolean result = apiInstance.invoiceApiChangeStatus(xAuthKey, xAuthSecret, changeStatusApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#invoiceApiChangeStatus");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **changeStatusApiModel** | [**ChangeStatusApiModel**](ChangeStatusApiModel.md)|  | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoiceApiDelete"></a>
# **invoiceApiDelete**
> Integer invoiceApiDelete(xAuthKey, xAuthSecret, invoiceDeleteApiModel)

Delete an existing invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    InvoiceDeleteApiModel invoiceDeleteApiModel = new InvoiceDeleteApiModel(); // InvoiceDeleteApiModel | 
    try {
      Integer result = apiInstance.invoiceApiDelete(xAuthKey, xAuthSecret, invoiceDeleteApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#invoiceApiDelete");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **invoiceDeleteApiModel** | [**InvoiceDeleteApiModel**](InvoiceDeleteApiModel.md)|  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoiceApiDetails"></a>
# **invoiceApiDetails**
> InvoiceFullDetailsApiModel invoiceApiDetails(id, xAuthKey, xAuthSecret)

Return invoice data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    Integer id = 56; // Integer | 
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    try {
      InvoiceFullDetailsApiModel result = apiInstance.invoiceApiDetails(id, xAuthKey, xAuthSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#invoiceApiDetails");
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
| **id** | **Integer**|  | |
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |

### Return type

[**InvoiceFullDetailsApiModel**](InvoiceFullDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoiceApiNew"></a>
# **invoiceApiNew**
> InvoiceFullDetailsApiModel invoiceApiNew(xAuthKey, xAuthSecret, invoiceCreateApiModel)

Create an invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    InvoiceCreateApiModel invoiceCreateApiModel = new InvoiceCreateApiModel(); // InvoiceCreateApiModel | 
    try {
      InvoiceFullDetailsApiModel result = apiInstance.invoiceApiNew(xAuthKey, xAuthSecret, invoiceCreateApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#invoiceApiNew");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **invoiceCreateApiModel** | [**InvoiceCreateApiModel**](InvoiceCreateApiModel.md)|  | |

### Return type

[**InvoiceFullDetailsApiModel**](InvoiceFullDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoiceApiPdf"></a>
# **invoiceApiPdf**
> InvoiceUriApiModel invoiceApiPdf(id, xAuthKey, xAuthSecret, signedVersion)

Return the PDF for the invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    Integer id = 56; // Integer | 
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    Boolean signedVersion = true; // Boolean | 
    try {
      InvoiceUriApiModel result = apiInstance.invoiceApiPdf(id, xAuthKey, xAuthSecret, signedVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#invoiceApiPdf");
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
| **id** | **Integer**|  | |
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **signedVersion** | **Boolean**|  | [optional] |

### Return type

[**InvoiceUriApiModel**](InvoiceUriApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoiceApiSendToAccountant"></a>
# **invoiceApiSendToAccountant**
> Integer invoiceApiSendToAccountant(xAuthKey, xAuthSecret, sendInvoiceToAccountantApiModel)

Send the provided invoice to the accountant

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    SendInvoiceToAccountantApiModel sendInvoiceToAccountantApiModel = new SendInvoiceToAccountantApiModel(); // SendInvoiceToAccountantApiModel | 
    try {
      Integer result = apiInstance.invoiceApiSendToAccountant(xAuthKey, xAuthSecret, sendInvoiceToAccountantApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#invoiceApiSendToAccountant");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **sendInvoiceToAccountantApiModel** | [**SendInvoiceToAccountantApiModel**](SendInvoiceToAccountantApiModel.md)|  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoiceApiSendToClient"></a>
# **invoiceApiSendToClient**
> Integer invoiceApiSendToClient(xAuthKey, xAuthSecret, sendInvoiceToClientApiModel)

Send the provided invoice to the client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    SendInvoiceToClientApiModel sendInvoiceToClientApiModel = new SendInvoiceToClientApiModel(); // SendInvoiceToClientApiModel | 
    try {
      Integer result = apiInstance.invoiceApiSendToClient(xAuthKey, xAuthSecret, sendInvoiceToClientApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#invoiceApiSendToClient");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **sendInvoiceToClientApiModel** | [**SendInvoiceToClientApiModel**](SendInvoiceToClientApiModel.md)|  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoiceApiStatus"></a>
# **invoiceApiStatus**
> String invoiceApiStatus(id, xAuthKey, xAuthSecret)

Retrieve the status of the invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    Integer id = 56; // Integer | 
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    try {
      String result = apiInstance.invoiceApiStatus(id, xAuthKey, xAuthSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#invoiceApiStatus");
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
| **id** | **Integer**|  | |
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoiceApiUpdate"></a>
# **invoiceApiUpdate**
> InvoiceFullDetailsApiModel invoiceApiUpdate(xAuthKey, xAuthSecret, invoiceUpdateApiModel)

Update an existing invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    InvoiceUpdateApiModel invoiceUpdateApiModel = new InvoiceUpdateApiModel(); // InvoiceUpdateApiModel | 
    try {
      InvoiceFullDetailsApiModel result = apiInstance.invoiceApiUpdate(xAuthKey, xAuthSecret, invoiceUpdateApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#invoiceApiUpdate");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **invoiceUpdateApiModel** | [**InvoiceUpdateApiModel**](InvoiceUpdateApiModel.md)|  | |

### Return type

[**InvoiceFullDetailsApiModel**](InvoiceFullDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoiceApiUri"></a>
# **invoiceApiUri**
> InvoiceUriApiModel invoiceApiUri(id, xAuthKey, xAuthSecret)

Return the unique url to the client&#39;s invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    InvoiceApi apiInstance = new InvoiceApi(defaultClient);
    Integer id = 56; // Integer | 
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    try {
      InvoiceUriApiModel result = apiInstance.invoiceApiUri(id, xAuthKey, xAuthSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceApi#invoiceApiUri");
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
| **id** | **Integer**|  | |
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |

### Return type

[**InvoiceUriApiModel**](InvoiceUriApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

