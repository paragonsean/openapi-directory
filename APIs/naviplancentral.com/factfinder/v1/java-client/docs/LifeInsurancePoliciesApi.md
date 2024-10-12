# LifeInsurancePoliciesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lifeInsurancePoliciesDeleteById**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesDeleteById) | **DELETE** /api/LifeInsurancePolicies/{id} |  |
| [**lifeInsurancePoliciesDeleteSubaccountByLifeinsurancepolicyidId**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesDeleteSubaccountByLifeinsurancepolicyidId) | **DELETE** /api/LifeInsurancePolicies/{lifeInsurancePolicyId}/Subaccounts/{id} |  |
| [**lifeInsurancePoliciesGetById**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesGetById) | **GET** /api/LifeInsurancePolicies/{id} |  |
| [**lifeInsurancePoliciesGetLifeInsurancePoliciesByFactFinderIdByFactfinderid**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesGetLifeInsurancePoliciesByFactFinderIdByFactfinderid) | **GET** /api/LifeInsurancePolicies |  |
| [**lifeInsurancePoliciesGetSubaccountByLifeinsurancepolicyidId**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesGetSubaccountByLifeinsurancepolicyidId) | **GET** /api/LifeInsurancePolicies/{lifeInsurancePolicyId}/Subaccounts/{id} |  |
| [**lifeInsurancePoliciesGetSubaccountsByLifeinsurancepolicyid**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesGetSubaccountsByLifeinsurancepolicyid) | **GET** /api/LifeInsurancePolicies/{lifeInsurancePolicyId}/Subaccounts |  |
| [**lifeInsurancePoliciesPostByModel**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesPostByModel) | **POST** /api/LifeInsurancePolicies |  |
| [**lifeInsurancePoliciesPostSubaccountByLifeinsurancepolicyidModel**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesPostSubaccountByLifeinsurancepolicyidModel) | **POST** /api/LifeInsurancePolicies/{lifeInsurancePolicyId}/Subaccounts |  |
| [**lifeInsurancePoliciesPutByIdModel**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesPutByIdModel) | **PUT** /api/LifeInsurancePolicies/{id} |  |
| [**lifeInsurancePoliciesPutSubaccountByLifeinsurancepolicyidIdModel**](LifeInsurancePoliciesApi.md#lifeInsurancePoliciesPutSubaccountByLifeinsurancepolicyidIdModel) | **PUT** /api/LifeInsurancePolicies/{lifeInsurancePolicyId}/Subaccounts/{id} |  |


<a id="lifeInsurancePoliciesDeleteById"></a>
# **lifeInsurancePoliciesDeleteById**
> lifeInsurancePoliciesDeleteById(id)



Description: The operation removes a Life Insurance Policy tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Life Insurance Policy and associated subaccounts from a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifeInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifeInsurancePoliciesApi apiInstance = new LifeInsurancePoliciesApi(defaultClient);
    Integer id = 56; // Integer | The Life Insurance Policy ID used to identify which Life Insurance Policy to remove
    try {
      apiInstance.lifeInsurancePoliciesDeleteById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifeInsurancePoliciesApi#lifeInsurancePoliciesDeleteById");
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
| **id** | **Integer**| The Life Insurance Policy ID used to identify which Life Insurance Policy to remove | |

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
| **401** | Unauthorized for Life Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Life Insurance Policy. |  -  |
| **404** | Life Insurance Policy not found. |  -  |

<a id="lifeInsurancePoliciesDeleteSubaccountByLifeinsurancepolicyidId"></a>
# **lifeInsurancePoliciesDeleteSubaccountByLifeinsurancepolicyidId**
> lifeInsurancePoliciesDeleteSubaccountByLifeinsurancepolicyidId(lifeInsurancePolicyId, id)



Description: Deletes an existing Life Insurance Policy Subaccount for an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Allows for removal of a subaccount from a Life Insurance Policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifeInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifeInsurancePoliciesApi apiInstance = new LifeInsurancePoliciesApi(defaultClient);
    Integer lifeInsurancePolicyId = 56; // Integer | The ID of the Life Insurance Policy used to delete the Life Insurance Policy Subaccount.
    Integer id = 56; // Integer | The ID of the Life Insurance Policy Subaccount.
    try {
      apiInstance.lifeInsurancePoliciesDeleteSubaccountByLifeinsurancepolicyidId(lifeInsurancePolicyId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifeInsurancePoliciesApi#lifeInsurancePoliciesDeleteSubaccountByLifeinsurancepolicyidId");
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
| **lifeInsurancePolicyId** | **Integer**| The ID of the Life Insurance Policy used to delete the Life Insurance Policy Subaccount. | |
| **id** | **Integer**| The ID of the Life Insurance Policy Subaccount. | |

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
| **401** | Unauthorized for Life Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Life Insurance Policy. |  -  |
| **404** | Life Insurance Policy Subaccount not found. |  -  |

<a id="lifeInsurancePoliciesGetById"></a>
# **lifeInsurancePoliciesGetById**
> LifeInsurancePolicyWithIdModel lifeInsurancePoliciesGetById(id)



Description: This operation retrieves a single Life Insurance Policy for the specified Life Insurance Policy ID.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policy including description and policy type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifeInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifeInsurancePoliciesApi apiInstance = new LifeInsurancePoliciesApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Life Insurance Policy used to retreive the Life Insurance Policy
    try {
      LifeInsurancePolicyWithIdModel result = apiInstance.lifeInsurancePoliciesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifeInsurancePoliciesApi#lifeInsurancePoliciesGetById");
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
| **id** | **Integer**| The ID of the Life Insurance Policy used to retreive the Life Insurance Policy | |

### Return type

[**LifeInsurancePolicyWithIdModel**](LifeInsurancePolicyWithIdModel.md)

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
| **401** | Unauthorized for Life Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Life Insurance Policy. |  -  |
| **404** | Life Insurance Policy not found. |  -  |

<a id="lifeInsurancePoliciesGetLifeInsurancePoliciesByFactFinderIdByFactfinderid"></a>
# **lifeInsurancePoliciesGetLifeInsurancePoliciesByFactFinderIdByFactfinderid**
> LifeInsurancePoliciesModel lifeInsurancePoliciesGetLifeInsurancePoliciesByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Life Insurance Policies for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policies including description and policy type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifeInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifeInsurancePoliciesApi apiInstance = new LifeInsurancePoliciesApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Life Insurance Policies
    try {
      LifeInsurancePoliciesModel result = apiInstance.lifeInsurancePoliciesGetLifeInsurancePoliciesByFactFinderIdByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifeInsurancePoliciesApi#lifeInsurancePoliciesGetLifeInsurancePoliciesByFactFinderIdByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Life Insurance Policies | |

### Return type

[**LifeInsurancePoliciesModel**](LifeInsurancePoliciesModel.md)

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
| **401** | Unauthorized for Life Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Life Insurance Policy. |  -  |
| **404** | Life Insurance Policy not found. |  -  |

<a id="lifeInsurancePoliciesGetSubaccountByLifeinsurancepolicyidId"></a>
# **lifeInsurancePoliciesGetSubaccountByLifeinsurancepolicyidId**
> LifeInsurancePolicySubaccountWithIdModel lifeInsurancePoliciesGetSubaccountByLifeinsurancepolicyidId(lifeInsurancePolicyId, id)



Description: Get a specific subaccount for an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policy subaccount.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifeInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifeInsurancePoliciesApi apiInstance = new LifeInsurancePoliciesApi(defaultClient);
    Integer lifeInsurancePolicyId = 56; // Integer | The ID of the Life Insurance Policy used to retrieve the Life Insurance Policy Subaccount.
    Integer id = 56; // Integer | The ID of the Life Insurance Policy Subaccount.
    try {
      LifeInsurancePolicySubaccountWithIdModel result = apiInstance.lifeInsurancePoliciesGetSubaccountByLifeinsurancepolicyidId(lifeInsurancePolicyId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifeInsurancePoliciesApi#lifeInsurancePoliciesGetSubaccountByLifeinsurancepolicyidId");
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
| **lifeInsurancePolicyId** | **Integer**| The ID of the Life Insurance Policy used to retrieve the Life Insurance Policy Subaccount. | |
| **id** | **Integer**| The ID of the Life Insurance Policy Subaccount. | |

### Return type

[**LifeInsurancePolicySubaccountWithIdModel**](LifeInsurancePolicySubaccountWithIdModel.md)

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
| **401** | Unauthorized for Life Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Life Insurance Policy. |  -  |
| **404** | Life Insurance Policy Subaccount not found. |  -  |

<a id="lifeInsurancePoliciesGetSubaccountsByLifeinsurancepolicyid"></a>
# **lifeInsurancePoliciesGetSubaccountsByLifeinsurancepolicyid**
> LifeInsurancePolicySubaccountsModel lifeInsurancePoliciesGetSubaccountsByLifeinsurancepolicyid(lifeInsurancePolicyId)



Description: Get all the subaccounts for an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Provides access to all the Life Insurance Policy subaccounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifeInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifeInsurancePoliciesApi apiInstance = new LifeInsurancePoliciesApi(defaultClient);
    Integer lifeInsurancePolicyId = 56; // Integer | The ID of the Life Insurance Policy used to retrieve the Life Insurance Policy Subaccounts.
    try {
      LifeInsurancePolicySubaccountsModel result = apiInstance.lifeInsurancePoliciesGetSubaccountsByLifeinsurancepolicyid(lifeInsurancePolicyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifeInsurancePoliciesApi#lifeInsurancePoliciesGetSubaccountsByLifeinsurancepolicyid");
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
| **lifeInsurancePolicyId** | **Integer**| The ID of the Life Insurance Policy used to retrieve the Life Insurance Policy Subaccounts. | |

### Return type

[**LifeInsurancePolicySubaccountsModel**](LifeInsurancePolicySubaccountsModel.md)

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
| **401** | Unauthorized for Life Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Life Insurance Policy. |  -  |
| **404** | Life Insurance Policy not found. |  -  |

<a id="lifeInsurancePoliciesPostByModel"></a>
# **lifeInsurancePoliciesPostByModel**
> LifeInsurancePolicyWithIdModel lifeInsurancePoliciesPostByModel(model)



Description: The operation creates a Life Insurance Policy.&lt;br /&gt;                Purpose: Allows for creation of Life Insurance Policies on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifeInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifeInsurancePoliciesApi apiInstance = new LifeInsurancePoliciesApi(defaultClient);
    LifeInsurancePolicyModel model = new LifeInsurancePolicyModel(); // LifeInsurancePolicyModel | The Life Insurance Policy to be added to the Fact Finder
    try {
      LifeInsurancePolicyWithIdModel result = apiInstance.lifeInsurancePoliciesPostByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifeInsurancePoliciesApi#lifeInsurancePoliciesPostByModel");
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
| **model** | [**LifeInsurancePolicyModel**](LifeInsurancePolicyModel.md)| The Life Insurance Policy to be added to the Fact Finder | |

### Return type

[**LifeInsurancePolicyWithIdModel**](LifeInsurancePolicyWithIdModel.md)

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
| **401** | Unauthorized for Life Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Life Insurance Policy. |  -  |
| **404** | Life Insurance Policy not found. |  -  |

<a id="lifeInsurancePoliciesPostSubaccountByLifeinsurancepolicyidModel"></a>
# **lifeInsurancePoliciesPostSubaccountByLifeinsurancepolicyidModel**
> LifeInsurancePolicySubaccountWithIdModel lifeInsurancePoliciesPostSubaccountByLifeinsurancepolicyidModel(lifeInsurancePolicyId, model)



Description: Creates a subaccount and adds it to an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Allows for creation of subaccount on a Life Insurance Policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifeInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifeInsurancePoliciesApi apiInstance = new LifeInsurancePoliciesApi(defaultClient);
    Integer lifeInsurancePolicyId = 56; // Integer | The ID of the Life Insurance Policy used to create the Life Insurance Policy Subaccount.
    LifeInsurancePolicySubaccountModel model = new LifeInsurancePolicySubaccountModel(); // LifeInsurancePolicySubaccountModel | The Life Insurance Policy Subaccount model.
    try {
      LifeInsurancePolicySubaccountWithIdModel result = apiInstance.lifeInsurancePoliciesPostSubaccountByLifeinsurancepolicyidModel(lifeInsurancePolicyId, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifeInsurancePoliciesApi#lifeInsurancePoliciesPostSubaccountByLifeinsurancepolicyidModel");
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
| **lifeInsurancePolicyId** | **Integer**| The ID of the Life Insurance Policy used to create the Life Insurance Policy Subaccount. | |
| **model** | [**LifeInsurancePolicySubaccountModel**](LifeInsurancePolicySubaccountModel.md)| The Life Insurance Policy Subaccount model. | |

### Return type

[**LifeInsurancePolicySubaccountWithIdModel**](LifeInsurancePolicySubaccountWithIdModel.md)

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
| **401** | Unauthorized for Life Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Life Insurance Policy. |  -  |
| **404** | Life Insurance Policy not found. |  -  |

<a id="lifeInsurancePoliciesPutByIdModel"></a>
# **lifeInsurancePoliciesPutByIdModel**
> LifeInsurancePolicyWithIdModel lifeInsurancePoliciesPutByIdModel(id, model)



Description: The operation updates a Life Insurance Policy, deletes associated sub-accounts if the policy type changes.&lt;br /&gt;                Purpose: Allows for complete replacement of a Life Insurance Policy on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifeInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifeInsurancePoliciesApi apiInstance = new LifeInsurancePoliciesApi(defaultClient);
    Integer id = 56; // Integer | The existing Life Insurance Policy ID used to identify which Life Insurance Policy to update
    LifeInsurancePolicyModel model = new LifeInsurancePolicyModel(); // LifeInsurancePolicyModel | The Life Insurance Policy to be updated on a Fact Finder
    try {
      LifeInsurancePolicyWithIdModel result = apiInstance.lifeInsurancePoliciesPutByIdModel(id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifeInsurancePoliciesApi#lifeInsurancePoliciesPutByIdModel");
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
| **id** | **Integer**| The existing Life Insurance Policy ID used to identify which Life Insurance Policy to update | |
| **model** | [**LifeInsurancePolicyModel**](LifeInsurancePolicyModel.md)| The Life Insurance Policy to be updated on a Fact Finder | |

### Return type

[**LifeInsurancePolicyWithIdModel**](LifeInsurancePolicyWithIdModel.md)

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
| **401** | Unauthorized for Life Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Life Insurance Policy. |  -  |
| **404** | Life Insurance Policy not found. |  -  |

<a id="lifeInsurancePoliciesPutSubaccountByLifeinsurancepolicyidIdModel"></a>
# **lifeInsurancePoliciesPutSubaccountByLifeinsurancepolicyidIdModel**
> LifeInsurancePolicySubaccountModel lifeInsurancePoliciesPutSubaccountByLifeinsurancepolicyidIdModel(lifeInsurancePolicyId, id, model)



Description: Updates an existing Life Insurance Policy Subaccount for an existing Life Insurance Policy.&lt;br /&gt;                Purpose: Allows for complete replacement of a subaccount on a Life Insurance Policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifeInsurancePoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifeInsurancePoliciesApi apiInstance = new LifeInsurancePoliciesApi(defaultClient);
    Integer lifeInsurancePolicyId = 56; // Integer | The ID of the Life Insurance Policy used to update the Life Insurance Policy Subaccount.
    Integer id = 56; // Integer | The ID of the Life Insurance Policy Subaccount.
    LifeInsurancePolicySubaccountModel model = new LifeInsurancePolicySubaccountModel(); // LifeInsurancePolicySubaccountModel | The Life Insurance Policy Subaccount model.
    try {
      LifeInsurancePolicySubaccountModel result = apiInstance.lifeInsurancePoliciesPutSubaccountByLifeinsurancepolicyidIdModel(lifeInsurancePolicyId, id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifeInsurancePoliciesApi#lifeInsurancePoliciesPutSubaccountByLifeinsurancepolicyidIdModel");
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
| **lifeInsurancePolicyId** | **Integer**| The ID of the Life Insurance Policy used to update the Life Insurance Policy Subaccount. | |
| **id** | **Integer**| The ID of the Life Insurance Policy Subaccount. | |
| **model** | [**LifeInsurancePolicySubaccountModel**](LifeInsurancePolicySubaccountModel.md)| The Life Insurance Policy Subaccount model. | |

### Return type

[**LifeInsurancePolicySubaccountModel**](LifeInsurancePolicySubaccountModel.md)

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
| **401** | Unauthorized for Life Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Life Insurance Policy. |  -  |
| **404** | Life Insurance Policy Subaccount not found. |  -  |

