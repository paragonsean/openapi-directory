

# MemberJoiningRuleRequestPartial

Polymorphic Member Joining Rule Request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacityMax** | **Integer** | An optional rate limit which has precedence over the capacity set in the network service config. |  [optional] |
|**capacityMin** | **Integer** | Require an optional minimum capacity to join the network service. |  [optional] |
|**consumingAccount** | **String** | The &#x60;id&#x60; of the account to which access to the network service should be granted or denied.  |  [optional] |
|**externalRef** | **String** | Reference field, free to use for the API user. |  [optional] |
|**managingAccount** | **String** | The &#x60;id&#x60; of the account responsible for managing the service via the API. A manager can read and update the state of entities.  |  [optional] |
|**networkService** | **String** |  |  [optional] |
|**type** | **String** |  |  |



