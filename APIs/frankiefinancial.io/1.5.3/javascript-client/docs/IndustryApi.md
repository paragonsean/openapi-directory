# FrankieFinancialApi.IndustryApi

All URIs are relative to *https://api.demo.frankiefinancial.io/compliance/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createProcessIndustryUtilityDocument**](IndustryApi.md#createProcessIndustryUtilityDocument) | **POST** /document/new/utility/process/compare | Create Document and Run Utility Price Comparison.
[**updateProcessIndustryUtilityDocument**](IndustryApi.md#updateProcessIndustryUtilityDocument) | **POST** /document/{documentId}/utility/process/compare | Update Document and Run Utility Price Comparison.
[**updateProcessIndustryUtilityDocumentConsent**](IndustryApi.md#updateProcessIndustryUtilityDocumentConsent) | **POST** /document/{documentId}/utility/process/consent | Provide Explicit Consent to Switch Utility Plans.
[**updateProcessIndustryUtilityDocumentSwitch**](IndustryApi.md#updateProcessIndustryUtilityDocumentSwitch) | **POST** /document/{documentId}/utility/process/switch | Initiate Switching of Utility Plan.



## createProcessIndustryUtilityDocument

> DocumentIndustryUtilityProcessResultObject createProcessIndustryUtilityDocument(xFrankieCustomerID, opts)

Create Document and Run Utility Price Comparison.

Create a document object. This is then processed to extract useful information, just like a normal OCR scan. The service will then push the document through an industry specific comparison process, where the details are used to find a better plan, based on the bill.  100&#39;s of datapoints are accurately extracted from the uploaded document. This data is then used to compare the bill against the whole market. A personalised comparison is returned that is a best fit for the customer&#39;s energy profile.  * NOTE: It is expected that the type of document being uploaded will be a PDF and the idType is UTILITY_BILL. (These values will be set automatically if not supplied).    You can optionally include the utility name (e.g. Origin Energy) in the idSubType if you wish. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.IndustryApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56, // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
  'planLimit': 30, // Number | The maximum number of plans to return
  'document': new FrankieFinancialApi.IdentityDocumentObject() // IdentityDocumentObject | 
};
apiInstance.createProcessIndustryUtilityDocument(xFrankieCustomerID, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 
 **planLimit** | **Number**| The maximum number of plans to return | [optional] [default to 30]
 **document** | [**IdentityDocumentObject**](IdentityDocumentObject.md)|  | [optional] 

### Return type

[**DocumentIndustryUtilityProcessResultObject**](DocumentIndustryUtilityProcessResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateProcessIndustryUtilityDocument

> DocumentIndustryUtilityProcessResultObject updateProcessIndustryUtilityDocument(xFrankieCustomerID, documentId, opts)

Update Document and Run Utility Price Comparison.

Using a previously uploaded but incomplete document, you can optionally supply updated details or simply request that the document be re-processed through the industry comparison service.   100&#39;s of datapoints are accurately extracted from the uploaded document. This data is then used to compare the bill against the whole market. A personalised comparison is returned that is a best fit for the customer&#39;s energy profile.  * NOTE: It is expected that the type of document being uploaded will be a PDF and the idType is UTILITY_BILL. (These values will be set automatically if not supplied).    You can optionally include the utility name (e.g. Origin Energy) in the idSubType if you wish. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.IndustryApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let documentId = "documentId_example"; // String | The documentId returned previously from an earlier call to /check or /entity or /document
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56, // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
  'planLimit': 30, // Number | The maximum number of plans to return
  'document': new FrankieFinancialApi.IdentityDocumentObject() // IdentityDocumentObject | 
};
apiInstance.updateProcessIndustryUtilityDocument(xFrankieCustomerID, documentId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **documentId** | **String**| The documentId returned previously from an earlier call to /check or /entity or /document | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 
 **planLimit** | **Number**| The maximum number of plans to return | [optional] [default to 30]
 **document** | [**IdentityDocumentObject**](IdentityDocumentObject.md)|  | [optional] 

### Return type

[**DocumentIndustryUtilityProcessResultObject**](DocumentIndustryUtilityProcessResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateProcessIndustryUtilityDocumentConsent

> DocumentIndustryUtilityConsentResultObject updateProcessIndustryUtilityDocumentConsent(xFrankieCustomerID, documentId, opts)

Provide Explicit Consent to Switch Utility Plans.

Using a previously uploaded and processed document, the user must provide explicit consent before being able to call the /switch function.   Before entering into a contract with a new energy retailer, consumers are first obliged to review the retailer&#39;s contractual terms and conditions, confirm they understand these terms as well as give explicit, informed consent (EIC) for the switch to occur. This API call retrieves all information        that must be displayed in order for a compliant EIC to be captured from a consumer.  * NOTE: as part of this call, you must provide a previously returned corellationId that is associated with this document and the returned plan options. Failure to do so will result in an error response. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.IndustryApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let documentId = "documentId_example"; // String | The documentId returned previously from an earlier call to /check or /entity or /document
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56, // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
  'consentRequest': new FrankieFinancialApi.EICRequest() // EICRequest | 
};
apiInstance.updateProcessIndustryUtilityDocumentConsent(xFrankieCustomerID, documentId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **documentId** | **String**| The documentId returned previously from an earlier call to /check or /entity or /document | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 
 **consentRequest** | [**EICRequest**](EICRequest.md)|  | [optional] 

### Return type

[**DocumentIndustryUtilityConsentResultObject**](DocumentIndustryUtilityConsentResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateProcessIndustryUtilityDocumentSwitch

> DocumentIndustryUtilitySwitchResultObject updateProcessIndustryUtilityDocumentSwitch(xFrankieCustomerID, documentId, opts)

Initiate Switching of Utility Plan.

Using a previously uploaded and processed document, the user must provide explicit consent before being able to call the /switch function.   The bill payer has uploaded their current bill, selected a new plan, accepted the terms and conditions and given their consent for the switch to occur. This API call will finalise the switch request and send all the customers data along with the requested plan to the selected retailer.  * NOTE: as part of this call, you must provide a previously returned corellationId that is associated with this document and the returned plan options. Failure to do so will result in an error response. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.IndustryApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let documentId = "documentId_example"; // String | The documentId returned previously from an earlier call to /check or /entity or /document
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56, // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
  'switchRequest': new FrankieFinancialApi.SwitchRequest() // SwitchRequest | 
};
apiInstance.updateProcessIndustryUtilityDocumentSwitch(xFrankieCustomerID, documentId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **documentId** | **String**| The documentId returned previously from an earlier call to /check or /entity or /document | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 
 **switchRequest** | [**SwitchRequest**](SwitchRequest.md)|  | [optional] 

### Return type

[**DocumentIndustryUtilitySwitchResultObject**](DocumentIndustryUtilitySwitchResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

