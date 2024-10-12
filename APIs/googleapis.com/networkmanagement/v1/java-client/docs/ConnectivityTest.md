

# ConnectivityTest

A Connectivity Test for a network reachability analysis.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time the test was created. |  [optional] [readonly] |
|**description** | **String** | The user-supplied description of the Connectivity Test. Maximum of 512 characters. |  [optional] |
|**destination** | [**Endpoint**](Endpoint.md) |  |  [optional] |
|**displayName** | **String** | Output only. The display name of a Connectivity Test. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Resource labels to represent user-provided metadata. |  [optional] |
|**name** | **String** | Required. Unique name of the resource using the form: &#x60;projects/{project_id}/locations/global/connectivityTests/{test_id}&#x60; |  [optional] |
|**probingDetails** | [**ProbingDetails**](ProbingDetails.md) |  |  [optional] |
|**protocol** | **String** | IP Protocol of the test. When not provided, \&quot;TCP\&quot; is assumed. |  [optional] |
|**reachabilityDetails** | [**ReachabilityDetails**](ReachabilityDetails.md) |  |  [optional] |
|**relatedProjects** | **List&lt;String&gt;** | Other projects that may be relevant for reachability analysis. This is applicable to scenarios where a test can cross project boundaries. |  [optional] |
|**source** | [**Endpoint**](Endpoint.md) |  |  [optional] |
|**updateTime** | **String** | Output only. The time the test&#39;s configuration was updated. |  [optional] [readonly] |



