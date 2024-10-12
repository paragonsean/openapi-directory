

# BucketLifecycleRuleInnerCondition

The condition(s) under which the action will be taken.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**age** | **Integer** | Age of an object (in days). This condition is satisfied when an object reaches the specified age. |  [optional] |
|**createdBefore** | **LocalDate** | A date in RFC 3339 format with only the date part (for instance, \&quot;2013-01-15\&quot;). This condition is satisfied when an object is created before midnight of the specified date in UTC. |  [optional] |
|**customTimeBefore** | **LocalDate** | A date in RFC 3339 format with only the date part (for instance, \&quot;2013-01-15\&quot;). This condition is satisfied when the custom time on an object is before this date in UTC. |  [optional] |
|**daysSinceCustomTime** | **Integer** | Number of days elapsed since the user-specified timestamp set on an object. The condition is satisfied if the days elapsed is at least this number. If no custom timestamp is specified on an object, the condition does not apply. |  [optional] |
|**daysSinceNoncurrentTime** | **Integer** | Number of days elapsed since the noncurrent timestamp of an object. The condition is satisfied if the days elapsed is at least this number. This condition is relevant only for versioned objects. The value of the field must be a nonnegative integer. If it&#39;s zero, the object version will become eligible for Lifecycle action as soon as it becomes noncurrent. |  [optional] |
|**isLive** | **Boolean** | Relevant only for versioned objects. If the value is true, this condition matches live objects; if the value is false, it matches archived objects. |  [optional] |
|**matchesPattern** | **String** | A regular expression that satisfies the RE2 syntax. This condition is satisfied when the name of the object matches the RE2 pattern. Note: This feature is currently in the \&quot;Early Access\&quot; launch stage and is only available to a whitelisted set of users; that means that this feature may be changed in backward-incompatible ways and that it is not guaranteed to be released. |  [optional] |
|**matchesPrefix** | **List&lt;String&gt;** | List of object name prefixes. This condition will be satisfied when at least one of the prefixes exactly matches the beginning of the object name. |  [optional] |
|**matchesStorageClass** | **List&lt;String&gt;** | Objects having any of the storage classes specified by this condition will be matched. Values include MULTI_REGIONAL, REGIONAL, NEARLINE, COLDLINE, ARCHIVE, STANDARD, and DURABLE_REDUCED_AVAILABILITY. |  [optional] |
|**matchesSuffix** | **List&lt;String&gt;** | List of object name suffixes. This condition will be satisfied when at least one of the suffixes exactly matches the end of the object name. |  [optional] |
|**noncurrentTimeBefore** | **LocalDate** | A date in RFC 3339 format with only the date part (for instance, \&quot;2013-01-15\&quot;). This condition is satisfied when the noncurrent time on an object is before this date in UTC. This condition is relevant only for versioned objects. |  [optional] |
|**numNewerVersions** | **Integer** | Relevant only for versioned objects. If the value is N, this condition is satisfied when there are at least N versions (including the live version) newer than this version of the object. |  [optional] |



