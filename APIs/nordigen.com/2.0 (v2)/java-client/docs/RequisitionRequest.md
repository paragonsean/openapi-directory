

# RequisitionRequest

RequisitionSerializer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSelection** | **Boolean** | option to enable account selection view for the end user |  [optional] |
|**agreement** | **UUID** | EUA associated with this requisition |  [optional] |
|**institutionId** | **String** | an Institution ID for this Requisition |  |
|**redirect** | **URI** | redirect URL to your application after end-user authorization with ASPSP |  |
|**redirectImmediate** | **Boolean** | enable redirect back to the client after account list received |  [optional] |
|**reference** | **String** | additional ID to identify the end user |  [optional] |
|**ssn** | **String** | optional SSN field to verify ownership of the account |  [optional] |
|**userLanguage** | **String** | A two-letter country code (ISO 639-1) |  [optional] |



