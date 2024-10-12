# UserContactMethodsApi

All URIs are relative to *https://api.victorops.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPublicV1UserUserContactMethodsDevicesContactIdDelete**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsDevicesContactIdDelete) | **DELETE** /api-public/v1/user/{user}/contact-methods/devices/{contactId} | Delete a contact device for a user |
| [**apiPublicV1UserUserContactMethodsDevicesContactIdGet**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsDevicesContactIdGet) | **GET** /api-public/v1/user/{user}/contact-methods/devices/{contactId} | Get the indicated contact device for a user |
| [**apiPublicV1UserUserContactMethodsDevicesContactIdPut**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsDevicesContactIdPut) | **PUT** /api-public/v1/user/{user}/contact-methods/devices/{contactId} | Update a contact device for a user |
| [**apiPublicV1UserUserContactMethodsDevicesGet**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsDevicesGet) | **GET** /api-public/v1/user/{user}/contact-methods/devices | Get a list of all contact devices for a user |
| [**apiPublicV1UserUserContactMethodsEmailsContactIdDelete**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsEmailsContactIdDelete) | **DELETE** /api-public/v1/user/{user}/contact-methods/emails/{contactId} | Delete a contact email for a user |
| [**apiPublicV1UserUserContactMethodsEmailsContactIdGet**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsEmailsContactIdGet) | **GET** /api-public/v1/user/{user}/contact-methods/emails/{contactId} | Get the indicated contact email for a user |
| [**apiPublicV1UserUserContactMethodsEmailsGet**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsEmailsGet) | **GET** /api-public/v1/user/{user}/contact-methods/emails | Get a list of all contact emails for a user |
| [**apiPublicV1UserUserContactMethodsEmailsPost**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsEmailsPost) | **POST** /api-public/v1/user/{user}/contact-methods/emails | Create a contact emails for a user |
| [**apiPublicV1UserUserContactMethodsGet**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsGet) | **GET** /api-public/v1/user/{user}/contact-methods | Get a list of all contact methods for a user |
| [**apiPublicV1UserUserContactMethodsPhonesContactIdDelete**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsPhonesContactIdDelete) | **DELETE** /api-public/v1/user/{user}/contact-methods/phones/{contactId} | Delete a contact phone for a user |
| [**apiPublicV1UserUserContactMethodsPhonesContactIdGet**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsPhonesContactIdGet) | **GET** /api-public/v1/user/{user}/contact-methods/phones/{contactId} | Get the indicated contact phone for a user |
| [**apiPublicV1UserUserContactMethodsPhonesGet**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsPhonesGet) | **GET** /api-public/v1/user/{user}/contact-methods/phones | Get a list of all contact phones for a user |
| [**apiPublicV1UserUserContactMethodsPhonesPost**](UserContactMethodsApi.md#apiPublicV1UserUserContactMethodsPhonesPost) | **POST** /api-public/v1/user/{user}/contact-methods/phones | Create a contact phones for a user |


<a id="apiPublicV1UserUserContactMethodsDevicesContactIdDelete"></a>
# **apiPublicV1UserUserContactMethodsDevicesContactIdDelete**
> ContactDevice apiPublicV1UserUserContactMethodsDevicesContactIdDelete(xVOApiId, xVOApiKey, user, contactId)

Delete a contact device for a user

Delete a contact device for a user  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserContactMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UserContactMethodsApi apiInstance = new UserContactMethodsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user ID
    String contactId = "contactId_example"; // String | The unique contact identifier
    try {
      ContactDevice result = apiInstance.apiPublicV1UserUserContactMethodsDevicesContactIdDelete(xVOApiId, xVOApiKey, user, contactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserContactMethodsApi#apiPublicV1UserUserContactMethodsDevicesContactIdDelete");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user ID | |
| **contactId** | **String**| The unique contact identifier | |

### Return type

[**ContactDevice**](ContactDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted contact device for the user |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserUserContactMethodsDevicesContactIdGet"></a>
# **apiPublicV1UserUserContactMethodsDevicesContactIdGet**
> List&lt;ContactDevice&gt; apiPublicV1UserUserContactMethodsDevicesContactIdGet(xVOApiId, xVOApiKey, user, contactId)

Get the indicated contact device for a user

Get the indicated contact device for a user  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserContactMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UserContactMethodsApi apiInstance = new UserContactMethodsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user ID
    String contactId = "contactId_example"; // String | The unique contact identifier
    try {
      List<ContactDevice> result = apiInstance.apiPublicV1UserUserContactMethodsDevicesContactIdGet(xVOApiId, xVOApiKey, user, contactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserContactMethodsApi#apiPublicV1UserUserContactMethodsDevicesContactIdGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user ID | |
| **contactId** | **String**| The unique contact identifier | |

### Return type

[**List&lt;ContactDevice&gt;**](ContactDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of contact devices for the user |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserUserContactMethodsDevicesContactIdPut"></a>
# **apiPublicV1UserUserContactMethodsDevicesContactIdPut**
> ContactDevice apiPublicV1UserUserContactMethodsDevicesContactIdPut(xVOApiId, xVOApiKey, user, contactId, body)

Update a contact device for a user

Update a contact device for a user  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserContactMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UserContactMethodsApi apiInstance = new UserContactMethodsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user ID
    String contactId = "contactId_example"; // String | The unique contact identifier
    ContactDeviceAdd body = new ContactDeviceAdd(); // ContactDeviceAdd | The contact device
    try {
      ContactDevice result = apiInstance.apiPublicV1UserUserContactMethodsDevicesContactIdPut(xVOApiId, xVOApiKey, user, contactId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserContactMethodsApi#apiPublicV1UserUserContactMethodsDevicesContactIdPut");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user ID | |
| **contactId** | **String**| The unique contact identifier | |
| **body** | [**ContactDeviceAdd**](ContactDeviceAdd.md)| The contact device | |

### Return type

[**ContactDevice**](ContactDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of contact devices for the user |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserUserContactMethodsDevicesGet"></a>
# **apiPublicV1UserUserContactMethodsDevicesGet**
> List&lt;ContactDevice&gt; apiPublicV1UserUserContactMethodsDevicesGet(xVOApiId, xVOApiKey, user)

Get a list of all contact devices for a user

Get the contact methods for a user  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserContactMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UserContactMethodsApi apiInstance = new UserContactMethodsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user ID
    try {
      List<ContactDevice> result = apiInstance.apiPublicV1UserUserContactMethodsDevicesGet(xVOApiId, xVOApiKey, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserContactMethodsApi#apiPublicV1UserUserContactMethodsDevicesGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user ID | |

### Return type

[**List&lt;ContactDevice&gt;**](ContactDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of contact devices for the user |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserUserContactMethodsEmailsContactIdDelete"></a>
# **apiPublicV1UserUserContactMethodsEmailsContactIdDelete**
> UserContact apiPublicV1UserUserContactMethodsEmailsContactIdDelete(xVOApiId, xVOApiKey, user, contactId)

Delete a contact email for a user

Delete the indicated contact email for the user  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserContactMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UserContactMethodsApi apiInstance = new UserContactMethodsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user ID
    String contactId = "contactId_example"; // String | The unique contact identifier
    try {
      UserContact result = apiInstance.apiPublicV1UserUserContactMethodsEmailsContactIdDelete(xVOApiId, xVOApiKey, user, contactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserContactMethodsApi#apiPublicV1UserUserContactMethodsEmailsContactIdDelete");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user ID | |
| **contactId** | **String**| The unique contact identifier | |

### Return type

[**UserContact**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted contact email for the user |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserUserContactMethodsEmailsContactIdGet"></a>
# **apiPublicV1UserUserContactMethodsEmailsContactIdGet**
> List&lt;UserContact&gt; apiPublicV1UserUserContactMethodsEmailsContactIdGet(xVOApiId, xVOApiKey, user, contactId)

Get the indicated contact email for a user

Get the indicated contact email for a user  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserContactMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UserContactMethodsApi apiInstance = new UserContactMethodsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user ID
    String contactId = "contactId_example"; // String | The unique contact identifier
    try {
      List<UserContact> result = apiInstance.apiPublicV1UserUserContactMethodsEmailsContactIdGet(xVOApiId, xVOApiKey, user, contactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserContactMethodsApi#apiPublicV1UserUserContactMethodsEmailsContactIdGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user ID | |
| **contactId** | **String**| The unique contact identifier | |

### Return type

[**List&lt;UserContact&gt;**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The indicated contact email for the user |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserUserContactMethodsEmailsGet"></a>
# **apiPublicV1UserUserContactMethodsEmailsGet**
> List&lt;UserContact&gt; apiPublicV1UserUserContactMethodsEmailsGet(xVOApiId, xVOApiKey, user)

Get a list of all contact emails for a user

Get the contact emails for a user  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserContactMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UserContactMethodsApi apiInstance = new UserContactMethodsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user ID
    try {
      List<UserContact> result = apiInstance.apiPublicV1UserUserContactMethodsEmailsGet(xVOApiId, xVOApiKey, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserContactMethodsApi#apiPublicV1UserUserContactMethodsEmailsGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user ID | |

### Return type

[**List&lt;UserContact&gt;**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of contact emails for the user |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserUserContactMethodsEmailsPost"></a>
# **apiPublicV1UserUserContactMethodsEmailsPost**
> UserContact apiPublicV1UserUserContactMethodsEmailsPost(xVOApiId, xVOApiKey, user, body)

Create a contact emails for a user

Create a contact email for a user  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserContactMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UserContactMethodsApi apiInstance = new UserContactMethodsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user ID
    ContactEmailAdd body = new ContactEmailAdd(); // ContactEmailAdd | The contact email
    try {
      UserContact result = apiInstance.apiPublicV1UserUserContactMethodsEmailsPost(xVOApiId, xVOApiKey, user, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserContactMethodsApi#apiPublicV1UserUserContactMethodsEmailsPost");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user ID | |
| **body** | [**ContactEmailAdd**](ContactEmailAdd.md)| The contact email | |

### Return type

[**UserContact**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of contact emails for the user |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserUserContactMethodsGet"></a>
# **apiPublicV1UserUserContactMethodsGet**
> ApiPublicV1UserUserContactMethodsGet200Response apiPublicV1UserUserContactMethodsGet(xVOApiId, xVOApiKey, user)

Get a list of all contact methods for a user

Get the contact methods for a user  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserContactMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UserContactMethodsApi apiInstance = new UserContactMethodsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user ID
    try {
      ApiPublicV1UserUserContactMethodsGet200Response result = apiInstance.apiPublicV1UserUserContactMethodsGet(xVOApiId, xVOApiKey, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserContactMethodsApi#apiPublicV1UserUserContactMethodsGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user ID | |

### Return type

[**ApiPublicV1UserUserContactMethodsGet200Response**](ApiPublicV1UserUserContactMethodsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All available contact methods for the user |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserUserContactMethodsPhonesContactIdDelete"></a>
# **apiPublicV1UserUserContactMethodsPhonesContactIdDelete**
> UserContact apiPublicV1UserUserContactMethodsPhonesContactIdDelete(xVOApiId, xVOApiKey, user, contactId)

Delete a contact phone for a user

Delete the indicated contact phone for the user  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserContactMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UserContactMethodsApi apiInstance = new UserContactMethodsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user ID
    String contactId = "contactId_example"; // String | The unique contact identifier
    try {
      UserContact result = apiInstance.apiPublicV1UserUserContactMethodsPhonesContactIdDelete(xVOApiId, xVOApiKey, user, contactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserContactMethodsApi#apiPublicV1UserUserContactMethodsPhonesContactIdDelete");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user ID | |
| **contactId** | **String**| The unique contact identifier | |

### Return type

[**UserContact**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted contact phone for the user |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserUserContactMethodsPhonesContactIdGet"></a>
# **apiPublicV1UserUserContactMethodsPhonesContactIdGet**
> List&lt;UserContact&gt; apiPublicV1UserUserContactMethodsPhonesContactIdGet(xVOApiId, xVOApiKey, user, contactId)

Get the indicated contact phone for a user

Get the indicated contact phone for a user  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserContactMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UserContactMethodsApi apiInstance = new UserContactMethodsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user ID
    String contactId = "contactId_example"; // String | The unique contact identifier
    try {
      List<UserContact> result = apiInstance.apiPublicV1UserUserContactMethodsPhonesContactIdGet(xVOApiId, xVOApiKey, user, contactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserContactMethodsApi#apiPublicV1UserUserContactMethodsPhonesContactIdGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user ID | |
| **contactId** | **String**| The unique contact identifier | |

### Return type

[**List&lt;UserContact&gt;**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The indicated contact phone for the user |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserUserContactMethodsPhonesGet"></a>
# **apiPublicV1UserUserContactMethodsPhonesGet**
> List&lt;UserContact&gt; apiPublicV1UserUserContactMethodsPhonesGet(xVOApiId, xVOApiKey, user)

Get a list of all contact phones for a user

Get the contact phones for a user  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserContactMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UserContactMethodsApi apiInstance = new UserContactMethodsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user ID
    try {
      List<UserContact> result = apiInstance.apiPublicV1UserUserContactMethodsPhonesGet(xVOApiId, xVOApiKey, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserContactMethodsApi#apiPublicV1UserUserContactMethodsPhonesGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user ID | |

### Return type

[**List&lt;UserContact&gt;**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of contact phones for the user |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserUserContactMethodsPhonesPost"></a>
# **apiPublicV1UserUserContactMethodsPhonesPost**
> UserContact apiPublicV1UserUserContactMethodsPhonesPost(xVOApiId, xVOApiKey, user, body)

Create a contact phones for a user

Create a contact phone for a user  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserContactMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UserContactMethodsApi apiInstance = new UserContactMethodsApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user ID
    ContactPhoneAdd body = new ContactPhoneAdd(); // ContactPhoneAdd | The contact phone
    try {
      UserContact result = apiInstance.apiPublicV1UserUserContactMethodsPhonesPost(xVOApiId, xVOApiKey, user, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserContactMethodsApi#apiPublicV1UserUserContactMethodsPhonesPost");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user ID | |
| **body** | [**ContactPhoneAdd**](ContactPhoneAdd.md)| The contact phone | |

### Return type

[**UserContact**](UserContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of contact phones for the user |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

