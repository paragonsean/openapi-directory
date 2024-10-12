# InfluxOssApiService.OnboardingRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **String** |  | 
**org** | **String** |  | 
**password** | **String** |  | [optional] 
**retentionPeriodHrs** | **Number** | Retention period *in nanoseconds* for the new bucket. This key&#39;s name has been misleading since OSS 2.0 GA, please transition to use &#x60;retentionPeriodSeconds&#x60;  | [optional] 
**retentionPeriodSeconds** | **Number** |  | [optional] 
**token** | **String** | Authentication token to set on the initial user. If not specified, the server will generate a token.  | [optional] 
**username** | **String** |  | 


