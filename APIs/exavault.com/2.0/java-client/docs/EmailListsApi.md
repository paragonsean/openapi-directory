# EmailListsApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addEmailList**](EmailListsApi.md#addEmailList) | **POST** /email-lists | Create new email list |
| [**deleteEmailListById**](EmailListsApi.md#deleteEmailListById) | **DELETE** /email-lists/{id} | Delete an email group with given id |
| [**getEmailListById**](EmailListsApi.md#getEmailListById) | **GET** /email-lists/{id} | Get individual email group |
| [**getEmailLists**](EmailListsApi.md#getEmailLists) | **GET** /email-lists | Get all email groups |
| [**updateEmailListById**](EmailListsApi.md#updateEmailListById) | **PATCH** /email-lists/{id} | Update an email group |


<a id="addEmailList"></a>
# **addEmailList**
> EmailListResponse addEmailList(evApiKey, evAccessToken, addEmailListRequestBody)

Create new email list

Create a new email list. Among other things, email lists can be used to send files or share folders with a group of email addresses at once.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    EmailListsApi apiInstance = new EmailListsApi(defaultClient);
    String evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    AddEmailListRequestBody addEmailListRequestBody = new AddEmailListRequestBody(); // AddEmailListRequestBody | 
    try {
      EmailListResponse result = apiInstance.addEmailList(evApiKey, evAccessToken, addEmailListRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailListsApi#addEmailList");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **addEmailListRequestBody** | [**AddEmailListRequestBody**](AddEmailListRequestBody.md)|  | [optional] |

### Return type

[**EmailListResponse**](EmailListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteEmailListById"></a>
# **deleteEmailListById**
> EmptyResponse deleteEmailListById(evApiKey, evAccessToken, id)

Delete an email group with given id

Permanently delete an email group. This action is not reversible. We recommend making a user confirm this action before sending the API call. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    EmailListsApi apiInstance = new EmailListsApi(defaultClient);
    String evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    Integer id = 56; // Integer | ID of the email list to delete
    try {
      EmptyResponse result = apiInstance.deleteEmailListById(evApiKey, evAccessToken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailListsApi#deleteEmailListById");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **id** | **Integer**| ID of the email list to delete | |

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="getEmailListById"></a>
# **getEmailListById**
> EmailListResponse getEmailListById(evApiKey, evAccessToken, id, include)

Get individual email group

Retrieve all the details of a specific email list including it&#39;s name, when it was created and all the email addresses that belong to the group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    EmailListsApi apiInstance = new EmailListsApi(defaultClient);
    String evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    Integer id = 56; // Integer | ID of the email list to return.
    String include = "include_example"; // String | Related record types to include in the response. Valid option is `ownerUser`
    try {
      EmailListResponse result = apiInstance.getEmailListById(evApiKey, evAccessToken, id, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailListsApi#getEmailListById");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **id** | **Integer**| ID of the email list to return. | |
| **include** | **String**| Related record types to include in the response. Valid option is &#x60;ownerUser&#x60; | [optional] |

### Return type

[**EmailListResponse**](EmailListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="getEmailLists"></a>
# **getEmailLists**
> EmailListCollectionResponse getEmailLists(evApiKey, evAccessToken, include)

Get all email groups

List all email groups for authenticated user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    EmailListsApi apiInstance = new EmailListsApi(defaultClient);
    String evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    String include = "include_example"; // String | Related record types to include in the response. Valid option is `ownerUser`
    try {
      EmailListCollectionResponse result = apiInstance.getEmailLists(evApiKey, evAccessToken, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailListsApi#getEmailLists");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **include** | **String**| Related record types to include in the response. Valid option is &#x60;ownerUser&#x60; | [optional] |

### Return type

[**EmailListCollectionResponse**](EmailListCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateEmailListById"></a>
# **updateEmailListById**
> EmailListResponse updateEmailListById(evApiKey, evAccessToken, id, updateEmailListRequestBody)

Update an email group

Add or remove emails from an email list that can be used to send and share files with groups.   **Notes**  *This call will **replace** your current email list in its entirety.* If you want to keep any existing emails on the list, be sure to submit the call with any current emails you want to keep on the list.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    EmailListsApi apiInstance = new EmailListsApi(defaultClient);
    String evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    Integer id = 56; // Integer | ID of the email list to update.
    UpdateEmailListRequestBody updateEmailListRequestBody = new UpdateEmailListRequestBody(); // UpdateEmailListRequestBody | 
    try {
      EmailListResponse result = apiInstance.updateEmailListById(evApiKey, evAccessToken, id, updateEmailListRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailListsApi#updateEmailListById");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **id** | **Integer**| ID of the email list to update. | |
| **updateEmailListRequestBody** | [**UpdateEmailListRequestBody**](UpdateEmailListRequestBody.md)|  | [optional] |

### Return type

[**EmailListResponse**](EmailListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

