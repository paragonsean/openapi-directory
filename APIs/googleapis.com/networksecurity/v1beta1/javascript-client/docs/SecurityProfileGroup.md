# NetworkSecurityApi.SecurityProfileGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Resource creation timestamp. | [optional] [readonly] 
**description** | **String** | Optional. An optional description of the profile group. Max length 2048 characters. | [optional] 
**etag** | **String** | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. | [optional] [readonly] 
**labels** | **{String: String}** | Optional. Labels as key value pairs. | [optional] 
**name** | **String** | Immutable. Identifier. Name of the SecurityProfileGroup resource. It matches pattern &#x60;projects|organizations/_*_/locations/{location}/securityProfileGroups/{security_profile_group}&#x60;. | [optional] 
**threatPreventionProfile** | **String** | Optional. Reference to a SecurityProfile with the threat prevention configuration for the SecurityProfileGroup. | [optional] 
**updateTime** | **String** | Output only. Last resource update timestamp. | [optional] [readonly] 


