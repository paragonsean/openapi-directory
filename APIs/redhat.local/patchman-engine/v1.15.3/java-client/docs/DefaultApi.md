# DefaultApi

All URIs are relative to *http://redhat.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deletesystem**](DefaultApi.md#deletesystem) | **DELETE** /api/patch/v1/systems/{inventory_id} | Delete system by inventory id |
| [**detailAdvisory**](DefaultApi.md#detailAdvisory) | **GET** /api/patch/v1/advisories/{advisory_id} | Show me details an advisory by given advisory name |
| [**detailSystem**](DefaultApi.md#detailSystem) | **GET** /api/patch/v1/systems/{inventory_id} | Show me details about a system by given inventory id |
| [**exportAdvisories**](DefaultApi.md#exportAdvisories) | **GET** /api/patch/v1/export/advisories | Export applicable advisories for all my systems |
| [**exportAdvisorySystems**](DefaultApi.md#exportAdvisorySystems) | **GET** /api/patch/v1/export/advisories/{advisory_id}/systems | Export systems for my account |
| [**exportPackageSystems**](DefaultApi.md#exportPackageSystems) | **GET** /api/patch/v1/export/packages/{package_name}/systems | Show me all my systems which have a package installed |
| [**exportPackages**](DefaultApi.md#exportPackages) | **GET** /api/patch/v1/export/packages | Show me all installed packages across my systems |
| [**exportSystemAdvisories**](DefaultApi.md#exportSystemAdvisories) | **GET** /api/patch/v1/export/systems/{inventory_id}/advisories | Export applicable advisories for all my systems |
| [**exportSystemPackages**](DefaultApi.md#exportSystemPackages) | **GET** /api/patch/v1/export/systems/{inventory_id}/packages | Show me details about a system packages by given inventory id |
| [**exportSystems**](DefaultApi.md#exportSystems) | **GET** /api/patch/v1/export/systems | Export systems for my account |
| [**latestPackage**](DefaultApi.md#latestPackage) | **GET** /api/patch/v1/packages/{package_name} | Show me metadata of selected package |
| [**listAdvisories**](DefaultApi.md#listAdvisories) | **GET** /api/patch/v1/advisories | Show me all applicable advisories for all my systems |
| [**listAdvisorySystems**](DefaultApi.md#listAdvisorySystems) | **GET** /api/patch/v1/advisories/{advisory_id}/systems | Show me systems on which the given advisory is applicable |
| [**listPackages**](DefaultApi.md#listPackages) | **GET** /api/patch/v1/packages/ | Show me all installed packages across my systems |
| [**listSystemAdvisories**](DefaultApi.md#listSystemAdvisories) | **GET** /api/patch/v1/systems/{inventory_id}/advisories | Show me advisories for a system by given inventory id |
| [**listSystems**](DefaultApi.md#listSystems) | **GET** /api/patch/v1/systems | Show me all my systems |
| [**packageSystems**](DefaultApi.md#packageSystems) | **GET** /api/patch/v1/packages/{package_name}/systems | Show me all my systems which have a package installed |
| [**packageVersions**](DefaultApi.md#packageVersions) | **GET** /api/patch/v1/packages/{package_name}/versions | Show me all package versions installed on some system |
| [**systemPackages**](DefaultApi.md#systemPackages) | **GET** /api/patch/v1/systems/{inventory_id}/packages | Show me details about a system packages by given inventory id |
| [**viewAdvisoriesSystems**](DefaultApi.md#viewAdvisoriesSystems) | **POST** /api/patch/v1/views/advisories/systems | View advisory-system pairs for selected systems and advisories |
| [**viewSystemsAdvisories**](DefaultApi.md#viewSystemsAdvisories) | **POST** /api/patch/v1/views/systems/advisories | View system-advisory pairs for selected systems and advisories |


<a id="deletesystem"></a>
# **deletesystem**
> deletesystem(inventoryId)

Delete system by inventory id

Delete system by inventory id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String inventoryId = "inventoryId_example"; // String | Inventory ID
    try {
      apiInstance.deletesystem(inventoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deletesystem");
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
| **inventoryId** | **String**| Inventory ID | |

### Return type

null (empty response body)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |

<a id="detailAdvisory"></a>
# **detailAdvisory**
> ControllersAdvisoryDetailResponse detailAdvisory(advisoryId)

Show me details an advisory by given advisory name

Show me details an advisory by given advisory name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String advisoryId = "advisoryId_example"; // String | Advisory ID
    try {
      ControllersAdvisoryDetailResponse result = apiInstance.detailAdvisory(advisoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#detailAdvisory");
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
| **advisoryId** | **String**| Advisory ID | |

### Return type

[**ControllersAdvisoryDetailResponse**](ControllersAdvisoryDetailResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="detailSystem"></a>
# **detailSystem**
> ControllersSystemDetailResponse detailSystem(inventoryId)

Show me details about a system by given inventory id

Show me details about a system by given inventory id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String inventoryId = "inventoryId_example"; // String | Inventory ID
    try {
      ControllersSystemDetailResponse result = apiInstance.detailSystem(inventoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#detailSystem");
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
| **inventoryId** | **String**| Inventory ID | |

### Return type

[**ControllersSystemDetailResponse**](ControllersSystemDetailResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="exportAdvisories"></a>
# **exportAdvisories**
> List&lt;ControllersAdvisoryInlineItem&gt; exportAdvisories(search, filterId, filterDescription, filterPublicDate, filterSynopsis, filterAdvisoryType, filterSeverity, filterApplicableSystems)

Export applicable advisories for all my systems

Export applicable advisories for all my systems

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String search = "search_example"; // String | Find matching text
    String filterId = "filterId_example"; // String | Filter
    String filterDescription = "filterDescription_example"; // String | Filter
    String filterPublicDate = "filterPublicDate_example"; // String | Filter
    String filterSynopsis = "filterSynopsis_example"; // String | Filter
    String filterAdvisoryType = "filterAdvisoryType_example"; // String | Filter
    String filterSeverity = "filterSeverity_example"; // String | Filter
    String filterApplicableSystems = "filterApplicableSystems_example"; // String | Filter
    try {
      List<ControllersAdvisoryInlineItem> result = apiInstance.exportAdvisories(search, filterId, filterDescription, filterPublicDate, filterSynopsis, filterAdvisoryType, filterSeverity, filterApplicableSystems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#exportAdvisories");
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
| **search** | **String**| Find matching text | [optional] |
| **filterId** | **String**| Filter | [optional] |
| **filterDescription** | **String**| Filter | [optional] |
| **filterPublicDate** | **String**| Filter | [optional] |
| **filterSynopsis** | **String**| Filter | [optional] |
| **filterAdvisoryType** | **String**| Filter | [optional] |
| **filterSeverity** | **String**| Filter | [optional] |
| **filterApplicableSystems** | **String**| Filter | [optional] |

### Return type

[**List&lt;ControllersAdvisoryInlineItem&gt;**](ControllersAdvisoryInlineItem.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="exportAdvisorySystems"></a>
# **exportAdvisorySystems**
> List&lt;ControllersSystemInlineItem&gt; exportAdvisorySystems(advisoryId, search, filterId, filterDisplayName, filterLastEvaluation, filterLastUpload, filterRhsaCount, filterRhbaCount, filterRheaCount, filterOtherCount, filterStale, filterPackagesInstalled, filterPackagesUpdatable, filterSystemProfileSapSystem, filterSystemProfileSapSidsIn, tags)

Export systems for my account

Export systems for my account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String advisoryId = "advisoryId_example"; // String | Advisory ID
    String search = "search_example"; // String | Find matching text
    String filterId = "filterId_example"; // String | Filter
    String filterDisplayName = "filterDisplayName_example"; // String | Filter
    String filterLastEvaluation = "filterLastEvaluation_example"; // String | Filter
    String filterLastUpload = "filterLastUpload_example"; // String | Filter
    String filterRhsaCount = "filterRhsaCount_example"; // String | Filter
    String filterRhbaCount = "filterRhbaCount_example"; // String | Filter
    String filterRheaCount = "filterRheaCount_example"; // String | Filter
    String filterOtherCount = "filterOtherCount_example"; // String | Filter
    String filterStale = "filterStale_example"; // String | Filter
    String filterPackagesInstalled = "filterPackagesInstalled_example"; // String | Filter
    String filterPackagesUpdatable = "filterPackagesUpdatable_example"; // String | Filter
    String filterSystemProfileSapSystem = "filterSystemProfileSapSystem_example"; // String | Filter only SAP systems
    List<String> filterSystemProfileSapSidsIn = Arrays.asList(); // List<String> | Filter systems by their SAP SIDs
    List<String> tags = Arrays.asList(); // List<String> | Tag filter
    try {
      List<ControllersSystemInlineItem> result = apiInstance.exportAdvisorySystems(advisoryId, search, filterId, filterDisplayName, filterLastEvaluation, filterLastUpload, filterRhsaCount, filterRhbaCount, filterRheaCount, filterOtherCount, filterStale, filterPackagesInstalled, filterPackagesUpdatable, filterSystemProfileSapSystem, filterSystemProfileSapSidsIn, tags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#exportAdvisorySystems");
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
| **advisoryId** | **String**| Advisory ID | |
| **search** | **String**| Find matching text | [optional] |
| **filterId** | **String**| Filter | [optional] |
| **filterDisplayName** | **String**| Filter | [optional] |
| **filterLastEvaluation** | **String**| Filter | [optional] |
| **filterLastUpload** | **String**| Filter | [optional] |
| **filterRhsaCount** | **String**| Filter | [optional] |
| **filterRhbaCount** | **String**| Filter | [optional] |
| **filterRheaCount** | **String**| Filter | [optional] |
| **filterOtherCount** | **String**| Filter | [optional] |
| **filterStale** | **String**| Filter | [optional] |
| **filterPackagesInstalled** | **String**| Filter | [optional] |
| **filterPackagesUpdatable** | **String**| Filter | [optional] |
| **filterSystemProfileSapSystem** | **String**| Filter only SAP systems | [optional] |
| **filterSystemProfileSapSidsIn** | [**List&lt;String&gt;**](String.md)| Filter systems by their SAP SIDs | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| Tag filter | [optional] |

### Return type

[**List&lt;ControllersSystemInlineItem&gt;**](ControllersSystemInlineItem.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="exportPackageSystems"></a>
# **exportPackageSystems**
> List&lt;ControllersPackageSystemItem&gt; exportPackageSystems(packageName, filterSystemProfileSapSystem, filterSystemProfileSapSidsIn, tags)

Show me all my systems which have a package installed

Show me all my systems which have a package installed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String packageName = "packageName_example"; // String | Package name
    String filterSystemProfileSapSystem = "filterSystemProfileSapSystem_example"; // String | Filter only SAP systems
    List<String> filterSystemProfileSapSidsIn = Arrays.asList(); // List<String> | Filter systems by their SAP SIDs
    List<String> tags = Arrays.asList(); // List<String> | Tag filter
    try {
      List<ControllersPackageSystemItem> result = apiInstance.exportPackageSystems(packageName, filterSystemProfileSapSystem, filterSystemProfileSapSidsIn, tags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#exportPackageSystems");
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
| **packageName** | **String**| Package name | |
| **filterSystemProfileSapSystem** | **String**| Filter only SAP systems | [optional] |
| **filterSystemProfileSapSidsIn** | [**List&lt;String&gt;**](String.md)| Filter systems by their SAP SIDs | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| Tag filter | [optional] |

### Return type

[**List&lt;ControllersPackageSystemItem&gt;**](ControllersPackageSystemItem.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="exportPackages"></a>
# **exportPackages**
> List&lt;ControllersPackageItem&gt; exportPackages(sort, search, filterName, filterSystemsInstalled, filterSystemsUpdatable, filterSummary)

Show me all installed packages across my systems

Show me all installed packages across my systems

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sort = "id"; // String | Sort field
    String search = "search_example"; // String | Find matching text
    String filterName = "filterName_example"; // String | Filter
    String filterSystemsInstalled = "filterSystemsInstalled_example"; // String | Filter
    String filterSystemsUpdatable = "filterSystemsUpdatable_example"; // String | Filter
    String filterSummary = "filterSummary_example"; // String | Filter
    try {
      List<ControllersPackageItem> result = apiInstance.exportPackages(sort, search, filterName, filterSystemsInstalled, filterSystemsUpdatable, filterSummary);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#exportPackages");
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
| **sort** | **String**| Sort field | [optional] [enum: id, name, systems_installed, systems_updatable] |
| **search** | **String**| Find matching text | [optional] |
| **filterName** | **String**| Filter | [optional] |
| **filterSystemsInstalled** | **String**| Filter | [optional] |
| **filterSystemsUpdatable** | **String**| Filter | [optional] |
| **filterSummary** | **String**| Filter | [optional] |

### Return type

[**List&lt;ControllersPackageItem&gt;**](ControllersPackageItem.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="exportSystemAdvisories"></a>
# **exportSystemAdvisories**
> List&lt;ControllersSystemAdvisoriesDBLookup&gt; exportSystemAdvisories(inventoryId, search, filterId, filterDescription, filterPublicDate, filterSynopsis, filterAdvisoryType, filterSeverity)

Export applicable advisories for all my systems

Export applicable advisories for all my systems

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String inventoryId = "inventoryId_example"; // String | Inventory ID
    String search = "search_example"; // String | Find matching text
    String filterId = "filterId_example"; // String | Filter
    String filterDescription = "filterDescription_example"; // String | Filter
    String filterPublicDate = "filterPublicDate_example"; // String | Filter
    String filterSynopsis = "filterSynopsis_example"; // String | Filter
    String filterAdvisoryType = "filterAdvisoryType_example"; // String | Filter
    String filterSeverity = "filterSeverity_example"; // String | Filter
    try {
      List<ControllersSystemAdvisoriesDBLookup> result = apiInstance.exportSystemAdvisories(inventoryId, search, filterId, filterDescription, filterPublicDate, filterSynopsis, filterAdvisoryType, filterSeverity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#exportSystemAdvisories");
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
| **inventoryId** | **String**| Inventory ID | |
| **search** | **String**| Find matching text | [optional] |
| **filterId** | **String**| Filter | [optional] |
| **filterDescription** | **String**| Filter | [optional] |
| **filterPublicDate** | **String**| Filter | [optional] |
| **filterSynopsis** | **String**| Filter | [optional] |
| **filterAdvisoryType** | **String**| Filter | [optional] |
| **filterSeverity** | **String**| Filter | [optional] |

### Return type

[**List&lt;ControllersSystemAdvisoriesDBLookup&gt;**](ControllersSystemAdvisoriesDBLookup.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="exportSystemPackages"></a>
# **exportSystemPackages**
> List&lt;ControllersSystemPackageInline&gt; exportSystemPackages(inventoryId, search, filterName, filterDescription, filterEvra, filterSummary, filterUpdatable)

Show me details about a system packages by given inventory id

Show me details about a system packages by given inventory id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String inventoryId = "inventoryId_example"; // String | Inventory ID
    String search = "search_example"; // String | Find matching text
    String filterName = "filterName_example"; // String | Filter
    String filterDescription = "filterDescription_example"; // String | Filter
    String filterEvra = "filterEvra_example"; // String | Filter
    String filterSummary = "filterSummary_example"; // String | Filter
    Boolean filterUpdatable = true; // Boolean | Filter
    try {
      List<ControllersSystemPackageInline> result = apiInstance.exportSystemPackages(inventoryId, search, filterName, filterDescription, filterEvra, filterSummary, filterUpdatable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#exportSystemPackages");
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
| **inventoryId** | **String**| Inventory ID | |
| **search** | **String**| Find matching text | [optional] |
| **filterName** | **String**| Filter | [optional] |
| **filterDescription** | **String**| Filter | [optional] |
| **filterEvra** | **String**| Filter | [optional] |
| **filterSummary** | **String**| Filter | [optional] |
| **filterUpdatable** | **Boolean**| Filter | [optional] |

### Return type

[**List&lt;ControllersSystemPackageInline&gt;**](ControllersSystemPackageInline.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="exportSystems"></a>
# **exportSystems**
> List&lt;ControllersSystemInlineItem&gt; exportSystems(search, filterId, filterDisplayName, filterLastEvaluation, filterLastUpload, filterRhsaCount, filterRhbaCount, filterRheaCount, filterOtherCount, filterStale, filterPackagesInstalled, filterPackagesUpdatable, filterSystemProfileSapSystem, filterSystemProfileSapSidsIn, tags)

Export systems for my account

Export systems for my account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String search = "search_example"; // String | Find matching text
    String filterId = "filterId_example"; // String | Filter
    String filterDisplayName = "filterDisplayName_example"; // String | Filter
    String filterLastEvaluation = "filterLastEvaluation_example"; // String | Filter
    String filterLastUpload = "filterLastUpload_example"; // String | Filter
    String filterRhsaCount = "filterRhsaCount_example"; // String | Filter
    String filterRhbaCount = "filterRhbaCount_example"; // String | Filter
    String filterRheaCount = "filterRheaCount_example"; // String | Filter
    String filterOtherCount = "filterOtherCount_example"; // String | Filter
    String filterStale = "filterStale_example"; // String | Filter
    String filterPackagesInstalled = "filterPackagesInstalled_example"; // String | Filter
    String filterPackagesUpdatable = "filterPackagesUpdatable_example"; // String | Filter
    String filterSystemProfileSapSystem = "filterSystemProfileSapSystem_example"; // String | Filter only SAP systems
    List<String> filterSystemProfileSapSidsIn = Arrays.asList(); // List<String> | Filter systems by their SAP SIDs
    List<String> tags = Arrays.asList(); // List<String> | Tag filter
    try {
      List<ControllersSystemInlineItem> result = apiInstance.exportSystems(search, filterId, filterDisplayName, filterLastEvaluation, filterLastUpload, filterRhsaCount, filterRhbaCount, filterRheaCount, filterOtherCount, filterStale, filterPackagesInstalled, filterPackagesUpdatable, filterSystemProfileSapSystem, filterSystemProfileSapSidsIn, tags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#exportSystems");
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
| **search** | **String**| Find matching text | [optional] |
| **filterId** | **String**| Filter | [optional] |
| **filterDisplayName** | **String**| Filter | [optional] |
| **filterLastEvaluation** | **String**| Filter | [optional] |
| **filterLastUpload** | **String**| Filter | [optional] |
| **filterRhsaCount** | **String**| Filter | [optional] |
| **filterRhbaCount** | **String**| Filter | [optional] |
| **filterRheaCount** | **String**| Filter | [optional] |
| **filterOtherCount** | **String**| Filter | [optional] |
| **filterStale** | **String**| Filter | [optional] |
| **filterPackagesInstalled** | **String**| Filter | [optional] |
| **filterPackagesUpdatable** | **String**| Filter | [optional] |
| **filterSystemProfileSapSystem** | **String**| Filter only SAP systems | [optional] |
| **filterSystemProfileSapSidsIn** | [**List&lt;String&gt;**](String.md)| Filter systems by their SAP SIDs | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| Tag filter | [optional] |

### Return type

[**List&lt;ControllersSystemInlineItem&gt;**](ControllersSystemInlineItem.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="latestPackage"></a>
# **latestPackage**
> ControllersPackageDetailResponse latestPackage(packageName)

Show me metadata of selected package

Show me metadata of selected package

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String packageName = "packageName_example"; // String | package_name - latest, nevra - exact version
    try {
      ControllersPackageDetailResponse result = apiInstance.latestPackage(packageName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#latestPackage");
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
| **packageName** | **String**| package_name - latest, nevra - exact version | |

### Return type

[**ControllersPackageDetailResponse**](ControllersPackageDetailResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAdvisories"></a>
# **listAdvisories**
> ControllersAdvisoriesResponse listAdvisories(limit, offset, sort, search, filterId, filterDescription, filterPublicDate, filterSynopsis, filterAdvisoryType, filterSeverity, filterApplicableSystems, tags, filterSystemProfileSapSystem, filterSystemProfileSapSidsIn)

Show me all applicable advisories for all my systems

Show me all applicable advisories for all my systems

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 56; // Integer | Limit for paging, set -1 to return all
    Integer offset = 56; // Integer | Offset for paging
    String sort = "id"; // String | Sort field
    String search = "search_example"; // String | Find matching text
    String filterId = "filterId_example"; // String | Filter 
    String filterDescription = "filterDescription_example"; // String | Filter
    String filterPublicDate = "filterPublicDate_example"; // String | Filter
    String filterSynopsis = "filterSynopsis_example"; // String | Filter
    String filterAdvisoryType = "filterAdvisoryType_example"; // String | Filter
    String filterSeverity = "filterSeverity_example"; // String | Filter
    String filterApplicableSystems = "filterApplicableSystems_example"; // String | Filter
    List<String> tags = Arrays.asList(); // List<String> | Tag filter
    String filterSystemProfileSapSystem = "filterSystemProfileSapSystem_example"; // String | Filter only SAP systems
    List<String> filterSystemProfileSapSidsIn = Arrays.asList(); // List<String> | Filter systems by their SAP SIDs
    try {
      ControllersAdvisoriesResponse result = apiInstance.listAdvisories(limit, offset, sort, search, filterId, filterDescription, filterPublicDate, filterSynopsis, filterAdvisoryType, filterSeverity, filterApplicableSystems, tags, filterSystemProfileSapSystem, filterSystemProfileSapSidsIn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAdvisories");
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
| **limit** | **Integer**| Limit for paging, set -1 to return all | [optional] |
| **offset** | **Integer**| Offset for paging | [optional] |
| **sort** | **String**| Sort field | [optional] [enum: id, name, advisory_type, synopsis, public_date, applicable_systems] |
| **search** | **String**| Find matching text | [optional] |
| **filterId** | **String**| Filter  | [optional] |
| **filterDescription** | **String**| Filter | [optional] |
| **filterPublicDate** | **String**| Filter | [optional] |
| **filterSynopsis** | **String**| Filter | [optional] |
| **filterAdvisoryType** | **String**| Filter | [optional] |
| **filterSeverity** | **String**| Filter | [optional] |
| **filterApplicableSystems** | **String**| Filter | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| Tag filter | [optional] |
| **filterSystemProfileSapSystem** | **String**| Filter only SAP systems | [optional] |
| **filterSystemProfileSapSidsIn** | [**List&lt;String&gt;**](String.md)| Filter systems by their SAP SIDs | [optional] |

### Return type

[**ControllersAdvisoriesResponse**](ControllersAdvisoriesResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAdvisorySystems"></a>
# **listAdvisorySystems**
> ControllersAdvisorySystemsResponse listAdvisorySystems(advisoryId, limit, offset, sort, search, filterId, filterInsightsId, filterDisplayName, filterLastEvaluation, filterLastUpload, filterRhsaCount, filterRhbaCount, filterRheaCount, filterOtherCount, filterStale, filterStaleTimestamp, filterStaleWarningTimestamp, filterCulledTimestamp, filterCreated, tags, filterSystemProfileSapSystem, filterSystemProfileSapSidsIn)

Show me systems on which the given advisory is applicable

Show me systems on which the given advisory is applicable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String advisoryId = "advisoryId_example"; // String | Advisory ID
    Integer limit = 56; // Integer | Limit for paging, set -1 to return all
    Integer offset = 56; // Integer | Offset for paging
    String sort = "id"; // String | Sort field
    String search = "search_example"; // String | Find matching text
    String filterId = "filterId_example"; // String | Filter
    String filterInsightsId = "filterInsightsId_example"; // String | Filter
    String filterDisplayName = "filterDisplayName_example"; // String | Filter
    String filterLastEvaluation = "filterLastEvaluation_example"; // String | Filter
    String filterLastUpload = "filterLastUpload_example"; // String | Filter
    String filterRhsaCount = "filterRhsaCount_example"; // String | Filter
    String filterRhbaCount = "filterRhbaCount_example"; // String | Filter
    String filterRheaCount = "filterRheaCount_example"; // String | Filter
    String filterOtherCount = "filterOtherCount_example"; // String | Filter
    String filterStale = "filterStale_example"; // String | Filter
    String filterStaleTimestamp = "filterStaleTimestamp_example"; // String | Filter
    String filterStaleWarningTimestamp = "filterStaleWarningTimestamp_example"; // String | Filter
    String filterCulledTimestamp = "filterCulledTimestamp_example"; // String | Filter
    String filterCreated = "filterCreated_example"; // String | Filter
    List<String> tags = Arrays.asList(); // List<String> | Tag filter
    String filterSystemProfileSapSystem = "filterSystemProfileSapSystem_example"; // String | Filter only SAP systems
    List<String> filterSystemProfileSapSidsIn = Arrays.asList(); // List<String> | Filter systems by their SAP SIDs
    try {
      ControllersAdvisorySystemsResponse result = apiInstance.listAdvisorySystems(advisoryId, limit, offset, sort, search, filterId, filterInsightsId, filterDisplayName, filterLastEvaluation, filterLastUpload, filterRhsaCount, filterRhbaCount, filterRheaCount, filterOtherCount, filterStale, filterStaleTimestamp, filterStaleWarningTimestamp, filterCulledTimestamp, filterCreated, tags, filterSystemProfileSapSystem, filterSystemProfileSapSidsIn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAdvisorySystems");
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
| **advisoryId** | **String**| Advisory ID | |
| **limit** | **Integer**| Limit for paging, set -1 to return all | [optional] |
| **offset** | **Integer**| Offset for paging | [optional] |
| **sort** | **String**| Sort field | [optional] [enum: id, display_name, last_evaluation, last_upload, rhsa_count, rhba_count, rhea_count, other_count, stale] |
| **search** | **String**| Find matching text | [optional] |
| **filterId** | **String**| Filter | [optional] |
| **filterInsightsId** | **String**| Filter | [optional] |
| **filterDisplayName** | **String**| Filter | [optional] |
| **filterLastEvaluation** | **String**| Filter | [optional] |
| **filterLastUpload** | **String**| Filter | [optional] |
| **filterRhsaCount** | **String**| Filter | [optional] |
| **filterRhbaCount** | **String**| Filter | [optional] |
| **filterRheaCount** | **String**| Filter | [optional] |
| **filterOtherCount** | **String**| Filter | [optional] |
| **filterStale** | **String**| Filter | [optional] |
| **filterStaleTimestamp** | **String**| Filter | [optional] |
| **filterStaleWarningTimestamp** | **String**| Filter | [optional] |
| **filterCulledTimestamp** | **String**| Filter | [optional] |
| **filterCreated** | **String**| Filter | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| Tag filter | [optional] |
| **filterSystemProfileSapSystem** | **String**| Filter only SAP systems | [optional] |
| **filterSystemProfileSapSidsIn** | [**List&lt;String&gt;**](String.md)| Filter systems by their SAP SIDs | [optional] |

### Return type

[**ControllersAdvisorySystemsResponse**](ControllersAdvisorySystemsResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listPackages"></a>
# **listPackages**
> ControllersPackagesResponse listPackages(limit, offset, sort, search, filterName, filterSystemsInstalled, filterSystemsUpdatable, filterSummary, tags, filterSystemProfileSapSystem, filterSystemProfileSapSidsIn)

Show me all installed packages across my systems

Show me all installed packages across my systems

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 56; // Integer | Limit for paging, set -1 to return all
    Integer offset = 56; // Integer | Offset for paging
    String sort = "id"; // String | Sort field
    String search = "search_example"; // String | Find matching text
    String filterName = "filterName_example"; // String | Filter
    String filterSystemsInstalled = "filterSystemsInstalled_example"; // String | Filter
    String filterSystemsUpdatable = "filterSystemsUpdatable_example"; // String | Filter
    String filterSummary = "filterSummary_example"; // String | Filter
    List<String> tags = Arrays.asList(); // List<String> | Tag filter
    String filterSystemProfileSapSystem = "filterSystemProfileSapSystem_example"; // String | Filter only SAP systems
    List<String> filterSystemProfileSapSidsIn = Arrays.asList(); // List<String> | Filter systems by their SAP SIDs
    try {
      ControllersPackagesResponse result = apiInstance.listPackages(limit, offset, sort, search, filterName, filterSystemsInstalled, filterSystemsUpdatable, filterSummary, tags, filterSystemProfileSapSystem, filterSystemProfileSapSidsIn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listPackages");
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
| **limit** | **Integer**| Limit for paging, set -1 to return all | [optional] |
| **offset** | **Integer**| Offset for paging | [optional] |
| **sort** | **String**| Sort field | [optional] [enum: id, name, systems_installed, systems_updatable] |
| **search** | **String**| Find matching text | [optional] |
| **filterName** | **String**| Filter | [optional] |
| **filterSystemsInstalled** | **String**| Filter | [optional] |
| **filterSystemsUpdatable** | **String**| Filter | [optional] |
| **filterSummary** | **String**| Filter | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| Tag filter | [optional] |
| **filterSystemProfileSapSystem** | **String**| Filter only SAP systems | [optional] |
| **filterSystemProfileSapSidsIn** | [**List&lt;String&gt;**](String.md)| Filter systems by their SAP SIDs | [optional] |

### Return type

[**ControllersPackagesResponse**](ControllersPackagesResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSystemAdvisories"></a>
# **listSystemAdvisories**
> ControllersSystemAdvisoriesResponse listSystemAdvisories(inventoryId, limit, offset, sort, search, filterId, filterDescription, filterPublicDate, filterSynopsis, filterAdvisoryType, filterSeverity)

Show me advisories for a system by given inventory id

Show me advisories for a system by given inventory id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String inventoryId = "inventoryId_example"; // String | Inventory ID
    Integer limit = 56; // Integer | Limit for paging, set -1 to return all
    Integer offset = 56; // Integer | Offset for paging
    String sort = "id"; // String | Sort field
    String search = "search_example"; // String | Find matching text
    String filterId = "filterId_example"; // String | Filter
    String filterDescription = "filterDescription_example"; // String | Filter
    String filterPublicDate = "filterPublicDate_example"; // String | Filter
    String filterSynopsis = "filterSynopsis_example"; // String | Filter
    String filterAdvisoryType = "filterAdvisoryType_example"; // String | Filter
    String filterSeverity = "filterSeverity_example"; // String | Filter
    try {
      ControllersSystemAdvisoriesResponse result = apiInstance.listSystemAdvisories(inventoryId, limit, offset, sort, search, filterId, filterDescription, filterPublicDate, filterSynopsis, filterAdvisoryType, filterSeverity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSystemAdvisories");
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
| **inventoryId** | **String**| Inventory ID | |
| **limit** | **Integer**| Limit for paging, set -1 to return all | [optional] |
| **offset** | **Integer**| Offset for paging | [optional] |
| **sort** | **String**| Sort field | [optional] [enum: id, name, type, synopsis, public_date] |
| **search** | **String**| Find matching text | [optional] |
| **filterId** | **String**| Filter | [optional] |
| **filterDescription** | **String**| Filter | [optional] |
| **filterPublicDate** | **String**| Filter | [optional] |
| **filterSynopsis** | **String**| Filter | [optional] |
| **filterAdvisoryType** | **String**| Filter | [optional] |
| **filterSeverity** | **String**| Filter | [optional] |

### Return type

[**ControllersSystemAdvisoriesResponse**](ControllersSystemAdvisoriesResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSystems"></a>
# **listSystems**
> ControllersSystemsResponse listSystems(limit, offset, sort, search, filterInsightsId, filterId, filterDisplayName, filterLastEvaluation, filterLastUpload, filterRhsaCount, filterRhbaCount, filterRheaCount, filterOtherCount, filterStale, filterPackagesInstalled, filterPackagesUpdatable, filterStaleTimestamp, filterStaleWarningTimestamp, filterCulledTimestamp, filterCreated, tags, filterSystemProfileSapSystem, filterSystemProfileSapSidsIn)

Show me all my systems

Show me all my systems

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer limit = 56; // Integer | Limit for paging, set -1 to return all
    Integer offset = 56; // Integer | Offset for paging
    String sort = "id"; // String | Sort field
    String search = "search_example"; // String | Find matching text
    String filterInsightsId = "filterInsightsId_example"; // String | Filter
    String filterId = "filterId_example"; // String | Filter
    String filterDisplayName = "filterDisplayName_example"; // String | Filter
    String filterLastEvaluation = "filterLastEvaluation_example"; // String | Filter
    String filterLastUpload = "filterLastUpload_example"; // String | Filter
    String filterRhsaCount = "filterRhsaCount_example"; // String | Filter
    String filterRhbaCount = "filterRhbaCount_example"; // String | Filter
    String filterRheaCount = "filterRheaCount_example"; // String | Filter
    String filterOtherCount = "filterOtherCount_example"; // String | Filter
    String filterStale = "filterStale_example"; // String | Filter
    String filterPackagesInstalled = "filterPackagesInstalled_example"; // String | Filter
    String filterPackagesUpdatable = "filterPackagesUpdatable_example"; // String | Filter
    String filterStaleTimestamp = "filterStaleTimestamp_example"; // String | Filter
    String filterStaleWarningTimestamp = "filterStaleWarningTimestamp_example"; // String | Filter
    String filterCulledTimestamp = "filterCulledTimestamp_example"; // String | Filter
    String filterCreated = "filterCreated_example"; // String | Filter
    List<String> tags = Arrays.asList(); // List<String> | Tag filter
    String filterSystemProfileSapSystem = "filterSystemProfileSapSystem_example"; // String | Filter only SAP systems
    List<String> filterSystemProfileSapSidsIn = Arrays.asList(); // List<String> | Filter systems by their SAP SIDs
    try {
      ControllersSystemsResponse result = apiInstance.listSystems(limit, offset, sort, search, filterInsightsId, filterId, filterDisplayName, filterLastEvaluation, filterLastUpload, filterRhsaCount, filterRhbaCount, filterRheaCount, filterOtherCount, filterStale, filterPackagesInstalled, filterPackagesUpdatable, filterStaleTimestamp, filterStaleWarningTimestamp, filterCulledTimestamp, filterCreated, tags, filterSystemProfileSapSystem, filterSystemProfileSapSidsIn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSystems");
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
| **limit** | **Integer**| Limit for paging, set -1 to return all | [optional] |
| **offset** | **Integer**| Offset for paging | [optional] |
| **sort** | **String**| Sort field | [optional] [enum: id, display_name, last_evaluation, last_upload, rhsa_count, rhba_count, rhea_count, other_count, stale, packages_installed, packages_updatable] |
| **search** | **String**| Find matching text | [optional] |
| **filterInsightsId** | **String**| Filter | [optional] |
| **filterId** | **String**| Filter | [optional] |
| **filterDisplayName** | **String**| Filter | [optional] |
| **filterLastEvaluation** | **String**| Filter | [optional] |
| **filterLastUpload** | **String**| Filter | [optional] |
| **filterRhsaCount** | **String**| Filter | [optional] |
| **filterRhbaCount** | **String**| Filter | [optional] |
| **filterRheaCount** | **String**| Filter | [optional] |
| **filterOtherCount** | **String**| Filter | [optional] |
| **filterStale** | **String**| Filter | [optional] |
| **filterPackagesInstalled** | **String**| Filter | [optional] |
| **filterPackagesUpdatable** | **String**| Filter | [optional] |
| **filterStaleTimestamp** | **String**| Filter | [optional] |
| **filterStaleWarningTimestamp** | **String**| Filter | [optional] |
| **filterCulledTimestamp** | **String**| Filter | [optional] |
| **filterCreated** | **String**| Filter | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| Tag filter | [optional] |
| **filterSystemProfileSapSystem** | **String**| Filter only SAP systems | [optional] |
| **filterSystemProfileSapSidsIn** | [**List&lt;String&gt;**](String.md)| Filter systems by their SAP SIDs | [optional] |

### Return type

[**ControllersSystemsResponse**](ControllersSystemsResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="packageSystems"></a>
# **packageSystems**
> ControllersPackageSystemsResponse packageSystems(packageName, limit, offset, tags, filterSystemProfileSapSystem, filterSystemProfileSapSidsIn)

Show me all my systems which have a package installed

Show me all my systems which have a package installed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String packageName = "packageName_example"; // String | Package name
    Integer limit = 56; // Integer | Limit for paging, set -1 to return all
    Integer offset = 56; // Integer | Offset for paging
    List<String> tags = Arrays.asList(); // List<String> | Tag filter
    String filterSystemProfileSapSystem = "filterSystemProfileSapSystem_example"; // String | Filter only SAP systems
    List<String> filterSystemProfileSapSidsIn = Arrays.asList(); // List<String> | Filter systems by their SAP SIDs
    try {
      ControllersPackageSystemsResponse result = apiInstance.packageSystems(packageName, limit, offset, tags, filterSystemProfileSapSystem, filterSystemProfileSapSidsIn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#packageSystems");
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
| **packageName** | **String**| Package name | |
| **limit** | **Integer**| Limit for paging, set -1 to return all | [optional] |
| **offset** | **Integer**| Offset for paging | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| Tag filter | [optional] |
| **filterSystemProfileSapSystem** | **String**| Filter only SAP systems | [optional] |
| **filterSystemProfileSapSidsIn** | [**List&lt;String&gt;**](String.md)| Filter systems by their SAP SIDs | [optional] |

### Return type

[**ControllersPackageSystemsResponse**](ControllersPackageSystemsResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="packageVersions"></a>
# **packageVersions**
> ControllersPackageVersionsResponse packageVersions(packageName, limit, offset)

Show me all package versions installed on some system

Show me all package versions installed on some system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String packageName = "packageName_example"; // String | Package name
    Integer limit = 56; // Integer | Limit for paging, set -1 to return all
    Integer offset = 56; // Integer | Offset for paging
    try {
      ControllersPackageVersionsResponse result = apiInstance.packageVersions(packageName, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#packageVersions");
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
| **packageName** | **String**| Package name | |
| **limit** | **Integer**| Limit for paging, set -1 to return all | [optional] |
| **offset** | **Integer**| Offset for paging | [optional] |

### Return type

[**ControllersPackageVersionsResponse**](ControllersPackageVersionsResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="systemPackages"></a>
# **systemPackages**
> ControllersSystemPackageResponse systemPackages(inventoryId, limit, offset, search, filterName, filterDescription, filterEvra, filterSummary, filterUpdatable)

Show me details about a system packages by given inventory id

Show me details about a system packages by given inventory id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String inventoryId = "inventoryId_example"; // String | Inventory ID
    Integer limit = 56; // Integer | Limit for paging, set -1 to return all
    Integer offset = 56; // Integer | Offset for paging
    String search = "search_example"; // String | Find matching text
    String filterName = "filterName_example"; // String | Filter
    String filterDescription = "filterDescription_example"; // String | Filter
    String filterEvra = "filterEvra_example"; // String | Filter
    String filterSummary = "filterSummary_example"; // String | Filter
    Boolean filterUpdatable = true; // Boolean | Filter
    try {
      ControllersSystemPackageResponse result = apiInstance.systemPackages(inventoryId, limit, offset, search, filterName, filterDescription, filterEvra, filterSummary, filterUpdatable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#systemPackages");
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
| **inventoryId** | **String**| Inventory ID | |
| **limit** | **Integer**| Limit for paging, set -1 to return all | [optional] |
| **offset** | **Integer**| Offset for paging | [optional] |
| **search** | **String**| Find matching text | [optional] |
| **filterName** | **String**| Filter | [optional] |
| **filterDescription** | **String**| Filter | [optional] |
| **filterEvra** | **String**| Filter | [optional] |
| **filterSummary** | **String**| Filter | [optional] |
| **filterUpdatable** | **Boolean**| Filter | [optional] |

### Return type

[**ControllersSystemPackageResponse**](ControllersSystemPackageResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="viewAdvisoriesSystems"></a>
# **viewAdvisoriesSystems**
> ControllersAdvisoriesSystemsResponse viewAdvisoriesSystems(body)

View advisory-system pairs for selected systems and advisories

View advisory-system pairs for selected systems and advisories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ControllersSystemsAdvisoriesRequest body = new ControllersSystemsAdvisoriesRequest(); // ControllersSystemsAdvisoriesRequest | Request body
    try {
      ControllersAdvisoriesSystemsResponse result = apiInstance.viewAdvisoriesSystems(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#viewAdvisoriesSystems");
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
| **body** | [**ControllersSystemsAdvisoriesRequest**](ControllersSystemsAdvisoriesRequest.md)| Request body | |

### Return type

[**ControllersAdvisoriesSystemsResponse**](ControllersAdvisoriesSystemsResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="viewSystemsAdvisories"></a>
# **viewSystemsAdvisories**
> ControllersSystemsAdvisoriesResponse viewSystemsAdvisories(body)

View system-advisory pairs for selected systems and advisories

View system-advisory pairs for selected systems and advisories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://redhat.local");
    
    // Configure API key authorization: RhIdentity
    ApiKeyAuth RhIdentity = (ApiKeyAuth) defaultClient.getAuthentication("RhIdentity");
    RhIdentity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RhIdentity.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ControllersSystemsAdvisoriesRequest body = new ControllersSystemsAdvisoriesRequest(); // ControllersSystemsAdvisoriesRequest | Request body
    try {
      ControllersSystemsAdvisoriesResponse result = apiInstance.viewSystemsAdvisories(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#viewSystemsAdvisories");
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
| **body** | [**ControllersSystemsAdvisoriesRequest**](ControllersSystemsAdvisoriesRequest.md)| Request body | |

### Return type

[**ControllersSystemsAdvisoriesResponse**](ControllersSystemsAdvisoriesResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

