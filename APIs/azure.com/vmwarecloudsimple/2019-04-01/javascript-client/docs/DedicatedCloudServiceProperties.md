# VMwareCloudSimple.DedicatedCloudServiceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gatewaySubnet** | **String** | gateway Subnet for the account. It will collect the subnet address and always treat it as /28 | 
**isAccountOnboarded** | **String** | indicates whether account onboarded or not in a given region | [optional] [readonly] 
**nodes** | **Number** | total nodes purchased | [optional] [readonly] 
**serviceURL** | **String** | link to a service management web portal | [optional] [readonly] 



## Enum: IsAccountOnboardedEnum


* `notOnBoarded` (value: `"notOnBoarded"`)

* `onBoarded` (value: `"onBoarded"`)

* `onBoardingFailed` (value: `"onBoardingFailed"`)

* `onBoarding` (value: `"onBoarding"`)




