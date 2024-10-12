# RudderApi.AgentKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **String** | Certification status of the security token (reset to &#x60;undefined&#x60; to trust a new certificate). If &#x60;certified&#x60;, inventory signature check will be enforced | [optional] 
**value** | **String** | Certificate (or public key for &lt;6.0 agents) used by the agent. Be careful write a \&quot;\\n\&quot; after header line and before footer line, JSON does not keep formatting in string. | 



## Enum: StatusEnum


* `certified` (value: `"certified"`)

* `undefined` (value: `"undefined"`)




