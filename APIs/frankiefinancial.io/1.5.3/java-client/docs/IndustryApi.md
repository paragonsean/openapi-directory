# IndustryApi

All URIs are relative to *https://api.demo.frankiefinancial.io/compliance/v1.2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProcessIndustryUtilityDocument**](IndustryApi.md#createProcessIndustryUtilityDocument) | **POST** /document/new/utility/process/compare | Create Document and Run Utility Price Comparison. |
| [**updateProcessIndustryUtilityDocument**](IndustryApi.md#updateProcessIndustryUtilityDocument) | **POST** /document/{documentId}/utility/process/compare | Update Document and Run Utility Price Comparison. |
| [**updateProcessIndustryUtilityDocumentConsent**](IndustryApi.md#updateProcessIndustryUtilityDocumentConsent) | **POST** /document/{documentId}/utility/process/consent | Provide Explicit Consent to Switch Utility Plans. |
| [**updateProcessIndustryUtilityDocumentSwitch**](IndustryApi.md#updateProcessIndustryUtilityDocumentSwitch) | **POST** /document/{documentId}/utility/process/switch | Initiate Switching of Utility Plan. |


<a id="createProcessIndustryUtilityDocument"></a>
# **createProcessIndustryUtilityDocument**
> DocumentIndustryUtilityProcessResultObject createProcessIndustryUtilityDocument(xFrankieCustomerID, xFrankieCustomerChildID, xFrankieBackground, planLimit, document)

Create Document and Run Utility Price Comparison.

Create a document object. This is then processed to extract useful information, just like a normal OCR scan. The service will then push the document through an industry specific comparison process, where the details are used to find a better plan, based on the bill.  100&#39;s of datapoints are accurately extracted from the uploaded document. This data is then used to compare the bill against the whole market. A personalised comparison is returned that is a best fit for the customer&#39;s energy profile.  * NOTE: It is expected that the type of document being uploaded will be a PDF and the idType is UTILITY_BILL. (These values will be set automatically if not supplied).    You can optionally include the utility name (e.g. Origin Energy) in the idSubType if you wish. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndustryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    IndustryApi apiInstance = new IndustryApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    Integer xFrankieBackground = 56; // Integer | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    Integer planLimit = 30; // Integer | The maximum number of plans to return
    IdentityDocumentObject document = new IdentityDocumentObject(); // IdentityDocumentObject | 
    try {
      DocumentIndustryUtilityProcessResultObject result = apiInstance.createProcessIndustryUtilityDocument(xFrankieCustomerID, xFrankieCustomerChildID, xFrankieBackground, planLimit, document);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndustryApi#createProcessIndustryUtilityDocument");
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
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **xFrankieBackground** | **Integer**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] |
| **planLimit** | **Integer**| The maximum number of plans to return | [optional] [default to 30] |
| **document** | [**IdentityDocumentObject**](IdentityDocumentObject.md)|  | [optional] |

### Return type

[**DocumentIndustryUtilityProcessResultObject**](DocumentIndustryUtilityProcessResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors.  Returns the results of the utility comparison directly from the service provider.  |  -  |
| **202** | The request was valid and can potentially be fulfilled. The Frankie service has now accepted responsibility for processing and we will either push the results to you, or send you a notification, depending on the request and your configuration. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **415** | For requests with payloads, an unsupported Content-Type was specified. The Frankie Financial API only supports a content type of application/json. |  -  |
| **422** | Unprocessable request. This can be triggered in a number of ways. * An attempt to force a check or scan to run, but there is insufficient data to be able to do so. * An attempt to run a utility comparison, or similar industry/document/entity specific scan or process on an unsupported document type (e.g. electricity comparison on a passport) Details of what is required will be in the issues list of the error response.  |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |

<a id="updateProcessIndustryUtilityDocument"></a>
# **updateProcessIndustryUtilityDocument**
> DocumentIndustryUtilityProcessResultObject updateProcessIndustryUtilityDocument(xFrankieCustomerID, documentId, xFrankieCustomerChildID, xFrankieBackground, planLimit, document)

Update Document and Run Utility Price Comparison.

Using a previously uploaded but incomplete document, you can optionally supply updated details or simply request that the document be re-processed through the industry comparison service.   100&#39;s of datapoints are accurately extracted from the uploaded document. This data is then used to compare the bill against the whole market. A personalised comparison is returned that is a best fit for the customer&#39;s energy profile.  * NOTE: It is expected that the type of document being uploaded will be a PDF and the idType is UTILITY_BILL. (These values will be set automatically if not supplied).    You can optionally include the utility name (e.g. Origin Energy) in the idSubType if you wish. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndustryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    IndustryApi apiInstance = new IndustryApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID documentId = UUID.randomUUID(); // UUID | The documentId returned previously from an earlier call to /check or /entity or /document
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    Integer xFrankieBackground = 56; // Integer | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    Integer planLimit = 30; // Integer | The maximum number of plans to return
    IdentityDocumentObject document = new IdentityDocumentObject(); // IdentityDocumentObject | 
    try {
      DocumentIndustryUtilityProcessResultObject result = apiInstance.updateProcessIndustryUtilityDocument(xFrankieCustomerID, documentId, xFrankieCustomerChildID, xFrankieBackground, planLimit, document);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndustryApi#updateProcessIndustryUtilityDocument");
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
| **documentId** | **UUID**| The documentId returned previously from an earlier call to /check or /entity or /document | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **xFrankieBackground** | **Integer**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] |
| **planLimit** | **Integer**| The maximum number of plans to return | [optional] [default to 30] |
| **document** | [**IdentityDocumentObject**](IdentityDocumentObject.md)|  | [optional] |

### Return type

[**DocumentIndustryUtilityProcessResultObject**](DocumentIndustryUtilityProcessResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors.  Returns the results of the utility comparison directly from the service provider.  |  -  |
| **202** | The request was valid and can potentially be fulfilled. The Frankie service has now accepted responsibility for processing and we will either push the results to you, or send you a notification, depending on the request and your configuration. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **415** | For requests with payloads, an unsupported Content-Type was specified. The Frankie Financial API only supports a content type of application/json. |  -  |
| **422** | Unprocessable request. This can be triggered in a number of ways. * An attempt to force a check or scan to run, but there is insufficient data to be able to do so. * An attempt to run a utility comparison, or similar industry/document/entity specific scan or process on an unsupported document type (e.g. electricity comparison on a passport) Details of what is required will be in the issues list of the error response.  |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |

<a id="updateProcessIndustryUtilityDocumentConsent"></a>
# **updateProcessIndustryUtilityDocumentConsent**
> DocumentIndustryUtilityConsentResultObject updateProcessIndustryUtilityDocumentConsent(xFrankieCustomerID, documentId, xFrankieCustomerChildID, xFrankieBackground, consentRequest)

Provide Explicit Consent to Switch Utility Plans.

Using a previously uploaded and processed document, the user must provide explicit consent before being able to call the /switch function.   Before entering into a contract with a new energy retailer, consumers are first obliged to review the retailer&#39;s contractual terms and conditions, confirm they understand these terms as well as give explicit, informed consent (EIC) for the switch to occur. This API call retrieves all information        that must be displayed in order for a compliant EIC to be captured from a consumer.  * NOTE: as part of this call, you must provide a previously returned corellationId that is associated with this document and the returned plan options. Failure to do so will result in an error response. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndustryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    IndustryApi apiInstance = new IndustryApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID documentId = UUID.randomUUID(); // UUID | The documentId returned previously from an earlier call to /check or /entity or /document
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    Integer xFrankieBackground = 56; // Integer | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    EICRequest consentRequest = new EICRequest(); // EICRequest | 
    try {
      DocumentIndustryUtilityConsentResultObject result = apiInstance.updateProcessIndustryUtilityDocumentConsent(xFrankieCustomerID, documentId, xFrankieCustomerChildID, xFrankieBackground, consentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndustryApi#updateProcessIndustryUtilityDocumentConsent");
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
| **documentId** | **UUID**| The documentId returned previously from an earlier call to /check or /entity or /document | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **xFrankieBackground** | **Integer**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] |
| **consentRequest** | [**EICRequest**](EICRequest.md)|  | [optional] |

### Return type

[**DocumentIndustryUtilityConsentResultObject**](DocumentIndustryUtilityConsentResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors. Returns the results directly from the service provider.  Returns the results of the provision of explicit informed consent directly from the service provider.  |  -  |
| **202** | The request was valid and can potentially be fulfilled. The Frankie service has now accepted responsibility for processing and we will either push the results to you, or send you a notification, depending on the request and your configuration. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **415** | For requests with payloads, an unsupported Content-Type was specified. The Frankie Financial API only supports a content type of application/json. |  -  |
| **422** | Unprocessable request. This can be triggered in a number of ways. * An attempt to force a check or scan to run, but there is insufficient data to be able to do so. * An attempt to run a utility comparison, or similar industry/document/entity specific scan or process on an unsupported document type (e.g. electricity comparison on a passport) Details of what is required will be in the issues list of the error response.  |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |

<a id="updateProcessIndustryUtilityDocumentSwitch"></a>
# **updateProcessIndustryUtilityDocumentSwitch**
> DocumentIndustryUtilitySwitchResultObject updateProcessIndustryUtilityDocumentSwitch(xFrankieCustomerID, documentId, xFrankieCustomerChildID, xFrankieBackground, switchRequest)

Initiate Switching of Utility Plan.

Using a previously uploaded and processed document, the user must provide explicit consent before being able to call the /switch function.   The bill payer has uploaded their current bill, selected a new plan, accepted the terms and conditions and given their consent for the switch to occur. This API call will finalise the switch request and send all the customers data along with the requested plan to the selected retailer.  * NOTE: as part of this call, you must provide a previously returned corellationId that is associated with this document and the returned plan options. Failure to do so will result in an error response. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndustryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    IndustryApi apiInstance = new IndustryApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID documentId = UUID.randomUUID(); // UUID | The documentId returned previously from an earlier call to /check or /entity or /document
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    Integer xFrankieBackground = 56; // Integer | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    SwitchRequest switchRequest = new SwitchRequest(); // SwitchRequest | 
    try {
      DocumentIndustryUtilitySwitchResultObject result = apiInstance.updateProcessIndustryUtilityDocumentSwitch(xFrankieCustomerID, documentId, xFrankieCustomerChildID, xFrankieBackground, switchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndustryApi#updateProcessIndustryUtilityDocumentSwitch");
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
| **documentId** | **UUID**| The documentId returned previously from an earlier call to /check or /entity or /document | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **xFrankieBackground** | **Integer**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] |
| **switchRequest** | [**SwitchRequest**](SwitchRequest.md)|  | [optional] |

### Return type

[**DocumentIndustryUtilitySwitchResultObject**](DocumentIndustryUtilitySwitchResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors. Returns the results directly from the service provider. Returns the results of the utility switch over directly from the service provider.  |  -  |
| **202** | The request was valid and can potentially be fulfilled. The Frankie service has now accepted responsibility for processing and we will either push the results to you, or send you a notification, depending on the request and your configuration. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **415** | For requests with payloads, an unsupported Content-Type was specified. The Frankie Financial API only supports a content type of application/json. |  -  |
| **422** | Unprocessable request. This can be triggered in a number of ways. * An attempt to force a check or scan to run, but there is insufficient data to be able to do so. * An attempt to run a utility comparison, or similar industry/document/entity specific scan or process on an unsupported document type (e.g. electricity comparison on a passport) Details of what is required will be in the issues list of the error response.  |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |

