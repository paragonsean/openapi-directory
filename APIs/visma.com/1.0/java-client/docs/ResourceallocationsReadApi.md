# ResourceallocationsReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourceAllocationsGetResourceAllocation**](ResourceallocationsReadApi.md#resourceAllocationsGetResourceAllocation) | **GET** /v1/resourceallocations/{guid} | Get resource allocation by ID |
| [**resourceAllocationsGetResourceAllocations**](ResourceallocationsReadApi.md#resourceAllocationsGetResourceAllocations) | **GET** /v1/resourceallocations | Get resource allocations |
| [**resourceAllocationsGetResourceAllocationsByPhaseGuid**](ResourceallocationsReadApi.md#resourceAllocationsGetResourceAllocationsByPhaseGuid) | **GET** /v1/phases/{phaseGuid}/resourceallocations/allocations | Get resource allocations for a phase with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once) |
| [**resourceAllocationsGetResourceAllocationsByProjectGuid**](ResourceallocationsReadApi.md#resourceAllocationsGetResourceAllocationsByProjectGuid) | **GET** /v1/projects/{projectGuid}/resourceallocations/allocations | Get resource allocations for a project with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once) |
| [**resourceAllocationsGetResourceAllocationsByUserGuid**](ResourceallocationsReadApi.md#resourceAllocationsGetResourceAllocationsByUserGuid) | **GET** /v1/users/{userGuid}/resourceallocations/allocations | Get resource allocations for a user with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once) |
| [**resourceAllocationsPostResourceAllocations**](ResourceallocationsReadApi.md#resourceAllocationsPostResourceAllocations) | **POST** /v1/resourceallocations/allocations | Get resource allocations (its POST because of being able to accommodate more filters) |
| [**roleAllocationsGetRoleAllocation**](ResourceallocationsReadApi.md#roleAllocationsGetRoleAllocation) | **GET** /v1/roleallocations/{guid} | Get role allocation by GUID. |
| [**roleAllocationsGetRoleAllocations**](ResourceallocationsReadApi.md#roleAllocationsGetRoleAllocations) | **GET** /v1/roleallocations | Get role allocations. |


<a id="resourceAllocationsGetResourceAllocation"></a>
# **resourceAllocationsGetResourceAllocation**
> ResourceAllocationOutputModel resourceAllocationsGetResourceAllocation(guid)

Get resource allocation by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceallocationsReadApi;

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

    ResourceallocationsReadApi apiInstance = new ResourceallocationsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the resource allocation.
    try {
      ResourceAllocationOutputModel result = apiInstance.resourceAllocationsGetResourceAllocation(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceallocationsReadApi#resourceAllocationsGetResourceAllocation");
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
| **guid** | **String**| GUID used to get the resource allocation. | |

### Return type

[**ResourceAllocationOutputModel**](ResourceAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ResourceAllocation |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="resourceAllocationsGetResourceAllocations"></a>
# **resourceAllocationsGetResourceAllocations**
> ResourceAllocationOutputModel resourceAllocationsGetResourceAllocations(rowCount, pageToken, changedSince)

Get resource allocations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceallocationsReadApi;

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

    ResourceallocationsReadApi apiInstance = new ResourceallocationsReadApi(defaultClient);
    Integer rowCount = 56; // Integer | Optional: Number of rows to fetch.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get resource allocations that have been added or changed after this date time (greater or equal).
    try {
      ResourceAllocationOutputModel result = apiInstance.resourceAllocationsGetResourceAllocations(rowCount, pageToken, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceallocationsReadApi#resourceAllocationsGetResourceAllocations");
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
| **rowCount** | **Integer**| Optional: Number of rows to fetch. | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get resource allocations that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**ResourceAllocationOutputModel**](ResourceAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ResourceAllocation |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="resourceAllocationsGetResourceAllocationsByPhaseGuid"></a>
# **resourceAllocationsGetResourceAllocationsByPhaseGuid**
> ResourceAllocationOutputModel resourceAllocationsGetResourceAllocationsByPhaseGuid(phaseGuid, startDate, endDate, changedSince, userLicenseTypes, projectGuid, userGuid, projectBusinessUnitGuid, userBusinessUnitGuid, projectManagerUserGuid, userTagGuid, useSalesProbability, projectStatusTypeGuid, projectTagGuid, superiorUserGuid, salesStatusTypeGuid, resourceAllocationGuid, salesProgress, rowCount, pageToken)

Get resource allocations for a phase with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceallocationsReadApi;

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

    ResourceallocationsReadApi apiInstance = new ResourceallocationsReadApi(defaultClient);
    String phaseGuid = "phaseGuid_example"; // String | 
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Get resource allocations with startDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Get resource allocations with endDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get resource allocations that have been added or changed after this date time (greater or equal).
    List<LicenseUserType> userLicenseTypes = Arrays.asList(); // List<LicenseUserType> | 
    String projectGuid = "projectGuid_example"; // String | 
    String userGuid = "userGuid_example"; // String | 
    String projectBusinessUnitGuid = "projectBusinessUnitGuid_example"; // String | 
    String userBusinessUnitGuid = "userBusinessUnitGuid_example"; // String | 
    String projectManagerUserGuid = "projectManagerUserGuid_example"; // String | 
    String userTagGuid = "userTagGuid_example"; // String | 
    Boolean useSalesProbability = true; // Boolean | 
    String projectStatusTypeGuid = "projectStatusTypeGuid_example"; // String | 
    String projectTagGuid = "projectTagGuid_example"; // String | 
    String superiorUserGuid = "superiorUserGuid_example"; // String | 
    String salesStatusTypeGuid = "salesStatusTypeGuid_example"; // String | 
    String resourceAllocationGuid = "resourceAllocationGuid_example"; // String | 
    SalesProgress salesProgress = SalesProgress.fromValue("None"); // SalesProgress | 
    Integer rowCount = 56; // Integer | Optional: Number of rows to fetch.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    try {
      ResourceAllocationOutputModel result = apiInstance.resourceAllocationsGetResourceAllocationsByPhaseGuid(phaseGuid, startDate, endDate, changedSince, userLicenseTypes, projectGuid, userGuid, projectBusinessUnitGuid, userBusinessUnitGuid, projectManagerUserGuid, userTagGuid, useSalesProbability, projectStatusTypeGuid, projectTagGuid, superiorUserGuid, salesStatusTypeGuid, resourceAllocationGuid, salesProgress, rowCount, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceallocationsReadApi#resourceAllocationsGetResourceAllocationsByPhaseGuid");
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
| **phaseGuid** | **String**|  | |
| **startDate** | **OffsetDateTime**| Get resource allocations with startDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days | [optional] |
| **endDate** | **OffsetDateTime**| Get resource allocations with endDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get resource allocations that have been added or changed after this date time (greater or equal). | [optional] |
| **userLicenseTypes** | [**List&lt;LicenseUserType&gt;**](LicenseUserType.md)|  | [optional] |
| **projectGuid** | **String**|  | [optional] |
| **userGuid** | **String**|  | [optional] |
| **projectBusinessUnitGuid** | **String**|  | [optional] |
| **userBusinessUnitGuid** | **String**|  | [optional] |
| **projectManagerUserGuid** | **String**|  | [optional] |
| **userTagGuid** | **String**|  | [optional] |
| **useSalesProbability** | **Boolean**|  | [optional] [default to true] |
| **projectStatusTypeGuid** | **String**|  | [optional] |
| **projectTagGuid** | **String**|  | [optional] |
| **superiorUserGuid** | **String**|  | [optional] |
| **salesStatusTypeGuid** | **String**|  | [optional] |
| **resourceAllocationGuid** | **String**|  | [optional] |
| **salesProgress** | [**SalesProgress**](.md)|  | [optional] [enum: None, InProgress, Won, Lost] |
| **rowCount** | **Integer**| Optional: Number of rows to fetch. | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |

### Return type

[**ResourceAllocationOutputModel**](ResourceAllocationOutputModel.md)

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

<a id="resourceAllocationsGetResourceAllocationsByProjectGuid"></a>
# **resourceAllocationsGetResourceAllocationsByProjectGuid**
> ResourceAllocationOutputModel resourceAllocationsGetResourceAllocationsByProjectGuid(projectGuid, startDate, endDate, changedSince, userLicenseTypes, phaseGuid, userGuid, projectBusinessUnitGuid, userBusinessUnitGuid, projectManagerUserGuid, userTagGuid, useSalesProbability, projectStatusTypeGuid, projectTagGuid, superiorUserGuid, salesStatusTypeGuid, resourceAllocationGuid, salesProgress, rowCount, pageToken)

Get resource allocations for a project with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceallocationsReadApi;

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

    ResourceallocationsReadApi apiInstance = new ResourceallocationsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | 
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Get resource allocations with startDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Get resource allocations with endDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get resource allocations that have been added or changed after this date time (greater or equal).
    List<LicenseUserType> userLicenseTypes = Arrays.asList(); // List<LicenseUserType> | 
    String phaseGuid = "phaseGuid_example"; // String | 
    String userGuid = "userGuid_example"; // String | 
    String projectBusinessUnitGuid = "projectBusinessUnitGuid_example"; // String | 
    String userBusinessUnitGuid = "userBusinessUnitGuid_example"; // String | 
    String projectManagerUserGuid = "projectManagerUserGuid_example"; // String | 
    String userTagGuid = "userTagGuid_example"; // String | 
    Boolean useSalesProbability = true; // Boolean | 
    String projectStatusTypeGuid = "projectStatusTypeGuid_example"; // String | 
    String projectTagGuid = "projectTagGuid_example"; // String | 
    String superiorUserGuid = "superiorUserGuid_example"; // String | 
    String salesStatusTypeGuid = "salesStatusTypeGuid_example"; // String | 
    String resourceAllocationGuid = "resourceAllocationGuid_example"; // String | 
    SalesProgress salesProgress = SalesProgress.fromValue("None"); // SalesProgress | 
    Integer rowCount = 56; // Integer | Optional: Number of rows to fetch.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    try {
      ResourceAllocationOutputModel result = apiInstance.resourceAllocationsGetResourceAllocationsByProjectGuid(projectGuid, startDate, endDate, changedSince, userLicenseTypes, phaseGuid, userGuid, projectBusinessUnitGuid, userBusinessUnitGuid, projectManagerUserGuid, userTagGuid, useSalesProbability, projectStatusTypeGuid, projectTagGuid, superiorUserGuid, salesStatusTypeGuid, resourceAllocationGuid, salesProgress, rowCount, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceallocationsReadApi#resourceAllocationsGetResourceAllocationsByProjectGuid");
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
| **projectGuid** | **String**|  | |
| **startDate** | **OffsetDateTime**| Get resource allocations with startDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days | [optional] |
| **endDate** | **OffsetDateTime**| Get resource allocations with endDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get resource allocations that have been added or changed after this date time (greater or equal). | [optional] |
| **userLicenseTypes** | [**List&lt;LicenseUserType&gt;**](LicenseUserType.md)|  | [optional] |
| **phaseGuid** | **String**|  | [optional] |
| **userGuid** | **String**|  | [optional] |
| **projectBusinessUnitGuid** | **String**|  | [optional] |
| **userBusinessUnitGuid** | **String**|  | [optional] |
| **projectManagerUserGuid** | **String**|  | [optional] |
| **userTagGuid** | **String**|  | [optional] |
| **useSalesProbability** | **Boolean**|  | [optional] [default to true] |
| **projectStatusTypeGuid** | **String**|  | [optional] |
| **projectTagGuid** | **String**|  | [optional] |
| **superiorUserGuid** | **String**|  | [optional] |
| **salesStatusTypeGuid** | **String**|  | [optional] |
| **resourceAllocationGuid** | **String**|  | [optional] |
| **salesProgress** | [**SalesProgress**](.md)|  | [optional] [enum: None, InProgress, Won, Lost] |
| **rowCount** | **Integer**| Optional: Number of rows to fetch. | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |

### Return type

[**ResourceAllocationOutputModel**](ResourceAllocationOutputModel.md)

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

<a id="resourceAllocationsGetResourceAllocationsByUserGuid"></a>
# **resourceAllocationsGetResourceAllocationsByUserGuid**
> ResourceAllocationOutputModel resourceAllocationsGetResourceAllocationsByUserGuid(userGuid, startDate, endDate, changedSince, userLicenseTypes, phaseGuid, projectGuid, projectBusinessUnitGuid, userBusinessUnitGuid, projectManagerUserGuid, userTagGuid, useSalesProbability, projectStatusTypeGuid, projectTagGuid, superiorUserGuid, salesStatusTypeGuid, resourceAllocationGuid, salesProgress, rowCount, pageToken)

Get resource allocations for a user with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceallocationsReadApi;

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

    ResourceallocationsReadApi apiInstance = new ResourceallocationsReadApi(defaultClient);
    String userGuid = "userGuid_example"; // String | 
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Get resource allocations with startDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Get resource allocations with endDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get resource allocations that have been added or changed after this date time (greater or equal).
    List<LicenseUserType> userLicenseTypes = Arrays.asList(); // List<LicenseUserType> | 
    String phaseGuid = "phaseGuid_example"; // String | 
    String projectGuid = "projectGuid_example"; // String | 
    String projectBusinessUnitGuid = "projectBusinessUnitGuid_example"; // String | 
    String userBusinessUnitGuid = "userBusinessUnitGuid_example"; // String | 
    String projectManagerUserGuid = "projectManagerUserGuid_example"; // String | 
    String userTagGuid = "userTagGuid_example"; // String | 
    Boolean useSalesProbability = true; // Boolean | 
    String projectStatusTypeGuid = "projectStatusTypeGuid_example"; // String | 
    String projectTagGuid = "projectTagGuid_example"; // String | 
    String superiorUserGuid = "superiorUserGuid_example"; // String | 
    String salesStatusTypeGuid = "salesStatusTypeGuid_example"; // String | 
    String resourceAllocationGuid = "resourceAllocationGuid_example"; // String | 
    SalesProgress salesProgress = SalesProgress.fromValue("None"); // SalesProgress | 
    Integer rowCount = 56; // Integer | Optional: Number of rows to fetch.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    try {
      ResourceAllocationOutputModel result = apiInstance.resourceAllocationsGetResourceAllocationsByUserGuid(userGuid, startDate, endDate, changedSince, userLicenseTypes, phaseGuid, projectGuid, projectBusinessUnitGuid, userBusinessUnitGuid, projectManagerUserGuid, userTagGuid, useSalesProbability, projectStatusTypeGuid, projectTagGuid, superiorUserGuid, salesStatusTypeGuid, resourceAllocationGuid, salesProgress, rowCount, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceallocationsReadApi#resourceAllocationsGetResourceAllocationsByUserGuid");
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
| **userGuid** | **String**|  | |
| **startDate** | **OffsetDateTime**| Get resource allocations with startDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days | [optional] |
| **endDate** | **OffsetDateTime**| Get resource allocations with endDate. Using startDate and endDate or changedSince parameters are required to fetch a maximum of 30 days | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get resource allocations that have been added or changed after this date time (greater or equal). | [optional] |
| **userLicenseTypes** | [**List&lt;LicenseUserType&gt;**](LicenseUserType.md)|  | [optional] |
| **phaseGuid** | **String**|  | [optional] |
| **projectGuid** | **String**|  | [optional] |
| **projectBusinessUnitGuid** | **String**|  | [optional] |
| **userBusinessUnitGuid** | **String**|  | [optional] |
| **projectManagerUserGuid** | **String**|  | [optional] |
| **userTagGuid** | **String**|  | [optional] |
| **useSalesProbability** | **Boolean**|  | [optional] [default to true] |
| **projectStatusTypeGuid** | **String**|  | [optional] |
| **projectTagGuid** | **String**|  | [optional] |
| **superiorUserGuid** | **String**|  | [optional] |
| **salesStatusTypeGuid** | **String**|  | [optional] |
| **resourceAllocationGuid** | **String**|  | [optional] |
| **salesProgress** | [**SalesProgress**](.md)|  | [optional] [enum: None, InProgress, Won, Lost] |
| **rowCount** | **Integer**| Optional: Number of rows to fetch. | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |

### Return type

[**ResourceAllocationOutputModel**](ResourceAllocationOutputModel.md)

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

<a id="resourceAllocationsPostResourceAllocations"></a>
# **resourceAllocationsPostResourceAllocations**
> List&lt;ResourceAllocationOutputModel&gt; resourceAllocationsPostResourceAllocations(rowCount, pageToken, changedSince, resourceAllocationCriteriaModel)

Get resource allocations (its POST because of being able to accommodate more filters)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceallocationsReadApi;

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

    ResourceallocationsReadApi apiInstance = new ResourceallocationsReadApi(defaultClient);
    Integer rowCount = 56; // Integer | Optional: Number of rows to fetch.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get resource allocations that have been added or changed after this date time (greater or equal).
    ResourceAllocationCriteriaModel resourceAllocationCriteriaModel = new ResourceAllocationCriteriaModel(); // ResourceAllocationCriteriaModel | resourceAllocationCriteriaModel
    try {
      List<ResourceAllocationOutputModel> result = apiInstance.resourceAllocationsPostResourceAllocations(rowCount, pageToken, changedSince, resourceAllocationCriteriaModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceallocationsReadApi#resourceAllocationsPostResourceAllocations");
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
| **rowCount** | **Integer**| Optional: Number of rows to fetch. | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get resource allocations that have been added or changed after this date time (greater or equal). | [optional] |
| **resourceAllocationCriteriaModel** | [**ResourceAllocationCriteriaModel**](ResourceAllocationCriteriaModel.md)| resourceAllocationCriteriaModel | [optional] |

### Return type

[**List&lt;ResourceAllocationOutputModel&gt;**](ResourceAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ResourceAllocationModel |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="roleAllocationsGetRoleAllocation"></a>
# **roleAllocationsGetRoleAllocation**
> RoleAllocationOutputModel roleAllocationsGetRoleAllocation(guid)

Get role allocation by GUID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceallocationsReadApi;

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

    ResourceallocationsReadApi apiInstance = new ResourceallocationsReadApi(defaultClient);
    String guid = "guid_example"; // String | ID used to get the role allocation.
    try {
      RoleAllocationOutputModel result = apiInstance.roleAllocationsGetRoleAllocation(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceallocationsReadApi#roleAllocationsGetRoleAllocation");
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
| **guid** | **String**| ID used to get the role allocation. | |

### Return type

[**RoleAllocationOutputModel**](RoleAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | RoleAllocationModel. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="roleAllocationsGetRoleAllocations"></a>
# **roleAllocationsGetRoleAllocations**
> List&lt;RoleAllocationOutputModel&gt; roleAllocationsGetRoleAllocations(startDate, endDate, pageToken, rowCount, useSalesProbability, roleGuids, phaseGuids, projectGuids)

Get role allocations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceallocationsReadApi;

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

    ResourceallocationsReadApi apiInstance = new ResourceallocationsReadApi(defaultClient);
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Starting date from which to get the role allocations. If end date is not specified on the role allocation then it will be compared with phase end date.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Optional: Ending date to which to get the role allocations. If start date is not specified on the role allocation then it will be compared with phase start date.
    String pageToken = "pageToken_example"; // String | Optional: Page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default all.
    Boolean useSalesProbability = true; // Boolean | Optional: Calculates the hours based on sales probability set for the project. Default is true.
    List<String> roleGuids = Arrays.asList(); // List<String> | Optional: Role IDs.
    List<String> phaseGuids = Arrays.asList(); // List<String> | Optional: Phase IDs.
    List<String> projectGuids = Arrays.asList(); // List<String> | Optional: Project IDs.
    try {
      List<RoleAllocationOutputModel> result = apiInstance.roleAllocationsGetRoleAllocations(startDate, endDate, pageToken, rowCount, useSalesProbability, roleGuids, phaseGuids, projectGuids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceallocationsReadApi#roleAllocationsGetRoleAllocations");
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
| **startDate** | **OffsetDateTime**| Starting date from which to get the role allocations. If end date is not specified on the role allocation then it will be compared with phase end date. | |
| **endDate** | **OffsetDateTime**| Optional: Ending date to which to get the role allocations. If start date is not specified on the role allocation then it will be compared with phase start date. | [optional] |
| **pageToken** | **String**| Optional: Page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default all. | [optional] |
| **useSalesProbability** | **Boolean**| Optional: Calculates the hours based on sales probability set for the project. Default is true. | [optional] [default to true] |
| **roleGuids** | [**List&lt;String&gt;**](String.md)| Optional: Role IDs. | [optional] |
| **phaseGuids** | [**List&lt;String&gt;**](String.md)| Optional: Phase IDs. | [optional] |
| **projectGuids** | [**List&lt;String&gt;**](String.md)| Optional: Project IDs. | [optional] |

### Return type

[**List&lt;RoleAllocationOutputModel&gt;**](RoleAllocationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | RoleAllocationModel. |  * NextPageToken - Page token to fetch the next page <br>  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

