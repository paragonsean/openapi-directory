# V2Api

All URIs are relative to *http://api.ote-godaddy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAcmeExternalAccountBinding**](V2Api.md#getAcmeExternalAccountBinding) | **GET** /v2/customers/{customerId}/certificates/acme/externalAccountBinding | Retrieves the external account binding for the specified customer |
| [**getCertificateDetailByCertIdentifier**](V2Api.md#getCertificateDetailByCertIdentifier) | **GET** /v2/customers/{customerId}/certificates/{certificateId} | Retrieve individual certificate details |
| [**getCustomerCertificatesByCustomerId**](V2Api.md#getCustomerCertificatesByCustomerId) | **GET** /v2/customers/{customerId}/certificates | Retrieve customer&#39;s certificates |
| [**getDomainDetailsByDomain**](V2Api.md#getDomainDetailsByDomain) | **GET** /v2/customers/{customerId}/certificates/{certificateId}/domainVerifications/{domain} | Retrieve detailed information for supplied domain |
| [**getDomainInformationByCertificateId**](V2Api.md#getDomainInformationByCertificateId) | **GET** /v2/customers/{customerId}/certificates/{certificateId}/domainVerifications | Retrieve domain verification status |


<a id="getAcmeExternalAccountBinding"></a>
# **getAcmeExternalAccountBinding**
> ExternalAccountBinding getAcmeExternalAccountBinding(customerId)

Retrieves the external account binding for the specified customer

Use this endpoint to retrieve a key identifier and Hash-based Message Authentication Code (HMAC) key for Automated Certificate Management Environment (ACME) External Account Binding (EAB). These credentials can be used with an ACME client that supports EAB (ex. CertBot) to automate the issuance request and deployment of DV SSL certificates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V2Api apiInstance = new V2Api(defaultClient);
    String customerId = "customerId_example"; // String | An identifier for a customer
    try {
      ExternalAccountBinding result = apiInstance.getAcmeExternalAccountBinding(customerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#getAcmeExternalAccountBinding");
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
| **customerId** | **String**| An identifier for a customer | |

### Return type

[**ExternalAccountBinding**](ExternalAccountBinding.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Acme key identifier and HMAC key for the external account binding. Directory URI is also provided for making ACME requests. |  -  |
| **401** | Authentication info not sent or is invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Resource not found |  -  |
| **422** | Application-specific request error |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |

<a id="getCertificateDetailByCertIdentifier"></a>
# **getCertificateDetailByCertIdentifier**
> CertificateDetailV2 getCertificateDetailByCertIdentifier(customerId, certificateId)

Retrieve individual certificate details

Once the certificate order has been created, this method can be used to check the status of the certificate. This method can also be used to retrieve details of the certificate. &lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**. **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V2Api apiInstance = new V2Api(defaultClient);
    String customerId = "customerId_example"; // String | An identifier for a customer
    String certificateId = "certificateId_example"; // String | Certificate id to lookup
    try {
      CertificateDetailV2 result = apiInstance.getCertificateDetailByCertIdentifier(customerId, certificateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#getCertificateDetailByCertIdentifier");
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
| **customerId** | **String**| An identifier for a customer | |
| **certificateId** | **String**| Certificate id to lookup | |

### Return type

[**CertificateDetailV2**](CertificateDetailV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Certificate details retrieved |  -  |
| **401** | Authentication info not sent or is invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Resource not found |  -  |
| **422** | Application-specific request error |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |

<a id="getCustomerCertificatesByCustomerId"></a>
# **getCustomerCertificatesByCustomerId**
> CertificateSummariesV2 getCustomerCertificatesByCustomerId(customerId, offset, limit)

Retrieve customer&#39;s certificates

This method can be used to retrieve a list of certificates for a specified customer. &lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V2Api apiInstance = new V2Api(defaultClient);
    String customerId = "customerId_example"; // String | An identifier for a customer
    Integer offset = 56; // Integer | Number of results to skip for pagination
    Integer limit = 56; // Integer | Maximum number of items to return
    try {
      CertificateSummariesV2 result = apiInstance.getCustomerCertificatesByCustomerId(customerId, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#getCustomerCertificatesByCustomerId");
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
| **customerId** | **String**| An identifier for a customer | |
| **offset** | **Integer**| Number of results to skip for pagination | [optional] |
| **limit** | **Integer**| Maximum number of items to return | [optional] |

### Return type

[**CertificateSummariesV2**](CertificateSummariesV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Customer certificate information retrieved. |  -  |
| **401** | Authentication info not sent or is invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **422** | Application-specific request error |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |

<a id="getDomainDetailsByDomain"></a>
# **getDomainDetailsByDomain**
> DomainVerificationDetail getDomainDetailsByDomain(customerId, certificateId, domain)

Retrieve detailed information for supplied domain

Retrieve detailed information for supplied domain, including domain verification details and Certificate Authority Authorization (CAA) verification details. &lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V2Api apiInstance = new V2Api(defaultClient);
    String customerId = "customerId_example"; // String | An identifier for a customer
    String certificateId = "certificateId_example"; // String | Certificate id to lookup
    String domain = "domain_example"; // String | A valid domain name in the certificate request
    try {
      DomainVerificationDetail result = apiInstance.getDomainDetailsByDomain(customerId, certificateId, domain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#getDomainDetailsByDomain");
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
| **customerId** | **String**| An identifier for a customer | |
| **certificateId** | **String**| Certificate id to lookup | |
| **domain** | **String**| A valid domain name in the certificate request | |

### Return type

[**DomainVerificationDetail**](DomainVerificationDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve detailed information for supplied domain, including domain verification details and Certificate Authority Authorization (CAA) verification details. |  -  |
| **401** | Authentication info not sent or is invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Resource not found |  -  |
| **422** | Application-specific request error |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |

<a id="getDomainInformationByCertificateId"></a>
# **getDomainInformationByCertificateId**
> List&lt;DomainVerificationSummary&gt; getDomainInformationByCertificateId(customerId, certificateId)

Retrieve domain verification status

This method can be used to retrieve the domain verification status for a certificate request.&lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V2Api apiInstance = new V2Api(defaultClient);
    String customerId = "customerId_example"; // String | An identifier for a customer
    String certificateId = "certificateId_example"; // String | Certificate id to lookup
    try {
      List<DomainVerificationSummary> result = apiInstance.getDomainInformationByCertificateId(customerId, certificateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V2Api#getDomainInformationByCertificateId");
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
| **customerId** | **String**| An identifier for a customer | |
| **certificateId** | **String**| Certificate id to lookup | |

### Return type

[**List&lt;DomainVerificationSummary&gt;**](DomainVerificationSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Domain verification status list for specified certificateId. |  -  |
| **401** | Authentication info not sent or is invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Resource not found |  -  |
| **422** | Application-specific request error |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |

