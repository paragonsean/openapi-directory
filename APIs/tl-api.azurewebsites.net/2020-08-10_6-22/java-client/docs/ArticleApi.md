# ArticleApi

All URIs are relative to *https://tl-api.azurewebsites.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**articleAddMeasureUnit**](ArticleApi.md#articleAddMeasureUnit) | **POST** /api/Article/MeasureUnit | Add measure unit |
| [**articleDelete**](ArticleApi.md#articleDelete) | **DELETE** /api/Article | Delete article from the system              |
| [**articleGet**](ArticleApi.md#articleGet) | **GET** /api/Article/{articleID} | Get article details This will return all properties related to article entity              |
| [**articleGetAddons**](ArticleApi.md#articleGetAddons) | **GET** /api/Article/GetAddons |  |
| [**articleGetMeasureUnits**](ArticleApi.md#articleGetMeasureUnits) | **GET** /api/Article/MeasureUnits | Get mesure units |
| [**articleGetRevenueAccounts**](ArticleApi.md#articleGetRevenueAccounts) | **GET** /api/Article/RevenueAccounts | Get Revenue Accounts  |
| [**articleGymArticleDetails**](ArticleApi.md#articleGymArticleDetails) | **GET** /api/Article/GymArticle/{articleId}/{gymId} | Get Gym specific properties for article              |
| [**articlePost**](ArticleApi.md#articlePost) | **POST** /api/Article | Add new article              |
| [**articlePut**](ArticleApi.md#articlePut) | **PUT** /api/Article | update existing article              |
| [**articleSearch**](ArticleApi.md#articleSearch) | **GET** /api/Article/Search | Search articles It will only return basic information of article              |
| [**articleUpdateArticleGymDetails**](ArticleApi.md#articleUpdateArticleGymDetails) | **PUT** /api/Article/ArticleGymDetails | Add article details that associate with a Gym              |
| [**articleUpdateStatus**](ArticleApi.md#articleUpdateStatus) | **PUT** /api/Article/UpdateStatus | Deactivate existing article  |


<a id="articleAddMeasureUnit"></a>
# **articleAddMeasureUnit**
> DefaultResponseDTOOfStatusDTO articleAddMeasureUnit(measureUnitDTO)

Add measure unit

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    ArticleApi apiInstance = new ArticleApi(defaultClient);
    List<MeasureUnitDTO> measureUnitDTO = Arrays.asList(); // List<MeasureUnitDTO> | list of measureUnit
    try {
      DefaultResponseDTOOfStatusDTO result = apiInstance.articleAddMeasureUnit(measureUnitDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticleApi#articleAddMeasureUnit");
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
| **measureUnitDTO** | [**List&lt;MeasureUnitDTO&gt;**](MeasureUnitDTO.md)| list of measureUnit | |

### Return type

[**DefaultResponseDTOOfStatusDTO**](DefaultResponseDTOOfStatusDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** |  |  -  |
| **500** |  |  -  |

<a id="articleDelete"></a>
# **articleDelete**
> DefaultResponseDTOOfInteger articleDelete(articleId)

Delete article from the system             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    ArticleApi apiInstance = new ArticleApi(defaultClient);
    Integer articleId = 56; // Integer | indentity number(primary key) for article object
    try {
      DefaultResponseDTOOfInteger result = apiInstance.articleDelete(articleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticleApi#articleDelete");
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
| **articleId** | **Integer**| indentity number(primary key) for article object | [optional] |

### Return type

[**DefaultResponseDTOOfInteger**](DefaultResponseDTOOfInteger.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | operation was success(true) or fail(false)  |  -  |
| **404** |  |  -  |
| **500** |  |  -  |

<a id="articleGet"></a>
# **articleGet**
> DefaultResponseDTOOfArticleDTO articleGet(articleID)

Get article details This will return all properties related to article entity             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    ArticleApi apiInstance = new ArticleApi(defaultClient);
    Integer articleID = 56; // Integer | indentity number (primary key) for article object
    try {
      DefaultResponseDTOOfArticleDTO result = apiInstance.articleGet(articleID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticleApi#articleGet");
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
| **articleID** | **Integer**| indentity number (primary key) for article object | |

### Return type

[**DefaultResponseDTOOfArticleDTO**](DefaultResponseDTOOfArticleDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | API Response with Article entity |  -  |
| **404** |  |  -  |

<a id="articleGetAddons"></a>
# **articleGetAddons**
> DefaultResponseDTOOfListOfArticleSearchDTO articleGetAddons(searchText, gymIds, type, limit, offset)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    ArticleApi apiInstance = new ArticleApi(defaultClient);
    String searchText = "searchText_example"; // String | Search text - will be search by the name
    String gymIds = "-1"; // String | Comma separated gymIds deafult \"-1\" for all gyms
    String type = "all"; // String | 
    Integer limit = 100; // Integer | 
    Integer offset = 0; // Integer | 
    try {
      DefaultResponseDTOOfListOfArticleSearchDTO result = apiInstance.articleGetAddons(searchText, gymIds, type, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticleApi#articleGetAddons");
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
| **searchText** | **String**| Search text - will be search by the name | [optional] |
| **gymIds** | **String**| Comma separated gymIds deafult \&quot;-1\&quot; for all gyms | [optional] [default to -1] |
| **type** | **String**|  | [optional] [default to all] |
| **limit** | **Integer**|  | [optional] [default to 100] |
| **offset** | **Integer**|  | [optional] [default to 0] |

### Return type

[**DefaultResponseDTOOfListOfArticleSearchDTO**](DefaultResponseDTOOfListOfArticleSearchDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** |  |  -  |
| **500** |  |  -  |

<a id="articleGetMeasureUnits"></a>
# **articleGetMeasureUnits**
> DefaultResponseDTOOfStatusDTO articleGetMeasureUnits(type)

Get mesure units

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    ArticleApi apiInstance = new ArticleApi(defaultClient);
    String type = "type_example"; // String | type of the measure unit (all, item, service)
    try {
      DefaultResponseDTOOfStatusDTO result = apiInstance.articleGetMeasureUnits(type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticleApi#articleGetMeasureUnits");
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
| **type** | **String**| type of the measure unit (all, item, service) | [optional] |

### Return type

[**DefaultResponseDTOOfStatusDTO**](DefaultResponseDTOOfStatusDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** |  |  -  |
| **500** |  |  -  |

<a id="articleGetRevenueAccounts"></a>
# **articleGetRevenueAccounts**
> DefaultResponseDTOOfStatusDTO articleGetRevenueAccounts()

Get Revenue Accounts 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    ArticleApi apiInstance = new ArticleApi(defaultClient);
    try {
      DefaultResponseDTOOfStatusDTO result = apiInstance.articleGetRevenueAccounts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticleApi#articleGetRevenueAccounts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DefaultResponseDTOOfStatusDTO**](DefaultResponseDTOOfStatusDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** |  |  -  |
| **500** |  |  -  |

<a id="articleGymArticleDetails"></a>
# **articleGymArticleDetails**
> GymArticleDetailsDTO articleGymArticleDetails(articleId, gymId)

Get Gym specific properties for article             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    ArticleApi apiInstance = new ArticleApi(defaultClient);
    Integer articleId = 56; // Integer | indentity number(primary key) for article object
    Integer gymId = 56; // Integer | indentity number(primary key) for gym object
    try {
      GymArticleDetailsDTO result = apiInstance.articleGymArticleDetails(articleId, gymId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticleApi#articleGymArticleDetails");
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
| **articleId** | **Integer**| indentity number(primary key) for article object | |
| **gymId** | **Integer**| indentity number(primary key) for gym object | |

### Return type

[**GymArticleDetailsDTO**](GymArticleDetailsDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | API Response with Article entity |  -  |
| **404** |  |  -  |
| **500** |  |  -  |

<a id="articlePost"></a>
# **articlePost**
> DefaultResponseDTOOfStatusDTO articlePost(articleDTO)

Add new article             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    ArticleApi apiInstance = new ArticleApi(defaultClient);
    ArticleDTO articleDTO = new ArticleDTO(); // ArticleDTO | article object
    try {
      DefaultResponseDTOOfStatusDTO result = apiInstance.articlePost(articleDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticleApi#articlePost");
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
| **articleDTO** | [**ArticleDTO**](ArticleDTO.md)| article object | |

### Return type

[**DefaultResponseDTOOfStatusDTO**](DefaultResponseDTOOfStatusDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | messageId that can use to get the status of import later on.! |  -  |
| **500** |  |  -  |

<a id="articlePut"></a>
# **articlePut**
> DefaultResponseDTOOfStatusDTO articlePut(articleDTO)

update existing article             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    ArticleApi apiInstance = new ArticleApi(defaultClient);
    ArticleDTO articleDTO = new ArticleDTO(); // ArticleDTO | article object
    try {
      DefaultResponseDTOOfStatusDTO result = apiInstance.articlePut(articleDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticleApi#articlePut");
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
| **articleDTO** | [**ArticleDTO**](ArticleDTO.md)| article object | |

### Return type

[**DefaultResponseDTOOfStatusDTO**](DefaultResponseDTOOfStatusDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | messageId that can use to get the status of import later on.! |  -  |
| **500** |  |  -  |

<a id="articleSearch"></a>
# **articleSearch**
> DefaultResponseDTOOfListOfArticleSearchDTO articleSearch(searchText, gymId, type, orderBy, limit, offset, activeStatus)

Search articles It will only return basic information of article             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    ArticleApi apiInstance = new ArticleApi(defaultClient);
    String searchText = "searchText_example"; // String | part of article name
    Integer gymId = -1; // Integer | -1 for all gyms 
    String type = "all"; // String | filter article type. default is 'all'
    String orderBy = "1"; // String | order by column.!-- invalid column will give internal server error
    Integer limit = 100; // Integer | number of recode in result and default is 100. use negative numbers to order by desc
    Integer offset = 0; // Integer | number of recodes to skip
    Integer activeStatus = 1; // Integer | Active Status 1 : Active, 2: Inactive, 3: All, Default : 1
    try {
      DefaultResponseDTOOfListOfArticleSearchDTO result = apiInstance.articleSearch(searchText, gymId, type, orderBy, limit, offset, activeStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticleApi#articleSearch");
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
| **searchText** | **String**| part of article name | [optional] |
| **gymId** | **Integer**| -1 for all gyms  | [optional] [default to -1] |
| **type** | **String**| filter article type. default is &#39;all&#39; | [optional] [default to all] |
| **orderBy** | **String**| order by column.!-- invalid column will give internal server error | [optional] [default to 1] |
| **limit** | **Integer**| number of recode in result and default is 100. use negative numbers to order by desc | [optional] [default to 100] |
| **offset** | **Integer**| number of recodes to skip | [optional] [default to 0] |
| **activeStatus** | **Integer**| Active Status 1 : Active, 2: Inactive, 3: All, Default : 1 | [optional] [default to 1] |

### Return type

[**DefaultResponseDTOOfListOfArticleSearchDTO**](DefaultResponseDTOOfListOfArticleSearchDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | API Response with set of a Article entities |  -  |
| **404** |  |  -  |
| **500** |  |  -  |

<a id="articleUpdateArticleGymDetails"></a>
# **articleUpdateArticleGymDetails**
> DefaultResponseDTOOfStatusDTO articleUpdateArticleGymDetails(gymArticleDetailsDTO)

Add article details that associate with a Gym             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    ArticleApi apiInstance = new ArticleApi(defaultClient);
    List<GymArticleDetailsDTO> gymArticleDetailsDTO = Arrays.asList(); // List<GymArticleDetailsDTO> | 
    try {
      DefaultResponseDTOOfStatusDTO result = apiInstance.articleUpdateArticleGymDetails(gymArticleDetailsDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticleApi#articleUpdateArticleGymDetails");
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
| **gymArticleDetailsDTO** | [**List&lt;GymArticleDetailsDTO&gt;**](GymArticleDetailsDTO.md)|  | |

### Return type

[**DefaultResponseDTOOfStatusDTO**](DefaultResponseDTOOfStatusDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | messageId that can use to get the status of import later on.! |  -  |
| **500** |  |  -  |

<a id="articleUpdateStatus"></a>
# **articleUpdateStatus**
> DefaultResponseDTOOfInteger articleUpdateStatus(articleId, status, userName)

Deactivate existing article 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    ArticleApi apiInstance = new ArticleApi(defaultClient);
    Integer articleId = 56; // Integer | 
    Integer status = 56; // Integer | 1 : activate , 2 deactivate
    String userName = "userName_example"; // String | Updating user
    try {
      DefaultResponseDTOOfInteger result = apiInstance.articleUpdateStatus(articleId, status, userName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticleApi#articleUpdateStatus");
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
| **articleId** | **Integer**|  | [optional] |
| **status** | **Integer**| 1 : activate , 2 deactivate | [optional] |
| **userName** | **String**| Updating user | [optional] |

### Return type

[**DefaultResponseDTOOfInteger**](DefaultResponseDTOOfInteger.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** |  |  -  |
| **500** |  |  -  |

