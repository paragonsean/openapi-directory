

# BucketLifecycleRuleInnerCondition

The condition(s) under which the action will be taken.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**age** | **Integer** | Age of an object (in days). This condition is satisfied when an object reaches the specified age. |  [optional] |
|**createdBefore** | **LocalDate** | A date in RFC 3339 format with only the date part, e.g. \&quot;2013-01-15\&quot;. This condition is satisfied when an object is created before midnight of the specified date in UTC. |  [optional] |
|**isLive** | **Boolean** | Relevant only for versioned objects. If the value is true, this condition matches live objects; if the value is false, it matches archived objects. |  [optional] |
|**numNewerVersions** | **Integer** | Relevant only for versioned objects. If the value is N, this condition is satisfied when there are at least N versions (including the live version) newer than this version of the object. |  [optional] |



