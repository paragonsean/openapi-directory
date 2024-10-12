# CredentialOperationsApi

All URIs are relative to *http://okta.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changePassword**](CredentialOperationsApi.md#changePassword) | **POST** /api/v1/users/{userId}/credentials/change_password | Change Password |
| [**changeRecoveryQuestion**](CredentialOperationsApi.md#changeRecoveryQuestion) | **POST** /api/v1/users/{userId}/credentials/change_recovery_question | Change Recovery Question |
| [**forgotPasswordOneTimeCode**](CredentialOperationsApi.md#forgotPasswordOneTimeCode) | **POST** /api/v1/users/{userId}/credentials/forgot_password | Forgot Password (One Time Code) |
| [**setRecoveryCredential**](CredentialOperationsApi.md#setRecoveryCredential) | **PUT** /api/v1/users/{userId} | Set Recovery Credential |


<a id="changePassword"></a>
# **changePassword**
> changePassword(userId, changePasswordRequest)

Change Password

Change Password

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CredentialOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://okta.local");

    CredentialOperationsApi apiInstance = new CredentialOperationsApi(defaultClient);
    String userId = "userId_example"; // String | 
    ChangePasswordRequest changePasswordRequest = new ChangePasswordRequest(); // ChangePasswordRequest | 
    try {
      apiInstance.changePassword(userId, changePasswordRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CredentialOperationsApi#changePassword");
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
| **userId** | **String**|  | |
| **changePasswordRequest** | [**ChangePasswordRequest**](ChangePasswordRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="changeRecoveryQuestion"></a>
# **changeRecoveryQuestion**
> changeRecoveryQuestion(userId, changeRecoveryQuestionRequest)

Change Recovery Question

Change Recovery Question

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CredentialOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://okta.local");

    CredentialOperationsApi apiInstance = new CredentialOperationsApi(defaultClient);
    String userId = "userId_example"; // String | 
    ChangeRecoveryQuestionRequest changeRecoveryQuestionRequest = new ChangeRecoveryQuestionRequest(); // ChangeRecoveryQuestionRequest | 
    try {
      apiInstance.changeRecoveryQuestion(userId, changeRecoveryQuestionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CredentialOperationsApi#changeRecoveryQuestion");
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
| **userId** | **String**|  | |
| **changeRecoveryQuestionRequest** | [**ChangeRecoveryQuestionRequest**](ChangeRecoveryQuestionRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="forgotPasswordOneTimeCode"></a>
# **forgotPasswordOneTimeCode**
> forgotPasswordOneTimeCode(userId, sendEmail)

Forgot Password (One Time Code)

Forgot Password (One Time Code)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CredentialOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://okta.local");

    CredentialOperationsApi apiInstance = new CredentialOperationsApi(defaultClient);
    String userId = "userId_example"; // String | 
    String sendEmail = "false"; // String | 
    try {
      apiInstance.forgotPasswordOneTimeCode(userId, sendEmail);
    } catch (ApiException e) {
      System.err.println("Exception when calling CredentialOperationsApi#forgotPasswordOneTimeCode");
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
| **userId** | **String**|  | |
| **sendEmail** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="setRecoveryCredential"></a>
# **setRecoveryCredential**
> setRecoveryCredential(userId, setRecoveryCredentialRequest)

Set Recovery Credential

Set Recovery Credential

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CredentialOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://okta.local");

    CredentialOperationsApi apiInstance = new CredentialOperationsApi(defaultClient);
    String userId = "userId_example"; // String | 
    SetRecoveryCredentialRequest setRecoveryCredentialRequest = new SetRecoveryCredentialRequest(); // SetRecoveryCredentialRequest | 
    try {
      apiInstance.setRecoveryCredential(userId, setRecoveryCredentialRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CredentialOperationsApi#setRecoveryCredential");
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
| **userId** | **String**|  | |
| **setRecoveryCredentialRequest** | [**SetRecoveryCredentialRequest**](SetRecoveryCredentialRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

