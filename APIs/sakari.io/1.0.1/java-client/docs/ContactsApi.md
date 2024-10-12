# ContactsApi

All URIs are relative to *https://api.sakari.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contactsCreate**](ContactsApi.md#contactsCreate) | **POST** /v1/accounts/{accountId}/contacts | Create contact |
| [**contactsFetch**](ContactsApi.md#contactsFetch) | **GET** /v1/accounts/{accountId}/contacts/{contactId} | Fetch contact by ID |
| [**contactsFetchAll**](ContactsApi.md#contactsFetchAll) | **GET** /v1/accounts/{accountId}/contacts | Fetch contacts |
| [**contactsRemove**](ContactsApi.md#contactsRemove) | **DELETE** /v1/accounts/{accountId}/contacts/{contactId} | Deletes a contact |
| [**contactsUpdate**](ContactsApi.md#contactsUpdate) | **PUT** /v1/accounts/{accountId}/contacts/{contactId} | Updates a contact |


<a id="contactsCreate"></a>
# **contactsCreate**
> ContactsCreate201Response contactsCreate(accountId, mergeStrategy, contactRequest)

Create contact

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
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    String mergeStrategy = "append"; // String | Determines how existing contacts with matching mobile numbers are treated
    ContactRequest contactRequest = new ContactRequest(); // ContactRequest | 
    try {
      ContactsCreate201Response result = apiInstance.contactsCreate(accountId, mergeStrategy, contactRequest);
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
| **accountId** | **String**| Account to apply operations to | |
| **mergeStrategy** | **String**| Determines how existing contacts with matching mobile numbers are treated | [optional] [enum: append, core, remove] |
| **contactRequest** | [**ContactRequest**](ContactRequest.md)|  | [optional] |

### Return type

[**ContactsCreate201Response**](ContactsCreate201Response.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/csv
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | successful operation |  -  |

<a id="contactsFetch"></a>
# **contactsFetch**
> ContactResponse contactsFetch(accountId, contactId)

Fetch contact by ID

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
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    String contactId = "contactId_example"; // String | ID of contact to return
    try {
      ContactResponse result = apiInstance.contactsFetch(accountId, contactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#contactsFetch");
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
| **accountId** | **String**| Account to apply operations to | |
| **contactId** | **String**| ID of contact to return | |

### Return type

[**ContactResponse**](ContactResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="contactsFetchAll"></a>
# **contactsFetchAll**
> ContactsResponse contactsFetchAll(accountId, offset, limit, firstName, lastName, mobile, email, tags)

Fetch contacts

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
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    Long offset = 56L; // Long | Results to skip when paginating through a result set
    Long limit = 56L; // Long | Maximum number of results to return
    String firstName = "firstName_example"; // String | Filter by first name or part of
    String lastName = "lastName_example"; // String | Filter by last name or part of
    String mobile = "mobile_example"; // String | Filter by mobile or part of
    String email = "email_example"; // String | Filter by email or part of
    String tags = "tags_example"; // String | Filter by tag(s)
    try {
      ContactsResponse result = apiInstance.contactsFetchAll(accountId, offset, limit, firstName, lastName, mobile, email, tags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#contactsFetchAll");
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
| **accountId** | **String**| Account to apply operations to | |
| **offset** | **Long**| Results to skip when paginating through a result set | [optional] |
| **limit** | **Long**| Maximum number of results to return | [optional] |
| **firstName** | **String**| Filter by first name or part of | [optional] |
| **lastName** | **String**| Filter by last name or part of | [optional] |
| **mobile** | **String**| Filter by mobile or part of | [optional] |
| **email** | **String**| Filter by email or part of | [optional] |
| **tags** | **String**| Filter by tag(s) | [optional] |

### Return type

[**ContactsResponse**](ContactsResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **4XX** | invalid request |  -  |
| **5XX** | invalid request |  -  |

<a id="contactsRemove"></a>
# **contactsRemove**
> CampaignsRemove200Response contactsRemove(accountId, contactId)

Deletes a contact

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
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    String contactId = "contactId_example"; // String | Contact id to delete
    try {
      CampaignsRemove200Response result = apiInstance.contactsRemove(accountId, contactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#contactsRemove");
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
| **accountId** | **String**| Account to apply operations to | |
| **contactId** | **String**| Contact id to delete | |

### Return type

[**CampaignsRemove200Response**](CampaignsRemove200Response.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="contactsUpdate"></a>
# **contactsUpdate**
> ContactResponse contactsUpdate(accountId, contactId)

Updates a contact

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
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    String contactId = "contactId_example"; // String | ID of contact
    try {
      ContactResponse result = apiInstance.contactsUpdate(accountId, contactId);
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
| **accountId** | **String**| Account to apply operations to | |
| **contactId** | **String**| ID of contact | |

### Return type

[**ContactResponse**](ContactResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

