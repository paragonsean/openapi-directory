# WorkloadManagerApi.Evaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigQueryDestination** | [**BigQueryDestination**](BigQueryDestination.md) |  | [optional] 
**createTime** | **String** | Output only. [Output only] Create time stamp | [optional] [readonly] 
**customRulesBucket** | **String** | The Cloud Storage bucket name for custom rules. | [optional] 
**description** | **String** | Description of the Evaluation | [optional] 
**labels** | **{String: String}** | Labels as key value pairs | [optional] 
**name** | **String** | name of resource names have the form &#39;projects/{project_id}/locations/{location_id}/evaluations/{evaluation_id}&#39; | [optional] 
**resourceFilter** | [**ResourceFilter**](ResourceFilter.md) |  | [optional] 
**resourceStatus** | [**ResourceStatus**](ResourceStatus.md) |  | [optional] 
**ruleNames** | **[String]** | the name of the rule | [optional] 
**ruleVersions** | **[String]** | Output only. [Output only] The updated rule ids if exist. | [optional] [readonly] 
**schedule** | **String** | crontab format schedule for scheduled evaluation, currently only support the following schedule: \&quot;0 *_/1 * * *\&quot;, \&quot;0 *_/6 * * *\&quot;, \&quot;0 *_/12 * * *\&quot;, \&quot;0 0 *_/1 * *\&quot;, \&quot;0 0 *_/7 * *\&quot;, | [optional] 
**updateTime** | **String** | Output only. [Output only] Update time stamp | [optional] [readonly] 


