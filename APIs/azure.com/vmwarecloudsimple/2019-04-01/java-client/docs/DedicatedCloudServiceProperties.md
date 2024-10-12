

# DedicatedCloudServiceProperties

Properties of dedicated cloud service

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gatewaySubnet** | **String** | gateway Subnet for the account. It will collect the subnet address and always treat it as /28 |  |
|**isAccountOnboarded** | [**IsAccountOnboardedEnum**](#IsAccountOnboardedEnum) | indicates whether account onboarded or not in a given region |  [optional] [readonly] |
|**nodes** | **Integer** | total nodes purchased |  [optional] [readonly] |
|**serviceURL** | **String** | link to a service management web portal |  [optional] [readonly] |



## Enum: IsAccountOnboardedEnum

| Name | Value |
|---- | -----|
| NOT_ON_BOARDED | &quot;notOnBoarded&quot; |
| ON_BOARDED | &quot;onBoarded&quot; |
| ON_BOARDING_FAILED | &quot;onBoardingFailed&quot; |
| ON_BOARDING | &quot;onBoarding&quot; |



