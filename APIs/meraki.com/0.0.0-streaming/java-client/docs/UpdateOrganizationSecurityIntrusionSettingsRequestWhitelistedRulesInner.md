

# UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | Message is optional and is ignored on a PUT call. It is allowed in order for PUT to be compatible with GET |  [optional] |
|**ruleId** | **String** | A rule identifier of the format meraki:intrusion/snort/GID/&lt;gid&gt;/SID/&lt;sid&gt;. gid and sid can be obtained from either https://www.snort.org/rule-docs or as ruleIds from the security events in /organization/[orgId]/securityEvents |  |



