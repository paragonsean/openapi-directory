

# Feed

A class of notifications that an application can register to receive. For example: \"all roster changes for a domain\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**courseRosterChangesInfo** | [**CourseRosterChangesInfo**](CourseRosterChangesInfo.md) |  |  [optional] |
|**courseWorkChangesInfo** | [**CourseWorkChangesInfo**](CourseWorkChangesInfo.md) |  |  [optional] |
|**feedType** | [**FeedTypeEnum**](#FeedTypeEnum) | The type of feed. |  [optional] |



## Enum: FeedTypeEnum

| Name | Value |
|---- | -----|
| FEED_TYPE_UNSPECIFIED | &quot;FEED_TYPE_UNSPECIFIED&quot; |
| DOMAIN_ROSTER_CHANGES | &quot;DOMAIN_ROSTER_CHANGES&quot; |
| COURSE_ROSTER_CHANGES | &quot;COURSE_ROSTER_CHANGES&quot; |
| COURSE_WORK_CHANGES | &quot;COURSE_WORK_CHANGES&quot; |



