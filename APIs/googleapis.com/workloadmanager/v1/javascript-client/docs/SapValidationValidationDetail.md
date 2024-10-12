# WorkloadManagerApi.SapValidationValidationDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **{String: String}** | Optional. The pairs of metrics data: field name &amp; field value. | [optional] 
**isPresent** | **Boolean** | Optional. Was there a SAP system detected for this validation type. | [optional] 
**sapValidationType** | **String** | Optional. The SAP system that the validation data is from. | [optional] 



## Enum: SapValidationTypeEnum


* `SAP_VALIDATION_TYPE_UNSPECIFIED` (value: `"SAP_VALIDATION_TYPE_UNSPECIFIED"`)

* `SYSTEM` (value: `"SYSTEM"`)

* `COROSYNC` (value: `"COROSYNC"`)

* `PACEMAKER` (value: `"PACEMAKER"`)

* `HANA` (value: `"HANA"`)

* `NETWEAVER` (value: `"NETWEAVER"`)

* `HANA_SECURITY` (value: `"HANA_SECURITY"`)

* `CUSTOM` (value: `"CUSTOM"`)




