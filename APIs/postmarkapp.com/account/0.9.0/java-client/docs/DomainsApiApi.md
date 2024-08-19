# DomainsApiApi

All URIs are relative to *http://api.postmarkapp.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDomain**](DomainsApiApi.md#createDomain) | **POST** /domains | Create a Domain |
| [**deleteDomain**](DomainsApiApi.md#deleteDomain) | **DELETE** /domains/{domainid} | Delete a Domain |
| [**editDomain**](DomainsApiApi.md#editDomain) | **PUT** /domains/{domainid} | Update a Domain |
| [**getDomain**](DomainsApiApi.md#getDomain) | **GET** /domains/{domainid} | Get a Domain |
| [**listDomains**](DomainsApiApi.md#listDomains) | **GET** /domains | List Domains |
| [**requestDkimVerificationForDomain**](DomainsApiApi.md#requestDkimVerificationForDomain) | **PUT** /domains/{domainid}/verifydkim | Request DNS Verification for DKIM |
| [**requestReturnPathVerificationForDomain**](DomainsApiApi.md#requestReturnPathVerificationForDomain) | **PUT** /domains/{domainid}/verifyreturnpath | Request DNS Verification for Return-Path |
| [**requestSPFVerificationForDomain**](DomainsApiApi.md#requestSPFVerificationForDomain) | **POST** /domains/{domainid}/verifyspf | Request DNS Verification for SPF |
| [**rotateDKIMKeyForDomain**](DomainsApiApi.md#rotateDKIMKeyForDomain) | **POST** /domains/{domainid}/rotatedkim | Rotate DKIM Key |


<a id="createDomain"></a>
# **createDomain**
> DomainExtendedInformation createDomain(xPostmarkAccountToken, body)

Create a Domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    DomainsApiApi apiInstance = new DomainsApiApi(defaultClient);
    String xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
    DomainCreationModel body = new DomainCreationModel(); // DomainCreationModel | 
    try {
      DomainExtendedInformation result = apiInstance.createDomain(xPostmarkAccountToken, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApiApi#createDomain");
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
| **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | |
| **body** | [**DomainCreationModel**](DomainCreationModel.md)|  | [optional] |

### Return type

[**DomainExtendedInformation**](DomainExtendedInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="deleteDomain"></a>
# **deleteDomain**
> StandardPostmarkResponse deleteDomain(xPostmarkAccountToken, domainid)

Delete a Domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    DomainsApiApi apiInstance = new DomainsApiApi(defaultClient);
    String xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
    Integer domainid = 56; // Integer | The ID for the Domain that should be deleted by the request.
    try {
      StandardPostmarkResponse result = apiInstance.deleteDomain(xPostmarkAccountToken, domainid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApiApi#deleteDomain");
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
| **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | |
| **domainid** | **Integer**| The ID for the Domain that should be deleted by the request. | |

### Return type

[**StandardPostmarkResponse**](StandardPostmarkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="editDomain"></a>
# **editDomain**
> DomainExtendedInformation editDomain(xPostmarkAccountToken, domainid, body)

Update a Domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    DomainsApiApi apiInstance = new DomainsApiApi(defaultClient);
    String xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
    Integer domainid = 56; // Integer | The ID for the Domain that should be modified by the request.
    DomainEditingModel body = new DomainEditingModel(); // DomainEditingModel | 
    try {
      DomainExtendedInformation result = apiInstance.editDomain(xPostmarkAccountToken, domainid, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApiApi#editDomain");
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
| **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | |
| **domainid** | **Integer**| The ID for the Domain that should be modified by the request. | |
| **body** | [**DomainEditingModel**](DomainEditingModel.md)|  | [optional] |

### Return type

[**DomainExtendedInformation**](DomainExtendedInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getDomain"></a>
# **getDomain**
> DomainExtendedInformation getDomain(xPostmarkAccountToken, domainid)

Get a Domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    DomainsApiApi apiInstance = new DomainsApiApi(defaultClient);
    String xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
    Integer domainid = 56; // Integer | The ID for the Domain that should be retrieved.
    try {
      DomainExtendedInformation result = apiInstance.getDomain(xPostmarkAccountToken, domainid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApiApi#getDomain");
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
| **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | |
| **domainid** | **Integer**| The ID for the Domain that should be retrieved. | |

### Return type

[**DomainExtendedInformation**](DomainExtendedInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="listDomains"></a>
# **listDomains**
> DomainListingResults listDomains(xPostmarkAccountToken, count, offset)

List Domains

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    DomainsApiApi apiInstance = new DomainsApiApi(defaultClient);
    String xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
    Integer count = 56; // Integer | Number of records to return per request. Max 500.
    Integer offset = 56; // Integer | Number of records to skip
    try {
      DomainListingResults result = apiInstance.listDomains(xPostmarkAccountToken, count, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApiApi#listDomains");
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
| **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | |
| **count** | **Integer**| Number of records to return per request. Max 500. | |
| **offset** | **Integer**| Number of records to skip | |

### Return type

[**DomainListingResults**](DomainListingResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="requestDkimVerificationForDomain"></a>
# **requestDkimVerificationForDomain**
> DomainExtendedInformation requestDkimVerificationForDomain(xPostmarkAccountToken, domainid)

Request DNS Verification for DKIM

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    DomainsApiApi apiInstance = new DomainsApiApi(defaultClient);
    String xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
    Integer domainid = 56; // Integer | The ID for the Domain for which DKIM DNS records should be verified.
    try {
      DomainExtendedInformation result = apiInstance.requestDkimVerificationForDomain(xPostmarkAccountToken, domainid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApiApi#requestDkimVerificationForDomain");
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
| **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | |
| **domainid** | **Integer**| The ID for the Domain for which DKIM DNS records should be verified. | |

### Return type

[**DomainExtendedInformation**](DomainExtendedInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="requestReturnPathVerificationForDomain"></a>
# **requestReturnPathVerificationForDomain**
> DomainExtendedInformation requestReturnPathVerificationForDomain(xPostmarkAccountToken, domainid)

Request DNS Verification for Return-Path

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    DomainsApiApi apiInstance = new DomainsApiApi(defaultClient);
    String xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
    Integer domainid = 56; // Integer | The ID for the Domain for which Return-Path DNS records should be verified.
    try {
      DomainExtendedInformation result = apiInstance.requestReturnPathVerificationForDomain(xPostmarkAccountToken, domainid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApiApi#requestReturnPathVerificationForDomain");
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
| **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | |
| **domainid** | **Integer**| The ID for the Domain for which Return-Path DNS records should be verified. | |

### Return type

[**DomainExtendedInformation**](DomainExtendedInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="requestSPFVerificationForDomain"></a>
# **requestSPFVerificationForDomain**
> DomainSPFResult requestSPFVerificationForDomain(xPostmarkAccountToken, domainid)

Request DNS Verification for SPF

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    DomainsApiApi apiInstance = new DomainsApiApi(defaultClient);
    String xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
    Integer domainid = 56; // Integer | The ID for the Domain for which SPF DNS records should be verified.
    try {
      DomainSPFResult result = apiInstance.requestSPFVerificationForDomain(xPostmarkAccountToken, domainid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApiApi#requestSPFVerificationForDomain");
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
| **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | |
| **domainid** | **Integer**| The ID for the Domain for which SPF DNS records should be verified. | |

### Return type

[**DomainSPFResult**](DomainSPFResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="rotateDKIMKeyForDomain"></a>
# **rotateDKIMKeyForDomain**
> DKIMRotationResponse rotateDKIMKeyForDomain(xPostmarkAccountToken, domainid)

Rotate DKIM Key

Creates a new DKIM key to replace your current key. Until the DNS entries are confirmed, the new values will be in the &#x60;DKIMPendingHost&#x60; and &#x60;DKIMPendingTextValue&#x60; fields. After the new DKIM value is verified in DNS, the pending values will migrate to &#x60;DKIMTextValue&#x60; and &#x60;DKIMPendingTextValue&#x60; and Postmark will begin to sign emails with the new DKIM key. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    DomainsApiApi apiInstance = new DomainsApiApi(defaultClient);
    String xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
    Integer domainid = 56; // Integer | The ID for the Sender Signature for which a new DKIM Key should be generated.
    try {
      DKIMRotationResponse result = apiInstance.rotateDKIMKeyForDomain(xPostmarkAccountToken, domainid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApiApi#rotateDKIMKeyForDomain");
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
| **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | |
| **domainid** | **Integer**| The ID for the Sender Signature for which a new DKIM Key should be generated. | |

### Return type

[**DKIMRotationResponse**](DKIMRotationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

