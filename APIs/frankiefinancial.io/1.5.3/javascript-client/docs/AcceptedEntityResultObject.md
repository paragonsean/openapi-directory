# FrankieFinancialApi.AcceptedEntityResultObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkId** | **String** | If you&#39;re calling a processing function of some kind, a check number will be issued. This field will only be present if the function you&#39;re calling would normally return a checkId (such as scan, verify, and compare).  | [optional] 
**entityId** | **String** | When an entity is created/uploaded, or generated from a document scan, it is assigned an entityId. This can then be referenced in subsequent calls if you&#39;re uploading more/updated data.  | [optional] 
**_function** | **String** | Short description of the function called.  | [optional] 
**linkURL** | **String** | Optional link that can be returned - used by the Push To Mobile service to allow API users to manage the use of the onboarding link themselves.  | [optional] 
**requestId** | **String** | Unique identifier for every request. Can be used for tracking down answers with technical support.   Uses the ULID format (a time-based, sortable UUID)  Note: this will be different for every request.  | [optional] 


