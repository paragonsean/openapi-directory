# AdSenseManagementApi.Alert

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** | Output only. The localized alert message. This may contain HTML markup, such as phrase elements or links. | [optional] [readonly] 
**name** | **String** | Output only. Resource name of the alert. Format: accounts/{account}/alerts/{alert} | [optional] [readonly] 
**severity** | **String** | Output only. Severity of this alert. | [optional] [readonly] 
**type** | **String** | Output only. Type of alert. This identifies the broad type of this alert, and provides a stable machine-readable identifier that will not be translated. For example, \&quot;payment-hold\&quot;. | [optional] [readonly] 



## Enum: SeverityEnum


* `SEVERITY_UNSPECIFIED` (value: `"SEVERITY_UNSPECIFIED"`)

* `INFO` (value: `"INFO"`)

* `WARNING` (value: `"WARNING"`)

* `SEVERE` (value: `"SEVERE"`)




