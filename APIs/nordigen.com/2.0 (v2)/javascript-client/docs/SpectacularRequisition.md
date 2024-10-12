# NordigenAccountInformationServicesApi.SpectacularRequisition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSelection** | **Boolean** | option to enable account selection view for the end user | [optional] [default to false]
**accounts** | **[Object]** | array of account IDs retrieved within a scope of this requisition | [optional] [readonly] 
**agreement** | **String** | EUA associated with this requisition | [optional] 
**created** | **Date** | The date &amp; time at which the requisition was created. | [optional] [readonly] 
**id** | **String** |  | [optional] [readonly] 
**institutionId** | **String** | an Institution ID for this Requisition | 
**link** | **String** | link to initiate authorization with Institution | [optional] [readonly] [default to &#39;https://ob.nordigen.com/psd2/start/3fa85f64-5717-4562-b3fc-2c963f66afa6/{$INSTITUTION_ID}&#39;]
**redirect** | **String** | redirect URL to your application after end-user authorization with ASPSP | 
**redirectImmediate** | **Boolean** | enable redirect back to the client after account list received | [optional] [default to false]
**reference** | **String** | additional ID to identify the end user | [optional] 
**ssn** | **String** | optional SSN field to verify ownership of the account | [optional] 
**status** | [**Status1c5Enum**](Status1c5Enum.md) | status of this requisition | [optional] [readonly] 
**userLanguage** | **String** | A two-letter country code (ISO 639-1) | [optional] 


