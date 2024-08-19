# NetworkSecurityApi.SecurityProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Resource creation timestamp. | [optional] [readonly] 
**description** | **String** | Optional. An optional description of the profile. Max length 512 characters. | [optional] 
**etag** | **String** | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. | [optional] [readonly] 
**labels** | **{String: String}** | Optional. Labels as key value pairs. | [optional] 
**name** | **String** | Immutable. Identifier. Name of the SecurityProfile resource. It matches pattern &#x60;projects|organizations/_*_/locations/{location}/securityProfiles/{security_profile}&#x60;. | [optional] 
**threatPreventionProfile** | [**ThreatPreventionProfile**](ThreatPreventionProfile.md) |  | [optional] 
**type** | **String** | Immutable. The single ProfileType that the SecurityProfile resource configures. | [optional] 
**updateTime** | **String** | Output only. Last resource update timestamp. | [optional] [readonly] 



## Enum: TypeEnum


* `PROFILE_TYPE_UNSPECIFIED` (value: `"PROFILE_TYPE_UNSPECIFIED"`)

* `THREAT_PREVENTION` (value: `"THREAT_PREVENTION"`)




