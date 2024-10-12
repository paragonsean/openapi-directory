

# GoogleCloudPolicysimulatorV1betaBindingExplanationAnnotatedMembership

Details about whether the binding includes the principal.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**membership** | [**MembershipEnum**](#MembershipEnum) | Indicates whether the binding includes the principal. |  [optional] |
|**relevance** | [**RelevanceEnum**](#RelevanceEnum) | The relevance of the principal&#39;s status to the overall determination for the binding. |  [optional] |



## Enum: MembershipEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;MEMBERSHIP_UNSPECIFIED&quot; |
| INCLUDED | &quot;MEMBERSHIP_INCLUDED&quot; |
| NOT_INCLUDED | &quot;MEMBERSHIP_NOT_INCLUDED&quot; |
| UNKNOWN_INFO_DENIED | &quot;MEMBERSHIP_UNKNOWN_INFO_DENIED&quot; |
| UNKNOWN_UNSUPPORTED | &quot;MEMBERSHIP_UNKNOWN_UNSUPPORTED&quot; |



## Enum: RelevanceEnum

| Name | Value |
|---- | -----|
| HEURISTIC_RELEVANCE_UNSPECIFIED | &quot;HEURISTIC_RELEVANCE_UNSPECIFIED&quot; |
| NORMAL | &quot;NORMAL&quot; |
| HIGH | &quot;HIGH&quot; |



