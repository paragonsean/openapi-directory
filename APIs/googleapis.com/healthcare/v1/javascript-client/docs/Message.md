# CloudHealthcareApi.Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The datetime when the message was created. Set by the server. | [optional] [readonly] 
**data** | **Blob** | Required. Raw message bytes. | [optional] 
**labels** | **{String: String}** | User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \\p{Ll}\\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}\\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. | [optional] 
**messageType** | **String** | The message type for this message. MSH-9.1. | [optional] 
**name** | **String** | Output only. Resource name of the Message, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7_v2_store_id}/messages/{message_id}&#x60;. Assigned by the server. | [optional] [readonly] 
**parsedData** | [**ParsedData**](ParsedData.md) |  | [optional] 
**patientIds** | [**[PatientId]**](PatientId.md) | All patient IDs listed in the PID-2, PID-3, and PID-4 segments of this message. | [optional] 
**schematizedData** | [**SchematizedData**](SchematizedData.md) |  | [optional] 
**sendFacility** | **String** | The hospital that this message came from. MSH-4. | [optional] 
**sendTime** | **String** | The datetime the sending application sent this message. MSH-7. | [optional] 


