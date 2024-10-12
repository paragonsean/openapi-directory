

# GetWorkingLocationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**locationType** | [**LocationTypeEnum**](#LocationTypeEnum) | &lt;p&gt;Specify the type of the working location.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SAGEMAKER&lt;/code&gt; – Use the Amazon S3 location as a temporary location to store data content when working with FinSpace Notebooks that run on SageMaker studio.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;INGESTION&lt;/code&gt; – Use the Amazon S3 location as a staging location to copy your data content and then use the location with the Changeset creation operation.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |



## Enum: LocationTypeEnum

| Name | Value |
|---- | -----|
| INGESTION | &quot;INGESTION&quot; |
| SAGEMAKER | &quot;SAGEMAKER&quot; |



