# NetworkSecurityApi.ThreatOverride

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Required. Threat action override. For some threat types, only a subset of actions applies. | [optional] 
**threatId** | **String** | Required. Vendor-specific ID of a threat to override. | [optional] 
**type** | **String** | Output only. Type of the threat (read only). | [optional] [readonly] 



## Enum: ActionEnum


* `THREAT_ACTION_UNSPECIFIED` (value: `"THREAT_ACTION_UNSPECIFIED"`)

* `DEFAULT_ACTION` (value: `"DEFAULT_ACTION"`)

* `ALLOW` (value: `"ALLOW"`)

* `ALERT` (value: `"ALERT"`)

* `DENY` (value: `"DENY"`)





## Enum: TypeEnum


* `THREAT_TYPE_UNSPECIFIED` (value: `"THREAT_TYPE_UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `VULNERABILITY` (value: `"VULNERABILITY"`)

* `ANTIVIRUS` (value: `"ANTIVIRUS"`)

* `SPYWARE` (value: `"SPYWARE"`)

* `DNS` (value: `"DNS"`)




