# AlloyDbApi.PscInterfaceConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumerEndpointIps** | **[String]** | A list of endpoints in the consumer VPC the interface might initiate outbound connections to. This list has to be provided when the PSC interface is created. | [optional] 
**networkAttachment** | **String** | The NetworkAttachment resource created in the consumer VPC to which the PSC interface will be linked, in the form of: &#x60;projects/${CONSUMER_PROJECT}/regions/${REGION}/networkAttachments/${NETWORK_ATTACHMENT_NAME}&#x60;. NetworkAttachment has to be provided when the PSC interface is created. | [optional] 


