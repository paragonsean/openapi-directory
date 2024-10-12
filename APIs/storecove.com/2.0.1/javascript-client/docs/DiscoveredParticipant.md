# StorecoveApi.DiscoveredParticipant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | The response code. | [optional] 
**email** | **Boolean** | Whether or not an &#39;OK&#39; response means the document will be sent via Peppol, but delivered by email. This happens in the Belgian Hermes system where all identifiers have been registered, but if the receiver hasn&#39;t registered with a service provider, the Hermes system will send a PDF created from the electronic invoice and email that. The electronic document will itself not be emailed. Also see https://einvoice.belgium.be/en/article/send-structured-invoices-all-your-customers-hermes[Hermes^]. | [optional] 



## Enum: CodeEnum


* `OK` (value: `"OK"`)

* `NOK` (value: `"NOK"`)




