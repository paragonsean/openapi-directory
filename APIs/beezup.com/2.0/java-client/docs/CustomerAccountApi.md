# CustomerAccountApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activateUserAccount**](CustomerAccountApi.md#activateUserAccount) | **POST** /v2/user/customer/account/activate | Activate the user account |
| [**changeEmail**](CustomerAccountApi.md#changeEmail) | **POST** /v2/user/customer/account/changeEmail | Change user email |
| [**changePassword**](CustomerAccountApi.md#changePassword) | **POST** /v2/user/customer/account/changePassword | Change user password |
| [**getCreditCardInfo**](CustomerAccountApi.md#getCreditCardInfo) | **GET** /v2/user/customer/account/creditCardInfo | Get credit card information |
| [**getProfilePictureInfo**](CustomerAccountApi.md#getProfilePictureInfo) | **GET** /v2/user/customer/account/profilePictureInfo | Get profile picture information |
| [**getUserAccountInfo**](CustomerAccountApi.md#getUserAccountInfo) | **GET** /v2/user/customer/account | Get user account information |
| [**resendEmailActivation**](CustomerAccountApi.md#resendEmailActivation) | **POST** /v2/user/customer/account/resendEmailActivation | Resend email activation |
| [**saveCompanyInfo**](CustomerAccountApi.md#saveCompanyInfo) | **PUT** /v2/user/customer/account/companyInfo | Change company information |
| [**saveCreditCardInfo**](CustomerAccountApi.md#saveCreditCardInfo) | **PUT** /v2/user/customer/account/creditCardInfo | Save user credit card info |
| [**savePersonalInfo**](CustomerAccountApi.md#savePersonalInfo) | **PUT** /v2/user/customer/account/personalInfo | Save user personal information |
| [**saveProfilePictureInfo**](CustomerAccountApi.md#saveProfilePictureInfo) | **PUT** /v2/user/customer/account/profilePictureInfo | Change user picture information |


<a id="activateUserAccount"></a>
# **activateUserAccount**
> activateUserAccount(body)

Activate the user account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerAccountApi apiInstance = new CustomerAccountApi(defaultClient);
    String body = "body_example"; // String | The email activation id received by email.
    try {
      apiInstance.activateUserAccount(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAccountApi#activateUserAccount");
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
| **body** | **String**| The email activation id received by email. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | User account activated. |  -  |
| **403** | Invalid email activation id |  -  |
| **409** | User account already activated. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="changeEmail"></a>
# **changeEmail**
> changeEmail(changeEmailRequest)

Change user email

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerAccountApi apiInstance = new CustomerAccountApi(defaultClient);
    ChangeEmailRequest changeEmailRequest = new ChangeEmailRequest(); // ChangeEmailRequest | 
    try {
      apiInstance.changeEmail(changeEmailRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAccountApi#changeEmail");
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
| **changeEmailRequest** | [**ChangeEmailRequest**](ChangeEmailRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Email updated |  -  |
| **400** | New email does not respect the emails&#39;s constraints |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="changePassword"></a>
# **changePassword**
> changePassword(changePasswordRequest)

Change user password

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerAccountApi apiInstance = new CustomerAccountApi(defaultClient);
    ChangePasswordRequest changePasswordRequest = new ChangePasswordRequest(); // ChangePasswordRequest | 
    try {
      apiInstance.changePassword(changePasswordRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAccountApi#changePassword");
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
| **changePasswordRequest** | [**ChangePasswordRequest**](ChangePasswordRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Password updated |  -  |
| **400** | Old password is invalid or the new password does not respect the password&#39;s constraints |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getCreditCardInfo"></a>
# **getCreditCardInfo**
> CreditCardInfoResponse getCreditCardInfo(ifNoneMatch)

Get credit card information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerAccountApi apiInstance = new CustomerAccountApi(defaultClient);
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    try {
      CreditCardInfoResponse result = apiInstance.getCreditCardInfo(ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAccountApi#getCreditCardInfo");
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
| **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] |

### Return type

[**CreditCardInfoResponse**](CreditCardInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User credit card information |  -  |
| **304** | The ETag sent in the http header If-None-Match did not change. So you are up to date ! |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  * Last-Modified - Last modification UTC date of the resource\\ For more details go to this link: https://tools.ietf.org/html/rfc7232#section-2.2  <br>  |
| **404** | Credit Card not found |  -  |
| **503** | We are unable to get your credit card info. This is a temporary state. Please retry later |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getProfilePictureInfo"></a>
# **getProfilePictureInfo**
> ProfilePictureInfoResponse getProfilePictureInfo(ifNoneMatch)

Get profile picture information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerAccountApi apiInstance = new CustomerAccountApi(defaultClient);
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    try {
      ProfilePictureInfoResponse result = apiInstance.getProfilePictureInfo(ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAccountApi#getProfilePictureInfo");
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
| **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] |

### Return type

[**ProfilePictureInfoResponse**](ProfilePictureInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Profile picture information |  -  |
| **304** | The ETag sent in the http header If-None-Match did not change. So you are up to date ! |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  * Last-Modified - Last modification UTC date of the resource\\ For more details go to this link: https://tools.ietf.org/html/rfc7232#section-2.2  <br>  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getUserAccountInfo"></a>
# **getUserAccountInfo**
> AccountInfo getUserAccountInfo(ifNoneMatch)

Get user account information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerAccountApi apiInstance = new CustomerAccountApi(defaultClient);
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    try {
      AccountInfo result = apiInstance.getUserAccountInfo(ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAccountApi#getUserAccountInfo");
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
| **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] |

### Return type

[**AccountInfo**](AccountInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User account information |  -  |
| **304** | The ETag sent in the http header If-None-Match did not change. So you are up to date ! |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  * Last-Modified - Last modification UTC date of the resource\\ For more details go to this link: https://tools.ietf.org/html/rfc7232#section-2.2  <br>  |
| **0** | Occurs when something goes wrong |  -  |

<a id="resendEmailActivation"></a>
# **resendEmailActivation**
> resendEmailActivation()

Resend email activation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerAccountApi apiInstance = new CustomerAccountApi(defaultClient);
    try {
      apiInstance.resendEmailActivation();
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAccountApi#resendEmailActivation");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Email activation resent |  -  |
| **400** | Email activation not sent because of email problem. Ensure that your email is the correct one. |  -  |
| **409** | Email activation not available because user account already activated. |  -  |
| **429** | Email activation sent recently, must retry later. (One per hour) |  * Retry-After - Indicates the duration in seconds to wait to be able to make this request again <br>  |
| **502** | Email activate send failed because of our email service. Ensure that your email is the correct one otherwise please contact our support if the problem persists. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="saveCompanyInfo"></a>
# **saveCompanyInfo**
> saveCompanyInfo(companyInfo)

Change company information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerAccountApi apiInstance = new CustomerAccountApi(defaultClient);
    CompanyInfo companyInfo = new CompanyInfo(); // CompanyInfo | 
    try {
      apiInstance.saveCompanyInfo(companyInfo);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAccountApi#saveCompanyInfo");
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
| **companyInfo** | [**CompanyInfo**](CompanyInfo.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Company information saved |  -  |
| **400** | Bad request or invalid VATNumber. |  -  |
| **403** | User not found or unauthorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="saveCreditCardInfo"></a>
# **saveCreditCardInfo**
> saveCreditCardInfo(creditCardInfo)

Save user credit card info

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerAccountApi apiInstance = new CustomerAccountApi(defaultClient);
    CreditCardInfo creditCardInfo = new CreditCardInfo(); // CreditCardInfo | Credit card info
    try {
      apiInstance.saveCreditCardInfo(creditCardInfo);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAccountApi#saveCreditCardInfo");
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
| **creditCardInfo** | [**CreditCardInfo**](CreditCardInfo.md)| Credit card info | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The credit card information has been accepted for processing, the authorization will be processed shortly. |  -  |
| **400** | BadRequest |  -  |
| **502** | Communication problem with our payment service |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="savePersonalInfo"></a>
# **savePersonalInfo**
> savePersonalInfo(personalInfo)

Save user personal information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerAccountApi apiInstance = new CustomerAccountApi(defaultClient);
    PersonalInfo personalInfo = new PersonalInfo(); // PersonalInfo | 
    try {
      apiInstance.savePersonalInfo(personalInfo);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAccountApi#savePersonalInfo");
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
| **personalInfo** | [**PersonalInfo**](PersonalInfo.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | User account information updated |  -  |
| **400** | Bad Request |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="saveProfilePictureInfo"></a>
# **saveProfilePictureInfo**
> saveProfilePictureInfo(profilePictureInfo)

Change user picture information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerAccountApi apiInstance = new CustomerAccountApi(defaultClient);
    ProfilePictureInfo profilePictureInfo = new ProfilePictureInfo(); // ProfilePictureInfo | 
    try {
      apiInstance.saveProfilePictureInfo(profilePictureInfo);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAccountApi#saveProfilePictureInfo");
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
| **profilePictureInfo** | [**ProfilePictureInfo**](ProfilePictureInfo.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | User profile picture information saved. |  -  |
| **400** | BadRequest (Url invalid) |  -  |
| **413** | The picture size is too large |  -  |
| **415** | The content type of the image must be an image |  -  |
| **0** | Occurs when something goes wrong |  -  |

