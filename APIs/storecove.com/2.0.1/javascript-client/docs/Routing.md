# StorecoveApi.Routing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clearWithoutSending** | **Boolean** | If you wish to send the document yourself in a Y-flow, use this flag. Wait for the &#39;cleared&#39; webhook and use the &lt;&lt;_openapi_show_document_submission_evidence&gt;&gt; endpoint to retrieve the clearing evidence. This will include a sendable document. | [optional] [default to false]
**eIdentifiers** | [**[RoutingIdentifier]**](RoutingIdentifier.md) | A list of electronic routing identifiers. These are the identifiers used on the Peppol network or for other destinations. | [optional] 
**emails** | **[String]** | The email addresses the invoice should be sent to if none of the other identifiers can be used | [optional] 


