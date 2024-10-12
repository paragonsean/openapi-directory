

# RecommendedActionStateInfo

Contains information of current state for an Azure SQL Database, Server or Elastic Pool Recommended Action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionInitiatedBy** | [**ActionInitiatedByEnum**](#ActionInitiatedByEnum) | Gets who initiated the execution of this recommended action. Possible Value are: User    -&gt; When user explicitly notified system to apply the recommended action. System  -&gt; When auto-execute status of this advisor was set to &#39;Enabled&#39;, in which case the system applied it. |  [optional] [readonly] |
|**currentValue** | [**CurrentValueEnum**](#CurrentValueEnum) | Current state the recommended action is in. Some commonly used states are: Active      -&gt; recommended action is active and no action has been taken yet. Pending     -&gt; recommended action is approved for and is awaiting execution. Executing   -&gt; recommended action is being applied on the user database. Verifying   -&gt; recommended action was applied and is being verified of its usefulness by the system. Success     -&gt; recommended action was applied and improvement found during verification. Pending Revert  -&gt; verification found little or no improvement so recommended action is queued for revert or user has manually reverted. Reverting   -&gt; changes made while applying recommended action are being reverted on the user database. Reverted    -&gt; successfully reverted the changes made by recommended action on user database. Ignored     -&gt; user explicitly ignored/discarded the recommended action.  |  |
|**lastModified** | **OffsetDateTime** | Gets the time when the state was last modified |  [optional] [readonly] |



## Enum: ActionInitiatedByEnum

| Name | Value |
|---- | -----|
| USER | &quot;User&quot; |
| SYSTEM | &quot;System&quot; |



## Enum: CurrentValueEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| PENDING | &quot;Pending&quot; |
| EXECUTING | &quot;Executing&quot; |
| VERIFYING | &quot;Verifying&quot; |
| PENDING_REVERT | &quot;PendingRevert&quot; |
| REVERT_CANCELLED | &quot;RevertCancelled&quot; |
| REVERTING | &quot;Reverting&quot; |
| REVERTED | &quot;Reverted&quot; |
| IGNORED | &quot;Ignored&quot; |
| EXPIRED | &quot;Expired&quot; |
| MONITORING | &quot;Monitoring&quot; |
| RESOLVED | &quot;Resolved&quot; |
| SUCCESS | &quot;Success&quot; |
| ERROR | &quot;Error&quot; |



