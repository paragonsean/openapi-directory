# IxApi.MemberJoiningRuleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacityMax** | **Number** | An optional rate limit which has precedence over the capacity set in the network service config. | [optional] 
**capacityMin** | **Number** | Require an optional minimum capacity to join the network service. | [optional] 
**consumingAccount** | **String** | The &#x60;id&#x60; of the account to which access to the network service should be granted or denied.  | 
**externalRef** | **String** | Reference field, free to use for the API user. | [optional] 
**managingAccount** | **String** | The &#x60;id&#x60; of the account responsible for managing the service via the API. A manager can read and update the state of entities.  | 
**networkService** | **String** |  | 
**type** | **String** |  | 


