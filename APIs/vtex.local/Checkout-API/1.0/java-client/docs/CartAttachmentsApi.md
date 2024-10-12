# CartAttachmentsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addClientPreferences**](CartAttachmentsApi.md#addClientPreferences) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/clientPreferencesData | Add client preferences |
| [**addClientProfile**](CartAttachmentsApi.md#addClientProfile) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/clientProfileData | Add client profile |
| [**addMarketingData**](CartAttachmentsApi.md#addMarketingData) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/marketingData | Add marketing data |
| [**addMerchantContextData**](CartAttachmentsApi.md#addMerchantContextData) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/merchantContextData | Add merchant context data |
| [**addPaymentData**](CartAttachmentsApi.md#addPaymentData) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/paymentData | Add payment data |
| [**addShippingAddress**](CartAttachmentsApi.md#addShippingAddress) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/shippingData | Add shipping address and select delivery option |
| [**getClientProfileByEmail**](CartAttachmentsApi.md#getClientProfileByEmail) | **GET** /api/checkout/pub/profiles | Get client profile by email |


<a id="addClientPreferences"></a>
# **addClientPreferences**
> Object addClientPreferences(contentType, accept, orderFormId, addClientPreferencesRequest)

Add client preferences

Use this request to include client preferences information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    CartAttachmentsApi apiInstance = new CartAttachmentsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String orderFormId = "orderFormId_example"; // String | ID of the orderForm that will receive client profile information.
    AddClientPreferencesRequest addClientPreferencesRequest = new AddClientPreferencesRequest(); // AddClientPreferencesRequest | 
    try {
      Object result = apiInstance.addClientPreferences(contentType, accept, orderFormId, addClientPreferencesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartAttachmentsApi#addClientPreferences");
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
| **orderFormId** | **String**| ID of the orderForm that will receive client profile information. | |
| **addClientPreferencesRequest** | [**AddClientPreferencesRequest**](AddClientPreferencesRequest.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="addClientProfile"></a>
# **addClientProfile**
> addClientProfile(contentType, accept, orderFormId, addClientProfileRequest)

Add client profile

Use this request to include client profile information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are modifying information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    CartAttachmentsApi apiInstance = new CartAttachmentsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String orderFormId = "orderFormId_example"; // String | ID of the orderForm that will receive client profile information.
    AddClientProfileRequest addClientProfileRequest = new AddClientProfileRequest(); // AddClientProfileRequest | 
    try {
      apiInstance.addClientProfile(contentType, accept, orderFormId, addClientProfileRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartAttachmentsApi#addClientProfile");
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
| **orderFormId** | **String**| ID of the orderForm that will receive client profile information. | |
| **addClientProfileRequest** | [**AddClientProfileRequest**](AddClientProfileRequest.md)|  | |

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
| **200** | OK |  -  |

<a id="addMarketingData"></a>
# **addMarketingData**
> addMarketingData(contentType, accept, orderFormId, addMarketingDataRequest)

Add marketing data

Use this request to include marketing information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    CartAttachmentsApi apiInstance = new CartAttachmentsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String orderFormId = "orderFormId_example"; // String | ID of the orderForm that will receive client profile information.
    AddMarketingDataRequest addMarketingDataRequest = new AddMarketingDataRequest(); // AddMarketingDataRequest | 
    try {
      apiInstance.addMarketingData(contentType, accept, orderFormId, addMarketingDataRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartAttachmentsApi#addMarketingData");
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
| **orderFormId** | **String**| ID of the orderForm that will receive client profile information. | |
| **addMarketingDataRequest** | [**AddMarketingDataRequest**](AddMarketingDataRequest.md)|  | |

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
| **200** | OK |  -  |

<a id="addMerchantContextData"></a>
# **addMerchantContextData**
> AddMerchantContextData200Response addMerchantContextData(contentType, accept, orderFormId, addMerchantContextDataRequest)

Add merchant context data

This endpoint is used for the merchant to add to the cart any relevant information that is related to the context of a specific order.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    CartAttachmentsApi apiInstance = new CartAttachmentsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String orderFormId = "29154e27383145cc8ce1f7a1df0d99c4"; // String | ID of the orderForm that will receive the relevant information added by the merchant.
    AddMerchantContextDataRequest addMerchantContextDataRequest = new AddMerchantContextDataRequest(); // AddMerchantContextDataRequest | 
    try {
      AddMerchantContextData200Response result = apiInstance.addMerchantContextData(contentType, accept, orderFormId, addMerchantContextDataRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartAttachmentsApi#addMerchantContextData");
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
| **orderFormId** | **String**| ID of the orderForm that will receive the relevant information added by the merchant. | |
| **addMerchantContextDataRequest** | [**AddMerchantContextDataRequest**](AddMerchantContextDataRequest.md)|  | |

### Return type

[**AddMerchantContextData200Response**](AddMerchantContextData200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="addPaymentData"></a>
# **addPaymentData**
> addPaymentData(contentType, accept, orderFormId, addPaymentDataRequest)

Add payment data

Use this request to include payment information to a given shopping cart. The payment information attachment in the shopping cart does not determine the final order payment method in itself. However, it allows tha platform to update any relevant information that may be impacted by the payment method.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    CartAttachmentsApi apiInstance = new CartAttachmentsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String orderFormId = "orderFormId_example"; // String | ID of the orderForm that will receive client profile information.
    AddPaymentDataRequest addPaymentDataRequest = new AddPaymentDataRequest(); // AddPaymentDataRequest | 
    try {
      apiInstance.addPaymentData(contentType, accept, orderFormId, addPaymentDataRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartAttachmentsApi#addPaymentData");
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
| **orderFormId** | **String**| ID of the orderForm that will receive client profile information. | |
| **addPaymentDataRequest** | [**AddPaymentDataRequest**](AddPaymentDataRequest.md)|  | |

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
| **200** |  |  -  |

<a id="addShippingAddress"></a>
# **addShippingAddress**
> addShippingAddress(contentType, accept, orderFormId, addShippingAddressRequest)

Add shipping address and select delivery option

Use this request to include shipping information and/or selected delivery option to a given shopping cart.    To add shipping addresses send the &#x60;selectedAddresses&#x60; array. For delivery option use the &#x60;logisticsInfo&#x60; array.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are modifying information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    CartAttachmentsApi apiInstance = new CartAttachmentsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String orderFormId = "orderFormId_example"; // String | ID of the orderForm that will receive client profile information.
    AddShippingAddressRequest addShippingAddressRequest = new AddShippingAddressRequest(); // AddShippingAddressRequest | 
    try {
      apiInstance.addShippingAddress(contentType, accept, orderFormId, addShippingAddressRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartAttachmentsApi#addShippingAddress");
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
| **orderFormId** | **String**| ID of the orderForm that will receive client profile information. | |
| **addShippingAddressRequest** | [**AddShippingAddressRequest**](AddShippingAddressRequest.md)|  | |

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
| **200** |  |  -  |

<a id="getClientProfileByEmail"></a>
# **getClientProfileByEmail**
> GetClientProfileByEmail200Response getClientProfileByEmail(contentType, accept, email)

Get client profile by email

Retrieve a client&#39;s profile information by providing an email address.    If the response body fields are empty, the following situations may have occurred:    1. There is no client registered with the email address provided in your store, or;  2. Client profile is invalid or incomplete. For more information, see [SmartCheckout - Customer information automatic fill-in](https://help.vtex.com/en/tutorial/smartcheckout-customer-information-automatic-fill-in--2Nuu3xAFzdhIzJIldAdtan).    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are consulting information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    CartAttachmentsApi apiInstance = new CartAttachmentsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String email = "clark.kent@examplemail.com"; // String | Client's email address to be searched.
    try {
      GetClientProfileByEmail200Response result = apiInstance.getClientProfileByEmail(contentType, accept, email);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartAttachmentsApi#getClientProfileByEmail");
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
| **email** | **String**| Client&#39;s email address to be searched. | [default to clark.kent@examplemail.com] |

### Return type

[**GetClientProfileByEmail200Response**](GetClientProfileByEmail200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

