# KKidApi

All URIs are relative to *https://restapi.kumpeapps.com/v5*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**kkidAllowanceGet**](KKidApi.md#kkidAllowanceGet) | **GET** /kkid/allowance | returns allowance balance and allowance transactions |
| [**kkidAllowancePost**](KKidApi.md#kkidAllowancePost) | **POST** /kkid/allowance | adds new allowance transaction to kidUserID |
| [**kkidApnsPost**](KKidApi.md#kkidApnsPost) | **POST** /kkid/apns | subscribes/unsubscribes/registers for apns push notifications |
| [**kkidChorelistDelete**](KKidApi.md#kkidChorelistDelete) | **DELETE** /kkid/chorelist | deletes chore for given chore id |
| [**kkidChorelistGet**](KKidApi.md#kkidChorelistGet) | **GET** /kkid/chorelist | returns list of chores for given user |
| [**kkidChorelistPost**](KKidApi.md#kkidChorelistPost) | **POST** /kkid/chorelist | adds chore for given user |
| [**kkidChorelistPut**](KKidApi.md#kkidChorelistPut) | **PUT** /kkid/chorelist | updates chore for given chore id |
| [**kkidMasteruserPost**](KKidApi.md#kkidMasteruserPost) | **POST** /kkid/masteruser | adds new master user account |
| [**kkidShareGet**](KKidApi.md#kkidShareGet) | **GET** /kkid/share | Create Share Link |
| [**kkidUserGet**](KKidApi.md#kkidUserGet) | **GET** /kkid/user | Gets user info |
| [**kkidUserlistDelete**](KKidApi.md#kkidUserlistDelete) | **DELETE** /kkid/userlist | deletes user |
| [**kkidUserlistGet**](KKidApi.md#kkidUserlistGet) | **GET** /kkid/userlist | returns list of users |
| [**kkidUserlistPost**](KKidApi.md#kkidUserlistPost) | **POST** /kkid/userlist | adds new child user |
| [**kkidUserlistPut**](KKidApi.md#kkidUserlistPut) | **PUT** /kkid/userlist | updates user |
| [**kkidWishlistDelete**](KKidApi.md#kkidWishlistDelete) | **DELETE** /kkid/wishlist | Delete item from wishlist |
| [**kkidWishlistGet**](KKidApi.md#kkidWishlistGet) | **GET** /kkid/wishlist | Get list of wishlist items |
| [**kkidWishlistPost**](KKidApi.md#kkidWishlistPost) | **POST** /kkid/wishlist | Add item to kid&#39;s wishlist |
| [**kkidWishlistPut**](KKidApi.md#kkidWishlistPut) | **PUT** /kkid/wishlist | Update item on kid&#39;s wishlist |


<a id="kkidAllowanceGet"></a>
# **kkidAllowanceGet**
> Allowance kkidAllowanceGet(kidUserId, transactionDays)

returns allowance balance and allowance transactions

By passing in the appropriate options, you can view allowance balance and allowance transactions for a given user provided that they are within the masterID account of the authenticated user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    Integer kidUserId = 56; // Integer | userID of the kid
    Integer transactionDays = 56; // Integer | number of days you wish to search allowance transactions (default is 90 days)
    try {
      Allowance result = apiInstance.kkidAllowanceGet(kidUserId, transactionDays);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidAllowanceGet");
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
| **kidUserId** | **Integer**| userID of the kid | |
| **transactionDays** | **Integer**| number of days you wish to search allowance transactions (default is 90 days) | [optional] |

### Return type

[**Allowance**](Allowance.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **202** | Accepted- Access Granted but data flow did not complete due to an unknown error. |  -  |
| **206** | No Data Returned |  -  |
| **400** | bad input parameter |  -  |
| **401** | Unauthorized- API credentials not supplied. Ensure you have passed proper Username and Password parameters |  -  |
| **403** | Forbidden- User access is denied. API user either does not have access or has been banned/locked. |  -  |
| **405** | Method Not Allowed- API user does not have access to use this method |  -  |
| **412** | API Access Denied! Your API key is invalid, expired, or not supplied! |  -  |

<a id="kkidAllowancePost"></a>
# **kkidAllowancePost**
> Success kkidAllowancePost(kidUserId, amount, description, transactionType)

adds new allowance transaction to kidUserID

By passing in the appropriate options, you can add an allowance transaction to a given user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    Integer kidUserId = 56; // Integer | userID of the kid
    BigDecimal amount = new BigDecimal(78); // BigDecimal | amount you wish to Add/Subtract (subtract value should be a negative value)
    String description = "description_example"; // String | Description (reason) of allowance transaction
    String transactionType = "Add"; // String | Transaction Type (Add/Subtract)
    try {
      Success result = apiInstance.kkidAllowancePost(kidUserId, amount, description, transactionType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidAllowancePost");
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
| **kidUserId** | **Integer**| userID of the kid | |
| **amount** | **BigDecimal**| amount you wish to Add/Subtract (subtract value should be a negative value) | |
| **description** | **String**| Description (reason) of allowance transaction | |
| **transactionType** | **String**| Transaction Type (Add/Subtract) | [enum: Add, Subtract] |

### Return type

[**Success**](Success.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **202** | Accepted- Access Granted but data flow did not complete due to an unknown error. |  -  |
| **206** | No Data Returned |  -  |
| **400** | bad input parameter |  -  |
| **401** | Unauthorized- API credentials not supplied. Ensure you have passed proper Username and Password parameters |  -  |
| **403** | Forbidden- User access is denied. API user either does not have access or has been banned/locked. |  -  |
| **405** | Method Not Allowed- API user does not have access to use this method |  -  |
| **412** | API Access Denied! Your API key is invalid, expired, or not supplied! |  -  |

<a id="kkidApnsPost"></a>
# **kkidApnsPost**
> Success kkidApnsPost(kidUserId, tool, token, devicename, title, message, badge, sound, section, priority)

subscribes/unsubscribes/registers for apns push notifications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    Integer kidUserId = 56; // Integer | userID of the kid
    String tool = "register"; // String | tool you wish to talk to
    String token = "token_example"; // String | device APNS token (required for register)
    String devicename = "devicename_example"; // String | Name of device to associate to token (required for register)
    String title = "title_example"; // String | title of APNS message (required for send)
    String message = "message_example"; // String | APNS message body (required for send)
    Integer badge = 56; // Integer | Number for badge icon (optional for send)
    String sound = "sound_example"; // String | Name of sound file to play for send notification (optional for send)
    String section = "Chores"; // String | Notification section name (required for send/subscribe/unsubscribe)
    String priority = "passive"; // String | Notification section name (optional for send, default is active)
    try {
      Success result = apiInstance.kkidApnsPost(kidUserId, tool, token, devicename, title, message, badge, sound, section, priority);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidApnsPost");
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
| **kidUserId** | **Integer**| userID of the kid | |
| **tool** | **String**| tool you wish to talk to | [enum: register, subscribe, unsubscribe, send] |
| **token** | **String**| device APNS token (required for register) | [optional] |
| **devicename** | **String**| Name of device to associate to token (required for register) | [optional] |
| **title** | **String**| title of APNS message (required for send) | [optional] |
| **message** | **String**| APNS message body (required for send) | [optional] |
| **badge** | **Integer**| Number for badge icon (optional for send) | [optional] |
| **sound** | **String**| Name of sound file to play for send notification (optional for send) | [optional] |
| **section** | **String**| Notification section name (required for send/subscribe/unsubscribe) | [optional] [enum: Chores, Chores-New, Chores-Reminders, Allowance, Allowance-New, WishList] |
| **priority** | **String**| Notification section name (optional for send, default is active) | [optional] [enum: passive, active, time-sensitive, critical] |

### Return type

[**Success**](Success.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **202** | Accepted- Access Granted but data flow did not complete due to an unknown error. |  -  |
| **206** | No Data Returned |  -  |
| **400** | bad input parameter |  -  |
| **401** | Unauthorized- API credentials not supplied. Ensure you have passed proper Username and Password parameters |  -  |
| **403** | Forbidden- User access is denied. API user either does not have access or has been banned/locked. |  -  |
| **405** | Method Not Allowed- API user does not have access to use this method |  -  |
| **412** | API Access Denied! Your API key is invalid, expired, or not supplied! |  -  |

<a id="kkidChorelistDelete"></a>
# **kkidChorelistDelete**
> Success kkidChorelistDelete(idChoreList)

deletes chore for given chore id

By passing in the appropriate options, you can delete a chore for the given chore id under authenticated user&#39;s master account 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    Integer idChoreList = 56; // Integer | id of the chore you wish to delete
    try {
      Success result = apiInstance.kkidChorelistDelete(idChoreList);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidChorelistDelete");
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
| **idChoreList** | **Integer**| id of the chore you wish to delete | |

### Return type

[**Success**](Success.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deletion successful |  -  |
| **202** | Accepted- Access Granted but data flow did not complete due to an unknown error. |  -  |
| **206** | No Data Found. |  -  |
| **400** | bad input parameter |  -  |
| **401** | Unauthorized- API credentials not supplied. Ensure you have passed proper Username and Password parameters |  -  |
| **403** | Forbidden- User access is denied. API user either does not have access or has been banned/locked. |  -  |
| **405** | Method Not Allowed- API user does not have access to use this method |  -  |
| **409** | Conflict- idChoreList parameter was not supplied or is blank |  -  |
| **412** | API Access Denied! Your API key is invalid, expired, or not supplied! |  -  |

<a id="kkidChorelistGet"></a>
# **kkidChorelistGet**
> Chorelist kkidChorelistGet(kidUsername, day, status, blockDash, optional, canSteal, includeCalendar)

returns list of chores for given user

By passing in the appropriate options, you can search for chores assigned to a given user within the authenticated user&#39;s master account 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    String kidUsername = "kidUsername_example"; // String | Username of kid you wish to search
    String day = "Sunday"; // String | Day of week for chores (Weekly for weekly chores)
    String status = "status_example"; // String | Status of Chore to search
    Boolean blockDash = true; // Boolean | Filter results by blockDash parameter
    Boolean optional = true; // Boolean | Filter results by optional parameter
    Boolean canSteal = true; // Boolean | Filter results by canSteal parameter
    Boolean includeCalendar = true; // Boolean | include calendar notations (default is false)
    try {
      Chorelist result = apiInstance.kkidChorelistGet(kidUsername, day, status, blockDash, optional, canSteal, includeCalendar);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidChorelistGet");
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
| **kidUsername** | **String**| Username of kid you wish to search | [optional] |
| **day** | **String**| Day of week for chores (Weekly for weekly chores) | [optional] [enum: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Weekly] |
| **status** | **String**| Status of Chore to search | [optional] |
| **blockDash** | **Boolean**| Filter results by blockDash parameter | [optional] |
| **optional** | **Boolean**| Filter results by optional parameter | [optional] |
| **canSteal** | **Boolean**| Filter results by canSteal parameter | [optional] |
| **includeCalendar** | **Boolean**| include calendar notations (default is false) | [optional] |

### Return type

[**Chorelist**](Chorelist.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **202** | Accepted- Access Granted but data flow did not complete due to an unknown error. |  -  |
| **206** | No Data Found. |  -  |
| **400** | bad input parameter |  -  |
| **401** | Unauthorized- API credentials not supplied. Ensure you have passed proper Username and Password parameters |  -  |
| **403** | Forbidden- User access is denied. API user either does not have access or has been banned/locked. |  -  |
| **405** | Method Not Allowed- API user does not have access to use this method |  -  |
| **412** | API Access Denied! Your API key is invalid, expired, or not supplied! |  -  |

<a id="kkidChorelistPost"></a>
# **kkidChorelistPost**
> Success kkidChorelistPost(kidUsername, choreName, day, nfcTag, status, choreDescription, choreNumber, blockDash, oneTime, extraAllowance, optional, reassignable, canSteal, startDate, notes, requireObjectDetection, objectDetectionTag, updatedByAutomation, aiIcon, isCalendar)

adds chore for given user

By passing in the appropriate options, you can add a chore to given kid username under authenticated user&#39;s master account 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    String kidUsername = "kidUsername_example"; // String | username of kid to assign the chore to.
    String choreName = "choreName_example"; // String | name of chore
    String day = "Sunday"; // String | day of week (Monday, Tuesday....) for the chore. For weekly chores put Weekly or leave blank
    String nfcTag = "nfcTag_example"; // String | text field of nfc tag required to check off chore
    String status = "status_example"; // String | status of chore (default is todo)
    String choreDescription = "choreDescription_example"; // String | optional chore description
    Integer choreNumber = 56; // Integer | number priority of chore (default is 5)
    Boolean blockDash = true; // Boolean | block dash option on this chore
    Boolean oneTime = true; // Boolean | mark as one time chore (does not repeat each week)
    Integer extraAllowance = 56; // Integer | ammount of allowance added at end of week for completing this chore
    Boolean optional = true; // Boolean | mark as optional chore
    Boolean reassignable = true; // Boolean | mark as reassignable (default is true)
    Boolean canSteal = true; // Boolean | mark as sibling can steal chore
    String startDate = "startDate_example"; // String | date (yyyy-mm-dd) that you wish the chore to start showing up. (default is today)
    String notes = "notes_example"; // String | notes added to chore (visable only on reports, kids do not see this note, this is mostly just for the developer)
    Boolean requireObjectDetection = true; // Boolean | require use of camera to detect object detection tag order to check off chore
    String objectDetectionTag = "objectDetectionTag_example"; // String | tag for object detection to search for (required if requireObjectDetection is true)
    Boolean updatedByAutomation = true; // Boolean | true if chore updated via API from an Automation System
    String aiIcon = "aiIcon_example"; // String | Notes if AI Icons should be used (n for no, y for yes, e for yes- error)
    Boolean isCalendar = true; // Boolean | True if this is a calendar note instead of a chore.
    try {
      Success result = apiInstance.kkidChorelistPost(kidUsername, choreName, day, nfcTag, status, choreDescription, choreNumber, blockDash, oneTime, extraAllowance, optional, reassignable, canSteal, startDate, notes, requireObjectDetection, objectDetectionTag, updatedByAutomation, aiIcon, isCalendar);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidChorelistPost");
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
| **kidUsername** | **String**| username of kid to assign the chore to. | |
| **choreName** | **String**| name of chore | |
| **day** | **String**| day of week (Monday, Tuesday....) for the chore. For weekly chores put Weekly or leave blank | [optional] [enum: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Weekly, Today] |
| **nfcTag** | **String**| text field of nfc tag required to check off chore | [optional] |
| **status** | **String**| status of chore (default is todo) | [optional] |
| **choreDescription** | **String**| optional chore description | [optional] |
| **choreNumber** | **Integer**| number priority of chore (default is 5) | [optional] |
| **blockDash** | **Boolean**| block dash option on this chore | [optional] |
| **oneTime** | **Boolean**| mark as one time chore (does not repeat each week) | [optional] |
| **extraAllowance** | **Integer**| ammount of allowance added at end of week for completing this chore | [optional] |
| **optional** | **Boolean**| mark as optional chore | [optional] |
| **reassignable** | **Boolean**| mark as reassignable (default is true) | [optional] |
| **canSteal** | **Boolean**| mark as sibling can steal chore | [optional] |
| **startDate** | **String**| date (yyyy-mm-dd) that you wish the chore to start showing up. (default is today) | [optional] |
| **notes** | **String**| notes added to chore (visable only on reports, kids do not see this note, this is mostly just for the developer) | [optional] |
| **requireObjectDetection** | **Boolean**| require use of camera to detect object detection tag order to check off chore | [optional] |
| **objectDetectionTag** | **String**| tag for object detection to search for (required if requireObjectDetection is true) | [optional] |
| **updatedByAutomation** | **Boolean**| true if chore updated via API from an Automation System | [optional] |
| **aiIcon** | **String**| Notes if AI Icons should be used (n for no, y for yes, e for yes- error) | [optional] |
| **isCalendar** | **Boolean**| True if this is a calendar note instead of a chore. | [optional] |

### Return type

[**Success**](Success.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **202** | Accepted- Access Granted but data flow did not complete due to an unknown error. |  -  |
| **206** | No Data Found. |  -  |
| **400** | bad input parameter |  -  |
| **401** | Unauthorized- API credentials not supplied. Ensure you have passed proper Username and Password parameters |  -  |
| **403** | Forbidden- User access is denied. API user either does not have access or has been banned/locked. |  -  |
| **405** | Method Not Allowed- API user does not have access to use this method |  -  |
| **409** | Conflict- idChoreList parameter was not supplied or is blank |  -  |
| **412** | API Access Denied! Your API key is invalid, expired, or not supplied! |  -  |

<a id="kkidChorelistPut"></a>
# **kkidChorelistPut**
> Success kkidChorelistPut(idChoreList, status, stolen, stolenBy, nfcTag, notes, latitude, longitude, altitude, updatedByAutomation, whereDay, whereStatus, whereName)

updates chore for given chore id

By passing in the appropriate options, you can update the fields of a specific core within the authenticated user&#39;s master account 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    Integer idChoreList = 56; // Integer | id number of chore you wish to update
    String status = "status_example"; // String | new status of chore
    Boolean stolen = true; // Boolean | mark chore as stolen by sibling
    String stolenBy = "stolenBy_example"; // String | username of sibling that stole the chore (required if stolen is true)
    String nfcTag = "nfcTag_example"; // String | text field of NFC tag that is required to be scanned to check off this chore (normally null)
    String notes = "notes_example"; // String | notes field for chore
    Integer latitude = 56; // Integer | GPS latitude of where the chore was marked
    Integer longitude = 56; // Integer | GPS longitude of where the chore was marked
    Integer altitude = 56; // Integer | GPS altitude of where the chore was marked
    Boolean updatedByAutomation = true; // Boolean | true if updated via API by automation system
    String whereDay = "Sunday"; // String | Where day equals...
    String whereStatus = "whereStatus_example"; // String | Where status equals...
    String whereName = "whereName_example"; // String | Where chore name equals...
    try {
      Success result = apiInstance.kkidChorelistPut(idChoreList, status, stolen, stolenBy, nfcTag, notes, latitude, longitude, altitude, updatedByAutomation, whereDay, whereStatus, whereName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidChorelistPut");
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
| **idChoreList** | **Integer**| id number of chore you wish to update | |
| **status** | **String**| new status of chore | [optional] |
| **stolen** | **Boolean**| mark chore as stolen by sibling | [optional] |
| **stolenBy** | **String**| username of sibling that stole the chore (required if stolen is true) | [optional] |
| **nfcTag** | **String**| text field of NFC tag that is required to be scanned to check off this chore (normally null) | [optional] |
| **notes** | **String**| notes field for chore | [optional] |
| **latitude** | **Integer**| GPS latitude of where the chore was marked | [optional] |
| **longitude** | **Integer**| GPS longitude of where the chore was marked | [optional] |
| **altitude** | **Integer**| GPS altitude of where the chore was marked | [optional] |
| **updatedByAutomation** | **Boolean**| true if updated via API by automation system | [optional] |
| **whereDay** | **String**| Where day equals... | [optional] [enum: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Weekly, Today] |
| **whereStatus** | **String**| Where status equals... | [optional] |
| **whereName** | **String**| Where chore name equals... | [optional] |

### Return type

[**Success**](Success.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **202** | Accepted- Access Granted but data flow did not complete due to an unknown error. |  -  |
| **206** | No Data Found. |  -  |
| **400** | bad input parameter |  -  |
| **401** | Unauthorized- API credentials not supplied. Ensure you have passed proper Username and Password parameters |  -  |
| **403** | Forbidden- User access is denied. API user either does not have access or has been banned/locked. |  -  |
| **405** | Method Not Allowed- API user does not have access to use this method |  -  |
| **412** | API Access Denied! Your API key is invalid, expired, or not supplied! |  -  |

<a id="kkidMasteruserPost"></a>
# **kkidMasteruserPost**
> AddUserResponse kkidMasteruserPost(username, password, email, firstName, lastName)

adds new master user account

By passing in the appropriate variables this method creates a new user with master account access. (The use of this method is restricted to Superusers ONLY) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: app_key
    ApiKeyAuth app_key = (ApiKeyAuth) defaultClient.getAuthentication("app_key");
    app_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //app_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    String username = "username_example"; // String | username of user to create
    String password = "password_example"; // String | password of user to create
    String email = "email_example"; // String | email address of user to create
    String firstName = "firstName_example"; // String | First Name of user to create
    String lastName = "lastName_example"; // String | Last Name of user to create
    try {
      AddUserResponse result = apiInstance.kkidMasteruserPost(username, password, email, firstName, lastName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidMasteruserPost");
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
| **username** | **String**| username of user to create | |
| **password** | **String**| password of user to create | |
| **email** | **String**| email address of user to create | |
| **firstName** | **String**| First Name of user to create | |
| **lastName** | **String**| Last Name of user to create | |

### Return type

[**AddUserResponse**](AddUserResponse.md)

### Authorization

[app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User Added |  -  |
| **202** | Accepted- Access Granted but data flow did not complete due to an unknown error. |  -  |
| **405** | Method Not Allowed- API user does not have access to use this method |  -  |
| **409** | Create user unsuccessful! This is normally because the username or password already exists in the KumpeApps system. |  -  |

<a id="kkidShareGet"></a>
# **kkidShareGet**
> Model201Share kkidShareGet(linkUserId, link, scope, scope2, scope3, scope4)

Create Share Link

Create share link

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    String linkUserId = "linkUserId_example"; // String | User ID that the link should be authenticated to
    String link = "https://khome.kumpeapps.com/portal/wish-list.php"; // String | Link to share
    String scope = "WishList"; // String | Authentication scope for link
    String scope2 = "WishList"; // String | Authentication scope for link
    String scope3 = "WishList"; // String | Authentication scope for link
    String scope4 = "WishList"; // String | Authentication scope for link
    try {
      Model201Share result = apiInstance.kkidShareGet(linkUserId, link, scope, scope2, scope3, scope4);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidShareGet");
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
| **linkUserId** | **String**| User ID that the link should be authenticated to | |
| **link** | **String**| Link to share | [enum: https://khome.kumpeapps.com/portal/wish-list.php, https://khome.kumpeapps.com/portal/chores-today.php] |
| **scope** | **String**| Authentication scope for link | [enum: WishList, WishListAdmin, Chores, ChoresAdmin] |
| **scope2** | **String**| Authentication scope for link | [optional] [enum: WishList, WishListAdmin, Chores, ChoresAdmin] |
| **scope3** | **String**| Authentication scope for link | [optional] [enum: WishList, WishListAdmin, Chores, ChoresAdmin] |
| **scope4** | **String**| Authentication scope for link | [optional] [enum: WishList, WishListAdmin, Chores, ChoresAdmin] |

### Return type

[**Model201Share**](Model201Share.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | authenticated link created |  -  |

<a id="kkidUserGet"></a>
# **kkidUserGet**
> Userlist kkidUserGet(enableBool)

Gets user info

Gets user info for authenticated user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    Boolean enableBool = true; // Boolean | Use bool values instead of Int 0/1
    try {
      Userlist result = apiInstance.kkidUserGet(enableBool);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidUserGet");
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
| **enableBool** | **Boolean**| Use bool values instead of Int 0/1 | [optional] |

### Return type

[**Userlist**](Userlist.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |

<a id="kkidUserlistDelete"></a>
# **kkidUserlistDelete**
> kkidUserlistDelete(userID)

deletes user

By passing in the appropriate variables this method deletes the specified user. (This function is restricted to Superusers ONLY) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    Integer userID = 56; // Integer | userID of the user you wish to delete
    try {
      apiInstance.kkidUserlistDelete(userID);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidUserlistDelete");
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
| **userID** | **Integer**| userID of the user you wish to delete | |

### Return type

null (empty response body)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User Deleted |  -  |
| **202** | Accepted- Access Granted but data flow did not complete due to an unknown error. |  -  |
| **405** | Method Not Allowed- API user does not have access to use this method |  -  |
| **409** | Create user unsuccessful! This is normally because the username or password already exists in the KumpeApps system. |  -  |
| **412** | API Access Denied! Your API key is invalid, expired, or not supplied! |  -  |

<a id="kkidUserlistGet"></a>
# **kkidUserlistGet**
> Userlist kkidUserlistGet(isChild, isActive, isAdmin, enableAllowance, enableChores, userID, username, email)

returns list of users

By passing in the appropriate options, you can search for users within the authenticated user&#39;s master account 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    Boolean isChild = true; // Boolean | Filter Search by isChild flag
    Boolean isActive = true; // Boolean | Filter Search by isActive flag
    Boolean isAdmin = true; // Boolean | Filter Search by isAdmin flag
    Boolean enableAllowance = true; // Boolean | Filter Search by enableAllowance flag
    Boolean enableChores = true; // Boolean | Filter Search by enableChores flag
    Integer userID = 56; // Integer | userID of user to search
    String username = "username_example"; // String | Username of user to search
    String email = "email_example"; // String | Email address of user to search
    try {
      Userlist result = apiInstance.kkidUserlistGet(isChild, isActive, isAdmin, enableAllowance, enableChores, userID, username, email);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidUserlistGet");
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
| **isChild** | **Boolean**| Filter Search by isChild flag | [optional] |
| **isActive** | **Boolean**| Filter Search by isActive flag | [optional] |
| **isAdmin** | **Boolean**| Filter Search by isAdmin flag | [optional] |
| **enableAllowance** | **Boolean**| Filter Search by enableAllowance flag | [optional] |
| **enableChores** | **Boolean**| Filter Search by enableChores flag | [optional] |
| **userID** | **Integer**| userID of user to search | [optional] |
| **username** | **String**| Username of user to search | [optional] |
| **email** | **String**| Email address of user to search | [optional] |

### Return type

[**Userlist**](Userlist.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **202** | Accepted- Access Granted but data flow did not complete due to an unknown error. |  -  |
| **204** | No Data Returned |  -  |
| **400** | bad input parameter |  -  |
| **401** | Unauthorized- API credentials not supplied. Ensure you have passed proper Username and Password parameters |  -  |
| **403** | Forbidden- User access is denied. API user either does not have access or has been banned/locked. |  -  |
| **405** | Method Not Allowed- API user does not have access to use this method |  -  |
| **412** | API Access Denied! Your API key is invalid, expired, or not supplied! |  -  |

<a id="kkidUserlistPost"></a>
# **kkidUserlistPost**
> AddUserResponse kkidUserlistPost(username, password, email, firstName, lastName)

adds new child user

By passing in the appropriate variables this method creates a new user and assigns it to the master account of the authenticated user. By default this user will have chores and allowance access. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    String username = "username_example"; // String | username of user to create
    String password = "password_example"; // String | password of user to create
    String email = "email_example"; // String | email address of user to create
    String firstName = "firstName_example"; // String | First Name of user to create
    String lastName = "lastName_example"; // String | Last Name of user to create
    try {
      AddUserResponse result = apiInstance.kkidUserlistPost(username, password, email, firstName, lastName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidUserlistPost");
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
| **username** | **String**| username of user to create | |
| **password** | **String**| password of user to create | |
| **email** | **String**| email address of user to create | |
| **firstName** | **String**| First Name of user to create | |
| **lastName** | **String**| Last Name of user to create | |

### Return type

[**AddUserResponse**](AddUserResponse.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User Added |  -  |
| **202** | Accepted- Access Granted but data flow did not complete due to an unknown error. |  -  |
| **405** | Method Not Allowed- API user does not have access to use this method |  -  |
| **409** | Create user unsuccessful! This is normally because the username or password already exists in the KumpeApps system. |  -  |
| **412** | API Access Denied! Your API key is invalid, expired, or not supplied! |  -  |

<a id="kkidUserlistPut"></a>
# **kkidUserlistPut**
> AddUserResponse kkidUserlistPut(userID, username, email, firstName, lastName, emoji, tmdbKey, enableWishList, enableChores, enableAllowance, enableAdmin, enableTmdb, enableObjectDetection)

updates user

By passing in the appropriate variables this method updates the user&#39;s profile 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    Integer userID = 56; // Integer | userID of the user you wish to update
    String username = "username_example"; // String | username of user to create
    String email = "email_example"; // String | email address of user to create
    String firstName = "firstName_example"; // String | First Name of user to create
    String lastName = "lastName_example"; // String | Last Name of user to create
    String emoji = "emoji_example"; // String | emoji character for user
    String tmdbKey = "tmdbKey_example"; // String | User's TMdB Session Key
    Boolean enableWishList = true; // Boolean | set status of Wish List module enabled
    Boolean enableChores = true; // Boolean | set status of chores module enabled
    Boolean enableAllowance = true; // Boolean | set status of allowance module enabled
    Boolean enableAdmin = true; // Boolean | set status of isAdmin
    Boolean enableTmdb = true; // Boolean | set status of enableTmdb (movie and tv search)
    Boolean enableObjectDetection = true; // Boolean | set status of enableObjectDetection
    try {
      AddUserResponse result = apiInstance.kkidUserlistPut(userID, username, email, firstName, lastName, emoji, tmdbKey, enableWishList, enableChores, enableAllowance, enableAdmin, enableTmdb, enableObjectDetection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidUserlistPut");
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
| **userID** | **Integer**| userID of the user you wish to update | |
| **username** | **String**| username of user to create | |
| **email** | **String**| email address of user to create | |
| **firstName** | **String**| First Name of user to create | |
| **lastName** | **String**| Last Name of user to create | |
| **emoji** | **String**| emoji character for user | [optional] |
| **tmdbKey** | **String**| User&#39;s TMdB Session Key | [optional] |
| **enableWishList** | **Boolean**| set status of Wish List module enabled | [optional] |
| **enableChores** | **Boolean**| set status of chores module enabled | [optional] |
| **enableAllowance** | **Boolean**| set status of allowance module enabled | [optional] |
| **enableAdmin** | **Boolean**| set status of isAdmin | [optional] |
| **enableTmdb** | **Boolean**| set status of enableTmdb (movie and tv search) | [optional] |
| **enableObjectDetection** | **Boolean**| set status of enableObjectDetection | [optional] |

### Return type

[**AddUserResponse**](AddUserResponse.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User Updated |  -  |
| **202** | Accepted- Access Granted but data flow did not complete due to an unknown error. |  -  |
| **405** | Method Not Allowed- API user does not have access to use this method |  -  |
| **409** | Update user unsuccessful. This could be due to invalid userID, new username already exists, new email already exists, or an unknown error. |  -  |
| **412** | API Access Denied! Your API key is invalid, expired, or not supplied! |  -  |

<a id="kkidWishlistDelete"></a>
# **kkidWishlistDelete**
> Success kkidWishlistDelete(wishId)

Delete item from wishlist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    Integer wishId = 56; // Integer | ID of wishlist item to delete
    try {
      Success result = apiInstance.kkidWishlistDelete(wishId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidWishlistDelete");
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
| **wishId** | **Integer**| ID of wishlist item to delete | |

### Return type

[**Success**](Success.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |

<a id="kkidWishlistGet"></a>
# **kkidWishlistGet**
> Wishlist kkidWishlistGet(kidUserId)

Get list of wishlist items

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    Integer kidUserId = 56; // Integer | userID of the kid
    try {
      Wishlist result = apiInstance.kkidWishlistGet(kidUserId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidWishlistGet");
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
| **kidUserId** | **Integer**| userID of the kid | [optional] |

### Return type

[**Wishlist**](Wishlist.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |

<a id="kkidWishlistPost"></a>
# **kkidWishlistPost**
> Success kkidWishlistPost(kidUserId, title, description, priority, link)

Add item to kid&#39;s wishlist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    Integer kidUserId = 56; // Integer | userID of the kid
    String title = "title_example"; // String | Item title
    String description = "description_example"; // String | Item Description
    Integer priority = 56; // Integer | Item Priority
    String link = "link_example"; // String | URL Link to item
    try {
      Success result = apiInstance.kkidWishlistPost(kidUserId, title, description, priority, link);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidWishlistPost");
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
| **kidUserId** | **Integer**| userID of the kid | |
| **title** | **String**| Item title | |
| **description** | **String**| Item Description | [optional] |
| **priority** | **Integer**| Item Priority | [optional] |
| **link** | **String**| URL Link to item | [optional] |

### Return type

[**Success**](Success.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | search results matching criteria |  -  |

<a id="kkidWishlistPut"></a>
# **kkidWishlistPut**
> Success kkidWishlistPut(wishId, title, description, priority, link)

Update item on kid&#39;s wishlist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KKidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://restapi.kumpeapps.com/v5");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KKidApi apiInstance = new KKidApi(defaultClient);
    Integer wishId = 56; // Integer | Wish list item ID to update
    String title = "title_example"; // String | Item title
    String description = "description_example"; // String | Item Description
    Integer priority = 56; // Integer | Item Priority
    String link = "link_example"; // String | URL Link to item
    try {
      Success result = apiInstance.kkidWishlistPut(wishId, title, description, priority, link);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KKidApi#kkidWishlistPut");
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
| **wishId** | **Integer**| Wish list item ID to update | |
| **title** | **String**| Item title | [optional] |
| **description** | **String**| Item Description | [optional] |
| **priority** | **Integer**| Item Priority | [optional] |
| **link** | **String**| URL Link to item | [optional] |

### Return type

[**Success**](Success.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | search results matching criteria |  -  |

