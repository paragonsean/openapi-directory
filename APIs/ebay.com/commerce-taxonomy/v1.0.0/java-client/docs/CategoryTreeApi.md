# CategoryTreeApi

All URIs are relative to *https://api.ebay.com/commerce/taxonomy/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchItemAspects**](CategoryTreeApi.md#fetchItemAspects) | **GET** /category_tree/{category_tree_id}/fetch_item_aspects | Get Aspects for All Leaf Categories in a Marketplace |
| [**getCategorySubtree**](CategoryTreeApi.md#getCategorySubtree) | **GET** /category_tree/{category_tree_id}/get_category_subtree | Get a Category Subtree |
| [**getCategorySuggestions**](CategoryTreeApi.md#getCategorySuggestions) | **GET** /category_tree/{category_tree_id}/get_category_suggestions | Get Suggested Categories |
| [**getCategoryTree**](CategoryTreeApi.md#getCategoryTree) | **GET** /category_tree/{category_tree_id} | Get a Category Tree |
| [**getCompatibilityProperties**](CategoryTreeApi.md#getCompatibilityProperties) | **GET** /category_tree/{category_tree_id}/get_compatibility_properties | Get Compatibility Properties |
| [**getCompatibilityPropertyValues**](CategoryTreeApi.md#getCompatibilityPropertyValues) | **GET** /category_tree/{category_tree_id}/get_compatibility_property_values | Get Compatibility Property Values |
| [**getDefaultCategoryTreeId**](CategoryTreeApi.md#getDefaultCategoryTreeId) | **GET** /get_default_category_tree_id | Get a Default Category Tree ID |
| [**getItemAspectsForCategory**](CategoryTreeApi.md#getItemAspectsForCategory) | **GET** /category_tree/{category_tree_id}/get_item_aspects_for_category |  |


<a id="fetchItemAspects"></a>
# **fetchItemAspects**
> GetCategoriesAspectResponse fetchItemAspects(categoryTreeId)

Get Aspects for All Leaf Categories in a Marketplace

Note: The General Availability (GA) version of the Taxonomy API has been released. Developers currently using the Beta version should make plans to migrate to the new GA version, as the Beta version will be decommissioned on March 31, 2021. Until that date, the Beta version documentation set can be accessed through the All API Documentation page. This call returns a complete list of aspects for all of the leaf categories that belong to an eBay marketplace. The eBay marketplace is specified through the category_tree_id URI parameter. Note: This call can return a large payload, so the call returns the response as a gzipped JSON file. The open source Taxonomy SDK can be used to compare the aspect metadata that is returned in this response. The bulk download capability that this method provides, when combined with the Taxonomy SDK, brings transparency to the evolution of the metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryTreeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/commerce/taxonomy/v1");
    
    // Configure OAuth2 access token for authorization: Client Credentials
    OAuth Client Credentials = (OAuth) defaultClient.getAuthentication("Client Credentials");
    Client Credentials.setAccessToken("YOUR ACCESS TOKEN");

    CategoryTreeApi apiInstance = new CategoryTreeApi(defaultClient);
    String categoryTreeId = "categoryTreeId_example"; // String | The unique identifier of the eBay category tree being requested.
    try {
      GetCategoriesAspectResponse result = apiInstance.fetchItemAspects(categoryTreeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryTreeApi#fetchItemAspects");
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
| **categoryTreeId** | **String**| The unique identifier of the eBay category tree being requested. | |

### Return type

[**GetCategoriesAspectResponse**](GetCategoriesAspectResponse.md)

### Authorization

[Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCategorySubtree"></a>
# **getCategorySubtree**
> CategorySubtree getCategorySubtree(categoryId, categoryTreeId)

Get a Category Subtree

Note: The General Availability (GA) version of the Taxonomy API has been released. Developers currently using the Beta version should make plans to migrate to the new GA version, as the Beta version will be decommissioned on March 31, 2021. Until that date, the Beta version documentation set can be accessed through the All API Documentation page. This call retrieves the details of all nodes of the category tree hierarchy (the subtree) below a specified category of a category tree. You identify the tree using the category_tree_id parameter, which was returned by the getDefaultCategoryTreeId call in the categoryTreeId field. Note: This call can return a very large payload, so you are strongly advised to submit the request with the following HTTP header: &amp;nbsp;&amp;nbsp;Accept-Encoding: application/gzip With this header (in addition to the required headers described under HTTP Request Headers), the call returns the response with gzip compression.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryTreeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/commerce/taxonomy/v1");
    
    // Configure OAuth2 access token for authorization: Client Credentials
    OAuth Client Credentials = (OAuth) defaultClient.getAuthentication("Client Credentials");
    Client Credentials.setAccessToken("YOUR ACCESS TOKEN");

    CategoryTreeApi apiInstance = new CategoryTreeApi(defaultClient);
    String categoryId = "categoryId_example"; // String | The unique identifier of the category at the top of the subtree being requested. Note: If the category_id submitted identifies the root node of the tree, this call returns an error. To retrieve the complete tree, use this value with the getCategoryTree call. If the category_id submitted identifies a leaf node of the tree, the call response will contain information about only that leaf node, which is a valid subtree.
    String categoryTreeId = "categoryTreeId_example"; // String | The unique identifier of the eBay category tree from which a category subtree is being requested.
    try {
      CategorySubtree result = apiInstance.getCategorySubtree(categoryId, categoryTreeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryTreeApi#getCategorySubtree");
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
| **categoryId** | **String**| The unique identifier of the category at the top of the subtree being requested. Note: If the category_id submitted identifies the root node of the tree, this call returns an error. To retrieve the complete tree, use this value with the getCategoryTree call. If the category_id submitted identifies a leaf node of the tree, the call response will contain information about only that leaf node, which is a valid subtree. | |
| **categoryTreeId** | **String**| The unique identifier of the eBay category tree from which a category subtree is being requested. | |

### Return type

[**CategorySubtree**](CategorySubtree.md)

### Authorization

[Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCategorySuggestions"></a>
# **getCategorySuggestions**
> CategorySuggestionResponse getCategorySuggestions(categoryTreeId, q)

Get Suggested Categories

Note: The General Availability (GA) version of the Taxonomy API has been released. Developers currently using the Beta version should make plans to migrate to the new GA version, as the Beta version will be decommissioned on March 31, 2021. Until that date, the Beta version documentation set can be accessed through the All API Documentation page. This call returns an array of category tree leaf nodes in the specified category tree that are considered by eBay to most closely correspond to the query string q. Returned with each suggested node is a localized name for that category (based on the Accept-Language header specified for the call), and details about each of the category&#39;s ancestor nodes, extending from its immediate parent up to the root of the category tree. Note: This call can return a large payload, so you are advised to submit the request with the following HTTP header: &amp;nbsp;&amp;nbsp;Accept-Encoding: application/gzip With this header (in addition to the required headers described under HTTP Request Headers), the call returns the response with gzip compression. You identify the tree using the category_tree_id parameter, which was returned by the getDefaultCategoryTreeId call in the categoryTreeId field. Important: This call is not supported in the Sandbox environment. It will return a response payload in which the categoryName fields contain random or boilerplate text regardless of the query submitted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryTreeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/commerce/taxonomy/v1");
    
    // Configure OAuth2 access token for authorization: Client Credentials
    OAuth Client Credentials = (OAuth) defaultClient.getAuthentication("Client Credentials");
    Client Credentials.setAccessToken("YOUR ACCESS TOKEN");

    CategoryTreeApi apiInstance = new CategoryTreeApi(defaultClient);
    String categoryTreeId = "categoryTreeId_example"; // String | The unique identifier of the eBay category tree for which suggested nodes are being requested.
    String q = "q_example"; // String | A quoted string that describes or characterizes the item being offered for sale. The string format is free form, and can contain any combination of phrases or keywords. eBay will parse the string and return suggested categories for the item.
    try {
      CategorySuggestionResponse result = apiInstance.getCategorySuggestions(categoryTreeId, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryTreeApi#getCategorySuggestions");
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
| **categoryTreeId** | **String**| The unique identifier of the eBay category tree for which suggested nodes are being requested. | |
| **q** | **String**| A quoted string that describes or characterizes the item being offered for sale. The string format is free form, and can contain any combination of phrases or keywords. eBay will parse the string and return suggested categories for the item. | |

### Return type

[**CategorySuggestionResponse**](CategorySuggestionResponse.md)

### Authorization

[Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **204** | No content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCategoryTree"></a>
# **getCategoryTree**
> CategoryTree getCategoryTree(categoryTreeId)

Get a Category Tree

Note: The General Availability (GA) version of the Taxonomy API has been released. Developers currently using the Beta version should make plans to migrate to the new GA version, as the Beta version will be decommissioned on March 31, 2021. Until that date, the Beta version documentation set can be accessed through the All API Documentation page. This call retrieves the complete category tree that is identified by the category_tree_id parameter. The value of category_tree_id was returned by the getDefaultCategoryTreeId call in the categoryTreeId field. The response contains details of all nodes of the specified eBay category tree, as well as the eBay marketplaces that use this category tree. Note: This call can return a very large payload, so you are strongly advised to submit the request with the following HTTP header: &amp;nbsp;&amp;nbsp;Accept-Encoding: application/gzip With this header (in addition to the required headers described under HTTP Request Headers), the call returns the response with gzip compression.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryTreeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/commerce/taxonomy/v1");
    
    // Configure OAuth2 access token for authorization: Client Credentials
    OAuth Client Credentials = (OAuth) defaultClient.getAuthentication("Client Credentials");
    Client Credentials.setAccessToken("YOUR ACCESS TOKEN");

    CategoryTreeApi apiInstance = new CategoryTreeApi(defaultClient);
    String categoryTreeId = "categoryTreeId_example"; // String | The unique identifier of the eBay category tree being requested.
    try {
      CategoryTree result = apiInstance.getCategoryTree(categoryTreeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryTreeApi#getCategoryTree");
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
| **categoryTreeId** | **String**| The unique identifier of the eBay category tree being requested. | |

### Return type

[**CategoryTree**](CategoryTree.md)

### Authorization

[Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCompatibilityProperties"></a>
# **getCompatibilityProperties**
> GetCompatibilityMetadataResponse getCompatibilityProperties(categoryTreeId, categoryId)

Get Compatibility Properties

Note: The General Availability (GA) version of the Taxonomy API has been released. Developers currently using the Beta version should make plans to migrate to the new GA version, as the Beta version will be decommissioned on March 31, 2021. Until that date, the Beta version documentation set can be accessed through the All API Documentation page. This call retrieves the compatible vehicle aspects that are used to define a motor vehicle that is compatible with a motor vehicle part or accessory. The values that are retrieved here might include motor vehicle aspects such as &#39;Make&#39;, &#39;Model&#39;, &#39;Year&#39;, &#39;Engine&#39;, and &#39;Trim&#39;, and each of these aspects are localized for the eBay marketplace. The category_tree_id value is passed in as a path parameter, and this value identifies the eBay category tree. The category_id value is passed in as a query parameter, as this parameter is also required. The specified category must be a category that supports parts compatibility. At this time, this operation only supports parts and accessories listings for cars, trucks, and motorcycles (not boats, power sports, or any other vehicle types). Only the following eBay marketplaces support parts compatibility: eBay US (Motors and non-Motors categories) eBay Canada (Motors and non-Motors categories) eBay UK eBay Germany eBay Australia eBay France eBay Italy eBay Spain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryTreeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/commerce/taxonomy/v1");
    
    // Configure OAuth2 access token for authorization: Client Credentials
    OAuth Client Credentials = (OAuth) defaultClient.getAuthentication("Client Credentials");
    Client Credentials.setAccessToken("YOUR ACCESS TOKEN");

    CategoryTreeApi apiInstance = new CategoryTreeApi(defaultClient);
    String categoryTreeId = "categoryTreeId_example"; // String | This is the unique identifier of category tree. The following is the list of category_tree_id values and the eBay marketplaces that they represent. One of these ID values must be passed in as a path parameter, and the category_id value, that is passed in as query parameter, must be a valid eBay category on that eBay marketplace that supports parts compatibility for cars, trucks, or motorcyles. eBay US: 0 eBay Motors US: 100 eBay Canada: 2 eBay UK: 3 eBay Germany: 77 eBay Australia: 15 eBay France: 71 eBay Italy: 101 eBay Spain: 186
    String categoryId = "categoryId_example"; // String | The unique identifier of an eBay category. This eBay category must be a valid eBay category on the specified eBay marketplace, and the category must support parts compatibility for cars, trucks, or motorcyles. The getAutomotivePartsCompatibilityPolicies method of the Selling Metadata API can be used to retrieve all eBay categories for an eBay marketplace that supports parts compatibility cars, trucks, or motorcyles. The getAutomotivePartsCompatibilityPolicies method can also be used to see if one or more specific eBay categories support parts compatibility.
    try {
      GetCompatibilityMetadataResponse result = apiInstance.getCompatibilityProperties(categoryTreeId, categoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryTreeApi#getCompatibilityProperties");
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
| **categoryTreeId** | **String**| This is the unique identifier of category tree. The following is the list of category_tree_id values and the eBay marketplaces that they represent. One of these ID values must be passed in as a path parameter, and the category_id value, that is passed in as query parameter, must be a valid eBay category on that eBay marketplace that supports parts compatibility for cars, trucks, or motorcyles. eBay US: 0 eBay Motors US: 100 eBay Canada: 2 eBay UK: 3 eBay Germany: 77 eBay Australia: 15 eBay France: 71 eBay Italy: 101 eBay Spain: 186 | |
| **categoryId** | **String**| The unique identifier of an eBay category. This eBay category must be a valid eBay category on the specified eBay marketplace, and the category must support parts compatibility for cars, trucks, or motorcyles. The getAutomotivePartsCompatibilityPolicies method of the Selling Metadata API can be used to retrieve all eBay categories for an eBay marketplace that supports parts compatibility cars, trucks, or motorcyles. The getAutomotivePartsCompatibilityPolicies method can also be used to see if one or more specific eBay categories support parts compatibility. | |

### Return type

[**GetCompatibilityMetadataResponse**](GetCompatibilityMetadataResponse.md)

### Authorization

[Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **204** | No content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCompatibilityPropertyValues"></a>
# **getCompatibilityPropertyValues**
> GetCompatibilityPropertyValuesResponse getCompatibilityPropertyValues(categoryTreeId, compatibilityProperty, categoryId, filter)

Get Compatibility Property Values

Note: The General Availability (GA) version of the Taxonomy API has been released. Developers currently using the Beta version should make plans to migrate to the new GA version, as the Beta version will be decommissioned on March 31, 2021. Until that date, the Beta version documentation set can be accessed through the All API Documentation page. This call retrieves applicable compatible vehicle property values based on the specified eBay marketplace, specified eBay category, and filters used in the request. Compatible vehicle properties are returned in the compatibilityProperties.name field of a getCompatibilityProperties response. One compatible vehicle property applicable to the specified eBay marketplace and eBay category is specified through the required compatibility_property filter. Then, the user has the option of further restricting the compatible vehicle property values that are returned in the response by specifying one or more compatible vehicle property name/value pairs through the filter query parameter. See the documentation in URI parameters section for more information on using the compatibility_property and filter query parameters together to customize the data that is retrieved.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryTreeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/commerce/taxonomy/v1");
    
    // Configure OAuth2 access token for authorization: Client Credentials
    OAuth Client Credentials = (OAuth) defaultClient.getAuthentication("Client Credentials");
    Client Credentials.setAccessToken("YOUR ACCESS TOKEN");

    CategoryTreeApi apiInstance = new CategoryTreeApi(defaultClient);
    String categoryTreeId = "categoryTreeId_example"; // String | This is the unique identifier of the category tree. The following is the list of category_tree_id values and the eBay marketplaces that they represent. One of these ID values must be passed in as a path parameter, and the category_id value, that is passed in as query parameter, must be a valid eBay category on that eBay marketplace that supports parts compatibility for cars, trucks, or motorcyles. eBay US: 0 eBay Motors US: 100 eBay Canada: 2 eBay UK: 3 eBay Germany: 77 eBay Australia: 15 eBay France: 71 eBay Italy: 101 eBay Spain: 186
    String compatibilityProperty = "compatibilityProperty_example"; // String | One compatible vehicle property applicable to the specified eBay marketplace and eBay category is specified in this required filter. Compatible vehicle properties are returned in the compatibilityProperties.name field of a getCompatibilityProperties response. For example, if you wanted to retrieve all vehicle trims for a 2018 Toyota Camry, you would set this filter as follows: compatibility_property=Trim; and then include the following three name/value filters through one filter parameter: filter=Year:2018,Make:Toyota,Model:Camry. So, putting this all together, your URI would look something like this: GET https://api.ebay.com/commerce/ taxonomy/v1/category_tree/100/ get_compatibility_property_values? category_id=6016&amp;compatibility_property=Trim &amp;filter=filter=Year:2018,Make:Toyota,Model:Camry
    String categoryId = "categoryId_example"; // String | The unique identifier of an eBay category. This eBay category must be a valid eBay category on the specified eBay marketplace, and the category must support parts compatibility for cars, trucks, or motorcyles. The getAutomotivePartsCompatibilityPolicies method of the Selling Metadata API can be used to retrieve all eBay categories for an eBay marketplace that supports parts compatibility cars, trucks, or motorcyles. The getAutomotivePartsCompatibilityPolicies method can also be used to see if one or more specific eBay categories support parts compatibility.
    String filter = "filter_example"; // String | One or more compatible vehicle property name/value pairs are passed in through this query parameter. The compatible vehicle property name and corresponding value are delimited with a colon (:), such as filter=Year:2018, and multiple compatible vehicle property name/value pairs are delimited with a comma (,). For example, if you wanted to retrieve all vehicle trims for a 2018 Toyota Camry, you would set the compatibility_property filter as follows: compatibility_property=Trim; and then include the following three name/value filters through one filter parameter: filter=Year:2018,Make:Toyota,Model:Camry. So, putting this all together, your URI would look something like this: GET https://api.ebay.com/commerce/ taxonomy/v1/category_tree/100/ get_compatibility_property_values? category_id=6016&amp;compatibility_property=Trim &amp;filter=filter=Year:2018,Make:Toyota,Model:Camry For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/commerce/taxonomy/types/txn:ConstraintFilter
    try {
      GetCompatibilityPropertyValuesResponse result = apiInstance.getCompatibilityPropertyValues(categoryTreeId, compatibilityProperty, categoryId, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryTreeApi#getCompatibilityPropertyValues");
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
| **categoryTreeId** | **String**| This is the unique identifier of the category tree. The following is the list of category_tree_id values and the eBay marketplaces that they represent. One of these ID values must be passed in as a path parameter, and the category_id value, that is passed in as query parameter, must be a valid eBay category on that eBay marketplace that supports parts compatibility for cars, trucks, or motorcyles. eBay US: 0 eBay Motors US: 100 eBay Canada: 2 eBay UK: 3 eBay Germany: 77 eBay Australia: 15 eBay France: 71 eBay Italy: 101 eBay Spain: 186 | |
| **compatibilityProperty** | **String**| One compatible vehicle property applicable to the specified eBay marketplace and eBay category is specified in this required filter. Compatible vehicle properties are returned in the compatibilityProperties.name field of a getCompatibilityProperties response. For example, if you wanted to retrieve all vehicle trims for a 2018 Toyota Camry, you would set this filter as follows: compatibility_property&#x3D;Trim; and then include the following three name/value filters through one filter parameter: filter&#x3D;Year:2018,Make:Toyota,Model:Camry. So, putting this all together, your URI would look something like this: GET https://api.ebay.com/commerce/ taxonomy/v1/category_tree/100/ get_compatibility_property_values? category_id&#x3D;6016&amp;amp;compatibility_property&#x3D;Trim &amp;amp;filter&#x3D;filter&#x3D;Year:2018,Make:Toyota,Model:Camry | |
| **categoryId** | **String**| The unique identifier of an eBay category. This eBay category must be a valid eBay category on the specified eBay marketplace, and the category must support parts compatibility for cars, trucks, or motorcyles. The getAutomotivePartsCompatibilityPolicies method of the Selling Metadata API can be used to retrieve all eBay categories for an eBay marketplace that supports parts compatibility cars, trucks, or motorcyles. The getAutomotivePartsCompatibilityPolicies method can also be used to see if one or more specific eBay categories support parts compatibility. | |
| **filter** | **String**| One or more compatible vehicle property name/value pairs are passed in through this query parameter. The compatible vehicle property name and corresponding value are delimited with a colon (:), such as filter&#x3D;Year:2018, and multiple compatible vehicle property name/value pairs are delimited with a comma (,). For example, if you wanted to retrieve all vehicle trims for a 2018 Toyota Camry, you would set the compatibility_property filter as follows: compatibility_property&#x3D;Trim; and then include the following three name/value filters through one filter parameter: filter&#x3D;Year:2018,Make:Toyota,Model:Camry. So, putting this all together, your URI would look something like this: GET https://api.ebay.com/commerce/ taxonomy/v1/category_tree/100/ get_compatibility_property_values? category_id&#x3D;6016&amp;amp;compatibility_property&#x3D;Trim &amp;amp;filter&#x3D;filter&#x3D;Year:2018,Make:Toyota,Model:Camry For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/commerce/taxonomy/types/txn:ConstraintFilter | [optional] |

### Return type

[**GetCompatibilityPropertyValuesResponse**](GetCompatibilityPropertyValuesResponse.md)

### Authorization

[Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **204** | No content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getDefaultCategoryTreeId"></a>
# **getDefaultCategoryTreeId**
> BaseCategoryTree getDefaultCategoryTreeId(marketplaceId, acceptLanguage)

Get a Default Category Tree ID

Note: The General Availability (GA) version of the Taxonomy API has been released. Developers currently using the Beta version should make plans to migrate to the new GA version, as the Beta version will be decommissioned on March 31, 2021. Until that date, the Beta version documentation set can be accessed through the All API Documentation page. A given eBay marketplace might use multiple category trees, but one of those trees is considered to be the default for that marketplace. This call retrieves a reference to the default category tree associated with the specified eBay marketplace ID. The response includes only the tree&#39;s unique identifier and version, which you can use to retrieve more details about the tree, its structure, and its individual category nodes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryTreeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/commerce/taxonomy/v1");
    
    // Configure OAuth2 access token for authorization: Client Credentials
    OAuth Client Credentials = (OAuth) defaultClient.getAuthentication("Client Credentials");
    Client Credentials.setAccessToken("YOUR ACCESS TOKEN");

    CategoryTreeApi apiInstance = new CategoryTreeApi(defaultClient);
    String marketplaceId = "marketplaceId_example"; // String | The ID of the eBay marketplace for which the category tree ID is being requested. For a list of supported marketplace IDs, see Marketplaces with Default Category Trees.
    String acceptLanguage = "acceptLanguage_example"; // String | A header used to indicate the natural language the seller prefers for the response. This specifies the language that the seller wants to use when the field values provided in the request body are displayed to consumers. Note: For details, see Accept-Language in HTTP request headers. Valid Values: For EBAY_CA in French: Accept-Language: fr-CA For EBAY_BE in French: Accept-Language: fr-BE
    try {
      BaseCategoryTree result = apiInstance.getDefaultCategoryTreeId(marketplaceId, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryTreeApi#getDefaultCategoryTreeId");
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
| **marketplaceId** | **String**| The ID of the eBay marketplace for which the category tree ID is being requested. For a list of supported marketplace IDs, see Marketplaces with Default Category Trees. | |
| **acceptLanguage** | **String**| A header used to indicate the natural language the seller prefers for the response. This specifies the language that the seller wants to use when the field values provided in the request body are displayed to consumers. Note: For details, see Accept-Language in HTTP request headers. Valid Values: For EBAY_CA in French: Accept-Language: fr-CA For EBAY_BE in French: Accept-Language: fr-BE | [optional] |

### Return type

[**BaseCategoryTree**](BaseCategoryTree.md)

### Authorization

[Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **204** | No content |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="getItemAspectsForCategory"></a>
# **getItemAspectsForCategory**
> AspectMetadata getItemAspectsForCategory(categoryId, categoryTreeId)



Note: The General Availability (GA) version of the Taxonomy API has been released. Developers currently using the Beta version should make plans to migrate to the new GA version, as the Beta version will be decommissioned on March 31, 2021. Until that date, the Beta version documentation set can be accessed through the All API Documentation page. This call returns a list of aspects that are appropriate or necessary for accurately describing items in the specified leaf category. Each aspect identifies an item attribute (for example, color) for which the seller will be required or encouraged to provide a value (or variation values) when offering an item in that category on eBay. For each aspect, getItemAspectsForCategory provides complete metadata, including: The aspect&#39;s data type, format, and entry mode Whether the aspect is required in listings Whether the aspect can be used for item variations Whether the aspect accepts multiple values for an item Allowed values for the aspect Use this information to construct an interface through which sellers can enter or select the appropriate values for their items or item variations. Once you collect those values, include them as product aspects when creating inventory items using the Inventory API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryTreeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/commerce/taxonomy/v1");
    
    // Configure OAuth2 access token for authorization: Client Credentials
    OAuth Client Credentials = (OAuth) defaultClient.getAuthentication("Client Credentials");
    Client Credentials.setAccessToken("YOUR ACCESS TOKEN");

    CategoryTreeApi apiInstance = new CategoryTreeApi(defaultClient);
    String categoryId = "categoryId_example"; // String | The unique identifier of the leaf category for which aspects are being requested. Note: If the category_id submitted does not identify a leaf node of the tree, this call returns an error.
    String categoryTreeId = "categoryTreeId_example"; // String | The unique identifier of the eBay category tree from which the specified category's aspects are being requested.
    try {
      AspectMetadata result = apiInstance.getItemAspectsForCategory(categoryId, categoryTreeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryTreeApi#getItemAspectsForCategory");
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
| **categoryId** | **String**| The unique identifier of the leaf category for which aspects are being requested. Note: If the category_id submitted does not identify a leaf node of the tree, this call returns an error. | |
| **categoryTreeId** | **String**| The unique identifier of the eBay category tree from which the specified category&#39;s aspects are being requested. | |

### Return type

[**AspectMetadata**](AspectMetadata.md)

### Authorization

[Client Credentials](../README.md#Client Credentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

