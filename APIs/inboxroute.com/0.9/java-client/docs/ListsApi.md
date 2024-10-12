# ListsApi

All URIs are relative to *https://api.inboxroute.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contactsListsGet**](ListsApi.md#contactsListsGet) | **GET** /contacts/lists |  |
| [**contactsListsListidDelete**](ListsApi.md#contactsListsListidDelete) | **DELETE** /contacts/lists/{listid} |  |
| [**contactsListsListidPut**](ListsApi.md#contactsListsListidPut) | **PUT** /contacts/lists/{listid} |  |
| [**contactsListsPost**](ListsApi.md#contactsListsPost) | **POST** /contacts/lists |  |


<a id="contactsListsGet"></a>
# **contactsListsGet**
> ContactListPage contactsListsGet(offset, limit, sort)



Get a paged result of contact lists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.inboxroute.com/api");
    
    // Configure API key authorization: mqApiKey
    ApiKeyAuth mqApiKey = (ApiKeyAuth) defaultClient.getAuthentication("mqApiKey");
    mqApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //mqApiKey.setApiKeyPrefix("Token");

    ListsApi apiInstance = new ListsApi(defaultClient);
    Integer offset = 56; // Integer | Skip that many records
    Integer limit = 56; // Integer | Maximum number of items in page
    String sort = "sort_example"; // String | Property to sort by. Append '-' for descending order.
    try {
      ContactListPage result = apiInstance.contactsListsGet(offset, limit, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListsApi#contactsListsGet");
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
| **offset** | **Integer**| Skip that many records | [optional] |
| **limit** | **Integer**| Maximum number of items in page | [optional] |
| **sort** | **String**| Property to sort by. Append &#39;-&#39; for descending order. | [optional] |

### Return type

[**ContactListPage**](ContactListPage.md)

### Authorization

[mqApiKey](../README.md#mqApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Page object |  -  |
| **401** | Invalid api key or key does not have access to this ressource |  -  |
| **404** | The requested resource was not found |  -  |
| **422** | The request parameters were invalid |  -  |

<a id="contactsListsListidDelete"></a>
# **contactsListsListidDelete**
> contactsListsListidDelete(listid)



Delete an existing contact list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.inboxroute.com/api");
    
    // Configure API key authorization: mqApiKey
    ApiKeyAuth mqApiKey = (ApiKeyAuth) defaultClient.getAuthentication("mqApiKey");
    mqApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //mqApiKey.setApiKeyPrefix("Token");

    ListsApi apiInstance = new ListsApi(defaultClient);
    String listid = "listid_example"; // String | Unique 16 characters ID of the contact list
    try {
      apiInstance.contactsListsListidDelete(listid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListsApi#contactsListsListidDelete");
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
| **listid** | **String**| Unique 16 characters ID of the contact list | |

### Return type

null (empty response body)

### Authorization

[mqApiKey](../README.md#mqApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Empty response |  -  |
| **401** | Invalid api key or key does not have access to this ressource |  -  |
| **404** | The requested resource was not found |  -  |

<a id="contactsListsListidPut"></a>
# **contactsListsListidPut**
> contactsListsListidPut(listid, contactlist)



Update an existing contact list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.inboxroute.com/api");
    
    // Configure API key authorization: mqApiKey
    ApiKeyAuth mqApiKey = (ApiKeyAuth) defaultClient.getAuthentication("mqApiKey");
    mqApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //mqApiKey.setApiKeyPrefix("Token");

    ListsApi apiInstance = new ListsApi(defaultClient);
    String listid = "listid_example"; // String | Unique 16 characters ID of the contact list
    ContactListUpdate contactlist = new ContactListUpdate(); // ContactListUpdate | Contact list properties to update
    try {
      apiInstance.contactsListsListidPut(listid, contactlist);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListsApi#contactsListsListidPut");
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
| **listid** | **String**| Unique 16 characters ID of the contact list | |
| **contactlist** | [**ContactListUpdate**](ContactListUpdate.md)| Contact list properties to update | [optional] |

### Return type

null (empty response body)

### Authorization

[mqApiKey](../README.md#mqApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Empty response |  -  |
| **401** | Invalid api key or key does not have access to this ressource |  -  |
| **404** | The requested resource was not found |  -  |
| **422** | The request parameters were invalid |  -  |

<a id="contactsListsPost"></a>
# **contactsListsPost**
> NewId contactsListsPost(contactlist)



Add a new contact list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.inboxroute.com/api");
    
    // Configure API key authorization: mqApiKey
    ApiKeyAuth mqApiKey = (ApiKeyAuth) defaultClient.getAuthentication("mqApiKey");
    mqApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //mqApiKey.setApiKeyPrefix("Token");

    ListsApi apiInstance = new ListsApi(defaultClient);
    ContactListUpdate contactlist = new ContactListUpdate(); // ContactListUpdate | Contact list initial properties
    try {
      NewId result = apiInstance.contactsListsPost(contactlist);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListsApi#contactsListsPost");
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
| **contactlist** | [**ContactListUpdate**](ContactListUpdate.md)| Contact list initial properties | [optional] |

### Return type

[**NewId**](NewId.md)

### Authorization

[mqApiKey](../README.md#mqApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Page object |  -  |
| **401** | Invalid api key or key does not have access to this ressource |  -  |
| **422** | The request parameters were invalid |  -  |

