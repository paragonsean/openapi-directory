# DemographicsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**demographicsDeleteDependentByDemographicidId**](DemographicsApi.md#demographicsDeleteDependentByDemographicidId) | **DELETE** /api/Demographics/{demographicId}/Dependents/{id} |  |
| [**demographicsGetById**](DemographicsApi.md#demographicsGetById) | **GET** /api/Demographics/{id} |  |
| [**demographicsGetDemographicsByFactFinderIdByFactfinderid**](DemographicsApi.md#demographicsGetDemographicsByFactFinderIdByFactfinderid) | **GET** /api/Demographics |  |
| [**demographicsGetDependentByDemographicidId**](DemographicsApi.md#demographicsGetDependentByDemographicidId) | **GET** /api/Demographics/{demographicId}/Dependents/{id} |  |
| [**demographicsGetDependentsByDemographicid**](DemographicsApi.md#demographicsGetDependentsByDemographicid) | **GET** /api/Demographics/{demographicId}/Dependents |  |
| [**demographicsPostByDemographicidModel**](DemographicsApi.md#demographicsPostByDemographicidModel) | **POST** /api/Demographics/{demographicId}/Dependents |  |
| [**demographicsPostByModel**](DemographicsApi.md#demographicsPostByModel) | **POST** /api/Demographics |  |
| [**demographicsPutByDemographicidIdModel**](DemographicsApi.md#demographicsPutByDemographicidIdModel) | **PUT** /api/Demographics/{demographicId}/Dependents/{id} |  |
| [**demographicsPutByIdModel**](DemographicsApi.md#demographicsPutByIdModel) | **PUT** /api/Demographics/{id} |  |


<a id="demographicsDeleteDependentByDemographicidId"></a>
# **demographicsDeleteDependentByDemographicidId**
> demographicsDeleteDependentByDemographicidId(demographicId, id)



Description: The operation removes a Dependent tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Dependent from a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DemographicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DemographicsApi apiInstance = new DemographicsApi(defaultClient);
    Integer demographicId = 56; // Integer | The ID of the Demographic information used to identify which Dependent to remove
    Integer id = 56; // Integer | The Dependent ID used to identify which Dependent to remove
    try {
      apiInstance.demographicsDeleteDependentByDemographicidId(demographicId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DemographicsApi#demographicsDeleteDependentByDemographicidId");
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
| **demographicId** | **Integer**| The ID of the Demographic information used to identify which Dependent to remove | |
| **id** | **Integer**| The Dependent ID used to identify which Dependent to remove | |

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
| **204** | Deleted |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Dependent information data access. |  -  |
| **403** | Request is restricted for access to Dependent information. |  -  |
| **404** | Dependent information not found. |  -  |

<a id="demographicsGetById"></a>
# **demographicsGetById**
> DemographicsWithIdModel demographicsGetById(id)



Description: This operation retrieves Demographic information for the specified Demographic information ID.&lt;br /&gt;                Purpose: Provides access to the Demographic information including city and state.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DemographicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DemographicsApi apiInstance = new DemographicsApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Demographic information used to retreive the Demographic information
    try {
      DemographicsWithIdModel result = apiInstance.demographicsGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DemographicsApi#demographicsGetById");
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
| **id** | **Integer**| The ID of the Demographic information used to retreive the Demographic information | |

### Return type

[**DemographicsWithIdModel**](DemographicsWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Demographic information data access. |  -  |
| **403** | Request is restricted for access to Demographic information. |  -  |
| **404** | Demographic information not found. |  -  |

<a id="demographicsGetDemographicsByFactFinderIdByFactfinderid"></a>
# **demographicsGetDemographicsByFactFinderIdByFactfinderid**
> DemographicsWithIdModel demographicsGetDemographicsByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Demographic information for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Demographic information including city and state.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DemographicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DemographicsApi apiInstance = new DemographicsApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Demographic information
    try {
      DemographicsWithIdModel result = apiInstance.demographicsGetDemographicsByFactFinderIdByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DemographicsApi#demographicsGetDemographicsByFactFinderIdByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Demographic information | |

### Return type

[**DemographicsWithIdModel**](DemographicsWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Demographic information data access. |  -  |
| **403** | Request is restricted for access to Demographic information. |  -  |
| **404** | Demographic information not found. |  -  |

<a id="demographicsGetDependentByDemographicidId"></a>
# **demographicsGetDependentByDemographicidId**
> DemographicsDependentWithIdModel demographicsGetDependentByDemographicidId(demographicId, id)



Description: This operation retrieves a single Dependent for the specified Dependent ID.&lt;br /&gt;                Purpose: Provides access to the Dependent including first and last name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DemographicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DemographicsApi apiInstance = new DemographicsApi(defaultClient);
    Integer demographicId = 56; // Integer | The ID of the Demographic information used to retrieve Dependents
    Integer id = 56; // Integer | The ID of the Dependent used to retreive the Dependent
    try {
      DemographicsDependentWithIdModel result = apiInstance.demographicsGetDependentByDemographicidId(demographicId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DemographicsApi#demographicsGetDependentByDemographicidId");
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
| **demographicId** | **Integer**| The ID of the Demographic information used to retrieve Dependents | |
| **id** | **Integer**| The ID of the Dependent used to retreive the Dependent | |

### Return type

[**DemographicsDependentWithIdModel**](DemographicsDependentWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Demographic information data access. |  -  |
| **403** | Request is restricted for access to Demographic information. |  -  |
| **404** | Demographic information not found. |  -  |

<a id="demographicsGetDependentsByDemographicid"></a>
# **demographicsGetDependentsByDemographicid**
> DemographicsDependentsModel demographicsGetDependentsByDemographicid(demographicId)



Description: This operation retrieves all Dependents for the specified Demographic information ID.&lt;br /&gt;                Purpose: Provides access to the Dependents including first and last name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DemographicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DemographicsApi apiInstance = new DemographicsApi(defaultClient);
    Integer demographicId = 56; // Integer | The ID of the Demographic information used to retrieve Dependents
    try {
      DemographicsDependentsModel result = apiInstance.demographicsGetDependentsByDemographicid(demographicId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DemographicsApi#demographicsGetDependentsByDemographicid");
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
| **demographicId** | **Integer**| The ID of the Demographic information used to retrieve Dependents | |

### Return type

[**DemographicsDependentsModel**](DemographicsDependentsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Demographic information data access. |  -  |
| **403** | Request is restricted for access to Demographic information. |  -  |
| **404** | Demographic information not found. |  -  |

<a id="demographicsPostByDemographicidModel"></a>
# **demographicsPostByDemographicidModel**
> DemographicsDependentWithIdModel demographicsPostByDemographicidModel(demographicId, model)



Description: The operation creates a Dependent.&lt;br /&gt;                Purpose: Allows for creation of Dependents on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DemographicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DemographicsApi apiInstance = new DemographicsApi(defaultClient);
    Integer demographicId = 56; // Integer | The ID of the Demographic information to add the Dependent to
    DemographicsDependentModel model = new DemographicsDependentModel(); // DemographicsDependentModel | The Dependent to be added to the Fact Finder
    try {
      DemographicsDependentWithIdModel result = apiInstance.demographicsPostByDemographicidModel(demographicId, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DemographicsApi#demographicsPostByDemographicidModel");
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
| **demographicId** | **Integer**| The ID of the Demographic information to add the Dependent to | |
| **model** | [**DemographicsDependentModel**](DemographicsDependentModel.md)| The Dependent to be added to the Fact Finder | |

### Return type

[**DemographicsDependentWithIdModel**](DemographicsDependentWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Dependent information data access. |  -  |
| **403** | Request is restricted for access to Dependent information. |  -  |
| **404** | Dependent information not found. |  -  |
| **409** | The request cannot be completed. |  -  |

<a id="demographicsPostByModel"></a>
# **demographicsPostByModel**
> DemographicsWithIdModel demographicsPostByModel(model)



Description: The operation creates Demographic information.&lt;br /&gt;                Purpose: Allows for creation of Demographic information on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DemographicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DemographicsApi apiInstance = new DemographicsApi(defaultClient);
    DemographicsModel model = new DemographicsModel(); // DemographicsModel | The Demographic information to be added to the Fact Finder
    try {
      DemographicsWithIdModel result = apiInstance.demographicsPostByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DemographicsApi#demographicsPostByModel");
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
| **model** | [**DemographicsModel**](DemographicsModel.md)| The Demographic information to be added to the Fact Finder | |

### Return type

[**DemographicsWithIdModel**](DemographicsWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Demographic information data access. |  -  |
| **403** | Request is restricted for access to Demographic information. |  -  |
| **404** | Demographic information not found. |  -  |

<a id="demographicsPutByDemographicidIdModel"></a>
# **demographicsPutByDemographicidIdModel**
> DemographicsDependentWithIdModel demographicsPutByDemographicidIdModel(demographicId, id, model)



Description: The operation updates a Dependent.&lt;br /&gt;                Purpose: Allows for complete replacement of a Dependent on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DemographicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DemographicsApi apiInstance = new DemographicsApi(defaultClient);
    Integer demographicId = 56; // Integer | The ID of the Demographic information used to identify which Dependent to update
    Integer id = 56; // Integer | The existing Dependent ID used to identify which Dependent to update
    DemographicsDependentModel model = new DemographicsDependentModel(); // DemographicsDependentModel | The Dependent to be updated on a Fact Finder
    try {
      DemographicsDependentWithIdModel result = apiInstance.demographicsPutByDemographicidIdModel(demographicId, id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DemographicsApi#demographicsPutByDemographicidIdModel");
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
| **demographicId** | **Integer**| The ID of the Demographic information used to identify which Dependent to update | |
| **id** | **Integer**| The existing Dependent ID used to identify which Dependent to update | |
| **model** | [**DemographicsDependentModel**](DemographicsDependentModel.md)| The Dependent to be updated on a Fact Finder | |

### Return type

[**DemographicsDependentWithIdModel**](DemographicsDependentWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Dependent information data access. |  -  |
| **403** | Request is restricted for access to Dependent information. |  -  |
| **404** | Dependent information not found. |  -  |

<a id="demographicsPutByIdModel"></a>
# **demographicsPutByIdModel**
> DemographicsWithIdModel demographicsPutByIdModel(id, model)



Description: The operation updates Demographic information.&lt;br /&gt;                Purpose: Allows for complete replacement of Demographic information on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DemographicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    DemographicsApi apiInstance = new DemographicsApi(defaultClient);
    Integer id = 56; // Integer | The existing Demographic information ID used to identify which Demographic information to update
    DemographicsModel model = new DemographicsModel(); // DemographicsModel | The Demographic information to be updated on a Fact Finder
    try {
      DemographicsWithIdModel result = apiInstance.demographicsPutByIdModel(id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DemographicsApi#demographicsPutByIdModel");
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
| **id** | **Integer**| The existing Demographic information ID used to identify which Demographic information to update | |
| **model** | [**DemographicsModel**](DemographicsModel.md)| The Demographic information to be updated on a Fact Finder | |

### Return type

[**DemographicsWithIdModel**](DemographicsWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Demographic information data access. |  -  |
| **403** | Request is restricted for access to Demographic information. |  -  |
| **404** | Demographic information not found. |  -  |
| **409** | The request cannot be completed. |  -  |

