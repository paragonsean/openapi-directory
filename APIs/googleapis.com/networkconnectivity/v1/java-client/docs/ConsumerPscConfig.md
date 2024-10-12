

# ConsumerPscConfig

Allow the producer to specify which consumers can connect to it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disableGlobalAccess** | **Boolean** | This is used in PSC consumer ForwardingRule to control whether the PSC endpoint can be accessed from another region. |  [optional] |
|**network** | **String** | The resource path of the consumer network where PSC connections are allowed to be created in. Note, this network does not need be in the ConsumerPscConfig.project in the case of SharedVPC. Example: projects/{projectNumOrId}/global/networks/{networkId}. |  [optional] |
|**project** | **String** | The consumer project where PSC connections are allowed to be created in. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Overall state of PSC Connections management for this consumer psc config. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| VALID | &quot;VALID&quot; |
| CONNECTION_POLICY_MISSING | &quot;CONNECTION_POLICY_MISSING&quot; |
| POLICY_LIMIT_REACHED | &quot;POLICY_LIMIT_REACHED&quot; |



