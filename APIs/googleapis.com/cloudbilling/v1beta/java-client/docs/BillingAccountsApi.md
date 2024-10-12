# BillingAccountsApi

All URIs are relative to *https://cloudbilling.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cloudbillingBillingAccountsEstimateCostScenario**](BillingAccountsApi.md#cloudbillingBillingAccountsEstimateCostScenario) | **POST** /v1beta/{billingAccount}:estimateCostScenario |  |
| [**cloudbillingBillingAccountsServicesList**](BillingAccountsApi.md#cloudbillingBillingAccountsServicesList) | **GET** /v1beta/{parent}/services |  |
| [**cloudbillingBillingAccountsSkuGroupsList**](BillingAccountsApi.md#cloudbillingBillingAccountsSkuGroupsList) | **GET** /v1beta/{parent}/skuGroups |  |


<a id="cloudbillingBillingAccountsEstimateCostScenario"></a>
# **cloudbillingBillingAccountsEstimateCostScenario**
> EstimateCostScenarioForBillingAccountResponse cloudbillingBillingAccountsEstimateCostScenario(billingAccount, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, estimateCostScenarioForBillingAccountRequest)



Use custom pricing in the estimate, using a &#x60;CostScenario&#x60; with a defined &#x60;billingAccount&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudbilling.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingAccountsApi apiInstance = new BillingAccountsApi(defaultClient);
    String billingAccount = "billingAccount_example"; // String | Resource name of the billing account for the cost estimate. The resource name has the form `billingAccounts/{billing_account_id}`. For example, `billingAccounts/012345-567890-ABCDEF` is the resource name for billing account `012345-567890-ABCDEF`. Must be specified.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    EstimateCostScenarioForBillingAccountRequest estimateCostScenarioForBillingAccountRequest = new EstimateCostScenarioForBillingAccountRequest(); // EstimateCostScenarioForBillingAccountRequest | 
    try {
      EstimateCostScenarioForBillingAccountResponse result = apiInstance.cloudbillingBillingAccountsEstimateCostScenario(billingAccount, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, estimateCostScenarioForBillingAccountRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingAccountsApi#cloudbillingBillingAccountsEstimateCostScenario");
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
| **billingAccount** | **String**| Resource name of the billing account for the cost estimate. The resource name has the form &#x60;billingAccounts/{billing_account_id}&#x60;. For example, &#x60;billingAccounts/012345-567890-ABCDEF&#x60; is the resource name for billing account &#x60;012345-567890-ABCDEF&#x60;. Must be specified. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **estimateCostScenarioForBillingAccountRequest** | [**EstimateCostScenarioForBillingAccountRequest**](EstimateCostScenarioForBillingAccountRequest.md)|  | [optional] |

### Return type

[**EstimateCostScenarioForBillingAccountResponse**](EstimateCostScenarioForBillingAccountResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudbillingBillingAccountsServicesList"></a>
# **cloudbillingBillingAccountsServicesList**
> GoogleCloudBillingBillingaccountservicesV1betaListBillingAccountServicesResponse cloudbillingBillingAccountsServicesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Lists services visible to a billing account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudbilling.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingAccountsApi apiInstance = new BillingAccountsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The billing account to list billing account service from. Format: billingAccounts/{billing_account}
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | Maximum number of billing account service to return. Results may return fewer than this value. Default value is 50 and maximum value is 5000.
    String pageToken = "pageToken_example"; // String | Page token received from a previous ListBillingAccountServices call to retrieve the next page of results. If this field is empty, the first page is returned.
    try {
      GoogleCloudBillingBillingaccountservicesV1betaListBillingAccountServicesResponse result = apiInstance.cloudbillingBillingAccountsServicesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingAccountsApi#cloudbillingBillingAccountsServicesList");
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
| **parent** | **String**| Required. The billing account to list billing account service from. Format: billingAccounts/{billing_account} | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| Maximum number of billing account service to return. Results may return fewer than this value. Default value is 50 and maximum value is 5000. | [optional] |
| **pageToken** | **String**| Page token received from a previous ListBillingAccountServices call to retrieve the next page of results. If this field is empty, the first page is returned. | [optional] |

### Return type

[**GoogleCloudBillingBillingaccountservicesV1betaListBillingAccountServicesResponse**](GoogleCloudBillingBillingaccountservicesV1betaListBillingAccountServicesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudbillingBillingAccountsSkuGroupsList"></a>
# **cloudbillingBillingAccountsSkuGroupsList**
> GoogleCloudBillingBillingaccountskugroupsV1betaListBillingAccountSkuGroupsResponse cloudbillingBillingAccountsSkuGroupsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Lists SKU groups visible to a billing account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudbilling.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingAccountsApi apiInstance = new BillingAccountsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The billing account to list billing account SKU groups from. Format: billingAccounts/{billing_account}
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | Maximum number of billing account SKU groups to return. Results may return fewer than this value. Default value is 50 and maximum value is 5000.
    String pageToken = "pageToken_example"; // String | Page token received from a previous ListBillingAccountSkuGroups call to retrieve the next page of results. If this field is empty, the first page is returned.
    try {
      GoogleCloudBillingBillingaccountskugroupsV1betaListBillingAccountSkuGroupsResponse result = apiInstance.cloudbillingBillingAccountsSkuGroupsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingAccountsApi#cloudbillingBillingAccountsSkuGroupsList");
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
| **parent** | **String**| Required. The billing account to list billing account SKU groups from. Format: billingAccounts/{billing_account} | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| Maximum number of billing account SKU groups to return. Results may return fewer than this value. Default value is 50 and maximum value is 5000. | [optional] |
| **pageToken** | **String**| Page token received from a previous ListBillingAccountSkuGroups call to retrieve the next page of results. If this field is empty, the first page is returned. | [optional] |

### Return type

[**GoogleCloudBillingBillingaccountskugroupsV1betaListBillingAccountSkuGroupsResponse**](GoogleCloudBillingBillingaccountskugroupsV1betaListBillingAccountSkuGroupsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

