# UserApi

All URIs are relative to *https://tl-api.azurewebsites.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userGet**](UserApi.md#userGet) | **GET** /api/User | Get all Users detail This will return all properties related to User entity              |
| [**userRegisterUser**](UserApi.md#userRegisterUser) | **POST** /api/User/registerUser | Register a new User              |
| [**userUpdateUser**](UserApi.md#userUpdateUser) | **PUT** /api/User/updateuser | Update an exsisting User              |


<a id="userGet"></a>
# **userGet**
> UserDTO userGet()

Get all Users detail This will return all properties related to User entity             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    UserApi apiInstance = new UserApi(defaultClient);
    try {
      UserDTO result = apiInstance.userGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userGet");
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

[**UserDTO**](UserDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | API Response with User entity |  -  |

<a id="userRegisterUser"></a>
# **userRegisterUser**
> userRegisterUser(userId, accountNumber, gymNumber, externalEntityNumber, name, number, introduceBy, guardian, typeId)

Register a new User             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    UserApi apiInstance = new UserApi(defaultClient);
    Integer userId = 56; // Integer | Indentity number(primary key) for user object. Generated in DB table when inserting a record.             
    String accountNumber = "accountNumber_example"; // String | Account number of the user.It can be any stakeholder of the application.even can be a gym.             
    String gymNumber = "gymNumber_example"; // String | If this user is a gym, then the gym number.             
    String externalEntityNumber = "externalEntityNumber_example"; // String | Entity number that make a relationship with BOX API DB.             
    String name = "name_example"; // String | Name of the user.             
    String number = "number_example"; // String | Unique number maintain by application to idenify user.             
    Integer introduceBy = 56; // Integer | If Someone introduced this user to the system, then that user's UserId.             
    Integer guardian = 56; // Integer | Gaurdian of the this user if he/she is under 18 years old.             
    Integer typeId = 56; // Integer | Type of the user.             
    try {
      apiInstance.userRegisterUser(userId, accountNumber, gymNumber, externalEntityNumber, name, number, introduceBy, guardian, typeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userRegisterUser");
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
| **userId** | **Integer**| Indentity number(primary key) for user object. Generated in DB table when inserting a record.              | [optional] |
| **accountNumber** | **String**| Account number of the user.It can be any stakeholder of the application.even can be a gym.              | [optional] |
| **gymNumber** | **String**| If this user is a gym, then the gym number.              | [optional] |
| **externalEntityNumber** | **String**| Entity number that make a relationship with BOX API DB.              | [optional] |
| **name** | **String**| Name of the user.              | [optional] |
| **number** | **String**| Unique number maintain by application to idenify user.              | [optional] |
| **introduceBy** | **Integer**| If Someone introduced this user to the system, then that user&#39;s UserId.              | [optional] |
| **guardian** | **Integer**| Gaurdian of the this user if he/she is under 18 years old.              | [optional] |
| **typeId** | **Integer**| Type of the user.              | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | API Response |  -  |
| **404** |  |  -  |

<a id="userUpdateUser"></a>
# **userUpdateUser**
> userUpdateUser(userId, accountNumber, gymNumber, externalEntityNumber, name, number, introduceBy, guardian, typeId)

Update an exsisting User             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    UserApi apiInstance = new UserApi(defaultClient);
    Integer userId = 56; // Integer | Indentity number(primary key) for user object. Generated in DB table when inserting a record.             
    String accountNumber = "accountNumber_example"; // String | Account number of the user.It can be any stakeholder of the application.even can be a gym.             
    String gymNumber = "gymNumber_example"; // String | If this user is a gym, then the gym number.             
    String externalEntityNumber = "externalEntityNumber_example"; // String | Entity number that make a relationship with BOX API DB.             
    String name = "name_example"; // String | Name of the user.             
    String number = "number_example"; // String | Unique number maintain by application to idenify user.             
    Integer introduceBy = 56; // Integer | If Someone introduced this user to the system, then that user's UserId.             
    Integer guardian = 56; // Integer | Gaurdian of the this user if he/she is under 18 years old.             
    Integer typeId = 56; // Integer | Type of the user.             
    try {
      apiInstance.userUpdateUser(userId, accountNumber, gymNumber, externalEntityNumber, name, number, introduceBy, guardian, typeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userUpdateUser");
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
| **userId** | **Integer**| Indentity number(primary key) for user object. Generated in DB table when inserting a record.              | [optional] |
| **accountNumber** | **String**| Account number of the user.It can be any stakeholder of the application.even can be a gym.              | [optional] |
| **gymNumber** | **String**| If this user is a gym, then the gym number.              | [optional] |
| **externalEntityNumber** | **String**| Entity number that make a relationship with BOX API DB.              | [optional] |
| **name** | **String**| Name of the user.              | [optional] |
| **number** | **String**| Unique number maintain by application to idenify user.              | [optional] |
| **introduceBy** | **Integer**| If Someone introduced this user to the system, then that user&#39;s UserId.              | [optional] |
| **guardian** | **Integer**| Gaurdian of the this user if he/she is under 18 years old.              | [optional] |
| **typeId** | **Integer**| Type of the user.              | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | API Response true or false |  -  |
| **404** |  |  -  |

