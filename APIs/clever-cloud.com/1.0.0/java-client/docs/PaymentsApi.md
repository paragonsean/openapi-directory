# PaymentsApi

All URIs are relative to *https://api.clever-cloud.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteOrganisationsIdPaymentsBillingsBid_1**](PaymentsApi.md#deleteOrganisationsIdPaymentsBillingsBid_1) | **DELETE** /organisations/{id}/payments/billings/{bid} |  |
| [**deleteOrganisationsIdPaymentsRecurring_1**](PaymentsApi.md#deleteOrganisationsIdPaymentsRecurring_1) | **DELETE** /organisations/{id}/payments/recurring |  |
| [**deleteSelfPaymentsBillingsBid_0**](PaymentsApi.md#deleteSelfPaymentsBillingsBid_0) | **DELETE** /self/payments/billings/{bid} |  |
| [**deleteSelfPaymentsMethodsMId_0**](PaymentsApi.md#deleteSelfPaymentsMethodsMId_0) | **DELETE** /self/payments/methods/{mId} |  |
| [**deleteSelfPaymentsRecurring_0**](PaymentsApi.md#deleteSelfPaymentsRecurring_0) | **DELETE** /self/payments/recurring |  |
| [**getOrganisationsIdPaymentsBillingsBidPdf_1**](PaymentsApi.md#getOrganisationsIdPaymentsBillingsBidPdf_1) | **GET** /organisations/{id}/payments/billings/{bid}.pdf |  |
| [**getOrganisationsIdPaymentsBillingsBid_1**](PaymentsApi.md#getOrganisationsIdPaymentsBillingsBid_1) | **GET** /organisations/{id}/payments/billings/{bid} |  |
| [**getOrganisationsIdPaymentsBillings_1**](PaymentsApi.md#getOrganisationsIdPaymentsBillings_1) | **GET** /organisations/{id}/payments/billings |  |
| [**getOrganisationsIdPaymentsFullPricePrice_1**](PaymentsApi.md#getOrganisationsIdPaymentsFullPricePrice_1) | **GET** /organisations/{id}/payments/fullprice/{price} |  |
| [**getPaymentsCouponsName_0**](PaymentsApi.md#getPaymentsCouponsName_0) | **GET** /payments/coupons/{name} |  |
| [**getPaymentsProviders_0**](PaymentsApi.md#getPaymentsProviders_0) | **GET** /payments/providers |  |
| [**getPaymentsTokensStripe_0**](PaymentsApi.md#getPaymentsTokensStripe_0) | **GET** /payments/tokens/stripe |  |
| [**getSelfPaymentsBillingsBidPdf_0**](PaymentsApi.md#getSelfPaymentsBillingsBidPdf_0) | **GET** /self/payments/billings/{bid}.pdf |  |
| [**getSelfPaymentsBillingsBid_0**](PaymentsApi.md#getSelfPaymentsBillingsBid_0) | **GET** /self/payments/billings/{bid} |  |
| [**getSelfPaymentsBillings_0**](PaymentsApi.md#getSelfPaymentsBillings_0) | **GET** /self/payments/billings |  |
| [**getSelfPaymentsFullpricePrice_0**](PaymentsApi.md#getSelfPaymentsFullpricePrice_0) | **GET** /self/payments/fullprice/{price} |  |
| [**getSelfPaymentsMethods_0**](PaymentsApi.md#getSelfPaymentsMethods_0) | **GET** /self/payments/methods |  |
| [**organisationsIdPaymentsBillingsUnpaidGet_1**](PaymentsApi.md#organisationsIdPaymentsBillingsUnpaidGet_1) | **GET** /organisations/{id}/payments/billings/unpaid |  |
| [**organisationsIdPaymentsMethodsDefaultGet_1**](PaymentsApi.md#organisationsIdPaymentsMethodsDefaultGet_1) | **GET** /organisations/{id}/payments/methods/default |  |
| [**organisationsIdPaymentsMethodsDefaultPut_1**](PaymentsApi.md#organisationsIdPaymentsMethodsDefaultPut_1) | **PUT** /organisations/{id}/payments/methods/default |  |
| [**organisationsIdPaymentsMethodsGet_1**](PaymentsApi.md#organisationsIdPaymentsMethodsGet_1) | **GET** /organisations/{id}/payments/methods |  |
| [**organisationsIdPaymentsMethodsMIdDelete_1**](PaymentsApi.md#organisationsIdPaymentsMethodsMIdDelete_1) | **DELETE** /organisations/{id}/payments/methods/{mId} |  |
| [**organisationsIdPaymentsMethodsPost_1**](PaymentsApi.md#organisationsIdPaymentsMethodsPost_1) | **POST** /organisations/{id}/payments/methods |  |
| [**organisationsIdPaymentsMonthlyinvoiceGet_1**](PaymentsApi.md#organisationsIdPaymentsMonthlyinvoiceGet_1) | **GET** /organisations/{id}/payments/monthlyinvoice |  |
| [**organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_1**](PaymentsApi.md#organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_1) | **PUT** /organisations/{id}/payments/monthlyinvoice/maxcredit |  |
| [**organisationsIdPaymentsRecurringGet_1**](PaymentsApi.md#organisationsIdPaymentsRecurringGet_1) | **GET** /organisations/{id}/payments/recurring |  |
| [**paymentsAssetsPayButtonTokenButtonPngGet_0**](PaymentsApi.md#paymentsAssetsPayButtonTokenButtonPngGet_0) | **GET** /payments/assets/pay_button/{token}/button.png |  |
| [**paymentsBidEndStripePost_0**](PaymentsApi.md#paymentsBidEndStripePost_0) | **POST** /payments/{bid}/end/stripe |  |
| [**postOrganisationsIdPaymentsBillings_1**](PaymentsApi.md#postOrganisationsIdPaymentsBillings_1) | **POST** /organisations/{id}/payments/billings |  |
| [**postSelfPaymentsBillings_0**](PaymentsApi.md#postSelfPaymentsBillings_0) | **POST** /self/payments/billings |  |
| [**postSelfPaymentsMethods_0**](PaymentsApi.md#postSelfPaymentsMethods_0) | **POST** /self/payments/methods |  |
| [**putOrganisationsIdPaymentsBillingsBid_1**](PaymentsApi.md#putOrganisationsIdPaymentsBillingsBid_1) | **PUT** /organisations/{id}/payments/billings/{bid} |  |
| [**putSelfPaymentsBillingsBid_0**](PaymentsApi.md#putSelfPaymentsBillingsBid_0) | **PUT** /self/payments/billings/{bid} |  |
| [**selfPaymentsMethodsDefaultGet_0**](PaymentsApi.md#selfPaymentsMethodsDefaultGet_0) | **GET** /self/payments/methods/default |  |
| [**selfPaymentsMethodsDefaultPut_0**](PaymentsApi.md#selfPaymentsMethodsDefaultPut_0) | **PUT** /self/payments/methods/default |  |
| [**selfPaymentsMonthlyinvoiceGet_0**](PaymentsApi.md#selfPaymentsMonthlyinvoiceGet_0) | **GET** /self/payments/monthlyinvoice |  |
| [**selfPaymentsMonthlyinvoiceMaxcreditPut_0**](PaymentsApi.md#selfPaymentsMonthlyinvoiceMaxcreditPut_0) | **PUT** /self/payments/monthlyinvoice/maxcredit |  |
| [**selfPaymentsRecurringGet_0**](PaymentsApi.md#selfPaymentsRecurringGet_0) | **GET** /self/payments/recurring |  |
| [**selfPaymentsTokensStripeGet_0**](PaymentsApi.md#selfPaymentsTokensStripeGet_0) | **GET** /self/payments/tokens/stripe |  |


<a id="deleteOrganisationsIdPaymentsBillingsBid_1"></a>
# **deleteOrganisationsIdPaymentsBillingsBid_1**
> deleteOrganisationsIdPaymentsBillingsBid_1(id, bid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String id = "id_example"; // String | 
    String bid = "bid_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdPaymentsBillingsBid_1(id, bid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#deleteOrganisationsIdPaymentsBillingsBid_1");
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
| **id** | **String**|  | |
| **bid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deletePurchaseOrder |  -  |

<a id="deleteOrganisationsIdPaymentsRecurring_1"></a>
# **deleteOrganisationsIdPaymentsRecurring_1**
> deleteOrganisationsIdPaymentsRecurring_1(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteOrganisationsIdPaymentsRecurring_1(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#deleteOrganisationsIdPaymentsRecurring_1");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteRecurrentPayment |  -  |

<a id="deleteSelfPaymentsBillingsBid_0"></a>
# **deleteSelfPaymentsBillingsBid_0**
> deleteSelfPaymentsBillingsBid_0(bid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String bid = "bid_example"; // String | 
    try {
      apiInstance.deleteSelfPaymentsBillingsBid_0(bid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#deleteSelfPaymentsBillingsBid_0");
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
| **bid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deletePurchaseOrder |  -  |

<a id="deleteSelfPaymentsMethodsMId_0"></a>
# **deleteSelfPaymentsMethodsMId_0**
> deleteSelfPaymentsMethodsMId_0(mId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String mId = "mId_example"; // String | 
    try {
      apiInstance.deleteSelfPaymentsMethodsMId_0(mId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#deleteSelfPaymentsMethodsMId_0");
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
| **mId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteUserCard |  -  |

<a id="deleteSelfPaymentsRecurring_0"></a>
# **deleteSelfPaymentsRecurring_0**
> deleteSelfPaymentsRecurring_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    try {
      apiInstance.deleteSelfPaymentsRecurring_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#deleteSelfPaymentsRecurring_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deleteRecurrentPayment |  -  |

<a id="getOrganisationsIdPaymentsBillingsBidPdf_1"></a>
# **getOrganisationsIdPaymentsBillingsBidPdf_1**
> getOrganisationsIdPaymentsBillingsBidPdf_1(id, bid, token)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String id = "id_example"; // String | 
    String bid = "bid_example"; // String | 
    String token = "token_example"; // String | 
    try {
      apiInstance.getOrganisationsIdPaymentsBillingsBidPdf_1(id, bid, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#getOrganisationsIdPaymentsBillingsBidPdf_1");
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
| **id** | **String**|  | |
| **bid** | **String**|  | |
| **token** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getPdfInvoice |  -  |

<a id="getOrganisationsIdPaymentsBillingsBid_1"></a>
# **getOrganisationsIdPaymentsBillingsBid_1**
> getOrganisationsIdPaymentsBillingsBid_1(id, bid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String id = "id_example"; // String | 
    String bid = "bid_example"; // String | 
    try {
      apiInstance.getOrganisationsIdPaymentsBillingsBid_1(id, bid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#getOrganisationsIdPaymentsBillingsBid_1");
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
| **id** | **String**|  | |
| **bid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getInvoice |  -  |

<a id="getOrganisationsIdPaymentsBillings_1"></a>
# **getOrganisationsIdPaymentsBillings_1**
> getOrganisationsIdPaymentsBillings_1(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.getOrganisationsIdPaymentsBillings_1(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#getOrganisationsIdPaymentsBillings_1");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getInvoices |  -  |

<a id="getOrganisationsIdPaymentsFullPricePrice_1"></a>
# **getOrganisationsIdPaymentsFullPricePrice_1**
> getOrganisationsIdPaymentsFullPricePrice_1(id, price)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String id = "id_example"; // String | 
    String price = "price_example"; // String | 
    try {
      apiInstance.getOrganisationsIdPaymentsFullPricePrice_1(id, price);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#getOrganisationsIdPaymentsFullPricePrice_1");
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
| **id** | **String**|  | |
| **price** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | priceWithTax |  -  |

<a id="getPaymentsCouponsName_0"></a>
# **getPaymentsCouponsName_0**
> getPaymentsCouponsName_0(name)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String name = "name_example"; // String | 
    try {
      apiInstance.getPaymentsCouponsName_0(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#getPaymentsCouponsName_0");
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
| **name** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getCoupon |  -  |

<a id="getPaymentsProviders_0"></a>
# **getPaymentsProviders_0**
> List&lt;PaymentProvider&gt; getPaymentsProviders_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    try {
      List<PaymentProvider> result = apiInstance.getPaymentsProviders_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#getPaymentsProviders_0");
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

[**List&lt;PaymentProvider&gt;**](PaymentProvider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAvailablePaymentProviders |  -  |

<a id="getPaymentsTokensStripe_0"></a>
# **getPaymentsTokensStripe_0**
> getPaymentsTokensStripe_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    try {
      apiInstance.getPaymentsTokensStripe_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#getPaymentsTokensStripe_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getStripeToken |  -  |

<a id="getSelfPaymentsBillingsBidPdf_0"></a>
# **getSelfPaymentsBillingsBidPdf_0**
> getSelfPaymentsBillingsBidPdf_0(bid, token)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String bid = "bid_example"; // String | 
    String token = "token_example"; // String | 
    try {
      apiInstance.getSelfPaymentsBillingsBidPdf_0(bid, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#getSelfPaymentsBillingsBidPdf_0");
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
| **bid** | **String**|  | |
| **token** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getPdfInvoice |  -  |

<a id="getSelfPaymentsBillingsBid_0"></a>
# **getSelfPaymentsBillingsBid_0**
> getSelfPaymentsBillingsBid_0(bid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String bid = "bid_example"; // String | 
    try {
      apiInstance.getSelfPaymentsBillingsBid_0(bid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#getSelfPaymentsBillingsBid_0");
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
| **bid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getInvoice |  -  |

<a id="getSelfPaymentsBillings_0"></a>
# **getSelfPaymentsBillings_0**
> getSelfPaymentsBillings_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    try {
      apiInstance.getSelfPaymentsBillings_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#getSelfPaymentsBillings_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getInvoices |  -  |

<a id="getSelfPaymentsFullpricePrice_0"></a>
# **getSelfPaymentsFullpricePrice_0**
> getSelfPaymentsFullpricePrice_0(price)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String price = "price_example"; // String | 
    try {
      apiInstance.getSelfPaymentsFullpricePrice_0(price);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#getSelfPaymentsFullpricePrice_0");
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
| **price** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | priceWithTax |  -  |

<a id="getSelfPaymentsMethods_0"></a>
# **getSelfPaymentsMethods_0**
> getSelfPaymentsMethods_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    try {
      apiInstance.getSelfPaymentsMethods_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#getSelfPaymentsMethods_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getUserPaymentMethods |  -  |

<a id="organisationsIdPaymentsBillingsUnpaidGet_1"></a>
# **organisationsIdPaymentsBillingsUnpaidGet_1**
> organisationsIdPaymentsBillingsUnpaidGet_1(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsBillingsUnpaidGet_1(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#organisationsIdPaymentsBillingsUnpaidGet_1");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdPaymentsMethodsDefaultGet_1"></a>
# **organisationsIdPaymentsMethodsDefaultGet_1**
> organisationsIdPaymentsMethodsDefaultGet_1(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsMethodsDefaultGet_1(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#organisationsIdPaymentsMethodsDefaultGet_1");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdPaymentsMethodsDefaultPut_1"></a>
# **organisationsIdPaymentsMethodsDefaultPut_1**
> organisationsIdPaymentsMethodsDefaultPut_1(id, paymentData)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String id = "id_example"; // String | 
    PaymentData paymentData = new PaymentData(); // PaymentData | 
    try {
      apiInstance.organisationsIdPaymentsMethodsDefaultPut_1(id, paymentData);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#organisationsIdPaymentsMethodsDefaultPut_1");
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
| **id** | **String**|  | |
| **paymentData** | [**PaymentData**](PaymentData.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdPaymentsMethodsGet_1"></a>
# **organisationsIdPaymentsMethodsGet_1**
> organisationsIdPaymentsMethodsGet_1(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsMethodsGet_1(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#organisationsIdPaymentsMethodsGet_1");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdPaymentsMethodsMIdDelete_1"></a>
# **organisationsIdPaymentsMethodsMIdDelete_1**
> organisationsIdPaymentsMethodsMIdDelete_1(mId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String mId = "mId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsMethodsMIdDelete_1(mId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#organisationsIdPaymentsMethodsMIdDelete_1");
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
| **mId** | **String**|  | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdPaymentsMethodsPost_1"></a>
# **organisationsIdPaymentsMethodsPost_1**
> organisationsIdPaymentsMethodsPost_1(id, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String id = "id_example"; // String | 
    Body body = new Body(); // Body | 
    try {
      apiInstance.organisationsIdPaymentsMethodsPost_1(id, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#organisationsIdPaymentsMethodsPost_1");
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
| **id** | **String**|  | |
| **body** | [**Body**](Body.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdPaymentsMonthlyinvoiceGet_1"></a>
# **organisationsIdPaymentsMonthlyinvoiceGet_1**
> organisationsIdPaymentsMonthlyinvoiceGet_1(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsMonthlyinvoiceGet_1(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#organisationsIdPaymentsMonthlyinvoiceGet_1");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_1"></a>
# **organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_1**
> organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_1(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_1(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#organisationsIdPaymentsMonthlyinvoiceMaxcreditPut_1");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="organisationsIdPaymentsRecurringGet_1"></a>
# **organisationsIdPaymentsRecurringGet_1**
> organisationsIdPaymentsRecurringGet_1(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.organisationsIdPaymentsRecurringGet_1(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#organisationsIdPaymentsRecurringGet_1");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="paymentsAssetsPayButtonTokenButtonPngGet_0"></a>
# **paymentsAssetsPayButtonTokenButtonPngGet_0**
> paymentsAssetsPayButtonTokenButtonPngGet_0(token)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String token = "token_example"; // String | 
    try {
      apiInstance.paymentsAssetsPayButtonTokenButtonPngGet_0(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#paymentsAssetsPayButtonTokenButtonPngGet_0");
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
| **token** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="paymentsBidEndStripePost_0"></a>
# **paymentsBidEndStripePost_0**
> paymentsBidEndStripePost_0(bid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String bid = "bid_example"; // String | 
    try {
      apiInstance.paymentsBidEndStripePost_0(bid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#paymentsBidEndStripePost_0");
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
| **bid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | endPaymentWithStripe |  -  |

<a id="postOrganisationsIdPaymentsBillings_1"></a>
# **postOrganisationsIdPaymentsBillings_1**
> postOrganisationsIdPaymentsBillings_1(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.postOrganisationsIdPaymentsBillings_1(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#postOrganisationsIdPaymentsBillings_1");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | buyDrops |  -  |

<a id="postSelfPaymentsBillings_0"></a>
# **postSelfPaymentsBillings_0**
> postSelfPaymentsBillings_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    try {
      apiInstance.postSelfPaymentsBillings_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#postSelfPaymentsBillings_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | buyDrops |  -  |

<a id="postSelfPaymentsMethods_0"></a>
# **postSelfPaymentsMethods_0**
> postSelfPaymentsMethods_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    try {
      apiInstance.postSelfPaymentsMethods_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#postSelfPaymentsMethods_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | addUserMethod |  -  |

<a id="putOrganisationsIdPaymentsBillingsBid_1"></a>
# **putOrganisationsIdPaymentsBillingsBid_1**
> putOrganisationsIdPaymentsBillingsBid_1(id, bid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String id = "id_example"; // String | 
    String bid = "bid_example"; // String | 
    try {
      apiInstance.putOrganisationsIdPaymentsBillingsBid_1(id, bid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#putOrganisationsIdPaymentsBillingsBid_1");
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
| **id** | **String**|  | |
| **bid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | choosePaymentProvider |  -  |

<a id="putSelfPaymentsBillingsBid_0"></a>
# **putSelfPaymentsBillingsBid_0**
> putSelfPaymentsBillingsBid_0(bid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    String bid = "bid_example"; // String | 
    try {
      apiInstance.putSelfPaymentsBillingsBid_0(bid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#putSelfPaymentsBillingsBid_0");
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
| **bid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | choosePaymentProvider |  -  |

<a id="selfPaymentsMethodsDefaultGet_0"></a>
# **selfPaymentsMethodsDefaultGet_0**
> selfPaymentsMethodsDefaultGet_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    try {
      apiInstance.selfPaymentsMethodsDefaultGet_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#selfPaymentsMethodsDefaultGet_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="selfPaymentsMethodsDefaultPut_0"></a>
# **selfPaymentsMethodsDefaultPut_0**
> selfPaymentsMethodsDefaultPut_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    try {
      apiInstance.selfPaymentsMethodsDefaultPut_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#selfPaymentsMethodsDefaultPut_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="selfPaymentsMonthlyinvoiceGet_0"></a>
# **selfPaymentsMonthlyinvoiceGet_0**
> selfPaymentsMonthlyinvoiceGet_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    try {
      apiInstance.selfPaymentsMonthlyinvoiceGet_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#selfPaymentsMonthlyinvoiceGet_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="selfPaymentsMonthlyinvoiceMaxcreditPut_0"></a>
# **selfPaymentsMonthlyinvoiceMaxcreditPut_0**
> selfPaymentsMonthlyinvoiceMaxcreditPut_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    try {
      apiInstance.selfPaymentsMonthlyinvoiceMaxcreditPut_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#selfPaymentsMonthlyinvoiceMaxcreditPut_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="selfPaymentsRecurringGet_0"></a>
# **selfPaymentsRecurringGet_0**
> selfPaymentsRecurringGet_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    try {
      apiInstance.selfPaymentsRecurringGet_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#selfPaymentsRecurringGet_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="selfPaymentsTokensStripeGet_0"></a>
# **selfPaymentsTokensStripeGet_0**
> selfPaymentsTokensStripeGet_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PaymentsApi apiInstance = new PaymentsApi(defaultClient);
    try {
      apiInstance.selfPaymentsTokensStripeGet_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsApi#selfPaymentsTokensStripeGet_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

