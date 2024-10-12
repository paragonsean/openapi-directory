# GmailPostmasterToolsApi.IpReputation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipCount** | **String** | Total number of unique IPs in this reputation category. This metric only pertains to traffic that passed [SPF](http://www.openspf.org/) or [DKIM](http://www.dkim.org/). | [optional] 
**reputation** | **String** | The reputation category this IP reputation represents. | [optional] 
**sampleIps** | **[String]** | A sample of IPs in this reputation category. | [optional] 



## Enum: ReputationEnum


* `REPUTATION_CATEGORY_UNSPECIFIED` (value: `"REPUTATION_CATEGORY_UNSPECIFIED"`)

* `HIGH` (value: `"HIGH"`)

* `MEDIUM` (value: `"MEDIUM"`)

* `LOW` (value: `"LOW"`)

* `BAD` (value: `"BAD"`)




