# FrankieFinancialApi.InternationalBusinessProfileResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**companyProfile** | [**CompanyProfileDTO**](CompanyProfileDTO.md) |  | [optional] 
**checkId** | **String** | Unique ID for the individual check that was run.  | [optional] 
**entityId** | **String** | If the response was successful and we returned a company profile, we save this as an ORGANISATION type entity in our service. We will also save the profile result as a REPORT type document, attached to the entity.  | [optional] 
**ibResponseCode** | **Number** | service provider response code | [optional] 
**ibResponseDetails** | **String** |  | [optional] 
**ibRetrievalLocation** | **String** |  | [optional] 
**ibTransactionId** | **String** | service provider ID | [optional] 
**requestId** | **String** | Unique identifier for every request. Can be used for tracking down answers with technical support.   Uses the ULID format (a time-based, sortable UUID)  Note: this will be different for every request.  | [optional] 


