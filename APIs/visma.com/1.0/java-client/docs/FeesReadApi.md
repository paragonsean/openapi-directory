# FeesReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**flatRatesGetAllFlatRates**](FeesReadApi.md#flatRatesGetAllFlatRates) | **GET** /v1/flatrates | Get all flat rates |
| [**flatRatesGetFlatrate**](FeesReadApi.md#flatRatesGetFlatrate) | **GET** /v1/flatrates/{guid} | Get flat rate. |
| [**flatRatesGetFlatratesForProject**](FeesReadApi.md#flatRatesGetFlatratesForProject) | **GET** /v1/projects/{projectGuid}/flatrates | Get project&#39;s flat rates. |
| [**projectFeesGetDeletedProjectFees**](FeesReadApi.md#projectFeesGetDeletedProjectFees) | **GET** /v1/deletedprojectfees | Get the deleted project fees. |
| [**projectFeesGetProjectFee**](FeesReadApi.md#projectFeesGetProjectFee) | **GET** /v1/projectfees/{guid} | Get projectFee by ID. |
| [**projectFeesGetProjectFeesByToken**](FeesReadApi.md#projectFeesGetProjectFeesByToken) | **GET** /v1/projectfees | Get the project fees. |
| [**projectFeesGetProjectFeesForProject**](FeesReadApi.md#projectFeesGetProjectFeesForProject) | **GET** /v1/projects/{projectGuid}/projectfees | Get all the project fees for a project |
| [**projectFeesGetUserProjectFees**](FeesReadApi.md#projectFeesGetUserProjectFees) | **GET** /v1/users/{userGuid}/projectfees | Get all the projectFees for a user |
| [**projectRecurringFeeRulesGetProjectRecurringFeeRule**](FeesReadApi.md#projectRecurringFeeRulesGetProjectRecurringFeeRule) | **GET** /v1/projectrecurringfeerules/{guid} | Get project&#39;s RecurringFeeRule by ID. |
| [**projectRecurringFeeRulesGetProjectRecurringFeeRules**](FeesReadApi.md#projectRecurringFeeRulesGetProjectRecurringFeeRules) | **GET** /v1/projectrecurringfeerules | Get the recurring fee rules. |
| [**projectRecurringFeeRulesGetProjectRecurringFeeRulesForProject**](FeesReadApi.md#projectRecurringFeeRulesGetProjectRecurringFeeRulesForProject) | **GET** /v1/projects/{projectGuid}/projectrecurringfeerules | Get all the Recurring Fee Rules for a project |


<a id="flatRatesGetAllFlatRates"></a>
# **flatRatesGetAllFlatRates**
> List&lt;FlatRateOutputModel&gt; flatRatesGetAllFlatRates(pageToken, rowCount, changedSince, invoiceGuid)

Get all flat rates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesReadApi apiInstance = new FeesReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | Optional: Page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get flat rates that have been added or changed after this date time (greater or equal).
    String invoiceGuid = "invoiceGuid_example"; // String | Optional: Get flat rates by invoice guid. Default all.
    try {
      List<FlatRateOutputModel> result = apiInstance.flatRatesGetAllFlatRates(pageToken, rowCount, changedSince, invoiceGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesReadApi#flatRatesGetAllFlatRates");
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
| **pageToken** | **String**| Optional: Page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get flat rates that have been added or changed after this date time (greater or equal). | [optional] |
| **invoiceGuid** | **String**| Optional: Get flat rates by invoice guid. Default all. | [optional] |

### Return type

[**List&lt;FlatRateOutputModel&gt;**](FlatRateOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the flat rates |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="flatRatesGetFlatrate"></a>
# **flatRatesGetFlatrate**
> List&lt;FlatRateOutputModel&gt; flatRatesGetFlatrate(guid)

Get flat rate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesReadApi apiInstance = new FeesReadApi(defaultClient);
    String guid = "guid_example"; // String | Id of the flat rate.
    try {
      List<FlatRateOutputModel> result = apiInstance.flatRatesGetFlatrate(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesReadApi#flatRatesGetFlatrate");
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
| **guid** | **String**| Id of the flat rate. | |

### Return type

[**List&lt;FlatRateOutputModel&gt;**](FlatRateOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | FlatRateModel. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="flatRatesGetFlatratesForProject"></a>
# **flatRatesGetFlatratesForProject**
> List&lt;FlatRateOutputModel&gt; flatRatesGetFlatratesForProject(projectGuid)

Get project&#39;s flat rates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesReadApi apiInstance = new FeesReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | Id of the project.
    try {
      List<FlatRateOutputModel> result = apiInstance.flatRatesGetFlatratesForProject(projectGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesReadApi#flatRatesGetFlatratesForProject");
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
| **projectGuid** | **String**| Id of the project. | |

### Return type

[**List&lt;FlatRateOutputModel&gt;**](FlatRateOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the flat rates for the project. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectFeesGetDeletedProjectFees"></a>
# **projectFeesGetDeletedProjectFees**
> List&lt;DeletedProjectFeeModel&gt; projectFeesGetDeletedProjectFees(pageToken, rowCount, projectGuids, userGuids, deletedSince)

Get the deleted project fees.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesReadApi apiInstance = new FeesReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | 
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    List<String> projectGuids = Arrays.asList(); // List<String> | Optional: ID of the project for the deleted project fees to be fetched. If not provided, returns for all projects. Default all.
    List<String> userGuids = Arrays.asList(); // List<String> | Optional: ID of the user. If not provided, returns for all users. Default all.
    OffsetDateTime deletedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get project fees that have been deleted after this date time (greater or equal).
    try {
      List<DeletedProjectFeeModel> result = apiInstance.projectFeesGetDeletedProjectFees(pageToken, rowCount, projectGuids, userGuids, deletedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesReadApi#projectFeesGetDeletedProjectFees");
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
| **pageToken** | **String**|  | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **projectGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the project for the deleted project fees to be fetched. If not provided, returns for all projects. Default all. | [optional] |
| **userGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the user. If not provided, returns for all users. Default all. | [optional] |
| **deletedSince** | **OffsetDateTime**| Optional: Get project fees that have been deleted after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;DeletedProjectFeeModel&gt;**](DeletedProjectFeeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectFeesGetProjectFee"></a>
# **projectFeesGetProjectFee**
> ProjectFeeOutputModel projectFeesGetProjectFee(guid)

Get projectFee by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesReadApi apiInstance = new FeesReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the projectFee.
    try {
      ProjectFeeOutputModel result = apiInstance.projectFeesGetProjectFee(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesReadApi#projectFeesGetProjectFee");
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
| **guid** | **String**| Id used to get the projectFee. | |

### Return type

[**ProjectFeeOutputModel**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectFeesGetProjectFeesByToken"></a>
# **projectFeesGetProjectFeesByToken**
> List&lt;ProjectFeeOutputModel&gt; projectFeesGetProjectFeesByToken(pageToken, rowCount, changedSince)

Get the project fees.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesReadApi apiInstance = new FeesReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: Number of rows to fetch
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get project fees that have been added or changed after this date time (greater or equal).
    try {
      List<ProjectFeeOutputModel> result = apiInstance.projectFeesGetProjectFeesByToken(pageToken, rowCount, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesReadApi#projectFeesGetProjectFeesByToken");
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
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: Number of rows to fetch | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get project fees that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;ProjectFeeOutputModel&gt;**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectFee |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectFeesGetProjectFeesForProject"></a>
# **projectFeesGetProjectFeesForProject**
> List&lt;ProjectFeeOutputModel&gt; projectFeesGetProjectFeesForProject(projectGuid, pageToken, rowCount, productType, isBillable, isBilled, invoiceableDate, includeRecurringRules, isBillablePeriodInFuture)

Get all the project fees for a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesReadApi apiInstance = new FeesReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | ID of the project.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: Number of rows to fetch.
    ProductType productType = ProductType.fromValue("FixedFees"); // ProductType | Optional: ProjectFee's product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting
    Boolean isBillable = true; // Boolean | Optional: Filter the project fees. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
    Boolean isBilled = true; // Boolean | Optional: Filter the project fees. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null.
    OffsetDateTime invoiceableDate = OffsetDateTime.now(); // OffsetDateTime | Optional: Filter the project fees. When given, only the ones that are invoiceable before or on the given date are returned. Default is null.
    Boolean includeRecurringRules = false; // Boolean | Optional: Also fetches recurring rules along with project fees. Default is false.
    Boolean isBillablePeriodInFuture = true; // Boolean | Optional. Filter the project fees. If true/false, only the ones that will be billable in the future are returned. If null, all are returned. Default is false.
    try {
      List<ProjectFeeOutputModel> result = apiInstance.projectFeesGetProjectFeesForProject(projectGuid, pageToken, rowCount, productType, isBillable, isBilled, invoiceableDate, includeRecurringRules, isBillablePeriodInFuture);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesReadApi#projectFeesGetProjectFeesForProject");
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
| **projectGuid** | **String**| ID of the project. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: Number of rows to fetch. | [optional] |
| **productType** | [**ProductType**](.md)| Optional: ProjectFee&#39;s product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting | [optional] [enum: FixedFees, Materials, Subcontracting] |
| **isBillable** | **Boolean**| Optional: Filter the project fees. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null. | [optional] |
| **isBilled** | **Boolean**| Optional: Filter the project fees. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null. | [optional] |
| **invoiceableDate** | **OffsetDateTime**| Optional: Filter the project fees. When given, only the ones that are invoiceable before or on the given date are returned. Default is null. | [optional] |
| **includeRecurringRules** | **Boolean**| Optional: Also fetches recurring rules along with project fees. Default is false. | [optional] [default to false] |
| **isBillablePeriodInFuture** | **Boolean**| Optional. Filter the project fees. If true/false, only the ones that will be billable in the future are returned. If null, all are returned. Default is false. | [optional] |

### Return type

[**List&lt;ProjectFeeOutputModel&gt;**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectFees |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectFeesGetUserProjectFees"></a>
# **projectFeesGetUserProjectFees**
> List&lt;ProjectFeeOutputModel&gt; projectFeesGetUserProjectFees(userGuid, pageToken, rowCount, productType, isBillable, isBilled, invoiceableDate, hasPhase, startDate, endDate)

Get all the projectFees for a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesReadApi apiInstance = new FeesReadApi(defaultClient);
    String userGuid = "userGuid_example"; // String | ID of the user.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: Number of rows to fetch.
    ProductType productType = ProductType.fromValue("FixedFees"); // ProductType | Optional: ProjectFee's product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting.
    Boolean isBillable = true; // Boolean | Optional: Filter the project fees. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
    Boolean isBilled = true; // Boolean | Optional: Filter the project fees. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null.
    OffsetDateTime invoiceableDate = OffsetDateTime.now(); // OffsetDateTime | Optional: Filter the project fees. When given, only the ones that are invoiceable before or on the given date are returned. Default is null.
    Boolean hasPhase = true; // Boolean | Optional: Filter the project fees. If true/false, only the ones are connected/not-connected to a phase are returned. If null, all are returned. Default is null.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Start date search criteria. Only get project fees that have event date from this date.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | End date search criteria. Only get project fees that have event date until this date.
    try {
      List<ProjectFeeOutputModel> result = apiInstance.projectFeesGetUserProjectFees(userGuid, pageToken, rowCount, productType, isBillable, isBilled, invoiceableDate, hasPhase, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesReadApi#projectFeesGetUserProjectFees");
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
| **userGuid** | **String**| ID of the user. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: Number of rows to fetch. | [optional] |
| **productType** | [**ProductType**](.md)| Optional: ProjectFee&#39;s product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting. | [optional] [enum: FixedFees, Materials, Subcontracting] |
| **isBillable** | **Boolean**| Optional: Filter the project fees. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null. | [optional] |
| **isBilled** | **Boolean**| Optional: Filter the project fees. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null. | [optional] |
| **invoiceableDate** | **OffsetDateTime**| Optional: Filter the project fees. When given, only the ones that are invoiceable before or on the given date are returned. Default is null. | [optional] |
| **hasPhase** | **Boolean**| Optional: Filter the project fees. If true/false, only the ones are connected/not-connected to a phase are returned. If null, all are returned. Default is null. | [optional] |
| **startDate** | **OffsetDateTime**| Start date search criteria. Only get project fees that have event date from this date. | [optional] |
| **endDate** | **OffsetDateTime**| End date search criteria. Only get project fees that have event date until this date. | [optional] |

### Return type

[**List&lt;ProjectFeeOutputModel&gt;**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectFees |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectRecurringFeeRulesGetProjectRecurringFeeRule"></a>
# **projectRecurringFeeRulesGetProjectRecurringFeeRule**
> ProjectRecurringFeeRuleOutputModel projectRecurringFeeRulesGetProjectRecurringFeeRule(guid, includeInactive)

Get project&#39;s RecurringFeeRule by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesReadApi apiInstance = new FeesReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the ProjectRecurringFeeRule.
    Boolean includeInactive = false; // Boolean | Indicates the rule should be returned even if it is not active. Default is false.
    try {
      ProjectRecurringFeeRuleOutputModel result = apiInstance.projectRecurringFeeRulesGetProjectRecurringFeeRule(guid, includeInactive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesReadApi#projectRecurringFeeRulesGetProjectRecurringFeeRule");
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
| **guid** | **String**| Id used to get the ProjectRecurringFeeRule. | |
| **includeInactive** | **Boolean**| Indicates the rule should be returned even if it is not active. Default is false. | [optional] [default to false] |

### Return type

[**ProjectRecurringFeeRuleOutputModel**](ProjectRecurringFeeRuleOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated project recurring fee rules. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectRecurringFeeRulesGetProjectRecurringFeeRules"></a>
# **projectRecurringFeeRulesGetProjectRecurringFeeRules**
> List&lt;ProjectRecurringFeeRuleOutputModel&gt; projectRecurringFeeRulesGetProjectRecurringFeeRules(firstRow, rowCount, productType, changedSince)

Get the recurring fee rules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesReadApi apiInstance = new FeesReadApi(defaultClient);
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    ProductType productType = ProductType.fromValue("FixedFees"); // ProductType | projectRecurringFeeRule's product type. if given, it filters the projectRecurringFeeRules by the given type.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get recurring fee rules that have been added or changed after this date time (greater or equal).
    try {
      List<ProjectRecurringFeeRuleOutputModel> result = apiInstance.projectRecurringFeeRulesGetProjectRecurringFeeRules(firstRow, rowCount, productType, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesReadApi#projectRecurringFeeRulesGetProjectRecurringFeeRules");
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
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **productType** | [**ProductType**](.md)| projectRecurringFeeRule&#39;s product type. if given, it filters the projectRecurringFeeRules by the given type. | [optional] [enum: FixedFees, Materials, Subcontracting] |
| **changedSince** | **OffsetDateTime**| Optional: Get recurring fee rules that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;ProjectRecurringFeeRuleOutputModel&gt;**](ProjectRecurringFeeRuleOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated project recurring fee rules |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectRecurringFeeRulesGetProjectRecurringFeeRulesForProject"></a>
# **projectRecurringFeeRulesGetProjectRecurringFeeRulesForProject**
> List&lt;ProjectRecurringFeeRuleOutputModel&gt; projectRecurringFeeRulesGetProjectRecurringFeeRulesForProject(projectGuid, productType, firstRow, rowCount, isBillablePeriodInFuture, billableTimePeriod)

Get all the Recurring Fee Rules for a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesReadApi apiInstance = new FeesReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | ID of the project to get the recurring fee rules.
    ProductType productType = ProductType.fromValue("FixedFees"); // ProductType | projectRecurringFeeRule's product type. if given, it filters the projectRecurringFeeRules by the given type.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    Boolean isBillablePeriodInFuture = true; // Boolean | Optional. Filter the project recurring fee rules. If true/false, only the ones that will be billable in the future are returned. If null, all are returned. Default is false.
    BillablePeriod billableTimePeriod = BillablePeriod.fromValue("Any"); // BillablePeriod | the time period for any uninvoiced recurring rules.
    try {
      List<ProjectRecurringFeeRuleOutputModel> result = apiInstance.projectRecurringFeeRulesGetProjectRecurringFeeRulesForProject(projectGuid, productType, firstRow, rowCount, isBillablePeriodInFuture, billableTimePeriod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesReadApi#projectRecurringFeeRulesGetProjectRecurringFeeRulesForProject");
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
| **projectGuid** | **String**| ID of the project to get the recurring fee rules. | |
| **productType** | [**ProductType**](.md)| projectRecurringFeeRule&#39;s product type. if given, it filters the projectRecurringFeeRules by the given type. | [optional] [enum: FixedFees, Materials, Subcontracting] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **isBillablePeriodInFuture** | **Boolean**| Optional. Filter the project recurring fee rules. If true/false, only the ones that will be billable in the future are returned. If null, all are returned. Default is false. | [optional] |
| **billableTimePeriod** | [**BillablePeriod**](.md)| the time period for any uninvoiced recurring rules. | [optional] [enum: Any, Past, Future, NowAndPast, NowAndFuture] |

### Return type

[**List&lt;ProjectRecurringFeeRuleOutputModel&gt;**](ProjectRecurringFeeRuleOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated project recurring fee rules |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

