

# SecurityProfile

SecurityProfile is a resource that defines the behavior for one of many ProfileTypes. Next ID: 9

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Resource creation timestamp. |  [optional] [readonly] |
|**description** | **String** | Optional. An optional description of the profile. Max length 512 characters. |  [optional] |
|**etag** | **String** | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Labels as key value pairs. |  [optional] |
|**name** | **String** | Immutable. Identifier. Name of the SecurityProfile resource. It matches pattern &#x60;projects|organizations/_*_/locations/{location}/securityProfiles/{security_profile}&#x60;. |  [optional] |
|**threatPreventionProfile** | [**ThreatPreventionProfile**](ThreatPreventionProfile.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Immutable. The single ProfileType that the SecurityProfile resource configures. |  [optional] |
|**updateTime** | **String** | Output only. Last resource update timestamp. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PROFILE_TYPE_UNSPECIFIED | &quot;PROFILE_TYPE_UNSPECIFIED&quot; |
| THREAT_PREVENTION | &quot;THREAT_PREVENTION&quot; |



