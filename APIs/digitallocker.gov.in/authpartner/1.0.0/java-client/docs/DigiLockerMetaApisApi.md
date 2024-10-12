# DigiLockerMetaApisApi

All URIs are relative to *https://betaapi.digitallocker.gov.in/public*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getListOfDocumentsProvidedByAnIssuerId**](DigiLockerMetaApisApi.md#getListOfDocumentsProvidedByAnIssuerId) | **POST** /oauth2/1/pull/doctype | Get List of Documents Provided by an Issuer |
| [**getListOfIssuersId**](DigiLockerMetaApisApi.md#getListOfIssuersId) | **POST** /oauth2/1/pull/issuers | Get List of Issuers |
| [**getSearchParametersForADocumentId**](DigiLockerMetaApisApi.md#getSearchParametersForADocumentId) | **POST** /oauth2/1/pull/parameters | Get Search Parameters for a Document |
| [**getStatisticsId**](DigiLockerMetaApisApi.md#getStatisticsId) | **POST** /statistics/1/counts | Get Statistics |
| [**pushURIToAccountId**](DigiLockerMetaApisApi.md#pushURIToAccountId) | **POST** /account/1/pushuri | Push URI to Account |
| [**verifyAccountId**](DigiLockerMetaApisApi.md#verifyAccountId) | **POST** /account/2/verify | Verify Account |


<a id="getListOfDocumentsProvidedByAnIssuerId"></a>
# **getListOfDocumentsProvidedByAnIssuerId**
> DocTypeResponse getListOfDocumentsProvidedByAnIssuerId(clientid, hmac, orgid, ts)

Get List of Documents Provided by an Issuer

Returns a list of documents/certificates issued by an issuer organization registered with DigiLocker.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DigiLockerMetaApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure OAuth2 access token for authorization: oauthsecurity
    OAuth oauthsecurity = (OAuth) defaultClient.getAuthentication("oauthsecurity");
    oauthsecurity.setAccessToken("YOUR ACCESS TOKEN");

    DigiLockerMetaApisApi apiInstance = new DigiLockerMetaApisApi(defaultClient);
    String clientid = "clientid_example"; // String | Provide the client id that was created during the application registration process on Partners Portal.
    File hmac = new File("/path/to/file"); // File | Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
    String orgid = "orgid_example"; // String | The organization id for the issuer in DigiLocker. This organization id is returned in Get List of Issuers API mentioned earlier.
    String ts = "ts_example"; // String | Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
    try {
      DocTypeResponse result = apiInstance.getListOfDocumentsProvidedByAnIssuerId(clientid, hmac, orgid, ts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DigiLockerMetaApisApi#getListOfDocumentsProvidedByAnIssuerId");
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
| **clientid** | **String**| Provide the client id that was created during the application registration process on Partners Portal. | [optional] |
| **hmac** | **File**| Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret. | [optional] |
| **orgid** | **String**| The organization id for the issuer in DigiLocker. This organization id is returned in Get List of Issuers API mentioned earlier. | [optional] |
| **ts** | **String**| Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes. | [optional] |

### Return type

[**DocTypeResponse**](DocTypeResponse.md)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized error |  -  |
| **500** | Internal Error |  -  |

<a id="getListOfIssuersId"></a>
# **getListOfIssuersId**
> IssuerResponse getListOfIssuersId(clientid, hmac, ts)

Get List of Issuers

Returns the list of issuers registered with DigiLocker.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DigiLockerMetaApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure OAuth2 access token for authorization: oauthsecurity
    OAuth oauthsecurity = (OAuth) defaultClient.getAuthentication("oauthsecurity");
    oauthsecurity.setAccessToken("YOUR ACCESS TOKEN");

    DigiLockerMetaApisApi apiInstance = new DigiLockerMetaApisApi(defaultClient);
    String clientid = "clientid_example"; // String | Provide the client id that was created during the application registration process on Partners Portal.
    File hmac = new File("/path/to/file"); // File | Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
    String ts = "ts_example"; // String | Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
    try {
      IssuerResponse result = apiInstance.getListOfIssuersId(clientid, hmac, ts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DigiLockerMetaApisApi#getListOfIssuersId");
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
| **clientid** | **String**| Provide the client id that was created during the application registration process on Partners Portal. | [optional] |
| **hmac** | **File**| Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret. | [optional] |
| **ts** | **String**| Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes. | [optional] |

### Return type

[**IssuerResponse**](IssuerResponse.md)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized error |  -  |
| **500** | Internal Error |  -  |

<a id="getSearchParametersForADocumentId"></a>
# **getSearchParametersForADocumentId**
> Set&lt;SearchParametersResponseInner&gt; getSearchParametersForADocumentId(clientid, doctype, hmac, orgid, ts)

Get Search Parameters for a Document

Returns a list of parameters required to search a document/certificate of an issuer organization registered with DigiLocker. These parameters are used to pull a document from issuer’s repository using Pull Document API mentioned in subsequent section.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DigiLockerMetaApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure OAuth2 access token for authorization: oauthsecurity
    OAuth oauthsecurity = (OAuth) defaultClient.getAuthentication("oauthsecurity");
    oauthsecurity.setAccessToken("YOUR ACCESS TOKEN");

    DigiLockerMetaApisApi apiInstance = new DigiLockerMetaApisApi(defaultClient);
    String clientid = "clientid_example"; // String | Provide the client id that was created during the application registration process on Partners Portal.
    String doctype = "doctype_example"; // String | A 5 character unique document type provided by DigiLocker.
    File hmac = new File("/path/to/file"); // File | Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
    String orgid = "orgid_example"; // String | The organization id for the issuer in DigiLocker. This organization id is returned in Get List of Issuers API mentioned earlier.
    String ts = "ts_example"; // String | Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
    try {
      Set<SearchParametersResponseInner> result = apiInstance.getSearchParametersForADocumentId(clientid, doctype, hmac, orgid, ts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DigiLockerMetaApisApi#getSearchParametersForADocumentId");
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
| **clientid** | **String**| Provide the client id that was created during the application registration process on Partners Portal. | [optional] |
| **doctype** | **String**| A 5 character unique document type provided by DigiLocker. | [optional] |
| **hmac** | **File**| Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret. | [optional] |
| **orgid** | **String**| The organization id for the issuer in DigiLocker. This organization id is returned in Get List of Issuers API mentioned earlier. | [optional] |
| **ts** | **String**| Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes. | [optional] |

### Return type

[**Set&lt;SearchParametersResponseInner&gt;**](SearchParametersResponseInner.md)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized error |  -  |
| **500** | Internal Error |  -  |

<a id="getStatisticsId"></a>
# **getStatisticsId**
> GetStatisticsResponse getStatisticsId(clientid, hmac, ts)

Get Statistics

Returns DigiLocker statistics such as the count of users, authentic documents, issuers and requesters as on a specific date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DigiLockerMetaApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure OAuth2 access token for authorization: oauthsecurity
    OAuth oauthsecurity = (OAuth) defaultClient.getAuthentication("oauthsecurity");
    oauthsecurity.setAccessToken("YOUR ACCESS TOKEN");

    DigiLockerMetaApisApi apiInstance = new DigiLockerMetaApisApi(defaultClient);
    String clientid = "clientid_example"; // String | Provide the client id that was created during the application registration process on Partners Portal.
    File hmac = new File("/path/to/file"); // File | Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
    String ts = "ts_example"; // String | Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
    try {
      GetStatisticsResponse result = apiInstance.getStatisticsId(clientid, hmac, ts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DigiLockerMetaApisApi#getStatisticsId");
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
| **clientid** | **String**| Provide the client id that was created during the application registration process on Partners Portal. | [optional] |
| **hmac** | **File**| Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret. | [optional] |
| **ts** | **String**| Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes. | [optional] |

### Return type

[**GetStatisticsResponse**](GetStatisticsResponse.md)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized error |  -  |
| **500** | Internal Error |  -  |

<a id="pushURIToAccountId"></a>
# **pushURIToAccountId**
> Object pushURIToAccountId(action, clientid, digilockerid, docid, hmac, issuedate, ts, uri, validfrom, validto)

Push URI to Account

The API can use to push or delete a single URI into Digital Locker using DigiLocker Id acquired using Get User Details API. This API can be used to push the certificate details to Digital Locker as and when a certificate is generated in the issuer system. The issuing departments must register on DigiLocker as a registered Issuer and implement the requisite Issuer APIs as mentioned in Digital Locker Issuer API Specification document prior to pushing certificates using this API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DigiLockerMetaApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure OAuth2 access token for authorization: oauthsecurity
    OAuth oauthsecurity = (OAuth) defaultClient.getAuthentication("oauthsecurity");
    oauthsecurity.setAccessToken("YOUR ACCESS TOKEN");

    DigiLockerMetaApisApi apiInstance = new DigiLockerMetaApisApi(defaultClient);
    String action = "action_example"; // String | Action that needs to be taken for the Aadhaar number and URI combination. Possible values are A for adding a new URI, U for updating an already added URI details or D for deleting the URI.
    String clientid = "clientid_example"; // String | Provide the client id that was created during the application registration process on Partners Portal.
    Integer digilockerid = 56; // Integer | This is the DigiLocker Id of the user that was acquired using Get User Details API.
    String docid = "docid_example"; // String | A unique number of the document. This id will be unique within the document type issued by the issuer.
    File hmac = new File("/path/to/file"); // File | Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
    String issuedate = "issuedate_example"; // String | The issue date of the document in DDMMYYYY format.
    String ts = "ts_example"; // String | Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
    String uri = "uri_example"; // String | This is the unique identifier of the document.
    Integer validfrom = 56; // Integer | The date from which the document is valid in DDMMYYYY format. This may be same as the issue date.
    String validto = "validto_example"; // String | The expiry date of the document in DDMMYYYY format.
    try {
      Object result = apiInstance.pushURIToAccountId(action, clientid, digilockerid, docid, hmac, issuedate, ts, uri, validfrom, validto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DigiLockerMetaApisApi#pushURIToAccountId");
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
| **action** | **String**| Action that needs to be taken for the Aadhaar number and URI combination. Possible values are A for adding a new URI, U for updating an already added URI details or D for deleting the URI. | [optional] |
| **clientid** | **String**| Provide the client id that was created during the application registration process on Partners Portal. | [optional] |
| **digilockerid** | **Integer**| This is the DigiLocker Id of the user that was acquired using Get User Details API. | [optional] |
| **docid** | **String**| A unique number of the document. This id will be unique within the document type issued by the issuer. | [optional] |
| **hmac** | **File**| Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret. | [optional] |
| **issuedate** | **String**| The issue date of the document in DDMMYYYY format. | [optional] |
| **ts** | **String**| Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes. | [optional] |
| **uri** | **String**| This is the unique identifier of the document. | [optional] |
| **validfrom** | **Integer**| The date from which the document is valid in DDMMYYYY format. This may be same as the issue date. | [optional] |
| **validto** | **String**| The expiry date of the document in DDMMYYYY format. | [optional] |

### Return type

**Object**

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized error |  -  |
| **404** | Not found |  -  |
| **500** | Internal Error |  -  |

<a id="verifyAccountId"></a>
# **verifyAccountId**
> VerifyAccountResponse verifyAccountId(clientid, hmac, mobile, ts, uid)

Verify Account

This API can be used to verify whether a mobile number or Aadhaar number is already registered with DigiLocker.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DigiLockerMetaApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure OAuth2 access token for authorization: oauthsecurity
    OAuth oauthsecurity = (OAuth) defaultClient.getAuthentication("oauthsecurity");
    oauthsecurity.setAccessToken("YOUR ACCESS TOKEN");

    DigiLockerMetaApisApi apiInstance = new DigiLockerMetaApisApi(defaultClient);
    String clientid = "clientid_example"; // String | Provide the client id that was created during the application registration process on Partners Portal.
    File hmac = new File("/path/to/file"); // File | Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
    Integer mobile = 56; // Integer | This is the mobile number of the user. DigiLocker will check whether an account exists for this mobile number. Either uid or mobile is required to verify whether an account exists.
    String ts = "ts_example"; // String | Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
    Integer uid = 56; // Integer | This is the Aadhaar number of the user. DigiLocker will check whether an account exists for this Aadhaar number. Either uid or mobile is required to verify whether an account exists.
    try {
      VerifyAccountResponse result = apiInstance.verifyAccountId(clientid, hmac, mobile, ts, uid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DigiLockerMetaApisApi#verifyAccountId");
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
| **clientid** | **String**| Provide the client id that was created during the application registration process on Partners Portal. | [optional] |
| **hmac** | **File**| Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret. | [optional] |
| **mobile** | **Integer**| This is the mobile number of the user. DigiLocker will check whether an account exists for this mobile number. Either uid or mobile is required to verify whether an account exists. | [optional] |
| **ts** | **String**| Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes. | [optional] |
| **uid** | **Integer**| This is the Aadhaar number of the user. DigiLocker will check whether an account exists for this Aadhaar number. Either uid or mobile is required to verify whether an account exists. | [optional] |

### Return type

[**VerifyAccountResponse**](VerifyAccountResponse.md)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized error |  -  |
| **500** | Internal Error |  -  |

