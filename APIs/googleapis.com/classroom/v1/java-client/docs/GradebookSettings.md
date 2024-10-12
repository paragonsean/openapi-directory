

# GradebookSettings

The gradebook settings for a course. See the [help center article](https://support.google.com/edu/classroom/answer/9184995) for details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**calculationType** | [**CalculationTypeEnum**](#CalculationTypeEnum) | Indicates how the overall grade is calculated. |  [optional] |
|**displaySetting** | [**DisplaySettingEnum**](#DisplaySettingEnum) | Indicates who can see the overall grade.. |  [optional] |
|**gradeCategories** | [**List&lt;GradeCategory&gt;**](GradeCategory.md) | Grade categories that are available for coursework in the course. |  [optional] |



## Enum: CalculationTypeEnum

| Name | Value |
|---- | -----|
| CALCULATION_TYPE_UNSPECIFIED | &quot;CALCULATION_TYPE_UNSPECIFIED&quot; |
| TOTAL_POINTS | &quot;TOTAL_POINTS&quot; |
| WEIGHTED_CATEGORIES | &quot;WEIGHTED_CATEGORIES&quot; |



## Enum: DisplaySettingEnum

| Name | Value |
|---- | -----|
| DISPLAY_SETTING_UNSPECIFIED | &quot;DISPLAY_SETTING_UNSPECIFIED&quot; |
| SHOW_OVERALL_GRADE | &quot;SHOW_OVERALL_GRADE&quot; |
| HIDE_OVERALL_GRADE | &quot;HIDE_OVERALL_GRADE&quot; |
| SHOW_TEACHERS_ONLY | &quot;SHOW_TEACHERS_ONLY&quot; |



