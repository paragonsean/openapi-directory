# PackageApi

All URIs are relative to *https://tl-api.azurewebsites.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**packageDelete**](PackageApi.md#packageDelete) | **DELETE** /api/Package | Delete existing package              |
| [**packageGet**](PackageApi.md#packageGet) | **GET** /api/Package | Get package details by packageId              |
| [**packagePost**](PackageApi.md#packagePost) | **POST** /api/Package | Insert new package into the system              |
| [**packagePut**](PackageApi.md#packagePut) | **PUT** /api/Package | Update existing package by its ID              |
| [**packageSearch**](PackageApi.md#packageSearch) | **GET** /api/Package/Search | Search packages              |
| [**packageUpdateStatus**](PackageApi.md#packageUpdateStatus) | **PUT** /api/Package/UpdateStatus | Status update of existing package  |


<a id="packageDelete"></a>
# **packageDelete**
> DefaultResponseDTOOfBoolean packageDelete(packageId)

Delete existing package             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    PackageApi apiInstance = new PackageApi(defaultClient);
    Integer packageId = 56; // Integer | primary key of package entity
    try {
      DefaultResponseDTOOfBoolean result = apiInstance.packageDelete(packageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageApi#packageDelete");
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
| **packageId** | **Integer**| primary key of package entity | [optional] |

### Return type

[**DefaultResponseDTOOfBoolean**](DefaultResponseDTOOfBoolean.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | status 1  : success, status 404 : package not found, status -2: package already in use  |  -  |
| **400** |  |  -  |
| **404** |  |  -  |
| **500** |  |  -  |

<a id="packageGet"></a>
# **packageGet**
> DefaultResponseDTOOfPackageDTO packageGet(packageId)

Get package details by packageId             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    PackageApi apiInstance = new PackageApi(defaultClient);
    Integer packageId = 56; // Integer | primary key of package entity
    try {
      DefaultResponseDTOOfPackageDTO result = apiInstance.packageGet(packageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageApi#packageGet");
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
| **packageId** | **Integer**| primary key of package entity | [optional] |

### Return type

[**DefaultResponseDTOOfPackageDTO**](DefaultResponseDTOOfPackageDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | all the fields that related to the package |  -  |
| **404** |  |  -  |
| **500** |  |  -  |

<a id="packagePost"></a>
# **packagePost**
> DefaultResponseDTOOfStatusDTO packagePost(packageDTO)

Insert new package into the system             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    PackageApi apiInstance = new PackageApi(defaultClient);
    PackageDTO packageDTO = new PackageDTO(); // PackageDTO | package object
    try {
      DefaultResponseDTOOfStatusDTO result = apiInstance.packagePost(packageDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageApi#packagePost");
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
| **packageDTO** | [**PackageDTO**](PackageDTO.md)| package object | |

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

<a id="packagePut"></a>
# **packagePut**
> DefaultResponseDTOOfStatusDTO packagePut(packageDTO)

Update existing package by its ID             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    PackageApi apiInstance = new PackageApi(defaultClient);
    PackageDTO packageDTO = new PackageDTO(); // PackageDTO | package object
    try {
      DefaultResponseDTOOfStatusDTO result = apiInstance.packagePut(packageDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageApi#packagePut");
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
| **packageDTO** | [**PackageDTO**](PackageDTO.md)| package object | |

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

<a id="packageSearch"></a>
# **packageSearch**
> List&lt;DefaultResponseDTOOfPackageSearchDTO&gt; packageSearch(searchText, gymId, type, orderBy, limit, offset, activeStatus, categoryId, startpPrice, endPrice, requestSource)

Search packages             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    PackageApi apiInstance = new PackageApi(defaultClient);
    String searchText = "searchText_example"; // String | part of package name
    Integer gymId = -1; // Integer | primary key of TL gym entity
    String type = "all"; // String | filter package type.!-- default is 'all'
    String orderBy = "1"; // String | order by column.!-- invalid column will give internal server error
    Integer limit = 100; // Integer | number of recode in result and default is 100. use negative numbers to order by desc
    Integer offset = 0; // Integer | number of recodes to skip
    Integer activeStatus = 1; // Integer | active status active : 1, inactive : 2, all 3, deafult : 1
    Integer categoryId = -1; // Integer | Packge Category Id
    BigDecimal startpPrice = new BigDecimal("0"); // BigDecimal | Start price of the price Range
    BigDecimal endPrice = new BigDecimal("9999999"); // BigDecimal | End Price of the price Range
    Integer requestSource = 1; // Integer | 1 : MRM, 2 : Mobile 
    try {
      List<DefaultResponseDTOOfPackageSearchDTO> result = apiInstance.packageSearch(searchText, gymId, type, orderBy, limit, offset, activeStatus, categoryId, startpPrice, endPrice, requestSource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageApi#packageSearch");
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
| **searchText** | **String**| part of package name | [optional] |
| **gymId** | **Integer**| primary key of TL gym entity | [optional] [default to -1] |
| **type** | **String**| filter package type.!-- default is &#39;all&#39; | [optional] [default to all] |
| **orderBy** | **String**| order by column.!-- invalid column will give internal server error | [optional] [default to 1] |
| **limit** | **Integer**| number of recode in result and default is 100. use negative numbers to order by desc | [optional] [default to 100] |
| **offset** | **Integer**| number of recodes to skip | [optional] [default to 0] |
| **activeStatus** | **Integer**| active status active : 1, inactive : 2, all 3, deafult : 1 | [optional] [default to 1] |
| **categoryId** | **Integer**| Packge Category Id | [optional] [default to -1] |
| **startpPrice** | **BigDecimal**| Start price of the price Range | [optional] [default to 0] |
| **endPrice** | **BigDecimal**| End Price of the price Range | [optional] [default to 9999999] |
| **requestSource** | **Integer**| 1 : MRM, 2 : Mobile  | [optional] [default to 1] |

### Return type

[**List&lt;DefaultResponseDTOOfPackageSearchDTO&gt;**](DefaultResponseDTOOfPackageSearchDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | basic information of package entity |  -  |
| **404** |  |  -  |
| **500** |  |  -  |

<a id="packageUpdateStatus"></a>
# **packageUpdateStatus**
> DefaultResponseDTOOfBoolean packageUpdateStatus(packageId, status, userName)

Status update of existing package 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    PackageApi apiInstance = new PackageApi(defaultClient);
    Integer packageId = 56; // Integer | package Id
    Integer status = 1; // Integer | status : 1 activate, 2 : deactivate
    String userName = "system"; // String | Status updated User
    try {
      DefaultResponseDTOOfBoolean result = apiInstance.packageUpdateStatus(packageId, status, userName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageApi#packageUpdateStatus");
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
| **packageId** | **Integer**| package Id | [optional] |
| **status** | **Integer**| status : 1 activate, 2 : deactivate | [optional] [default to 1] |
| **userName** | **String**| Status updated User | [optional] [default to system] |

### Return type

[**DefaultResponseDTOOfBoolean**](DefaultResponseDTOOfBoolean.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | status 1 : success, status 404 : package not found, status -2: package already in use  |  -  |
| **400** |  |  -  |
| **404** |  |  -  |
| **500** |  |  -  |

