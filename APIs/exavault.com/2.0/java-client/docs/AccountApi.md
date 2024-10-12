# AccountApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAccount**](AccountApi.md#getAccount) | **GET** /account | Get account settings |
| [**updateAccount**](AccountApi.md#updateAccount) | **PATCH** /account | Update account settings |


<a id="getAccount"></a>
# **getAccount**
> AccountResponse getAccount(evApiKey, evAccessToken, include)

Get account settings

Get settings for your account, such as current space usage, webhooks settings, welcome email content and IP address restrictions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key required for the request
    String evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access Token for the request
    String include = "masterUser"; // String | Related records to include in the response. Valid option is **masterUser**
    try {
      AccountResponse result = apiInstance.getAccount(evApiKey, evAccessToken, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#getAccount");
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
| **evApiKey** | **String**| API Key required for the request | |
| **evAccessToken** | **String**| Access Token for the request | |
| **include** | **String**| Related records to include in the response. Valid option is **masterUser** | [optional] |

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateAccount"></a>
# **updateAccount**
> AccountResponse updateAccount(evApiKey, evAccessToken, updateAccountRequestBody)

Update account settings

Update account settings, such as welcome email content, IP address restrictions, webhooks settings and secure password requirements.  **Notes**  - You must have [admin-level access](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to change account settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key required to make the API call.
    String evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access token required to make the API call.
    UpdateAccountRequestBody updateAccountRequestBody = new UpdateAccountRequestBody(); // UpdateAccountRequestBody | Update Account Settings
    try {
      AccountResponse result = apiInstance.updateAccount(evApiKey, evAccessToken, updateAccountRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#updateAccount");
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
| **updateAccountRequestBody** | [**UpdateAccountRequestBody**](UpdateAccountRequestBody.md)| Update Account Settings | [optional] |

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

