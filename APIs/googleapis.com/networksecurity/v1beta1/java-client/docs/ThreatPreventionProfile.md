

# ThreatPreventionProfile

ThreatPreventionProfile defines an action for specific threat signatures or severity levels.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**severityOverrides** | [**List&lt;SeverityOverride&gt;**](SeverityOverride.md) | Optional. Configuration for overriding threats actions by severity match. |  [optional] |
|**threatOverrides** | [**List&lt;ThreatOverride&gt;**](ThreatOverride.md) | Optional. Configuration for overriding threats actions by threat_id match. If a threat is matched both by configuration provided in severity_overrides and threat_overrides, the threat_overrides action is applied. |  [optional] |



