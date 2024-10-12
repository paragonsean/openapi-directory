# AwsRoboMaker.CreateSimulationJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientRequestToken** | **String** | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. | [optional] 
**outputLocation** | [**CreateSimulationJobRequestOutputLocation**](CreateSimulationJobRequestOutputLocation.md) |  | [optional] 
**loggingConfig** | [**CreateSimulationJobRequestLoggingConfig**](CreateSimulationJobRequestLoggingConfig.md) |  | [optional] 
**maxJobDurationInSeconds** | **Number** | The maximum simulation job duration in seconds (up to 14 days or 1,209,600 seconds. When &lt;code&gt;maxJobDurationInSeconds&lt;/code&gt; is reached, the simulation job will status will transition to &lt;code&gt;Completed&lt;/code&gt;. | 
**iamRole** | **String** | The IAM role name that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf. This is how credentials are passed in to your simulation job.  | 
**failureBehavior** | **String** | &lt;p&gt;The failure behavior the simulation job.&lt;/p&gt; &lt;dl&gt; &lt;dt&gt;Continue&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Leaves the instance running for its maximum timeout duration after a &lt;code&gt;4XX&lt;/code&gt; error code.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;Fail&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Stop the simulation job and terminate the instance.&lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt; | [optional] 
**robotApplications** | [**[RobotApplicationConfig]**](RobotApplicationConfig.md) | The robot application to use in the simulation job. | [optional] 
**simulationApplications** | [**[SimulationApplicationConfig]**](SimulationApplicationConfig.md) | The simulation application to use in the simulation job. | [optional] 
**dataSources** | [**[DataSourceConfig]**](DataSourceConfig.md) | &lt;p&gt;Specify data sources to mount read-only files from S3 into your simulation. These files are available under &lt;code&gt;/opt/robomaker/datasources/data_source_name&lt;/code&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;There is a limit of 100 files and a combined size of 25GB for all &lt;code&gt;DataSourceConfig&lt;/code&gt; objects. &lt;/p&gt; &lt;/note&gt; | [optional] 
**tags** | **{String: String}** | A map that contains tag keys and tag values that are attached to the simulation job. | [optional] 
**vpcConfig** | [**CreateSimulationJobRequestVpcConfig**](CreateSimulationJobRequestVpcConfig.md) |  | [optional] 
**compute** | [**CreateSimulationJobRequestCompute**](CreateSimulationJobRequestCompute.md) |  | [optional] 



## Enum: FailureBehaviorEnum


* `Fail` (value: `"Fail"`)

* `Continue` (value: `"Continue"`)




