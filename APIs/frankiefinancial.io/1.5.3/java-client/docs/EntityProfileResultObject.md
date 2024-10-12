

# EntityProfileResultObject

Contains the results of a check against an entity profile.   The entityProfileResult will be returned instead of a checkSummary to provide the full details of the verification process. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionRecommended** | **String** | The recommended onboarding action for this entity after the profile check this result refers to. The action can also be an entity state set by you. - UNCHECKED: New entity with no checks applied - PASS - FAIL - PASS_MANUAL: Manual intervention was applied to achieve a pass - FAIL_MANUAL: Manual intervention was applied but the entity still fails - REFER: Manual intervention required - WAIT: Externally applied state, waiting for more entity details - ARCHIVED: Externally applied state, entity hidden from on onboarding list - INACTIVE: Externally applied state, entity hidden from on onboarding list, indexes and further changes will be blocked.  |  [optional] |
|**addressResults** | [**Map&lt;String, EntityProfileItemMatchResultObject&gt;**](EntityProfileItemMatchResultObject.md) | KYC match counts for each checked address, whether matched or not. The keys in this map are the address IDs. The match type in the value will be either \&quot;curr_addr\&quot; or \&quot;prev_addr\&quot;. The resultant structure would look like:      \&quot;addressResults\&quot;: {       \&quot;addressId\&quot;: {         \&quot;matchType\&quot;: \&quot;curr_addr\&quot;,         \&quot;matchCount\&quot;: 5,         \&quot;verified\&quot;: true       },       \&quot;addressId\&quot;: {         \&quot;matchType\&quot;: \&quot;prev_addr\&quot;,         \&quot;matchCount\&quot;: 5,         \&quot;verified\&quot;: true       }     }  |  [optional] |
|**checkId** | **UUID** | Unique identifier for every check/comparison/verification. Make sure you reference this ID whenever updating check details. This ID will also be used when pushing check results back to you. |  [optional] |
|**checkResults** | [**List&lt;EntityProfileCheckResultMessage&gt;**](EntityProfileCheckResultMessage.md) | The basic result for each check type required for the profile.  The results are listed in the order they are run so you can also see how far progressed through a check process you are.  |  [optional] |
|**checkType** | **String** | Comma separated list of checks required for the entity profile. |  [optional] |
|**creditHeaderFailures** | **List&lt;String&gt;** | List of vendors from failed credit header sources. |  [optional] |
|**documentResults** | [**Map&lt;String, EntityProfileItemMatchResultObject&gt;**](EntityProfileItemMatchResultObject.md) | KYC match counts for each checked document, whether matched or not. The keys in this map are the document IDs. The match type in the value will be either \&quot;gov_id\&quot; or \&quot;other_id\&quot;. The resultant structure would look like:  documentResults: {     \&quot;documentId\&quot; : {       \&quot;matchType\&quot;: \&quot;gov_id\&quot;,       \&quot;matchCount\&quot;: 5,       \&quot;verified\&quot;: true     },     \&quot;documentId\&quot;: {       \&quot;matchType\&quot;: \&quot;other_id\&quot;,       \&quot;matchCount\&quot;: 5,       \&quot;verified\&quot;: true     } }  |  [optional] |
|**entityId** | **UUID** | Unique ID for the entity.  |  [optional] |
|**issueList** | **List&lt;String&gt;** |  |  [optional] |
|**kycResults** | [**List&lt;EntityProfileKYCMatchResultObject&gt;**](EntityProfileKYCMatchResultObject.md) | Summary of KYC match counts. |  [optional] |
|**latestCheckDate** | **OffsetDateTime** | The date and time of the last check that contributed to this result. |  [optional] |
|**manualIntervention** | **Boolean** | Indicates if any manual actions have been involved in the check result. |  [optional] |
|**policyName** | **String** | The name of the policy within the profile used for this check. This may or may not incorporate the &#39;riskPolicy&#39; that is also an attribute in this object. |  [optional] |
|**profileName** | **String** | The name of the profile used for this check. |  [optional] |
|**resolverRecommended** | **String** | Workflow hint by arrangement with Frankie |  [optional] |
|**riskLevel** | **String** | Risk level. One of:  - LOW,  - MEDIUM,  - HIGH,  - UACCEPTABLE  - or UNKNOWN  |  [optional] |
|**riskPolicy** | **String** | Risk policy. Contents depend on account configuration but would typically be one of:  - SDD,  - CDD,  - EDD  - or FAIL  |  [optional] |



