# ConfirmationOfFundsServicePiisApi

All URIs are relative to *https://api.dev.openbankingproject.ch*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkAvailabilityOfFunds**](ConfirmationOfFundsServicePiisApi.md#checkAvailabilityOfFunds) | **POST** /v1/funds-confirmations | Confirmation of funds request |


<a id="checkAvailabilityOfFunds"></a>
# **checkAvailabilityOfFunds**
> CheckAvailabilityOfFunds200Response checkAvailabilityOfFunds(xRequestID, confirmationOfFunds, authorization, digest, signature, tpPSignatureCertificate)

Confirmation of funds request

Creates a confirmation of funds request at the ASPSP. Checks whether a specific amount is available at point of time of the request on an account linked to a given tuple card issuer(TPP)/card number, or addressed by IBAN and TPP respectively. If the related extended services are used a conditional Consent-ID is contained in the header. This field is contained but commented out in this specification.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfirmationOfFundsServicePiisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dev.openbankingproject.ch");
    
    // Configure HTTP bearer authorization: BearerAuthOAuth
    HttpBearerAuth BearerAuthOAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuthOAuth");
    BearerAuthOAuth.setBearerToken("BEARER TOKEN");

    ConfirmationOfFundsServicePiisApi apiInstance = new ConfirmationOfFundsServicePiisApi(defaultClient);
    String xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
    ConfirmationOfFunds confirmationOfFunds = new ConfirmationOfFunds(); // ConfirmationOfFunds | Request body for a confirmation of funds request. 
    String authorization = "authorization_example"; // String | This field  might be used in case where a consent was agreed between ASPSP and PSU through an OAuth2 based protocol, facilitated by the TPP. 
    String digest = "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A="; // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
    String signature = "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" "; // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
    byte[] tpPSignatureCertificate = null; // byte[] | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
    try {
      CheckAvailabilityOfFunds200Response result = apiInstance.checkAvailabilityOfFunds(xRequestID, confirmationOfFunds, authorization, digest, signature, tpPSignatureCertificate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfirmationOfFundsServicePiisApi#checkAvailabilityOfFunds");
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
| **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | |
| **confirmationOfFunds** | [**ConfirmationOfFunds**](ConfirmationOfFunds.md)| Request body for a confirmation of funds request.  | |
| **authorization** | **String**| This field  might be used in case where a consent was agreed between ASPSP and PSU through an OAuth2 based protocol, facilitated by the TPP.  | [optional] |
| **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] |
| **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] |
| **tpPSignatureCertificate** | **byte[]**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] |

### Return type

[**CheckAvailabilityOfFunds200Response**](CheckAvailabilityOfFunds200Response.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Location -  <br>  * X-Request-ID -  <br>  |
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

