# ContactsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contactsCreate**](ContactsApi.md#contactsCreate) | **POST** /contacts |  |
| [**contactsDestroy**](ContactsApi.md#contactsDestroy) | **DELETE** /contacts/{id} |  |
| [**contactsList**](ContactsApi.md#contactsList) | **GET** /contacts |  |
| [**contactsPartialUpdate**](ContactsApi.md#contactsPartialUpdate) | **PATCH** /contacts/{id} |  |
| [**contactsRead**](ContactsApi.md#contactsRead) | **GET** /contacts/{id} |  |
| [**contactsUpdate**](ContactsApi.md#contactsUpdate) | **PUT** /contacts/{id} |  |


<a id="contactsCreate"></a>
# **contactsCreate**
> Contact contactsCreate(contactRequest)



Create a new contact.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    ContactRequest contactRequest = new ContactRequest(); // ContactRequest | A contact creation request
    try {
      Contact result = apiInstance.contactsCreate(contactRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#contactsCreate");
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
| **contactRequest** | [**ContactRequest**](ContactRequest.md)| A contact creation request | [optional] |

### Return type

[**Contact**](Contact.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Contact |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="contactsDestroy"></a>
# **contactsDestroy**
> Contact contactsDestroy(id)



Remove a contact.  Please note, that a contact can only be removed if it is not longer in use in a network service or config through a role assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      Contact result = apiInstance.contactsDestroy(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#contactsDestroy");
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
| **id** | **String**| Get by id | |

### Return type

[**Contact**](Contact.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contact |  -  |
| **400** | UnableToFulfill |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="contactsList"></a>
# **contactsList**
> List&lt;Contact&gt; contactsList(id, managingAccount, consumingAccount, externalRef)



List available contacts managed by the authorized account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    String managingAccount = "managingAccount_example"; // String | Filter by managing_account
    String consumingAccount = "consumingAccount_example"; // String | Filter by consuming_account
    String externalRef = "externalRef_example"; // String | Filter by external_ref
    try {
      List<Contact> result = apiInstance.contactsList(id, managingAccount, consumingAccount, externalRef);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#contactsList");
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
| **id** | [**List&lt;String&gt;**](String.md)| Filter by id | [optional] |
| **managingAccount** | **String**| Filter by managing_account | [optional] |
| **consumingAccount** | **String**| Filter by consuming_account | [optional] |
| **externalRef** | **String**| Filter by external_ref | [optional] |

### Return type

[**List&lt;Contact&gt;**](Contact.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: Contact |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="contactsPartialUpdate"></a>
# **contactsPartialUpdate**
> Contact contactsPartialUpdate(id, contactRequestPartial)



Update parts of a contact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    ContactRequestPartial contactRequestPartial = new ContactRequestPartial(); // ContactRequestPartial | A contact creation request
    try {
      Contact result = apiInstance.contactsPartialUpdate(id, contactRequestPartial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#contactsPartialUpdate");
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
| **id** | **String**| Get by id | |
| **contactRequestPartial** | [**ContactRequestPartial**](ContactRequestPartial.md)| A contact creation request | [optional] |

### Return type

[**Contact**](Contact.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contact |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="contactsRead"></a>
# **contactsRead**
> Contact contactsRead(id)



Get a contact by it&#39;s id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      Contact result = apiInstance.contactsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#contactsRead");
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
| **id** | **String**| Get by id | |

### Return type

[**Contact**](Contact.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contact |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="contactsUpdate"></a>
# **contactsUpdate**
> Contact contactsUpdate(id, contactRequest)



Update a contact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    ContactRequest contactRequest = new ContactRequest(); // ContactRequest | A contact creation request
    try {
      Contact result = apiInstance.contactsUpdate(id, contactRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#contactsUpdate");
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
| **id** | **String**| Get by id | |
| **contactRequest** | [**ContactRequest**](ContactRequest.md)| A contact creation request | [optional] |

### Return type

[**Contact**](Contact.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contact |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

