# MerakiDashboardApi.CreateOrganizationActionBatchRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**[CreateOrganizationActionBatchRequestActionsInner]**](CreateOrganizationActionBatchRequestActionsInner.md) | A set of changes to make as part of this action (&lt;a href&#x3D;&#39;https://developer.cisco.com/meraki/api/#/rest/guides/action-batches/&#39;&gt;more details&lt;/a&gt;) | 
**confirmed** | **Boolean** | Set to true for immediate execution. Set to false if the action should be previewed before executing. This property cannot be unset once it is true. Defaults to false. | [optional] 
**synchronous** | **Boolean** | Set to true to force the batch to run synchronous. There can be at most 20 actions in synchronous batch. Defaults to false. | [optional] 


