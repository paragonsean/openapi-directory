

# PscInterfaceConfig

Configuration for setting up a PSC interface. This information needs to be provided by the customer. PSC interfaces will be created and added to VMs via SLM (adding a network interface will require recreating the VM). For HA instances this will be done via LDTM.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumerEndpointIps** | **List&lt;String&gt;** | A list of endpoints in the consumer VPC the interface might initiate outbound connections to. This list has to be provided when the PSC interface is created. |  [optional] |
|**networkAttachment** | **String** | The NetworkAttachment resource created in the consumer VPC to which the PSC interface will be linked, in the form of: &#x60;projects/${CONSUMER_PROJECT}/regions/${REGION}/networkAttachments/${NETWORK_ATTACHMENT_NAME}&#x60;. NetworkAttachment has to be provided when the PSC interface is created. |  [optional] |



