# ProviderAccountsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteProviderAccount**](ProviderAccountsApi.md#deleteProviderAccount) | **DELETE** /providerAccounts/{providerAccountId} | Delete Provider Account |
| [**editCredentialsOrRefreshProviderAccount**](ProviderAccountsApi.md#editCredentialsOrRefreshProviderAccount) | **PUT** /providerAccounts | Update Account |
| [**getAllProviderAccounts**](ProviderAccountsApi.md#getAllProviderAccounts) | **GET** /providerAccounts | Get Provider Accounts |
| [**getProviderAccount**](ProviderAccountsApi.md#getProviderAccount) | **GET** /providerAccounts/{providerAccountId} | Get Provider Account Details |
| [**getProviderAccountProfiles**](ProviderAccountsApi.md#getProviderAccountProfiles) | **GET** /providerAccounts/profile | Get User Profile Details |
| [**updatePreferences**](ProviderAccountsApi.md#updatePreferences) | **PUT** /providerAccounts/{providerAccountId}/preferences | Update Preferences |


<a id="deleteProviderAccount"></a>
# **deleteProviderAccount**
> deleteProviderAccount(providerAccountId)

Delete Provider Account

The delete provider account service is used to delete a provider account from the Yodlee system. This service also deletes the accounts that are created in the Yodlee system for that provider account. &lt;br&gt;This service does not return a response. The HTTP response code is 204 (Success with no content).&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ProviderAccountsApi apiInstance = new ProviderAccountsApi(defaultClient);
    Long providerAccountId = 56L; // Long | providerAccountId
    try {
      apiInstance.deleteProviderAccount(providerAccountId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderAccountsApi#deleteProviderAccount");
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
| **providerAccountId** | **Long**| providerAccountId | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for providerAccountId&lt;br&gt;Y868 : No action is allowed, as the data is being migrated to the Open Banking provider&lt;br&gt; |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="editCredentialsOrRefreshProviderAccount"></a>
# **editCredentialsOrRefreshProviderAccount**
> UpdatedProviderAccountResponse editCredentialsOrRefreshProviderAccount(providerAccountIds, providerAccountRequest)

Update Account

The update account API is used to:&lt;br&gt; &lt;ul&gt;&lt;li&gt;Retrieve the latest information for accounts that belong to one providerAccount from the provider site. You must allow at least 15 min between requests.&lt;li&gt;Retrieve the latest information of all the eligible accounts that belong to the user.&lt;li&gt;Data to be retrieved from the provider site can be overridden using datasetName or dataset. If you do pass datasetName, all the datasets that are implicitly configured for the dataset will be retrieved. This action is allowed for single provider account refresh flows only.&lt;li&gt;Check the status of the providerAccount before invoking this API. Do not call this API to trigger any action on a providerAccount when an action is already in progress for the providerAccount.&lt;li&gt;If the customer has subscribed to the REFRESH event notification and invoked this API, relevant notifications will be sent to the customer.&lt;li&gt;A dataset may depend on another dataset for retrieval, so the response will include the requested and dependent datasets.&lt;li&gt;Check all the dataset additional statuses returned in the response because the provider account status is drawn from the dataset additional statuses.&lt;li&gt;Updating preferences using this API will trigger refreshes.&lt;li&gt; The content type has to be passed as application/json for the body parameter.&lt;/ul&gt;&lt;br&gt;-----------------------------------------------------------------------------------------------------------------------------------------&lt;br&gt;&lt;br&gt;&lt;b&gt;Update All Eligible Accounts - Notes:&lt;/b&gt;&lt;br&gt;&lt;ul&gt;&lt;li&gt;This API will trigger a refresh for all the eligible provider accounts(both OB and credential-based accounts).&lt;li&gt;This API will not refresh closed, inactive, or UAR accounts, or accounts with refreshes in-progress or recently refreshed non-OB accounts.&lt;li&gt;No parameters should be passed to this API to trigger this action.&lt;li&gt;Do not call this API often. Our recommendation is to call this only at the time the user logs in to your app because it can hamper other API calls performance.&lt;li&gt;The response only contains information for accounts that were refreshed. If no accounts are eligible for refresh, no response is returned.&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ProviderAccountsApi apiInstance = new ProviderAccountsApi(defaultClient);
    String providerAccountIds = "providerAccountIds_example"; // String | comma separated providerAccountIds
    ProviderAccountRequest providerAccountRequest = new ProviderAccountRequest(); // ProviderAccountRequest | loginForm or field entity
    try {
      UpdatedProviderAccountResponse result = apiInstance.editCredentialsOrRefreshProviderAccount(providerAccountIds, providerAccountRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderAccountsApi#editCredentialsOrRefreshProviderAccount");
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
| **providerAccountIds** | **String**| comma separated providerAccountIds | |
| **providerAccountRequest** | [**ProviderAccountRequest**](ProviderAccountRequest.md)| loginForm or field entity | [optional] |

### Return type

[**UpdatedProviderAccountResponse**](UpdatedProviderAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y805 : Multiple providerAccountId not supported for updating credentials&lt;br&gt;Y800 : Invalid value for credentialsParam&lt;br&gt;Y400 : id and value in credentialsParam are mandatory&lt;br&gt;Y806 : Invalid input&lt;br&gt;Y823 : Credentials are not applicable for real estate aggregated / manual accounts&lt;br&gt;Y868 : No action is allowed, as the data is being migrated to the Open Banking provider&lt;br&gt; |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getAllProviderAccounts"></a>
# **getAllProviderAccounts**
> ProviderAccountResponse getAllProviderAccounts(include, providerIds)

Get Provider Accounts

The get provider accounts service is used to return all the provider accounts added by the user. &lt;br&gt;This includes the failed and successfully added provider accounts.&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ProviderAccountsApi apiInstance = new ProviderAccountsApi(defaultClient);
    String include = "include_example"; // String | include
    String providerIds = "providerIds_example"; // String | Comma separated providerIds.
    try {
      ProviderAccountResponse result = apiInstance.getAllProviderAccounts(include, providerIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderAccountsApi#getAllProviderAccounts");
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
| **include** | **String**| include | [optional] |
| **providerIds** | **String**| Comma separated providerIds. | [optional] |

### Return type

[**ProviderAccountResponse**](ProviderAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getProviderAccount"></a>
# **getProviderAccount**
> ProviderAccountDetailResponse getProviderAccount(providerAccountId, include, requestId)

Get Provider Account Details

The get provider account details service is used to learn the status of adding accounts and updating accounts.&lt;br&gt;This service has to be called continuously to know the progress level of the triggered process. This service also provides the MFA information requested by the provider site.&lt;br&gt;When &lt;i&gt;include &#x3D; credentials&lt;/i&gt;, questions is passed as input, the service returns the credentials (non-password values) and questions stored in the Yodlee system for that provider account. &lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;The password and answer fields are not returned in the response.&lt;/li&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ProviderAccountsApi apiInstance = new ProviderAccountsApi(defaultClient);
    Long providerAccountId = 56L; // Long | providerAccountId
    String include = "include_example"; // String | include credentials,questions
    String requestId = "requestId_example"; // String | The unique identifier for the request that returns contextual data
    try {
      ProviderAccountDetailResponse result = apiInstance.getProviderAccount(providerAccountId, include, requestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderAccountsApi#getProviderAccount");
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
| **providerAccountId** | **Long**| providerAccountId | |
| **include** | **String**| include credentials,questions | [optional] |
| **requestId** | **String**| The unique identifier for the request that returns contextual data | [optional] |

### Return type

[**ProviderAccountDetailResponse**](ProviderAccountDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for providerAccountId&lt;br&gt;Y816 : questions can only be requested for questionAndAnswer Supported Sites |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getProviderAccountProfiles"></a>
# **getProviderAccountProfiles**
> ProviderAccountUserProfileResponse getProviderAccountProfiles(providerAccountId)

Get User Profile Details

The get provider accounts profile service is used to return the user profile details that are associated to the provider account. &lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ProviderAccountsApi apiInstance = new ProviderAccountsApi(defaultClient);
    String providerAccountId = "providerAccountId_example"; // String | Comma separated providerAccountIds.
    try {
      ProviderAccountUserProfileResponse result = apiInstance.getProviderAccountProfiles(providerAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderAccountsApi#getProviderAccountProfiles");
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
| **providerAccountId** | **String**| Comma separated providerAccountIds. | [optional] |

### Return type

[**ProviderAccountUserProfileResponse**](ProviderAccountUserProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="updatePreferences"></a>
# **updatePreferences**
> updatePreferences(providerAccountId, providerAccountPreferencesRequest)

Update Preferences

This endpoint is used to update preferences like data extracts and auto refreshes without triggering refresh for the providerAccount.&lt;br&gt;Setting isDataExtractsEnabled to false will not trigger data extracts notification and dataExtracts/events will not reflect any data change that is happening for the providerAccount.&lt;br&gt;Modified data will not be provided in the dataExtracts/userData endpoint.&lt;br&gt;Setting isAutoRefreshEnabled to false will not trigger auto refreshes for the provider account.&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ProviderAccountsApi apiInstance = new ProviderAccountsApi(defaultClient);
    Long providerAccountId = 56L; // Long | providerAccountId
    ProviderAccountPreferencesRequest providerAccountPreferencesRequest = new ProviderAccountPreferencesRequest(); // ProviderAccountPreferencesRequest | preferences
    try {
      apiInstance.updatePreferences(providerAccountId, providerAccountPreferencesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderAccountsApi#updatePreferences");
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
| **providerAccountId** | **Long**| providerAccountId | |
| **providerAccountPreferencesRequest** | [**ProviderAccountPreferencesRequest**](ProviderAccountPreferencesRequest.md)| preferences | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK |  -  |
| **400** | Y800 : Invalid value for preferences&lt;br&gt;Y800 : Invalid value for preferences.isDataExtractsEnabled&lt;br&gt;Y800 : Invalid value for preferences.isAutoRefreshEnabled&lt;br&gt;Y807 : Resource not found&lt;br&gt;Y830 : Data extracts feature has to be enabled to set preferences.isDataExtractsEnabled as true&lt;br&gt;Y830 : Auto refresh feature has to be enabled to set preferences.isAutoRefreshEnabled as true&lt;br&gt;Y868 : No action is allowed, as the data is being migrated to the Open Banking provider&lt;br&gt; |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

