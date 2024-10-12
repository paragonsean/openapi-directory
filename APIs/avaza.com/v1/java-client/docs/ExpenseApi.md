# ExpenseApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expenseApproval**](ExpenseApi.md#expenseApproval) | **POST** /api/ExpenseApproval/Submit | Submit Expenses for Approval. |
| [**expenseAttachment**](ExpenseApi.md#expenseAttachment) | **POST** /api/Expense/Attachment |  |
| [**expenseDelete**](ExpenseApi.md#expenseDelete) | **DELETE** /api/Expense | Delete a Timesheet Entry |
| [**expenseGet**](ExpenseApi.md#expenseGet) | **GET** /api/Expense | Gets list of Expenses |
| [**expenseGetByID**](ExpenseApi.md#expenseGetByID) | **GET** /api/Expense/{id} | Gets an Expense Entry by Expense ID |
| [**expensePost**](ExpenseApi.md#expensePost) | **POST** /api/Expense | Create an Expense |
| [**expensePut**](ExpenseApi.md#expensePut) | **PUT** /api/Expense | Update an Expense |


<a id="expenseApproval"></a>
# **expenseApproval**
> Object expenseApproval(expenseIDs, userID, sendNotifications)

Submit Expenses for Approval.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ExpenseApi apiInstance = new ExpenseApi(defaultClient);
    List<Long> expenseIDs = Arrays.asList(); // List<Long> | A collection of ExpenseID's that should be submitted for approval. If not provided, submits all verified expenses for approval.
    Integer userID = 56; // Integer | The user to submit the Expenses for. Defaults to current user. Only allowed to be different from the current user when the current user has rights to Impersonate other users.
    Boolean sendNotifications = true; // Boolean | Send email alerts to expense approvers. Defaults to true
    try {
      Object result = apiInstance.expenseApproval(expenseIDs, userID, sendNotifications);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseApi#expenseApproval");
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
| **expenseIDs** | [**List&lt;Long&gt;**](Long.md)| A collection of ExpenseID&#39;s that should be submitted for approval. If not provided, submits all verified expenses for approval. | |
| **userID** | **Integer**| The user to submit the Expenses for. Defaults to current user. Only allowed to be different from the current user when the current user has rights to Impersonate other users. | [optional] |
| **sendNotifications** | **Boolean**| Send email alerts to expense approvers. Defaults to true | [optional] |

### Return type

**Object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="expenseAttachment"></a>
# **expenseAttachment**
> ExpenseAttachmentUploadResult expenseAttachment(expenseAttachmentRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ExpenseApi apiInstance = new ExpenseApi(defaultClient);
    ExpenseAttachmentRequest expenseAttachmentRequest = new ExpenseAttachmentRequest(); // ExpenseAttachmentRequest | 
    try {
      ExpenseAttachmentUploadResult result = apiInstance.expenseAttachment(expenseAttachmentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseApi#expenseAttachment");
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
| **expenseAttachmentRequest** | [**ExpenseAttachmentRequest**](ExpenseAttachmentRequest.md)|  | |

### Return type

[**ExpenseAttachmentUploadResult**](ExpenseAttachmentUploadResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="expenseDelete"></a>
# **expenseDelete**
> ExpenseDeleteResultSet expenseDelete(expenseIDs)

Delete a Timesheet Entry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ExpenseApi apiInstance = new ExpenseApi(defaultClient);
    List<Long> expenseIDs = Arrays.asList(); // List<Long> | A collection of ExpenseIDs to delete
    try {
      ExpenseDeleteResultSet result = apiInstance.expenseDelete(expenseIDs);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseApi#expenseDelete");
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
| **expenseIDs** | [**List&lt;Long&gt;**](Long.md)| A collection of ExpenseIDs to delete | |

### Return type

[**ExpenseDeleteResultSet**](ExpenseDeleteResultSet.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="expenseGet"></a>
# **expenseGet**
> ExpenseList expenseGet(updatedAfter, expenseDateFrom, expenseDateTo, userEmail, userID, categoryName, customerID, projectID, isChargeable, isInvoiced, expenseReimbursementIDFK, expensePaymentMethodIDFK, expenseApprovalStatusCode, search, pageSize, pageNumber, sort)

Gets list of Expenses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ExpenseApi apiInstance = new ExpenseApi(defaultClient);
    OffsetDateTime updatedAfter = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime expenseDateFrom = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime expenseDateTo = OffsetDateTime.now(); // OffsetDateTime | 
    String userEmail = "userEmail_example"; // String | 
    Integer userID = 56; // Integer | 
    String categoryName = "categoryName_example"; // String | 
    Integer customerID = 56; // Integer | 
    Integer projectID = 56; // Integer | 
    Boolean isChargeable = true; // Boolean | 
    Boolean isInvoiced = true; // Boolean | 
    Long expenseReimbursementIDFK = 56L; // Long | 
    Integer expensePaymentMethodIDFK = 56; // Integer | 
    String expenseApprovalStatusCode = "expenseApprovalStatusCode_example"; // String | 
    String search = "search_example"; // String | 
    Integer pageSize = 56; // Integer | Number of items per page (max 1000)
    Integer pageNumber = 56; // Integer | Page to display. Starts from 1.
    String sort = "sort_example"; // String | 
    try {
      ExpenseList result = apiInstance.expenseGet(updatedAfter, expenseDateFrom, expenseDateTo, userEmail, userID, categoryName, customerID, projectID, isChargeable, isInvoiced, expenseReimbursementIDFK, expensePaymentMethodIDFK, expenseApprovalStatusCode, search, pageSize, pageNumber, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseApi#expenseGet");
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
| **updatedAfter** | **OffsetDateTime**|  | [optional] |
| **expenseDateFrom** | **OffsetDateTime**|  | [optional] |
| **expenseDateTo** | **OffsetDateTime**|  | [optional] |
| **userEmail** | **String**|  | [optional] |
| **userID** | **Integer**|  | [optional] |
| **categoryName** | **String**|  | [optional] |
| **customerID** | **Integer**|  | [optional] |
| **projectID** | **Integer**|  | [optional] |
| **isChargeable** | **Boolean**|  | [optional] |
| **isInvoiced** | **Boolean**|  | [optional] |
| **expenseReimbursementIDFK** | **Long**|  | [optional] |
| **expensePaymentMethodIDFK** | **Integer**|  | [optional] |
| **expenseApprovalStatusCode** | **String**|  | [optional] |
| **search** | **String**|  | [optional] |
| **pageSize** | **Integer**| Number of items per page (max 1000) | [optional] |
| **pageNumber** | **Integer**| Page to display. Starts from 1. | [optional] |
| **sort** | **String**|  | [optional] |

### Return type

[**ExpenseList**](ExpenseList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="expenseGetByID"></a>
# **expenseGetByID**
> ExpenseDetails expenseGetByID(id)

Gets an Expense Entry by Expense ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ExpenseApi apiInstance = new ExpenseApi(defaultClient);
    Long id = 56L; // Long | Expense ID number
    try {
      ExpenseDetails result = apiInstance.expenseGetByID(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseApi#expenseGetByID");
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
| **id** | **Long**| Expense ID number | |

### Return type

[**ExpenseDetails**](ExpenseDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="expensePost"></a>
# **expensePost**
> ExpenseDetails expensePost(model)

Create an Expense

Create an Expense

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ExpenseApi apiInstance = new ExpenseApi(defaultClient);
    NewExpense model = new NewExpense(); // NewExpense | 
    try {
      ExpenseDetails result = apiInstance.expensePost(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseApi#expensePost");
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
| **model** | [**NewExpense**](NewExpense.md)|  | |

### Return type

[**ExpenseDetails**](ExpenseDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="expensePut"></a>
# **expensePut**
> ExpenseDetails expensePut(model)

Update an Expense

Update an Expense

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ExpenseApi apiInstance = new ExpenseApi(defaultClient);
    UpdateExpense model = new UpdateExpense(); // UpdateExpense | 
    try {
      ExpenseDetails result = apiInstance.expensePut(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseApi#expensePut");
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
| **model** | [**UpdateExpense**](UpdateExpense.md)|  | |

### Return type

[**ExpenseDetails**](ExpenseDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

