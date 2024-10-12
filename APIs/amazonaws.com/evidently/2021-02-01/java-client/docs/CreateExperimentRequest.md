

# CreateExperimentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | An optional description of the experiment. |  [optional] |
|**metricGoals** | [**List&lt;MetricGoalConfig&gt;**](MetricGoalConfig.md) | An array of structures that defines the metrics used for the experiment, and whether a higher or lower value for each metric is the goal. |  |
|**name** | **String** | A name for the new experiment. |  |
|**onlineAbConfig** | [**CreateExperimentRequestOnlineAbConfig**](CreateExperimentRequestOnlineAbConfig.md) |  |  [optional] |
|**randomizationSalt** | **String** | When Evidently assigns a particular user session to an experiment, it must use a randomization ID to determine which variation the user session is served. This randomization ID is a combination of the entity ID and &lt;code&gt;randomizationSalt&lt;/code&gt;. If you omit &lt;code&gt;randomizationSalt&lt;/code&gt;, Evidently uses the experiment name as the &lt;code&gt;randomizationSalt&lt;/code&gt;. |  [optional] |
|**samplingRate** | **Integer** | &lt;p&gt;The portion of the available audience that you want to allocate to this experiment, in thousandths of a percent. The available audience is the total audience minus the audience that you have allocated to overrides or current launches of this feature.&lt;/p&gt; &lt;p&gt;This is represented in thousandths of a percent. For example, specify 10,000 to allocate 10% of the available audience.&lt;/p&gt; |  [optional] |
|**segment** | **String** | Specifies an audience &lt;i&gt;segment&lt;/i&gt; to use in the experiment. When a segment is used in an experiment, only user sessions that match the segment pattern are used in the experiment. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | &lt;p&gt;Assigns one or more tags (key-value pairs) to the experiment.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with an experiment.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services resources&lt;/a&gt;.&lt;/p&gt; |  [optional] |
|**treatments** | [**List&lt;TreatmentConfig&gt;**](TreatmentConfig.md) | An array of structures that describe the configuration of each feature variation used in the experiment. |  |



