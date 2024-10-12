# AwsWellArchitectedTool.CreateWorkloadRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workloadName** | **String** | &lt;p&gt;The name of the workload.&lt;/p&gt; &lt;p&gt;The name must be unique within an account within an Amazon Web Services Region. Spaces and capitalization are ignored when checking for uniqueness.&lt;/p&gt; | 
**description** | **String** | The description for the workload. | 
**environment** | **String** | The environment for the workload. | 
**accountIds** | **[String]** | The list of Amazon Web Services account IDs associated with the workload. | [optional] 
**awsRegions** | **[String]** | The list of Amazon Web Services Regions associated with the workload, for example, &lt;code&gt;us-east-2&lt;/code&gt;, or &lt;code&gt;ca-central-1&lt;/code&gt;. | [optional] 
**nonAwsRegions** | **[String]** |  The list of non-Amazon Web Services Regions associated with the workload. | [optional] 
**pillarPriorities** | **[String]** | The priorities of the pillars, which are used to order items in the improvement plan. Each pillar is represented by its &lt;a&gt;PillarReviewSummary$PillarId&lt;/a&gt;. | [optional] 
**architecturalDesign** | **String** | The URL of the architectural design for the workload. | [optional] 
**reviewOwner** | **String** | The review owner of the workload. The name, email address, or identifier for the primary group or individual that owns the workload review process. | [optional] 
**industryType** | **String** | &lt;p&gt;The industry type for the workload.&lt;/p&gt; &lt;p&gt;If specified, must be one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Agriculture&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Automobile&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Defense&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Design and Engineering&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Digital Advertising&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Education&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Environmental Protection&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Financial Services&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Gaming&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;General Public Services&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Healthcare&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Hospitality&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;InfoTech&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Justice and Public Safety&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Life Sciences&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Manufacturing&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Media &amp;amp; Entertainment&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Mining &amp;amp; Resources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Oil &amp;amp; Gas&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Power &amp;amp; Utilities&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Professional Services&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Real Estate &amp;amp; Construction&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Retail &amp;amp; Wholesale&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Social Protection&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Telecommunications&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Travel, Transportation &amp;amp; Logistics&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Other&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
**industry** | **String** | The industry for the workload. | [optional] 
**lenses** | **[String]** | The list of lenses associated with the workload. Each lens is identified by its &lt;a&gt;LensSummary$LensAlias&lt;/a&gt;. | 
**notes** | **String** | The notes associated with the workload. | [optional] 
**clientRequestToken** | **String** | &lt;p&gt;A unique case-sensitive string used to ensure that this request is idempotent (executes only once).&lt;/p&gt; &lt;p&gt;You should not reuse the same token for other requests. If you retry a request with the same client request token and the same parameters after the original request has completed successfully, the result of the original request is returned.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This token is listed as required, however, if you do not specify it, the Amazon Web Services SDKs automatically generate one for you. If you are not using the Amazon Web Services SDK or the CLI, you must provide this token or the request will fail.&lt;/p&gt; &lt;/important&gt; | 
**tags** | **{String: String}** | The tags to be associated with the workload. | [optional] 
**discoveryConfig** | [**CreateWorkloadRequestDiscoveryConfig**](CreateWorkloadRequestDiscoveryConfig.md) |  | [optional] 
**applications** | **[String]** | List of AppRegistry application ARNs associated to the workload. | [optional] 
**profileArns** | **[String]** | The list of profile ARNs associated with the workload. | [optional] 



## Enum: EnvironmentEnum


* `PRODUCTION` (value: `"PRODUCTION"`)

* `PREPRODUCTION` (value: `"PREPRODUCTION"`)




