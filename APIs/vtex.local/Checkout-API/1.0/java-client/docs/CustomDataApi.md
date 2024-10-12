# CustomDataApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**removesinglecustomfieldvalue**](CustomDataApi.md#removesinglecustomfieldvalue) | **DELETE** /api/checkout/pub/orderForm/{orderFormId}/customData/{appId}/{appFieldName} | Remove single custom field value |
| [**setMultipleCustomFieldValues**](CustomDataApi.md#setMultipleCustomFieldValues) | **PUT** /api/checkout/pub/orderForm/{orderFormId}/customData/{appId} | Set multiple custom field values |
| [**setSingleCustomFieldValue**](CustomDataApi.md#setSingleCustomFieldValue) | **PUT** /api/checkout/pub/orderForm/{orderFormId}/customData/{appId}/{appFieldName} | Set single custom field value |


<a id="removesinglecustomfieldvalue"></a>
# **removesinglecustomfieldvalue**
> removesinglecustomfieldvalue(contentType, accept, orderFormId, appId, appFieldName)

Remove single custom field value

Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) request. The value of a specific custom field can be removed by this request.    To do that, you need to inform in the URL the ID of the app you created with the configuration API (&#x60;appId&#x60;).    You also need to iform the specific field created in this app (identified by the &#x60;appFieldName&#x60; parameter, also passed through the URL) whose value you want to remove.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    CustomDataApi apiInstance = new CustomDataApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String orderFormId = "orderFormId_example"; // String | The ID of the orderForm from which you want to remove the custom field value.
    String appId = "appId_example"; // String | ID of the app created through the Update orderForm Configuration endpoint.
    String appFieldName = "appFieldName_example"; // String | Name of the app's field created through the Update orderForm Configuration endpoint and which will be deleted.
    try {
      apiInstance.removesinglecustomfieldvalue(contentType, accept, orderFormId, appId, appFieldName);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomDataApi#removesinglecustomfieldvalue");
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
| **orderFormId** | **String**| The ID of the orderForm from which you want to remove the custom field value. | |
| **appId** | **String**| ID of the app created through the Update orderForm Configuration endpoint. | |
| **appFieldName** | **String**| Name of the app&#39;s field created through the Update orderForm Configuration endpoint and which will be deleted. | |

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

<a id="setMultipleCustomFieldValues"></a>
# **setMultipleCustomFieldValues**
> Object setMultipleCustomFieldValues(orderFormId, contentType, accept, appId, requestBody)

Set multiple custom field values

Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference/configuration#updateorderformconfiguration) request. The values of these custom fields can then be updated by this request.    To do that, you need to inform the ID of the app you created with the configuration API (&#x60;appId&#x60;).    In the body of the request, for each field created in this app (&#x60;appFieldName&#x60;) you will inform a value (&#x60;appFieldValue&#x60;).    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    CustomDataApi apiInstance = new CustomDataApi(defaultClient);
    String orderFormId = "orderFormId_example"; // String | ID of the orderForm that will receive the new custom field values.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String appId = "appId_example"; // String | ID of the app created with the configuration API.
    Map<String, Object> requestBody = null; // Map<String, Object> | 
    try {
      Object result = apiInstance.setMultipleCustomFieldValues(orderFormId, contentType, accept, appId, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomDataApi#setMultipleCustomFieldValues");
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
| **orderFormId** | **String**| ID of the orderForm that will receive the new custom field values. | |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **appId** | **String**| ID of the app created with the configuration API. | |
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)|  | |

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

<a id="setSingleCustomFieldValue"></a>
# **setSingleCustomFieldValue**
> setSingleCustomFieldValue(orderFormId, appId, appFieldName, contentType, accept, setsinglecustomfieldvalueRequest)

Set single custom field value

Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) request. The value of a specific custom field can then be updated by this request.    To do that, you need to inform in the URL the ID of the app you created with the configuration API (&#x60;appId&#x60;).    In the body of the request, you will inform the new value (&#x60;appFieldValue&#x60;, passed through the body) of the specific field created in this app (identified by the &#x60;appFieldName&#x60; parameter, passed through the URL).    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    CustomDataApi apiInstance = new CustomDataApi(defaultClient);
    String orderFormId = "orderFormId_example"; // String | The ID of the orderForm whose custom field's value you want to change.
    String appId = "appId_example"; // String | ID of the app created through the Update orderForm Configuration endpoint.
    String appFieldName = "appFieldName_example"; // String | Name of the app's field created through the Update orderForm Configuration endpoint.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    SetsinglecustomfieldvalueRequest setsinglecustomfieldvalueRequest = new SetsinglecustomfieldvalueRequest(); // SetsinglecustomfieldvalueRequest | 
    try {
      apiInstance.setSingleCustomFieldValue(orderFormId, appId, appFieldName, contentType, accept, setsinglecustomfieldvalueRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomDataApi#setSingleCustomFieldValue");
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
| **orderFormId** | **String**| The ID of the orderForm whose custom field&#39;s value you want to change. | |
| **appId** | **String**| ID of the app created through the Update orderForm Configuration endpoint. | |
| **appFieldName** | **String**| Name of the app&#39;s field created through the Update orderForm Configuration endpoint. | |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **setsinglecustomfieldvalueRequest** | [**SetsinglecustomfieldvalueRequest**](SetsinglecustomfieldvalueRequest.md)|  | |

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

