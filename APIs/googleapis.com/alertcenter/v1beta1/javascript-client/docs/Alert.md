# GoogleWorkspaceAlertCenterApi.Alert

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertId** | **String** | Output only. The unique identifier for the alert. | [optional] 
**createTime** | **String** | Output only. The time this alert was created. | [optional] 
**customerId** | **String** | Output only. The unique identifier of the Google Workspace account of the customer. | [optional] 
**data** | **{String: Object}** | Optional. The data associated with this alert, for example google.apps.alertcenter.type.DeviceCompromised. | [optional] 
**deleted** | **Boolean** | Output only. &#x60;True&#x60; if this alert is marked for deletion. | [optional] 
**endTime** | **String** | Optional. The time the event that caused this alert ceased being active. If provided, the end time must not be earlier than the start time. If not provided, it indicates an ongoing alert. | [optional] 
**etag** | **String** | Optional. &#x60;etag&#x60; is used for optimistic concurrency control as a way to help prevent simultaneous updates of an alert from overwriting each other. It is strongly suggested that systems make use of the &#x60;etag&#x60; in the read-modify-write cycle to perform alert updates in order to avoid race conditions: An &#x60;etag&#x60; is returned in the response which contains alerts, and systems are expected to put that etag in the request to update alert to ensure that their change will be applied to the same version of the alert. If no &#x60;etag&#x60; is provided in the call to update alert, then the existing alert is overwritten blindly. | [optional] 
**metadata** | [**AlertMetadata**](AlertMetadata.md) |  | [optional] 
**securityInvestigationToolLink** | **String** | Output only. An optional [Security Investigation Tool](https://support.google.com/a/answer/7575955) query for this alert. | [optional] 
**source** | **String** | Required. A unique identifier for the system that reported the alert. This is output only after alert is created. Supported sources are any of the following: * Google Operations * Mobile device management * Gmail phishing * Data Loss Prevention * Domain wide takeout * State sponsored attack * Google identity * Apps outage | [optional] 
**startTime** | **String** | Required. The time the event that caused this alert was started or detected. | [optional] 
**type** | **String** | Required. The type of the alert. This is output only after alert is created. For a list of available alert types see [Google Workspace Alert types](https://developers.google.com/admin-sdk/alertcenter/reference/alert-types). | [optional] 
**updateTime** | **String** | Output only. The time this alert was last updated. | [optional] 


