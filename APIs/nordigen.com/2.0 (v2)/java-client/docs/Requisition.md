

# Requisition

RequisitionSerializer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSelection** | **Boolean** | option to enable account selection view for the end user |  [optional] |
|**accounts** | **List&lt;UUID&gt;** | array of account IDs retrieved within a scope of this requisition |  [optional] [readonly] |
|**agreement** | **UUID** | EUA associated with this requisition |  [optional] |
|**created** | **OffsetDateTime** | The date &amp; time at which the requisition was created. |  [optional] [readonly] |
|**id** | **UUID** |  |  [optional] [readonly] |
|**institutionId** | **String** | an Institution ID for this Requisition |  |
|**link** | **URI** | link to initiate authorization with Institution |  [optional] [readonly] |
|**redirect** | **URI** | redirect URL to your application after end-user authorization with ASPSP |  |
|**redirectImmediate** | **Boolean** | enable redirect back to the client after account list received |  [optional] |
|**reference** | **String** | additional ID to identify the end user |  [optional] |
|**ssn** | **String** | optional SSN field to verify ownership of the account |  [optional] |
|**status** | **Status1c5Enum** | status of this requisition |  [optional] [readonly] |
|**userLanguage** | **String** | A two-letter country code (ISO 639-1) |  [optional] |



