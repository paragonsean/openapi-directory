# AdExchangeBuyerApiIi.TargetingCriteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusions** | [**[TargetingValue]**](TargetingValue.md) | The list of values to exclude from targeting. Each value is AND&#39;d together. | [optional] 
**inclusions** | [**[TargetingValue]**](TargetingValue.md) | The list of value to include as part of the targeting. Each value is OR&#39;d together. | [optional] 
**key** | **String** | The key representing the shared targeting criterion. Targeting criteria defined by Google ad servers will begin with GOOG_. Third parties may define their own keys. A list of permissible keys along with the acceptable values will be provided as part of the external documentation. | [optional] 


