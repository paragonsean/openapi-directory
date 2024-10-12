# OrderinvoicesApi

All URIs are relative to *https://shoppingcontent.googleapis.com/content/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contentOrderinvoicesCreatechargeinvoice**](OrderinvoicesApi.md#contentOrderinvoicesCreatechargeinvoice) | **POST** /{merchantId}/orderinvoices/{orderId}/createChargeInvoice |  |
| [**contentOrderinvoicesCreaterefundinvoice**](OrderinvoicesApi.md#contentOrderinvoicesCreaterefundinvoice) | **POST** /{merchantId}/orderinvoices/{orderId}/createRefundInvoice |  |


<a id="contentOrderinvoicesCreatechargeinvoice"></a>
# **contentOrderinvoicesCreatechargeinvoice**
> OrderinvoicesCreateChargeInvoiceResponse contentOrderinvoicesCreatechargeinvoice(merchantId, orderId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, orderinvoicesCreateChargeInvoiceRequest)



Creates a charge invoice for a shipment group, and triggers a charge capture for orderinvoice enabled orders.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderinvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://shoppingcontent.googleapis.com/content/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrderinvoicesApi apiInstance = new OrderinvoicesApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The ID of the account that manages the order. This cannot be a multi-client account.
    String orderId = "orderId_example"; // String | The ID of the order.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    OrderinvoicesCreateChargeInvoiceRequest orderinvoicesCreateChargeInvoiceRequest = new OrderinvoicesCreateChargeInvoiceRequest(); // OrderinvoicesCreateChargeInvoiceRequest | 
    try {
      OrderinvoicesCreateChargeInvoiceResponse result = apiInstance.contentOrderinvoicesCreatechargeinvoice(merchantId, orderId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, orderinvoicesCreateChargeInvoiceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderinvoicesApi#contentOrderinvoicesCreatechargeinvoice");
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
| **merchantId** | **String**| The ID of the account that manages the order. This cannot be a multi-client account. | |
| **orderId** | **String**| The ID of the order. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **orderinvoicesCreateChargeInvoiceRequest** | [**OrderinvoicesCreateChargeInvoiceRequest**](OrderinvoicesCreateChargeInvoiceRequest.md)|  | [optional] |

### Return type

[**OrderinvoicesCreateChargeInvoiceResponse**](OrderinvoicesCreateChargeInvoiceResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="contentOrderinvoicesCreaterefundinvoice"></a>
# **contentOrderinvoicesCreaterefundinvoice**
> OrderinvoicesCreateRefundInvoiceResponse contentOrderinvoicesCreaterefundinvoice(merchantId, orderId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, orderinvoicesCreateRefundInvoiceRequest)



Creates a refund invoice for one or more shipment groups, and triggers a refund for orderinvoice enabled orders. This can only be used for line items that have previously been charged using &#x60;createChargeInvoice&#x60;. All amounts (except for the summary) are incremental with respect to the previous invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderinvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://shoppingcontent.googleapis.com/content/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrderinvoicesApi apiInstance = new OrderinvoicesApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The ID of the account that manages the order. This cannot be a multi-client account.
    String orderId = "orderId_example"; // String | The ID of the order.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    OrderinvoicesCreateRefundInvoiceRequest orderinvoicesCreateRefundInvoiceRequest = new OrderinvoicesCreateRefundInvoiceRequest(); // OrderinvoicesCreateRefundInvoiceRequest | 
    try {
      OrderinvoicesCreateRefundInvoiceResponse result = apiInstance.contentOrderinvoicesCreaterefundinvoice(merchantId, orderId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, orderinvoicesCreateRefundInvoiceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderinvoicesApi#contentOrderinvoicesCreaterefundinvoice");
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
| **merchantId** | **String**| The ID of the account that manages the order. This cannot be a multi-client account. | |
| **orderId** | **String**| The ID of the order. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **orderinvoicesCreateRefundInvoiceRequest** | [**OrderinvoicesCreateRefundInvoiceRequest**](OrderinvoicesCreateRefundInvoiceRequest.md)|  | [optional] |

### Return type

[**OrderinvoicesCreateRefundInvoiceResponse**](OrderinvoicesCreateRefundInvoiceResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

