# GoogleClassroomApi.GradebookSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculationType** | **String** | Indicates how the overall grade is calculated. | [optional] 
**displaySetting** | **String** | Indicates who can see the overall grade.. | [optional] 
**gradeCategories** | [**[GradeCategory]**](GradeCategory.md) | Grade categories that are available for coursework in the course. | [optional] 



## Enum: CalculationTypeEnum


* `CALCULATION_TYPE_UNSPECIFIED` (value: `"CALCULATION_TYPE_UNSPECIFIED"`)

* `TOTAL_POINTS` (value: `"TOTAL_POINTS"`)

* `WEIGHTED_CATEGORIES` (value: `"WEIGHTED_CATEGORIES"`)





## Enum: DisplaySettingEnum


* `DISPLAY_SETTING_UNSPECIFIED` (value: `"DISPLAY_SETTING_UNSPECIFIED"`)

* `SHOW_OVERALL_GRADE` (value: `"SHOW_OVERALL_GRADE"`)

* `HIDE_OVERALL_GRADE` (value: `"HIDE_OVERALL_GRADE"`)

* `SHOW_TEACHERS_ONLY` (value: `"SHOW_TEACHERS_ONLY"`)




