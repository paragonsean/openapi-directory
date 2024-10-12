

# CleanupPolicyCondition

CleanupPolicyCondition is a set of conditions attached to a CleanupPolicy. If multiple entries are set, all must be satisfied for the condition to be satisfied.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**newerThan** | **String** | Match versions newer than a duration. |  [optional] |
|**olderThan** | **String** | Match versions older than a duration. |  [optional] |
|**packageNamePrefixes** | **List&lt;String&gt;** | Match versions by package prefix. Applied on any prefix match. |  [optional] |
|**tagPrefixes** | **List&lt;String&gt;** | Match versions by tag prefix. Applied on any prefix match. |  [optional] |
|**tagState** | [**TagStateEnum**](#TagStateEnum) | Match versions by tag status. |  [optional] |
|**versionNamePrefixes** | **List&lt;String&gt;** | Match versions by version name prefix. Applied on any prefix match. |  [optional] |



## Enum: TagStateEnum

| Name | Value |
|---- | -----|
| TAG_STATE_UNSPECIFIED | &quot;TAG_STATE_UNSPECIFIED&quot; |
| TAGGED | &quot;TAGGED&quot; |
| UNTAGGED | &quot;UNTAGGED&quot; |
| ANY | &quot;ANY&quot; |



