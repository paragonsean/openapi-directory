

# WageSetting

An object representing a team member's wage information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** | The timestamp, in RFC 3339 format, describing when the wage setting object was created. For example, \&quot;2018-10-04T04:00:00-07:00\&quot; or \&quot;2019-02-05T12:00:00Z\&quot;. |  [optional] |
|**isOvertimeExempt** | **Boolean** | Whether the team member is exempt from the overtime rules of the seller&#39;s country. |  [optional] |
|**jobAssignments** | [**List&lt;JobAssignment&gt;**](JobAssignment.md) | Required. The ordered list of jobs that the team member is assigned to. The first job assignment is considered the team member&#39;s primary job.  The minimum length is 1 and the maximum length is 12. |  [optional] |
|**teamMemberId** | **String** | The unique ID of the &#x60;TeamMember&#x60; whom this wage setting describes. |  [optional] |
|**updatedAt** | **String** | The timestamp, in RFC 3339 format, describing when the wage setting object was last updated. For example, \&quot;2018-10-04T04:00:00-07:00\&quot; or \&quot;2019-02-05T12:00:00Z\&quot;. |  [optional] |
|**version** | **Integer** | Used for resolving concurrency issues. The request fails if the version provided does not match the server version at the time of the request. If not provided, Square executes a blind write, potentially overwriting data from another write. For more information, see [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency). |  [optional] |



