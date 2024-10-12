# ContactPersonsApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addContactPerson**](ContactPersonsApi.md#addContactPerson) | **POST** /contacts/{contact_id}/contact_persons | Add a new contact person to a contact |
| [**contactsContactIdContactPersonsContactPersonIdDelete**](ContactPersonsApi.md#contactsContactIdContactPersonsContactPersonIdDelete) | **DELETE** /contacts/{contact_id}/contact_persons/{contact_person_id} | Delete a contact person |
| [**editContactPerson**](ContactPersonsApi.md#editContactPerson) | **PUT** /contacts/{contact_id}/contact_persons/{contact_person_id} | Edit a contact person |
| [**getContactPerson**](ContactPersonsApi.md#getContactPerson) | **GET** /contacts/{contact_id}/contact_persons/{contact_person_id} | Get a contact person |
| [**getContactPersonsList**](ContactPersonsApi.md#getContactPersonsList) | **GET** /contacts/{contact_id}/contact_persons | Get a list of contact people |


<a id="addContactPerson"></a>
# **addContactPerson**
> ClockingRecordsPost201Response addContactPerson(contactId, addContactPersonRequest)

Add a new contact person to a contact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactPersonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    ContactPersonsApi apiInstance = new ContactPersonsApi(defaultClient);
    String contactId = "contactId_example"; // String | 
    AddContactPersonRequest addContactPersonRequest = new AddContactPersonRequest(); // AddContactPersonRequest | 
    try {
      ClockingRecordsPost201Response result = apiInstance.addContactPerson(contactId, addContactPersonRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactPersonsApi#addContactPerson");
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
| **contactId** | **String**|  | |
| **addContactPersonRequest** | [**AddContactPersonRequest**](AddContactPersonRequest.md)|  | [optional] |

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successfully added contact person |  -  |
| **404** | Not found |  -  |
| **422** | Validation error |  -  |

<a id="contactsContactIdContactPersonsContactPersonIdDelete"></a>
# **contactsContactIdContactPersonsContactPersonIdDelete**
> ClockingRecordsClockingRecordIdDelete200Response contactsContactIdContactPersonsContactPersonIdDelete(contactId, contactPersonId)

Delete a contact person

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactPersonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    ContactPersonsApi apiInstance = new ContactPersonsApi(defaultClient);
    String contactId = "contactId_example"; // String | 
    String contactPersonId = "contactPersonId_example"; // String | 
    try {
      ClockingRecordsClockingRecordIdDelete200Response result = apiInstance.contactsContactIdContactPersonsContactPersonIdDelete(contactId, contactPersonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactPersonsApi#contactsContactIdContactPersonsContactPersonIdDelete");
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
| **contactId** | **String**|  | |
| **contactPersonId** | **String**|  | |

### Return type

[**ClockingRecordsClockingRecordIdDelete200Response**](ClockingRecordsClockingRecordIdDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="editContactPerson"></a>
# **editContactPerson**
> ClockingRecordsClockingRecordIdPut200Response editContactPerson(contactId, contactPersonId, addContactPersonRequest)

Edit a contact person

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactPersonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    ContactPersonsApi apiInstance = new ContactPersonsApi(defaultClient);
    String contactId = "contactId_example"; // String | 
    String contactPersonId = "contactPersonId_example"; // String | 
    AddContactPersonRequest addContactPersonRequest = new AddContactPersonRequest(); // AddContactPersonRequest | 
    try {
      ClockingRecordsClockingRecordIdPut200Response result = apiInstance.editContactPerson(contactId, contactPersonId, addContactPersonRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactPersonsApi#editContactPerson");
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
| **contactId** | **String**|  | |
| **contactPersonId** | **String**|  | |
| **addContactPersonRequest** | [**AddContactPersonRequest**](AddContactPersonRequest.md)|  | [optional] |

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="getContactPerson"></a>
# **getContactPerson**
> GetContactPerson200Response getContactPerson(contactId, contactPersonId)

Get a contact person

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactPersonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    ContactPersonsApi apiInstance = new ContactPersonsApi(defaultClient);
    String contactId = "contactId_example"; // String | 
    String contactPersonId = "contactPersonId_example"; // String | 
    try {
      GetContactPerson200Response result = apiInstance.getContactPerson(contactId, contactPersonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactPersonsApi#getContactPerson");
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
| **contactId** | **String**|  | |
| **contactPersonId** | **String**|  | |

### Return type

[**GetContactPerson200Response**](GetContactPerson200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="getContactPersonsList"></a>
# **getContactPersonsList**
> GetContactPersonsList200Response getContactPersonsList(contactId, q, createdGte, createdLte)

Get a list of contact people

Get a list of contact people associated with a contact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactPersonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    ContactPersonsApi apiInstance = new ContactPersonsApi(defaultClient);
    String contactId = "contactId_example"; // String | 
    String q = "q_example"; // String | 
    LocalDate createdGte = LocalDate.now(); // LocalDate | 
    LocalDate createdLte = LocalDate.now(); // LocalDate | 
    try {
      GetContactPersonsList200Response result = apiInstance.getContactPersonsList(contactId, q, createdGte, createdLte);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactPersonsApi#getContactPersonsList");
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
| **contactId** | **String**|  | |
| **q** | **String**|  | [optional] |
| **createdGte** | **LocalDate**|  | [optional] |
| **createdLte** | **LocalDate**|  | [optional] |

### Return type

[**GetContactPersonsList200Response**](GetContactPersonsList200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

