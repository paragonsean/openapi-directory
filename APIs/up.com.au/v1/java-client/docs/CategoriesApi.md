# CategoriesApi

All URIs are relative to *https://api.up.com.au/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**categoriesGet**](CategoriesApi.md#categoriesGet) | **GET** /categories | List categories |
| [**categoriesIdGet**](CategoriesApi.md#categoriesIdGet) | **GET** /categories/{id} | Retrieve category |
| [**transactionsTransactionIdRelationshipsCategoryPatch**](CategoriesApi.md#transactionsTransactionIdRelationshipsCategoryPatch) | **PATCH** /transactions/{transactionId}/relationships/category | Categorize transaction |


<a id="categoriesGet"></a>
# **categoriesGet**
> ListCategoriesResponse categoriesGet(filterParent)

List categories

Retrieve a list of all categories and their ancestry. The returned list is not paginated. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String filterParent = "good-life"; // String | The unique identifier of a parent category for which to return only its children. Providing an invalid category identifier results in a `404` response. 
    try {
      ListCategoriesResponse result = apiInstance.categoriesGet(filterParent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesGet");
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
| **filterParent** | **String**| The unique identifier of a parent category for which to return only its children. Providing an invalid category identifier results in a &#x60;404&#x60; response.  | [optional] |

### Return type

[**ListCategoriesResponse**](ListCategoriesResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="categoriesIdGet"></a>
# **categoriesIdGet**
> GetCategoryResponse categoriesIdGet(id)

Retrieve category

Retrieve a specific category by providing its unique identifier. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String id = "restaurants-and-cafes"; // String | The unique identifier for the category. 
    try {
      GetCategoryResponse result = apiInstance.categoriesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesIdGet");
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
| **id** | **String**| The unique identifier for the category.  | |

### Return type

[**GetCategoryResponse**](GetCategoryResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="transactionsTransactionIdRelationshipsCategoryPatch"></a>
# **transactionsTransactionIdRelationshipsCategoryPatch**
> transactionsTransactionIdRelationshipsCategoryPatch(transactionId, updateTransactionCategoryRequest)

Categorize transaction

Updates the category associated with a transaction. Only transactions for which &#x60;isCategorizable&#x60; is set to true support this operation. The &#x60;id&#x60; is taken from the list exposed on &#x60;/categories&#x60; and cannot be one of the top-level (parent) categories. To de-categorize a transaction, set the entire &#x60;data&#x60; key to &#x60;null&#x60;. An HTTP &#x60;204&#x60; is returned on success. The associated category, along with its request URL is also exposed via the &#x60;category&#x60; relationship on the transaction resource returned from &#x60;/transactions/{id}&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String transactionId = "a572c7c3-b637-433c-a4ce-c0be5dcb0a5a"; // String | The unique identifier for the transaction. 
    UpdateTransactionCategoryRequest updateTransactionCategoryRequest = new UpdateTransactionCategoryRequest(); // UpdateTransactionCategoryRequest | 
    try {
      apiInstance.transactionsTransactionIdRelationshipsCategoryPatch(transactionId, updateTransactionCategoryRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#transactionsTransactionIdRelationshipsCategoryPatch");
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
| **transactionId** | **String**| The unique identifier for the transaction.  | |
| **updateTransactionCategoryRequest** | [**UpdateTransactionCategoryRequest**](UpdateTransactionCategoryRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful Response |  -  |

