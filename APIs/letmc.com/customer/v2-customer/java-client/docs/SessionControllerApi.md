# SessionControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sessionControllerChangePassword**](SessionControllerApi.md#sessionControllerChangePassword) | **PUT** /v2/customer/{shortName}/session/password | Change the password of a customer given their existing and new password. |
| [**sessionControllerCreateLandlordLogin**](SessionControllerApi.md#sessionControllerCreateLandlordLogin) | **POST** /v2/customer/{shortName}/session/createlandlordlogin | Send a request to the in-tray to create a landlord login. |
| [**sessionControllerGetSessionInfo**](SessionControllerApi.md#sessionControllerGetSessionInfo) | **GET** /v2/customer/{shortName}/session | Gets information about the currently logged on customer. |
| [**sessionControllerLogin**](SessionControllerApi.md#sessionControllerLogin) | **POST** /v2/customer/{shortName}/session | Login as a customer given their username and password. |
| [**sessionControllerLogout**](SessionControllerApi.md#sessionControllerLogout) | **DELETE** /v2/customer/{shortName}/session | Logout a customer previously logged in via the Login endpoint. |
| [**sessionControllerResetPassword**](SessionControllerApi.md#sessionControllerResetPassword) | **POST** /v2/customer/{shortName}/session/resetpassword | Reset the customer&#39;s password. An email will be sent out to reset. |


<a id="sessionControllerChangePassword"></a>
# **sessionControllerChangePassword**
> sessionControllerChangePassword(shortName, token, oldPassword, newPassword)

Change the password of a customer given their existing and new password.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    SessionControllerApi apiInstance = new SessionControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    String oldPassword = "oldPassword_example"; // String | The customer's existing password.
    String newPassword = "newPassword_example"; // String | The customer's new password.
    try {
      apiInstance.sessionControllerChangePassword(shortName, token, oldPassword, newPassword);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionControllerApi#sessionControllerChangePassword");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |
| **oldPassword** | **String**| The customer&#39;s existing password. | |
| **newPassword** | **String**| The customer&#39;s new password. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="sessionControllerCreateLandlordLogin"></a>
# **sessionControllerCreateLandlordLogin**
> sessionControllerCreateLandlordLogin(shortName, email, title, forename, surname, propertyAddress, contactDetails, branchID)

Send a request to the in-tray to create a landlord login.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    SessionControllerApi apiInstance = new SessionControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String email = "email_example"; // String | The email address of the landlord
    String title = "title_example"; // String | The title of the landlord
    String forename = "forename_example"; // String | The forename of the landlord
    String surname = "surname_example"; // String | The surname of the landlord
    String propertyAddress = "propertyAddress_example"; // String | Address of the property linked to the landlord
    String contactDetails = "contactDetails_example"; // String | Contact details of the landlord
    String branchID = "branchID_example"; // String | (Optional) The branch ID linked to the login. This will determine which in tray the request display in
    try {
      apiInstance.sessionControllerCreateLandlordLogin(shortName, email, title, forename, surname, propertyAddress, contactDetails, branchID);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionControllerApi#sessionControllerCreateLandlordLogin");
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
| **shortName** | **String**| The unique client short-name | |
| **email** | **String**| The email address of the landlord | |
| **title** | **String**| The title of the landlord | |
| **forename** | **String**| The forename of the landlord | |
| **surname** | **String**| The surname of the landlord | |
| **propertyAddress** | **String**| Address of the property linked to the landlord | |
| **contactDetails** | **String**| Contact details of the landlord | |
| **branchID** | **String**| (Optional) The branch ID linked to the login. This will determine which in tray the request display in | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="sessionControllerGetSessionInfo"></a>
# **sessionControllerGetSessionInfo**
> String sessionControllerGetSessionInfo(shortName, token)

Gets information about the currently logged on customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    SessionControllerApi apiInstance = new SessionControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    try {
      String result = apiInstance.sessionControllerGetSessionInfo(shortName, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionControllerApi#sessionControllerGetSessionInfo");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sessionControllerLogin"></a>
# **sessionControllerLogin**
> String sessionControllerLogin(shortName, username, password)

Login as a customer given their username and password.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    SessionControllerApi apiInstance = new SessionControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String username = "username_example"; // String | The user's username.
    String password = "password_example"; // String | The user's password.
    try {
      String result = apiInstance.sessionControllerLogin(shortName, username, password);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionControllerApi#sessionControllerLogin");
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
| **shortName** | **String**| The unique client short-name | |
| **username** | **String**| The user&#39;s username. | |
| **password** | **String**| The user&#39;s password. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="sessionControllerLogout"></a>
# **sessionControllerLogout**
> sessionControllerLogout(shortName, token)

Logout a customer previously logged in via the Login endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    SessionControllerApi apiInstance = new SessionControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    try {
      apiInstance.sessionControllerLogout(shortName, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionControllerApi#sessionControllerLogout");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="sessionControllerResetPassword"></a>
# **sessionControllerResetPassword**
> sessionControllerResetPassword(shortName, email)

Reset the customer&#39;s password. An email will be sent out to reset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    SessionControllerApi apiInstance = new SessionControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String email = "email_example"; // String | The login Email Address.
    try {
      apiInstance.sessionControllerResetPassword(shortName, email);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionControllerApi#sessionControllerResetPassword");
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
| **shortName** | **String**| The unique client short-name | |
| **email** | **String**| The login Email Address. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

