# ApigeeApi.GoogleCloudApigeeV1SecurityIncident

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detectionTypes** | **[String]** | Output only. Detection types which are part of the incident. Examples: Flooder, OAuth Abuser, Static Content Scraper, Anomaly Detection. | [optional] [readonly] 
**displayName** | **String** | Optional. Display name of the security incident. | [optional] 
**firstDetectedTime** | **String** | Output only. The time when events associated with the incident were first detected. | [optional] [readonly] 
**lastDetectedTime** | **String** | Output only. The time when events associated with the incident were last detected. | [optional] [readonly] 
**lastObservabilityChangeTime** | **String** | Output only. The time when the incident observability was last changed. | [optional] [readonly] 
**name** | **String** | Immutable. Name of the security incident resource. Format: organizations/{org}/environments/{environment}/securityIncidents/{incident} Example: organizations/apigee-org/environments/dev/securityIncidents/1234-5678-9101-1111 | [optional] 
**observability** | **String** | Optional. Indicates if the user archived this incident. | [optional] 
**riskLevel** | **String** | Output only. Risk level of the incident. | [optional] [readonly] 
**trafficCount** | **String** | Total traffic detected as part of the incident. | [optional] 



## Enum: ObservabilityEnum


* `OBSERVABILITY_UNSPECIFIED` (value: `"OBSERVABILITY_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `ARCHIVED` (value: `"ARCHIVED"`)





## Enum: RiskLevelEnum


* `RISK_LEVEL_UNSPECIFIED` (value: `"RISK_LEVEL_UNSPECIFIED"`)

* `LOW` (value: `"LOW"`)

* `MODERATE` (value: `"MODERATE"`)

* `SEVERE` (value: `"SEVERE"`)




