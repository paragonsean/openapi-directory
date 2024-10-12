# AdExchangeBuyerApi.CreativeServingRestrictionsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contexts** | [**[CreativeServingRestrictionsInnerContextsInner]**](CreativeServingRestrictionsInnerContextsInner.md) | All known contexts/restrictions. | [optional] 
**disapprovalReasons** | [**[CreativeServingRestrictionsInnerDisapprovalReasonsInner]**](CreativeServingRestrictionsInnerDisapprovalReasonsInner.md) | The reasons for disapproval within this restriction, if any. Note that not all disapproval reasons may be categorized, so it is possible for the creative to have a status of DISAPPROVED or CONDITIONALLY_APPROVED with an empty list for disapproval_reasons. In this case, please reach out to your TAM to help debug the issue. | [optional] 
**reason** | **String** | Why the creative is ineligible to serve in this context (e.g., it has been explicitly disapproved or is pending review). | [optional] 


