# BusinessApi

All URIs are relative to *https://api.demo.frankiefinancial.io/compliance/v1.2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**businessOwnershipQuery**](BusinessApi.md#businessOwnershipQuery) | **POST** /business/ownership/query | Create Business Entity and Query UBO (AUS Only) |
| [**checkOrganisation**](BusinessApi.md#checkOrganisation) | **POST** /business/{entityId}/verify | Run KYC/AML Checks on Organisation and/or Associated Individuals. |
| [**internationalBusinessProfile**](BusinessApi.md#internationalBusinessProfile) | **POST** /business/international/profile | Retrieve a business profile from any country (AUS included). |
| [**internationalBusinessSearch**](BusinessApi.md#internationalBusinessSearch) | **POST** /business/international/search | Search for a business from any country (AUS included). |
| [**runBusinessReports**](BusinessApi.md#runBusinessReports) | **POST** /business/reports | Run Report(s) against a new or existing organisation entity (AUS Only). |


<a id="businessOwnershipQuery"></a>
# **businessOwnershipQuery**
> OrganisationCheckResponseObject businessOwnershipQuery(xFrankieCustomerID, query, xFrankieCustomerChildID, checkType, entityCategories, resultLevel, validation, generateReport, includeHistorical, onlyProfile)

Create Business Entity and Query UBO (AUS Only)

Process a request for ownership details for an Australian organisation.  See below for more generic international queries.  At a minimum, you just need to supply an ACN or ABN and we can retrieve the rest. You also have the option of supplying company name, type (as per ABR types) and both ABN/ACN and we&#39;ll attempt to verfy that that data matches what is on record before attempting any further verification and validation.  KYC/AML for a selection of entities associated with an organisation and/or the organisation itself can optionally be run, but not by default. To enable KYC/AML checks one or more entity categories must be provided. If such a list of entity categories is given then default checks based on configuration will be run for those categories. If a check type is also provided in the request then that type will be used for entities representing individual entities, and the AML subset of that check will be used for organisations if any. Specifying a check type without an entity category will result in an error.  NOTE: This query will always run asynchronously and you will only ever be returned a 202 ACCEPT response, or an error. Results will be pushed using the Push Notification API below and you will be able to retrieve the results using the Retrieve API.  We have supplied the 200 response in the definition below only so what will be sent to you when you later retrieve the details.  More details on how to use this API and interpret the results can be found here:      https://apidocs.frankiefinancial.com/docs/which-function-to-use 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BusinessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    BusinessApi apiInstance = new BusinessApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    OwnershipQuery query = new OwnershipQuery(); // OwnershipQuery | The organisation to be queried. An entity object that must have an organisation object with at least one organisation number. 
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    Set<String> checkType = Arrays.asList(); // Set<String> | When creating a new check, we need to define the checks we wish to run. If this parameter is not supplied then the check will be based on a configured check type for each entity category.    The checkType is make up of a comma separated list of the types of check we wish to run.  The order is important, and must be of the form:   - Entity Check (if you're running this). Choose one from the available options   - ID Check (If you want this)   - PEP Checks (again if you want this, choose one of the options)  Entity Checks - One of:   - \"one_plus\": Checks name, address and DoB against a minimum of 1 data source. (also known as a 1+1)   - \"two_plus\": Checks name, address and DoB against a minimum of 2 independent data sources (also known as a 2+2)  ID Checks - One of:   - \"id\": Checks all of the identity documents, but not necessarily the entity itself independently. Use this in conjunction with a one_plus or two_plus for more.    Fraud Checks - One or more  of:   - \"fraudlist\": Checks to see if the identity appears on any known fraud lists. Should be run after KYC/ID checks have passed.   - \"fraudid\": Checks external ID services to see if details appear in fraud detection services (e.g. EmailAge or FraudNet)    PEP Checks - One of:   - \"pep\": Will only run PEP/Sanctions checks (no identity verification)   - \"pep_media\": Will run PEP/Sanctions checks, as well as watchlist and adverse media checks. (no identity verification)      * NOTE: These checks will ONLY run if either the KYC/ID checks have been run prior, or it is the only check requested.    Pre-defined combinations:   - \"full\": equivalent to \"two_plus,id,pep_media\" or \"pep_media\" if the target is an organisation.   - \"default\": Currently defined as \"two_plus,id\" or \"pep\" if the target is an organisation.  Custom:   - By arrangement with Frankie you can define your own KYC check type.      This will allow you to set the minimum number of matches for:     - name      - date of birth     - address     - government id      This allows for alternatives to the \"standard\" two_plus or one_plus (note, these can be overridden too).    Profile:   - \"profile\": By arrangement with Frankie you can have a \"profile\" check type that applies checks according to a profile that you assign to the entity from a predefined set of profiles.      The profile to use will be taken from the entity.entityProfile field if set, or be run through a set of configurable rules to determine which one to use.      Profiles act a little like the Pre-defined combinations above in that they can map to a defined list. But they offer a lot more besides, including rules for determining default settings, inbuild data aging and other configurable features.   They also allow for a new result set top be returned that provides a more detailed and useful breakdown of the check/verification process.      Entity Profiles are the future of checks with Frankie Financial. 
    Set<String> entityCategories = Arrays.asList(); // Set<String> | A comma separated list that specifies the categories of entities associated with the target organisation that will be checked.    - organisation - Just the organisation itself.   - ubos - All ultimate beneficial owners.   - pseudo_ubos - Use an alterntive category when an organisation has no actual UBOs. The actual category to use is defined via configuration, default is no alterntive category.   - direct_owners - All direct owners of the company, both organisations and individuals, may include UBOs for for simple ownership.   - officers - All officers of the company   - officers_directors - All directors of the company   - officers_other - All non-director officers of the company   - all - All direct and indirect owners, both organisations and individuals (including UBOs), and officers of all organisations. 
    String resultLevel = "summary"; // String | The result level allows you to specify the level of detail returned for the entity check. You can choose summary or full. 
    String validation = "true"; // String | Should a validation check be run before the ownership query. The default is specified via configuration. The validation checks to see if the provided organisation is suitable for an ownership query by looking for the ACN in public data sources.  Options are: - \"on\": Validate only when ACN is not provided. This is the typical default. - \"acn\": Validate even if ACN is provided. - \"only\": Like \"acn\" but only do validation query, don't proceed with ownership query. This option cannot be set as the default via configuration. - \"off\": Never validate. The Ownership query will then fail if an ACN is not provided. 
    String generateReport = "generateReport_example"; // String | The type of human readable report, if any, to generate based on the ownership query results. 
    Boolean includeHistorical = true; // Boolean | If set to true, historical ownership data will be requested. 
    Boolean onlyProfile = true; // Boolean | If set to true, a full UBO report will not be requested. 
    try {
      OrganisationCheckResponseObject result = apiInstance.businessOwnershipQuery(xFrankieCustomerID, query, xFrankieCustomerChildID, checkType, entityCategories, resultLevel, validation, generateReport, includeHistorical, onlyProfile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BusinessApi#businessOwnershipQuery");
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
| **query** | [**OwnershipQuery**](OwnershipQuery.md)| The organisation to be queried. An entity object that must have an organisation object with at least one organisation number.  | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **checkType** | [**Set&lt;String&gt;**](String.md)| When creating a new check, we need to define the checks we wish to run. If this parameter is not supplied then the check will be based on a configured check type for each entity category.    The checkType is make up of a comma separated list of the types of check we wish to run.  The order is important, and must be of the form:   - Entity Check (if you&#39;re running this). Choose one from the available options   - ID Check (If you want this)   - PEP Checks (again if you want this, choose one of the options)  Entity Checks - One of:   - \&quot;one_plus\&quot;: Checks name, address and DoB against a minimum of 1 data source. (also known as a 1+1)   - \&quot;two_plus\&quot;: Checks name, address and DoB against a minimum of 2 independent data sources (also known as a 2+2)  ID Checks - One of:   - \&quot;id\&quot;: Checks all of the identity documents, but not necessarily the entity itself independently. Use this in conjunction with a one_plus or two_plus for more.    Fraud Checks - One or more  of:   - \&quot;fraudlist\&quot;: Checks to see if the identity appears on any known fraud lists. Should be run after KYC/ID checks have passed.   - \&quot;fraudid\&quot;: Checks external ID services to see if details appear in fraud detection services (e.g. EmailAge or FraudNet)    PEP Checks - One of:   - \&quot;pep\&quot;: Will only run PEP/Sanctions checks (no identity verification)   - \&quot;pep_media\&quot;: Will run PEP/Sanctions checks, as well as watchlist and adverse media checks. (no identity verification)      * NOTE: These checks will ONLY run if either the KYC/ID checks have been run prior, or it is the only check requested.    Pre-defined combinations:   - \&quot;full\&quot;: equivalent to \&quot;two_plus,id,pep_media\&quot; or \&quot;pep_media\&quot; if the target is an organisation.   - \&quot;default\&quot;: Currently defined as \&quot;two_plus,id\&quot; or \&quot;pep\&quot; if the target is an organisation.  Custom:   - By arrangement with Frankie you can define your own KYC check type.      This will allow you to set the minimum number of matches for:     - name      - date of birth     - address     - government id      This allows for alternatives to the \&quot;standard\&quot; two_plus or one_plus (note, these can be overridden too).    Profile:   - \&quot;profile\&quot;: By arrangement with Frankie you can have a \&quot;profile\&quot; check type that applies checks according to a profile that you assign to the entity from a predefined set of profiles.      The profile to use will be taken from the entity.entityProfile field if set, or be run through a set of configurable rules to determine which one to use.      Profiles act a little like the Pre-defined combinations above in that they can map to a defined list. But they offer a lot more besides, including rules for determining default settings, inbuild data aging and other configurable features.   They also allow for a new result set top be returned that provides a more detailed and useful breakdown of the check/verification process.      Entity Profiles are the future of checks with Frankie Financial.  | [optional] [enum: full, default, one_plus, two_plus, id, fraudlist, fraudcheck, pep, pep_media, profile] |
| **entityCategories** | [**Set&lt;String&gt;**](String.md)| A comma separated list that specifies the categories of entities associated with the target organisation that will be checked.    - organisation - Just the organisation itself.   - ubos - All ultimate beneficial owners.   - pseudo_ubos - Use an alterntive category when an organisation has no actual UBOs. The actual category to use is defined via configuration, default is no alterntive category.   - direct_owners - All direct owners of the company, both organisations and individuals, may include UBOs for for simple ownership.   - officers - All officers of the company   - officers_directors - All directors of the company   - officers_other - All non-director officers of the company   - all - All direct and indirect owners, both organisations and individuals (including UBOs), and officers of all organisations.  | [optional] [enum: organisation, ubos, pseudo_ubos, direct_owners, officers, officers_directors, officers_other, all] |
| **resultLevel** | **String**| The result level allows you to specify the level of detail returned for the entity check. You can choose summary or full.  | [optional] [default to summary] [enum: summary, full] |
| **validation** | **String**| Should a validation check be run before the ownership query. The default is specified via configuration. The validation checks to see if the provided organisation is suitable for an ownership query by looking for the ACN in public data sources.  Options are: - \&quot;on\&quot;: Validate only when ACN is not provided. This is the typical default. - \&quot;acn\&quot;: Validate even if ACN is provided. - \&quot;only\&quot;: Like \&quot;acn\&quot; but only do validation query, don&#39;t proceed with ownership query. This option cannot be set as the default via configuration. - \&quot;off\&quot;: Never validate. The Ownership query will then fail if an ACN is not provided.  | [optional] [enum: true, false, only, acn] |
| **generateReport** | **String**| The type of human readable report, if any, to generate based on the ownership query results.  | [optional] |
| **includeHistorical** | **Boolean**| If set to true, historical ownership data will be requested.  | [optional] |
| **onlyProfile** | **Boolean**| If set to true, a full UBO report will not be requested.  | [optional] |

### Return type

[**OrganisationCheckResponseObject**](OrganisationCheckResponseObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | !!!! This response will never be sent synchronously !!!!  This is what you will find in the payload of a retrieved response should the ownership query succeed.  |  -  |
| **202** | The request was valid and can potentially be fulfilled. The Frankie service has now accepted responsibility for processing and we will either push the results to you, or send you a notification, depending on the request and your configuration. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **405** | A request to POST an update to an object was not allowed due to it&#39;s state. This may indicate an already completed check, or a document that has been processed. You need to create a new document/check if you wish to update the object in question. |  -  |
| **422** | Unprocessable request. This can be triggered in a number of ways. * An attempt to force a check or scan to run, but there is insufficient data to be able to do so. * An attempt to run a utility comparison, or similar industry/document/entity specific scan or process on an unsupported document type (e.g. electricity comparison on a passport) Details of what is required will be in the issues list of the error response.  |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |
| **503** | All of the ID sources configured by the customer are unavailable, or there is no available document processor. |  -  |

<a id="checkOrganisation"></a>
# **checkOrganisation**
> AcceptedEntityResultObject checkOrganisation(xFrankieCustomerID, entityId, xFrankieCustomerChildID, checkType, entityCategories, resultLevel, generateReport)

Run KYC/AML Checks on Organisation and/or Associated Individuals.

Run KYC/AML for a selection of entities associated with an organisation and/or the organisation itself based on a previous ownership query. By default AML will be checked for just the organisation itself. If a list of entity categories is given then default checks based on configuration will be run for those categories. If a check type is also provided in the request then that type will be used for entities representing individual entities, and the AML subset of that check will be used for organisations if any. If no ownership query has been run, then this operation will return an error. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BusinessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    BusinessApi apiInstance = new BusinessApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID entityId = UUID.randomUUID(); // UUID | The entityId returned previously from an earlier call to /check or /entity
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    Set<String> checkType = Arrays.asList(); // Set<String> | When creating a new check, we need to define the checks we wish to run. If this parameter is not supplied then the check will be based on a configured check type for each entity category.    The checkType is make up of a comma separated list of the types of check we wish to run.  The order is important, and must be of the form:   - Entity Check (if you're running this). Choose one from the available options   - ID Check (If you want this)   - PEP Checks (again if you want this, choose one of the options)  Entity Checks - One of:   - \"one_plus\": Checks name, address and DoB against a minimum of 1 data source. (also known as a 1+1)   - \"two_plus\": Checks name, address and DoB against a minimum of 2 independent data sources (also known as a 2+2)  ID Checks - One of:   - \"id\": Checks all of the identity documents, but not necessarily the entity itself independently. Use this in conjunction with a one_plus or two_plus for more.    Fraud Checks - One or more  of:   - \"fraudlist\": Checks to see if the identity appears on any known fraud lists. Should be run after KYC/ID checks have passed.   - \"fraudid\": Checks external ID services to see if details appear in fraud detection services (e.g. EmailAge or FraudNet)    PEP Checks - One of:   - \"pep\": Will only run PEP/Sanctions checks (no identity verification)   - \"pep_media\": Will run PEP/Sanctions checks, as well as watchlist and adverse media checks. (no identity verification)      * NOTE: These checks will ONLY run if either the KYC/ID checks have been run prior, or it is the only check requested.    Pre-defined combinations:   - \"full\": equivalent to \"two_plus,id,pep_media\" or \"pep_media\" if the target is an organisation.   - \"default\": Currently defined as \"two_plus,id\" or \"pep\" if the target is an organisation.  Custom:   - By arrangement with Frankie you can define your own KYC check type.      This will allow you to set the minimum number of matches for:     - name      - date of birth     - address     - government id      This allows for alternatives to the \"standard\" two_plus or one_plus (note, these can be overridden too).    Profile:   - \"profile\": By arrangement with Frankie you can have a \"profile\" check type that applies checks according to a profile that you assign to the entity from a predefined set of profiles.      The profile to use will be taken from the entity.entityProfile field if set, or be run through a set of configurable rules to determine which one to use.      Profiles act a little like the Pre-defined combinations above in that they can map to a defined list. But they offer a lot more besides, including rules for determining default settings, inbuild data aging and other configurable features.   They also allow for a new result set top be returned that provides a more detailed and useful breakdown of the check/verification process.      Entity Profiles are the future of checks with Frankie Financial. 
    Set<String> entityCategories = Arrays.asList(); // Set<String> | A comma separated list that specifies the categories of entities associated with the target organisation that will be checked.    - organisation - Just the organisation itself.   - ubos - All ultimate beneficial owners.   - pseudo_ubos - Use an alterntive category when an organisation has no actual UBOs. The actual category to use is defined via configuration, default is no alterntive category.   - direct_owners - All direct owners of the company, both organisations and individuals, may include UBOs for for simple ownership.   - officers - All officers of the company   - officers_directors - All directors of the company   - officers_other - All non-director officers of the company   - all - All direct and indirect owners, both organisations and individuals (including UBOs), and officers of all organisations. 
    String resultLevel = "summary"; // String | The result level allows you to specify the level of detail returned for the entity check. You can choose summary or full. 
    String generateReport = "generateReport_example"; // String | The type of human readable report, if any, to generate based on the ownership query results. 
    try {
      AcceptedEntityResultObject result = apiInstance.checkOrganisation(xFrankieCustomerID, entityId, xFrankieCustomerChildID, checkType, entityCategories, resultLevel, generateReport);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BusinessApi#checkOrganisation");
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
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **checkType** | [**Set&lt;String&gt;**](String.md)| When creating a new check, we need to define the checks we wish to run. If this parameter is not supplied then the check will be based on a configured check type for each entity category.    The checkType is make up of a comma separated list of the types of check we wish to run.  The order is important, and must be of the form:   - Entity Check (if you&#39;re running this). Choose one from the available options   - ID Check (If you want this)   - PEP Checks (again if you want this, choose one of the options)  Entity Checks - One of:   - \&quot;one_plus\&quot;: Checks name, address and DoB against a minimum of 1 data source. (also known as a 1+1)   - \&quot;two_plus\&quot;: Checks name, address and DoB against a minimum of 2 independent data sources (also known as a 2+2)  ID Checks - One of:   - \&quot;id\&quot;: Checks all of the identity documents, but not necessarily the entity itself independently. Use this in conjunction with a one_plus or two_plus for more.    Fraud Checks - One or more  of:   - \&quot;fraudlist\&quot;: Checks to see if the identity appears on any known fraud lists. Should be run after KYC/ID checks have passed.   - \&quot;fraudid\&quot;: Checks external ID services to see if details appear in fraud detection services (e.g. EmailAge or FraudNet)    PEP Checks - One of:   - \&quot;pep\&quot;: Will only run PEP/Sanctions checks (no identity verification)   - \&quot;pep_media\&quot;: Will run PEP/Sanctions checks, as well as watchlist and adverse media checks. (no identity verification)      * NOTE: These checks will ONLY run if either the KYC/ID checks have been run prior, or it is the only check requested.    Pre-defined combinations:   - \&quot;full\&quot;: equivalent to \&quot;two_plus,id,pep_media\&quot; or \&quot;pep_media\&quot; if the target is an organisation.   - \&quot;default\&quot;: Currently defined as \&quot;two_plus,id\&quot; or \&quot;pep\&quot; if the target is an organisation.  Custom:   - By arrangement with Frankie you can define your own KYC check type.      This will allow you to set the minimum number of matches for:     - name      - date of birth     - address     - government id      This allows for alternatives to the \&quot;standard\&quot; two_plus or one_plus (note, these can be overridden too).    Profile:   - \&quot;profile\&quot;: By arrangement with Frankie you can have a \&quot;profile\&quot; check type that applies checks according to a profile that you assign to the entity from a predefined set of profiles.      The profile to use will be taken from the entity.entityProfile field if set, or be run through a set of configurable rules to determine which one to use.      Profiles act a little like the Pre-defined combinations above in that they can map to a defined list. But they offer a lot more besides, including rules for determining default settings, inbuild data aging and other configurable features.   They also allow for a new result set top be returned that provides a more detailed and useful breakdown of the check/verification process.      Entity Profiles are the future of checks with Frankie Financial.  | [optional] [enum: full, default, one_plus, two_plus, id, fraudlist, fraudcheck, pep, pep_media, profile] |
| **entityCategories** | [**Set&lt;String&gt;**](String.md)| A comma separated list that specifies the categories of entities associated with the target organisation that will be checked.    - organisation - Just the organisation itself.   - ubos - All ultimate beneficial owners.   - pseudo_ubos - Use an alterntive category when an organisation has no actual UBOs. The actual category to use is defined via configuration, default is no alterntive category.   - direct_owners - All direct owners of the company, both organisations and individuals, may include UBOs for for simple ownership.   - officers - All officers of the company   - officers_directors - All directors of the company   - officers_other - All non-director officers of the company   - all - All direct and indirect owners, both organisations and individuals (including UBOs), and officers of all organisations.  | [optional] [enum: organisation, ubos, pseudo_ubos, direct_owners, officers, officers_directors, officers_other, all] |
| **resultLevel** | **String**| The result level allows you to specify the level of detail returned for the entity check. You can choose summary or full.  | [optional] [default to summary] [enum: summary, full] |
| **generateReport** | **String**| The type of human readable report, if any, to generate based on the ownership query results.  | [optional] |

### Return type

[**AcceptedEntityResultObject**](AcceptedEntityResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The request was valid and can potentially be fulfilled. The Frankie service has now accepted responsibility for processing and we will either push the results to you, or send you a notification, depending on the request and your configuration. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **405** | A request to POST an update to an object was not allowed due to it&#39;s state. This may indicate an already completed check, or a document that has been processed. You need to create a new document/check if you wish to update the object in question. |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |
| **503** | All of the ID sources configured by the customer are unavailable, or there is no available document processor. |  -  |

<a id="internationalBusinessProfile"></a>
# **internationalBusinessProfile**
> InternationalBusinessProfileResponse internationalBusinessProfile(xFrankieCustomerID, organisation, xFrankieCustomerChildID)

Retrieve a business profile from any country (AUS included).

Using the Company Code retrieved from the search response (see above) you can pull back the details of the company.  The Frankie platform will save the details of the response as an ORGANISATION type entity with the profile attached as a report which you can potentially re-retrieve later if you wish. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BusinessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    BusinessApi apiInstance = new BusinessApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    InternationalBusinessProfileCriteria organisation = new InternationalBusinessProfileCriteria(); // InternationalBusinessProfileCriteria | The country, cxompany code and optional registry of the organisation to be queried. 
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    try {
      InternationalBusinessProfileResponse result = apiInstance.internationalBusinessProfile(xFrankieCustomerID, organisation, xFrankieCustomerChildID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BusinessApi#internationalBusinessProfile");
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
| **organisation** | [**InternationalBusinessProfileCriteria**](InternationalBusinessProfileCriteria.md)| The country, cxompany code and optional registry of the organisation to be queried.  | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |

### Return type

[**InternationalBusinessProfileResponse**](InternationalBusinessProfileResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and was successfully processed. The search has been carried out and the results are attached. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **405** | A request to POST an update to an object was not allowed due to it&#39;s state. This may indicate an already completed check, or a document that has been processed. You need to create a new document/check if you wish to update the object in question. |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |
| **503** | All of the ID sources configured by the customer are unavailable, or there is no available document processor. |  -  |

<a id="internationalBusinessSearch"></a>
# **internationalBusinessSearch**
> InternationalBusinessSearchResponse internationalBusinessSearch(xFrankieCustomerID, organisation, xFrankieCustomerChildID)

Search for a business from any country (AUS included).

Search for a given business name or business number across international business registers.  The search will return a list of matching companies that you can then potentially query using the international profile query (see below). Each search result will have a CompanyCode that you use to retrieve the specific company details using the profile function.  This process will not save any details from the search results. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BusinessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    BusinessApi apiInstance = new BusinessApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    InternationalBusinessSearchCriteria organisation = new InternationalBusinessSearchCriteria(); // InternationalBusinessSearchCriteria | The country, name or business number of the organisation to be queried. 
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    try {
      InternationalBusinessSearchResponse result = apiInstance.internationalBusinessSearch(xFrankieCustomerID, organisation, xFrankieCustomerChildID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BusinessApi#internationalBusinessSearch");
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
| **organisation** | [**InternationalBusinessSearchCriteria**](InternationalBusinessSearchCriteria.md)| The country, name or business number of the organisation to be queried.  | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |

### Return type

[**InternationalBusinessSearchResponse**](InternationalBusinessSearchResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and was successfully processed. The search has been carried out and the results are attached. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **405** | A request to POST an update to an object was not allowed due to it&#39;s state. This may indicate an already completed check, or a document that has been processed. You need to create a new document/check if you wish to update the object in question. |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |
| **503** | All of the ID sources configured by the customer are unavailable, or there is no available document processor. |  -  |

<a id="runBusinessReports"></a>
# **runBusinessReports**
> BusinessReportResponseDetails runBusinessReports(xFrankieCustomerID, reportTypes, organisation, xFrankieCustomerChildID)

Run Report(s) against a new or existing organisation entity (AUS Only).

NOTE: Australian companies ONLY. Create or find and update an ORGANISATION type entity, then run the requested reports. Reports include:  - Credit Report  - Credit Score  At a minimum, you just need to supply an ACN and/or ABN and an entity type set to ORGANISATION. Alternatively the entity ID of an existing ORGANISATION entity gan be given in the request body  Note: these reports are different to the Ultimate Beneficial Owner and Business Detail requests - these reports are independent data and analysis over and above company information and verification details.  You can request multiple reports to be run at once and they will be returned as a group (where feasible).  If a report can only be generated over time, then a temporary response will be returned and a webhook notification will be pushed later once the report has been completed. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BusinessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    BusinessApi apiInstance = new BusinessApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    String reportTypes = "reportTypes_example"; // String | Define the report(s) you wish to run.  You can request more than one as a comma separated list.  Duplicates will be ignored.  Note: These reports are different to the business details and UBO queries and are meant to provide deeper detail and background on a business or organisation.    Current valid report types are:   - creditScore   - creditReport 
    EntityObject organisation = new EntityObject(); // EntityObject | The organisation to be queried. An entity object that must have be an ORGANISATION type with at least one organisation number (ABN or ACN). 
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    try {
      BusinessReportResponseDetails result = apiInstance.runBusinessReports(xFrankieCustomerID, reportTypes, organisation, xFrankieCustomerChildID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BusinessApi#runBusinessReports");
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
| **reportTypes** | **String**| Define the report(s) you wish to run.  You can request more than one as a comma separated list.  Duplicates will be ignored.  Note: These reports are different to the business details and UBO queries and are meant to provide deeper detail and background on a business or organisation.    Current valid report types are:   - creditScore   - creditReport  | |
| **organisation** | [**EntityObject**](EntityObject.md)| The organisation to be queried. An entity object that must have be an ORGANISATION type with at least one organisation number (ABN or ACN).  | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |

### Return type

[**BusinessReportResponseDetails**](BusinessReportResponseDetails.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and was successfully processed. The report was run and the results have been attached. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **405** | A request to POST an update to an object was not allowed due to it&#39;s state. This may indicate an already completed check, or a document that has been processed. You need to create a new document/check if you wish to update the object in question. |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |
| **503** | All of the ID sources configured by the customer are unavailable, or there is no available document processor. |  -  |

