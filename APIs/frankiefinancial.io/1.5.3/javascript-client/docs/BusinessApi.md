# FrankieFinancialApi.BusinessApi

All URIs are relative to *https://api.demo.frankiefinancial.io/compliance/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**businessOwnershipQuery**](BusinessApi.md#businessOwnershipQuery) | **POST** /business/ownership/query | Create Business Entity and Query UBO (AUS Only)
[**checkOrganisation**](BusinessApi.md#checkOrganisation) | **POST** /business/{entityId}/verify | Run KYC/AML Checks on Organisation and/or Associated Individuals.
[**internationalBusinessProfile**](BusinessApi.md#internationalBusinessProfile) | **POST** /business/international/profile | Retrieve a business profile from any country (AUS included).
[**internationalBusinessSearch**](BusinessApi.md#internationalBusinessSearch) | **POST** /business/international/search | Search for a business from any country (AUS included).
[**runBusinessReports**](BusinessApi.md#runBusinessReports) | **POST** /business/reports | Run Report(s) against a new or existing organisation entity (AUS Only).



## businessOwnershipQuery

> OrganisationCheckResponseObject businessOwnershipQuery(xFrankieCustomerID, query, opts)

Create Business Entity and Query UBO (AUS Only)

Process a request for ownership details for an Australian organisation.  See below for more generic international queries.  At a minimum, you just need to supply an ACN or ABN and we can retrieve the rest. You also have the option of supplying company name, type (as per ABR types) and both ABN/ACN and we&#39;ll attempt to verfy that that data matches what is on record before attempting any further verification and validation.  KYC/AML for a selection of entities associated with an organisation and/or the organisation itself can optionally be run, but not by default. To enable KYC/AML checks one or more entity categories must be provided. If such a list of entity categories is given then default checks based on configuration will be run for those categories. If a check type is also provided in the request then that type will be used for entities representing individual entities, and the AML subset of that check will be used for organisations if any. Specifying a check type without an entity category will result in an error.  NOTE: This query will always run asynchronously and you will only ever be returned a 202 ACCEPT response, or an error. Results will be pushed using the Push Notification API below and you will be able to retrieve the results using the Retrieve API.  We have supplied the 200 response in the definition below only so what will be sent to you when you later retrieve the details.  More details on how to use this API and interpret the results can be found here:      https://apidocs.frankiefinancial.com/docs/which-function-to-use 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.BusinessApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let query = new FrankieFinancialApi.OwnershipQuery(); // OwnershipQuery | The organisation to be queried. An entity object that must have an organisation object with at least one organisation number. 
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'checkType': ["null"], // [String] | When creating a new check, we need to define the checks we wish to run. If this parameter is not supplied then the check will be based on a configured check type for each entity category.    The checkType is make up of a comma separated list of the types of check we wish to run.  The order is important, and must be of the form:   - Entity Check (if you're running this). Choose one from the available options   - ID Check (If you want this)   - PEP Checks (again if you want this, choose one of the options)  Entity Checks - One of:   - \"one_plus\": Checks name, address and DoB against a minimum of 1 data source. (also known as a 1+1)   - \"two_plus\": Checks name, address and DoB against a minimum of 2 independent data sources (also known as a 2+2)  ID Checks - One of:   - \"id\": Checks all of the identity documents, but not necessarily the entity itself independently. Use this in conjunction with a one_plus or two_plus for more.    Fraud Checks - One or more  of:   - \"fraudlist\": Checks to see if the identity appears on any known fraud lists. Should be run after KYC/ID checks have passed.   - \"fraudid\": Checks external ID services to see if details appear in fraud detection services (e.g. EmailAge or FraudNet)    PEP Checks - One of:   - \"pep\": Will only run PEP/Sanctions checks (no identity verification)   - \"pep_media\": Will run PEP/Sanctions checks, as well as watchlist and adverse media checks. (no identity verification)      * NOTE: These checks will ONLY run if either the KYC/ID checks have been run prior, or it is the only check requested.    Pre-defined combinations:   - \"full\": equivalent to \"two_plus,id,pep_media\" or \"pep_media\" if the target is an organisation.   - \"default\": Currently defined as \"two_plus,id\" or \"pep\" if the target is an organisation.  Custom:   - By arrangement with Frankie you can define your own KYC check type.      This will allow you to set the minimum number of matches for:     - name      - date of birth     - address     - government id      This allows for alternatives to the \"standard\" two_plus or one_plus (note, these can be overridden too).    Profile:   - \"profile\": By arrangement with Frankie you can have a \"profile\" check type that applies checks according to a profile that you assign to the entity from a predefined set of profiles.      The profile to use will be taken from the entity.entityProfile field if set, or be run through a set of configurable rules to determine which one to use.      Profiles act a little like the Pre-defined combinations above in that they can map to a defined list. But they offer a lot more besides, including rules for determining default settings, inbuild data aging and other configurable features.   They also allow for a new result set top be returned that provides a more detailed and useful breakdown of the check/verification process.      Entity Profiles are the future of checks with Frankie Financial. 
  'entityCategories': ["null"], // [String] | A comma separated list that specifies the categories of entities associated with the target organisation that will be checked.    - organisation - Just the organisation itself.   - ubos - All ultimate beneficial owners.   - pseudo_ubos - Use an alterntive category when an organisation has no actual UBOs. The actual category to use is defined via configuration, default is no alterntive category.   - direct_owners - All direct owners of the company, both organisations and individuals, may include UBOs for for simple ownership.   - officers - All officers of the company   - officers_directors - All directors of the company   - officers_other - All non-director officers of the company   - all - All direct and indirect owners, both organisations and individuals (including UBOs), and officers of all organisations. 
  'resultLevel': "'summary'", // String | The result level allows you to specify the level of detail returned for the entity check. You can choose summary or full. 
  'validation': "validation_example", // String | Should a validation check be run before the ownership query. The default is specified via configuration. The validation checks to see if the provided organisation is suitable for an ownership query by looking for the ACN in public data sources.  Options are: - \"on\": Validate only when ACN is not provided. This is the typical default. - \"acn\": Validate even if ACN is provided. - \"only\": Like \"acn\" but only do validation query, don't proceed with ownership query. This option cannot be set as the default via configuration. - \"off\": Never validate. The Ownership query will then fail if an ACN is not provided. 
  'generateReport': "generateReport_example", // String | The type of human readable report, if any, to generate based on the ownership query results. 
  'includeHistorical': true, // Boolean | If set to true, historical ownership data will be requested. 
  'onlyProfile': true // Boolean | If set to true, a full UBO report will not be requested. 
};
apiInstance.businessOwnershipQuery(xFrankieCustomerID, query, opts, (error, data, response) => {
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
 **query** | [**OwnershipQuery**](OwnershipQuery.md)| The organisation to be queried. An entity object that must have an organisation object with at least one organisation number.  | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **checkType** | [**[String]**](String.md)| When creating a new check, we need to define the checks we wish to run. If this parameter is not supplied then the check will be based on a configured check type for each entity category.    The checkType is make up of a comma separated list of the types of check we wish to run.  The order is important, and must be of the form:   - Entity Check (if you&#39;re running this). Choose one from the available options   - ID Check (If you want this)   - PEP Checks (again if you want this, choose one of the options)  Entity Checks - One of:   - \&quot;one_plus\&quot;: Checks name, address and DoB against a minimum of 1 data source. (also known as a 1+1)   - \&quot;two_plus\&quot;: Checks name, address and DoB against a minimum of 2 independent data sources (also known as a 2+2)  ID Checks - One of:   - \&quot;id\&quot;: Checks all of the identity documents, but not necessarily the entity itself independently. Use this in conjunction with a one_plus or two_plus for more.    Fraud Checks - One or more  of:   - \&quot;fraudlist\&quot;: Checks to see if the identity appears on any known fraud lists. Should be run after KYC/ID checks have passed.   - \&quot;fraudid\&quot;: Checks external ID services to see if details appear in fraud detection services (e.g. EmailAge or FraudNet)    PEP Checks - One of:   - \&quot;pep\&quot;: Will only run PEP/Sanctions checks (no identity verification)   - \&quot;pep_media\&quot;: Will run PEP/Sanctions checks, as well as watchlist and adverse media checks. (no identity verification)      * NOTE: These checks will ONLY run if either the KYC/ID checks have been run prior, or it is the only check requested.    Pre-defined combinations:   - \&quot;full\&quot;: equivalent to \&quot;two_plus,id,pep_media\&quot; or \&quot;pep_media\&quot; if the target is an organisation.   - \&quot;default\&quot;: Currently defined as \&quot;two_plus,id\&quot; or \&quot;pep\&quot; if the target is an organisation.  Custom:   - By arrangement with Frankie you can define your own KYC check type.      This will allow you to set the minimum number of matches for:     - name      - date of birth     - address     - government id      This allows for alternatives to the \&quot;standard\&quot; two_plus or one_plus (note, these can be overridden too).    Profile:   - \&quot;profile\&quot;: By arrangement with Frankie you can have a \&quot;profile\&quot; check type that applies checks according to a profile that you assign to the entity from a predefined set of profiles.      The profile to use will be taken from the entity.entityProfile field if set, or be run through a set of configurable rules to determine which one to use.      Profiles act a little like the Pre-defined combinations above in that they can map to a defined list. But they offer a lot more besides, including rules for determining default settings, inbuild data aging and other configurable features.   They also allow for a new result set top be returned that provides a more detailed and useful breakdown of the check/verification process.      Entity Profiles are the future of checks with Frankie Financial.  | [optional] 
 **entityCategories** | [**[String]**](String.md)| A comma separated list that specifies the categories of entities associated with the target organisation that will be checked.    - organisation - Just the organisation itself.   - ubos - All ultimate beneficial owners.   - pseudo_ubos - Use an alterntive category when an organisation has no actual UBOs. The actual category to use is defined via configuration, default is no alterntive category.   - direct_owners - All direct owners of the company, both organisations and individuals, may include UBOs for for simple ownership.   - officers - All officers of the company   - officers_directors - All directors of the company   - officers_other - All non-director officers of the company   - all - All direct and indirect owners, both organisations and individuals (including UBOs), and officers of all organisations.  | [optional] 
 **resultLevel** | **String**| The result level allows you to specify the level of detail returned for the entity check. You can choose summary or full.  | [optional] [default to &#39;summary&#39;]
 **validation** | **String**| Should a validation check be run before the ownership query. The default is specified via configuration. The validation checks to see if the provided organisation is suitable for an ownership query by looking for the ACN in public data sources.  Options are: - \&quot;on\&quot;: Validate only when ACN is not provided. This is the typical default. - \&quot;acn\&quot;: Validate even if ACN is provided. - \&quot;only\&quot;: Like \&quot;acn\&quot; but only do validation query, don&#39;t proceed with ownership query. This option cannot be set as the default via configuration. - \&quot;off\&quot;: Never validate. The Ownership query will then fail if an ACN is not provided.  | [optional] 
 **generateReport** | **String**| The type of human readable report, if any, to generate based on the ownership query results.  | [optional] 
 **includeHistorical** | **Boolean**| If set to true, historical ownership data will be requested.  | [optional] 
 **onlyProfile** | **Boolean**| If set to true, a full UBO report will not be requested.  | [optional] 

### Return type

[**OrganisationCheckResponseObject**](OrganisationCheckResponseObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## checkOrganisation

> AcceptedEntityResultObject checkOrganisation(xFrankieCustomerID, entityId, opts)

Run KYC/AML Checks on Organisation and/or Associated Individuals.

Run KYC/AML for a selection of entities associated with an organisation and/or the organisation itself based on a previous ownership query. By default AML will be checked for just the organisation itself. If a list of entity categories is given then default checks based on configuration will be run for those categories. If a check type is also provided in the request then that type will be used for entities representing individual entities, and the AML subset of that check will be used for organisations if any. If no ownership query has been run, then this operation will return an error. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.BusinessApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let entityId = "entityId_example"; // String | The entityId returned previously from an earlier call to /check or /entity
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'checkType': ["null"], // [String] | When creating a new check, we need to define the checks we wish to run. If this parameter is not supplied then the check will be based on a configured check type for each entity category.    The checkType is make up of a comma separated list of the types of check we wish to run.  The order is important, and must be of the form:   - Entity Check (if you're running this). Choose one from the available options   - ID Check (If you want this)   - PEP Checks (again if you want this, choose one of the options)  Entity Checks - One of:   - \"one_plus\": Checks name, address and DoB against a minimum of 1 data source. (also known as a 1+1)   - \"two_plus\": Checks name, address and DoB against a minimum of 2 independent data sources (also known as a 2+2)  ID Checks - One of:   - \"id\": Checks all of the identity documents, but not necessarily the entity itself independently. Use this in conjunction with a one_plus or two_plus for more.    Fraud Checks - One or more  of:   - \"fraudlist\": Checks to see if the identity appears on any known fraud lists. Should be run after KYC/ID checks have passed.   - \"fraudid\": Checks external ID services to see if details appear in fraud detection services (e.g. EmailAge or FraudNet)    PEP Checks - One of:   - \"pep\": Will only run PEP/Sanctions checks (no identity verification)   - \"pep_media\": Will run PEP/Sanctions checks, as well as watchlist and adverse media checks. (no identity verification)      * NOTE: These checks will ONLY run if either the KYC/ID checks have been run prior, or it is the only check requested.    Pre-defined combinations:   - \"full\": equivalent to \"two_plus,id,pep_media\" or \"pep_media\" if the target is an organisation.   - \"default\": Currently defined as \"two_plus,id\" or \"pep\" if the target is an organisation.  Custom:   - By arrangement with Frankie you can define your own KYC check type.      This will allow you to set the minimum number of matches for:     - name      - date of birth     - address     - government id      This allows for alternatives to the \"standard\" two_plus or one_plus (note, these can be overridden too).    Profile:   - \"profile\": By arrangement with Frankie you can have a \"profile\" check type that applies checks according to a profile that you assign to the entity from a predefined set of profiles.      The profile to use will be taken from the entity.entityProfile field if set, or be run through a set of configurable rules to determine which one to use.      Profiles act a little like the Pre-defined combinations above in that they can map to a defined list. But they offer a lot more besides, including rules for determining default settings, inbuild data aging and other configurable features.   They also allow for a new result set top be returned that provides a more detailed and useful breakdown of the check/verification process.      Entity Profiles are the future of checks with Frankie Financial. 
  'entityCategories': ["null"], // [String] | A comma separated list that specifies the categories of entities associated with the target organisation that will be checked.    - organisation - Just the organisation itself.   - ubos - All ultimate beneficial owners.   - pseudo_ubos - Use an alterntive category when an organisation has no actual UBOs. The actual category to use is defined via configuration, default is no alterntive category.   - direct_owners - All direct owners of the company, both organisations and individuals, may include UBOs for for simple ownership.   - officers - All officers of the company   - officers_directors - All directors of the company   - officers_other - All non-director officers of the company   - all - All direct and indirect owners, both organisations and individuals (including UBOs), and officers of all organisations. 
  'resultLevel': "'summary'", // String | The result level allows you to specify the level of detail returned for the entity check. You can choose summary or full. 
  'generateReport': "generateReport_example" // String | The type of human readable report, if any, to generate based on the ownership query results. 
};
apiInstance.checkOrganisation(xFrankieCustomerID, entityId, opts, (error, data, response) => {
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
 **checkType** | [**[String]**](String.md)| When creating a new check, we need to define the checks we wish to run. If this parameter is not supplied then the check will be based on a configured check type for each entity category.    The checkType is make up of a comma separated list of the types of check we wish to run.  The order is important, and must be of the form:   - Entity Check (if you&#39;re running this). Choose one from the available options   - ID Check (If you want this)   - PEP Checks (again if you want this, choose one of the options)  Entity Checks - One of:   - \&quot;one_plus\&quot;: Checks name, address and DoB against a minimum of 1 data source. (also known as a 1+1)   - \&quot;two_plus\&quot;: Checks name, address and DoB against a minimum of 2 independent data sources (also known as a 2+2)  ID Checks - One of:   - \&quot;id\&quot;: Checks all of the identity documents, but not necessarily the entity itself independently. Use this in conjunction with a one_plus or two_plus for more.    Fraud Checks - One or more  of:   - \&quot;fraudlist\&quot;: Checks to see if the identity appears on any known fraud lists. Should be run after KYC/ID checks have passed.   - \&quot;fraudid\&quot;: Checks external ID services to see if details appear in fraud detection services (e.g. EmailAge or FraudNet)    PEP Checks - One of:   - \&quot;pep\&quot;: Will only run PEP/Sanctions checks (no identity verification)   - \&quot;pep_media\&quot;: Will run PEP/Sanctions checks, as well as watchlist and adverse media checks. (no identity verification)      * NOTE: These checks will ONLY run if either the KYC/ID checks have been run prior, or it is the only check requested.    Pre-defined combinations:   - \&quot;full\&quot;: equivalent to \&quot;two_plus,id,pep_media\&quot; or \&quot;pep_media\&quot; if the target is an organisation.   - \&quot;default\&quot;: Currently defined as \&quot;two_plus,id\&quot; or \&quot;pep\&quot; if the target is an organisation.  Custom:   - By arrangement with Frankie you can define your own KYC check type.      This will allow you to set the minimum number of matches for:     - name      - date of birth     - address     - government id      This allows for alternatives to the \&quot;standard\&quot; two_plus or one_plus (note, these can be overridden too).    Profile:   - \&quot;profile\&quot;: By arrangement with Frankie you can have a \&quot;profile\&quot; check type that applies checks according to a profile that you assign to the entity from a predefined set of profiles.      The profile to use will be taken from the entity.entityProfile field if set, or be run through a set of configurable rules to determine which one to use.      Profiles act a little like the Pre-defined combinations above in that they can map to a defined list. But they offer a lot more besides, including rules for determining default settings, inbuild data aging and other configurable features.   They also allow for a new result set top be returned that provides a more detailed and useful breakdown of the check/verification process.      Entity Profiles are the future of checks with Frankie Financial.  | [optional] 
 **entityCategories** | [**[String]**](String.md)| A comma separated list that specifies the categories of entities associated with the target organisation that will be checked.    - organisation - Just the organisation itself.   - ubos - All ultimate beneficial owners.   - pseudo_ubos - Use an alterntive category when an organisation has no actual UBOs. The actual category to use is defined via configuration, default is no alterntive category.   - direct_owners - All direct owners of the company, both organisations and individuals, may include UBOs for for simple ownership.   - officers - All officers of the company   - officers_directors - All directors of the company   - officers_other - All non-director officers of the company   - all - All direct and indirect owners, both organisations and individuals (including UBOs), and officers of all organisations.  | [optional] 
 **resultLevel** | **String**| The result level allows you to specify the level of detail returned for the entity check. You can choose summary or full.  | [optional] [default to &#39;summary&#39;]
 **generateReport** | **String**| The type of human readable report, if any, to generate based on the ownership query results.  | [optional] 

### Return type

[**AcceptedEntityResultObject**](AcceptedEntityResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## internationalBusinessProfile

> InternationalBusinessProfileResponse internationalBusinessProfile(xFrankieCustomerID, organisation, opts)

Retrieve a business profile from any country (AUS included).

Using the Company Code retrieved from the search response (see above) you can pull back the details of the company.  The Frankie platform will save the details of the response as an ORGANISATION type entity with the profile attached as a report which you can potentially re-retrieve later if you wish. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.BusinessApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let organisation = new FrankieFinancialApi.InternationalBusinessProfileCriteria(); // InternationalBusinessProfileCriteria | The country, cxompany code and optional registry of the organisation to be queried. 
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example" // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
};
apiInstance.internationalBusinessProfile(xFrankieCustomerID, organisation, opts, (error, data, response) => {
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
 **organisation** | [**InternationalBusinessProfileCriteria**](InternationalBusinessProfileCriteria.md)| The country, cxompany code and optional registry of the organisation to be queried.  | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 

### Return type

[**InternationalBusinessProfileResponse**](InternationalBusinessProfileResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## internationalBusinessSearch

> InternationalBusinessSearchResponse internationalBusinessSearch(xFrankieCustomerID, organisation, opts)

Search for a business from any country (AUS included).

Search for a given business name or business number across international business registers.  The search will return a list of matching companies that you can then potentially query using the international profile query (see below). Each search result will have a CompanyCode that you use to retrieve the specific company details using the profile function.  This process will not save any details from the search results. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.BusinessApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let organisation = new FrankieFinancialApi.InternationalBusinessSearchCriteria(); // InternationalBusinessSearchCriteria | The country, name or business number of the organisation to be queried. 
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example" // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
};
apiInstance.internationalBusinessSearch(xFrankieCustomerID, organisation, opts, (error, data, response) => {
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
 **organisation** | [**InternationalBusinessSearchCriteria**](InternationalBusinessSearchCriteria.md)| The country, name or business number of the organisation to be queried.  | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 

### Return type

[**InternationalBusinessSearchResponse**](InternationalBusinessSearchResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## runBusinessReports

> BusinessReportResponseDetails runBusinessReports(xFrankieCustomerID, reportTypes, organisation, opts)

Run Report(s) against a new or existing organisation entity (AUS Only).

NOTE: Australian companies ONLY. Create or find and update an ORGANISATION type entity, then run the requested reports. Reports include:  - Credit Report  - Credit Score  At a minimum, you just need to supply an ACN and/or ABN and an entity type set to ORGANISATION. Alternatively the entity ID of an existing ORGANISATION entity gan be given in the request body  Note: these reports are different to the Ultimate Beneficial Owner and Business Detail requests - these reports are independent data and analysis over and above company information and verification details.  You can request multiple reports to be run at once and they will be returned as a group (where feasible).  If a report can only be generated over time, then a temporary response will be returned and a webhook notification will be pushed later once the report has been completed. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.BusinessApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let reportTypes = "reportTypes_example"; // String | Define the report(s) you wish to run.  You can request more than one as a comma separated list.  Duplicates will be ignored.  Note: These reports are different to the business details and UBO queries and are meant to provide deeper detail and background on a business or organisation.    Current valid report types are:   - creditScore   - creditReport 
let organisation = new FrankieFinancialApi.EntityObject(); // EntityObject | The organisation to be queried. An entity object that must have be an ORGANISATION type with at least one organisation number (ABN or ACN). 
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example" // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
};
apiInstance.runBusinessReports(xFrankieCustomerID, reportTypes, organisation, opts, (error, data, response) => {
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
 **reportTypes** | **String**| Define the report(s) you wish to run.  You can request more than one as a comma separated list.  Duplicates will be ignored.  Note: These reports are different to the business details and UBO queries and are meant to provide deeper detail and background on a business or organisation.    Current valid report types are:   - creditScore   - creditReport  | 
 **organisation** | [**EntityObject**](EntityObject.md)| The organisation to be queried. An entity object that must have be an ORGANISATION type with at least one organisation number (ABN or ACN).  | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 

### Return type

[**BusinessReportResponseDetails**](BusinessReportResponseDetails.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

