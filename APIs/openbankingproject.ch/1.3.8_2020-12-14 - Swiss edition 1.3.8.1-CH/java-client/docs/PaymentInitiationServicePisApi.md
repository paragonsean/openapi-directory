# PaymentInitiationServicePisApi

All URIs are relative to *https://api.dev.openbankingproject.ch*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelPayment**](PaymentInitiationServicePisApi.md#cancelPayment) | **DELETE** /v1/{payment-service}/{payment-product}/{paymentId} | Payment cancellation request |
| [**getPaymentCancellationScaStatus**](PaymentInitiationServicePisApi.md#getPaymentCancellationScaStatus) | **GET** /v1/{payment-service}/{payment-product}/{paymentId}/cancellation-authorisations/{authorisationId} | Read the SCA status of the payment cancellation&#39;s authorisation |
| [**getPaymentInformation**](PaymentInitiationServicePisApi.md#getPaymentInformation) | **GET** /v1/{payment-service}/{payment-product}/{paymentId} | Get payment information |
| [**getPaymentInitiationAuthorisation**](PaymentInitiationServicePisApi.md#getPaymentInitiationAuthorisation) | **GET** /v1/{payment-service}/{payment-product}/{paymentId}/authorisations | Get payment initiation authorisation sub-resources request |
| [**getPaymentInitiationCancellationAuthorisationInformation**](PaymentInitiationServicePisApi.md#getPaymentInitiationCancellationAuthorisationInformation) | **GET** /v1/{payment-service}/{payment-product}/{paymentId}/cancellation-authorisations | Will deliver an array of resource identifications to all generated cancellation authorisation sub-resources |
| [**getPaymentInitiationScaStatus**](PaymentInitiationServicePisApi.md#getPaymentInitiationScaStatus) | **GET** /v1/{payment-service}/{payment-product}/{paymentId}/authorisations/{authorisationId} | Read the SCA status of the payment authorisation |
| [**getPaymentInitiationStatus**](PaymentInitiationServicePisApi.md#getPaymentInitiationStatus) | **GET** /v1/{payment-service}/{payment-product}/{paymentId}/status | Payment initiation status request |
| [**initiatePayment**](PaymentInitiationServicePisApi.md#initiatePayment) | **POST** /v1/{payment-service}/{payment-product} | Payment initiation request |
| [**startPaymentAuthorisation**](PaymentInitiationServicePisApi.md#startPaymentAuthorisation) | **POST** /v1/{payment-service}/{payment-product}/{paymentId}/authorisations | Start the authorisation process for a payment initiation |
| [**startPaymentInitiationCancellationAuthorisation**](PaymentInitiationServicePisApi.md#startPaymentInitiationCancellationAuthorisation) | **POST** /v1/{payment-service}/{payment-product}/{paymentId}/cancellation-authorisations | Start the authorisation process for the cancellation of the addressed payment |
| [**updatePaymentCancellationPsuData**](PaymentInitiationServicePisApi.md#updatePaymentCancellationPsuData) | **PUT** /v1/{payment-service}/{payment-product}/{paymentId}/cancellation-authorisations/{authorisationId} | Update PSU data for payment initiation cancellation |
| [**updatePaymentPsuData**](PaymentInitiationServicePisApi.md#updatePaymentPsuData) | **PUT** /v1/{payment-service}/{payment-product}/{paymentId}/authorisations/{authorisationId} | Update PSU data for payment initiation |


<a id="cancelPayment"></a>
# **cancelPayment**
> PaymentInitiationCancelResponse202 cancelPayment(paymentService, paymentProduct, paymentId, xRequestID, digest, signature, tpPSignatureCertificate, tpPRedirectPreferred, tpPNokRedirectURI, tpPRedirectURI, tpPExplicitAuthorisationPreferred, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation)

Payment cancellation request

This method initiates the cancellation of a payment.  Depending on the payment-service, the payment-product and the ASPSP&#39;s implementation,  this TPP call might be sufficient to cancel a payment.  If an authorisation of the payment cancellation is mandated by the ASPSP,  a corresponding hyperlink will be contained in the response message.  Cancels the addressed payment with resource identification paymentId if applicable to the payment-service, payment-product and received in product related timelines (e.g. before end of business day for scheduled payments of the last business day before the scheduled execution day).   The response to this DELETE command will tell the TPP whether the   * access method was rejected,   * access method was successful, or   * access method is generally applicable, but further authorisation processes are needed. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentInitiationServicePisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dev.openbankingproject.ch");
    
    // Configure HTTP bearer authorization: BearerAuthOAuth
    HttpBearerAuth BearerAuthOAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuthOAuth");
    BearerAuthOAuth.setBearerToken("BEARER TOKEN");

    PaymentInitiationServicePisApi apiInstance = new PaymentInitiationServicePisApi(defaultClient);
    String paymentService = "payments"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    String paymentProduct = "domestic-swiss-credit-transfers-isr"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    String paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
    String xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
    String digest = "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A="; // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
    String signature = "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" "; // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    byte[] tpPSignatureCertificate = null; // byte[] | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    Boolean tpPRedirectPreferred = true; // Boolean | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU. 
    URI tpPNokRedirectURI = new URI(); // URI | If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP. 
    URI tpPRedirectURI = new URI(); // URI | URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \"true\". It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification. 
    Boolean tpPExplicitAuthorisationPreferred = true; // Boolean | If it equals \"true\", the TPP prefers to start the authorisation process separately, e.g. because of the usage of a signing basket. This preference might be ignored by the ASPSP, if a signing basket is not supported as functionality.  If it equals \"false\" or if the parameter is not used, there is no preference of the TPP. This especially indicates that the TPP assumes a direct authorisation of the transaction in the next step, without using a signing basket. 
    String psUIPAddress = "192.168.8.78"; // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
    String psUIPPort = "1234"; // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    String psUAccept = "psUAccept_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptCharset = "psUAcceptCharset_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptEncoding = "psUAcceptEncoding_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptLanguage = "psUAcceptLanguage_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUUserAgent = "psUUserAgent_example"; // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    String psUHttpMethod = "GET"; // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    String psUDeviceID = "99435c7e-ad88-49ec-a2ad-99ddcb1f5555"; // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    String psUGeoLocation = "GEO:52.506931;13.144558"; // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    try {
      PaymentInitiationCancelResponse202 result = apiInstance.cancelPayment(paymentService, paymentProduct, paymentId, xRequestID, digest, signature, tpPSignatureCertificate, tpPRedirectPreferred, tpPNokRedirectURI, tpPRedirectURI, tpPExplicitAuthorisationPreferred, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentInitiationServicePisApi#cancelPayment");
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
| **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | [enum: payments, bulk-payments, periodic-payments] |
| **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | [enum: domestic-swiss-credit-transfers-isr, domestic-swiss-credit-transfers, domestic-swiss-credit-transfers-qr, domestic-swiss-foreign-credit-transfers, swiss-sepa-credit-transfers, swiss-cross-border-credit-transfers, pain.001-sepa-credit-transfers, pain.001-cross-border-credit-transfers, pain.001-swiss-six-credit-transfers] |
| **paymentId** | **String**| Resource identification of the generated payment initiation resource. | |
| **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | |
| **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] |
| **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] |
| **tpPSignatureCertificate** | **byte[]**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] |
| **tpPRedirectPreferred** | **Boolean**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] |
| **tpPNokRedirectURI** | **URI**| If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP.  | [optional] |
| **tpPRedirectURI** | **URI**| URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \&quot;true\&quot;. It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification.  | [optional] |
| **tpPExplicitAuthorisationPreferred** | **Boolean**| If it equals \&quot;true\&quot;, the TPP prefers to start the authorisation process separately, e.g. because of the usage of a signing basket. This preference might be ignored by the ASPSP, if a signing basket is not supported as functionality.  If it equals \&quot;false\&quot; or if the parameter is not used, there is no preference of the TPP. This especially indicates that the TPP assumes a direct authorisation of the transaction in the next step, without using a signing basket.  | [optional] |
| **psUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] |
| **psUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] |
| **psUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] |
| **psUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] [enum: GET, POST, PUT, PATCH, DELETE] |
| **psUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] |
| **psUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] |

### Return type

[**PaymentInitiationCancelResponse202**](PaymentInitiationCancelResponse202.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Received |  * X-Request-ID -  <br>  |
| **204** | No Content |  * X-Request-ID -  <br>  |
| **400** | Bad Request |  * Location -  <br>  * X-Request-ID -  <br>  |
| **401** | Unauthorized |  * Location -  <br>  * X-Request-ID -  <br>  |
| **403** | Forbidden |  * Location -  <br>  * X-Request-ID -  <br>  |
| **404** | Not found |  * Location -  <br>  * X-Request-ID -  <br>  |
| **405** | Method Not Allowed |  * Location -  <br>  * X-Request-ID -  <br>  |
| **406** | Not Acceptable |  * Location -  <br>  * X-Request-ID -  <br>  |
| **408** | Request Timeout |  * Location -  <br>  * X-Request-ID -  <br>  |
| **409** | Conflict |  * Location -  <br>  * X-Request-ID -  <br>  |
| **415** | Unsupported Media Type |  * Location -  <br>  * X-Request-ID -  <br>  |
| **429** | Too Many Requests |  * Location -  <br>  * X-Request-ID -  <br>  |
| **500** | Internal Server Error |  * Location -  <br>  * X-Request-ID -  <br>  |
| **503** | Service Unavailable |  * Location -  <br>  * X-Request-ID -  <br>  |

<a id="getPaymentCancellationScaStatus"></a>
# **getPaymentCancellationScaStatus**
> ScaStatusResponse getPaymentCancellationScaStatus(paymentService, paymentProduct, paymentId, authorisationId, xRequestID, digest, signature, tpPSignatureCertificate, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation)

Read the SCA status of the payment cancellation&#39;s authorisation

This method returns the SCA status of a payment initiation&#39;s authorisation sub-resource. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentInitiationServicePisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dev.openbankingproject.ch");
    
    // Configure HTTP bearer authorization: BearerAuthOAuth
    HttpBearerAuth BearerAuthOAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuthOAuth");
    BearerAuthOAuth.setBearerToken("BEARER TOKEN");

    PaymentInitiationServicePisApi apiInstance = new PaymentInitiationServicePisApi(defaultClient);
    String paymentService = "payments"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    String paymentProduct = "domestic-swiss-credit-transfers-isr"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    String paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
    String authorisationId = "authorisationId_example"; // String | Resource identification of the related SCA.
    String xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
    String digest = "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A="; // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
    String signature = "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" "; // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    byte[] tpPSignatureCertificate = null; // byte[] | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    String psUIPAddress = "192.168.8.78"; // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
    String psUIPPort = "1234"; // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    String psUAccept = "psUAccept_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptCharset = "psUAcceptCharset_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptEncoding = "psUAcceptEncoding_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptLanguage = "psUAcceptLanguage_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUUserAgent = "psUUserAgent_example"; // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    String psUHttpMethod = "GET"; // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    String psUDeviceID = "99435c7e-ad88-49ec-a2ad-99ddcb1f5555"; // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    String psUGeoLocation = "GEO:52.506931;13.144558"; // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    try {
      ScaStatusResponse result = apiInstance.getPaymentCancellationScaStatus(paymentService, paymentProduct, paymentId, authorisationId, xRequestID, digest, signature, tpPSignatureCertificate, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentInitiationServicePisApi#getPaymentCancellationScaStatus");
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
| **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | [enum: payments, bulk-payments, periodic-payments] |
| **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | [enum: domestic-swiss-credit-transfers-isr, domestic-swiss-credit-transfers, domestic-swiss-credit-transfers-qr, domestic-swiss-foreign-credit-transfers, swiss-sepa-credit-transfers, swiss-cross-border-credit-transfers, pain.001-sepa-credit-transfers, pain.001-cross-border-credit-transfers, pain.001-swiss-six-credit-transfers] |
| **paymentId** | **String**| Resource identification of the generated payment initiation resource. | |
| **authorisationId** | **String**| Resource identification of the related SCA. | |
| **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | |
| **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] |
| **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] |
| **tpPSignatureCertificate** | **byte[]**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] |
| **psUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] |
| **psUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] |
| **psUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] |
| **psUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] [enum: GET, POST, PUT, PATCH, DELETE] |
| **psUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] |
| **psUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] |

### Return type

[**ScaStatusResponse**](ScaStatusResponse.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Request-ID -  <br>  |
| **400** | Bad Request |  * Location -  <br>  * X-Request-ID -  <br>  |
| **401** | Unauthorized |  * Location -  <br>  * X-Request-ID -  <br>  |
| **403** | Forbidden |  * Location -  <br>  * X-Request-ID -  <br>  |
| **404** | Not found |  * Location -  <br>  * X-Request-ID -  <br>  |
| **405** | Method Not Allowed |  * Location -  <br>  * X-Request-ID -  <br>  |
| **406** | Not Acceptable |  * Location -  <br>  * X-Request-ID -  <br>  |
| **408** | Request Timeout |  * Location -  <br>  * X-Request-ID -  <br>  |
| **409** | Conflict |  * Location -  <br>  * X-Request-ID -  <br>  |
| **415** | Unsupported Media Type |  * Location -  <br>  * X-Request-ID -  <br>  |
| **429** | Too Many Requests |  * Location -  <br>  * X-Request-ID -  <br>  |
| **500** | Internal Server Error |  * Location -  <br>  * X-Request-ID -  <br>  |
| **503** | Service Unavailable |  * Location -  <br>  * X-Request-ID -  <br>  |

<a id="getPaymentInformation"></a>
# **getPaymentInformation**
> GetPaymentInformation200Response getPaymentInformation(paymentService, paymentProduct, paymentId, xRequestID, digest, signature, tpPSignatureCertificate, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation)

Get payment information

Returns the content of a payment object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentInitiationServicePisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dev.openbankingproject.ch");
    
    // Configure HTTP bearer authorization: BearerAuthOAuth
    HttpBearerAuth BearerAuthOAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuthOAuth");
    BearerAuthOAuth.setBearerToken("BEARER TOKEN");

    PaymentInitiationServicePisApi apiInstance = new PaymentInitiationServicePisApi(defaultClient);
    String paymentService = "payments"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    String paymentProduct = "domestic-swiss-credit-transfers-isr"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    String paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
    String xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
    String digest = "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A="; // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
    String signature = "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" "; // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    byte[] tpPSignatureCertificate = null; // byte[] | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    String psUIPAddress = "192.168.8.78"; // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
    String psUIPPort = "1234"; // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    String psUAccept = "psUAccept_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptCharset = "psUAcceptCharset_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptEncoding = "psUAcceptEncoding_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptLanguage = "psUAcceptLanguage_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUUserAgent = "psUUserAgent_example"; // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    String psUHttpMethod = "GET"; // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    String psUDeviceID = "99435c7e-ad88-49ec-a2ad-99ddcb1f5555"; // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    String psUGeoLocation = "GEO:52.506931;13.144558"; // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    try {
      GetPaymentInformation200Response result = apiInstance.getPaymentInformation(paymentService, paymentProduct, paymentId, xRequestID, digest, signature, tpPSignatureCertificate, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentInitiationServicePisApi#getPaymentInformation");
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
| **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | [enum: payments, bulk-payments, periodic-payments] |
| **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | [enum: domestic-swiss-credit-transfers-isr, domestic-swiss-credit-transfers, domestic-swiss-credit-transfers-qr, domestic-swiss-foreign-credit-transfers, swiss-sepa-credit-transfers, swiss-cross-border-credit-transfers, pain.001-sepa-credit-transfers, pain.001-cross-border-credit-transfers, pain.001-swiss-six-credit-transfers] |
| **paymentId** | **String**| Resource identification of the generated payment initiation resource. | |
| **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | |
| **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] |
| **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] |
| **tpPSignatureCertificate** | **byte[]**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] |
| **psUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] |
| **psUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] |
| **psUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] |
| **psUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] [enum: GET, POST, PUT, PATCH, DELETE] |
| **psUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] |
| **psUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] |

### Return type

[**GetPaymentInformation200Response**](GetPaymentInformation200Response.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Request-ID -  <br>  |
| **400** | Bad Request |  * Location -  <br>  * X-Request-ID -  <br>  |
| **401** | Unauthorized |  * Location -  <br>  * X-Request-ID -  <br>  |
| **403** | Forbidden |  * Location -  <br>  * X-Request-ID -  <br>  |
| **404** | Not found |  * Location -  <br>  * X-Request-ID -  <br>  |
| **405** | Method Not Allowed |  * Location -  <br>  * X-Request-ID -  <br>  |
| **406** | Not Acceptable |  * Location -  <br>  * X-Request-ID -  <br>  |
| **408** | Request Timeout |  * Location -  <br>  * X-Request-ID -  <br>  |
| **409** | Conflict |  * Location -  <br>  * X-Request-ID -  <br>  |
| **415** | Unsupported Media Type |  * Location -  <br>  * X-Request-ID -  <br>  |
| **429** | Too Many Requests |  * Location -  <br>  * X-Request-ID -  <br>  |
| **500** | Internal Server Error |  * Location -  <br>  * X-Request-ID -  <br>  |
| **503** | Service Unavailable |  * Location -  <br>  * X-Request-ID -  <br>  |

<a id="getPaymentInitiationAuthorisation"></a>
# **getPaymentInitiationAuthorisation**
> Authorisations getPaymentInitiationAuthorisation(paymentService, paymentProduct, paymentId, xRequestID, digest, signature, tpPSignatureCertificate, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation)

Get payment initiation authorisation sub-resources request

Read a list of all authorisation subresources IDs which have been created.  This function returns an array of hyperlinks to all generated authorisation sub-resources. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentInitiationServicePisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dev.openbankingproject.ch");
    
    // Configure HTTP bearer authorization: BearerAuthOAuth
    HttpBearerAuth BearerAuthOAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuthOAuth");
    BearerAuthOAuth.setBearerToken("BEARER TOKEN");

    PaymentInitiationServicePisApi apiInstance = new PaymentInitiationServicePisApi(defaultClient);
    String paymentService = "payments"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    String paymentProduct = "domestic-swiss-credit-transfers-isr"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    String paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
    String xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
    String digest = "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A="; // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
    String signature = "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" "; // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    byte[] tpPSignatureCertificate = null; // byte[] | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    String psUIPAddress = "192.168.8.78"; // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
    String psUIPPort = "1234"; // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    String psUAccept = "psUAccept_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptCharset = "psUAcceptCharset_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptEncoding = "psUAcceptEncoding_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptLanguage = "psUAcceptLanguage_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUUserAgent = "psUUserAgent_example"; // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    String psUHttpMethod = "GET"; // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    String psUDeviceID = "99435c7e-ad88-49ec-a2ad-99ddcb1f5555"; // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    String psUGeoLocation = "GEO:52.506931;13.144558"; // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    try {
      Authorisations result = apiInstance.getPaymentInitiationAuthorisation(paymentService, paymentProduct, paymentId, xRequestID, digest, signature, tpPSignatureCertificate, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentInitiationServicePisApi#getPaymentInitiationAuthorisation");
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
| **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | [enum: payments, bulk-payments, periodic-payments] |
| **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | [enum: domestic-swiss-credit-transfers-isr, domestic-swiss-credit-transfers, domestic-swiss-credit-transfers-qr, domestic-swiss-foreign-credit-transfers, swiss-sepa-credit-transfers, swiss-cross-border-credit-transfers, pain.001-sepa-credit-transfers, pain.001-cross-border-credit-transfers, pain.001-swiss-six-credit-transfers] |
| **paymentId** | **String**| Resource identification of the generated payment initiation resource. | |
| **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | |
| **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] |
| **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] |
| **tpPSignatureCertificate** | **byte[]**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] |
| **psUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] |
| **psUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] |
| **psUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] |
| **psUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] [enum: GET, POST, PUT, PATCH, DELETE] |
| **psUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] |
| **psUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] |

### Return type

[**Authorisations**](Authorisations.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Request-ID -  <br>  |
| **400** | Bad Request |  * Location -  <br>  * X-Request-ID -  <br>  |
| **401** | Unauthorized |  * Location -  <br>  * X-Request-ID -  <br>  |
| **403** | Forbidden |  * Location -  <br>  * X-Request-ID -  <br>  |
| **404** | Not found |  * Location -  <br>  * X-Request-ID -  <br>  |
| **405** | Method Not Allowed |  * Location -  <br>  * X-Request-ID -  <br>  |
| **406** | Not Acceptable |  * Location -  <br>  * X-Request-ID -  <br>  |
| **408** | Request Timeout |  * Location -  <br>  * X-Request-ID -  <br>  |
| **409** | Conflict |  * Location -  <br>  * X-Request-ID -  <br>  |
| **415** | Unsupported Media Type |  * Location -  <br>  * X-Request-ID -  <br>  |
| **429** | Too Many Requests |  * Location -  <br>  * X-Request-ID -  <br>  |
| **500** | Internal Server Error |  * Location -  <br>  * X-Request-ID -  <br>  |
| **503** | Service Unavailable |  * Location -  <br>  * X-Request-ID -  <br>  |

<a id="getPaymentInitiationCancellationAuthorisationInformation"></a>
# **getPaymentInitiationCancellationAuthorisationInformation**
> Authorisations getPaymentInitiationCancellationAuthorisationInformation(paymentService, paymentProduct, paymentId, xRequestID, digest, signature, tpPSignatureCertificate, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation)

Will deliver an array of resource identifications to all generated cancellation authorisation sub-resources

Retrieve a list of all created cancellation authorisation sub-resources. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentInitiationServicePisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dev.openbankingproject.ch");
    
    // Configure HTTP bearer authorization: BearerAuthOAuth
    HttpBearerAuth BearerAuthOAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuthOAuth");
    BearerAuthOAuth.setBearerToken("BEARER TOKEN");

    PaymentInitiationServicePisApi apiInstance = new PaymentInitiationServicePisApi(defaultClient);
    String paymentService = "payments"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    String paymentProduct = "domestic-swiss-credit-transfers-isr"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    String paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
    String xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
    String digest = "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A="; // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
    String signature = "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" "; // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    byte[] tpPSignatureCertificate = null; // byte[] | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    String psUIPAddress = "192.168.8.78"; // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
    String psUIPPort = "1234"; // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    String psUAccept = "psUAccept_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptCharset = "psUAcceptCharset_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptEncoding = "psUAcceptEncoding_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptLanguage = "psUAcceptLanguage_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUUserAgent = "psUUserAgent_example"; // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    String psUHttpMethod = "GET"; // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    String psUDeviceID = "99435c7e-ad88-49ec-a2ad-99ddcb1f5555"; // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    String psUGeoLocation = "GEO:52.506931;13.144558"; // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    try {
      Authorisations result = apiInstance.getPaymentInitiationCancellationAuthorisationInformation(paymentService, paymentProduct, paymentId, xRequestID, digest, signature, tpPSignatureCertificate, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentInitiationServicePisApi#getPaymentInitiationCancellationAuthorisationInformation");
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
| **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | [enum: payments, bulk-payments, periodic-payments] |
| **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | [enum: domestic-swiss-credit-transfers-isr, domestic-swiss-credit-transfers, domestic-swiss-credit-transfers-qr, domestic-swiss-foreign-credit-transfers, swiss-sepa-credit-transfers, swiss-cross-border-credit-transfers, pain.001-sepa-credit-transfers, pain.001-cross-border-credit-transfers, pain.001-swiss-six-credit-transfers] |
| **paymentId** | **String**| Resource identification of the generated payment initiation resource. | |
| **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | |
| **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] |
| **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] |
| **tpPSignatureCertificate** | **byte[]**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] |
| **psUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] |
| **psUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] |
| **psUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] |
| **psUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] [enum: GET, POST, PUT, PATCH, DELETE] |
| **psUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] |
| **psUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] |

### Return type

[**Authorisations**](Authorisations.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Request-ID -  <br>  |
| **400** | Bad Request |  * Location -  <br>  * X-Request-ID -  <br>  |
| **401** | Unauthorized |  * Location -  <br>  * X-Request-ID -  <br>  |
| **403** | Forbidden |  * Location -  <br>  * X-Request-ID -  <br>  |
| **404** | Not found |  * Location -  <br>  * X-Request-ID -  <br>  |
| **405** | Method Not Allowed |  * Location -  <br>  * X-Request-ID -  <br>  |
| **406** | Not Acceptable |  * Location -  <br>  * X-Request-ID -  <br>  |
| **408** | Request Timeout |  * Location -  <br>  * X-Request-ID -  <br>  |
| **409** | Conflict |  * Location -  <br>  * X-Request-ID -  <br>  |
| **415** | Unsupported Media Type |  * Location -  <br>  * X-Request-ID -  <br>  |
| **429** | Too Many Requests |  * Location -  <br>  * X-Request-ID -  <br>  |
| **500** | Internal Server Error |  * Location -  <br>  * X-Request-ID -  <br>  |
| **503** | Service Unavailable |  * Location -  <br>  * X-Request-ID -  <br>  |

<a id="getPaymentInitiationScaStatus"></a>
# **getPaymentInitiationScaStatus**
> ScaStatusResponse getPaymentInitiationScaStatus(paymentService, paymentProduct, paymentId, authorisationId, xRequestID, digest, signature, tpPSignatureCertificate, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation)

Read the SCA status of the payment authorisation

This method returns the SCA status of a payment initiation&#39;s authorisation sub-resource. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentInitiationServicePisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dev.openbankingproject.ch");
    
    // Configure HTTP bearer authorization: BearerAuthOAuth
    HttpBearerAuth BearerAuthOAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuthOAuth");
    BearerAuthOAuth.setBearerToken("BEARER TOKEN");

    PaymentInitiationServicePisApi apiInstance = new PaymentInitiationServicePisApi(defaultClient);
    String paymentService = "payments"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    String paymentProduct = "domestic-swiss-credit-transfers-isr"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    String paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
    String authorisationId = "authorisationId_example"; // String | Resource identification of the related SCA.
    String xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
    String digest = "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A="; // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
    String signature = "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" "; // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    byte[] tpPSignatureCertificate = null; // byte[] | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    String psUIPAddress = "192.168.8.78"; // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
    String psUIPPort = "1234"; // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    String psUAccept = "psUAccept_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptCharset = "psUAcceptCharset_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptEncoding = "psUAcceptEncoding_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptLanguage = "psUAcceptLanguage_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUUserAgent = "psUUserAgent_example"; // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    String psUHttpMethod = "GET"; // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    String psUDeviceID = "99435c7e-ad88-49ec-a2ad-99ddcb1f5555"; // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    String psUGeoLocation = "GEO:52.506931;13.144558"; // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    try {
      ScaStatusResponse result = apiInstance.getPaymentInitiationScaStatus(paymentService, paymentProduct, paymentId, authorisationId, xRequestID, digest, signature, tpPSignatureCertificate, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentInitiationServicePisApi#getPaymentInitiationScaStatus");
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
| **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | [enum: payments, bulk-payments, periodic-payments] |
| **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | [enum: domestic-swiss-credit-transfers-isr, domestic-swiss-credit-transfers, domestic-swiss-credit-transfers-qr, domestic-swiss-foreign-credit-transfers, swiss-sepa-credit-transfers, swiss-cross-border-credit-transfers, pain.001-sepa-credit-transfers, pain.001-cross-border-credit-transfers, pain.001-swiss-six-credit-transfers] |
| **paymentId** | **String**| Resource identification of the generated payment initiation resource. | |
| **authorisationId** | **String**| Resource identification of the related SCA. | |
| **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | |
| **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] |
| **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] |
| **tpPSignatureCertificate** | **byte[]**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] |
| **psUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] |
| **psUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] |
| **psUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] |
| **psUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] [enum: GET, POST, PUT, PATCH, DELETE] |
| **psUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] |
| **psUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] |

### Return type

[**ScaStatusResponse**](ScaStatusResponse.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Request-ID -  <br>  |
| **400** | Bad Request |  * Location -  <br>  * X-Request-ID -  <br>  |
| **401** | Unauthorized |  * Location -  <br>  * X-Request-ID -  <br>  |
| **403** | Forbidden |  * Location -  <br>  * X-Request-ID -  <br>  |
| **404** | Not found |  * Location -  <br>  * X-Request-ID -  <br>  |
| **405** | Method Not Allowed |  * Location -  <br>  * X-Request-ID -  <br>  |
| **406** | Not Acceptable |  * Location -  <br>  * X-Request-ID -  <br>  |
| **408** | Request Timeout |  * Location -  <br>  * X-Request-ID -  <br>  |
| **409** | Conflict |  * Location -  <br>  * X-Request-ID -  <br>  |
| **415** | Unsupported Media Type |  * Location -  <br>  * X-Request-ID -  <br>  |
| **429** | Too Many Requests |  * Location -  <br>  * X-Request-ID -  <br>  |
| **500** | Internal Server Error |  * Location -  <br>  * X-Request-ID -  <br>  |
| **503** | Service Unavailable |  * Location -  <br>  * X-Request-ID -  <br>  |

<a id="getPaymentInitiationStatus"></a>
# **getPaymentInitiationStatus**
> PaymentInitiationStatusResponse200Json getPaymentInitiationStatus(paymentService, paymentProduct, paymentId, xRequestID, digest, signature, tpPSignatureCertificate, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation)

Payment initiation status request

Check the transaction status of a payment initiation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentInitiationServicePisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dev.openbankingproject.ch");
    
    // Configure HTTP bearer authorization: BearerAuthOAuth
    HttpBearerAuth BearerAuthOAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuthOAuth");
    BearerAuthOAuth.setBearerToken("BEARER TOKEN");

    PaymentInitiationServicePisApi apiInstance = new PaymentInitiationServicePisApi(defaultClient);
    String paymentService = "payments"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    String paymentProduct = "domestic-swiss-credit-transfers-isr"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    String paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
    String xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
    String digest = "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A="; // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
    String signature = "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" "; // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    byte[] tpPSignatureCertificate = null; // byte[] | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    String psUIPAddress = "192.168.8.78"; // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
    String psUIPPort = "1234"; // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    String psUAccept = "psUAccept_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptCharset = "psUAcceptCharset_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptEncoding = "psUAcceptEncoding_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptLanguage = "psUAcceptLanguage_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUUserAgent = "psUUserAgent_example"; // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    String psUHttpMethod = "GET"; // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    String psUDeviceID = "99435c7e-ad88-49ec-a2ad-99ddcb1f5555"; // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    String psUGeoLocation = "GEO:52.506931;13.144558"; // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    try {
      PaymentInitiationStatusResponse200Json result = apiInstance.getPaymentInitiationStatus(paymentService, paymentProduct, paymentId, xRequestID, digest, signature, tpPSignatureCertificate, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentInitiationServicePisApi#getPaymentInitiationStatus");
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
| **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | [enum: payments, bulk-payments, periodic-payments] |
| **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | [enum: domestic-swiss-credit-transfers-isr, domestic-swiss-credit-transfers, domestic-swiss-credit-transfers-qr, domestic-swiss-foreign-credit-transfers, swiss-sepa-credit-transfers, swiss-cross-border-credit-transfers, pain.001-sepa-credit-transfers, pain.001-cross-border-credit-transfers, pain.001-swiss-six-credit-transfers] |
| **paymentId** | **String**| Resource identification of the generated payment initiation resource. | |
| **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | |
| **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] |
| **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] |
| **tpPSignatureCertificate** | **byte[]**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] |
| **psUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] |
| **psUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] |
| **psUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] |
| **psUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] [enum: GET, POST, PUT, PATCH, DELETE] |
| **psUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] |
| **psUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] |

### Return type

[**PaymentInitiationStatusResponse200Json**](PaymentInitiationStatusResponse200Json.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Request-ID -  <br>  |
| **400** | Bad Request |  * Location -  <br>  * X-Request-ID -  <br>  |
| **401** | Unauthorized |  * Location -  <br>  * X-Request-ID -  <br>  |
| **403** | Forbidden |  * Location -  <br>  * X-Request-ID -  <br>  |
| **404** | Not found |  * Location -  <br>  * X-Request-ID -  <br>  |
| **405** | Method Not Allowed |  * Location -  <br>  * X-Request-ID -  <br>  |
| **406** | Not Acceptable |  * Location -  <br>  * X-Request-ID -  <br>  |
| **408** | Request Timeout |  * Location -  <br>  * X-Request-ID -  <br>  |
| **409** | Conflict |  * Location -  <br>  * X-Request-ID -  <br>  |
| **415** | Unsupported Media Type |  * Location -  <br>  * X-Request-ID -  <br>  |
| **429** | Too Many Requests |  * Location -  <br>  * X-Request-ID -  <br>  |
| **500** | Internal Server Error |  * Location -  <br>  * X-Request-ID -  <br>  |
| **503** | Service Unavailable |  * Location -  <br>  * X-Request-ID -  <br>  |

<a id="initiatePayment"></a>
# **initiatePayment**
> PaymentInitationRequestResponse201 initiatePayment(paymentService, paymentProduct, xRequestID, psUIPAddress, initiatePaymentRequest, digest, signature, tpPSignatureCertificate, PSU_ID, psUIDType, psUCorporateID, psUCorporateIDType, consentID, tpPRedirectPreferred, tpPRedirectURI, tpPNokRedirectURI, tpPExplicitAuthorisationPreferred, tpPRejectionNoFundsPreferred, tpPBrandLoggingInformation, tpPNotificationURI, tpPNotificationContentPreferred, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation)

Payment initiation request

This method is used to initiate a payment at the ASPSP.  ## Variants of payment initiation requests  This method to initiate a payment initiation at the ASPSP can be sent with either a JSON body or an pain.001 body depending on the payment product in the path.  There are the following **payment products**:    - Payment products with payment information in *JSON* format:     - ***domestic-swiss-credit-transfers-isr***     - ***domestic-swiss-credit-transfers***     - ***domestic-swiss-credit-transfers-qr***     - ***domestic-swiss-foreign-credit-transfers***     - ***swiss-sepa-credit-transfers***     - ***swiss-cross-border-credit-transfers***   - Payment products with payment information in *SIX pain.001* XML format:     - ***pain.001-sepa-credit-transfers***     - ***pain.001-cross-border-credit-transfers***     - ***pain.001-swiss-six-credit-transfers***  Furthermore the request body depends on the **payment-service**:   * ***payments***: A single payment initiation request.   * ***bulk-payments***: A collection of several payment initiation requests.        In case of a *pain.001* message there are more than one payments contained in the *pain.001 message.      In case of a *JSON* there are several JSON payment blocks contained in a joining list.   * ***periodic-payments***:     Create a standing order initiation resource for recurrent i.e. periodic payments addressable under {paymentId}      with all data relevant for the corresponding payment product and the execution of the standing order contained in a JSON body.  This is the first step in the API to initiate the related recurring/periodic payment.  ## Single and mulitilevel SCA Processes  The payment initiation requests are independent from the need of one or multilevel  SCA processing, i.e. independent from the number of authorisations needed for the execution of payments.   But the response messages are specific to either one SCA processing or multilevel SCA processing.   For payment initiation with multilevel SCA, this specification requires an explicit start of the authorisation,  i.e. links directly associated with SCA processing like &#39;scaRedirect&#39; or &#39;scaOAuth&#39; cannot be contained in the  response message of a Payment Initation Request for a payment, where multiple authorisations are needed.  Also if any data is needed for the next action, like selecting an SCA method is not supported in the response,  since all starts of the multiple authorisations are fully equal.  In these cases, first an authorisation sub-resource has to be generated following the &#39;startAuthorisation&#39; link. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentInitiationServicePisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dev.openbankingproject.ch");
    
    // Configure HTTP bearer authorization: BearerAuthOAuth
    HttpBearerAuth BearerAuthOAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuthOAuth");
    BearerAuthOAuth.setBearerToken("BEARER TOKEN");

    PaymentInitiationServicePisApi apiInstance = new PaymentInitiationServicePisApi(defaultClient);
    String paymentService = "payments"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    String paymentProduct = "domestic-swiss-credit-transfers-isr"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    String xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
    String psUIPAddress = "192.168.8.78"; // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. If not available, the TPP shall use the IP Address used by the TPP when submitting this request. 
    InitiatePaymentRequest initiatePaymentRequest = new InitiatePaymentRequest(); // InitiatePaymentRequest | JSON request body for a payment inition request message.  There are the following payment-products supported:   * \"domestic-swiss-credit-transfers-isr\"   * \"domestic-swiss-credit-transfers\"   * \"domestic-swiss-credit-transfers-qr\"   * \"domestic-swiss-foreign-credit-transfers\"   * \"swiss-sepa-credit-transfers\" with JSON-Body   * \"swiss-cross-border-credit-transfers\" with JSON-Body   * \"pain.001-sepa-credit-transfers\" with XML pain.001.001.03 body for SCT scheme     Only country specific schemes are currently available   * \"pain.001-cross-border-credit-transfers\" with pain.001 body.     Only country specific schemes are currently available   * \"pain.001-swiss-six-credit-transfers\"  There are the following payment-services supported:   * \"payments\"   * \"periodic-payments\"   * \"bulk-paments\"  All optional, conditional and predefined but not yet used fields are defined. 
    String digest = "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A="; // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
    String signature = "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" "; // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    byte[] tpPSignatureCertificate = null; // byte[] | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    String PSU_ID = "PSU-1234"; // String | Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP's documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation. 
    String psUIDType = "psUIDType_example"; // String | Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP's documentation. 
    String psUCorporateID = "psUCorporateID_example"; // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
    String psUCorporateIDType = "psUCorporateIDType_example"; // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
    String consentID = "consentID_example"; // String | This data element may be contained, if the payment initiation transaction is part of a session, i.e. combined AIS/PIS service. This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
    Boolean tpPRedirectPreferred = true; // Boolean | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU. 
    URI tpPRedirectURI = new URI(); // URI | URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \"true\". It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification. 
    URI tpPNokRedirectURI = new URI(); // URI | If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP. 
    Boolean tpPExplicitAuthorisationPreferred = true; // Boolean | If it equals \"true\", the TPP prefers to start the authorisation process separately, e.g. because of the usage of a signing basket. This preference might be ignored by the ASPSP, if a signing basket is not supported as functionality.  If it equals \"false\" or if the parameter is not used, there is no preference of the TPP. This especially indicates that the TPP assumes a direct authorisation of the transaction in the next step, without using a signing basket. 
    Boolean tpPRejectionNoFundsPreferred = true; // Boolean | If it equals \"true\" then the TPP prefers a rejection of the payment initiation in case the ASPSP is providing an integrated confirmation of funds request an the result of this is that not sufficient funds are available.  If it equals \"false\" then the TPP prefers that the ASPSP is dealing with the payment initiation like in the ASPSPs online channel, potentially waiting for a certain time period for funds to arrive to initiate the payment.  This parameter might be ignored by the ASPSP. 
    String tpPBrandLoggingInformation = "tpPBrandLoggingInformation_example"; // String | This header might be used by TPPs to inform the ASPSP about the brand used by the TPP towards the PSU.  This information is meant for logging entries to enhance communication between ASPSP and PSU or ASPSP and TPP.  This header might be ignored by the ASPSP. 
    String tpPNotificationURI = "tpPNotificationURI_example"; // String | URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  For security reasons, it shall be ensured that the TPP-Notification-URI as introduced above is secured by the TPP eIDAS QWAC used for identification of the TPP. The following applies:  URIs which are provided by TPPs in TPP-Notification-URI shall comply with the domain secured by the eIDAS QWAC certificate of the TPP in the field CN or SubjectAltName of the certificate. Please note that in case of example-TPP.com as certificate entry TPP- Notification-URI like www.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications or notifications.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications would be compliant.  Wildcard definitions shall be taken into account for compliance checks by the ASPSP.  ASPSPs may respond with ASPSP-Notification-Support set to false, if the provided URIs do not comply. 
    String tpPNotificationContentPreferred = "tpPNotificationContentPreferred_example"; // String | The string has the form  status=X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP. 
    String psUIPPort = "1234"; // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    String psUAccept = "psUAccept_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptCharset = "psUAcceptCharset_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptEncoding = "psUAcceptEncoding_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptLanguage = "psUAcceptLanguage_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUUserAgent = "psUUserAgent_example"; // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    String psUHttpMethod = "GET"; // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    String psUDeviceID = "99435c7e-ad88-49ec-a2ad-99ddcb1f5555"; // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    String psUGeoLocation = "GEO:52.506931;13.144558"; // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    try {
      PaymentInitationRequestResponse201 result = apiInstance.initiatePayment(paymentService, paymentProduct, xRequestID, psUIPAddress, initiatePaymentRequest, digest, signature, tpPSignatureCertificate, PSU_ID, psUIDType, psUCorporateID, psUCorporateIDType, consentID, tpPRedirectPreferred, tpPRedirectURI, tpPNokRedirectURI, tpPExplicitAuthorisationPreferred, tpPRejectionNoFundsPreferred, tpPBrandLoggingInformation, tpPNotificationURI, tpPNotificationContentPreferred, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentInitiationServicePisApi#initiatePayment");
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
| **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | [enum: payments, bulk-payments, periodic-payments] |
| **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | [enum: domestic-swiss-credit-transfers-isr, domestic-swiss-credit-transfers, domestic-swiss-credit-transfers-qr, domestic-swiss-foreign-credit-transfers, swiss-sepa-credit-transfers, swiss-cross-border-credit-transfers, pain.001-sepa-credit-transfers, pain.001-cross-border-credit-transfers, pain.001-swiss-six-credit-transfers] |
| **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | |
| **psUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. If not available, the TPP shall use the IP Address used by the TPP when submitting this request.  | |
| **initiatePaymentRequest** | [**InitiatePaymentRequest**](InitiatePaymentRequest.md)| JSON request body for a payment inition request message.  There are the following payment-products supported:   * \&quot;domestic-swiss-credit-transfers-isr\&quot;   * \&quot;domestic-swiss-credit-transfers\&quot;   * \&quot;domestic-swiss-credit-transfers-qr\&quot;   * \&quot;domestic-swiss-foreign-credit-transfers\&quot;   * \&quot;swiss-sepa-credit-transfers\&quot; with JSON-Body   * \&quot;swiss-cross-border-credit-transfers\&quot; with JSON-Body   * \&quot;pain.001-sepa-credit-transfers\&quot; with XML pain.001.001.03 body for SCT scheme     Only country specific schemes are currently available   * \&quot;pain.001-cross-border-credit-transfers\&quot; with pain.001 body.     Only country specific schemes are currently available   * \&quot;pain.001-swiss-six-credit-transfers\&quot;  There are the following payment-services supported:   * \&quot;payments\&quot;   * \&quot;periodic-payments\&quot;   * \&quot;bulk-paments\&quot;  All optional, conditional and predefined but not yet used fields are defined.  | |
| **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] |
| **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] |
| **tpPSignatureCertificate** | **byte[]**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] |
| **PSU_ID** | **String**| Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP&#39;s documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation.  | [optional] |
| **psUIDType** | **String**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP&#39;s documentation.  | [optional] |
| **psUCorporateID** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] |
| **psUCorporateIDType** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] |
| **consentID** | **String**| This data element may be contained, if the payment initiation transaction is part of a session, i.e. combined AIS/PIS service. This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation.  | [optional] |
| **tpPRedirectPreferred** | **Boolean**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] |
| **tpPRedirectURI** | **URI**| URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \&quot;true\&quot;. It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification.  | [optional] |
| **tpPNokRedirectURI** | **URI**| If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP.  | [optional] |
| **tpPExplicitAuthorisationPreferred** | **Boolean**| If it equals \&quot;true\&quot;, the TPP prefers to start the authorisation process separately, e.g. because of the usage of a signing basket. This preference might be ignored by the ASPSP, if a signing basket is not supported as functionality.  If it equals \&quot;false\&quot; or if the parameter is not used, there is no preference of the TPP. This especially indicates that the TPP assumes a direct authorisation of the transaction in the next step, without using a signing basket.  | [optional] |
| **tpPRejectionNoFundsPreferred** | **Boolean**| If it equals \&quot;true\&quot; then the TPP prefers a rejection of the payment initiation in case the ASPSP is providing an integrated confirmation of funds request an the result of this is that not sufficient funds are available.  If it equals \&quot;false\&quot; then the TPP prefers that the ASPSP is dealing with the payment initiation like in the ASPSPs online channel, potentially waiting for a certain time period for funds to arrive to initiate the payment.  This parameter might be ignored by the ASPSP.  | [optional] |
| **tpPBrandLoggingInformation** | **String**| This header might be used by TPPs to inform the ASPSP about the brand used by the TPP towards the PSU.  This information is meant for logging entries to enhance communication between ASPSP and PSU or ASPSP and TPP.  This header might be ignored by the ASPSP.  | [optional] |
| **tpPNotificationURI** | **String**| URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  For security reasons, it shall be ensured that the TPP-Notification-URI as introduced above is secured by the TPP eIDAS QWAC used for identification of the TPP. The following applies:  URIs which are provided by TPPs in TPP-Notification-URI shall comply with the domain secured by the eIDAS QWAC certificate of the TPP in the field CN or SubjectAltName of the certificate. Please note that in case of example-TPP.com as certificate entry TPP- Notification-URI like www.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications or notifications.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications would be compliant.  Wildcard definitions shall be taken into account for compliance checks by the ASPSP.  ASPSPs may respond with ASPSP-Notification-Support set to false, if the provided URIs do not comply.  | [optional] |
| **tpPNotificationContentPreferred** | **String**| The string has the form  status&#x3D;X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP.  | [optional] |
| **psUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] |
| **psUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] |
| **psUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] [enum: GET, POST, PUT, PATCH, DELETE] |
| **psUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] |
| **psUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] |

### Return type

[**PaymentInitationRequestResponse201**](PaymentInitationRequestResponse201.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | CREATED |  * ASPSP-Notification-Content -  <br>  * ASPSP-Notification-Support -  <br>  * ASPSP-SCA-Approach -  <br>  * Location -  <br>  * X-Request-ID -  <br>  |
| **400** | Bad Request |  * Location -  <br>  * X-Request-ID -  <br>  |
| **401** | Unauthorized |  * Location -  <br>  * X-Request-ID -  <br>  |
| **403** | Forbidden |  * Location -  <br>  * X-Request-ID -  <br>  |
| **404** | Not found |  * Location -  <br>  * X-Request-ID -  <br>  |
| **405** | Method Not Allowed |  * Location -  <br>  * X-Request-ID -  <br>  |
| **406** | Not Acceptable |  * Location -  <br>  * X-Request-ID -  <br>  |
| **408** | Request Timeout |  * Location -  <br>  * X-Request-ID -  <br>  |
| **409** | Conflict |  * Location -  <br>  * X-Request-ID -  <br>  |
| **415** | Unsupported Media Type |  * Location -  <br>  * X-Request-ID -  <br>  |
| **429** | Too Many Requests |  * Location -  <br>  * X-Request-ID -  <br>  |
| **500** | Internal Server Error |  * Location -  <br>  * X-Request-ID -  <br>  |
| **503** | Service Unavailable |  * Location -  <br>  * X-Request-ID -  <br>  |

<a id="startPaymentAuthorisation"></a>
# **startPaymentAuthorisation**
> StartScaprocessResponse startPaymentAuthorisation(paymentService, paymentProduct, paymentId, xRequestID, PSU_ID, psUIDType, psUCorporateID, psUCorporateIDType, tpPRedirectPreferred, tpPRedirectURI, tpPNokRedirectURI, tpPNotificationURI, tpPNotificationContentPreferred, digest, signature, tpPSignatureCertificate, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation, startConsentAuthorisationRequest)

Start the authorisation process for a payment initiation

Create an authorisation sub-resource and start the authorisation process. The message might in addition transmit authentication and authorisation related data.  This method is iterated n times for a n times SCA authorisation in a corporate context, each creating an own authorisation sub-endpoint for the corresponding PSU authorising the transaction.  The ASPSP might make the usage of this access method unnecessary in case of only one SCA process needed, since the related authorisation resource might be automatically created by the ASPSP after the submission of the payment data with the first POST payments/{payment-product} call.  The start authorisation process is a process which is needed for creating a new authorisation or cancellation sub-resource.  This applies in the following scenarios:    * The ASPSP has indicated with a &#39;startAuthorisation&#39; hyperlink in the preceding Payment      initiation response that an explicit start of the authorisation process is needed by the TPP.      The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be      uploaded by using the extended forms:     * &#39;startAuthorisationWithPsuIdentfication&#39;     * &#39;startAuthorisationWithPsuAuthentication&#39;     * &#39;startAuthorisationWithEncryptedPsuAuthentication&#39;     * &#39;startAuthorisationWithAuthentciationMethodSelection&#39;   * The related payment initiation cannot yet be executed since a multilevel SCA is mandated.   * The ASPSP has indicated with a &#39;startAuthorisation&#39; hyperlink in the preceding      Payment cancellation response that an explicit start of the authorisation process is needed by the TPP.      The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be uploaded      by using the extended forms as indicated above.   * The related payment cancellation request cannot be applied yet since a multilevel SCA is mandate for     executing the cancellation.   * The signing basket needs to be authorised yet. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentInitiationServicePisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dev.openbankingproject.ch");
    
    // Configure HTTP bearer authorization: BearerAuthOAuth
    HttpBearerAuth BearerAuthOAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuthOAuth");
    BearerAuthOAuth.setBearerToken("BEARER TOKEN");

    PaymentInitiationServicePisApi apiInstance = new PaymentInitiationServicePisApi(defaultClient);
    String paymentService = "payments"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    String paymentProduct = "domestic-swiss-credit-transfers-isr"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    String paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
    String xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
    String PSU_ID = "PSU-1234"; // String | Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP's documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation. 
    String psUIDType = "psUIDType_example"; // String | Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP's documentation. 
    String psUCorporateID = "psUCorporateID_example"; // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
    String psUCorporateIDType = "psUCorporateIDType_example"; // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
    Boolean tpPRedirectPreferred = true; // Boolean | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU. 
    URI tpPRedirectURI = new URI(); // URI | URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \"true\". It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification. 
    URI tpPNokRedirectURI = new URI(); // URI | If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP. 
    String tpPNotificationURI = "tpPNotificationURI_example"; // String | URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  For security reasons, it shall be ensured that the TPP-Notification-URI as introduced above is secured by the TPP eIDAS QWAC used for identification of the TPP. The following applies:  URIs which are provided by TPPs in TPP-Notification-URI shall comply with the domain secured by the eIDAS QWAC certificate of the TPP in the field CN or SubjectAltName of the certificate. Please note that in case of example-TPP.com as certificate entry TPP- Notification-URI like www.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications or notifications.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications would be compliant.  Wildcard definitions shall be taken into account for compliance checks by the ASPSP.  ASPSPs may respond with ASPSP-Notification-Support set to false, if the provided URIs do not comply. 
    String tpPNotificationContentPreferred = "tpPNotificationContentPreferred_example"; // String | The string has the form  status=X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP. 
    String digest = "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A="; // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
    String signature = "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" "; // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    byte[] tpPSignatureCertificate = null; // byte[] | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    String psUIPAddress = "192.168.8.78"; // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
    String psUIPPort = "1234"; // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    String psUAccept = "psUAccept_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptCharset = "psUAcceptCharset_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptEncoding = "psUAcceptEncoding_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptLanguage = "psUAcceptLanguage_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUUserAgent = "psUUserAgent_example"; // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    String psUHttpMethod = "GET"; // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    String psUDeviceID = "99435c7e-ad88-49ec-a2ad-99ddcb1f5555"; // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    String psUGeoLocation = "GEO:52.506931;13.144558"; // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    StartConsentAuthorisationRequest startConsentAuthorisationRequest = new StartConsentAuthorisationRequest(); // StartConsentAuthorisationRequest | 
    try {
      StartScaprocessResponse result = apiInstance.startPaymentAuthorisation(paymentService, paymentProduct, paymentId, xRequestID, PSU_ID, psUIDType, psUCorporateID, psUCorporateIDType, tpPRedirectPreferred, tpPRedirectURI, tpPNokRedirectURI, tpPNotificationURI, tpPNotificationContentPreferred, digest, signature, tpPSignatureCertificate, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation, startConsentAuthorisationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentInitiationServicePisApi#startPaymentAuthorisation");
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
| **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | [enum: payments, bulk-payments, periodic-payments] |
| **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | [enum: domestic-swiss-credit-transfers-isr, domestic-swiss-credit-transfers, domestic-swiss-credit-transfers-qr, domestic-swiss-foreign-credit-transfers, swiss-sepa-credit-transfers, swiss-cross-border-credit-transfers, pain.001-sepa-credit-transfers, pain.001-cross-border-credit-transfers, pain.001-swiss-six-credit-transfers] |
| **paymentId** | **String**| Resource identification of the generated payment initiation resource. | |
| **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | |
| **PSU_ID** | **String**| Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP&#39;s documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation.  | [optional] |
| **psUIDType** | **String**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP&#39;s documentation.  | [optional] |
| **psUCorporateID** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] |
| **psUCorporateIDType** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] |
| **tpPRedirectPreferred** | **Boolean**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] |
| **tpPRedirectURI** | **URI**| URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \&quot;true\&quot;. It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification.  | [optional] |
| **tpPNokRedirectURI** | **URI**| If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP.  | [optional] |
| **tpPNotificationURI** | **String**| URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  For security reasons, it shall be ensured that the TPP-Notification-URI as introduced above is secured by the TPP eIDAS QWAC used for identification of the TPP. The following applies:  URIs which are provided by TPPs in TPP-Notification-URI shall comply with the domain secured by the eIDAS QWAC certificate of the TPP in the field CN or SubjectAltName of the certificate. Please note that in case of example-TPP.com as certificate entry TPP- Notification-URI like www.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications or notifications.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications would be compliant.  Wildcard definitions shall be taken into account for compliance checks by the ASPSP.  ASPSPs may respond with ASPSP-Notification-Support set to false, if the provided URIs do not comply.  | [optional] |
| **tpPNotificationContentPreferred** | **String**| The string has the form  status&#x3D;X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP.  | [optional] |
| **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] |
| **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] |
| **tpPSignatureCertificate** | **byte[]**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] |
| **psUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] |
| **psUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] |
| **psUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] |
| **psUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] [enum: GET, POST, PUT, PATCH, DELETE] |
| **psUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] |
| **psUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] |
| **startConsentAuthorisationRequest** | [**StartConsentAuthorisationRequest**](StartConsentAuthorisationRequest.md)|  | [optional] |

### Return type

[**StartScaprocessResponse**](StartScaprocessResponse.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * ASPSP-SCA-Approach -  <br>  * X-Request-ID -  <br>  |
| **400** | Bad Request |  * Location -  <br>  * X-Request-ID -  <br>  |
| **401** | Unauthorized |  * Location -  <br>  * X-Request-ID -  <br>  |
| **403** | Forbidden |  * Location -  <br>  * X-Request-ID -  <br>  |
| **404** | Not found |  * Location -  <br>  * X-Request-ID -  <br>  |
| **405** | Method Not Allowed |  * Location -  <br>  * X-Request-ID -  <br>  |
| **406** | Not Acceptable |  * Location -  <br>  * X-Request-ID -  <br>  |
| **408** | Request Timeout |  * Location -  <br>  * X-Request-ID -  <br>  |
| **409** | Conflict |  * Location -  <br>  * X-Request-ID -  <br>  |
| **415** | Unsupported Media Type |  * Location -  <br>  * X-Request-ID -  <br>  |
| **429** | Too Many Requests |  * Location -  <br>  * X-Request-ID -  <br>  |
| **500** | Internal Server Error |  * Location -  <br>  * X-Request-ID -  <br>  |
| **503** | Service Unavailable |  * Location -  <br>  * X-Request-ID -  <br>  |

<a id="startPaymentInitiationCancellationAuthorisation"></a>
# **startPaymentInitiationCancellationAuthorisation**
> StartScaprocessResponse startPaymentInitiationCancellationAuthorisation(paymentService, paymentProduct, paymentId, xRequestID, digest, signature, tpPSignatureCertificate, PSU_ID, psUIDType, psUCorporateID, psUCorporateIDType, tpPRedirectPreferred, tpPRedirectURI, tpPNokRedirectURI, tpPNotificationURI, tpPNotificationContentPreferred, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation, startConsentAuthorisationRequest)

Start the authorisation process for the cancellation of the addressed payment

Creates an authorisation sub-resource and start the authorisation process of the cancellation of the addressed payment. The message might in addition transmit authentication and authorisation related data.  This method is iterated n times for a n times SCA authorisation in a corporate context, each creating an own authorisation sub-endpoint for the corresponding PSU authorising the cancellation-authorisation.  The ASPSP might make the usage of this access method unnecessary in case of only one SCA process needed, since the related authorisation resource might be automatically created by the ASPSP after the submission of the payment data with the first POST payments/{payment-product} call.  The start authorisation process is a process which is needed for creating a new authorisation or cancellation sub-resource.  This applies in the following scenarios:    * The ASPSP has indicated with a &#39;startAuthorisation&#39; hyperlink in the preceding payment      initiation response that an explicit start of the authorisation process is needed by the TPP.      The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be      uploaded by using the extended forms:     * &#39;startAuthorisationWithPsuIdentfication&#39;     * &#39;startAuthorisationWithPsuAuthentication&#39;     * &#39;startAuthorisationWithAuthentciationMethodSelection&#39;    * The related payment initiation cannot yet be executed since a multilevel SCA is mandated.   * The ASPSP has indicated with a &#39;startAuthorisation&#39; hyperlink in the preceding      payment cancellation response that an explicit start of the authorisation process is needed by the TPP.      The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be uploaded      by using the extended forms as indicated above.   * The related payment cancellation request cannot be applied yet since a multilevel SCA is mandate for     executing the cancellation.   * The signing basket needs to be authorised yet. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentInitiationServicePisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dev.openbankingproject.ch");
    
    // Configure HTTP bearer authorization: BearerAuthOAuth
    HttpBearerAuth BearerAuthOAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuthOAuth");
    BearerAuthOAuth.setBearerToken("BEARER TOKEN");

    PaymentInitiationServicePisApi apiInstance = new PaymentInitiationServicePisApi(defaultClient);
    String paymentService = "payments"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    String paymentProduct = "domestic-swiss-credit-transfers-isr"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    String paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
    String xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
    String digest = "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A="; // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
    String signature = "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" "; // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    byte[] tpPSignatureCertificate = null; // byte[] | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    String PSU_ID = "PSU-1234"; // String | Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP's documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation. 
    String psUIDType = "psUIDType_example"; // String | Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP's documentation. 
    String psUCorporateID = "psUCorporateID_example"; // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
    String psUCorporateIDType = "psUCorporateIDType_example"; // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
    Boolean tpPRedirectPreferred = true; // Boolean | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU. 
    URI tpPRedirectURI = new URI(); // URI | URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \"true\". It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification. 
    URI tpPNokRedirectURI = new URI(); // URI | If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP. 
    String tpPNotificationURI = "tpPNotificationURI_example"; // String | URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  For security reasons, it shall be ensured that the TPP-Notification-URI as introduced above is secured by the TPP eIDAS QWAC used for identification of the TPP. The following applies:  URIs which are provided by TPPs in TPP-Notification-URI shall comply with the domain secured by the eIDAS QWAC certificate of the TPP in the field CN or SubjectAltName of the certificate. Please note that in case of example-TPP.com as certificate entry TPP- Notification-URI like www.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications or notifications.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications would be compliant.  Wildcard definitions shall be taken into account for compliance checks by the ASPSP.  ASPSPs may respond with ASPSP-Notification-Support set to false, if the provided URIs do not comply. 
    String tpPNotificationContentPreferred = "tpPNotificationContentPreferred_example"; // String | The string has the form  status=X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP. 
    String psUIPAddress = "192.168.8.78"; // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
    String psUIPPort = "1234"; // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    String psUAccept = "psUAccept_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptCharset = "psUAcceptCharset_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptEncoding = "psUAcceptEncoding_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptLanguage = "psUAcceptLanguage_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUUserAgent = "psUUserAgent_example"; // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    String psUHttpMethod = "GET"; // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    String psUDeviceID = "99435c7e-ad88-49ec-a2ad-99ddcb1f5555"; // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    String psUGeoLocation = "GEO:52.506931;13.144558"; // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    StartConsentAuthorisationRequest startConsentAuthorisationRequest = new StartConsentAuthorisationRequest(); // StartConsentAuthorisationRequest | 
    try {
      StartScaprocessResponse result = apiInstance.startPaymentInitiationCancellationAuthorisation(paymentService, paymentProduct, paymentId, xRequestID, digest, signature, tpPSignatureCertificate, PSU_ID, psUIDType, psUCorporateID, psUCorporateIDType, tpPRedirectPreferred, tpPRedirectURI, tpPNokRedirectURI, tpPNotificationURI, tpPNotificationContentPreferred, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation, startConsentAuthorisationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentInitiationServicePisApi#startPaymentInitiationCancellationAuthorisation");
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
| **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | [enum: payments, bulk-payments, periodic-payments] |
| **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | [enum: domestic-swiss-credit-transfers-isr, domestic-swiss-credit-transfers, domestic-swiss-credit-transfers-qr, domestic-swiss-foreign-credit-transfers, swiss-sepa-credit-transfers, swiss-cross-border-credit-transfers, pain.001-sepa-credit-transfers, pain.001-cross-border-credit-transfers, pain.001-swiss-six-credit-transfers] |
| **paymentId** | **String**| Resource identification of the generated payment initiation resource. | |
| **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | |
| **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] |
| **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] |
| **tpPSignatureCertificate** | **byte[]**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] |
| **PSU_ID** | **String**| Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP&#39;s documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation.  | [optional] |
| **psUIDType** | **String**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP&#39;s documentation.  | [optional] |
| **psUCorporateID** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] |
| **psUCorporateIDType** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] |
| **tpPRedirectPreferred** | **Boolean**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] |
| **tpPRedirectURI** | **URI**| URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \&quot;true\&quot;. It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification.  | [optional] |
| **tpPNokRedirectURI** | **URI**| If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP.  | [optional] |
| **tpPNotificationURI** | **String**| URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  For security reasons, it shall be ensured that the TPP-Notification-URI as introduced above is secured by the TPP eIDAS QWAC used for identification of the TPP. The following applies:  URIs which are provided by TPPs in TPP-Notification-URI shall comply with the domain secured by the eIDAS QWAC certificate of the TPP in the field CN or SubjectAltName of the certificate. Please note that in case of example-TPP.com as certificate entry TPP- Notification-URI like www.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications or notifications.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications would be compliant.  Wildcard definitions shall be taken into account for compliance checks by the ASPSP.  ASPSPs may respond with ASPSP-Notification-Support set to false, if the provided URIs do not comply.  | [optional] |
| **tpPNotificationContentPreferred** | **String**| The string has the form  status&#x3D;X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP.  | [optional] |
| **psUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] |
| **psUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] |
| **psUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] |
| **psUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] [enum: GET, POST, PUT, PATCH, DELETE] |
| **psUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] |
| **psUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] |
| **startConsentAuthorisationRequest** | [**StartConsentAuthorisationRequest**](StartConsentAuthorisationRequest.md)|  | [optional] |

### Return type

[**StartScaprocessResponse**](StartScaprocessResponse.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * ASPSP-SCA-Approach -  <br>  * X-Request-ID -  <br>  |
| **400** | Bad Request |  * Location -  <br>  * X-Request-ID -  <br>  |
| **401** | Unauthorized |  * Location -  <br>  * X-Request-ID -  <br>  |
| **403** | Forbidden |  * Location -  <br>  * X-Request-ID -  <br>  |
| **404** | Not found |  * Location -  <br>  * X-Request-ID -  <br>  |
| **405** | Method Not Allowed |  * Location -  <br>  * X-Request-ID -  <br>  |
| **406** | Not Acceptable |  * Location -  <br>  * X-Request-ID -  <br>  |
| **408** | Request Timeout |  * Location -  <br>  * X-Request-ID -  <br>  |
| **409** | Conflict |  * Location -  <br>  * X-Request-ID -  <br>  |
| **415** | Unsupported Media Type |  * Location -  <br>  * X-Request-ID -  <br>  |
| **429** | Too Many Requests |  * Location -  <br>  * X-Request-ID -  <br>  |
| **500** | Internal Server Error |  * Location -  <br>  * X-Request-ID -  <br>  |
| **503** | Service Unavailable |  * Location -  <br>  * X-Request-ID -  <br>  |

<a id="updatePaymentCancellationPsuData"></a>
# **updatePaymentCancellationPsuData**
> UpdateConsentsPsuData200Response updatePaymentCancellationPsuData(paymentService, paymentProduct, paymentId, authorisationId, xRequestID, digest, signature, tpPSignatureCertificate, PSU_ID, psUIDType, psUCorporateID, psUCorporateIDType, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation, updateConsentsPsuDataRequest)

Update PSU data for payment initiation cancellation

This method updates PSU data on the cancellation authorisation resource if needed.  It may authorise a cancellation of the payment within the Embedded SCA Approach where needed.  Independently from the SCA Approach it supports e.g. the selection of the authentication method and a non-SCA PSU authentication.  There are several possible update PSU data requests in the context of a cancellation authorisation within the payment initiation services needed,  which depends on the SCA approach:  * Redirect SCA Approach:   A specific Update PSU data request is applicable for      * the selection of authentication methods, before choosing the actual SCA approach. * Decoupled SCA Approach:   A specific Update PSU data request is only applicable for   * adding the PSU Identification, if not provided yet in the payment initiation request or the Account Information Consent Request, or if no OAuth2 access token is used, or   * the selection of authentication methods. * Embedded SCA Approach:    The Update PSU data request might be used    * to add credentials as a first factor authentication data of the PSU and   * to select the authentication method and   * transaction authorisation.  The SCA approach might depend on the chosen SCA method.  For that reason, the following possible update PSU data request can apply to all SCA approaches:  * Select an SCA method in case of several SCA methods are available for the customer.  There are the following request types on this access path:   * Update PSU identification   * Update PSU authentication   * Select PSU autorization method      WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change.   * Transaction Authorisation     WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentInitiationServicePisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dev.openbankingproject.ch");
    
    // Configure HTTP bearer authorization: BearerAuthOAuth
    HttpBearerAuth BearerAuthOAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuthOAuth");
    BearerAuthOAuth.setBearerToken("BEARER TOKEN");

    PaymentInitiationServicePisApi apiInstance = new PaymentInitiationServicePisApi(defaultClient);
    String paymentService = "payments"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    String paymentProduct = "domestic-swiss-credit-transfers-isr"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    String paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
    String authorisationId = "authorisationId_example"; // String | Resource identification of the related SCA.
    String xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
    String digest = "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A="; // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
    String signature = "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" "; // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    byte[] tpPSignatureCertificate = null; // byte[] | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    String PSU_ID = "PSU-1234"; // String | Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP's documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation. 
    String psUIDType = "psUIDType_example"; // String | Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP's documentation. 
    String psUCorporateID = "psUCorporateID_example"; // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
    String psUCorporateIDType = "psUCorporateIDType_example"; // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
    String psUIPAddress = "192.168.8.78"; // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
    String psUIPPort = "1234"; // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    String psUAccept = "psUAccept_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptCharset = "psUAcceptCharset_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptEncoding = "psUAcceptEncoding_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptLanguage = "psUAcceptLanguage_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUUserAgent = "psUUserAgent_example"; // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    String psUHttpMethod = "GET"; // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    String psUDeviceID = "99435c7e-ad88-49ec-a2ad-99ddcb1f5555"; // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    String psUGeoLocation = "GEO:52.506931;13.144558"; // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    UpdateConsentsPsuDataRequest updateConsentsPsuDataRequest = new UpdateConsentsPsuDataRequest(); // UpdateConsentsPsuDataRequest | 
    try {
      UpdateConsentsPsuData200Response result = apiInstance.updatePaymentCancellationPsuData(paymentService, paymentProduct, paymentId, authorisationId, xRequestID, digest, signature, tpPSignatureCertificate, PSU_ID, psUIDType, psUCorporateID, psUCorporateIDType, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation, updateConsentsPsuDataRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentInitiationServicePisApi#updatePaymentCancellationPsuData");
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
| **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | [enum: payments, bulk-payments, periodic-payments] |
| **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | [enum: domestic-swiss-credit-transfers-isr, domestic-swiss-credit-transfers, domestic-swiss-credit-transfers-qr, domestic-swiss-foreign-credit-transfers, swiss-sepa-credit-transfers, swiss-cross-border-credit-transfers, pain.001-sepa-credit-transfers, pain.001-cross-border-credit-transfers, pain.001-swiss-six-credit-transfers] |
| **paymentId** | **String**| Resource identification of the generated payment initiation resource. | |
| **authorisationId** | **String**| Resource identification of the related SCA. | |
| **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | |
| **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] |
| **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] |
| **tpPSignatureCertificate** | **byte[]**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] |
| **PSU_ID** | **String**| Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP&#39;s documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation.  | [optional] |
| **psUIDType** | **String**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP&#39;s documentation.  | [optional] |
| **psUCorporateID** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] |
| **psUCorporateIDType** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] |
| **psUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] |
| **psUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] |
| **psUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] |
| **psUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] [enum: GET, POST, PUT, PATCH, DELETE] |
| **psUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] |
| **psUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] |
| **updateConsentsPsuDataRequest** | [**UpdateConsentsPsuDataRequest**](UpdateConsentsPsuDataRequest.md)|  | [optional] |

### Return type

[**UpdateConsentsPsuData200Response**](UpdateConsentsPsuData200Response.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * ASPSP-SCA-Approach -  <br>  * X-Request-ID -  <br>  |
| **400** | Bad Request |  * Location -  <br>  * X-Request-ID -  <br>  |
| **401** | Unauthorized |  * Location -  <br>  * X-Request-ID -  <br>  |
| **403** | Forbidden |  * Location -  <br>  * X-Request-ID -  <br>  |
| **404** | Not found |  * Location -  <br>  * X-Request-ID -  <br>  |
| **405** | Method Not Allowed |  * Location -  <br>  * X-Request-ID -  <br>  |
| **406** | Not Acceptable |  * Location -  <br>  * X-Request-ID -  <br>  |
| **408** | Request Timeout |  * Location -  <br>  * X-Request-ID -  <br>  |
| **409** | Conflict |  * Location -  <br>  * X-Request-ID -  <br>  |
| **415** | Unsupported Media Type |  * Location -  <br>  * X-Request-ID -  <br>  |
| **429** | Too Many Requests |  * Location -  <br>  * X-Request-ID -  <br>  |
| **500** | Internal Server Error |  * Location -  <br>  * X-Request-ID -  <br>  |
| **503** | Service Unavailable |  * Location -  <br>  * X-Request-ID -  <br>  |

<a id="updatePaymentPsuData"></a>
# **updatePaymentPsuData**
> UpdateConsentsPsuData200Response updatePaymentPsuData(paymentService, paymentProduct, paymentId, authorisationId, xRequestID, digest, signature, tpPSignatureCertificate, PSU_ID, psUIDType, psUCorporateID, psUCorporateIDType, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation, updateConsentsPsuDataRequest)

Update PSU data for payment initiation

This methods updates PSU data on the authorisation resource if needed. It may authorise a payment within the Embedded SCA Approach where needed.  Independently from the SCA Approach it supports e.g. the selection of the authentication method and a non-SCA PSU authentication.  There are several possible update PSU data requests in the context of payment initiation services needed,  which depends on the SCA approach:  * Redirect SCA Approach:   A specific update PSU data request is applicable for      * the selection of authentication methods, before choosing the actual SCA approach. * Decoupled SCA Approach:   A specific update PSU data request is only applicable for   * adding the PSU identification, if not provided yet in the payment initiation request or the account information consent request, or if no OAuth2 access token is used, or   * the selection of authentication methods. * Embedded SCA Approach:    The Update PSU Data request might be used    * to add credentials as a first factor authentication data of the PSU and   * to select the authentication method and   * transaction authorisation.  The SCA Approach might depend on the chosen SCA method.  For that reason, the following possible Update PSU data request can apply to all SCA approaches:  * Select an SCA method in case of several SCA methods are available for the customer.  There are the following request types on this access path:   * Update PSU identification   * Update PSU authentication   * Select PSU autorization method      WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change.   * Transaction authorisation     WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentInitiationServicePisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dev.openbankingproject.ch");
    
    // Configure HTTP bearer authorization: BearerAuthOAuth
    HttpBearerAuth BearerAuthOAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuthOAuth");
    BearerAuthOAuth.setBearerToken("BEARER TOKEN");

    PaymentInitiationServicePisApi apiInstance = new PaymentInitiationServicePisApi(defaultClient);
    String paymentService = "payments"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
    String paymentProduct = "domestic-swiss-credit-transfers-isr"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
    String paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
    String authorisationId = "authorisationId_example"; // String | Resource identification of the related SCA.
    String xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
    String digest = "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A="; // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
    String signature = "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" "; // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    byte[] tpPSignatureCertificate = null; // byte[] | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    String PSU_ID = "PSU-1234"; // String | Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP's documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation. 
    String psUIDType = "psUIDType_example"; // String | Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP's documentation. 
    String psUCorporateID = "psUCorporateID_example"; // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
    String psUCorporateIDType = "psUCorporateIDType_example"; // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
    String psUIPAddress = "192.168.8.78"; // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
    String psUIPPort = "1234"; // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
    String psUAccept = "psUAccept_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptCharset = "psUAcceptCharset_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptEncoding = "psUAcceptEncoding_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUAcceptLanguage = "psUAcceptLanguage_example"; // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
    String psUUserAgent = "psUUserAgent_example"; // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
    String psUHttpMethod = "GET"; // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
    String psUDeviceID = "99435c7e-ad88-49ec-a2ad-99ddcb1f5555"; // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
    String psUGeoLocation = "GEO:52.506931;13.144558"; // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
    UpdateConsentsPsuDataRequest updateConsentsPsuDataRequest = new UpdateConsentsPsuDataRequest(); // UpdateConsentsPsuDataRequest | 
    try {
      UpdateConsentsPsuData200Response result = apiInstance.updatePaymentPsuData(paymentService, paymentProduct, paymentId, authorisationId, xRequestID, digest, signature, tpPSignatureCertificate, PSU_ID, psUIDType, psUCorporateID, psUCorporateIDType, psUIPAddress, psUIPPort, psUAccept, psUAcceptCharset, psUAcceptEncoding, psUAcceptLanguage, psUUserAgent, psUHttpMethod, psUDeviceID, psUGeoLocation, updateConsentsPsuDataRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentInitiationServicePisApi#updatePaymentPsuData");
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
| **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | [enum: payments, bulk-payments, periodic-payments] |
| **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | [enum: domestic-swiss-credit-transfers-isr, domestic-swiss-credit-transfers, domestic-swiss-credit-transfers-qr, domestic-swiss-foreign-credit-transfers, swiss-sepa-credit-transfers, swiss-cross-border-credit-transfers, pain.001-sepa-credit-transfers, pain.001-cross-border-credit-transfers, pain.001-swiss-six-credit-transfers] |
| **paymentId** | **String**| Resource identification of the generated payment initiation resource. | |
| **authorisationId** | **String**| Resource identification of the related SCA. | |
| **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | |
| **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] |
| **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] |
| **tpPSignatureCertificate** | **byte[]**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] |
| **PSU_ID** | **String**| Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP&#39;s documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation.  | [optional] |
| **psUIDType** | **String**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP&#39;s documentation.  | [optional] |
| **psUCorporateID** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] |
| **psUCorporateIDType** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] |
| **psUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] |
| **psUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] |
| **psUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] |
| **psUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] |
| **psUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] [enum: GET, POST, PUT, PATCH, DELETE] |
| **psUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] |
| **psUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] |
| **updateConsentsPsuDataRequest** | [**UpdateConsentsPsuDataRequest**](UpdateConsentsPsuDataRequest.md)|  | [optional] |

### Return type

[**UpdateConsentsPsuData200Response**](UpdateConsentsPsuData200Response.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * ASPSP-SCA-Approach -  <br>  * X-Request-ID -  <br>  |
| **400** | Bad Request |  * Location -  <br>  * X-Request-ID -  <br>  |
| **401** | Unauthorized |  * Location -  <br>  * X-Request-ID -  <br>  |
| **403** | Forbidden |  * Location -  <br>  * X-Request-ID -  <br>  |
| **404** | Not found |  * Location -  <br>  * X-Request-ID -  <br>  |
| **405** | Method Not Allowed |  * Location -  <br>  * X-Request-ID -  <br>  |
| **406** | Not Acceptable |  * Location -  <br>  * X-Request-ID -  <br>  |
| **408** | Request Timeout |  * Location -  <br>  * X-Request-ID -  <br>  |
| **409** | Conflict |  * Location -  <br>  * X-Request-ID -  <br>  |
| **415** | Unsupported Media Type |  * Location -  <br>  * X-Request-ID -  <br>  |
| **429** | Too Many Requests |  * Location -  <br>  * X-Request-ID -  <br>  |
| **500** | Internal Server Error |  * Location -  <br>  * X-Request-ID -  <br>  |
| **503** | Service Unavailable |  * Location -  <br>  * X-Request-ID -  <br>  |

