# NumbersV2BundleApi

All URIs are relative to *https://numbers.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBundle**](NumbersV2BundleApi.md#createBundle) | **POST** /v2/RegulatoryCompliance/Bundles |  |
| [**deleteBundle**](NumbersV2BundleApi.md#deleteBundle) | **DELETE** /v2/RegulatoryCompliance/Bundles/{Sid} |  |
| [**fetchBundle**](NumbersV2BundleApi.md#fetchBundle) | **GET** /v2/RegulatoryCompliance/Bundles/{Sid} |  |
| [**listBundle**](NumbersV2BundleApi.md#listBundle) | **GET** /v2/RegulatoryCompliance/Bundles |  |
| [**updateBundle**](NumbersV2BundleApi.md#updateBundle) | **POST** /v2/RegulatoryCompliance/Bundles/{Sid} |  |


<a id="createBundle"></a>
# **createBundle**
> NumbersV2RegulatoryComplianceBundle createBundle(email, friendlyName, endUserType, isoCountry, numberType, regulationSid, statusCallback)



Create a new Bundle.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2BundleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2BundleApi apiInstance = new NumbersV2BundleApi(defaultClient);
    String email = "email_example"; // String | The email address that will receive updates when the Bundle resource changes status.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    BundleEnumEndUserType endUserType = BundleEnumEndUserType.fromValue("individual"); // BundleEnumEndUserType | 
    String isoCountry = "isoCountry_example"; // String | The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Bundle's phone number country ownership request.
    String numberType = "numberType_example"; // String | The type of phone number of the Bundle's ownership request. Can be `local`, `mobile`, `national`, or `toll free`.
    String regulationSid = "regulationSid_example"; // String | The unique string of a regulation that is associated to the Bundle resource.
    URI statusCallback = new URI(); // URI | The URL we call to inform your application of status changes.
    try {
      NumbersV2RegulatoryComplianceBundle result = apiInstance.createBundle(email, friendlyName, endUserType, isoCountry, numberType, regulationSid, statusCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2BundleApi#createBundle");
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
| **email** | **String**| The email address that will receive updates when the Bundle resource changes status. | |
| **friendlyName** | **String**| The string that you assigned to describe the resource. | |
| **endUserType** | **BundleEnumEndUserType**|  | [optional] [enum: individual, business] |
| **isoCountry** | **String**| The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Bundle&#39;s phone number country ownership request. | [optional] |
| **numberType** | **String**| The type of phone number of the Bundle&#39;s ownership request. Can be &#x60;local&#x60;, &#x60;mobile&#x60;, &#x60;national&#x60;, or &#x60;toll free&#x60;. | [optional] |
| **regulationSid** | **String**| The unique string of a regulation that is associated to the Bundle resource. | [optional] |
| **statusCallback** | **URI**| The URL we call to inform your application of status changes. | [optional] |

### Return type

[**NumbersV2RegulatoryComplianceBundle**](NumbersV2RegulatoryComplianceBundle.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteBundle"></a>
# **deleteBundle**
> deleteBundle(sid)



Delete a specific Bundle.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2BundleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2BundleApi apiInstance = new NumbersV2BundleApi(defaultClient);
    String sid = "sid_example"; // String | The unique string that we created to identify the Bundle resource.
    try {
      apiInstance.deleteBundle(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2BundleApi#deleteBundle");
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
| **sid** | **String**| The unique string that we created to identify the Bundle resource. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchBundle"></a>
# **fetchBundle**
> NumbersV2RegulatoryComplianceBundle fetchBundle(sid)



Fetch a specific Bundle instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2BundleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2BundleApi apiInstance = new NumbersV2BundleApi(defaultClient);
    String sid = "sid_example"; // String | The unique string that we created to identify the Bundle resource.
    try {
      NumbersV2RegulatoryComplianceBundle result = apiInstance.fetchBundle(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2BundleApi#fetchBundle");
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
| **sid** | **String**| The unique string that we created to identify the Bundle resource. | |

### Return type

[**NumbersV2RegulatoryComplianceBundle**](NumbersV2RegulatoryComplianceBundle.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listBundle"></a>
# **listBundle**
> ListBundleResponse listBundle(status, friendlyName, regulationSid, isoCountry, numberType, hasValidUntilDate, sortBy, sortDirection, validUntilDate, validUntilDateLessThan, validUntilDateGreaterThan, pageSize, page, pageToken)



Retrieve a list of all Bundles for an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2BundleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2BundleApi apiInstance = new NumbersV2BundleApi(defaultClient);
    BundleEnumStatus status = BundleEnumStatus.fromValue("draft"); // BundleEnumStatus | The verification status of the Bundle resource. Please refer to [Bundle Statuses](https://www.twilio.com/docs/phone-numbers/regulatory/api/bundles#bundle-statuses) for more details.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource. The column can contain 255 variable characters.
    String regulationSid = "regulationSid_example"; // String | The unique string of a [Regulation resource](https://www.twilio.com/docs/phone-numbers/regulatory/api/regulations) that is associated to the Bundle resource.
    String isoCountry = "isoCountry_example"; // String | The 2-digit [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Bundle's phone number country ownership request.
    String numberType = "numberType_example"; // String | The type of phone number of the Bundle's ownership request. Can be `local`, `mobile`, `national`, or `tollfree`.
    Boolean hasValidUntilDate = true; // Boolean | Indicates that the Bundle is a valid Bundle until a specified expiration date.
    BundleEnumSortBy sortBy = BundleEnumSortBy.fromValue("valid-until"); // BundleEnumSortBy | Can be `valid-until` or `date-updated`. Defaults to `date-created`.
    BundleEnumSortDirection sortDirection = BundleEnumSortDirection.fromValue("ASC"); // BundleEnumSortDirection | Default is `DESC`. Can be `ASC` or `DESC`.
    OffsetDateTime validUntilDate = OffsetDateTime.now(); // OffsetDateTime | Date to filter Bundles having their `valid_until_date` before or after the specified date. Can be `ValidUntilDate>=` or `ValidUntilDate<=`. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
    OffsetDateTime validUntilDateLessThan = OffsetDateTime.now(); // OffsetDateTime | Date to filter Bundles having their `valid_until_date` before or after the specified date. Can be `ValidUntilDate>=` or `ValidUntilDate<=`. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
    OffsetDateTime validUntilDateGreaterThan = OffsetDateTime.now(); // OffsetDateTime | Date to filter Bundles having their `valid_until_date` before or after the specified date. Can be `ValidUntilDate>=` or `ValidUntilDate<=`. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListBundleResponse result = apiInstance.listBundle(status, friendlyName, regulationSid, isoCountry, numberType, hasValidUntilDate, sortBy, sortDirection, validUntilDate, validUntilDateLessThan, validUntilDateGreaterThan, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2BundleApi#listBundle");
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
| **status** | **BundleEnumStatus**| The verification status of the Bundle resource. Please refer to [Bundle Statuses](https://www.twilio.com/docs/phone-numbers/regulatory/api/bundles#bundle-statuses) for more details. | [optional] [enum: draft, pending-review, in-review, twilio-rejected, twilio-approved, provisionally-approved] |
| **friendlyName** | **String**| The string that you assigned to describe the resource. The column can contain 255 variable characters. | [optional] |
| **regulationSid** | **String**| The unique string of a [Regulation resource](https://www.twilio.com/docs/phone-numbers/regulatory/api/regulations) that is associated to the Bundle resource. | [optional] |
| **isoCountry** | **String**| The 2-digit [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Bundle&#39;s phone number country ownership request. | [optional] |
| **numberType** | **String**| The type of phone number of the Bundle&#39;s ownership request. Can be &#x60;local&#x60;, &#x60;mobile&#x60;, &#x60;national&#x60;, or &#x60;tollfree&#x60;. | [optional] |
| **hasValidUntilDate** | **Boolean**| Indicates that the Bundle is a valid Bundle until a specified expiration date. | [optional] |
| **sortBy** | **BundleEnumSortBy**| Can be &#x60;valid-until&#x60; or &#x60;date-updated&#x60;. Defaults to &#x60;date-created&#x60;. | [optional] [enum: valid-until, date-updated] |
| **sortDirection** | **BundleEnumSortDirection**| Default is &#x60;DESC&#x60;. Can be &#x60;ASC&#x60; or &#x60;DESC&#x60;. | [optional] [enum: ASC, DESC] |
| **validUntilDate** | **OffsetDateTime**| Date to filter Bundles having their &#x60;valid_until_date&#x60; before or after the specified date. Can be &#x60;ValidUntilDate&gt;&#x3D;&#x60; or &#x60;ValidUntilDate&lt;&#x3D;&#x60;. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format. | [optional] |
| **validUntilDateLessThan** | **OffsetDateTime**| Date to filter Bundles having their &#x60;valid_until_date&#x60; before or after the specified date. Can be &#x60;ValidUntilDate&gt;&#x3D;&#x60; or &#x60;ValidUntilDate&lt;&#x3D;&#x60;. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format. | [optional] |
| **validUntilDateGreaterThan** | **OffsetDateTime**| Date to filter Bundles having their &#x60;valid_until_date&#x60; before or after the specified date. Can be &#x60;ValidUntilDate&gt;&#x3D;&#x60; or &#x60;ValidUntilDate&lt;&#x3D;&#x60;. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListBundleResponse**](ListBundleResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateBundle"></a>
# **updateBundle**
> NumbersV2RegulatoryComplianceBundle updateBundle(sid, email, friendlyName, status, statusCallback)



Updates a Bundle in an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2BundleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2BundleApi apiInstance = new NumbersV2BundleApi(defaultClient);
    String sid = "sid_example"; // String | The unique string that we created to identify the Bundle resource.
    String email = "email_example"; // String | The email address that will receive updates when the Bundle resource changes status.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    BundleEnumStatus status = BundleEnumStatus.fromValue("draft"); // BundleEnumStatus | 
    URI statusCallback = new URI(); // URI | The URL we call to inform your application of status changes.
    try {
      NumbersV2RegulatoryComplianceBundle result = apiInstance.updateBundle(sid, email, friendlyName, status, statusCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2BundleApi#updateBundle");
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
| **sid** | **String**| The unique string that we created to identify the Bundle resource. | |
| **email** | **String**| The email address that will receive updates when the Bundle resource changes status. | [optional] |
| **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] |
| **status** | **BundleEnumStatus**|  | [optional] [enum: draft, pending-review, in-review, twilio-rejected, twilio-approved, provisionally-approved] |
| **statusCallback** | **URI**| The URL we call to inform your application of status changes. | [optional] |

### Return type

[**NumbersV2RegulatoryComplianceBundle**](NumbersV2RegulatoryComplianceBundle.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

