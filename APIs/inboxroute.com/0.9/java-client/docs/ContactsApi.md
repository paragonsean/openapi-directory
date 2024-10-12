# ContactsApi

All URIs are relative to *https://api.inboxroute.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contactsContactidDelete**](ContactsApi.md#contactsContactidDelete) | **DELETE** /contacts/{contactid} |  |
| [**contactsContactidPut**](ContactsApi.md#contactsContactidPut) | **PUT** /contacts/{contactid} |  |
| [**contactsGet**](ContactsApi.md#contactsGet) | **GET** /contacts |  |


<a id="contactsContactidDelete"></a>
# **contactsContactidDelete**
> contactsContactidDelete(contactid)



Delete an existing contact

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
    defaultClient.setBasePath("https://api.inboxroute.com/api");
    
    // Configure API key authorization: mqApiKey
    ApiKeyAuth mqApiKey = (ApiKeyAuth) defaultClient.getAuthentication("mqApiKey");
    mqApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //mqApiKey.setApiKeyPrefix("Token");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String contactid = "contactid_example"; // String | Unique 16 characters ID of the contact
    try {
      apiInstance.contactsContactidDelete(contactid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#contactsContactidDelete");
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
| **contactid** | **String**| Unique 16 characters ID of the contact | |

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

<a id="contactsContactidPut"></a>
# **contactsContactidPut**
> contactsContactidPut(contactid, contact)



Update an existing contact

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
    defaultClient.setBasePath("https://api.inboxroute.com/api");
    
    // Configure API key authorization: mqApiKey
    ApiKeyAuth mqApiKey = (ApiKeyAuth) defaultClient.getAuthentication("mqApiKey");
    mqApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //mqApiKey.setApiKeyPrefix("Token");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String contactid = "contactid_example"; // String | Unique 16 characters ID of the contact
    ContactUpdate contact = new ContactUpdate(); // ContactUpdate | Contact properties to update
    try {
      apiInstance.contactsContactidPut(contactid, contact);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#contactsContactidPut");
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
| **contactid** | **String**| Unique 16 characters ID of the contact | |
| **contact** | [**ContactUpdate**](ContactUpdate.md)| Contact properties to update | |

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

<a id="contactsGet"></a>
# **contactsGet**
> ContactPage contactsGet(listid, offset, limit, sort)



Get a paged result of contacts from a list

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
    defaultClient.setBasePath("https://api.inboxroute.com/api");
    
    // Configure API key authorization: mqApiKey
    ApiKeyAuth mqApiKey = (ApiKeyAuth) defaultClient.getAuthentication("mqApiKey");
    mqApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //mqApiKey.setApiKeyPrefix("Token");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String listid = "listid_example"; // String | Unique 16 characters ID of the contact list to get contacts of
    Integer offset = 56; // Integer | Skip that many records
    Integer limit = 56; // Integer | Maximum number of items in page
    String sort = "sort_example"; // String | Property to sort by. Append '-' for descending order.
    try {
      ContactPage result = apiInstance.contactsGet(listid, offset, limit, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#contactsGet");
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
| **listid** | **String**| Unique 16 characters ID of the contact list to get contacts of | [optional] |
| **offset** | **Integer**| Skip that many records | [optional] |
| **limit** | **Integer**| Maximum number of items in page | [optional] |
| **sort** | **String**| Property to sort by. Append &#39;-&#39; for descending order. | [optional] |

### Return type

[**ContactPage**](ContactPage.md)

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

