# BetaAppReviewSubmissionsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**betaAppReviewSubmissionsBuildGetToOneRelated**](BetaAppReviewSubmissionsApi.md#betaAppReviewSubmissionsBuildGetToOneRelated) | **GET** /v1/betaAppReviewSubmissions/{id}/build |  |
| [**betaAppReviewSubmissionsCreateInstance**](BetaAppReviewSubmissionsApi.md#betaAppReviewSubmissionsCreateInstance) | **POST** /v1/betaAppReviewSubmissions |  |
| [**betaAppReviewSubmissionsGetCollection**](BetaAppReviewSubmissionsApi.md#betaAppReviewSubmissionsGetCollection) | **GET** /v1/betaAppReviewSubmissions |  |
| [**betaAppReviewSubmissionsGetInstance**](BetaAppReviewSubmissionsApi.md#betaAppReviewSubmissionsGetInstance) | **GET** /v1/betaAppReviewSubmissions/{id} |  |


<a id="betaAppReviewSubmissionsBuildGetToOneRelated"></a>
# **betaAppReviewSubmissionsBuildGetToOneRelated**
> BuildResponse betaAppReviewSubmissionsBuildGetToOneRelated(id, fieldsBuilds)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaAppReviewSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaAppReviewSubmissionsApi apiInstance = new BetaAppReviewSubmissionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    try {
      BuildResponse result = apiInstance.betaAppReviewSubmissionsBuildGetToOneRelated(id, fieldsBuilds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaAppReviewSubmissionsApi#betaAppReviewSubmissionsBuildGetToOneRelated");
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
| **id** | **String**| the id of the requested resource | |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |

### Return type

[**BuildResponse**](BuildResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Related resource |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="betaAppReviewSubmissionsCreateInstance"></a>
# **betaAppReviewSubmissionsCreateInstance**
> BetaAppReviewSubmissionResponse betaAppReviewSubmissionsCreateInstance(betaAppReviewSubmissionCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaAppReviewSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaAppReviewSubmissionsApi apiInstance = new BetaAppReviewSubmissionsApi(defaultClient);
    BetaAppReviewSubmissionCreateRequest betaAppReviewSubmissionCreateRequest = new BetaAppReviewSubmissionCreateRequest(); // BetaAppReviewSubmissionCreateRequest | BetaAppReviewSubmission representation
    try {
      BetaAppReviewSubmissionResponse result = apiInstance.betaAppReviewSubmissionsCreateInstance(betaAppReviewSubmissionCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaAppReviewSubmissionsApi#betaAppReviewSubmissionsCreateInstance");
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
| **betaAppReviewSubmissionCreateRequest** | [**BetaAppReviewSubmissionCreateRequest**](BetaAppReviewSubmissionCreateRequest.md)| BetaAppReviewSubmission representation | |

### Return type

[**BetaAppReviewSubmissionResponse**](BetaAppReviewSubmissionResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single BetaAppReviewSubmission |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="betaAppReviewSubmissionsGetCollection"></a>
# **betaAppReviewSubmissionsGetCollection**
> BetaAppReviewSubmissionsResponse betaAppReviewSubmissionsGetCollection(filterBuild, filterBetaReviewState, fieldsBetaAppReviewSubmissions, limit, include, fieldsBuilds)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaAppReviewSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaAppReviewSubmissionsApi apiInstance = new BetaAppReviewSubmissionsApi(defaultClient);
    List<String> filterBuild = Arrays.asList(); // List<String> | filter by id(s) of related 'build'
    List<String> filterBetaReviewState = Arrays.asList(); // List<String> | filter by attribute 'betaReviewState'
    List<String> fieldsBetaAppReviewSubmissions = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaAppReviewSubmissions
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    try {
      BetaAppReviewSubmissionsResponse result = apiInstance.betaAppReviewSubmissionsGetCollection(filterBuild, filterBetaReviewState, fieldsBetaAppReviewSubmissions, limit, include, fieldsBuilds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaAppReviewSubmissionsApi#betaAppReviewSubmissionsGetCollection");
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
| **filterBuild** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;build&#39; | |
| **filterBetaReviewState** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;betaReviewState&#39; | [optional] [enum: WAITING_FOR_REVIEW, IN_REVIEW, REJECTED, APPROVED] |
| **fieldsBetaAppReviewSubmissions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaAppReviewSubmissions | [optional] [enum: betaReviewState, build] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: build] |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |

### Return type

[**BetaAppReviewSubmissionsResponse**](BetaAppReviewSubmissionsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of BetaAppReviewSubmissions |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

<a id="betaAppReviewSubmissionsGetInstance"></a>
# **betaAppReviewSubmissionsGetInstance**
> BetaAppReviewSubmissionResponse betaAppReviewSubmissionsGetInstance(id, fieldsBetaAppReviewSubmissions, include, fieldsBuilds)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaAppReviewSubmissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaAppReviewSubmissionsApi apiInstance = new BetaAppReviewSubmissionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBetaAppReviewSubmissions = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaAppReviewSubmissions
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    try {
      BetaAppReviewSubmissionResponse result = apiInstance.betaAppReviewSubmissionsGetInstance(id, fieldsBetaAppReviewSubmissions, include, fieldsBuilds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaAppReviewSubmissionsApi#betaAppReviewSubmissionsGetInstance");
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
| **id** | **String**| the id of the requested resource | |
| **fieldsBetaAppReviewSubmissions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaAppReviewSubmissions | [optional] [enum: betaReviewState, build] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: build] |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |

### Return type

[**BetaAppReviewSubmissionResponse**](BetaAppReviewSubmissionResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single BetaAppReviewSubmission |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

