# AmazonCloudWatchEvidently.UpdateExperimentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | An optional description of the experiment. | [optional] 
**metricGoals** | [**[MetricGoalConfig]**](MetricGoalConfig.md) | An array of structures that defines the metrics used for the experiment, and whether a higher or lower value for each metric is the goal. | [optional] 
**onlineAbConfig** | [**CreateExperimentRequestOnlineAbConfig**](CreateExperimentRequestOnlineAbConfig.md) |  | [optional] 
**randomizationSalt** | **String** | When Evidently assigns a particular user session to an experiment, it must use a randomization ID to determine which variation the user session is served. This randomization ID is a combination of the entity ID and &lt;code&gt;randomizationSalt&lt;/code&gt;. If you omit &lt;code&gt;randomizationSalt&lt;/code&gt;, Evidently uses the experiment name as the &lt;code&gt;randomizationSalt&lt;/code&gt;. | [optional] 
**removeSegment** | **Boolean** | Removes a segment from being used in an experiment. You can&#39;t use this parameter if the experiment is currently running. | [optional] 
**samplingRate** | **Number** | &lt;p&gt;The portion of the available audience that you want to allocate to this experiment, in thousandths of a percent. The available audience is the total audience minus the audience that you have allocated to overrides or current launches of this feature.&lt;/p&gt; &lt;p&gt;This is represented in thousandths of a percent. For example, specify 20,000 to allocate 20% of the available audience.&lt;/p&gt; | [optional] 
**segment** | **String** | Adds an audience &lt;i&gt;segment&lt;/i&gt; to an experiment. When a segment is used in an experiment, only user sessions that match the segment pattern are used in the experiment. You can&#39;t use this parameter if the experiment is currently running. | [optional] 
**treatments** | [**[TreatmentConfig]**](TreatmentConfig.md) | An array of structures that define the variations being tested in the experiment. | [optional] 


