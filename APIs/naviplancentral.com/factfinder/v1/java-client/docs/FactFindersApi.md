# FactFindersApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**factFindersDeleteById**](FactFindersApi.md#factFindersDeleteById) | **DELETE** /api/FactFinders/{id} |  |
| [**factFindersGetByHouseholdIdByHouseholdid**](FactFindersApi.md#factFindersGetByHouseholdIdByHouseholdid) | **GET** /api/FactFinders |  |
| [**factFindersGetById**](FactFindersApi.md#factFindersGetById) | **GET** /api/FactFinders/{id} |  |
| [**factFindersGetSnapshotsByFactfinderid**](FactFindersApi.md#factFindersGetSnapshotsByFactfinderid) | **GET** /api/FactFinders/{factFinderId}/Snapshots |  |
| [**factFindersPostByModel**](FactFindersApi.md#factFindersPostByModel) | **POST** /api/FactFinders |  |
| [**factFindersPostPopulateByModel**](FactFindersApi.md#factFindersPostPopulateByModel) | **POST** /api/FactFinders/Populate |  |
| [**factFindersPostSnapshotsByFactfinderid**](FactFindersApi.md#factFindersPostSnapshotsByFactfinderid) | **POST** /api/FactFinders/{factFinderId}/Snapshots |  |
| [**factFindersPutByIdModel**](FactFindersApi.md#factFindersPutByIdModel) | **PUT** /api/FactFinders/{id} |  |
| [**factFindersPutPopulateFactFinderByIdModel**](FactFindersApi.md#factFindersPutPopulateFactFinderByIdModel) | **PUT** /api/FactFinders/{id}/Populate |  |


<a id="factFindersDeleteById"></a>
# **factFindersDeleteById**
> Object factFindersDeleteById(id)



Description: This operation deletes a single Fact Finder for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Deletes the fact finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FactFindersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    FactFindersApi apiInstance = new FactFindersApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Fact Finder to be deleted
    try {
      Object result = apiInstance.factFindersDeleteById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FactFindersApi#factFindersDeleteById");
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
| **id** | **Integer**| The ID of the Fact Finder to be deleted | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | Deleted |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Fact Finder data access. |  -  |
| **403** | Request is restricted for access to Fact Finder. |  -  |
| **404** | Fact Finder not found. |  -  |

<a id="factFindersGetByHouseholdIdByHouseholdid"></a>
# **factFindersGetByHouseholdIdByHouseholdid**
> List&lt;FactFinderWithIdModel&gt; factFindersGetByHouseholdIdByHouseholdid(householdId)



Description: This operation retrieves all Fact Finders for the specified householdId,                 or if null, all households associated with the user.&lt;br /&gt;                Purpose: Provides access to the Fact Finder including status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FactFindersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    FactFindersApi apiInstance = new FactFindersApi(defaultClient);
    Integer householdId = 56; // Integer | The ID of the household used to retrieve the fact finders. If not set, uses all households associated with the user
    try {
      List<FactFinderWithIdModel> result = apiInstance.factFindersGetByHouseholdIdByHouseholdid(householdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FactFindersApi#factFindersGetByHouseholdIdByHouseholdid");
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
| **householdId** | **Integer**| The ID of the household used to retrieve the fact finders. If not set, uses all households associated with the user | [optional] |

### Return type

[**List&lt;FactFinderWithIdModel&gt;**](FactFinderWithIdModel.md)

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
| **401** | Unauthorized for Fact Finder data access. |  -  |
| **403** | Request is restricted for access to Fact Finder. |  -  |
| **404** | Fact Finder not found. |  -  |

<a id="factFindersGetById"></a>
# **factFindersGetById**
> FactFinderWithIdModel factFindersGetById(id)



Description: This operation retrieves a single Fact Finder for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Fact Finder including status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FactFindersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    FactFindersApi apiInstance = new FactFindersApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Fact Finder used to retrieve the Fact Finder
    try {
      FactFinderWithIdModel result = apiInstance.factFindersGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FactFindersApi#factFindersGetById");
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
| **id** | **Integer**| The ID of the Fact Finder used to retrieve the Fact Finder | |

### Return type

[**FactFinderWithIdModel**](FactFinderWithIdModel.md)

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
| **401** | Unauthorized for Fact Finder data access. |  -  |
| **403** | Request is restricted for access to Fact Finder. |  -  |
| **404** | Fact Finder not found. |  -  |

<a id="factFindersGetSnapshotsByFactfinderid"></a>
# **factFindersGetSnapshotsByFactfinderid**
> FactFinderSnapshotsModel factFindersGetSnapshotsByFactfinderid(factFinderId)



Description: The operation retrieves Snapshots of a Fact Finder.&lt;br /&gt;                Purpose: Allows for advisors to view all Snapshots taken of a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FactFindersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    FactFindersApi apiInstance = new FactFindersApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder to retrieve Snapshots for
    try {
      FactFinderSnapshotsModel result = apiInstance.factFindersGetSnapshotsByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FactFindersApi#factFindersGetSnapshotsByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder to retrieve Snapshots for | |

### Return type

[**FactFinderSnapshotsModel**](FactFinderSnapshotsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Created |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Fact Finder data access. |  -  |
| **403** | Request is restricted for access to Fact Finder. |  -  |
| **404** | Fact Finder not found. |  -  |

<a id="factFindersPostByModel"></a>
# **factFindersPostByModel**
> Object factFindersPostByModel(model)



Description: The operation creates a completely empty draft Fact Finder.&lt;br /&gt;                Requirements: A householdId and list of modules must be provided.&lt;br /&gt;                Purpose: Stages a Fact Finder for population.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FactFindersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    FactFindersApi apiInstance = new FactFindersApi(defaultClient);
    FactFinderEntityModel model = new FactFinderEntityModel(); // FactFinderEntityModel | The Household the Fact Finder will belong to and the modules that are available.
    try {
      Object result = apiInstance.factFindersPostByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FactFindersApi#factFindersPostByModel");
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
| **model** | [**FactFinderEntityModel**](FactFinderEntityModel.md)| The Household the Fact Finder will belong to and the modules that are available. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Fact Finder data access. |  -  |
| **403** | Request is restricted for access to Fact Finder. |  -  |
| **404** | Fact Finder not found. |  -  |
| **409** | The request cannot be completed. |  -  |

<a id="factFindersPostPopulateByModel"></a>
# **factFindersPostPopulateByModel**
> Object factFindersPostPopulateByModel(model)



Description: The operation creates a new Populated Fact Finder.&lt;br /&gt;                Requirements: A householdId and list of modules must be provided.&lt;br /&gt;                Purpose: Creation of a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FactFindersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    FactFindersApi apiInstance = new FactFindersApi(defaultClient);
    FactFinderPopulatableEntityModel model = new FactFinderPopulatableEntityModel(); // FactFinderPopulatableEntityModel | The Household the Fact Finder will belong to and the modules that are available.               Optional PlanId to populate from
    try {
      Object result = apiInstance.factFindersPostPopulateByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FactFindersApi#factFindersPostPopulateByModel");
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
| **model** | [**FactFinderPopulatableEntityModel**](FactFinderPopulatableEntityModel.md)| The Household the Fact Finder will belong to and the modules that are available.               Optional PlanId to populate from | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Fact Finder data access. |  -  |
| **403** | Request is restricted for access to Fact Finder. |  -  |
| **404** | Fact Finder not found. |  -  |
| **409** | The request cannot be completed. |  -  |

<a id="factFindersPostSnapshotsByFactfinderid"></a>
# **factFindersPostSnapshotsByFactfinderid**
> Object factFindersPostSnapshotsByFactfinderid(factFinderId)



Description: The operation creates a Snapshot of a Fact Finder.&lt;br /&gt;                Purpose: Allows for advisors to compare the current fact finder to a snapshot prior to acceptance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FactFindersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    FactFindersApi apiInstance = new FactFindersApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to create the Fact Finder Snapshot
    try {
      Object result = apiInstance.factFindersPostSnapshotsByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FactFindersApi#factFindersPostSnapshotsByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to create the Fact Finder Snapshot | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Fact Finder data access. |  -  |
| **403** | Request is restricted for access to Fact Finder. |  -  |
| **404** | Fact Finder not found. |  -  |

<a id="factFindersPutByIdModel"></a>
# **factFindersPutByIdModel**
> FactFinderWithIdModel factFindersPutByIdModel(id, model)



Description: The operation updates a Fact Finder.&lt;br /&gt;                Purpose: Allows for the updating of a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FactFindersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    FactFindersApi apiInstance = new FactFindersApi(defaultClient);
    Integer id = 56; // Integer | The existing Fact Finder ID used to identify which Fact Finder to update
    FactFinderModel model = new FactFinderModel(); // FactFinderModel | The Fact Finder to be updated
    try {
      FactFinderWithIdModel result = apiInstance.factFindersPutByIdModel(id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FactFindersApi#factFindersPutByIdModel");
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
| **id** | **Integer**| The existing Fact Finder ID used to identify which Fact Finder to update | |
| **model** | [**FactFinderModel**](FactFinderModel.md)| The Fact Finder to be updated | |

### Return type

[**FactFinderWithIdModel**](FactFinderWithIdModel.md)

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
| **401** | Unauthorized for Fact Finder data access. |  -  |
| **403** | Request is restricted for access to Fact Finder. |  -  |
| **404** | Fact Finder not found. |  -  |

<a id="factFindersPutPopulateFactFinderByIdModel"></a>
# **factFindersPutPopulateFactFinderByIdModel**
> FactFinderWithIdModel factFindersPutPopulateFactFinderByIdModel(id, model)



Description: The operation populates a fact finder.&lt;br /&gt;                Purpose: Allows for the population of a Fact Finder based on a NaviPlan plan or client. This                         operation cannot be performed on a Fact Finder more than once.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FactFindersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    FactFindersApi apiInstance = new FactFindersApi(defaultClient);
    Integer id = 56; // Integer | The existing Fact Finder ID used to identify which Fact Finder to populate.
    FactFinderPopulationModel model = new FactFinderPopulationModel(); // FactFinderPopulationModel | The plan to populate a fact finder from. If not provided, the client id will be inferred.
    try {
      FactFinderWithIdModel result = apiInstance.factFindersPutPopulateFactFinderByIdModel(id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FactFindersApi#factFindersPutPopulateFactFinderByIdModel");
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
| **id** | **Integer**| The existing Fact Finder ID used to identify which Fact Finder to populate. | |
| **model** | [**FactFinderPopulationModel**](FactFinderPopulationModel.md)| The plan to populate a fact finder from. If not provided, the client id will be inferred. | |

### Return type

[**FactFinderWithIdModel**](FactFinderWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Fact Finder was successfully populated. |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Fact Finder data access. |  -  |
| **403** | Request is restricted for access to Fact Finder. |  -  |
| **404** | Fact Finder not found. |  -  |
| **409** | Fact Finder already populated. |  -  |

