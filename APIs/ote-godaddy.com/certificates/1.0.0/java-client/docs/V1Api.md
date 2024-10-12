# V1Api

All URIs are relative to *http://api.ote-godaddy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**certificateActionRetrieve**](V1Api.md#certificateActionRetrieve) | **GET** /v1/certificates/{certificateId}/actions | Retrieve all certificate actions |
| [**certificateAlternateEmailAddress**](V1Api.md#certificateAlternateEmailAddress) | **POST** /v1/certificates/{certificateId}/email/resend/{emailAddress} | Add alternate email address |
| [**certificateCallbackDelete**](V1Api.md#certificateCallbackDelete) | **DELETE** /v1/certificates/{certificateId}/callback | Unregister system callback |
| [**certificateCallbackGet**](V1Api.md#certificateCallbackGet) | **GET** /v1/certificates/{certificateId}/callback | Retrieve system stateful action callback url |
| [**certificateCallbackReplace**](V1Api.md#certificateCallbackReplace) | **PUT** /v1/certificates/{certificateId}/callback | Register of certificate action callback |
| [**certificateCancel**](V1Api.md#certificateCancel) | **POST** /v1/certificates/{certificateId}/cancel | Cancel a pending certificate |
| [**certificateCreate**](V1Api.md#certificateCreate) | **POST** /v1/certificates | Create a pending order for certificate |
| [**certificateDownload**](V1Api.md#certificateDownload) | **GET** /v1/certificates/{certificateId}/download | Download certificate |
| [**certificateDownloadEntitlement**](V1Api.md#certificateDownloadEntitlement) | **GET** /v2/certificates/download | Download certificate by entitlement |
| [**certificateEmailHistory**](V1Api.md#certificateEmailHistory) | **GET** /v1/certificates/{certificateId}/email/history | Retrieve email history |
| [**certificateGet**](V1Api.md#certificateGet) | **GET** /v1/certificates/{certificateId} | Retrieve certificate details |
| [**certificateGetEntitlement**](V1Api.md#certificateGetEntitlement) | **GET** /v2/certificates | Search for certificate details by entitlement |
| [**certificateReissue**](V1Api.md#certificateReissue) | **POST** /v1/certificates/{certificateId}/reissue | Reissue active certificate |
| [**certificateRenew**](V1Api.md#certificateRenew) | **POST** /v1/certificates/{certificateId}/renew | Renew active certificate |
| [**certificateResendEmail**](V1Api.md#certificateResendEmail) | **POST** /v1/certificates/{certificateId}/email/{emailId}/resend | Resend an email |
| [**certificateResendEmailAddress**](V1Api.md#certificateResendEmailAddress) | **POST** /v1/certificates/{certificateId}/email/{emailId}/resend/{emailAddress} | Resend email to email address |
| [**certificateRevoke**](V1Api.md#certificateRevoke) | **POST** /v1/certificates/{certificateId}/revoke | Revoke active certificate |
| [**certificateSitesealGet**](V1Api.md#certificateSitesealGet) | **GET** /v1/certificates/{certificateId}/siteSeal | Get Site seal |
| [**certificateValidate**](V1Api.md#certificateValidate) | **POST** /v1/certificates/validate | Validate a pending order for certificate |
| [**certificateVerifydomaincontrol**](V1Api.md#certificateVerifydomaincontrol) | **POST** /v1/certificates/{certificateId}/verifyDomainControl | Check Domain Control |


<a id="certificateActionRetrieve"></a>
# **certificateActionRetrieve**
> List&lt;CertificateAction&gt; certificateActionRetrieve(certificateId)

Retrieve all certificate actions

This method is used to retrieve all stateful actions relating to a certificate lifecycle.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String certificateId = "certificateId_example"; // String | Certificate id to register for callback
    try {
      List<CertificateAction> result = apiInstance.certificateActionRetrieve(certificateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateActionRetrieve");
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
| **certificateId** | **String**| Certificate id to register for callback | |

### Return type

[**List&lt;CertificateAction&gt;**](CertificateAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Action retrieval successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Certificate not found |  -  |
| **500** | Internal server error |  -  |

<a id="certificateAlternateEmailAddress"></a>
# **certificateAlternateEmailAddress**
> CertificateEmailHistory certificateAlternateEmailAddress(certificateId, emailAddress)

Add alternate email address

This method adds an alternate email address to a certificate order and re-sends all existing request emails to that address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String certificateId = "certificateId_example"; // String | Certificate id to resend emails
    String emailAddress = "emailAddress_example"; // String | Specific email address to resend email
    try {
      CertificateEmailHistory result = apiInstance.certificateAlternateEmailAddress(certificateId, emailAddress);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateAlternateEmailAddress");
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
| **certificateId** | **String**| Certificate id to resend emails | |
| **emailAddress** | **String**| Specific email address to resend email | |

### Return type

[**CertificateEmailHistory**](CertificateEmailHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Alternate email address added and emails re-sent |  -  |
| **404** | Certificate not found |  -  |
| **409** | Certificate state does not allow alternate email address |  -  |
| **500** | Internal server error |  -  |

<a id="certificateCallbackDelete"></a>
# **certificateCallbackDelete**
> certificateCallbackDelete(certificateId)

Unregister system callback

Unregister the callback for a particular certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String certificateId = "certificateId_example"; // String | Certificate id to unregister callback
    try {
      apiInstance.certificateCallbackDelete(certificateId);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateCallbackDelete");
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
| **certificateId** | **String**| Certificate id to unregister callback | |

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
| **204** | Callback removed |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Certificate id not found |  -  |
| **500** | Internal server error |  -  |

<a id="certificateCallbackGet"></a>
# **certificateCallbackGet**
> CertificateCallback certificateCallbackGet(certificateId)

Retrieve system stateful action callback url

This method is used to retrieve the registered callback url for a certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String certificateId = "certificateId_example"; // String | Certificate id to register for stateful action callback
    try {
      CertificateCallback result = apiInstance.certificateCallbackGet(certificateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateCallbackGet");
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
| **certificateId** | **String**| Certificate id to register for stateful action callback | |

### Return type

[**CertificateCallback**](CertificateCallback.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Callback registered |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Certificate id not found |  -  |
| **500** | Internal server error |  -  |

<a id="certificateCallbackReplace"></a>
# **certificateCallbackReplace**
> certificateCallbackReplace(certificateId, callbackUrl)

Register of certificate action callback

This method is used to register/replace url for callbacks for stateful actions relating to a certificate lifecycle. The callback url is a Webhook style pattern and will receive POST http requests with json body defined in the CertificateAction model definition for each certificate action.  Only one callback URL is allowed to be registered for each certificateId, so it will replace a previous registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String certificateId = "certificateId_example"; // String | Certificate id to register/replace for callback
    String callbackUrl = "callbackUrl_example"; // String | Callback url registered/replaced to receive stateful actions
    try {
      apiInstance.certificateCallbackReplace(certificateId, callbackUrl);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateCallbackReplace");
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
| **certificateId** | **String**| Certificate id to register/replace for callback | |
| **callbackUrl** | **String**| Callback url registered/replaced to receive stateful actions | |

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
| **204** | Callback replaced/registered |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Certificate id not found |  -  |
| **422** | Callback url is missing &lt;br&gt; Callback url is malformed |  -  |
| **500** | Internal server error |  -  |

<a id="certificateCancel"></a>
# **certificateCancel**
> certificateCancel(certificateId)

Cancel a pending certificate

Use the cancel call to cancel a pending certificate order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String certificateId = "certificateId_example"; // String | Certificate id to cancel
    try {
      apiInstance.certificateCancel(certificateId);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateCancel");
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
| **certificateId** | **String**| Certificate id to cancel | |

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
| **204** | Certificate order has been canceled |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Certificate id not found |  -  |
| **409** | Certificate state does not allow cancel |  -  |
| **500** | Internal server error |  -  |

<a id="certificateCreate"></a>
# **certificateCreate**
> CertificateIdentifier certificateCreate(certificateCreate, xMarketId)

Create a pending order for certificate

&lt;p&gt;Creating a certificate order can be a long running asynchronous operation in the PKI workflow. The PKI API supports 2 options for getting the completion stateful actions for this asynchronous operations: 1) by polling operations -- see /v1/certificates/{certificateId}/actions 2) via WebHook style callback -- see &#39;/v1/certificates/{certificateId}/callback&#39;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    CertificateCreate certificateCreate = new CertificateCreate(); // CertificateCreate | The certificate order information
    String xMarketId = "Default locale for shopper account"; // String | Setting locale for communications such as emails and error messages
    try {
      CertificateIdentifier result = apiInstance.certificateCreate(certificateCreate, xMarketId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateCreate");
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
| **certificateCreate** | [**CertificateCreate**](CertificateCreate.md)| The certificate order information | |
| **xMarketId** | **String**| Setting locale for communications such as emails and error messages | [optional] [default to Default locale for shopper account] |

### Return type

[**CertificateIdentifier**](CertificateIdentifier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Request was successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **409** | Certificate state does not allow renew |  -  |
| **422** | &#x60;email&#x60; is not empty&lt;br&gt;&#x60;csr&#x60; is invalid |  -  |
| **500** | Internal server error |  -  |

<a id="certificateDownload"></a>
# **certificateDownload**
> CertificateBundle certificateDownload(certificateId)

Download certificate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String certificateId = "certificateId_example"; // String | Certificate id to download
    try {
      CertificateBundle result = apiInstance.certificateDownload(certificateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateDownload");
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
| **certificateId** | **String**| Certificate id to download | |

### Return type

[**CertificateBundle**](CertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Certificate retrieved |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Certificate id not found |  -  |
| **409** | Certificate state does not allow download |  -  |
| **500** | Internal server error |  -  |

<a id="certificateDownloadEntitlement"></a>
# **certificateDownloadEntitlement**
> CertificateBundle certificateDownloadEntitlement(entitlementId)

Download certificate by entitlement

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String entitlementId = "entitlementId_example"; // String | Entitlement id to download
    try {
      CertificateBundle result = apiInstance.certificateDownloadEntitlement(entitlementId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateDownloadEntitlement");
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
| **entitlementId** | **String**| Entitlement id to download | |

### Return type

[**CertificateBundle**](CertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Certificate retrieved |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Entitlement id not found |  -  |
| **409** | Certificate state does not allow download |  -  |
| **422** | Entitlement id not provided |  -  |
| **500** | Internal server error |  -  |

<a id="certificateEmailHistory"></a>
# **certificateEmailHistory**
> CertificateEmailHistory certificateEmailHistory(certificateId)

Retrieve email history

This method can be used to retrieve all emails sent for a certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String certificateId = "certificateId_example"; // String | Certificate id to retrieve email history
    try {
      CertificateEmailHistory result = apiInstance.certificateEmailHistory(certificateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateEmailHistory");
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
| **certificateId** | **String**| Certificate id to retrieve email history | |

### Return type

[**CertificateEmailHistory**](CertificateEmailHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Email history retrieval successful |  -  |
| **409** | Email history not found |  -  |
| **500** | Internal server error |  -  |

<a id="certificateGet"></a>
# **certificateGet**
> Certificate certificateGet(certificateId)

Retrieve certificate details

Once the certificate order has been created, this method can be used to check the status of the certificate. This method can also be used to retrieve details of the certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String certificateId = "certificateId_example"; // String | Certificate id to lookup
    try {
      Certificate result = apiInstance.certificateGet(certificateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateGet");
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
| **certificateId** | **String**| Certificate id to lookup | |

### Return type

[**Certificate**](Certificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Certificate details retrieved |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Certificate id not found |  -  |
| **500** | Internal server error |  -  |

<a id="certificateGetEntitlement"></a>
# **certificateGetEntitlement**
> List&lt;Certificate&gt; certificateGetEntitlement(entitlementId, latest)

Search for certificate details by entitlement

Once the certificate order has been created, this method can be used to check the status of the certificate. This method can also be used to retrieve details of the certificates associated to an entitlement.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String entitlementId = "entitlementId_example"; // String | Entitlement id to lookup
    Boolean latest = true; // Boolean | Fetch only the most recent certificate
    try {
      List<Certificate> result = apiInstance.certificateGetEntitlement(entitlementId, latest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateGetEntitlement");
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
| **entitlementId** | **String**| Entitlement id to lookup | |
| **latest** | **Boolean**| Fetch only the most recent certificate | [optional] [default to true] |

### Return type

[**List&lt;Certificate&gt;**](Certificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Certificate details retrieved |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **422** | Entitlement id not provided |  -  |
| **500** | Internal server error |  -  |

<a id="certificateReissue"></a>
# **certificateReissue**
> certificateReissue(certificateId, certificateReissue)

Reissue active certificate

&lt;p&gt;Rekeying is the process by which the private and public key is changed for a certificate. It is a simplified reissue,where only the CSR is changed. Reissuing is the process by which domain names are added or removed from a certificate.Once a request is validated and approved, the certificate will be reissued with the new common name and sans specified. Unlimited reissues are available during the lifetime of the certificate.New names added to a certificate that do not share the base domain of the common name may take additional time to validate. If this API call is made before a previous pending reissue has been validated and issued, the previous reissue request is automatically rejected and replaced with the current request.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String certificateId = "certificateId_example"; // String | Certificate id to reissue
    CertificateReissue certificateReissue = new CertificateReissue(); // CertificateReissue | The reissue request info
    try {
      apiInstance.certificateReissue(certificateId, certificateReissue);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateReissue");
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
| **certificateId** | **String**| Certificate id to reissue | |
| **certificateReissue** | [**CertificateReissue**](CertificateReissue.md)| The reissue request info | |

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
| **202** | Reissue request created |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Certificate id not found |  -  |
| **409** | Certificate state does not allow reissue |  -  |
| **422** | &#x60;csr&#x60; is invalid&lt;br&gt;Delay revocation exceeds maximum |  -  |
| **500** | Internal server error |  -  |

<a id="certificateRenew"></a>
# **certificateRenew**
> certificateRenew(certificateId, certificateRenew)

Renew active certificate

Renewal is the process by which the validity of a certificate is extended. Renewal is only available 60 days prior to expiration of the previous certificate and 30 days after the expiration of the previous certificate. The renewal supports modifying a set of the original certificate order information. Once a request is validated and approved, the certificate will be issued with extended validity. Since subject alternative names can be removed during a renewal, we require that you provide the subject alternative names you expect in the renewed certificate. New names added to a certificate that do not share the base domain of the common name may take additional time to validate. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String certificateId = "certificateId_example"; // String | Certificate id to renew
    CertificateRenew certificateRenew = new CertificateRenew(); // CertificateRenew | The renew request info
    try {
      apiInstance.certificateRenew(certificateId, certificateRenew);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateRenew");
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
| **certificateId** | **String**| Certificate id to renew | |
| **certificateRenew** | [**CertificateRenew**](CertificateRenew.md)| The renew request info | |

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
| **202** | Renew request created |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Certificate id not found |  -  |
| **409** | Certificate state does not allow renew |  -  |
| **422** | &#x60;csr&#x60; is invalid |  -  |
| **500** | Internal server error |  -  |

<a id="certificateResendEmail"></a>
# **certificateResendEmail**
> certificateResendEmail(certificateId, emailId)

Resend an email

This method can be used to resend emails by providing the certificate id and the email id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String certificateId = "certificateId_example"; // String | Certificate id to resend email
    String emailId = "emailId_example"; // String | Email id for email to resend
    try {
      apiInstance.certificateResendEmail(certificateId, emailId);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateResendEmail");
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
| **certificateId** | **String**| Certificate id to resend email | |
| **emailId** | **String**| Email id for email to resend | |

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
| **204** | Email sent successfully |  -  |
| **404** | Certificate not found |  -  |
| **409** | Email Id not found |  -  |
| **500** | Internal server error |  -  |

<a id="certificateResendEmailAddress"></a>
# **certificateResendEmailAddress**
> certificateResendEmailAddress(certificateId, emailId, emailAddress)

Resend email to email address

This method can be used to resend emails by providing the certificate id, the email id, and the recipient email address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String certificateId = "certificateId_example"; // String | Certificate id to resend emails
    String emailId = "emailId_example"; // String | Email id for email to resend
    String emailAddress = "emailAddress_example"; // String | Specific email address to resend email
    try {
      apiInstance.certificateResendEmailAddress(certificateId, emailId, emailAddress);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateResendEmailAddress");
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
| **certificateId** | **String**| Certificate id to resend emails | |
| **emailId** | **String**| Email id for email to resend | |
| **emailAddress** | **String**| Specific email address to resend email | |

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
| **204** | Email sent successfully |  -  |
| **404** | Certificate not found |  -  |
| **409** | Email Id not found |  -  |
| **500** | Internal server error |  -  |

<a id="certificateRevoke"></a>
# **certificateRevoke**
> certificateRevoke(certificateId, certificateRevoke)

Revoke active certificate

Use revoke call to revoke an active certificate, if the certificate has not been issued a 404 response will be returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String certificateId = "certificateId_example"; // String | Certificate id to revoke
    CertificateRevoke certificateRevoke = new CertificateRevoke(); // CertificateRevoke | The certificate revocation request
    try {
      apiInstance.certificateRevoke(certificateId, certificateRevoke);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateRevoke");
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
| **certificateId** | **String**| Certificate id to revoke | |
| **certificateRevoke** | [**CertificateRevoke**](CertificateRevoke.md)| The certificate revocation request | |

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
| **204** | Certificate Revoked |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Certificate id not found |  -  |
| **409** | Certificate state does not allow revoke |  -  |
| **500** | Internal server error |  -  |

<a id="certificateSitesealGet"></a>
# **certificateSitesealGet**
> CertificateSiteSeal certificateSitesealGet(certificateId, theme, locale)

Get Site seal

&lt;p&gt;This method is used to obtain the site seal information for an issued certificate. A site seal is a graphic that the certificate purchaser can embed on their web site to show their visitors information about their SSL certificate. If a web site visitor clicks on the site seal image, a pop-up page is displayed that contains detailed information about the SSL certificate. The site seal token is used to link the site seal graphic image to the appropriate certificate details pop-up page display when a user clicks on the site seal. The site seal images are expected to be static images and hosted on the reseller&#39;s website, to minimize delays for customer page load times.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String certificateId = "certificateId_example"; // String | Certificate id
    String theme = "DARK"; // String | This value represents the visual theme of the seal. If seal doesn't exist, default values are used if params not present. If seal does exist, default values will not be used to update unless params present.
    String locale = "en"; // String | Determine locale for text displayed in seal image and verification page. If seal doesn't exist, default values are used if params not present. If seal does exist, default values will not be used to update unless params present.
    try {
      CertificateSiteSeal result = apiInstance.certificateSitesealGet(certificateId, theme, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateSitesealGet");
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
| **certificateId** | **String**| Certificate id | |
| **theme** | **String**| This value represents the visual theme of the seal. If seal doesn&#39;t exist, default values are used if params not present. If seal does exist, default values will not be used to update unless params present. | [optional] [default to LIGHT] [enum: DARK, LIGHT] |
| **locale** | **String**| Determine locale for text displayed in seal image and verification page. If seal doesn&#39;t exist, default values are used if params not present. If seal does exist, default values will not be used to update unless params present. | [optional] [default to en] |

### Return type

[**CertificateSiteSeal**](CertificateSiteSeal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Site seal retrieved |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Certificate id not found |  -  |
| **409** | Certificate state does not allow seal |  -  |
| **422** | &#39;locale&#39; is invalid |  -  |
| **500** | Internal server error |  -  |

<a id="certificateValidate"></a>
# **certificateValidate**
> certificateValidate(certificateCreate, xMarketId)

Validate a pending order for certificate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    CertificateCreate certificateCreate = new CertificateCreate(); // CertificateCreate | The certificate order info
    String xMarketId = "Default locale for shopper account"; // String | Setting locale for communications such as emails and error messages
    try {
      apiInstance.certificateValidate(certificateCreate, xMarketId);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateValidate");
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
| **certificateCreate** | [**CertificateCreate**](CertificateCreate.md)| The certificate order info | |
| **xMarketId** | **String**| Setting locale for communications such as emails and error messages | [optional] [default to Default locale for shopper account] |

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
| **204** | Request validated successfully |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **409** | Certificate state does not allow renew |  -  |
| **422** | &#x60;email&#x60; is not empty &lt;br&gt; &#x60;csr&#x60; is invalid |  -  |
| **500** | Internal server error |  -  |

<a id="certificateVerifydomaincontrol"></a>
# **certificateVerifydomaincontrol**
> certificateVerifydomaincontrol(certificateId)

Check Domain Control

Domain control is a means for verifying the domain included in the certificate order. This resource is useful for resellers that control the domains for their customers, and can expedite the verification process. See https://www.godaddy.com/help/verifying-your-domain-ownership-for-ssl-certificate-requests-html-or-dns-7452

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String certificateId = "certificateId_example"; // String | Certificate id to lookup
    try {
      apiInstance.certificateVerifydomaincontrol(certificateId);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#certificateVerifydomaincontrol");
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
| **certificateId** | **String**| Certificate id to lookup | |

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
| **204** | Domain control was successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Certificate id not found |  -  |
| **409** | Domain control was not successful &lt;br&gt; Certificate state does not allow domain control |  -  |
| **500** | Internal server error |  -  |

