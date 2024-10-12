# PayeesApi

All URIs are relative to *https://api.sandbox.velopayments.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deletePayeeByIdV3**](PayeesApi.md#deletePayeeByIdV3) | **DELETE** /v3/payees/{payeeId} | Delete Payee by Id |
| [**deletePayeeByIdV4**](PayeesApi.md#deletePayeeByIdV4) | **DELETE** /v4/payees/{payeeId} | Delete Payee by Id |
| [**getPayeeByIdV3**](PayeesApi.md#getPayeeByIdV3) | **GET** /v3/payees/{payeeId} | Get Payee by Id |
| [**getPayeeByIdV4**](PayeesApi.md#getPayeeByIdV4) | **GET** /v4/payees/{payeeId} | Get Payee by Id |
| [**listPayeeChangesV3**](PayeesApi.md#listPayeeChangesV3) | **GET** /v3/payees/deltas | List Payee Changes |
| [**listPayeeChangesV4**](PayeesApi.md#listPayeeChangesV4) | **GET** /v4/payees/deltas | List Payee Changes |
| [**listPayeesV3**](PayeesApi.md#listPayeesV3) | **GET** /v3/payees | List Payees |
| [**listPayeesV4**](PayeesApi.md#listPayeesV4) | **GET** /v4/payees | List Payees |
| [**payeeDetailsUpdateV3**](PayeesApi.md#payeeDetailsUpdateV3) | **POST** /v3/payees/{payeeId}/payeeDetailsUpdate | Update Payee Details |
| [**payeeDetailsUpdateV4**](PayeesApi.md#payeeDetailsUpdateV4) | **POST** /v4/payees/{payeeId}/payeeDetailsUpdate | Update Payee Details |
| [**v3PayeesPayeeIdRemoteIdUpdatePost**](PayeesApi.md#v3PayeesPayeeIdRemoteIdUpdatePost) | **POST** /v3/payees/{payeeId}/remoteIdUpdate | Update Payee Remote Id |
| [**v4PayeesPayeeIdRemoteIdUpdatePost**](PayeesApi.md#v4PayeesPayeeIdRemoteIdUpdatePost) | **POST** /v4/payees/{payeeId}/remoteIdUpdate | Update Payee Remote Id |


<a id="deletePayeeByIdV3"></a>
# **deletePayeeByIdV3**
> deletePayeeByIdV3(payeeId)

Delete Payee by Id

&lt;p&gt;Use v4 instead&lt;/p&gt; &lt;p&gt;This API will delete Payee by Id (UUID). Deletion by ID is not allowed if:&lt;/p&gt; &lt;p&gt;* Payee ID is not found&lt;/p&gt; &lt;p&gt;* If Payee has not been on-boarded&lt;/p&gt; &lt;p&gt;* If Payee is in grace period&lt;/p&gt; &lt;p&gt;* If Payee has existing payments&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeesApi apiInstance = new PayeesApi(defaultClient);
    UUID payeeId = UUID.fromString("2aa5d7e0-2ecb-403f-8494-1865ed0454e9"); // UUID | The UUID of the payee.
    try {
      apiInstance.deletePayeeByIdV3(payeeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeesApi#deletePayeeByIdV3");
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
| **payeeId** | **UUID**| The UUID of the payee. | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content. Payee Id accepted for deletion. |  -  |
| **400** | Bad Request. Payee Id failed validation for deletion. |  -  |
| **404** | Payee Id not found |  -  |

<a id="deletePayeeByIdV4"></a>
# **deletePayeeByIdV4**
> deletePayeeByIdV4(payeeId)

Delete Payee by Id

&lt;p&gt;This API will delete Payee by Id (UUID). Deletion by ID is not allowed if:&lt;/p&gt; &lt;p&gt;* Payee ID is not found&lt;/p&gt; &lt;p&gt;* If Payee has not been on-boarded&lt;/p&gt; &lt;p&gt;* If Payee is in grace period&lt;/p&gt; &lt;p&gt;* If Payee has existing payments&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeesApi apiInstance = new PayeesApi(defaultClient);
    UUID payeeId = UUID.fromString("2aa5d7e0-2ecb-403f-8494-1865ed0454e9"); // UUID | The UUID of the payee.
    try {
      apiInstance.deletePayeeByIdV4(payeeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeesApi#deletePayeeByIdV4");
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
| **payeeId** | **UUID**| The UUID of the payee. | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content. Payee Id accepted for deletion. |  -  |
| **400** | Bad Request. Payee Id failed validation for deletion. |  -  |
| **404** | Payee Id not found |  -  |

<a id="getPayeeByIdV3"></a>
# **getPayeeByIdV3**
> PayeeDetailResponseV3 getPayeeByIdV3(payeeId, sensitive)

Get Payee by Id

&lt;p&gt;Use v4 instead&lt;/p&gt; &lt;p&gt;Get Payee by Id&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeesApi apiInstance = new PayeesApi(defaultClient);
    UUID payeeId = UUID.fromString("2aa5d7e0-2ecb-403f-8494-1865ed0454e9"); // UUID | The UUID of the payee.
    Boolean sensitive = true; // Boolean | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
    try {
      PayeeDetailResponseV3 result = apiInstance.getPayeeByIdV3(payeeId, sensitive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeesApi#getPayeeByIdV3");
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
| **payeeId** | **UUID**| The UUID of the payee. | |
| **sensitive** | **Boolean**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional] |

### Return type

[**PayeeDetailResponseV3**](PayeeDetailResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success response, request completed okay |  -  |
| **404** | Payee Not found |  -  |

<a id="getPayeeByIdV4"></a>
# **getPayeeByIdV4**
> PayeeDetailResponseV4 getPayeeByIdV4(payeeId, sensitive)

Get Payee by Id

Get Payee by Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeesApi apiInstance = new PayeesApi(defaultClient);
    UUID payeeId = UUID.fromString("2aa5d7e0-2ecb-403f-8494-1865ed0454e9"); // UUID | The UUID of the payee.
    Boolean sensitive = true; // Boolean | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
    try {
      PayeeDetailResponseV4 result = apiInstance.getPayeeByIdV4(payeeId, sensitive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeesApi#getPayeeByIdV4");
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
| **payeeId** | **UUID**| The UUID of the payee. | |
| **sensitive** | **Boolean**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional] |

### Return type

[**PayeeDetailResponseV4**](PayeeDetailResponseV4.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success response, request completed okay |  -  |
| **404** | Payee Not found |  -  |

<a id="listPayeeChangesV3"></a>
# **listPayeeChangesV3**
> PayeeDeltaResponseV3 listPayeeChangesV3(payorId, updatedSince, page, pageSize)

List Payee Changes

&lt;p&gt;Use v4 instead&lt;/p&gt; &lt;p&gt;Get a paginated response listing payee changes.&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeesApi apiInstance = new PayeesApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The Payor ID to find associated Payees
    OffsetDateTime updatedSince = OffsetDateTime.now(); // OffsetDateTime | The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 100; // Integer | Page size. Default is 100. Max allowable is 1000.
    try {
      PayeeDeltaResponseV3 result = apiInstance.listPayeeChangesV3(payorId, updatedSince, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeesApi#listPayeeChangesV3");
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
| **payorId** | **UUID**| The Payor ID to find associated Payees | |
| **updatedSince** | **OffsetDateTime**| The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm | |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| Page size. Default is 100. Max allowable is 1000. | [optional] [default to 100] |

### Return type

[**PayeeDeltaResponseV3**](PayeeDeltaResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of Payee Changes |  -  |
| **400** | Bad Request |  -  |

<a id="listPayeeChangesV4"></a>
# **listPayeeChangesV4**
> PayeeDeltaResponseV4 listPayeeChangesV4(payorId, updatedSince, page, pageSize)

List Payee Changes

Get a paginated response listing payee changes (updated since a particular time) to a limited set of fields: - dbaName - displayName - email - onboardedStatus - payeeCountry - payeeId - remoteId 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeesApi apiInstance = new PayeesApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The Payor ID to find associated Payees
    OffsetDateTime updatedSince = OffsetDateTime.now(); // OffsetDateTime | The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 100; // Integer | Page size. Default is 100. Max allowable is 1000.
    try {
      PayeeDeltaResponseV4 result = apiInstance.listPayeeChangesV4(payorId, updatedSince, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeesApi#listPayeeChangesV4");
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
| **payorId** | **UUID**| The Payor ID to find associated Payees | |
| **updatedSince** | **OffsetDateTime**| The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm | |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| Page size. Default is 100. Max allowable is 1000. | [optional] [default to 100] |

### Return type

[**PayeeDeltaResponseV4**](PayeeDeltaResponseV4.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of Payee Changes |  -  |
| **400** | Bad Request |  -  |

<a id="listPayeesV3"></a>
# **listPayeesV3**
> PagedPayeeResponseV3 listPayeesV3(payorId, watchlistStatus, disabled, onboardedStatus, email, displayName, remoteId, payeeType, payeeCountry, page, pageSize, sort)

List Payees

&lt;p&gt;Use v4 instead&lt;/p&gt; Get a paginated response listing the payees for a payor. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeesApi apiInstance = new PayeesApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The account owner Payor ID
    String watchlistStatus = "watchlistStatus_example"; // String | The watchlistStatus of the payees.
    Boolean disabled = true; // Boolean | Payee disabled
    String onboardedStatus = "onboardedStatus_example"; // String | The onboarded status of the payees.
    String email = "bob@example.com"; // String | Email address
    String displayName = "Bob Smith"; // String | The display name of the payees.
    String remoteId = "remoteId123"; // String | The remote id of the payees.
    String payeeType = "payeeType_example"; // String | The onboarded status of the payees.
    String payeeCountry = "US"; // String | The country of the payee - 2 letter ISO 3166-1 country code (upper case)
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | Page size. Default is 25. Max allowable is 100.
    String sort = "displayName:asc"; // String | List of sort fields (e.g. ?sort=onboardedStatus:asc,name:asc) Default is name:asc 'name' is treated as company name for companies - last name + ',' + firstName for individuals The supported sort fields are - payeeId, displayName, payoutStatus, onboardedStatus. 
    try {
      PagedPayeeResponseV3 result = apiInstance.listPayeesV3(payorId, watchlistStatus, disabled, onboardedStatus, email, displayName, remoteId, payeeType, payeeCountry, page, pageSize, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeesApi#listPayeesV3");
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
| **payorId** | **UUID**| The account owner Payor ID | |
| **watchlistStatus** | **String**| The watchlistStatus of the payees. | [optional] |
| **disabled** | **Boolean**| Payee disabled | [optional] |
| **onboardedStatus** | **String**| The onboarded status of the payees. | [optional] |
| **email** | **String**| Email address | [optional] |
| **displayName** | **String**| The display name of the payees. | [optional] |
| **remoteId** | **String**| The remote id of the payees. | [optional] |
| **payeeType** | **String**| The onboarded status of the payees. | [optional] |
| **payeeCountry** | **String**| The country of the payee - 2 letter ISO 3166-1 country code (upper case) | [optional] |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25] |
| **sort** | **String**| List of sort fields (e.g. ?sort&#x3D;onboardedStatus:asc,name:asc) Default is name:asc &#39;name&#39; is treated as company name for companies - last name + &#39;,&#39; + firstName for individuals The supported sort fields are - payeeId, displayName, payoutStatus, onboardedStatus.  | [optional] [default to displayName:asc] |

### Return type

[**PagedPayeeResponseV3**](PagedPayeeResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of Payee |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="listPayeesV4"></a>
# **listPayeesV4**
> PagedPayeeResponseV4 listPayeesV4(payorId, watchlistStatus, disabled, onboardedStatus, email, displayName, remoteId, payeeType, payeeCountry, ofacStatus, page, pageSize, sort)

List Payees

Get a paginated response listing the payees for a payor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeesApi apiInstance = new PayeesApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The account owner Payor ID
    String watchlistStatus = "watchlistStatus_example"; // String | The watchlistStatus of the payees.
    Boolean disabled = true; // Boolean | Payee disabled
    String onboardedStatus = "onboardedStatus_example"; // String | The onboarded status of the payees.
    String email = "bob@example.com"; // String | Email address
    String displayName = "Bob Smith"; // String | The display name of the payees.
    String remoteId = "remoteId123"; // String | The remote id of the payees.
    String payeeType = "payeeType_example"; // String | The onboarded status of the payees.
    String payeeCountry = "US"; // String | The country of the payee - 2 letter ISO 3166-1 country code (upper case)
    String ofacStatus = "ofacStatus_example"; // String | The ofacStatus of the payees.
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | Page size. Default is 25. Max allowable is 100.
    String sort = "displayName:asc"; // String | List of sort fields (e.g. ?sort=onboardedStatus:asc,name:asc) Default is name:asc 'name' is treated as company name for companies - last name + ',' + firstName for individuals The supported sort fields are - payeeId, displayName, payoutStatus, onboardedStatus. 
    try {
      PagedPayeeResponseV4 result = apiInstance.listPayeesV4(payorId, watchlistStatus, disabled, onboardedStatus, email, displayName, remoteId, payeeType, payeeCountry, ofacStatus, page, pageSize, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeesApi#listPayeesV4");
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
| **payorId** | **UUID**| The account owner Payor ID | |
| **watchlistStatus** | **String**| The watchlistStatus of the payees. | [optional] |
| **disabled** | **Boolean**| Payee disabled | [optional] |
| **onboardedStatus** | **String**| The onboarded status of the payees. | [optional] |
| **email** | **String**| Email address | [optional] |
| **displayName** | **String**| The display name of the payees. | [optional] |
| **remoteId** | **String**| The remote id of the payees. | [optional] |
| **payeeType** | **String**| The onboarded status of the payees. | [optional] |
| **payeeCountry** | **String**| The country of the payee - 2 letter ISO 3166-1 country code (upper case) | [optional] |
| **ofacStatus** | **String**| The ofacStatus of the payees. | [optional] |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25] |
| **sort** | **String**| List of sort fields (e.g. ?sort&#x3D;onboardedStatus:asc,name:asc) Default is name:asc &#39;name&#39; is treated as company name for companies - last name + &#39;,&#39; + firstName for individuals The supported sort fields are - payeeId, displayName, payoutStatus, onboardedStatus.  | [optional] [default to displayName:asc] |

### Return type

[**PagedPayeeResponseV4**](PagedPayeeResponseV4.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of Payee |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="payeeDetailsUpdateV3"></a>
# **payeeDetailsUpdateV3**
> payeeDetailsUpdateV3(payeeId, updatePayeeDetailsRequestV3)

Update Payee Details

&lt;p&gt;Use v4 instead&lt;/p&gt; &lt;p&gt;Update payee details for the given Payee Id.&lt;p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeesApi apiInstance = new PayeesApi(defaultClient);
    UUID payeeId = UUID.fromString("2aa5d7e0-2ecb-403f-8494-1865ed0454e9"); // UUID | The UUID of the payee.
    UpdatePayeeDetailsRequestV3 updatePayeeDetailsRequestV3 = new UpdatePayeeDetailsRequestV3(); // UpdatePayeeDetailsRequestV3 | Request to update payee details
    try {
      apiInstance.payeeDetailsUpdateV3(payeeId, updatePayeeDetailsRequestV3);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeesApi#payeeDetailsUpdateV3");
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
| **payeeId** | **UUID**| The UUID of the payee. | |
| **updatePayeeDetailsRequestV3** | [**UpdatePayeeDetailsRequestV3**](UpdatePayeeDetailsRequestV3.md)| Request to update payee details | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Request accepted |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="payeeDetailsUpdateV4"></a>
# **payeeDetailsUpdateV4**
> payeeDetailsUpdateV4(payeeId, updatePayeeDetailsRequestV4)

Update Payee Details

&lt;p&gt;Update payee details for the given Payee Id.&lt;/p&gt; &lt;p&gt;Payors may only update the payee details if the payee has not yet onboarded&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeesApi apiInstance = new PayeesApi(defaultClient);
    UUID payeeId = UUID.fromString("2aa5d7e0-2ecb-403f-8494-1865ed0454e9"); // UUID | The UUID of the payee.
    UpdatePayeeDetailsRequestV4 updatePayeeDetailsRequestV4 = new UpdatePayeeDetailsRequestV4(); // UpdatePayeeDetailsRequestV4 | Request to update payee details
    try {
      apiInstance.payeeDetailsUpdateV4(payeeId, updatePayeeDetailsRequestV4);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeesApi#payeeDetailsUpdateV4");
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
| **payeeId** | **UUID**| The UUID of the payee. | |
| **updatePayeeDetailsRequestV4** | [**UpdatePayeeDetailsRequestV4**](UpdatePayeeDetailsRequestV4.md)| Request to update payee details | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Request accepted |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="v3PayeesPayeeIdRemoteIdUpdatePost"></a>
# **v3PayeesPayeeIdRemoteIdUpdatePost**
> v3PayeesPayeeIdRemoteIdUpdatePost(payeeId, updateRemoteIdRequestV3)

Update Payee Remote Id

&lt;p&gt;Use v4 instead&lt;/p&gt; &lt;p&gt;Update the remote Id for the given Payee Id.&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeesApi apiInstance = new PayeesApi(defaultClient);
    UUID payeeId = UUID.fromString("2aa5d7e0-2ecb-403f-8494-1865ed0454e9"); // UUID | The UUID of the payee.
    UpdateRemoteIdRequestV3 updateRemoteIdRequestV3 = new UpdateRemoteIdRequestV3(); // UpdateRemoteIdRequestV3 | Request to update payee remote id v3
    try {
      apiInstance.v3PayeesPayeeIdRemoteIdUpdatePost(payeeId, updateRemoteIdRequestV3);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeesApi#v3PayeesPayeeIdRemoteIdUpdatePost");
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
| **payeeId** | **UUID**| The UUID of the payee. | |
| **updateRemoteIdRequestV3** | [**UpdateRemoteIdRequestV3**](UpdateRemoteIdRequestV3.md)| Request to update payee remote id v3 | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Accepted, No Content |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |
| **409** | The request contained data that would result in a duplicate value  |  -  |

<a id="v4PayeesPayeeIdRemoteIdUpdatePost"></a>
# **v4PayeesPayeeIdRemoteIdUpdatePost**
> v4PayeesPayeeIdRemoteIdUpdatePost(payeeId, updateRemoteIdRequestV4)

Update Payee Remote Id

&lt;p&gt;Update the remote Id for the given Payee Id.&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayeesApi apiInstance = new PayeesApi(defaultClient);
    UUID payeeId = UUID.fromString("2aa5d7e0-2ecb-403f-8494-1865ed0454e9"); // UUID | The UUID of the payee.
    UpdateRemoteIdRequestV4 updateRemoteIdRequestV4 = new UpdateRemoteIdRequestV4(); // UpdateRemoteIdRequestV4 | Request to update payee remote id v4
    try {
      apiInstance.v4PayeesPayeeIdRemoteIdUpdatePost(payeeId, updateRemoteIdRequestV4);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeesApi#v4PayeesPayeeIdRemoteIdUpdatePost");
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
| **payeeId** | **UUID**| The UUID of the payee. | |
| **updateRemoteIdRequestV4** | [**UpdateRemoteIdRequestV4**](UpdateRemoteIdRequestV4.md)| Request to update payee remote id v4 | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Accepted, No Content |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |
| **409** | The request contained data that would result in a duplicate value  |  -  |

