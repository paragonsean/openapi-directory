# FormApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteFormMessageById**](FormApi.md#deleteFormMessageById) | **DELETE** /forms/entries/{id} | Delete a receive form submission |
| [**getFormById**](FormApi.md#getFormById) | **GET** /forms/{id} | Get receive folder form by Id |
| [**getFormByShareHash**](FormApi.md#getFormByShareHash) | **GET** /forms | Get receive folder form settings |
| [**getFormEntries**](FormApi.md#getFormEntries) | **GET** /forms/entries/{id} | Get form data entries for a receive |
| [**updateFormById**](FormApi.md#updateFormById) | **PATCH** /forms/{id} | Updates a form with given parameters |


<a id="deleteFormMessageById"></a>
# **deleteFormMessageById**
> EmptyResponse deleteFormMessageById(evApiKey, evAccessToken, id)

Delete a receive form submission

Deletes a form submission entry, which represents one time that a visitor filled out the form and uploaded files. This deletes only the record of the submission (the date, the values entered in the form and the names of the files uploaded by the visitor).The share and any associated file resources will not be deleted by this.   **Notes**:  - Use the [GET /form/entries/{formId}](#operation/getFormMessageById) to list the submissions and obtain the ID of the entry you want to delete - You must have the [DeleteFormData permission](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) in order to use this operation - It is not possible to un-delete data that is removed in this way 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    FormApi apiInstance = new FormApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call. 
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    Long id = 56L; // Long | ID of the entry to be deleted data for
    try {
      EmptyResponse result = apiInstance.deleteFormMessageById(evApiKey, evAccessToken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormApi#deleteFormMessageById");
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
| **evApiKey** | **String**| API Key required to make the API call.  | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **id** | **Long**| ID of the entry to be deleted data for | |

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
| **200** | Successful operation |  -  |

<a id="getFormById"></a>
# **getFormById**
> FormResponse getFormById(id, evApiKey, evAccessToken, include)

Get receive folder form by Id

Returns the [file upload form](/docs/account/05-file-sharing/05-form-builder) assigned to a [receive folder](/docs/account/05-file-sharing/04-receive-folders). The form details will return all the input fields and their settings.   Use the &#x60;include&#x60; parameter (with the value **share**) to also retrieve the details of the associated receive folder.   **Note**  If you prefer to find a form by its shareHash, you can use the [GET /forms](#operation/getFormByShareHash) endpoint instead.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    FormApi apiInstance = new FormApi(defaultClient);
    Integer id = 56; // Integer | Form unique ID number.
    String evApiKey = "evApiKey_example"; // String | API key required to make the API call.
    String evAccessToken = "evAccessToken_example"; // String | Access Token required to make the API call.
    String include = "share"; // String | Enter \"**share**\" to get information about associated receive folder.
    try {
      FormResponse result = apiInstance.getFormById(id, evApiKey, evAccessToken, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormApi#getFormById");
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
| **id** | **Integer**| Form unique ID number. | |
| **evApiKey** | **String**| API key required to make the API call. | |
| **evAccessToken** | **String**| Access Token required to make the API call. | |
| **include** | **String**| Enter \&quot;**share**\&quot; to get information about associated receive folder. | [optional] |

### Return type

[**FormResponse**](FormResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getFormByShareHash"></a>
# **getFormByShareHash**
> FormResponse getFormByShareHash(evApiKey, evAccessToken, shareHash, include)

Get receive folder form settings

Get the information for the [file upload form](/docs/account/05-file-sharing/05-form-builder) assigned to a [receive folder](/docs/account/05-file-sharing/04-receive-folders) by its shareHash. The form details will return all the input field settings and the CSS for the form.  Use the &#x60;include&#x60; parameter (with the value **share**) to also get the details of the associated receive folder.  **Note**  - If you prefer to find a form by its ID, you can use the [GET /forms/{id}](#operation/getFormById) endpoint instead.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    FormApi apiInstance = new FormApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API key required to make the API call.
    String evAccessToken = "evAccessToken_example"; // String | Access Token required to make the API call.
    String shareHash = "shareHash_example"; // String | Share hash to retrieve the form for.
    String include = "share"; // String | Related record types to include in the response. Valid option is **share**
    try {
      FormResponse result = apiInstance.getFormByShareHash(evApiKey, evAccessToken, shareHash, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormApi#getFormByShareHash");
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
| **evApiKey** | **String**| API key required to make the API call. | |
| **evAccessToken** | **String**| Access Token required to make the API call. | |
| **shareHash** | **String**| Share hash to retrieve the form for. | |
| **include** | **String**| Related record types to include in the response. Valid option is **share** | [optional] [enum: share] |

### Return type

[**FormResponse**](FormResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getFormEntries"></a>
# **getFormEntries**
> FormEntryResponse getFormEntries(evApiKey, evAccessToken, id, limit, offset)

Get form data entries for a receive

Returns the form data entries for a specific form for a receive. Optional parameters can be included in the call to manage larger data sets. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    FormApi apiInstance = new FormApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call. 
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    Integer id = 56; // Integer | ID of the form to retrieve entries for.
    Integer limit = 10; // Integer | Limit of records to be returned (for pagination)
    Integer offset = 100; // Integer | Current offset of records (for pagination)
    try {
      FormEntryResponse result = apiInstance.getFormEntries(evApiKey, evAccessToken, id, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormApi#getFormEntries");
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
| **evApiKey** | **String**| API Key required to make the API call.  | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **id** | **Integer**| ID of the form to retrieve entries for. | |
| **limit** | **Integer**| Limit of records to be returned (for pagination) | [optional] |
| **offset** | **Integer**| Current offset of records (for pagination) | [optional] |

### Return type

[**FormEntryResponse**](FormEntryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateFormById"></a>
# **updateFormById**
> FormResponse updateFormById(id, evApiKey, evAccessToken, updateFormByIdRequestBody)

Updates a form with given parameters

Add, update, or delete a form&#39;s parameters. This will alter how your users/customers will see and interact with the form when sending you files.   **Notes**  *This call will **replace** your current form in its entirety.* If you want to keep any existing elements unchanged, be sure to submit the call with an element&#39;s current settings to preserve them.                          

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    FormApi apiInstance = new FormApi(defaultClient);
    Integer id = 56; // Integer | Form unique ID number.
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    UpdateFormByIdRequestBody updateFormByIdRequestBody = new UpdateFormByIdRequestBody(); // UpdateFormByIdRequestBody | 
    try {
      FormResponse result = apiInstance.updateFormById(id, evApiKey, evAccessToken, updateFormByIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormApi#updateFormById");
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
| **id** | **Integer**| Form unique ID number. | |
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **updateFormByIdRequestBody** | [**UpdateFormByIdRequestBody**](UpdateFormByIdRequestBody.md)|  | [optional] |

### Return type

[**FormResponse**](FormResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

