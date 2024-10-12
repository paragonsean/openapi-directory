

# GradeCategory

Details for a grade category in a course. Coursework may have zero or one grade category, and the category may be used in computing the overall grade. See the [help center article](https://support.google.com/edu/classroom/answer/9184995) for details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultGradeDenominator** | **Integer** | Default value of denominator. Only applicable when grade calculation type is TOTAL_POINTS. |  [optional] |
|**id** | **String** | ID of the grade category. |  [optional] |
|**name** | **String** | Name of the grade category. |  [optional] |
|**weight** | **Integer** | The weight of the category average as part of overall average. A weight of 12.34% is represented as 123400 (100% is 1,000,000). The last two digits should always be zero since we use two decimal precision. Only applicable when grade calculation type is WEIGHTED_CATEGORIES. |  [optional] |



