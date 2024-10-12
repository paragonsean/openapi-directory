# CloudHealthcareApi.Hl7V2Store

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **{String: String}** | User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \\p{Ll}\\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}\\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. | [optional] 
**name** | **String** | Identifier. Resource name of the HL7v2 store, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7v2_store_id}&#x60;. | [optional] 
**notificationConfigs** | [**[Hl7V2NotificationConfig]**](Hl7V2NotificationConfig.md) | A list of notification configs. Each configuration uses a filter to determine whether to publish a message (both Ingest &amp; Create) on the corresponding notification destination. Only the message name is sent as part of the notification. Supplied by the client. | [optional] 
**parserConfig** | [**ParserConfig**](ParserConfig.md) |  | [optional] 
**rejectDuplicateMessage** | **Boolean** | Determines whether to reject duplicate messages. A duplicate message is a message with the same raw bytes as a message that has already been ingested/created in this HL7v2 store. The default value is false, meaning that the store accepts the duplicate messages and it also returns the same ACK message in the IngestMessageResponse as has been returned previously. Note that only one resource is created in the store. When this field is set to true, CreateMessage/IngestMessage requests with a duplicate message will be rejected by the store, and IngestMessageErrorDetail returns a NACK message upon rejection. | [optional] 


