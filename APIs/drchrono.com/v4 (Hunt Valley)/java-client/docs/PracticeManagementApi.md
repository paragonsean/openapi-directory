# PracticeManagementApi

All URIs are relative to *https://app.drchrono.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**inventoryCategoriesList**](PracticeManagementApi.md#inventoryCategoriesList) | **GET** /api/inventory_categories |  |
| [**inventoryCategoriesRead**](PracticeManagementApi.md#inventoryCategoriesRead) | **GET** /api/inventory_categories/{id} |  |
| [**inventoryVaccinesCreate**](PracticeManagementApi.md#inventoryVaccinesCreate) | **POST** /api/inventory_vaccines |  |
| [**inventoryVaccinesList**](PracticeManagementApi.md#inventoryVaccinesList) | **GET** /api/inventory_vaccines |  |
| [**inventoryVaccinesRead**](PracticeManagementApi.md#inventoryVaccinesRead) | **GET** /api/inventory_vaccines/{id} |  |
| [**messagesCreate**](PracticeManagementApi.md#messagesCreate) | **POST** /api/messages |  |
| [**messagesDelete**](PracticeManagementApi.md#messagesDelete) | **DELETE** /api/messages/{id} |  |
| [**messagesList**](PracticeManagementApi.md#messagesList) | **GET** /api/messages |  |
| [**messagesPartialUpdate**](PracticeManagementApi.md#messagesPartialUpdate) | **PATCH** /api/messages/{id} |  |
| [**messagesRead**](PracticeManagementApi.md#messagesRead) | **GET** /api/messages/{id} |  |
| [**messagesUpdate**](PracticeManagementApi.md#messagesUpdate) | **PUT** /api/messages/{id} |  |
| [**officesAddExamRoom**](PracticeManagementApi.md#officesAddExamRoom) | **POST** /api/offices/{id}/add_exam_room |  |
| [**officesList**](PracticeManagementApi.md#officesList) | **GET** /api/offices |  |
| [**officesPartialUpdate**](PracticeManagementApi.md#officesPartialUpdate) | **PATCH** /api/offices/{id} |  |
| [**officesRead**](PracticeManagementApi.md#officesRead) | **GET** /api/offices/{id} |  |
| [**officesUpdate**](PracticeManagementApi.md#officesUpdate) | **PUT** /api/offices/{id} |  |
| [**taskCategoriesCreate**](PracticeManagementApi.md#taskCategoriesCreate) | **POST** /api/task_categories |  |
| [**taskCategoriesList**](PracticeManagementApi.md#taskCategoriesList) | **GET** /api/task_categories |  |
| [**taskCategoriesPartialUpdate**](PracticeManagementApi.md#taskCategoriesPartialUpdate) | **PATCH** /api/task_categories/{id} |  |
| [**taskCategoriesRead**](PracticeManagementApi.md#taskCategoriesRead) | **GET** /api/task_categories/{id} |  |
| [**taskCategoriesUpdate**](PracticeManagementApi.md#taskCategoriesUpdate) | **PUT** /api/task_categories/{id} |  |
| [**taskNotesCreate**](PracticeManagementApi.md#taskNotesCreate) | **POST** /api/task_notes |  |
| [**taskNotesList**](PracticeManagementApi.md#taskNotesList) | **GET** /api/task_notes |  |
| [**taskNotesPartialUpdate**](PracticeManagementApi.md#taskNotesPartialUpdate) | **PATCH** /api/task_notes/{id} |  |
| [**taskNotesRead**](PracticeManagementApi.md#taskNotesRead) | **GET** /api/task_notes/{id} |  |
| [**taskNotesUpdate**](PracticeManagementApi.md#taskNotesUpdate) | **PUT** /api/task_notes/{id} |  |
| [**taskStatusesCreate**](PracticeManagementApi.md#taskStatusesCreate) | **POST** /api/task_statuses |  |
| [**taskStatusesList**](PracticeManagementApi.md#taskStatusesList) | **GET** /api/task_statuses |  |
| [**taskStatusesPartialUpdate**](PracticeManagementApi.md#taskStatusesPartialUpdate) | **PATCH** /api/task_statuses/{id} |  |
| [**taskStatusesRead**](PracticeManagementApi.md#taskStatusesRead) | **GET** /api/task_statuses/{id} |  |
| [**taskStatusesUpdate**](PracticeManagementApi.md#taskStatusesUpdate) | **PUT** /api/task_statuses/{id} |  |
| [**taskTemplatesCreate**](PracticeManagementApi.md#taskTemplatesCreate) | **POST** /api/task_templates |  |
| [**taskTemplatesList**](PracticeManagementApi.md#taskTemplatesList) | **GET** /api/task_templates |  |
| [**taskTemplatesPartialUpdate**](PracticeManagementApi.md#taskTemplatesPartialUpdate) | **PATCH** /api/task_templates/{id} |  |
| [**taskTemplatesRead**](PracticeManagementApi.md#taskTemplatesRead) | **GET** /api/task_templates/{id} |  |
| [**taskTemplatesUpdate**](PracticeManagementApi.md#taskTemplatesUpdate) | **PUT** /api/task_templates/{id} |  |
| [**tasksCreate**](PracticeManagementApi.md#tasksCreate) | **POST** /api/tasks |  |
| [**tasksList**](PracticeManagementApi.md#tasksList) | **GET** /api/tasks |  |
| [**tasksPartialUpdate**](PracticeManagementApi.md#tasksPartialUpdate) | **PATCH** /api/tasks/{id} |  |
| [**tasksRead**](PracticeManagementApi.md#tasksRead) | **GET** /api/tasks/{id} |  |
| [**tasksUpdate**](PracticeManagementApi.md#tasksUpdate) | **PUT** /api/tasks/{id} |  |


<a id="inventoryCategoriesList"></a>
# **inventoryCategoriesList**
> InventoryCategoriesList200Response inventoryCategoriesList(cursor, pageSize, since, doctor)



Retrieve or search inventory categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer doctor = 56; // Integer | 
    try {
      InventoryCategoriesList200Response result = apiInstance.inventoryCategoriesList(cursor, pageSize, since, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#inventoryCategoriesList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**InventoryCategoriesList200Response**](InventoryCategoriesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="inventoryCategoriesRead"></a>
# **inventoryCategoriesRead**
> InventoryCategory inventoryCategoriesRead(id, since, doctor)



Retrieve an existing inventory category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    String since = "since_example"; // String | 
    Integer doctor = 56; // Integer | 
    try {
      InventoryCategory result = apiInstance.inventoryCategoriesRead(id, since, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#inventoryCategoriesRead");
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
| **id** | **String**|  | |
| **since** | **String**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**InventoryCategory**](InventoryCategory.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="inventoryVaccinesCreate"></a>
# **inventoryVaccinesCreate**
> InventoryVaccine inventoryVaccinesCreate(status, cvxCode, since, doctor)



Create vaccine inventory

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String status = "status_example"; // String | 
    String cvxCode = "cvxCode_example"; // String | 
    String since = "since_example"; // String | 
    Integer doctor = 56; // Integer | 
    try {
      InventoryVaccine result = apiInstance.inventoryVaccinesCreate(status, cvxCode, since, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#inventoryVaccinesCreate");
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
| **status** | **String**|  | [optional] |
| **cvxCode** | **String**|  | [optional] |
| **since** | **String**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**InventoryVaccine**](InventoryVaccine.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="inventoryVaccinesList"></a>
# **inventoryVaccinesList**
> InventoryVaccinesList200Response inventoryVaccinesList(cursor, pageSize, status, cvxCode, since, doctor)



Retrieve or search vaccine inventories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    String status = "status_example"; // String | 
    String cvxCode = "cvxCode_example"; // String | 
    String since = "since_example"; // String | 
    Integer doctor = 56; // Integer | 
    try {
      InventoryVaccinesList200Response result = apiInstance.inventoryVaccinesList(cursor, pageSize, status, cvxCode, since, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#inventoryVaccinesList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **status** | **String**|  | [optional] |
| **cvxCode** | **String**|  | [optional] |
| **since** | **String**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**InventoryVaccinesList200Response**](InventoryVaccinesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="inventoryVaccinesRead"></a>
# **inventoryVaccinesRead**
> InventoryVaccine inventoryVaccinesRead(id, status, cvxCode, since, doctor)



Retrieve an existing vaccine inventory

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    String status = "status_example"; // String | 
    String cvxCode = "cvxCode_example"; // String | 
    String since = "since_example"; // String | 
    Integer doctor = 56; // Integer | 
    try {
      InventoryVaccine result = apiInstance.inventoryVaccinesRead(id, status, cvxCode, since, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#inventoryVaccinesRead");
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
| **id** | **String**|  | |
| **status** | **String**|  | [optional] |
| **cvxCode** | **String**|  | [optional] |
| **since** | **String**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**InventoryVaccine**](InventoryVaccine.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="messagesCreate"></a>
# **messagesCreate**
> DoctorMessage messagesCreate(patient, doctor, responsibleUser, updatedSince, receivedSince, owner, type)



Create messages in doctor&#39;s message center

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    Integer patient = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    Integer responsibleUser = 56; // Integer | 
    String updatedSince = "updatedSince_example"; // String | 
    String receivedSince = "receivedSince_example"; // String | 
    Integer owner = 56; // Integer | 
    String type = "type_example"; // String | 
    try {
      DoctorMessage result = apiInstance.messagesCreate(patient, doctor, responsibleUser, updatedSince, receivedSince, owner, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#messagesCreate");
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
| **patient** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |
| **responsibleUser** | **Integer**|  | [optional] |
| **updatedSince** | **String**|  | [optional] |
| **receivedSince** | **String**|  | [optional] |
| **owner** | **Integer**|  | [optional] |
| **type** | **String**|  | [optional] |

### Return type

[**DoctorMessage**](DoctorMessage.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="messagesDelete"></a>
# **messagesDelete**
> messagesDelete(id, patient, doctor, responsibleUser, updatedSince, receivedSince, owner, type)



Delete an existing message in doctor&#39;s message center

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    Integer responsibleUser = 56; // Integer | 
    String updatedSince = "updatedSince_example"; // String | 
    String receivedSince = "receivedSince_example"; // String | 
    Integer owner = 56; // Integer | 
    String type = "type_example"; // String | 
    try {
      apiInstance.messagesDelete(id, patient, doctor, responsibleUser, updatedSince, receivedSince, owner, type);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#messagesDelete");
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
| **id** | **String**|  | |
| **patient** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |
| **responsibleUser** | **Integer**|  | [optional] |
| **updatedSince** | **String**|  | [optional] |
| **receivedSince** | **String**|  | [optional] |
| **owner** | **Integer**|  | [optional] |
| **type** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="messagesList"></a>
# **messagesList**
> MessagesList200Response messagesList(cursor, pageSize, patient, doctor, responsibleUser, updatedSince, receivedSince, owner, type)



Retrieve or search messages in doctor&#39;s message center

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    Integer patient = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    Integer responsibleUser = 56; // Integer | 
    String updatedSince = "updatedSince_example"; // String | 
    String receivedSince = "receivedSince_example"; // String | 
    Integer owner = 56; // Integer | 
    String type = "type_example"; // String | 
    try {
      MessagesList200Response result = apiInstance.messagesList(cursor, pageSize, patient, doctor, responsibleUser, updatedSince, receivedSince, owner, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#messagesList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **patient** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |
| **responsibleUser** | **Integer**|  | [optional] |
| **updatedSince** | **String**|  | [optional] |
| **receivedSince** | **String**|  | [optional] |
| **owner** | **Integer**|  | [optional] |
| **type** | **String**|  | [optional] |

### Return type

[**MessagesList200Response**](MessagesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="messagesPartialUpdate"></a>
# **messagesPartialUpdate**
> messagesPartialUpdate(id, patient, doctor, responsibleUser, updatedSince, receivedSince, owner, type)



Update an existing message in doctor&#39;s message center

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    Integer responsibleUser = 56; // Integer | 
    String updatedSince = "updatedSince_example"; // String | 
    String receivedSince = "receivedSince_example"; // String | 
    Integer owner = 56; // Integer | 
    String type = "type_example"; // String | 
    try {
      apiInstance.messagesPartialUpdate(id, patient, doctor, responsibleUser, updatedSince, receivedSince, owner, type);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#messagesPartialUpdate");
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
| **id** | **String**|  | |
| **patient** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |
| **responsibleUser** | **Integer**|  | [optional] |
| **updatedSince** | **String**|  | [optional] |
| **receivedSince** | **String**|  | [optional] |
| **owner** | **Integer**|  | [optional] |
| **type** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="messagesRead"></a>
# **messagesRead**
> DoctorMessage messagesRead(id, patient, doctor, responsibleUser, updatedSince, receivedSince, owner, type)



Retrieve an existing message in doctor&#39;s message center

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    Integer responsibleUser = 56; // Integer | 
    String updatedSince = "updatedSince_example"; // String | 
    String receivedSince = "receivedSince_example"; // String | 
    Integer owner = 56; // Integer | 
    String type = "type_example"; // String | 
    try {
      DoctorMessage result = apiInstance.messagesRead(id, patient, doctor, responsibleUser, updatedSince, receivedSince, owner, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#messagesRead");
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
| **id** | **String**|  | |
| **patient** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |
| **responsibleUser** | **Integer**|  | [optional] |
| **updatedSince** | **String**|  | [optional] |
| **receivedSince** | **String**|  | [optional] |
| **owner** | **Integer**|  | [optional] |
| **type** | **String**|  | [optional] |

### Return type

[**DoctorMessage**](DoctorMessage.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="messagesUpdate"></a>
# **messagesUpdate**
> messagesUpdate(id, patient, doctor, responsibleUser, updatedSince, receivedSince, owner, type)



Update an existing message in doctor&#39;s message center

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    Integer responsibleUser = 56; // Integer | 
    String updatedSince = "updatedSince_example"; // String | 
    String receivedSince = "receivedSince_example"; // String | 
    Integer owner = 56; // Integer | 
    String type = "type_example"; // String | 
    try {
      apiInstance.messagesUpdate(id, patient, doctor, responsibleUser, updatedSince, receivedSince, owner, type);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#messagesUpdate");
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
| **id** | **String**|  | |
| **patient** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |
| **responsibleUser** | **Integer**|  | [optional] |
| **updatedSince** | **String**|  | [optional] |
| **receivedSince** | **String**|  | [optional] |
| **owner** | **Integer**|  | [optional] |
| **type** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="officesAddExamRoom"></a>
# **officesAddExamRoom**
> Office officesAddExamRoom(id, doctor)



Add an exam room to the office

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    Integer doctor = 56; // Integer | 
    try {
      Office result = apiInstance.officesAddExamRoom(id, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#officesAddExamRoom");
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
| **id** | **String**|  | |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**Office**](Office.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="officesList"></a>
# **officesList**
> OfficesList200Response officesList(cursor, pageSize, doctor)



Retrieve or search offices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    try {
      OfficesList200Response result = apiInstance.officesList(cursor, pageSize, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#officesList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**OfficesList200Response**](OfficesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="officesPartialUpdate"></a>
# **officesPartialUpdate**
> officesPartialUpdate(id, doctor)



Update an existing office

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    Integer doctor = 56; // Integer | 
    try {
      apiInstance.officesPartialUpdate(id, doctor);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#officesPartialUpdate");
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
| **id** | **String**|  | |
| **doctor** | **Integer**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="officesRead"></a>
# **officesRead**
> Office officesRead(id, doctor)



Retrieve an existing office

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    Integer doctor = 56; // Integer | 
    try {
      Office result = apiInstance.officesRead(id, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#officesRead");
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
| **id** | **String**|  | |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**Office**](Office.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="officesUpdate"></a>
# **officesUpdate**
> officesUpdate(id, doctor)



Update an existing office

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    Integer doctor = 56; // Integer | 
    try {
      apiInstance.officesUpdate(id, doctor);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#officesUpdate");
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
| **id** | **String**|  | |
| **doctor** | **Integer**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskCategoriesCreate"></a>
# **taskCategoriesCreate**
> TaskCategory taskCategoriesCreate(since)



Create a task category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String since = "since_example"; // String | 
    try {
      TaskCategory result = apiInstance.taskCategoriesCreate(since);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskCategoriesCreate");
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
| **since** | **String**|  | [optional] |

### Return type

[**TaskCategory**](TaskCategory.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskCategoriesList"></a>
# **taskCategoriesList**
> TaskCategoriesList200Response taskCategoriesList(cursor, pageSize, since)



Retrieve or search task categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    String since = "since_example"; // String | 
    try {
      TaskCategoriesList200Response result = apiInstance.taskCategoriesList(cursor, pageSize, since);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskCategoriesList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |

### Return type

[**TaskCategoriesList200Response**](TaskCategoriesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskCategoriesPartialUpdate"></a>
# **taskCategoriesPartialUpdate**
> taskCategoriesPartialUpdate(id, since)



Update an existing task category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    String since = "since_example"; // String | 
    try {
      apiInstance.taskCategoriesPartialUpdate(id, since);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskCategoriesPartialUpdate");
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
| **id** | **String**|  | |
| **since** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskCategoriesRead"></a>
# **taskCategoriesRead**
> TaskCategory taskCategoriesRead(id, since)



Retrieve an existing task category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    String since = "since_example"; // String | 
    try {
      TaskCategory result = apiInstance.taskCategoriesRead(id, since);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskCategoriesRead");
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
| **id** | **String**|  | |
| **since** | **String**|  | [optional] |

### Return type

[**TaskCategory**](TaskCategory.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskCategoriesUpdate"></a>
# **taskCategoriesUpdate**
> taskCategoriesUpdate(id, since)



Update an existing task category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    String since = "since_example"; // String | 
    try {
      apiInstance.taskCategoriesUpdate(id, since);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskCategoriesUpdate");
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
| **id** | **String**|  | |
| **since** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskNotesCreate"></a>
# **taskNotesCreate**
> TaskNote taskNotesCreate(task, since)



Create a task note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    Integer task = 56; // Integer | 
    String since = "since_example"; // String | 
    try {
      TaskNote result = apiInstance.taskNotesCreate(task, since);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskNotesCreate");
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
| **task** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |

### Return type

[**TaskNote**](TaskNote.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskNotesList"></a>
# **taskNotesList**
> TaskNotesList200Response taskNotesList(cursor, pageSize, task, since)



Retrieve or search task notes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    Integer task = 56; // Integer | 
    String since = "since_example"; // String | 
    try {
      TaskNotesList200Response result = apiInstance.taskNotesList(cursor, pageSize, task, since);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskNotesList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **task** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |

### Return type

[**TaskNotesList200Response**](TaskNotesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskNotesPartialUpdate"></a>
# **taskNotesPartialUpdate**
> taskNotesPartialUpdate(id, task, since)



Update an existing task note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    Integer task = 56; // Integer | 
    String since = "since_example"; // String | 
    try {
      apiInstance.taskNotesPartialUpdate(id, task, since);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskNotesPartialUpdate");
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
| **id** | **String**|  | |
| **task** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskNotesRead"></a>
# **taskNotesRead**
> TaskNote taskNotesRead(id, task, since)



Retrieve an existing task note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    Integer task = 56; // Integer | 
    String since = "since_example"; // String | 
    try {
      TaskNote result = apiInstance.taskNotesRead(id, task, since);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskNotesRead");
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
| **id** | **String**|  | |
| **task** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |

### Return type

[**TaskNote**](TaskNote.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskNotesUpdate"></a>
# **taskNotesUpdate**
> taskNotesUpdate(id, task, since)



Update an existing task note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    Integer task = 56; // Integer | 
    String since = "since_example"; // String | 
    try {
      apiInstance.taskNotesUpdate(id, task, since);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskNotesUpdate");
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
| **id** | **String**|  | |
| **task** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskStatusesCreate"></a>
# **taskStatusesCreate**
> TaskStatus taskStatusesCreate(since)



Create a task status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String since = "since_example"; // String | 
    try {
      TaskStatus result = apiInstance.taskStatusesCreate(since);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskStatusesCreate");
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
| **since** | **String**|  | [optional] |

### Return type

[**TaskStatus**](TaskStatus.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskStatusesList"></a>
# **taskStatusesList**
> TaskStatusesList200Response taskStatusesList(cursor, pageSize, since)



Retrieve or search task statuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    String since = "since_example"; // String | 
    try {
      TaskStatusesList200Response result = apiInstance.taskStatusesList(cursor, pageSize, since);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskStatusesList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |

### Return type

[**TaskStatusesList200Response**](TaskStatusesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskStatusesPartialUpdate"></a>
# **taskStatusesPartialUpdate**
> taskStatusesPartialUpdate(id, since)



Update an existing task status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    String since = "since_example"; // String | 
    try {
      apiInstance.taskStatusesPartialUpdate(id, since);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskStatusesPartialUpdate");
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
| **id** | **String**|  | |
| **since** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskStatusesRead"></a>
# **taskStatusesRead**
> TaskStatus taskStatusesRead(id, since)



Retrieve an existing task status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    String since = "since_example"; // String | 
    try {
      TaskStatus result = apiInstance.taskStatusesRead(id, since);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskStatusesRead");
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
| **id** | **String**|  | |
| **since** | **String**|  | [optional] |

### Return type

[**TaskStatus**](TaskStatus.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskStatusesUpdate"></a>
# **taskStatusesUpdate**
> taskStatusesUpdate(id, since)



Update an existing task status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    String since = "since_example"; // String | 
    try {
      apiInstance.taskStatusesUpdate(id, since);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskStatusesUpdate");
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
| **id** | **String**|  | |
| **since** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskTemplatesCreate"></a>
# **taskTemplatesCreate**
> TaskTemplate taskTemplatesCreate(assigneeUser, status, assigneeGroup, since, category)



Create a task template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    Integer assigneeUser = 56; // Integer | 
    Integer status = 56; // Integer | 
    Integer assigneeGroup = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer category = 56; // Integer | 
    try {
      TaskTemplate result = apiInstance.taskTemplatesCreate(assigneeUser, status, assigneeGroup, since, category);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskTemplatesCreate");
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
| **assigneeUser** | **Integer**|  | [optional] |
| **status** | **Integer**|  | [optional] |
| **assigneeGroup** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **category** | **Integer**|  | [optional] |

### Return type

[**TaskTemplate**](TaskTemplate.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskTemplatesList"></a>
# **taskTemplatesList**
> TaskTemplatesList200Response taskTemplatesList(cursor, pageSize, assigneeUser, status, assigneeGroup, since, category)



Retrieve or search task templates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    Integer assigneeUser = 56; // Integer | 
    Integer status = 56; // Integer | 
    Integer assigneeGroup = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer category = 56; // Integer | 
    try {
      TaskTemplatesList200Response result = apiInstance.taskTemplatesList(cursor, pageSize, assigneeUser, status, assigneeGroup, since, category);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskTemplatesList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **assigneeUser** | **Integer**|  | [optional] |
| **status** | **Integer**|  | [optional] |
| **assigneeGroup** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **category** | **Integer**|  | [optional] |

### Return type

[**TaskTemplatesList200Response**](TaskTemplatesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskTemplatesPartialUpdate"></a>
# **taskTemplatesPartialUpdate**
> taskTemplatesPartialUpdate(id, assigneeUser, status, assigneeGroup, since, category)



Update an existing task template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    Integer assigneeUser = 56; // Integer | 
    Integer status = 56; // Integer | 
    Integer assigneeGroup = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer category = 56; // Integer | 
    try {
      apiInstance.taskTemplatesPartialUpdate(id, assigneeUser, status, assigneeGroup, since, category);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskTemplatesPartialUpdate");
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
| **id** | **String**|  | |
| **assigneeUser** | **Integer**|  | [optional] |
| **status** | **Integer**|  | [optional] |
| **assigneeGroup** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **category** | **Integer**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskTemplatesRead"></a>
# **taskTemplatesRead**
> TaskTemplate taskTemplatesRead(id, assigneeUser, status, assigneeGroup, since, category)



Retrieve an existing task template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    Integer assigneeUser = 56; // Integer | 
    Integer status = 56; // Integer | 
    Integer assigneeGroup = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer category = 56; // Integer | 
    try {
      TaskTemplate result = apiInstance.taskTemplatesRead(id, assigneeUser, status, assigneeGroup, since, category);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskTemplatesRead");
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
| **id** | **String**|  | |
| **assigneeUser** | **Integer**|  | [optional] |
| **status** | **Integer**|  | [optional] |
| **assigneeGroup** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **category** | **Integer**|  | [optional] |

### Return type

[**TaskTemplate**](TaskTemplate.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="taskTemplatesUpdate"></a>
# **taskTemplatesUpdate**
> taskTemplatesUpdate(id, assigneeUser, status, assigneeGroup, since, category)



Update an existing task template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    Integer assigneeUser = 56; // Integer | 
    Integer status = 56; // Integer | 
    Integer assigneeGroup = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer category = 56; // Integer | 
    try {
      apiInstance.taskTemplatesUpdate(id, assigneeUser, status, assigneeGroup, since, category);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#taskTemplatesUpdate");
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
| **id** | **String**|  | |
| **assigneeUser** | **Integer**|  | [optional] |
| **status** | **Integer**|  | [optional] |
| **assigneeGroup** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **category** | **Integer**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="tasksCreate"></a>
# **tasksCreate**
> Task tasksCreate(status, category, dueAtDate, dueAtUnknown, since, dueAtSince, assigneeUser, assigneeGroup, dueAtRange)



Create a task

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    Integer status = 56; // Integer | 
    Integer category = 56; // Integer | 
    String dueAtDate = "dueAtDate_example"; // String | 
    String dueAtUnknown = "dueAtUnknown_example"; // String | 
    String since = "since_example"; // String | 
    String dueAtSince = "dueAtSince_example"; // String | 
    Integer assigneeUser = 56; // Integer | 
    Integer assigneeGroup = 56; // Integer | 
    String dueAtRange = "dueAtRange_example"; // String | 
    try {
      Task result = apiInstance.tasksCreate(status, category, dueAtDate, dueAtUnknown, since, dueAtSince, assigneeUser, assigneeGroup, dueAtRange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#tasksCreate");
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
| **status** | **Integer**|  | [optional] |
| **category** | **Integer**|  | [optional] |
| **dueAtDate** | **String**|  | [optional] |
| **dueAtUnknown** | **String**|  | [optional] |
| **since** | **String**|  | [optional] |
| **dueAtSince** | **String**|  | [optional] |
| **assigneeUser** | **Integer**|  | [optional] |
| **assigneeGroup** | **Integer**|  | [optional] |
| **dueAtRange** | **String**|  | [optional] |

### Return type

[**Task**](Task.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="tasksList"></a>
# **tasksList**
> TasksList200Response tasksList(cursor, pageSize, status, category, dueAtDate, dueAtUnknown, since, dueAtSince, assigneeUser, assigneeGroup, dueAtRange)



Retrieve or search tasks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    Integer status = 56; // Integer | 
    Integer category = 56; // Integer | 
    String dueAtDate = "dueAtDate_example"; // String | 
    String dueAtUnknown = "dueAtUnknown_example"; // String | 
    String since = "since_example"; // String | 
    String dueAtSince = "dueAtSince_example"; // String | 
    Integer assigneeUser = 56; // Integer | 
    Integer assigneeGroup = 56; // Integer | 
    String dueAtRange = "dueAtRange_example"; // String | 
    try {
      TasksList200Response result = apiInstance.tasksList(cursor, pageSize, status, category, dueAtDate, dueAtUnknown, since, dueAtSince, assigneeUser, assigneeGroup, dueAtRange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#tasksList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **status** | **Integer**|  | [optional] |
| **category** | **Integer**|  | [optional] |
| **dueAtDate** | **String**|  | [optional] |
| **dueAtUnknown** | **String**|  | [optional] |
| **since** | **String**|  | [optional] |
| **dueAtSince** | **String**|  | [optional] |
| **assigneeUser** | **Integer**|  | [optional] |
| **assigneeGroup** | **Integer**|  | [optional] |
| **dueAtRange** | **String**|  | [optional] |

### Return type

[**TasksList200Response**](TasksList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="tasksPartialUpdate"></a>
# **tasksPartialUpdate**
> tasksPartialUpdate(id, status, category, dueAtDate, dueAtUnknown, since, dueAtSince, assigneeUser, assigneeGroup, dueAtRange)



Update an existing task

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    Integer status = 56; // Integer | 
    Integer category = 56; // Integer | 
    String dueAtDate = "dueAtDate_example"; // String | 
    String dueAtUnknown = "dueAtUnknown_example"; // String | 
    String since = "since_example"; // String | 
    String dueAtSince = "dueAtSince_example"; // String | 
    Integer assigneeUser = 56; // Integer | 
    Integer assigneeGroup = 56; // Integer | 
    String dueAtRange = "dueAtRange_example"; // String | 
    try {
      apiInstance.tasksPartialUpdate(id, status, category, dueAtDate, dueAtUnknown, since, dueAtSince, assigneeUser, assigneeGroup, dueAtRange);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#tasksPartialUpdate");
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
| **id** | **String**|  | |
| **status** | **Integer**|  | [optional] |
| **category** | **Integer**|  | [optional] |
| **dueAtDate** | **String**|  | [optional] |
| **dueAtUnknown** | **String**|  | [optional] |
| **since** | **String**|  | [optional] |
| **dueAtSince** | **String**|  | [optional] |
| **assigneeUser** | **Integer**|  | [optional] |
| **assigneeGroup** | **Integer**|  | [optional] |
| **dueAtRange** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="tasksRead"></a>
# **tasksRead**
> Task tasksRead(id, status, category, dueAtDate, dueAtUnknown, since, dueAtSince, assigneeUser, assigneeGroup, dueAtRange)



Retrieve an existing task

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    Integer status = 56; // Integer | 
    Integer category = 56; // Integer | 
    String dueAtDate = "dueAtDate_example"; // String | 
    String dueAtUnknown = "dueAtUnknown_example"; // String | 
    String since = "since_example"; // String | 
    String dueAtSince = "dueAtSince_example"; // String | 
    Integer assigneeUser = 56; // Integer | 
    Integer assigneeGroup = 56; // Integer | 
    String dueAtRange = "dueAtRange_example"; // String | 
    try {
      Task result = apiInstance.tasksRead(id, status, category, dueAtDate, dueAtUnknown, since, dueAtSince, assigneeUser, assigneeGroup, dueAtRange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#tasksRead");
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
| **id** | **String**|  | |
| **status** | **Integer**|  | [optional] |
| **category** | **Integer**|  | [optional] |
| **dueAtDate** | **String**|  | [optional] |
| **dueAtUnknown** | **String**|  | [optional] |
| **since** | **String**|  | [optional] |
| **dueAtSince** | **String**|  | [optional] |
| **assigneeUser** | **Integer**|  | [optional] |
| **assigneeGroup** | **Integer**|  | [optional] |
| **dueAtRange** | **String**|  | [optional] |

### Return type

[**Task**](Task.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="tasksUpdate"></a>
# **tasksUpdate**
> tasksUpdate(id, status, category, dueAtDate, dueAtUnknown, since, dueAtSince, assigneeUser, assigneeGroup, dueAtRange)



Update an existing task

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PracticeManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PracticeManagementApi apiInstance = new PracticeManagementApi(defaultClient);
    String id = "id_example"; // String | 
    Integer status = 56; // Integer | 
    Integer category = 56; // Integer | 
    String dueAtDate = "dueAtDate_example"; // String | 
    String dueAtUnknown = "dueAtUnknown_example"; // String | 
    String since = "since_example"; // String | 
    String dueAtSince = "dueAtSince_example"; // String | 
    Integer assigneeUser = 56; // Integer | 
    Integer assigneeGroup = 56; // Integer | 
    String dueAtRange = "dueAtRange_example"; // String | 
    try {
      apiInstance.tasksUpdate(id, status, category, dueAtDate, dueAtUnknown, since, dueAtSince, assigneeUser, assigneeGroup, dueAtRange);
    } catch (ApiException e) {
      System.err.println("Exception when calling PracticeManagementApi#tasksUpdate");
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
| **id** | **String**|  | |
| **status** | **Integer**|  | [optional] |
| **category** | **Integer**|  | [optional] |
| **dueAtDate** | **String**|  | [optional] |
| **dueAtUnknown** | **String**|  | [optional] |
| **since** | **String**|  | [optional] |
| **dueAtSince** | **String**|  | [optional] |
| **assigneeUser** | **Integer**|  | [optional] |
| **assigneeGroup** | **Integer**|  | [optional] |
| **dueAtRange** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

