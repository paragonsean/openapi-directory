# ReversePlanningPermissionApiApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postApplicantSingleApplicantMulti**](ReversePlanningPermissionApiApi.md#postApplicantSingleApplicantMulti) | **POST** /applicant_multi |  |
| [**postApplicantSingleApplicantSingle**](ReversePlanningPermissionApiApi.md#postApplicantSingleApplicantSingle) | **POST** /applicant_single |  |
| [**postFreeEndPointFree**](ReversePlanningPermissionApiApi.md#postFreeEndPointFree) | **POST** /free |  |
| [**postPartialAddresSinglePartialAddressSingle**](ReversePlanningPermissionApiApi.md#postPartialAddresSinglePartialAddressSingle) | **POST** /partial_address_single |  |
| [**postPartialAddressMultiPartialAddressMulti**](ReversePlanningPermissionApiApi.md#postPartialAddressMultiPartialAddressMulti) | **POST** /partial_address_multi |  |
| [**postPostcodeMultiPostcodeMulti**](ReversePlanningPermissionApiApi.md#postPostcodeMultiPostcodeMulti) | **POST** /postcode_multi |  |
| [**postPostcodeSinglePostcodeSingle**](ReversePlanningPermissionApiApi.md#postPostcodeSinglePostcodeSingle) | **POST** /postcode_single |  |
| [**postProposalMultiProposal**](ReversePlanningPermissionApiApi.md#postProposalMultiProposal) | **POST** /proposal |  |


<a id="postApplicantSingleApplicantMulti"></a>
# **postApplicantSingleApplicantMulti**
> postApplicantSingleApplicantMulti(payload)



Retrieve 50 planning applications for an applicant name (example: John Smith). Rate limit is 100/day;10/minute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReversePlanningPermissionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReversePlanningPermissionApiApi apiInstance = new ReversePlanningPermissionApiApi(defaultClient);
    PostApplicantSingleApplicantMultiRequest payload = new PostApplicantSingleApplicantMultiRequest(); // PostApplicantSingleApplicantMultiRequest | 
    try {
      apiInstance.postApplicantSingleApplicantMulti(payload);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReversePlanningPermissionApiApi#postApplicantSingleApplicantMulti");
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
| **payload** | [**PostApplicantSingleApplicantMultiRequest**](PostApplicantSingleApplicantMultiRequest.md)|  | |

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
| **200** | Success |  -  |

<a id="postApplicantSingleApplicantSingle"></a>
# **postApplicantSingleApplicantSingle**
> postApplicantSingleApplicantSingle(payload)



Retrieve a single planning application for an applicant (example: John Smith). Rate limit is 100/day;10/minute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReversePlanningPermissionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReversePlanningPermissionApiApi apiInstance = new ReversePlanningPermissionApiApi(defaultClient);
    PostApplicantSingleApplicantMultiRequest payload = new PostApplicantSingleApplicantMultiRequest(); // PostApplicantSingleApplicantMultiRequest | 
    try {
      apiInstance.postApplicantSingleApplicantSingle(payload);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReversePlanningPermissionApiApi#postApplicantSingleApplicantSingle");
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
| **payload** | [**PostApplicantSingleApplicantMultiRequest**](PostApplicantSingleApplicantMultiRequest.md)|  | |

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
| **200** | Success |  -  |

<a id="postFreeEndPointFree"></a>
# **postFreeEndPointFree**
> postFreeEndPointFree(payload)



Retrieve 1 planning application for proposal key word (example: Swimming Pool). Rate limit is 100/day;10/minute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReversePlanningPermissionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReversePlanningPermissionApiApi apiInstance = new ReversePlanningPermissionApiApi(defaultClient);
    PostFreeEndPointFreeRequest payload = new PostFreeEndPointFreeRequest(); // PostFreeEndPointFreeRequest | 
    try {
      apiInstance.postFreeEndPointFree(payload);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReversePlanningPermissionApiApi#postFreeEndPointFree");
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
| **payload** | [**PostFreeEndPointFreeRequest**](PostFreeEndPointFreeRequest.md)|  | |

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
| **200** | Success |  -  |

<a id="postPartialAddresSinglePartialAddressSingle"></a>
# **postPartialAddresSinglePartialAddressSingle**
> postPartialAddresSinglePartialAddressSingle(payload)



Retrieve a single planning application for a partial address (example: Station Road). Rate limit is 100/day;10/minute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReversePlanningPermissionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReversePlanningPermissionApiApi apiInstance = new ReversePlanningPermissionApiApi(defaultClient);
    PostPartialAddressMultiPartialAddressMultiRequest payload = new PostPartialAddressMultiPartialAddressMultiRequest(); // PostPartialAddressMultiPartialAddressMultiRequest | 
    try {
      apiInstance.postPartialAddresSinglePartialAddressSingle(payload);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReversePlanningPermissionApiApi#postPartialAddresSinglePartialAddressSingle");
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
| **payload** | [**PostPartialAddressMultiPartialAddressMultiRequest**](PostPartialAddressMultiPartialAddressMultiRequest.md)|  | |

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
| **200** | Success |  -  |

<a id="postPartialAddressMultiPartialAddressMulti"></a>
# **postPartialAddressMultiPartialAddressMulti**
> postPartialAddressMultiPartialAddressMulti(payload)



Retrieve 50 planning applications for a partial address (example: Station Road). Rate limit is 100/day;10/minute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReversePlanningPermissionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReversePlanningPermissionApiApi apiInstance = new ReversePlanningPermissionApiApi(defaultClient);
    PostPartialAddressMultiPartialAddressMultiRequest payload = new PostPartialAddressMultiPartialAddressMultiRequest(); // PostPartialAddressMultiPartialAddressMultiRequest | 
    try {
      apiInstance.postPartialAddressMultiPartialAddressMulti(payload);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReversePlanningPermissionApiApi#postPartialAddressMultiPartialAddressMulti");
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
| **payload** | [**PostPartialAddressMultiPartialAddressMultiRequest**](PostPartialAddressMultiPartialAddressMultiRequest.md)|  | |

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
| **200** | Success |  -  |

<a id="postPostcodeMultiPostcodeMulti"></a>
# **postPostcodeMultiPostcodeMulti**
> postPostcodeMultiPostcodeMulti(payload)



Retrieve 50 planning applications for a postcode. Rate limit is 100/day;10/minute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReversePlanningPermissionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReversePlanningPermissionApiApi apiInstance = new ReversePlanningPermissionApiApi(defaultClient);
    PostPostcodeMultiPostcodeMultiRequest payload = new PostPostcodeMultiPostcodeMultiRequest(); // PostPostcodeMultiPostcodeMultiRequest | 
    try {
      apiInstance.postPostcodeMultiPostcodeMulti(payload);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReversePlanningPermissionApiApi#postPostcodeMultiPostcodeMulti");
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
| **payload** | [**PostPostcodeMultiPostcodeMultiRequest**](PostPostcodeMultiPostcodeMultiRequest.md)|  | |

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
| **200** | Success |  -  |

<a id="postPostcodeSinglePostcodeSingle"></a>
# **postPostcodeSinglePostcodeSingle**
> postPostcodeSinglePostcodeSingle(payload)



Retrieve a single planning application for a postcode. Rate limit is 100/day;10/minute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReversePlanningPermissionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReversePlanningPermissionApiApi apiInstance = new ReversePlanningPermissionApiApi(defaultClient);
    PostPostcodeMultiPostcodeMultiRequest payload = new PostPostcodeMultiPostcodeMultiRequest(); // PostPostcodeMultiPostcodeMultiRequest | 
    try {
      apiInstance.postPostcodeSinglePostcodeSingle(payload);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReversePlanningPermissionApiApi#postPostcodeSinglePostcodeSingle");
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
| **payload** | [**PostPostcodeMultiPostcodeMultiRequest**](PostPostcodeMultiPostcodeMultiRequest.md)|  | |

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
| **200** | Success |  -  |

<a id="postProposalMultiProposal"></a>
# **postProposalMultiProposal**
> postProposalMultiProposal(payload)



Retrieve 50 planning applications for proposal key word (example: Swimming Pool). Rate limit is 100/day;10/minute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReversePlanningPermissionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReversePlanningPermissionApiApi apiInstance = new ReversePlanningPermissionApiApi(defaultClient);
    PostProposalMultiProposalRequest payload = new PostProposalMultiProposalRequest(); // PostProposalMultiProposalRequest | 
    try {
      apiInstance.postProposalMultiProposal(payload);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReversePlanningPermissionApiApi#postProposalMultiProposal");
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
| **payload** | [**PostProposalMultiProposalRequest**](PostProposalMultiProposalRequest.md)|  | |

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
| **200** | Success |  -  |

