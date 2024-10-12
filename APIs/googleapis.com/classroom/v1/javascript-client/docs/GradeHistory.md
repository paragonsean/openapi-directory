# GoogleClassroomApi.GradeHistory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actorUserId** | **String** | The teacher who made the grade change. | [optional] 
**gradeChangeType** | **String** | The type of grade change at this time in the submission grade history. | [optional] 
**gradeTimestamp** | **String** | When the grade of the submission was changed. | [optional] 
**maxPoints** | **Number** | The denominator of the grade at this time in the submission grade history. | [optional] 
**pointsEarned** | **Number** | The numerator of the grade at this time in the submission grade history. | [optional] 



## Enum: GradeChangeTypeEnum


* `UNKNOWN_GRADE_CHANGE_TYPE` (value: `"UNKNOWN_GRADE_CHANGE_TYPE"`)

* `DRAFT_GRADE_POINTS_EARNED_CHANGE` (value: `"DRAFT_GRADE_POINTS_EARNED_CHANGE"`)

* `ASSIGNED_GRADE_POINTS_EARNED_CHANGE` (value: `"ASSIGNED_GRADE_POINTS_EARNED_CHANGE"`)

* `MAX_POINTS_CHANGE` (value: `"MAX_POINTS_CHANGE"`)




