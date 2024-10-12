# AcmeChallengeSetsApi

All URIs are relative to *https://acmedns.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**acmednsAcmeChallengeSetsGet**](AcmeChallengeSetsApi.md#acmednsAcmeChallengeSetsGet) | **GET** /v1/acmeChallengeSets/{rootDomain} |  |
| [**acmednsAcmeChallengeSetsRotateChallenges**](AcmeChallengeSetsApi.md#acmednsAcmeChallengeSetsRotateChallenges) | **POST** /v1/acmeChallengeSets/{rootDomain}:rotateChallenges |  |


<a id="acmednsAcmeChallengeSetsGet"></a>
# **acmednsAcmeChallengeSetsGet**
> AcmeChallengeSet acmednsAcmeChallengeSetsGet(rootDomain, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Gets the ACME challenge set for a given domain name. Domain names must be provided in Punycode.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AcmeChallengeSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://acmedns.googleapis.com");

    AcmeChallengeSetsApi apiInstance = new AcmeChallengeSetsApi(defaultClient);
    String rootDomain = "rootDomain_example"; // String | Required. SLD + TLD domain name to list challenges. For example, this would be \"google.com\" for any FQDN under \"google.com\". That includes challenges for \"subdomain.google.com\". This MAY be Unicode or Punycode.
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
    try {
      AcmeChallengeSet result = apiInstance.acmednsAcmeChallengeSetsGet(rootDomain, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AcmeChallengeSetsApi#acmednsAcmeChallengeSetsGet");
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
| **rootDomain** | **String**| Required. SLD + TLD domain name to list challenges. For example, this would be \&quot;google.com\&quot; for any FQDN under \&quot;google.com\&quot;. That includes challenges for \&quot;subdomain.google.com\&quot;. This MAY be Unicode or Punycode. | |
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

### Return type

[**AcmeChallengeSet**](AcmeChallengeSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="acmednsAcmeChallengeSetsRotateChallenges"></a>
# **acmednsAcmeChallengeSetsRotateChallenges**
> AcmeChallengeSet acmednsAcmeChallengeSetsRotateChallenges(rootDomain, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, rotateChallengesRequest)



Rotate the ACME challenges for a given domain name. By default, removes any challenges that are older than 30 days. Domain names must be provided in Punycode.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AcmeChallengeSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://acmedns.googleapis.com");

    AcmeChallengeSetsApi apiInstance = new AcmeChallengeSetsApi(defaultClient);
    String rootDomain = "rootDomain_example"; // String | Required. SLD + TLD domain name to update records for. For example, this would be \"google.com\" for any FQDN under \"google.com\". That includes challenges for \"subdomain.google.com\". This MAY be Unicode or Punycode.
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
    RotateChallengesRequest rotateChallengesRequest = new RotateChallengesRequest(); // RotateChallengesRequest | 
    try {
      AcmeChallengeSet result = apiInstance.acmednsAcmeChallengeSetsRotateChallenges(rootDomain, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, rotateChallengesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AcmeChallengeSetsApi#acmednsAcmeChallengeSetsRotateChallenges");
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
| **rootDomain** | **String**| Required. SLD + TLD domain name to update records for. For example, this would be \&quot;google.com\&quot; for any FQDN under \&quot;google.com\&quot;. That includes challenges for \&quot;subdomain.google.com\&quot;. This MAY be Unicode or Punycode. | |
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
| **rotateChallengesRequest** | [**RotateChallengesRequest**](RotateChallengesRequest.md)|  | [optional] |

### Return type

[**AcmeChallengeSet**](AcmeChallengeSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

