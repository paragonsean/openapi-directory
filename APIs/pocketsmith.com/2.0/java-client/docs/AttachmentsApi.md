# AttachmentsApi

All URIs are relative to *https://api.pocketsmith.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**attachmentsIdDelete**](AttachmentsApi.md#attachmentsIdDelete) | **DELETE** /attachments/{id} | Delete attachment |
| [**attachmentsIdGet**](AttachmentsApi.md#attachmentsIdGet) | **GET** /attachments/{id} | Get attachment |
| [**attachmentsIdPut**](AttachmentsApi.md#attachmentsIdPut) | **PUT** /attachments/{id} | Update attachment |
| [**transactionsIdAttachmentsGet**](AttachmentsApi.md#transactionsIdAttachmentsGet) | **GET** /transactions/{id}/attachments | List attachments in transaction |
| [**transactionsIdAttachmentsPost**](AttachmentsApi.md#transactionsIdAttachmentsPost) | **POST** /transactions/{id}/attachments | Assigns attachment to transaction |
| [**transactionsTransactionIdAttachmentsAttachmentIdDelete**](AttachmentsApi.md#transactionsTransactionIdAttachmentsAttachmentIdDelete) | **DELETE** /transactions/{transaction_id}/attachments/{attachment_id} | Unassigns attachment in transaction |
| [**usersIdAttachmentsGet**](AttachmentsApi.md#usersIdAttachmentsGet) | **GET** /users/{id}/attachments | Lists attachments in user |
| [**usersIdAttachmentsPost**](AttachmentsApi.md#usersIdAttachmentsPost) | **POST** /users/{id}/attachments | Create attachment in user |


<a id="attachmentsIdDelete"></a>
# **attachmentsIdDelete**
> attachmentsIdDelete(id)

Delete attachment

Deletes a particular attachment by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the attachment.
    try {
      apiInstance.attachmentsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#attachmentsIdDelete");
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
| **id** | **Integer**| The unique identifier of the attachment. | |

### Return type

null (empty response body)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="attachmentsIdGet"></a>
# **attachmentsIdGet**
> Attachment attachmentsIdGet(id)

Get attachment

Gets a particular attachment by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the attachment.
    try {
      Attachment result = apiInstance.attachmentsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#attachmentsIdGet");
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
| **id** | **Integer**| The unique identifier of the attachment. | |

### Return type

[**Attachment**](Attachment.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="attachmentsIdPut"></a>
# **attachmentsIdPut**
> Attachment attachmentsIdPut(id, attachmentsIdPutRequest)

Update attachment

Updates the title of the attachment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the attachment.
    AttachmentsIdPutRequest attachmentsIdPutRequest = new AttachmentsIdPutRequest(); // AttachmentsIdPutRequest | 
    try {
      Attachment result = apiInstance.attachmentsIdPut(id, attachmentsIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#attachmentsIdPut");
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
| **id** | **Integer**| The unique identifier of the attachment. | |
| **attachmentsIdPutRequest** | [**AttachmentsIdPutRequest**](AttachmentsIdPutRequest.md)|  | [optional] |

### Return type

[**Attachment**](Attachment.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |
| **422** | Validation Error |  -  |

<a id="transactionsIdAttachmentsGet"></a>
# **transactionsIdAttachmentsGet**
> List&lt;Attachment&gt; transactionsIdAttachmentsGet(id)

List attachments in transaction

Lists attachments belonging to a transaction by their ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the transaction.
    try {
      List<Attachment> result = apiInstance.transactionsIdAttachmentsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#transactionsIdAttachmentsGet");
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
| **id** | **Integer**| The unique identifier of the transaction. | |

### Return type

[**List&lt;Attachment&gt;**](Attachment.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="transactionsIdAttachmentsPost"></a>
# **transactionsIdAttachmentsPost**
> Attachment transactionsIdAttachmentsPost(id, transactionsIdAttachmentsPostRequest)

Assigns attachment to transaction

Assigns an attachment to the transaction by their ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the transaction.
    TransactionsIdAttachmentsPostRequest transactionsIdAttachmentsPostRequest = new TransactionsIdAttachmentsPostRequest(); // TransactionsIdAttachmentsPostRequest | 
    try {
      Attachment result = apiInstance.transactionsIdAttachmentsPost(id, transactionsIdAttachmentsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#transactionsIdAttachmentsPost");
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
| **id** | **Integer**| The unique identifier of the transaction. | |
| **transactionsIdAttachmentsPostRequest** | [**TransactionsIdAttachmentsPostRequest**](TransactionsIdAttachmentsPostRequest.md)|  | [optional] |

### Return type

[**Attachment**](Attachment.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="transactionsTransactionIdAttachmentsAttachmentIdDelete"></a>
# **transactionsTransactionIdAttachmentsAttachmentIdDelete**
> transactionsTransactionIdAttachmentsAttachmentIdDelete(transactionId, attachmentId)

Unassigns attachment in transaction

Unassigns a particular attachment by its ID from the transaction ID. This does not delete the attachment, it only removes its association from the transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    Integer transactionId = 42; // Integer | The unique identifier of the transaction.
    Integer attachmentId = 1438154; // Integer | The unique identifier of the attachment.
    try {
      apiInstance.transactionsTransactionIdAttachmentsAttachmentIdDelete(transactionId, attachmentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#transactionsTransactionIdAttachmentsAttachmentIdDelete");
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
| **transactionId** | **Integer**| The unique identifier of the transaction. | |
| **attachmentId** | **Integer**| The unique identifier of the attachment. | |

### Return type

null (empty response body)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="usersIdAttachmentsGet"></a>
# **usersIdAttachmentsGet**
> List&lt;Attachment&gt; usersIdAttachmentsGet(id, unassigned)

Lists attachments in user

Lists attachments belonging to a user by their ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the user.
    Integer unassigned = 1; // Integer | If set, returns unassigned attachments, that are available for assigning to a transaction.
    try {
      List<Attachment> result = apiInstance.usersIdAttachmentsGet(id, unassigned);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#usersIdAttachmentsGet");
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
| **id** | **Integer**| The unique identifier of the user. | |
| **unassigned** | **Integer**| If set, returns unassigned attachments, that are available for assigning to a transaction. | [optional] |

### Return type

[**List&lt;Attachment&gt;**](Attachment.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="usersIdAttachmentsPost"></a>
# **usersIdAttachmentsPost**
> Attachment usersIdAttachmentsPost(id, usersIdAttachmentsPostRequest)

Create attachment in user

Creates an attachment belonging to the user by their ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the user.
    UsersIdAttachmentsPostRequest usersIdAttachmentsPostRequest = new UsersIdAttachmentsPostRequest(); // UsersIdAttachmentsPostRequest | 
    try {
      Attachment result = apiInstance.usersIdAttachmentsPost(id, usersIdAttachmentsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#usersIdAttachmentsPost");
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
| **id** | **Integer**| The unique identifier of the user. | |
| **usersIdAttachmentsPostRequest** | [**UsersIdAttachmentsPostRequest**](UsersIdAttachmentsPostRequest.md)|  | [optional] |

### Return type

[**Attachment**](Attachment.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |
| **422** | Validation Error |  -  |

