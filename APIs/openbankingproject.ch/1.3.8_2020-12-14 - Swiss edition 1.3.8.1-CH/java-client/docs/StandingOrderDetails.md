

# StandingOrderDetails

Details of underlying standing orders. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfExecution** | **DayOfExecution** |  |  [optional] |
|**endDate** | **LocalDate** | The last applicable day of execution. If not given, it is an infinite standing order.  |  [optional] |
|**executionRule** | **ExecutionRule** |  |  [optional] |
|**frequency** | **FrequencyCode** |  |  |
|**limitAmount** | [**Amount**](Amount.md) |  |  [optional] |
|**monthsOfExecution** | [**List&lt;MonthsOfExecutionEnum&gt;**](#List&lt;MonthsOfExecutionEnum&gt;) | The format is following the regular expression \\d{1,2}.  The array is restricted to 11 entries.  The values contained in the array entries shall all be different and the maximum value of one entry is 12. This attribute is contained if and only if the frequency equals \&quot;MonthlyVariable\&quot;. Example: An execution on January, April and October each year is addressed by [\&quot;1\&quot;, \&quot;4\&quot;, \&quot;10\&quot;].  |  [optional] |
|**multiplicator** | **Integer** | This is multiplying the given frequency resulting the exact frequency, e.g. Frequency&#x3D;weekly and multiplicator&#x3D;3 means every 3 weeks. Remark: This attribute is rarely supported in the market.  |  [optional] |
|**startDate** | **LocalDate** | The first applicable day of execution starting from this date is the first payment.  |  |
|**withinAMonthFlag** | **Boolean** | This element is only used in case of frequency equals \&quot;Monthly\&quot;.  If this element equals false it has no effect. If this element equals true, then the execution rule is overruled if the day of execution would fall into a different month using the execution rule.  Example: executionRule equals \&quot;preceding\&quot;, dayOfExecution equals \&quot;02\&quot; and the second of a month is a Sunday.  In this case, the transaction date would be on the last day of the month before.  This would be overruled if withinAMonthFlag equals true and the payment is processed on Monday the third of the Month. Remark: This attribute is rarely supported in the market.  |  [optional] |



## Enum: List&lt;MonthsOfExecutionEnum&gt;

| Name | Value |
|---- | -----|
| _1 | &quot;1&quot; |
| _2 | &quot;2&quot; |
| _3 | &quot;3&quot; |
| _4 | &quot;4&quot; |
| _5 | &quot;5&quot; |
| _6 | &quot;6&quot; |
| _7 | &quot;7&quot; |
| _8 | &quot;8&quot; |
| _9 | &quot;9&quot; |
| _10 | &quot;10&quot; |
| _11 | &quot;11&quot; |
| _12 | &quot;12&quot; |



