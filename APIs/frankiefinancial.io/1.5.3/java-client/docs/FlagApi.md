# FlagApi

All URIs are relative to *https://api.demo.frankiefinancial.io/compliance/v1.2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**blacklistEntity**](FlagApi.md#blacklistEntity) | **POST** /entity/{entityId}/flag/blacklist | Set Entity Blacklist State. |
| [**entityMonitoring**](FlagApi.md#entityMonitoring) | **POST** /entity/{entityId}/flag/monitor | Set Entity Ongoing AML Monitoring Status. |
| [**flagDuplicateEntity**](FlagApi.md#flagDuplicateEntity) | **POST** /entity/{entityId}/flag/duplicate/{otherId} | Resolve Duplicate States. |
| [**watchlistEntity**](FlagApi.md#watchlistEntity) | **POST** /entity/{entityId}/flag/watchlist | Set Entity Watchlist State. |


<a id="blacklistEntity"></a>
# **blacklistEntity**
> EntityResultObject blacklistEntity(xFrankieCustomerID, entityId, set, xFrankieCustomerChildID, reason, blockedBy, attribute, originalId)

Set Entity Blacklist State.

Mark the entity as blacklisted or not with the &#39;?set&#x3D;&#39; query parameter as &#39;true&#39; or &#39;false&#39;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FlagApi apiInstance = new FlagApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID entityId = UUID.randomUUID(); // UUID | The entityId returned previously from an earlier call to /check or /entity
    Boolean set = true; // Boolean | Set the value of an entity flag. 
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    String reason = "reason_example"; // String | Set the reason for blacklisting. Valid values are:   - \"NO_REASON_SUPPLIED\"   - \"FABRICATED_IDENTITY\"   - \"IDENTITY_TAKEOVER\"   - \"FALSIFIED_ID_DOCUMENTS\"   - \"STOLEN_ID_DOCUMENTS\"   - \"MERCHANT_FRAUD\"   - \"NEVER_PAY_BUST_OUT\"   - \"CONFLICTING_DATA_PROVIDED\"   - \"MONEY_MULE\"   - \"FALSE_FRAUD_CLAIM\"   - \"FRAUDULENT_3RD_PARTY\"   - \"COMPANY_TAKEOVER\"   - \"FICTITIOUS_EMPLOYER\"   - \"COLLUSIVE_EMPLOYER\"   - \"OVER_VALUATION_OF_ASSETS\"   - \"FALSIFIED_EMPLOYMENT_DETAILS\"   - \"MANIPULATED_IDENTITY\"   - \"SYNDICATED_FRAUD\"   - \"INTERNAL_FRAUD\"   - \"BANK_FRAUD\"   - \"UNDISCLOSED_DATA\"   - \"FALSE_HARDSHIP\"   - \"SMR_REPORT_LODGED\"   - \"2X_SMR_REPORTS_LODGED\" 
    String blockedBy = "blockedBy_example"; // String | Specify who is setting the entity as blacklisted. 
    String attribute = "attribute_example"; // String | Specify the blacklisted attribute. Valid values are:   - \"ENTIRE_PROFILE\"   - \"FULL_NAME\"   - \"EMAIL_ADDRESS\"   - \"PHONE_NUMBER\"   - \"ID_DOCUMENT\"   - \"MAILING_ADDRESS\"   - \"RESIDENTIAL_ADDRESS\"    
    String originalId = "originalId_example"; // String | Specify the Id of the matching blacklisted entity or single data-point. 
    try {
      EntityResultObject result = apiInstance.blacklistEntity(xFrankieCustomerID, entityId, set, xFrankieCustomerChildID, reason, blockedBy, attribute, originalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlagApi#blacklistEntity");
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
| **xFrankieCustomerID** | **UUID**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | |
| **entityId** | **UUID**| The entityId returned previously from an earlier call to /check or /entity | |
| **set** | **Boolean**| Set the value of an entity flag.  | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **reason** | **String**| Set the reason for blacklisting. Valid values are:   - \&quot;NO_REASON_SUPPLIED\&quot;   - \&quot;FABRICATED_IDENTITY\&quot;   - \&quot;IDENTITY_TAKEOVER\&quot;   - \&quot;FALSIFIED_ID_DOCUMENTS\&quot;   - \&quot;STOLEN_ID_DOCUMENTS\&quot;   - \&quot;MERCHANT_FRAUD\&quot;   - \&quot;NEVER_PAY_BUST_OUT\&quot;   - \&quot;CONFLICTING_DATA_PROVIDED\&quot;   - \&quot;MONEY_MULE\&quot;   - \&quot;FALSE_FRAUD_CLAIM\&quot;   - \&quot;FRAUDULENT_3RD_PARTY\&quot;   - \&quot;COMPANY_TAKEOVER\&quot;   - \&quot;FICTITIOUS_EMPLOYER\&quot;   - \&quot;COLLUSIVE_EMPLOYER\&quot;   - \&quot;OVER_VALUATION_OF_ASSETS\&quot;   - \&quot;FALSIFIED_EMPLOYMENT_DETAILS\&quot;   - \&quot;MANIPULATED_IDENTITY\&quot;   - \&quot;SYNDICATED_FRAUD\&quot;   - \&quot;INTERNAL_FRAUD\&quot;   - \&quot;BANK_FRAUD\&quot;   - \&quot;UNDISCLOSED_DATA\&quot;   - \&quot;FALSE_HARDSHIP\&quot;   - \&quot;SMR_REPORT_LODGED\&quot;   - \&quot;2X_SMR_REPORTS_LODGED\&quot;  | [optional] |
| **blockedBy** | **String**| Specify who is setting the entity as blacklisted.  | [optional] |
| **attribute** | **String**| Specify the blacklisted attribute. Valid values are:   - \&quot;ENTIRE_PROFILE\&quot;   - \&quot;FULL_NAME\&quot;   - \&quot;EMAIL_ADDRESS\&quot;   - \&quot;PHONE_NUMBER\&quot;   - \&quot;ID_DOCUMENT\&quot;   - \&quot;MAILING_ADDRESS\&quot;   - \&quot;RESIDENTIAL_ADDRESS\&quot;     | [optional] |
| **originalId** | **String**| Specify the Id of the matching blacklisted entity or single data-point.  | [optional] |

### Return type

[**EntityResultObject**](EntityResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors. Returns the entity object as it stands now. No docScan file data from any attached ID documents will be returned unless the /full variant is requested. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |

<a id="entityMonitoring"></a>
# **entityMonitoring**
> EntityResultObject entityMonitoring(xFrankieCustomerID, entityId, set, xFrankieCustomerChildID)

Set Entity Ongoing AML Monitoring Status.

Mark the entity as being monitored or not with the &#39;?set&#x3D;&#39; query parameter as &#39;true&#39; or &#39;false&#39;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FlagApi apiInstance = new FlagApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID entityId = UUID.randomUUID(); // UUID | The entityId returned previously from an earlier call to /check or /entity
    Boolean set = true; // Boolean | Set the value of an entity flag. 
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    try {
      EntityResultObject result = apiInstance.entityMonitoring(xFrankieCustomerID, entityId, set, xFrankieCustomerChildID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlagApi#entityMonitoring");
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
| **xFrankieCustomerID** | **UUID**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | |
| **entityId** | **UUID**| The entityId returned previously from an earlier call to /check or /entity | |
| **set** | **Boolean**| Set the value of an entity flag.  | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |

### Return type

[**EntityResultObject**](EntityResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors. Returns the entity object as it stands now. No docScan file data from any attached ID documents will be returned unless the /full variant is requested. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |

<a id="flagDuplicateEntity"></a>
# **flagDuplicateEntity**
> EntityResultObject flagDuplicateEntity(xFrankieCustomerID, entityId, otherId, set, xFrankieCustomerChildID)

Resolve Duplicate States.

Resolve the state of a pair of duplicate entities with the &#39;?set&#x3D;&#39; query parameter as &#39;true&#39; or &#39;false&#39;. Setting duplicate to &#39;true&#39; will make entityId invisible for most purposes and otherId will continue to function as normal. Setting duplicate to &#39;false&#39; means the two entities are in fact separate but similar and they will both continue to exist independently but will no longer be identified as duplicates of eachother. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FlagApi apiInstance = new FlagApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID entityId = UUID.randomUUID(); // UUID | The entityId returned previously from an earlier call to /check or /entity
    UUID otherId = UUID.randomUUID(); // UUID | An entityId returned previously from an earlier call to /check or /entity. Used when an operation requires two entityIds
    Boolean set = true; // Boolean | Set the value of an entity flag. 
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    try {
      EntityResultObject result = apiInstance.flagDuplicateEntity(xFrankieCustomerID, entityId, otherId, set, xFrankieCustomerChildID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlagApi#flagDuplicateEntity");
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
| **xFrankieCustomerID** | **UUID**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | |
| **entityId** | **UUID**| The entityId returned previously from an earlier call to /check or /entity | |
| **otherId** | **UUID**| An entityId returned previously from an earlier call to /check or /entity. Used when an operation requires two entityIds | |
| **set** | **Boolean**| Set the value of an entity flag.  | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |

### Return type

[**EntityResultObject**](EntityResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors. Returns the entity object as it stands now. No docScan file data from any attached ID documents will be returned unless the /full variant is requested. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |

<a id="watchlistEntity"></a>
# **watchlistEntity**
> EntityResultObject watchlistEntity(xFrankieCustomerID, entityId, set, xFrankieCustomerChildID, reason, comment)

Set Entity Watchlist State.

Mark the entity as watchlisted or not with the &#39;?set&#x3D;&#39; query parameter as &#39;true&#39; or &#39;false&#39;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlagApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    FlagApi apiInstance = new FlagApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID entityId = UUID.randomUUID(); // UUID | The entityId returned previously from an earlier call to /check or /entity
    Boolean set = true; // Boolean | Set the value of an entity flag. 
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    String reason = "reason_example"; // String | Set the reason for watchlisting. Valid values are:  - \"WAS_BLACKLISTED\" 
    String comment = "comment_example"; // String | A comment describing the reason for a request. 
    try {
      EntityResultObject result = apiInstance.watchlistEntity(xFrankieCustomerID, entityId, set, xFrankieCustomerChildID, reason, comment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlagApi#watchlistEntity");
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
| **xFrankieCustomerID** | **UUID**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | |
| **entityId** | **UUID**| The entityId returned previously from an earlier call to /check or /entity | |
| **set** | **Boolean**| Set the value of an entity flag.  | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **reason** | **String**| Set the reason for watchlisting. Valid values are:  - \&quot;WAS_BLACKLISTED\&quot;  | [optional] |
| **comment** | **String**| A comment describing the reason for a request.  | [optional] |

### Return type

[**EntityResultObject**](EntityResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors. Returns the entity object as it stands now. No docScan file data from any attached ID documents will be returned unless the /full variant is requested. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |

