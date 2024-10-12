# OauthApi

All URIs are relative to *https://api.clever-cloud.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOauthAuthorize_0**](OauthApi.md#getOauthAuthorize_0) | **GET** /oauth/authorize |  |
| [**getOauthRights_0**](OauthApi.md#getOauthRights_0) | **GET** /oauth/rights |  |
| [**oauthAccessTokenQueryPost_0**](OauthApi.md#oauthAccessTokenQueryPost_0) | **POST** /oauth/access_token_query |  |
| [**oauthRequestTokenQueryPost_0**](OauthApi.md#oauthRequestTokenQueryPost_0) | **POST** /oauth/request_token_query |  |
| [**postOauthAccessToken_0**](OauthApi.md#postOauthAccessToken_0) | **POST** /oauth/access_token |  |
| [**postOauthAuthorize_0**](OauthApi.md#postOauthAuthorize_0) | **POST** /oauth/authorize |  |
| [**postOauthRequestToken_0**](OauthApi.md#postOauthRequestToken_0) | **POST** /oauth/request_token |  |


<a id="getOauthAuthorize_0"></a>
# **getOauthAuthorize_0**
> getOauthAuthorize_0(oauthToken, cookie)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String oauthToken = "oauthToken_example"; // String | 
    String cookie = "cookie_example"; // String | 
    try {
      apiInstance.getOauthAuthorize_0(oauthToken, cookie);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#getOauthAuthorize_0");
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
| **oauthToken** | **String**|  | [optional] |
| **cookie** | **String**|  | [optional] |

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
| **200** | authorizeForm |  -  |

<a id="getOauthRights_0"></a>
# **getOauthRights_0**
> Rights getOauthRights_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OauthApi apiInstance = new OauthApi(defaultClient);
    try {
      Rights result = apiInstance.getOauthRights_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#getOauthRights_0");
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

[**Rights**](Rights.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getAvailableRights |  -  |

<a id="oauthAccessTokenQueryPost_0"></a>
# **oauthAccessTokenQueryPost_0**
> oauthAccessTokenQueryPost_0(oauthConsumerKey, oauthToken, oauthSignatureMethod, oauthSignature, oauthTimestamp, oauthNonce, oauthVersion, oauthVerifier, oauthCallback, oauthTokenSecret, oauthCallbackConfirmed)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String oauthConsumerKey = "oauthConsumerKey_example"; // String | 
    String oauthToken = "oauthToken_example"; // String | 
    String oauthSignatureMethod = "oauthSignatureMethod_example"; // String | 
    String oauthSignature = "oauthSignature_example"; // String | 
    String oauthTimestamp = "oauthTimestamp_example"; // String | 
    String oauthNonce = "oauthNonce_example"; // String | 
    String oauthVersion = "oauthVersion_example"; // String | 
    String oauthVerifier = "oauthVerifier_example"; // String | 
    String oauthCallback = "oauthCallback_example"; // String | 
    String oauthTokenSecret = "oauthTokenSecret_example"; // String | 
    String oauthCallbackConfirmed = "oauthCallbackConfirmed_example"; // String | 
    try {
      apiInstance.oauthAccessTokenQueryPost_0(oauthConsumerKey, oauthToken, oauthSignatureMethod, oauthSignature, oauthTimestamp, oauthNonce, oauthVersion, oauthVerifier, oauthCallback, oauthTokenSecret, oauthCallbackConfirmed);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#oauthAccessTokenQueryPost_0");
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
| **oauthConsumerKey** | **String**|  | [optional] |
| **oauthToken** | **String**|  | [optional] |
| **oauthSignatureMethod** | **String**|  | [optional] |
| **oauthSignature** | **String**|  | [optional] |
| **oauthTimestamp** | **String**|  | [optional] |
| **oauthNonce** | **String**|  | [optional] |
| **oauthVersion** | **String**|  | [optional] |
| **oauthVerifier** | **String**|  | [optional] |
| **oauthCallback** | **String**|  | [optional] |
| **oauthTokenSecret** | **String**|  | [optional] |
| **oauthCallbackConfirmed** | **String**|  | [optional] |

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
| **200** | Status 200 |  -  |

<a id="oauthRequestTokenQueryPost_0"></a>
# **oauthRequestTokenQueryPost_0**
> oauthRequestTokenQueryPost_0(oauthConsumerKey, oauthToken, oauthSignatureMethod, oauthSignature, oauthTimestamp, oauthNonce, oauthVersion, oauthVerifier, oauthCallback, oauthTokenSecret, oauthCallbackConfirmed)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String oauthConsumerKey = "oauthConsumerKey_example"; // String | 
    String oauthToken = "oauthToken_example"; // String | 
    String oauthSignatureMethod = "oauthSignatureMethod_example"; // String | 
    String oauthSignature = "oauthSignature_example"; // String | 
    String oauthTimestamp = "oauthTimestamp_example"; // String | 
    String oauthNonce = "oauthNonce_example"; // String | 
    String oauthVersion = "oauthVersion_example"; // String | 
    String oauthVerifier = "oauthVerifier_example"; // String | 
    String oauthCallback = "oauthCallback_example"; // String | 
    String oauthTokenSecret = "oauthTokenSecret_example"; // String | 
    String oauthCallbackConfirmed = "oauthCallbackConfirmed_example"; // String | 
    try {
      apiInstance.oauthRequestTokenQueryPost_0(oauthConsumerKey, oauthToken, oauthSignatureMethod, oauthSignature, oauthTimestamp, oauthNonce, oauthVersion, oauthVerifier, oauthCallback, oauthTokenSecret, oauthCallbackConfirmed);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#oauthRequestTokenQueryPost_0");
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
| **oauthConsumerKey** | **String**|  | [optional] |
| **oauthToken** | **String**|  | [optional] |
| **oauthSignatureMethod** | **String**|  | [optional] |
| **oauthSignature** | **String**|  | [optional] |
| **oauthTimestamp** | **String**|  | [optional] |
| **oauthNonce** | **String**|  | [optional] |
| **oauthVersion** | **String**|  | [optional] |
| **oauthVerifier** | **String**|  | [optional] |
| **oauthCallback** | **String**|  | [optional] |
| **oauthTokenSecret** | **String**|  | [optional] |
| **oauthCallbackConfirmed** | **String**|  | [optional] |

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
| **200** | Status 200 |  -  |

<a id="postOauthAccessToken_0"></a>
# **postOauthAccessToken_0**
> postOauthAccessToken_0(oauthConsumerKey, oauthToken, oauthSignatureMethod, oauthSignature, oauthTimestamp, oauthNonce, oauthVersion, oauthVerifier, oauthCallback, oauthTokenSecret, oauthCallbackConfirmed)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String oauthConsumerKey = "oauthConsumerKey_example"; // String | 
    String oauthToken = "oauthToken_example"; // String | 
    String oauthSignatureMethod = "oauthSignatureMethod_example"; // String | 
    String oauthSignature = "oauthSignature_example"; // String | 
    String oauthTimestamp = "oauthTimestamp_example"; // String | 
    String oauthNonce = "oauthNonce_example"; // String | 
    String oauthVersion = "oauthVersion_example"; // String | 
    String oauthVerifier = "oauthVerifier_example"; // String | 
    String oauthCallback = "oauthCallback_example"; // String | 
    String oauthTokenSecret = "oauthTokenSecret_example"; // String | 
    String oauthCallbackConfirmed = "oauthCallbackConfirmed_example"; // String | 
    try {
      apiInstance.postOauthAccessToken_0(oauthConsumerKey, oauthToken, oauthSignatureMethod, oauthSignature, oauthTimestamp, oauthNonce, oauthVersion, oauthVerifier, oauthCallback, oauthTokenSecret, oauthCallbackConfirmed);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#postOauthAccessToken_0");
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
| **oauthConsumerKey** | **String**|  | [optional] |
| **oauthToken** | **String**|  | [optional] |
| **oauthSignatureMethod** | **String**|  | [optional] |
| **oauthSignature** | **String**|  | [optional] |
| **oauthTimestamp** | **String**|  | [optional] |
| **oauthNonce** | **String**|  | [optional] |
| **oauthVersion** | **String**|  | [optional] |
| **oauthVerifier** | **String**|  | [optional] |
| **oauthCallback** | **String**|  | [optional] |
| **oauthTokenSecret** | **String**|  | [optional] |
| **oauthCallbackConfirmed** | **String**|  | [optional] |

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
| **200** | postAccessTokenRequest |  -  |

<a id="postOauthAuthorize_0"></a>
# **postOauthAuthorize_0**
> postOauthAuthorize_0(almighty, accessOrganisations, manageOrganisations, manageOrganisationsServices, manageOrganisationsApplications, manageOrganisationsMembers, accessOrganisationsBills, accessOrganisationsCreditCount, accessOrganisationsConsumptionStatistics, accessPersonalInformation, managePersonalInformation, manageSshKeys, manageServices, manageApplications, accessBills, accessCreditCount, accessConsumptionStatistics, cookie)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String almighty = "almighty_example"; // String | 
    String accessOrganisations = "accessOrganisations_example"; // String | 
    String manageOrganisations = "manageOrganisations_example"; // String | 
    String manageOrganisationsServices = "manageOrganisationsServices_example"; // String | 
    String manageOrganisationsApplications = "manageOrganisationsApplications_example"; // String | 
    String manageOrganisationsMembers = "manageOrganisationsMembers_example"; // String | 
    String accessOrganisationsBills = "accessOrganisationsBills_example"; // String | 
    String accessOrganisationsCreditCount = "accessOrganisationsCreditCount_example"; // String | 
    String accessOrganisationsConsumptionStatistics = "accessOrganisationsConsumptionStatistics_example"; // String | 
    String accessPersonalInformation = "accessPersonalInformation_example"; // String | 
    String managePersonalInformation = "managePersonalInformation_example"; // String | 
    String manageSshKeys = "manageSshKeys_example"; // String | 
    String manageServices = "manageServices_example"; // String | 
    String manageApplications = "manageApplications_example"; // String | 
    String accessBills = "accessBills_example"; // String | 
    String accessCreditCount = "accessCreditCount_example"; // String | 
    String accessConsumptionStatistics = "accessConsumptionStatistics_example"; // String | 
    String cookie = "cookie_example"; // String | 
    try {
      apiInstance.postOauthAuthorize_0(almighty, accessOrganisations, manageOrganisations, manageOrganisationsServices, manageOrganisationsApplications, manageOrganisationsMembers, accessOrganisationsBills, accessOrganisationsCreditCount, accessOrganisationsConsumptionStatistics, accessPersonalInformation, managePersonalInformation, manageSshKeys, manageServices, manageApplications, accessBills, accessCreditCount, accessConsumptionStatistics, cookie);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#postOauthAuthorize_0");
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
| **almighty** | **String**|  | [optional] |
| **accessOrganisations** | **String**|  | [optional] |
| **manageOrganisations** | **String**|  | [optional] |
| **manageOrganisationsServices** | **String**|  | [optional] |
| **manageOrganisationsApplications** | **String**|  | [optional] |
| **manageOrganisationsMembers** | **String**|  | [optional] |
| **accessOrganisationsBills** | **String**|  | [optional] |
| **accessOrganisationsCreditCount** | **String**|  | [optional] |
| **accessOrganisationsConsumptionStatistics** | **String**|  | [optional] |
| **accessPersonalInformation** | **String**|  | [optional] |
| **managePersonalInformation** | **String**|  | [optional] |
| **manageSshKeys** | **String**|  | [optional] |
| **manageServices** | **String**|  | [optional] |
| **manageApplications** | **String**|  | [optional] |
| **accessBills** | **String**|  | [optional] |
| **accessCreditCount** | **String**|  | [optional] |
| **accessConsumptionStatistics** | **String**|  | [optional] |
| **cookie** | **String**|  | [optional] |

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
| **200** | authorizeToken |  -  |

<a id="postOauthRequestToken_0"></a>
# **postOauthRequestToken_0**
> postOauthRequestToken_0(oauthConsumerKey, oauthToken, oauthSignatureMethod, oauthSignature, oauthTimestamp, oauthNonce, oauthVersion, oauthVerifier, oauthCallback, oauthTokenSecret, oauthCallbackConfirmed)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String oauthConsumerKey = "oauthConsumerKey_example"; // String | 
    String oauthToken = "oauthToken_example"; // String | 
    String oauthSignatureMethod = "oauthSignatureMethod_example"; // String | 
    String oauthSignature = "oauthSignature_example"; // String | 
    String oauthTimestamp = "oauthTimestamp_example"; // String | 
    String oauthNonce = "oauthNonce_example"; // String | 
    String oauthVersion = "oauthVersion_example"; // String | 
    String oauthVerifier = "oauthVerifier_example"; // String | 
    String oauthCallback = "oauthCallback_example"; // String | 
    String oauthTokenSecret = "oauthTokenSecret_example"; // String | 
    String oauthCallbackConfirmed = "oauthCallbackConfirmed_example"; // String | 
    try {
      apiInstance.postOauthRequestToken_0(oauthConsumerKey, oauthToken, oauthSignatureMethod, oauthSignature, oauthTimestamp, oauthNonce, oauthVersion, oauthVerifier, oauthCallback, oauthTokenSecret, oauthCallbackConfirmed);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#postOauthRequestToken_0");
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
| **oauthConsumerKey** | **String**|  | [optional] |
| **oauthToken** | **String**|  | [optional] |
| **oauthSignatureMethod** | **String**|  | [optional] |
| **oauthSignature** | **String**|  | [optional] |
| **oauthTimestamp** | **String**|  | [optional] |
| **oauthNonce** | **String**|  | [optional] |
| **oauthVersion** | **String**|  | [optional] |
| **oauthVerifier** | **String**|  | [optional] |
| **oauthCallback** | **String**|  | [optional] |
| **oauthTokenSecret** | **String**|  | [optional] |
| **oauthCallbackConfirmed** | **String**|  | [optional] |

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
| **200** | postReqTokenRequest |  -  |

