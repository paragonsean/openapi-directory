# DefaultApi

All URIs are relative to *https://api.roaring.io/company/1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyBoardMembersGet**](DefaultApi.md#companyBoardMembersGet) | **GET** /company-board-members |  |
| [**companyBoardMembersPost**](DefaultApi.md#companyBoardMembersPost) | **POST** /company-board-members |  |
| [**companyCreditDecisionGet**](DefaultApi.md#companyCreditDecisionGet) | **GET** /company-credit-decision |  |
| [**companyEconomyOverviewGet**](DefaultApi.md#companyEconomyOverviewGet) | **GET** /company-economy-overview |  |
| [**companyEconomyOverviewPost**](DefaultApi.md#companyEconomyOverviewPost) | **POST** /company-economy-overview |  |
| [**companyEventPost**](DefaultApi.md#companyEventPost) | **POST** /company-event |  |
| [**companyOverviewGet**](DefaultApi.md#companyOverviewGet) | **GET** /company-overview |  |
| [**companyOverviewPost**](DefaultApi.md#companyOverviewPost) | **POST** /company-overview |  |
| [**companySignatoryGet**](DefaultApi.md#companySignatoryGet) | **GET** /company-signatory |  |
| [**companySignatoryPost**](DefaultApi.md#companySignatoryPost) | **POST** /company-signatory |  |
| [**companySimpleSearchGet**](DefaultApi.md#companySimpleSearchGet) | **GET** /company-simple-search |  |


<a id="companyBoardMembersGet"></a>
# **companyBoardMembersGet**
> CompanyBoardMembersResult companyBoardMembersGet(countryCode, companyId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.roaring.io/company/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String countryCode = "countryCode_example"; // String | Country code for the company
    String companyId = "companyId_example"; // String | Company identification for the company
    try {
      CompanyBoardMembersResult result = apiInstance.companyBoardMembersGet(countryCode, companyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyBoardMembersGet");
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
| **countryCode** | **String**| Country code for the company | |
| **companyId** | **String**| Company identification for the company | |

### Return type

[**CompanyBoardMembersResult**](CompanyBoardMembersResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK, successful response |  -  |
| **400** | Returned when something is wrong in the request, e.g. too many entities are requested or arguments are missing |  -  |
| **404** | Requested resource could not be found |  -  |
| **500** | An internal server error occurred, please contact the system administrator with information on the error |  -  |

<a id="companyBoardMembersPost"></a>
# **companyBoardMembersPost**
> CompanyBoardMembersMulti companyBoardMembersPost(countryCode, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.roaring.io/company/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String countryCode = "countryCode_example"; // String | Country code for the company
    CompanyLookupRequestBody body = new CompanyLookupRequestBody(); // CompanyLookupRequestBody | Request body with company identifiers to lookup
    try {
      CompanyBoardMembersMulti result = apiInstance.companyBoardMembersPost(countryCode, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyBoardMembersPost");
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
| **countryCode** | **String**| Country code for the company | |
| **body** | [**CompanyLookupRequestBody**](CompanyLookupRequestBody.md)| Request body with company identifiers to lookup | |

### Return type

[**CompanyBoardMembersMulti**](CompanyBoardMembersMulti.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK, successfull response |  -  |
| **400** | Returned when something is wrong in the request, e.g. too many entities are requested or arguments are missing |  -  |
| **404** | Requested resource could not be found |  -  |
| **500** | An internal server error occurred, please contact the system administrator with information on the error |  -  |

<a id="companyCreditDecisionGet"></a>
# **companyCreditDecisionGet**
> CompanyCreditDecisionResult companyCreditDecisionGet(countryCode, companyId, template)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.roaring.io/company/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String countryCode = "countryCode_example"; // String | Country code for the company
    String companyId = "companyId_example"; // String | Company identification for the company
    String template = "template_example"; // String | Template for credit decision
    try {
      CompanyCreditDecisionResult result = apiInstance.companyCreditDecisionGet(countryCode, companyId, template);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyCreditDecisionGet");
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
| **countryCode** | **String**| Country code for the company | |
| **companyId** | **String**| Company identification for the company | |
| **template** | **String**| Template for credit decision | |

### Return type

[**CompanyCreditDecisionResult**](CompanyCreditDecisionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK, successful response |  -  |
| **400** | Returned when something is wrong in the request, e.g. too many entities are requested or arguments are missing |  -  |
| **404** | Requested resource could not be found |  -  |
| **500** | An internal server error occurred, please contact the system administrator with information on the error |  -  |

<a id="companyEconomyOverviewGet"></a>
# **companyEconomyOverviewGet**
> CompanyEconomyOverviewResult companyEconomyOverviewGet(countryCode, companyId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.roaring.io/company/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String countryCode = "countryCode_example"; // String | Country code for the company
    String companyId = "companyId_example"; // String | Company identification for the company
    try {
      CompanyEconomyOverviewResult result = apiInstance.companyEconomyOverviewGet(countryCode, companyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyEconomyOverviewGet");
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
| **countryCode** | **String**| Country code for the company | |
| **companyId** | **String**| Company identification for the company | |

### Return type

[**CompanyEconomyOverviewResult**](CompanyEconomyOverviewResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK, successful response |  -  |
| **400** | Returned when something is wrong in the request, e.g. too many entities are requested or arguments are missing |  -  |
| **404** | Requested resource could not be found |  -  |
| **500** | An internal server error occurred, please contact the system administrator with information on the error |  -  |

<a id="companyEconomyOverviewPost"></a>
# **companyEconomyOverviewPost**
> CompanyEconomyOverviewMulti companyEconomyOverviewPost(countryCode, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.roaring.io/company/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String countryCode = "countryCode_example"; // String | Country code for the company
    CompanyLookupRequestBody body = new CompanyLookupRequestBody(); // CompanyLookupRequestBody | Request body with company identifiers to lookup
    try {
      CompanyEconomyOverviewMulti result = apiInstance.companyEconomyOverviewPost(countryCode, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyEconomyOverviewPost");
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
| **countryCode** | **String**| Country code for the company | |
| **body** | [**CompanyLookupRequestBody**](CompanyLookupRequestBody.md)| Request body with company identifiers to lookup | |

### Return type

[**CompanyEconomyOverviewMulti**](CompanyEconomyOverviewMulti.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK, successfull response |  -  |
| **400** | Returned when something is wrong in the request, e.g. too many entities are requested or arguments are missing |  -  |
| **404** | Requested resource could not be found |  -  |
| **500** | An internal server error occurred, please contact the system administrator with information on the error |  -  |

<a id="companyEventPost"></a>
# **companyEventPost**
> CompanyEventResult companyEventPost(countryCode, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.roaring.io/company/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String countryCode = "countryCode_example"; // String | Country code for the company
    CompanyEventRequestBody body = new CompanyEventRequestBody(); // CompanyEventRequestBody | Request body with company identifiers to lookup
    try {
      CompanyEventResult result = apiInstance.companyEventPost(countryCode, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyEventPost");
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
| **countryCode** | **String**| Country code for the company | |
| **body** | [**CompanyEventRequestBody**](CompanyEventRequestBody.md)| Request body with company identifiers to lookup | |

### Return type

[**CompanyEventResult**](CompanyEventResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK, successfull response |  -  |
| **400** | Returned when something is wrong in the request, e.g. too many entities are requested or arguments are missing |  -  |
| **404** | Requested resource could not be found |  -  |
| **500** | An internal server error occurred, please contact the system administrator with information on the error |  -  |

<a id="companyOverviewGet"></a>
# **companyOverviewGet**
> CompanyOverviewResult companyOverviewGet(countryCode, companyId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.roaring.io/company/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String countryCode = "countryCode_example"; // String | Country code for the company
    String companyId = "companyId_example"; // String | Company identification for the company
    try {
      CompanyOverviewResult result = apiInstance.companyOverviewGet(countryCode, companyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyOverviewGet");
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
| **countryCode** | **String**| Country code for the company | |
| **companyId** | **String**| Company identification for the company | |

### Return type

[**CompanyOverviewResult**](CompanyOverviewResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK, successfull response |  -  |
| **400** | Returned when something is wrong in the request, e.g. too many entities are requested or arguments are missing |  -  |
| **404** | Requested resource could not be found |  -  |
| **500** | An internal server error occurred, please contact the system administrator with information on the error |  -  |

<a id="companyOverviewPost"></a>
# **companyOverviewPost**
> CompanyOverviewMulti companyOverviewPost(countryCode, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.roaring.io/company/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String countryCode = "countryCode_example"; // String | Country code for the company
    CompanyLookupRequestBody body = new CompanyLookupRequestBody(); // CompanyLookupRequestBody | Request body with company identifiers to lookup
    try {
      CompanyOverviewMulti result = apiInstance.companyOverviewPost(countryCode, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companyOverviewPost");
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
| **countryCode** | **String**| Country code for the company | |
| **body** | [**CompanyLookupRequestBody**](CompanyLookupRequestBody.md)| Request body with company identifiers to lookup | |

### Return type

[**CompanyOverviewMulti**](CompanyOverviewMulti.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK, successfull response |  -  |
| **400** | Returned when something is wrong in the request, e.g. too many entities are requested or arguments are missing |  -  |
| **404** | Requested resource could not be found |  -  |
| **500** | An internal server error occurred, please contact the system administrator with information on the error |  -  |

<a id="companySignatoryGet"></a>
# **companySignatoryGet**
> CompanySignatoryResult companySignatoryGet(countryCode, companyId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.roaring.io/company/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String countryCode = "countryCode_example"; // String | Country code for the company
    String companyId = "companyId_example"; // String | Company identification for the company
    try {
      CompanySignatoryResult result = apiInstance.companySignatoryGet(countryCode, companyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companySignatoryGet");
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
| **countryCode** | **String**| Country code for the company | |
| **companyId** | **String**| Company identification for the company | |

### Return type

[**CompanySignatoryResult**](CompanySignatoryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK, successful response |  -  |
| **400** | Returned when something is wrong in the request, e.g. too many entities are requested or arguments are missing |  -  |
| **404** | Requested resource could not be found |  -  |
| **500** | An internal server error occurred, please contact the system administrator with information on the error |  -  |

<a id="companySignatoryPost"></a>
# **companySignatoryPost**
> CompanySignatoryMulti companySignatoryPost(countryCode, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.roaring.io/company/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String countryCode = "countryCode_example"; // String | Country code for the company
    CompanyLookupRequestBody body = new CompanyLookupRequestBody(); // CompanyLookupRequestBody | Request body with company identifiers to lookup
    try {
      CompanySignatoryMulti result = apiInstance.companySignatoryPost(countryCode, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companySignatoryPost");
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
| **countryCode** | **String**| Country code for the company | |
| **body** | [**CompanyLookupRequestBody**](CompanyLookupRequestBody.md)| Request body with company identifiers to lookup | |

### Return type

[**CompanySignatoryMulti**](CompanySignatoryMulti.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK, successfull response |  -  |
| **400** | Returned when something is wrong in the request, e.g. too many entities are requested or arguments are missing |  -  |
| **404** | Requested resource could not be found |  -  |
| **500** | An internal server error occurred, please contact the system administrator with information on the error |  -  |

<a id="companySimpleSearchGet"></a>
# **companySimpleSearchGet**
> companySimpleSearchGet(countryCode, companyName, town)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.roaring.io/company/1.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String countryCode = "countryCode_example"; // String | Country code for the company
    String companyName = "companyName_example"; // String | Company name
    String town = "town_example"; // String | Town
    try {
      apiInstance.companySimpleSearchGet(countryCode, companyName, town);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#companySimpleSearchGet");
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
| **countryCode** | **String**| Country code for the company | |
| **companyName** | **String**| Company name | [optional] |
| **town** | **String**| Town | [optional] |

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
| **200** |  |  -  |

