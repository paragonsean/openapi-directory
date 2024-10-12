

# UpdateWorkloadInput

Input to update a workload.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**workloadName** | **String** | &lt;p&gt;The name of the workload.&lt;/p&gt; &lt;p&gt;The name must be unique within an account within an Amazon Web Services Region. Spaces and capitalization are ignored when checking for uniqueness.&lt;/p&gt; |  [optional] |
|**description** | **String** | The description for the workload. |  [optional] |
|**environment** | **WorkloadEnvironment** |  |  [optional] |
|**accountIds** | **List&lt;String&gt;** | The list of Amazon Web Services account IDs associated with the workload. |  [optional] |
|**awsRegions** | **List&lt;String&gt;** | The list of Amazon Web Services Regions associated with the workload, for example, &lt;code&gt;us-east-2&lt;/code&gt;, or &lt;code&gt;ca-central-1&lt;/code&gt;. |  [optional] |
|**nonAwsRegions** | **List&lt;String&gt;** |  The list of non-Amazon Web Services Regions associated with the workload. |  [optional] |
|**pillarPriorities** | **List&lt;String&gt;** | The priorities of the pillars, which are used to order items in the improvement plan. Each pillar is represented by its &lt;a&gt;PillarReviewSummary$PillarId&lt;/a&gt;. |  [optional] |
|**architecturalDesign** | **String** | The URL of the architectural design for the workload. |  [optional] |
|**reviewOwner** | **String** | The review owner of the workload. The name, email address, or identifier for the primary group or individual that owns the workload review process. |  [optional] |
|**isReviewOwnerUpdateAcknowledged** | [**Boolean**](Boolean.md) |  |  [optional] |
|**industryType** | **String** | &lt;p&gt;The industry type for the workload.&lt;/p&gt; &lt;p&gt;If specified, must be one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Agriculture&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Automobile&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Defense&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Design and Engineering&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Digital Advertising&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Education&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Environmental Protection&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Financial Services&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Gaming&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;General Public Services&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Healthcare&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Hospitality&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;InfoTech&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Justice and Public Safety&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Life Sciences&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Manufacturing&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Media &amp;amp; Entertainment&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Mining &amp;amp; Resources&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Oil &amp;amp; Gas&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Power &amp;amp; Utilities&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Professional Services&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Real Estate &amp;amp; Construction&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Retail &amp;amp; Wholesale&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Social Protection&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Telecommunications&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Travel, Transportation &amp;amp; Logistics&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Other&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**industry** | **String** | The industry for the workload. |  [optional] |
|**notes** | **String** | The notes associated with the workload. |  [optional] |
|**improvementStatus** | **WorkloadImprovementStatus** |  |  [optional] |
|**discoveryConfig** | [**UpdateWorkloadInputDiscoveryConfig**](UpdateWorkloadInputDiscoveryConfig.md) |  |  [optional] |
|**applications** | [**List**](List.md) |  |  [optional] |



