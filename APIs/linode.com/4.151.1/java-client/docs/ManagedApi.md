# ManagedApi

All URIs are relative to *https://api.linode.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createManagedContact**](ManagedApi.md#createManagedContact) | **POST** /managed/contacts | Managed Contact Create |
| [**createManagedCredential**](ManagedApi.md#createManagedCredential) | **POST** /managed/credentials | Managed Credential Create |
| [**createManagedService**](ManagedApi.md#createManagedService) | **POST** /managed/services | Managed Service Create |
| [**deleteManagedContact**](ManagedApi.md#deleteManagedContact) | **DELETE** /managed/contacts/{contactId} | Managed Contact Delete |
| [**deleteManagedCredential**](ManagedApi.md#deleteManagedCredential) | **POST** /managed/credentials/{credentialId}/revoke | Managed Credential Delete |
| [**deleteManagedService**](ManagedApi.md#deleteManagedService) | **DELETE** /managed/services/{serviceId} | Managed Service Delete |
| [**disableManagedService**](ManagedApi.md#disableManagedService) | **POST** /managed/services/{serviceId}/disable | Managed Service Disable |
| [**enableManagedService**](ManagedApi.md#enableManagedService) | **POST** /managed/services/{serviceId}/enable | Managed Service Enable |
| [**getManagedContact**](ManagedApi.md#getManagedContact) | **GET** /managed/contacts/{contactId} | Managed Contact View |
| [**getManagedContacts**](ManagedApi.md#getManagedContacts) | **GET** /managed/contacts | Managed Contacts List |
| [**getManagedCredential**](ManagedApi.md#getManagedCredential) | **GET** /managed/credentials/{credentialId} | Managed Credential View |
| [**getManagedCredentials**](ManagedApi.md#getManagedCredentials) | **GET** /managed/credentials | Managed Credentials List |
| [**getManagedIssue**](ManagedApi.md#getManagedIssue) | **GET** /managed/issues/{issueId} | Managed Issue View |
| [**getManagedIssues**](ManagedApi.md#getManagedIssues) | **GET** /managed/issues | Managed Issues List |
| [**getManagedLinodeSetting**](ManagedApi.md#getManagedLinodeSetting) | **GET** /managed/linode-settings/{linodeId} | Linode&#39;s Managed Settings View |
| [**getManagedLinodeSettings**](ManagedApi.md#getManagedLinodeSettings) | **GET** /managed/linode-settings | Managed Linode Settings List |
| [**getManagedService**](ManagedApi.md#getManagedService) | **GET** /managed/services/{serviceId} | Managed Service View |
| [**getManagedServices**](ManagedApi.md#getManagedServices) | **GET** /managed/services | Managed Services List |
| [**getManagedStats**](ManagedApi.md#getManagedStats) | **GET** /managed/stats | Managed Stats List |
| [**updateManagedContact**](ManagedApi.md#updateManagedContact) | **PUT** /managed/contacts/{contactId} | Managed Contact Update |
| [**updateManagedCredential**](ManagedApi.md#updateManagedCredential) | **PUT** /managed/credentials/{credentialId} | Managed Credential Update |
| [**updateManagedCredentialUsernamePassword**](ManagedApi.md#updateManagedCredentialUsernamePassword) | **POST** /managed/credentials/{credentialId}/update | Managed Credential Username and Password Update |
| [**updateManagedLinodeSetting**](ManagedApi.md#updateManagedLinodeSetting) | **PUT** /managed/linode-settings/{linodeId} | Linode&#39;s Managed Settings Update |
| [**updateManagedService**](ManagedApi.md#updateManagedService) | **PUT** /managed/services/{serviceId} | Managed Service Update |
| [**viewManagedSSHKey**](ManagedApi.md#viewManagedSSHKey) | **GET** /managed/credentials/sshkey | Managed SSH Key View |


<a id="createManagedContact"></a>
# **createManagedContact**
> ManagedContact createManagedContact(managedContact)

Managed Contact Create

Creates a Managed Contact.  A Managed Contact is someone Linode special forces can contact in the course of attempting to resolve an issue with a Managed Service.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    ManagedContact managedContact = new ManagedContact(); // ManagedContact | Information about the contact to create.
    try {
      ManagedContact result = apiInstance.createManagedContact(managedContact);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#createManagedContact");
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
| **managedContact** | [**ManagedContact**](ManagedContact.md)| Information about the contact to create. | [optional] |

### Return type

[**ManagedContact**](ManagedContact.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contact created. |  -  |
| **0** | Error |  -  |

<a id="createManagedCredential"></a>
# **createManagedCredential**
> ManagedCredential createManagedCredential(createManagedCredentialRequest)

Managed Credential Create

Creates a Managed Credential. A Managed Credential is stored securely to allow Linode special forces to access your Managed Services and resolve issues.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    CreateManagedCredentialRequest createManagedCredentialRequest = new CreateManagedCredentialRequest(); // CreateManagedCredentialRequest | Information about the Credential to create.
    try {
      ManagedCredential result = apiInstance.createManagedCredential(createManagedCredentialRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#createManagedCredential");
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
| **createManagedCredentialRequest** | [**CreateManagedCredentialRequest**](CreateManagedCredentialRequest.md)| Information about the Credential to create. | [optional] |

### Return type

[**ManagedCredential**](ManagedCredential.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Credential created. |  -  |
| **0** | Error |  -  |

<a id="createManagedService"></a>
# **createManagedService**
> ManagedService createManagedService(managedService)

Managed Service Create

Creates a Managed Service. Linode Managed will begin monitoring this service and reporting and attempting to resolve any Issues.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    ManagedService managedService = new ManagedService(); // ManagedService | Information about the service to monitor.
    try {
      ManagedService result = apiInstance.createManagedService(managedService);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#createManagedService");
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
| **managedService** | [**ManagedService**](ManagedService.md)| Information about the service to monitor. | [optional] |

### Return type

[**ManagedService**](ManagedService.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service created. |  -  |
| **0** | Error |  -  |

<a id="deleteManagedContact"></a>
# **deleteManagedContact**
> Object deleteManagedContact(contactId)

Managed Contact Delete

Deletes a Managed Contact.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer contactId = 56; // Integer | The ID of the contact to access.
    try {
      Object result = apiInstance.deleteManagedContact(contactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#deleteManagedContact");
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
| **contactId** | **Integer**| The ID of the contact to access. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contact deleted successfully. |  -  |
| **0** | Error |  -  |

<a id="deleteManagedCredential"></a>
# **deleteManagedCredential**
> Object deleteManagedCredential(credentialId)

Managed Credential Delete

Deletes a Managed Credential.  Linode special forces will no longer have access to this Credential when attempting to resolve issues.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer credentialId = 56; // Integer | The ID of the Credential to access.
    try {
      Object result = apiInstance.deleteManagedCredential(credentialId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#deleteManagedCredential");
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
| **credentialId** | **Integer**| The ID of the Credential to access. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Credential deleted successfully. |  -  |
| **0** | Error |  -  |

<a id="deleteManagedService"></a>
# **deleteManagedService**
> Object deleteManagedService(serviceId)

Managed Service Delete

Deletes a Managed Service.  This service will no longer be monitored by Linode Managed.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer serviceId = 56; // Integer | The ID of the Managed Service to access.
    try {
      Object result = apiInstance.deleteManagedService(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#deleteManagedService");
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
| **serviceId** | **Integer**| The ID of the Managed Service to access. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service deleted successfully. |  -  |
| **0** | Error |  -  |

<a id="disableManagedService"></a>
# **disableManagedService**
> ManagedService disableManagedService(serviceId)

Managed Service Disable

Temporarily disables monitoring of a Managed Service.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer serviceId = 56; // Integer | The ID of the Managed Service to disable.
    try {
      ManagedService result = apiInstance.disableManagedService(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#disableManagedService");
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
| **serviceId** | **Integer**| The ID of the Managed Service to disable. | |

### Return type

[**ManagedService**](ManagedService.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service disabled. |  -  |
| **0** | Error |  -  |

<a id="enableManagedService"></a>
# **enableManagedService**
> ManagedService enableManagedService(serviceId)

Managed Service Enable

Enables monitoring of a Managed Service.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer serviceId = 56; // Integer | The ID of the Managed Service to enable.
    try {
      ManagedService result = apiInstance.enableManagedService(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#enableManagedService");
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
| **serviceId** | **Integer**| The ID of the Managed Service to enable. | |

### Return type

[**ManagedService**](ManagedService.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service enabled. |  -  |
| **0** | Error |  -  |

<a id="getManagedContact"></a>
# **getManagedContact**
> ManagedContact getManagedContact(contactId)

Managed Contact View

Returns a single Managed Contact.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer contactId = 56; // Integer | The ID of the contact to access.
    try {
      ManagedContact result = apiInstance.getManagedContact(contactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#getManagedContact");
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
| **contactId** | **Integer**| The ID of the contact to access. | |

### Return type

[**ManagedContact**](ManagedContact.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested Managed Contact. |  -  |
| **0** | Error |  -  |

<a id="getManagedContacts"></a>
# **getManagedContacts**
> GetManagedContacts200Response getManagedContacts(page, pageSize)

Managed Contacts List

Returns a paginated list of Managed Contacts on your Account.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetManagedContacts200Response result = apiInstance.getManagedContacts(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#getManagedContacts");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetManagedContacts200Response**](GetManagedContacts200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of ManagedContacts |  -  |
| **0** | Error |  -  |

<a id="getManagedCredential"></a>
# **getManagedCredential**
> ManagedCredential getManagedCredential(credentialId)

Managed Credential View

Returns a single Managed Credential.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer credentialId = 56; // Integer | The ID of the Credential to access.
    try {
      ManagedCredential result = apiInstance.getManagedCredential(credentialId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#getManagedCredential");
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
| **credentialId** | **Integer**| The ID of the Credential to access. | |

### Return type

[**ManagedCredential**](ManagedCredential.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested Managed Credential. |  -  |
| **0** | Error |  -  |

<a id="getManagedCredentials"></a>
# **getManagedCredentials**
> GetManagedCredentials200Response getManagedCredentials(page, pageSize)

Managed Credentials List

Returns a paginated list of Managed Credentials on your Account.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetManagedCredentials200Response result = apiInstance.getManagedCredentials(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#getManagedCredentials");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetManagedCredentials200Response**](GetManagedCredentials200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of ManagedCredentials |  -  |
| **0** | Error |  -  |

<a id="getManagedIssue"></a>
# **getManagedIssue**
> ManagedIssue getManagedIssue(issueId)

Managed Issue View

Returns a single Issue that is impacting or did impact one of your Managed Services.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer issueId = 56; // Integer | The Issue to look up.
    try {
      ManagedIssue result = apiInstance.getManagedIssue(issueId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#getManagedIssue");
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
| **issueId** | **Integer**| The Issue to look up. | |

### Return type

[**ManagedIssue**](ManagedIssue.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested issue. |  -  |
| **0** | Error |  -  |

<a id="getManagedIssues"></a>
# **getManagedIssues**
> GetManagedIssues200Response getManagedIssues(page, pageSize)

Managed Issues List

Returns a paginated list of recent and ongoing issues detected on your Managed Services.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetManagedIssues200Response result = apiInstance.getManagedIssues(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#getManagedIssues");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetManagedIssues200Response**](GetManagedIssues200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of open or ongoing Managed Issues.  |  -  |
| **0** | Error |  -  |

<a id="getManagedLinodeSetting"></a>
# **getManagedLinodeSetting**
> ManagedLinodeSettings getManagedLinodeSetting(linodeId)

Linode&#39;s Managed Settings View

Returns a single Linode&#39;s Managed settings.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer linodeId = 56; // Integer | The Linode ID whose settings we are accessing.
    try {
      ManagedLinodeSettings result = apiInstance.getManagedLinodeSetting(linodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#getManagedLinodeSetting");
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
| **linodeId** | **Integer**| The Linode ID whose settings we are accessing. | |

### Return type

[**ManagedLinodeSettings**](ManagedLinodeSettings.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested Linode&#39;s Managed settings. |  -  |
| **0** | Error |  -  |

<a id="getManagedLinodeSettings"></a>
# **getManagedLinodeSettings**
> GetManagedLinodeSettings200Response getManagedLinodeSettings(page, pageSize)

Managed Linode Settings List

Returns a paginated list of Managed Settings for your Linodes. There will be one entry per Linode on your Account.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetManagedLinodeSettings200Response result = apiInstance.getManagedLinodeSettings(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#getManagedLinodeSettings");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetManagedLinodeSettings200Response**](GetManagedLinodeSettings200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of Managed settings for your Linodes.  |  -  |
| **0** | Error |  -  |

<a id="getManagedService"></a>
# **getManagedService**
> ManagedService getManagedService(serviceId)

Managed Service View

Returns information about a single Managed Service on your Account.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer serviceId = 56; // Integer | The ID of the Managed Service to access.
    try {
      ManagedService result = apiInstance.getManagedService(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#getManagedService");
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
| **serviceId** | **Integer**| The ID of the Managed Service to access. | |

### Return type

[**ManagedService**](ManagedService.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested Managed Service. |  -  |
| **0** | Error |  -  |

<a id="getManagedServices"></a>
# **getManagedServices**
> GetManagedServices200Response getManagedServices()

Managed Services List

Returns a paginated list of Managed Services on your Account. These are the services Linode Managed is monitoring and will report and attempt to resolve issues with.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    try {
      GetManagedServices200Response result = apiInstance.getManagedServices();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#getManagedServices");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetManagedServices200Response**](GetManagedServices200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of Managed Services |  -  |
| **0** | Error |  -  |

<a id="getManagedStats"></a>
# **getManagedStats**
> GetManagedStats200Response getManagedStats()

Managed Stats List

Returns a list of Managed Stats on your Account in the form of x and y data points. You can use these data points to plot your own graph visualizations. These stats reflect the last 24 hours of combined usage across all managed Linodes on your account giving you a high-level snapshot of data for the following:   * cpu * disk * swap * network in * network out  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    try {
      GetManagedStats200Response result = apiInstance.getManagedStats();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#getManagedStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetManagedStats200Response**](GetManagedStats200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Managed Stats from the last 24 hours. |  -  |
| **0** | Error |  -  |

<a id="updateManagedContact"></a>
# **updateManagedContact**
> ManagedContact updateManagedContact(contactId, managedContact)

Managed Contact Update

Updates information about a Managed Contact. This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer contactId = 56; // Integer | The ID of the contact to access.
    ManagedContact managedContact = new ManagedContact(); // ManagedContact | The fields to update.
    try {
      ManagedContact result = apiInstance.updateManagedContact(contactId, managedContact);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#updateManagedContact");
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
| **contactId** | **Integer**| The ID of the contact to access. | |
| **managedContact** | [**ManagedContact**](ManagedContact.md)| The fields to update. | |

### Return type

[**ManagedContact**](ManagedContact.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contact updated successfully. |  -  |
| **0** | Error |  -  |

<a id="updateManagedCredential"></a>
# **updateManagedCredential**
> ManagedCredential updateManagedCredential(credentialId, managedCredential)

Managed Credential Update

Updates the label of a Managed Credential. This endpoint does not update the username and password for a Managed Credential. To do this, use the Managed Credential Username and Password Update ([POST /managed/credentials/{credentialId}/update](/docs/api/managed/#managed-credential-username-and-password-update)) endpoint instead. This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer credentialId = 56; // Integer | The ID of the Credential to access.
    ManagedCredential managedCredential = new ManagedCredential(); // ManagedCredential | The fields to update.
    try {
      ManagedCredential result = apiInstance.updateManagedCredential(credentialId, managedCredential);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#updateManagedCredential");
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
| **credentialId** | **Integer**| The ID of the Credential to access. | |
| **managedCredential** | [**ManagedCredential**](ManagedCredential.md)| The fields to update. | |

### Return type

[**ManagedCredential**](ManagedCredential.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Credential updated successfully. |  -  |
| **0** | Error |  -  |

<a id="updateManagedCredentialUsernamePassword"></a>
# **updateManagedCredentialUsernamePassword**
> Object updateManagedCredentialUsernamePassword(credentialId, updateManagedCredentialUsernamePasswordRequest)

Managed Credential Username and Password Update

Updates the username and password for a Managed Credential.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer credentialId = 56; // Integer | The ID of the Credential to update.
    UpdateManagedCredentialUsernamePasswordRequest updateManagedCredentialUsernamePasswordRequest = new UpdateManagedCredentialUsernamePasswordRequest(); // UpdateManagedCredentialUsernamePasswordRequest | The new username and password to assign to the Managed Credential. 
    try {
      Object result = apiInstance.updateManagedCredentialUsernamePassword(credentialId, updateManagedCredentialUsernamePasswordRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#updateManagedCredentialUsernamePassword");
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
| **credentialId** | **Integer**| The ID of the Credential to update. | |
| **updateManagedCredentialUsernamePasswordRequest** | [**UpdateManagedCredentialUsernamePasswordRequest**](UpdateManagedCredentialUsernamePasswordRequest.md)| The new username and password to assign to the Managed Credential.  | [optional] |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Credential username and password updated. |  -  |
| **0** | Error |  -  |

<a id="updateManagedLinodeSetting"></a>
# **updateManagedLinodeSetting**
> ManagedLinodeSettings updateManagedLinodeSetting(linodeId, managedLinodeSettings)

Linode&#39;s Managed Settings Update

Updates a single Linode&#39;s Managed settings. This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer linodeId = 56; // Integer | The Linode ID whose settings we are accessing.
    ManagedLinodeSettings managedLinodeSettings = new ManagedLinodeSettings(); // ManagedLinodeSettings | The settings to update.
    try {
      ManagedLinodeSettings result = apiInstance.updateManagedLinodeSetting(linodeId, managedLinodeSettings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#updateManagedLinodeSetting");
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
| **linodeId** | **Integer**| The Linode ID whose settings we are accessing. | |
| **managedLinodeSettings** | [**ManagedLinodeSettings**](ManagedLinodeSettings.md)| The settings to update. | |

### Return type

[**ManagedLinodeSettings**](ManagedLinodeSettings.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings updated successfully. |  -  |
| **0** | Error |  -  |

<a id="updateManagedService"></a>
# **updateManagedService**
> ManagedService updateManagedService(serviceId, managedService)

Managed Service Update

Updates information about a Managed Service.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    Integer serviceId = 56; // Integer | The ID of the Managed Service to access.
    ManagedService managedService = new ManagedService(); // ManagedService | The fields to update.
    try {
      ManagedService result = apiInstance.updateManagedService(serviceId, managedService);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#updateManagedService");
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
| **serviceId** | **Integer**| The ID of the Managed Service to access. | |
| **managedService** | [**ManagedService**](ManagedService.md)| The fields to update. | |

### Return type

[**ManagedService**](ManagedService.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service updated successfully. |  -  |
| **0** | Error |  -  |

<a id="viewManagedSSHKey"></a>
# **viewManagedSSHKey**
> ViewManagedSSHKey200Response viewManagedSSHKey()

Managed SSH Key View

Returns the unique SSH public key assigned to your Linode account&#39;s Managed service. If you [add this public key](/docs/guides/linode-managed/#adding-the-public-key) to a Linode on your account, Linode special forces will be able to log in to the Linode with this key when attempting to resolve issues.  This command can only be accessed by the unrestricted users of an account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedApi apiInstance = new ManagedApi(defaultClient);
    try {
      ViewManagedSSHKey200Response result = apiInstance.viewManagedSSHKey();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedApi#viewManagedSSHKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ViewManagedSSHKey200Response**](ViewManagedSSHKey200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested Managed SSH public key. |  -  |
| **0** | Error |  -  |

