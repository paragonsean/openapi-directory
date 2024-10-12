# ShoppingCartApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addCoupons**](ShoppingCartApi.md#addCoupons) | **POST** /api/checkout/pub/orderForm/{orderFormId}/coupons | Add coupons to the cart |
| [**cartSimulation**](ShoppingCartApi.md#cartSimulation) | **POST** /api/checkout/pub/orderForms/simulation | Cart simulation |
| [**createANewCart**](ShoppingCartApi.md#createANewCart) | **GET** /api/checkout/pub/orderForm | Get current or create a new cart |
| [**getCartInformationById**](ShoppingCartApi.md#getCartInformationById) | **GET** /api/checkout/pub/orderForm/{orderFormId} | Get cart information by ID |
| [**getCartInstallments**](ShoppingCartApi.md#getCartInstallments) | **GET** /api/checkout/pub/orderForm/{orderFormId}/installments | Cart installments |
| [**ignoreProfileData**](ShoppingCartApi.md#ignoreProfileData) | **PATCH** /api/checkout/pub/orderForm/{orderFormId}/profile | Ignore profile data |
| [**items**](ShoppingCartApi.md#items) | **POST** /api/checkout/pub/orderForm/{orderFormId}/items | Add cart items |
| [**itemsUpdate**](ShoppingCartApi.md#itemsUpdate) | **POST** /api/checkout/pub/orderForm/{orderFormId}/items/update | Update cart items |
| [**priceChange**](ShoppingCartApi.md#priceChange) | **PUT** /api/checkout/pub/orderForm/{orderFormId}/items/{itemIndex}/price | Change price |
| [**removeAllItems**](ShoppingCartApi.md#removeAllItems) | **POST** /api/checkout/pub/orderForm/{orderFormId}/items/removeAll | Remove all items |
| [**removeallpersonaldata**](ShoppingCartApi.md#removeallpersonaldata) | **GET** /checkout/changeToAnonymousUser/{orderFormId} | Remove all personal data |


<a id="addCoupons"></a>
# **addCoupons**
> AddCoupons200Response addCoupons(orderFormId, contentType, accept, addCouponsRequest)

Add coupons to the cart

Use this request to add coupons to a given shopping cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShoppingCartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    ShoppingCartApi apiInstance = new ShoppingCartApi(defaultClient);
    String orderFormId = "ede846222cd44046ba6c638442c3505a"; // String | ID of the orderForm that will receive coupon information.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    AddCouponsRequest addCouponsRequest = new AddCouponsRequest(); // AddCouponsRequest | 
    try {
      AddCoupons200Response result = apiInstance.addCoupons(orderFormId, contentType, accept, addCouponsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShoppingCartApi#addCoupons");
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
| **orderFormId** | **String**| ID of the orderForm that will receive coupon information. | [default to ede846222cd44046ba6c638442c3505a] |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **addCouponsRequest** | [**AddCouponsRequest**](AddCouponsRequest.md)|  | |

### Return type

[**AddCoupons200Response**](AddCoupons200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="cartSimulation"></a>
# **cartSimulation**
> CartSimulation200Response cartSimulation(contentType, accept, rnbBehavior, sc, cartSimulationRequest)

Cart simulation

This endpoint is used to simulate a cart in VTEX Checkout.    It receives an **SKU ID**, the **quantity** of items in the cart and the ID of the **Seller**.    It sends back all information about the cart, such as the selling price of each item, rates and benefits data, payment and logistics info.    This is useful whenever you need to know the availability of fulfilling an order for a specific cart setting, since the API response will let you know the updated price, inventory and shipping data.    **Important**: The fields (&#x60;sku id&#x60;, &#x60;quantity&#x60;, &#x60;seller&#x60;, &#x60;country&#x60;, &#x60;postalCode&#x60; and &#x60;geoCoordinates&#x60;) are just examples of content that you can simulate in your cart. You can add more fields to the request as per your need. Access the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) guide to check the available fields.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShoppingCartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    ShoppingCartApi apiInstance = new ShoppingCartApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer rnbBehavior = 0; // Integer | This parameter defines which promotions apply to the simulation. Use `0` for simulations at cart stage, which means all promotions apply. In case of window simulation use `1`, which indicates promotions that apply nominal discounts over the total purchase value shouldn't be considered on the simulation.    Note that if this not sent, the parameter is `1`.
    Integer sc = 1; // Integer | Trade Policy (Sales Channel) identification.
    CartSimulationRequest cartSimulationRequest = new CartSimulationRequest(); // CartSimulationRequest | 
    try {
      CartSimulation200Response result = apiInstance.cartSimulation(contentType, accept, rnbBehavior, sc, cartSimulationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShoppingCartApi#cartSimulation");
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
| **rnbBehavior** | **Integer**| This parameter defines which promotions apply to the simulation. Use &#x60;0&#x60; for simulations at cart stage, which means all promotions apply. In case of window simulation use &#x60;1&#x60;, which indicates promotions that apply nominal discounts over the total purchase value shouldn&#39;t be considered on the simulation.    Note that if this not sent, the parameter is &#x60;1&#x60;. | [optional] [default to 0] |
| **sc** | **Integer**| Trade Policy (Sales Channel) identification. | [optional] |
| **cartSimulationRequest** | [**CartSimulationRequest**](CartSimulationRequest.md)|  | [optional] |

### Return type

[**CartSimulation200Response**](CartSimulation200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="createANewCart"></a>
# **createANewCart**
> createANewCart(contentType, accept, forceNewCart)

Get current or create a new cart

You can use this request to get your current shopping cart information (&#x60;orderFormId&#x60;) or to create a new cart.    **Important**: To create a new empty shopping cart you need to send this request with the query param &#x60;forceNewCart&#x3D;true&#x60;.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; obtained in response is the identification code of the newly created cart.    &gt; This request has a time out of 45 seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShoppingCartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    ShoppingCartApi apiInstance = new ShoppingCartApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Boolean forceNewCart = true; // Boolean | Use this query parameter to create a new empty shopping cart.
    try {
      apiInstance.createANewCart(contentType, accept, forceNewCart);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShoppingCartApi#createANewCart");
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
| **forceNewCart** | **Boolean**| Use this query parameter to create a new empty shopping cart. | [optional] [default to true] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getCartInformationById"></a>
# **getCartInformationById**
> getCartInformationById(orderFormId, contentType, accept, refreshOutdatedData)

Get cart information by ID

Use this request to get all information associated to a given shopping  cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShoppingCartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    ShoppingCartApi apiInstance = new ShoppingCartApi(defaultClient);
    String orderFormId = "ede846222cd44046ba6c638442c3505a"; // String | ID of the orderForm corresponding to the cart whose information you want to retrieve.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Boolean refreshOutdatedData = true; // Boolean | It is possible to use the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/cart-update#itemsupdate) so as to allow outdated information in the `orderForm`, which may improve performance in some cases. To guarantee that all cart information is updated, send this request with this parameter as `true`. We recommend doing this in the final stages of the shopping experience, starting from the checkout page.
    try {
      apiInstance.getCartInformationById(orderFormId, contentType, accept, refreshOutdatedData);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShoppingCartApi#getCartInformationById");
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
| **orderFormId** | **String**| ID of the orderForm corresponding to the cart whose information you want to retrieve. | [default to ede846222cd44046ba6c638442c3505a] |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **refreshOutdatedData** | **Boolean**| It is possible to use the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/cart-update#itemsupdate) so as to allow outdated information in the &#x60;orderForm&#x60;, which may improve performance in some cases. To guarantee that all cart information is updated, send this request with this parameter as &#x60;true&#x60;. We recommend doing this in the final stages of the shopping experience, starting from the checkout page. | [optional] [default to true] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getCartInstallments"></a>
# **getCartInstallments**
> getCartInstallments(orderFormId, paymentSystem, contentType, accept)

Cart installments

Retrieves possible amount of installments and respective values for a given cart with a given payment method.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    This endpoint can be used to get the installment options for only one payment method at a time.    This endpoint should be called only after the selected &#x60;orderForm&#x60; already has a &#x60;paymentData&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShoppingCartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    ShoppingCartApi apiInstance = new ShoppingCartApi(defaultClient);
    String orderFormId = "orderFormId_example"; // String | ID of the `orderForm` to be consulted for installments.
    Integer paymentSystem = 56; // Integer | ID of the payment method to be consulted for installments.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      apiInstance.getCartInstallments(orderFormId, paymentSystem, contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShoppingCartApi#getCartInstallments");
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
| **orderFormId** | **String**| ID of the &#x60;orderForm&#x60; to be consulted for installments. | |
| **paymentSystem** | **Integer**| ID of the payment method to be consulted for installments. | |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="ignoreProfileData"></a>
# **ignoreProfileData**
> ignoreProfileData(orderFormId, contentType, accept, ignoreProfileDataRequest)

Ignore profile data

When a shopper provides an email address at Checkout, the platform tries to retrieve existing profile information for that email and add it to the shopping cart information. Use this request if you want to change this behavior for a given cart, meaning profile information will not be included in the order automattically.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    Note that this request will only work if you have not sent the &#x60;clientProfileData&#x60; to the cart yet. Sending it to a cart that already has a &#x60;clientProfileData&#x60; should return a status &#x60;403 Forbidden&#x60; error, with an &#x60;Access denied&#x60; message.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShoppingCartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    ShoppingCartApi apiInstance = new ShoppingCartApi(defaultClient);
    String orderFormId = "ede846222cd44046ba6c638442c3505a"; // String | ID of the orderForm corresponding to the cart whose items will have the price changed.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    IgnoreProfileDataRequest ignoreProfileDataRequest = new IgnoreProfileDataRequest(); // IgnoreProfileDataRequest | 
    try {
      apiInstance.ignoreProfileData(orderFormId, contentType, accept, ignoreProfileDataRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShoppingCartApi#ignoreProfileData");
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
| **orderFormId** | **String**| ID of the orderForm corresponding to the cart whose items will have the price changed. | [default to ede846222cd44046ba6c638442c3505a] |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **ignoreProfileDataRequest** | [**IgnoreProfileDataRequest**](IgnoreProfileDataRequest.md)|  | |

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

<a id="items"></a>
# **items**
> Items200Response items(contentType, accept, orderFormId, itemsRequest, allowedOutdatedData)

Add cart items

Use this request to add a new item to the shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShoppingCartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    ShoppingCartApi apiInstance = new ShoppingCartApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String orderFormId = "ede846222cd44046ba6c638442c3505a"; // String | ID of the orderForm corresponding to the cart in which the new item will be added.
    ItemsRequest itemsRequest = new ItemsRequest(); // ItemsRequest | 
    List<Object> allowedOutdatedData = Arrays.asList(null); // List<Object> | In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is `”paymentData”`.
    try {
      Items200Response result = apiInstance.items(contentType, accept, orderFormId, itemsRequest, allowedOutdatedData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShoppingCartApi#items");
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
| **orderFormId** | **String**| ID of the orderForm corresponding to the cart in which the new item will be added. | [default to ede846222cd44046ba6c638442c3505a] |
| **itemsRequest** | [**ItemsRequest**](ItemsRequest.md)|  | |
| **allowedOutdatedData** | [**List&lt;Object&gt;**](Object.md)| In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is &#x60;”paymentData”&#x60;. | [optional] |

### Return type

[**Items200Response**](Items200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="itemsUpdate"></a>
# **itemsUpdate**
> ItemsUpdate200Response itemsUpdate(contentType, accept, orderFormId, itemsUpdateRequest, allowedOutdatedData)

Update cart items

You can use this request to:    1. Change the quantity of one or more items in a specific cart.  2. Remove an item from the cart (by sending the &#x60;quantity&#x60; value &#x3D; &#x60;0&#x60; in the request body).    **Important**: To remove all items from the cart at the same time, use the [Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems) endpoint.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure that represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShoppingCartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    ShoppingCartApi apiInstance = new ShoppingCartApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String orderFormId = "ede846222cd44046ba6c638442c3505a"; // String | ID of the `orderForm` corresponding to the cart whose items you want to update.
    ItemsUpdateRequest itemsUpdateRequest = new ItemsUpdateRequest(); // ItemsUpdateRequest | 
    List<Object> allowedOutdatedData = Arrays.asList(null); // List<Object> | In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is `”paymentData”`.
    try {
      ItemsUpdate200Response result = apiInstance.itemsUpdate(contentType, accept, orderFormId, itemsUpdateRequest, allowedOutdatedData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShoppingCartApi#itemsUpdate");
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
| **orderFormId** | **String**| ID of the &#x60;orderForm&#x60; corresponding to the cart whose items you want to update. | [default to ede846222cd44046ba6c638442c3505a] |
| **itemsUpdateRequest** | [**ItemsUpdateRequest**](ItemsUpdateRequest.md)|  | |
| **allowedOutdatedData** | [**List&lt;Object&gt;**](Object.md)| In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is &#x60;”paymentData”&#x60;. | [optional] |

### Return type

[**ItemsUpdate200Response**](ItemsUpdate200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="priceChange"></a>
# **priceChange**
> priceChange(orderFormId, itemIndex, contentType, accept, priceChangeRequest)

Change price

This request changes the price of an SKU in a cart. You can also perform type of bulk price change with the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/shopping-cart#itemsupdate)    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    You need to inform which cart you are referring to, by sending its &#x60;orderFormId&#x60;; and what is the item whose price you want to change, by sending its &#x60;itemIndex&#x60;.    You also need to pass the new price value in the body.    Remember that, to use this endpoint, the feature of *manual price* must be active. To check if it&#39;s active, use the [Get orderForm configuration](https://developers.vtex.com/reference#getorderformconfiguration) endpoint. To make it active, use the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) endpoint, making the &#x60;allowManualPrice&#x60; field &#x60;true&#x60;.    &gt; Whenever you use this request to change the price of an item, all items in that cart with the same SKU are affected by this change. This applies even to items that share the SKU but have been separated into different objects in the &#x60;items&#x60; array due to customizations or attachments, for example.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShoppingCartApi;

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

    ShoppingCartApi apiInstance = new ShoppingCartApi(defaultClient);
    String orderFormId = "ede846222cd44046ba6c638442c3505a"; // String | ID of the orderForm corresponding to the cart whose items will have the price changed.
    String itemIndex = "itemIndex_example"; // String | The index of the item in the cart. Each cart item is identified by an index, starting in 0.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    PriceChangeRequest priceChangeRequest = new PriceChangeRequest(); // PriceChangeRequest | 
    try {
      apiInstance.priceChange(orderFormId, itemIndex, contentType, accept, priceChangeRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShoppingCartApi#priceChange");
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
| **orderFormId** | **String**| ID of the orderForm corresponding to the cart whose items will have the price changed. | [default to ede846222cd44046ba6c638442c3505a] |
| **itemIndex** | **String**| The index of the item in the cart. Each cart item is identified by an index, starting in 0. | |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **priceChangeRequest** | [**PriceChangeRequest**](PriceChangeRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="removeAllItems"></a>
# **removeAllItems**
> Object removeAllItems(orderFormId, contentType, accept, body)

Remove all items

This request removes all items from a given cart, leaving it empty.    You must send an empty JSON in the body of the request.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    **Important**: **Request Body** must always be sent with empty value \&quot;{ }\&quot; in this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShoppingCartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    ShoppingCartApi apiInstance = new ShoppingCartApi(defaultClient);
    String orderFormId = "ede846222cd44046ba6c638442c3505a"; // String | ID of the orderForm corresponding to the cart whose items you want to remove.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Object body = null; // Object | 
    try {
      Object result = apiInstance.removeAllItems(orderFormId, contentType, accept, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShoppingCartApi#removeAllItems");
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
| **orderFormId** | **String**| ID of the orderForm corresponding to the cart whose items you want to remove. | [default to ede846222cd44046ba6c638442c3505a] |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **body** | **Object**|  | [optional] |

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
| **200** |  |  -  |

<a id="removeallpersonaldata"></a>
# **removeallpersonaldata**
> Object removeallpersonaldata(contentType, accept, orderFormId)

Remove all personal data

This call removes all user information, making a cart anonymous while leaving the items.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure that represents a shopping cart and contains all information about it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    This call works by creating a new orderForm, setting a new cookie, and returning a redirect 302 to the cart URL (&#x60;/checkout/#/orderform&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShoppingCartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    ShoppingCartApi apiInstance = new ShoppingCartApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String orderFormId = "ede846222cd44046ba6c638442c3505a"; // String | ID of the orderForm corresponding to the cart whose user's personal data you want to remove.
    try {
      Object result = apiInstance.removeallpersonaldata(contentType, accept, orderFormId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShoppingCartApi#removeallpersonaldata");
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
| **orderFormId** | **String**| ID of the orderForm corresponding to the cart whose user&#39;s personal data you want to remove. | [default to ede846222cd44046ba6c638442c3505a] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

