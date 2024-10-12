# RubrikRestApi.BatchVmwareVmMissedRecoverableRangesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**afterTime** | **Date** | Query filter - only ranges that occur after this time are included. The date-time string should be in ISO8601 format. For example, &#x60;2018-01-01T01:23:45.678Z&#x60;. | [optional] 
**beforeTime** | **Date** | Query filter - only ranges that occur before this time are included. The date-time string should be in ISO8601 format. For example, &#x60;2018-01-01T01:23:45.678Z&#x60;. | [optional] 
**vmIds** | **[String]** | ID of each CDP-enabled virtual machine for which missed recoverable ranges are being retrieved. | 


