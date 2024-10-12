# FrankieFinancialApi.EntityApi

All URIs are relative to *https://api.demo.frankiefinancial.io/compliance/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCheckEntity**](EntityApi.md#createCheckEntity) | **POST** /entity/new/verify/{checkType}/{resultLevel} | Create and Verify Entity
[**createCheckEntityPushToMobile**](EntityApi.md#createCheckEntityPushToMobile) | **POST** /entity/new/verify/pushToMobile | Create Entity and Push Self-Verification Link
[**createEntity**](EntityApi.md#createEntity) | **POST** /entity | Create New Entity.
[**createEntityGetIDVToken**](EntityApi.md#createEntityGetIDVToken) | **POST** /entity/new/idvalidate/getToken | Create Entity and Get IDV Token
[**deleteEntity**](EntityApi.md#deleteEntity) | **DELETE** /entity/{entityId} | Delete Entity
[**queryEntity**](EntityApi.md#queryEntity) | **GET** /entity/{entityId} | Retrieve Entity Details
[**queryEntityChecks**](EntityApi.md#queryEntityChecks) | **GET** /entity/{entityId}/checks | Retrieve Entity Verication Check Details 
[**queryEntityFull**](EntityApi.md#queryEntityFull) | **GET** /entity/{entityId}/full | Retrieve Entity Details and Document Scan Data 
[**searchEntity**](EntityApi.md#searchEntity) | **POST** /entity/search | Search for Entity
[**updateCheckClassResult**](EntityApi.md#updateCheckClassResult) | **POST** /entity/{entityId}/check/{checkId}/{checkClass}/{checkClassId} | Update Check Result State
[**updateCheckClassResults**](EntityApi.md#updateCheckClassResults) | **POST** /entity/{entityId}/check/{checkId}/{checkClass} | Update Check Result States (Batch)
[**updateCheckEntity**](EntityApi.md#updateCheckEntity) | **POST** /entity/{entityId}/verify/{checkType}/{resultLevel} | Update Entity and Verify Details
[**updateCheckEntityPushToMobile**](EntityApi.md#updateCheckEntityPushToMobile) | **POST** /entity/{entityId}/verify/pushToMobile | Update Entity and Push Self-Verification Link
[**updateEntity**](EntityApi.md#updateEntity) | **POST** /entity/{entityId} | Update Existing Entity.
[**updateEntityGetIDVToken**](EntityApi.md#updateEntityGetIDVToken) | **POST** /entity/{entityId}/idvalidate/getToken | Update Entity and Get IDV Token
[**updateEntityInitIDVProcess**](EntityApi.md#updateEntityInitIDVProcess) | **POST** /entity/{entityId}/idvalidate/initProcess | Update Entity and Initiate IDV Process
[**updateEntityState**](EntityApi.md#updateEntityState) | **POST** /entity/{entityId}/status | Update Entity States



## createCheckEntity

> CheckEntityCheckResultObject createCheckEntity(xFrankieCustomerID, checkType, resultLevel, entityDetails, opts)

Create and Verify Entity

Create an entity object. An entity object can be used to simply store data around a given identity. You can attach ID documents, scans, PDFs, photos, videos, etc to the entity if you wish and these may be processed later (using the /scan function) to extract useful information. Or you can manually supply the  information if you choose.  If the entity is successfully created, take the details and documents provided, and set about verifying them all. So for example, you might extract:  * The name from the entity.name object * The address from the entity.address object * The DoB..  All documents that are attached to the entity will also be verified (if possible).  You can also specify the level of detail returned using the resultLevel parameter. You can choose \&quot;summary\&quot; or \&quot;full\&quot;. For the \&quot;profile\&quot; check type you can also select \&quot;simple\&quot; to only get the entity profile result.  SPECIAL NOTE: A \&quot;Full\&quot; response includes details of all checks and how they map against each element, along with all the details of pep/sanctions/etc checks too.  Your account also needs to be configured to support a full response too (talk to your account manager for more information). If you&#39;re not configured for full responses, we&#39;ll only return summary level data regardless. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.EntityApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let checkType = "'default'"; // String | When creating a new check, you need to define the checks you wish to run.    The checkType is make up of a comma separated list of the types of check you wish to run. The order of the requested checks is not important, they will be re-ordered by the service and in some cases, depending on your account configuration, may be skipped.    The validation that is performed on the requested checks is to:   - ensure the check type is known   - is suitable for the type of entity (no KYC for organisations)   - disallow manual (mKYC) check with any other kind of KYC   - disallow mixing the \"profile\" check with any other kind of check.  The supported check types are:  Profile:   - \"profile\": By arrangement with Frankie we will create a \"profile\" check type that applies checks according to a recipe that you assign to the entity from a predefined set of profiles.      The profile to use will be taken from the entity.entityProfile field if set, or be run through a set of configurable rules to determine which one to use.      Profiles provide a pre-defined combination of individual checkTypes (see the list below). But they offer a lot more besides, including rules for determining default settings, inbuilt data aging and other configurable features.   They also allow for a new result set top be returned that provides a more detailed and useful breakdown of the check/verification process.      Entity Profiles are a recent feature (since v1.4.0) but are now the default checkType to use with Frankie Financial.  **Individual Check Types**  Whilst we strongly recommend the use of the \"profile\" checktype, it does map of any combination of the types below. If you wish to use these individually, please contact developer support for more details on how to use these effectively.  Entity Checks - One of:   - \"one_plus\": Checks name, address and DoB against a minimum of 1 data source. (also known as a 1+1)   - \"two_plus\": Checks name, address and DoB against a minimum of 2 independent data sources (also known as a 2+2)  ID Checks - One of:   - \"id\": Checks all of the identity documents, but not necessarily the entity itself independently. Use this in conjunction with a one_plus or two_plus for more.   - \"visa\":    ID Validate - One of:   - \"idvalidate\": Checks to see if photo ID has had OCR scanning, ID document validation and photo comparison run against it. Can be used in conjunction with any of the KYC/ID/AML checks.    Manual Check:   - \"manual\": (mKYC) Checks user has a sufficient amount of operator verified ID and will then \"pass\" all Entity and ID related checks.    Fraud Checks - One or more of:   - \"fraudlist\": Checks to see if the identity appears on any known fraud lists. Should be run after KYC/ID checks have passed.   - \"fraudcheck\": Checks external ID services to see if details appear in fraud detection services (e.g. EmailAge or FraudNet)    PEP Checks - One of:   - \"pep\": Will only run PEP/Sanctions checks (no identity verification)   - \"pep_media\": Will run PEP/Sanctions checks, as well as watchlist and adverse media checks. (no identity verification)      * NOTE: These checks will ONLY run if either the KYC/ID checks have been run prior, or it is the only check requested.    Custom:   - By arrangement with Frankie you can define your own KYC check type.      This will allow you to set the minimum number of matches for:     - name      - date of birth     - address     - government id      This allows for alternatives to the \"standard\" two_plus or one_plus (note, these can be overridden too). 
let resultLevel = "resultLevel_example"; // String | How much detail we return.   Acceptable values are:   * simple - Only available with \"profile\" check type. Returns just an EntityProfileResultObject (which is also included for \"profile\" checks at the other result levels), and a CheckEntityCheckResultObjectEntityResult with just the entity details but no separate results.   * summary   * full - You need to have your account configured for this. 
let entityDetails = new FrankieFinancialApi.EntityCheckDetailsObject(); // EntityCheckDetailsObject | The entity and any associated / additional information to be checked
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56 // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
};
apiInstance.createCheckEntity(xFrankieCustomerID, checkType, resultLevel, entityDetails, opts, (error, data, response) => {
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
 **checkType** | **String**| When creating a new check, you need to define the checks you wish to run.    The checkType is make up of a comma separated list of the types of check you wish to run. The order of the requested checks is not important, they will be re-ordered by the service and in some cases, depending on your account configuration, may be skipped.    The validation that is performed on the requested checks is to:   - ensure the check type is known   - is suitable for the type of entity (no KYC for organisations)   - disallow manual (mKYC) check with any other kind of KYC   - disallow mixing the \&quot;profile\&quot; check with any other kind of check.  The supported check types are:  Profile:   - \&quot;profile\&quot;: By arrangement with Frankie we will create a \&quot;profile\&quot; check type that applies checks according to a recipe that you assign to the entity from a predefined set of profiles.      The profile to use will be taken from the entity.entityProfile field if set, or be run through a set of configurable rules to determine which one to use.      Profiles provide a pre-defined combination of individual checkTypes (see the list below). But they offer a lot more besides, including rules for determining default settings, inbuilt data aging and other configurable features.   They also allow for a new result set top be returned that provides a more detailed and useful breakdown of the check/verification process.      Entity Profiles are a recent feature (since v1.4.0) but are now the default checkType to use with Frankie Financial.  **Individual Check Types**  Whilst we strongly recommend the use of the \&quot;profile\&quot; checktype, it does map of any combination of the types below. If you wish to use these individually, please contact developer support for more details on how to use these effectively.  Entity Checks - One of:   - \&quot;one_plus\&quot;: Checks name, address and DoB against a minimum of 1 data source. (also known as a 1+1)   - \&quot;two_plus\&quot;: Checks name, address and DoB against a minimum of 2 independent data sources (also known as a 2+2)  ID Checks - One of:   - \&quot;id\&quot;: Checks all of the identity documents, but not necessarily the entity itself independently. Use this in conjunction with a one_plus or two_plus for more.   - \&quot;visa\&quot;:    ID Validate - One of:   - \&quot;idvalidate\&quot;: Checks to see if photo ID has had OCR scanning, ID document validation and photo comparison run against it. Can be used in conjunction with any of the KYC/ID/AML checks.    Manual Check:   - \&quot;manual\&quot;: (mKYC) Checks user has a sufficient amount of operator verified ID and will then \&quot;pass\&quot; all Entity and ID related checks.    Fraud Checks - One or more of:   - \&quot;fraudlist\&quot;: Checks to see if the identity appears on any known fraud lists. Should be run after KYC/ID checks have passed.   - \&quot;fraudcheck\&quot;: Checks external ID services to see if details appear in fraud detection services (e.g. EmailAge or FraudNet)    PEP Checks - One of:   - \&quot;pep\&quot;: Will only run PEP/Sanctions checks (no identity verification)   - \&quot;pep_media\&quot;: Will run PEP/Sanctions checks, as well as watchlist and adverse media checks. (no identity verification)      * NOTE: These checks will ONLY run if either the KYC/ID checks have been run prior, or it is the only check requested.    Custom:   - By arrangement with Frankie you can define your own KYC check type.      This will allow you to set the minimum number of matches for:     - name      - date of birth     - address     - government id      This allows for alternatives to the \&quot;standard\&quot; two_plus or one_plus (note, these can be overridden too).  | [default to &#39;default&#39;]
 **resultLevel** | **String**| How much detail we return.   Acceptable values are:   * simple - Only available with \&quot;profile\&quot; check type. Returns just an EntityProfileResultObject (which is also included for \&quot;profile\&quot; checks at the other result levels), and a CheckEntityCheckResultObjectEntityResult with just the entity details but no separate results.   * summary   * full - You need to have your account configured for this.  | 
 **entityDetails** | [**EntityCheckDetailsObject**](EntityCheckDetailsObject.md)| The entity and any associated / additional information to be checked | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 

### Return type

[**CheckEntityCheckResultObject**](CheckEntityCheckResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCheckEntityPushToMobile

> AcceptedEntityResultObject createCheckEntityPushToMobile(xFrankieCustomerID, entityDetails, opts)

Create Entity and Push Self-Verification Link

Create an entity object and begin the process of verification after pushing a message to a mobile number.  The entity will receive a link on their mobile and will then be guided through a series of steps to capture and OCR scan their ID, and perform a selfie comparison. We&#39;ll then attempt to verify the data received and push a notification back to the calling customer.  At a minimum, you will need to supply the name and a MOBILE_PHONE document type.   SPECIAL NOTE: This will only ever return a 202 response if successfully accepted. You will need to ensure your account is configured for push notifications. Contact developer supprt to arrange this. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.EntityApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let entityDetails = new FrankieFinancialApi.EntityCheckDetailsObject(); // EntityCheckDetailsObject | The entity and any associated / additional information to be checked
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56, // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
  'nopush': true // Boolean | If set to true, then no SMS/email will be pushed. It will be up to the API caller to manage the delivery of the link. 
};
apiInstance.createCheckEntityPushToMobile(xFrankieCustomerID, entityDetails, opts, (error, data, response) => {
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
 **entityDetails** | [**EntityCheckDetailsObject**](EntityCheckDetailsObject.md)| The entity and any associated / additional information to be checked | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 
 **nopush** | **Boolean**| If set to true, then no SMS/email will be pushed. It will be up to the API caller to manage the delivery of the link.  | [optional] 

### Return type

[**AcceptedEntityResultObject**](AcceptedEntityResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createEntity

> EntityResultObject createEntity(xFrankieCustomerID, opts)

Create New Entity.

Create an entity object. An entity object can be used to simply store data around a given identity. You can attach ID documents, scans, PDFs, photos, videos, etc to the entity if you wish and these may be processed later (using the /scan function) to extract useful information. Or you can manually supply the  information if you choose.  Entity objects can be used to run a check, using the data held in the records. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.EntityApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'entity': new FrankieFinancialApi.EntityObject() // EntityObject | 
};
apiInstance.createEntity(xFrankieCustomerID, opts, (error, data, response) => {
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
 **entity** | [**EntityObject**](EntityObject.md)|  | [optional] 

### Return type

[**EntityResultObject**](EntityResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createEntityGetIDVToken

> EntityIDVResultObject createEntityGetIDVToken(xFrankieCustomerID, entityIDVDetails, opts)

Create Entity and Get IDV Token

Create an entity object and if successful, obtain a token for use in an ID Validation service SDK (web or native app)   At a minimum, you will need to supply:  - the entity familyName.   - the entity givenName    For best results, you should gather the DoB, address, ID document details as well before  calling the initProcess function.  SPECIAL NOTE 1: Tokens have a limited lifespan, typically only 1 hour. Make sure you&#39;ve used it or you will need to create another using update version of this function.   SPECIAL NOTE 2: This function will need to be followed up with a call to /entity/{id}/idvalidate/initProcess once you&#39;ve collected all your data in your app/web capture process. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.EntityApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let entityIDVDetails = new FrankieFinancialApi.EntityIDVDetailsObject(); // EntityIDVDetailsObject | The entity and required data to generate an IDV token
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example" // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
};
apiInstance.createEntityGetIDVToken(xFrankieCustomerID, entityIDVDetails, opts, (error, data, response) => {
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
 **entityIDVDetails** | [**EntityIDVDetailsObject**](EntityIDVDetailsObject.md)| The entity and required data to generate an IDV token | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 

### Return type

[**EntityIDVResultObject**](EntityIDVResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteEntity

> BasicStatusResultObject deleteEntity(xFrankieCustomerID, entityId, opts)

Delete Entity

Marks the entity as deleted in the system, and no further operations or general queries may be executed against it by the Customer. If another customer is presently relying on this data, it will still be available to them (but only in the partially anonymised form they originally had.  An entity and its related data is only completely deleted from the database when either:    - a) There are no more references to it (i.e. it has been DELETEd by all Customers relying on the data), and 12 months have passed.      - b) The actual consumer who owns the data makes a direct request. If this occurs, then all subscribing Customers will be notified that this entity has been removed and they will need to contact them if needed in order to update their own records again. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.EntityApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let entityId = "entityId_example"; // String | The entityId returned previously from an earlier call to /check or /entity
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56 // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
};
apiInstance.deleteEntity(xFrankieCustomerID, entityId, opts, (error, data, response) => {
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
 **entityId** | **String**| The entityId returned previously from an earlier call to /check or /entity | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 

### Return type

[**BasicStatusResultObject**](BasicStatusResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryEntity

> EntityResultObject queryEntity(xFrankieCustomerID, entityId, opts)

Retrieve Entity Details

Query the current status and details of a given entityId. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.EntityApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let entityId = "entityId_example"; // String | The entityId returned previously from an earlier call to /check or /entity
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example" // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
};
apiInstance.queryEntity(xFrankieCustomerID, entityId, opts, (error, data, response) => {
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
 **entityId** | **String**| The entityId returned previously from an earlier call to /check or /entity | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 

### Return type

[**EntityResultObject**](EntityResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryEntityChecks

> CheckEntityCheckResultObject queryEntityChecks(xFrankieCustomerID, entityId, opts)

Retrieve Entity Verication Check Details 

Get the complete list of all checks that have been performed upon a given entity and its documents, including the checks that have been performed by others (in those cases you just get the id, status and date run, none of the details). 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.EntityApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let entityId = "entityId_example"; // String | The entityId returned previously from an earlier call to /check or /entity
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'alldata': true // Boolean | Requests that literally all data should be included in the response to a \"get checks\" request. This is as opposed to a filtered view where expired results are by default not included for entities that have an assigned profile. 
};
apiInstance.queryEntityChecks(xFrankieCustomerID, entityId, opts, (error, data, response) => {
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
 **entityId** | **String**| The entityId returned previously from an earlier call to /check or /entity | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **alldata** | **Boolean**| Requests that literally all data should be included in the response to a \&quot;get checks\&quot; request. This is as opposed to a filtered view where expired results are by default not included for entities that have an assigned profile.  | [optional] 

### Return type

[**CheckEntityCheckResultObject**](CheckEntityCheckResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryEntityFull

> EntityResultObject queryEntityFull(xFrankieCustomerID, entityId, opts)

Retrieve Entity Details and Document Scan Data 

Query the current status and details of a given entityId. Also returns all attached document file data, not just the metadata. Equivalent to a get /document/{documentId}/full) 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.EntityApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let entityId = "entityId_example"; // String | The entityId returned previously from an earlier call to /check or /entity
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example" // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
};
apiInstance.queryEntityFull(xFrankieCustomerID, entityId, opts, (error, data, response) => {
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
 **entityId** | **String**| The entityId returned previously from an earlier call to /check or /entity | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 

### Return type

[**EntityResultObject**](EntityResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchEntity

> EntitySearchResultObject searchEntity(xFrankieCustomerID, searchEntity, opts)

Search for Entity

 Search for an existing entity that matches the criteria supplied  Criteria are supplied in the form of a populated entity object, with the name/address/DoB details supplied. You can also include documents that can be used to further refine your search (see the /document/search function for minimum requirements for a document search)  At an absolute minimum, you must supply one of the following combinations:    * name.familyName +   * name.givenNames      or      * name.familyName +   * one identityDocument object (that meets minimum criteria)    Obviously, the more data you provide, the better search results we can provide.  The service will return a list of matching entities with confidence levels.  If you are the \&quot;owner\&quot; of the entity - i.e. the same CustomerID and CustomerChildID (if relevant) - then the full details of the entity and any owned documents will be returned, except for the contents of any attached scans.  If you are not the owner of the entity (or linked documents), then just the ID and confidence level is returned. You can still use this ID to retrieve any check results (see GET  /entity/{entityId}/checks and GET /document/{documentId}/checks)  Note: This functionality must be enabled by Frankie administrators. Please contact your sales representative if you wish to discuss this. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.EntityApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let searchEntity = new FrankieFinancialApi.EntityObject(); // EntityObject | An entity object with the parameters you wish to search on. 
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example" // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
};
apiInstance.searchEntity(xFrankieCustomerID, searchEntity, opts, (error, data, response) => {
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
 **searchEntity** | [**EntityObject**](EntityObject.md)| An entity object with the parameters you wish to search on.  | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 

### Return type

[**EntitySearchResultObject**](EntitySearchResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCheckClassResult

> CheckEntityCheckResultObject updateCheckClassResult(xFrankieCustomerID, entityId, checkId, checkClass, checkClassId, status, opts)

Update Check Result State

Internal only  Update a given KYC or AML check result status in order to force a re-evaluation of the overall check result. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.EntityApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let entityId = "entityId_example"; // String | The entityId returned previously from an earlier call to /check or /entity
let checkId = "checkId_example"; // String | The checkId returned previously from an earlier call to *_/verify
let checkClass = "checkClass_example"; // String | Specify which check Class this action will apply to (PRO, BCRO etc.). Valid values are:   - \"pro\": Update a Process Result Object   - \"bcro\": Update a Background Check Result Object. The class IDs in the request must be the IDs from Background Check Result Object Containers.   - \"fraudlist\": Update a fraud list Process Result Object. The class IDs in the request must be check sources from fraudlist Process Result Objects. 
let checkClassId = "checkClassId_example"; // String | A PRO/BCRO ID 
let status = "status_example"; // String | Set the new status of the Check Class (PRO/BCRO). Valid values are:   - \"unknown\"   - \"true_positive\"   - \"true_positive_accept\"   - \"true_positive_reject\"   - \"false_positive\"   - \"stale\" 
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'undo': true // Boolean | Undo a prior operation. 
};
apiInstance.updateCheckClassResult(xFrankieCustomerID, entityId, checkId, checkClass, checkClassId, status, opts, (error, data, response) => {
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
 **entityId** | **String**| The entityId returned previously from an earlier call to /check or /entity | 
 **checkId** | **String**| The checkId returned previously from an earlier call to *_/verify | 
 **checkClass** | **String**| Specify which check Class this action will apply to (PRO, BCRO etc.). Valid values are:   - \&quot;pro\&quot;: Update a Process Result Object   - \&quot;bcro\&quot;: Update a Background Check Result Object. The class IDs in the request must be the IDs from Background Check Result Object Containers.   - \&quot;fraudlist\&quot;: Update a fraud list Process Result Object. The class IDs in the request must be check sources from fraudlist Process Result Objects.  | 
 **checkClassId** | **String**| A PRO/BCRO ID  | 
 **status** | **String**| Set the new status of the Check Class (PRO/BCRO). Valid values are:   - \&quot;unknown\&quot;   - \&quot;true_positive\&quot;   - \&quot;true_positive_accept\&quot;   - \&quot;true_positive_reject\&quot;   - \&quot;false_positive\&quot;   - \&quot;stale\&quot;  | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **undo** | **Boolean**| Undo a prior operation.  | [optional] 

### Return type

[**CheckEntityCheckResultObject**](CheckEntityCheckResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCheckClassResults

> CheckEntityCheckResultObject updateCheckClassResults(xFrankieCustomerID, entityId, checkId, checkClass, checkResultUpdate, opts)

Update Check Result States (Batch)

Internal only  Update a given set of KYC and/or AML check result statuses in order to force a re-evaluation of the overall check result. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.EntityApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let entityId = "entityId_example"; // String | The entityId returned previously from an earlier call to /check or /entity
let checkId = "checkId_example"; // String | The checkId returned previously from an earlier call to *_/verify
let checkClass = "checkClass_example"; // String | Specify which check Class this action will apply to (PRO, BCRO etc.). Valid values are:   - \"pro\": Update a Process Result Object   - \"bcro\": Update a Background Check Result Object. The class IDs in the request must be the IDs from Background Check Result Object Containers.   - \"fraudlist\": Update a fraud list Process Result Object. The class IDs in the request must be check sources from fraudlist Process Result Objects. 
let checkResultUpdate = new FrankieFinancialApi.CheckResultUpdateObject(); // CheckResultUpdateObject | The check result status change details to apply
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example" // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
};
apiInstance.updateCheckClassResults(xFrankieCustomerID, entityId, checkId, checkClass, checkResultUpdate, opts, (error, data, response) => {
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
 **entityId** | **String**| The entityId returned previously from an earlier call to /check or /entity | 
 **checkId** | **String**| The checkId returned previously from an earlier call to *_/verify | 
 **checkClass** | **String**| Specify which check Class this action will apply to (PRO, BCRO etc.). Valid values are:   - \&quot;pro\&quot;: Update a Process Result Object   - \&quot;bcro\&quot;: Update a Background Check Result Object. The class IDs in the request must be the IDs from Background Check Result Object Containers.   - \&quot;fraudlist\&quot;: Update a fraud list Process Result Object. The class IDs in the request must be check sources from fraudlist Process Result Objects.  | 
 **checkResultUpdate** | [**CheckResultUpdateObject**](CheckResultUpdateObject.md)| The check result status change details to apply | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 

### Return type

[**CheckEntityCheckResultObject**](CheckEntityCheckResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCheckEntity

> CheckEntityCheckResultObject updateCheckEntity(xFrankieCustomerID, entityId, checkType, resultLevel, entityDetails, opts)

Update Entity and Verify Details

Take the details and documents provided in the entity, and set about verifying them all. So for example, you might extract:  * The name from the entity.name object * The address from the entity.address object * The DoB..  All documents that are presently attached to the entity will also be verified (if requested)  You can also specify the level of detail returned using the resultLevel parameter. You can choose \&quot;summary\&quot; or \&quot;full\&quot;. For the \&quot;profile\&quot; check type you can also select \&quot;simple\&quot; to only get the entity profile result.  SPECIAL NOTE: A \&quot;Full\&quot; response includes details of all checks and how they map against each element, along with all the details of pep/sanctions/etc checks too.  Your account also needs to be configured to support a full response too (talk to your account manager for more information). If you&#39;re not configured for full responses, we&#39;ll only return summary level data regardless. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.EntityApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let entityId = "entityId_example"; // String | The entityId returned previously from an earlier call to /check or /entity
let checkType = "'default'"; // String | When creating a new check, you need to define the checks you wish to run.    The checkType is make up of a comma separated list of the types of check you wish to run. The order of the requested checks is not important, they will be re-ordered by the service and in some cases, depending on your account configuration, may be skipped.    The validation that is performed on the requested checks is to:   - ensure the check type is known   - is suitable for the type of entity (no KYC for organisations)   - disallow manual (mKYC) check with any other kind of KYC   - disallow mixing the \"profile\" check with any other kind of check.  The supported check types are:  Profile:   - \"profile\": By arrangement with Frankie we will create a \"profile\" check type that applies checks according to a recipe that you assign to the entity from a predefined set of profiles.      The profile to use will be taken from the entity.entityProfile field if set, or be run through a set of configurable rules to determine which one to use.      Profiles provide a pre-defined combination of individual checkTypes (see the list below). But they offer a lot more besides, including rules for determining default settings, inbuilt data aging and other configurable features.   They also allow for a new result set top be returned that provides a more detailed and useful breakdown of the check/verification process.      Entity Profiles are a recent feature (since v1.4.0) but are now the default checkType to use with Frankie Financial.  **Individual Check Types**  Whilst we strongly recommend the use of the \"profile\" checktype, it does map of any combination of the types below. If you wish to use these individually, please contact developer support for more details on how to use these effectively.  Entity Checks - One of:   - \"one_plus\": Checks name, address and DoB against a minimum of 1 data source. (also known as a 1+1)   - \"two_plus\": Checks name, address and DoB against a minimum of 2 independent data sources (also known as a 2+2)  ID Checks - One of:   - \"id\": Checks all of the identity documents, but not necessarily the entity itself independently. Use this in conjunction with a one_plus or two_plus for more.   - \"visa\":    ID Validate - One of:   - \"idvalidate\": Checks to see if photo ID has had OCR scanning, ID document validation and photo comparison run against it. Can be used in conjunction with any of the KYC/ID/AML checks.    Manual Check:   - \"manual\": (mKYC) Checks user has a sufficient amount of operator verified ID and will then \"pass\" all Entity and ID related checks.    Fraud Checks - One or more of:   - \"fraudlist\": Checks to see if the identity appears on any known fraud lists. Should be run after KYC/ID checks have passed.   - \"fraudcheck\": Checks external ID services to see if details appear in fraud detection services (e.g. EmailAge or FraudNet)    PEP Checks - One of:   - \"pep\": Will only run PEP/Sanctions checks (no identity verification)   - \"pep_media\": Will run PEP/Sanctions checks, as well as watchlist and adverse media checks. (no identity verification)      * NOTE: These checks will ONLY run if either the KYC/ID checks have been run prior, or it is the only check requested.    Custom:   - By arrangement with Frankie you can define your own KYC check type.      This will allow you to set the minimum number of matches for:     - name      - date of birth     - address     - government id      This allows for alternatives to the \"standard\" two_plus or one_plus (note, these can be overridden too). 
let resultLevel = "resultLevel_example"; // String | How much detail we return.   Acceptable values are:   * simple - Only available with \"profile\" check type. Returns just an EntityProfileResultObject (which is also included for \"profile\" checks at the other result levels), and a CheckEntityCheckResultObjectEntityResult with just the entity details but no separate results.   * summary   * full - You need to have your account configured for this. 
let entityDetails = new FrankieFinancialApi.EntityCheckDetailsObject(); // EntityCheckDetailsObject | The entity to be checked
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56, // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
  'force': true, // Boolean | Force the verification to run, overriding any data aging or past check 
  'noInvalidate': true // Boolean | Disable check result invalidation for this update request. 
};
apiInstance.updateCheckEntity(xFrankieCustomerID, entityId, checkType, resultLevel, entityDetails, opts, (error, data, response) => {
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
 **entityId** | **String**| The entityId returned previously from an earlier call to /check or /entity | 
 **checkType** | **String**| When creating a new check, you need to define the checks you wish to run.    The checkType is make up of a comma separated list of the types of check you wish to run. The order of the requested checks is not important, they will be re-ordered by the service and in some cases, depending on your account configuration, may be skipped.    The validation that is performed on the requested checks is to:   - ensure the check type is known   - is suitable for the type of entity (no KYC for organisations)   - disallow manual (mKYC) check with any other kind of KYC   - disallow mixing the \&quot;profile\&quot; check with any other kind of check.  The supported check types are:  Profile:   - \&quot;profile\&quot;: By arrangement with Frankie we will create a \&quot;profile\&quot; check type that applies checks according to a recipe that you assign to the entity from a predefined set of profiles.      The profile to use will be taken from the entity.entityProfile field if set, or be run through a set of configurable rules to determine which one to use.      Profiles provide a pre-defined combination of individual checkTypes (see the list below). But they offer a lot more besides, including rules for determining default settings, inbuilt data aging and other configurable features.   They also allow for a new result set top be returned that provides a more detailed and useful breakdown of the check/verification process.      Entity Profiles are a recent feature (since v1.4.0) but are now the default checkType to use with Frankie Financial.  **Individual Check Types**  Whilst we strongly recommend the use of the \&quot;profile\&quot; checktype, it does map of any combination of the types below. If you wish to use these individually, please contact developer support for more details on how to use these effectively.  Entity Checks - One of:   - \&quot;one_plus\&quot;: Checks name, address and DoB against a minimum of 1 data source. (also known as a 1+1)   - \&quot;two_plus\&quot;: Checks name, address and DoB against a minimum of 2 independent data sources (also known as a 2+2)  ID Checks - One of:   - \&quot;id\&quot;: Checks all of the identity documents, but not necessarily the entity itself independently. Use this in conjunction with a one_plus or two_plus for more.   - \&quot;visa\&quot;:    ID Validate - One of:   - \&quot;idvalidate\&quot;: Checks to see if photo ID has had OCR scanning, ID document validation and photo comparison run against it. Can be used in conjunction with any of the KYC/ID/AML checks.    Manual Check:   - \&quot;manual\&quot;: (mKYC) Checks user has a sufficient amount of operator verified ID and will then \&quot;pass\&quot; all Entity and ID related checks.    Fraud Checks - One or more of:   - \&quot;fraudlist\&quot;: Checks to see if the identity appears on any known fraud lists. Should be run after KYC/ID checks have passed.   - \&quot;fraudcheck\&quot;: Checks external ID services to see if details appear in fraud detection services (e.g. EmailAge or FraudNet)    PEP Checks - One of:   - \&quot;pep\&quot;: Will only run PEP/Sanctions checks (no identity verification)   - \&quot;pep_media\&quot;: Will run PEP/Sanctions checks, as well as watchlist and adverse media checks. (no identity verification)      * NOTE: These checks will ONLY run if either the KYC/ID checks have been run prior, or it is the only check requested.    Custom:   - By arrangement with Frankie you can define your own KYC check type.      This will allow you to set the minimum number of matches for:     - name      - date of birth     - address     - government id      This allows for alternatives to the \&quot;standard\&quot; two_plus or one_plus (note, these can be overridden too).  | [default to &#39;default&#39;]
 **resultLevel** | **String**| How much detail we return.   Acceptable values are:   * simple - Only available with \&quot;profile\&quot; check type. Returns just an EntityProfileResultObject (which is also included for \&quot;profile\&quot; checks at the other result levels), and a CheckEntityCheckResultObjectEntityResult with just the entity details but no separate results.   * summary   * full - You need to have your account configured for this.  | 
 **entityDetails** | [**EntityCheckDetailsObject**](EntityCheckDetailsObject.md)| The entity to be checked | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 
 **force** | **Boolean**| Force the verification to run, overriding any data aging or past check  | [optional] 
 **noInvalidate** | **Boolean**| Disable check result invalidation for this update request.  | [optional] 

### Return type

[**CheckEntityCheckResultObject**](CheckEntityCheckResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCheckEntityPushToMobile

> AcceptedEntityResultObject updateCheckEntityPushToMobile(xFrankieCustomerID, entityId, entityDetails, opts)

Update Entity and Push Self-Verification Link

Update an existing entity object and begin the process of verification after pushing a message to a mobile number.  The entity will receive a link on their mobile and will then be guided through a series of steps to capture and OCR scan their ID, and perform a selfie comparison. We&#39;ll then attempt to verify the data received and push a notification back to the calling customer.  At a minimum, you will need to supply the name and a MOBILE_PHONE document type.         If you wish to skip the detail capture and jump straight to the ID and selfie capture, the append the call with the ?phase&#x3D;2 parameter.   SPECIAL NOTE: This will only ever return a 202 response if successfully accepted. You will need to ensure your account is configured for push notifications. Contact developer supprt to arrange this. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.EntityApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let entityId = "entityId_example"; // String | The entityId returned previously from an earlier call to /check or /entity
let entityDetails = new FrankieFinancialApi.EntityCheckDetailsObject(); // EntityCheckDetailsObject | The entity and any associated / additional information to be checked
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56, // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
  'nopush': true, // Boolean | If set to true, then no SMS/email will be pushed. It will be up to the API caller to manage the delivery of the link. 
  'phase': 56 // Number | Set the Push To Mobile phase.  Currently supported values: - 2 
};
apiInstance.updateCheckEntityPushToMobile(xFrankieCustomerID, entityId, entityDetails, opts, (error, data, response) => {
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
 **entityId** | **String**| The entityId returned previously from an earlier call to /check or /entity | 
 **entityDetails** | [**EntityCheckDetailsObject**](EntityCheckDetailsObject.md)| The entity and any associated / additional information to be checked | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 
 **nopush** | **Boolean**| If set to true, then no SMS/email will be pushed. It will be up to the API caller to manage the delivery of the link.  | [optional] 
 **phase** | **Number**| Set the Push To Mobile phase.  Currently supported values: - 2  | [optional] 

### Return type

[**AcceptedEntityResultObject**](AcceptedEntityResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEntity

> EntityResultObject updateEntity(xFrankieCustomerID, entityId, entity, opts)

Update Existing Entity.

Using a previously uploaded but incomplete Entity, you can optionally supply updated details (such as corrections on a previous address), along with one or more additional ID docs/scans (e.g. new documents to parse, etc). 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.EntityApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let entityId = "entityId_example"; // String | The entityId returned previously from an earlier call to /check or /entity
let entity = new FrankieFinancialApi.EntityObject(); // EntityObject | The entity to be updated
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56, // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
  'noInvalidate': true // Boolean | Disable check result invalidation for this update request. 
};
apiInstance.updateEntity(xFrankieCustomerID, entityId, entity, opts, (error, data, response) => {
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
 **entityId** | **String**| The entityId returned previously from an earlier call to /check or /entity | 
 **entity** | [**EntityObject**](EntityObject.md)| The entity to be updated | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 
 **noInvalidate** | **Boolean**| Disable check result invalidation for this update request.  | [optional] 

### Return type

[**EntityResultObject**](EntityResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEntityGetIDVToken

> EntityIDVResultObject updateEntityGetIDVToken(xFrankieCustomerID, entityId, entityIDVDetails, opts)

Update Entity and Get IDV Token

Update an entity object and if successful, obtain a token for use in an ID Validation service SDK (web or native app)   At a minimum, the entity will need to have a name. For best results, you should gather the DoB, address, ID document details as well before calling the initProcess function.  SPECIAL NOTE 1: Tokens have a limited lifespan, typically only 1 hour. Make sure you&#39;ve used it or you will need to create another using update version of this function.   SPECIAL NOTE 2: This function will need to be followed up with a call to /entity/{id}/idvalidate/initProcess once you&#39;ve collected all your data in your app/web capture process. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.EntityApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let entityId = "entityId_example"; // String | The entityId returned previously from an earlier call to /check or /entity
let entityIDVDetails = new FrankieFinancialApi.EntityIDVDetailsObject(); // EntityIDVDetailsObject | The entity to update and required data to generate an IDV token
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example" // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
};
apiInstance.updateEntityGetIDVToken(xFrankieCustomerID, entityId, entityIDVDetails, opts, (error, data, response) => {
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
 **entityId** | **String**| The entityId returned previously from an earlier call to /check or /entity | 
 **entityIDVDetails** | [**EntityIDVDetailsObject**](EntityIDVDetailsObject.md)| The entity to update and required data to generate an IDV token | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 

### Return type

[**EntityIDVResultObject**](EntityIDVResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEntityInitIDVProcess

> EntityIDVResultObject updateEntityInitIDVProcess(xFrankieCustomerID, entityId, entityDetails, opts)

Update Entity and Initiate IDV Process

Update an entity object and if successful, start the process of downloading the captured data and processing the reports and results of the ID validation process.   At a minimum, the entity will need to have a name. For best results, you should gather the DoB, address, ID document details as well before calling this initProcess function, or supply the details as part of this update. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.EntityApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let entityId = "entityId_example"; // String | The entityId returned previously from an earlier call to /check or /entity
let entityDetails = new FrankieFinancialApi.EntityCheckDetailsObject(); // EntityCheckDetailsObject | The entity to update
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example" // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
};
apiInstance.updateEntityInitIDVProcess(xFrankieCustomerID, entityId, entityDetails, opts, (error, data, response) => {
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
 **entityId** | **String**| The entityId returned previously from an earlier call to /check or /entity | 
 **entityDetails** | [**EntityCheckDetailsObject**](EntityCheckDetailsObject.md)| The entity to update | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 

### Return type

[**EntityIDVResultObject**](EntityIDVResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEntityState

> CheckEntityCheckResultObject updateEntityState(xFrankieCustomerID, entityId, opts)

Update Entity States

Internal only  Add a special internal &#39;entity result&#39; to superceed any previous real checks until the next one. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.EntityApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let entityId = "entityId_example"; // String | The entityId returned previously from an earlier call to /check or /entity
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'set': "set_example", // String | The status of an entity. Valid values are:   - \"wait\": Waiting for new details from entity.   - \"fail\": Manually fail the onboarding process.   - \"archived\": Hide entity from on onboarding.   - \"clear\": Remove any of the above manual states as well as any manual risk.   - \"inactive\": Hide entity and prevent any further operations on it. Cannot be cleared. 
  'risk': "risk_example", // String | The risk override setting for an entity. This value will be used until a verify result updates a real risk factor. Valid values are:   - \"low\"   - \"medium\"   - \"high\"   - \"unacceptable\"   - \"significant\" 
  'comment': "comment_example" // String | A comment describing the reason for a request. 
};
apiInstance.updateEntityState(xFrankieCustomerID, entityId, opts, (error, data, response) => {
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
 **entityId** | **String**| The entityId returned previously from an earlier call to /check or /entity | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **set** | **String**| The status of an entity. Valid values are:   - \&quot;wait\&quot;: Waiting for new details from entity.   - \&quot;fail\&quot;: Manually fail the onboarding process.   - \&quot;archived\&quot;: Hide entity from on onboarding.   - \&quot;clear\&quot;: Remove any of the above manual states as well as any manual risk.   - \&quot;inactive\&quot;: Hide entity and prevent any further operations on it. Cannot be cleared.  | [optional] 
 **risk** | **String**| The risk override setting for an entity. This value will be used until a verify result updates a real risk factor. Valid values are:   - \&quot;low\&quot;   - \&quot;medium\&quot;   - \&quot;high\&quot;   - \&quot;unacceptable\&quot;   - \&quot;significant\&quot;  | [optional] 
 **comment** | **String**| A comment describing the reason for a request.  | [optional] 

### Return type

[**CheckEntityCheckResultObject**](CheckEntityCheckResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

