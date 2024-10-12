

# GetExperimentResultsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseStat** | [**BaseStatEnum**](#BaseStatEnum) | The statistic used to calculate experiment results. Currently the only valid value is &lt;code&gt;mean&lt;/code&gt;, which uses the mean of the collected values as the statistic. |  [optional] |
|**endTime** | **OffsetDateTime** | The date and time that the experiment ended, if it is completed. This must be no longer than 30 days after the experiment start time. |  [optional] |
|**metricNames** | **List&lt;String&gt;** | The names of the experiment metrics that you want to see the results of. |  |
|**period** | **Integer** | In seconds, the amount of time to aggregate results together.  |  [optional] |
|**reportNames** | **List&lt;ExperimentReportName&gt;** | The names of the report types that you want to see. Currently, &lt;code&gt;BayesianInference&lt;/code&gt; is the only valid value. |  [optional] |
|**resultStats** | **List&lt;ExperimentResultRequestType&gt;** | &lt;p&gt;The statistics that you want to see in the returned results.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PValue&lt;/code&gt; specifies to use p-values for the results. A p-value is used in hypothesis testing to measure how often you are willing to make a mistake in rejecting the null hypothesis. A general practice is to reject the null hypothesis and declare that the results are statistically significant when the p-value is less than 0.05.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ConfidenceInterval&lt;/code&gt; specifies a confidence interval for the results. The confidence interval represents the range of values for the chosen metric that is likely to contain the true difference between the &lt;code&gt;baseStat&lt;/code&gt; of a variation and the baseline. Evidently returns the 95% confidence interval. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TreatmentEffect&lt;/code&gt; is the difference in the statistic specified by the &lt;code&gt;baseStat&lt;/code&gt; parameter between each variation and the default variation. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;BaseStat&lt;/code&gt; returns the statistical values collected for the metric for each variation. The statistic uses the same statistic specified in the &lt;code&gt;baseStat&lt;/code&gt; parameter. Therefore, if &lt;code&gt;baseStat&lt;/code&gt; is &lt;code&gt;mean&lt;/code&gt;, this returns the mean of the values collected for each variation.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**startTime** | **OffsetDateTime** | The date and time that the experiment started. |  [optional] |
|**treatmentNames** | **List&lt;String&gt;** | The names of the experiment treatments that you want to see the results for. |  |



## Enum: BaseStatEnum

| Name | Value |
|---- | -----|
| MEAN | &quot;Mean&quot; |



