# LinodeApi.GrantsResponseGlobal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountAccess** | **String** | The level of access this User has to Account-level actions, like billing information. A restricted User will never be able to manage users.  | [optional] 
**addDatabases** | **Boolean** | if true, this User may add Managed Databases. | [optional] 
**addDomains** | **Boolean** | If true, this User may add Domains. | [optional] 
**addFirewalls** | **Boolean** | If true, this User may add Firewalls. | [optional] 
**addImages** | **Boolean** | If true, this User may add Images. | [optional] 
**addLinodes** | **Boolean** | If true, this User may create Linodes. | [optional] 
**addLongview** | **Boolean** | If true, this User may create Longview clients and view the current plan. | [optional] 
**addNodebalancers** | **Boolean** | If true, this User may add NodeBalancers. | [optional] 
**addStackscripts** | **Boolean** | If true, this User may add StackScripts. | [optional] 
**addVolumes** | **Boolean** | If true, this User may add Volumes. | [optional] 
**cancelAccount** | **Boolean** | If true, this User may cancel the entire Account. | [optional] 
**longviewSubscription** | **Boolean** | If true, this User may manage the Account&#39;s Longview subscription. | [optional] 



## Enum: AccountAccessEnum


* `only` (value: `"read_only"`)

* `write` (value: `"read_write"`)




