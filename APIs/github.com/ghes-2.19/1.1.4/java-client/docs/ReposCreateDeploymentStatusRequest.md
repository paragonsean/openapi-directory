

# ReposCreateDeploymentStatusRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoInactive** | **Boolean** | Adds a new &#x60;inactive&#x60; status to all prior non-transient, non-production environment deployments with the same repository and &#x60;environment&#x60; name as the created status&#39;s deployment. An &#x60;inactive&#x60; status is only added to deployments that had a &#x60;success&#x60; state. Default: &#x60;true&#x60;   **Note:** To add an &#x60;inactive&#x60; status to &#x60;production&#x60; environments, you must use the [&#x60;application/vnd.github.flash-preview+json&#x60;](https://docs.github.com/enterprise-server@2.19/rest/overview/api-previews#deployment-statuses) custom media type.   **Note:** This parameter requires you to use the [&#x60;application/vnd.github.ant-man-preview+json&#x60;](https://docs.github.com/enterprise-server@2.19/rest/overview/api-previews#enhanced-deployments) custom media type. |  [optional] |
|**description** | **String** | A short description of the status. The maximum description length is 140 characters. |  [optional] |
|**environment** | [**EnvironmentEnum**](#EnvironmentEnum) | Name for the target deployment environment, which can be changed when setting a deploy status. For example, &#x60;production&#x60;, &#x60;staging&#x60;, or &#x60;qa&#x60;. **Note:** This parameter requires you to use the [&#x60;application/vnd.github.flash-preview+json&#x60;](https://docs.github.com/enterprise-server@2.19/rest/overview/api-previews#deployment-statuses) custom media type. |  [optional] |
|**environmentUrl** | **String** | Sets the URL for accessing your environment. Default: &#x60;\&quot;\&quot;&#x60;   **Note:** This parameter requires you to use the [&#x60;application/vnd.github.ant-man-preview+json&#x60;](https://docs.github.com/enterprise-server@2.19/rest/overview/api-previews#enhanced-deployments) custom media type. |  [optional] |
|**logUrl** | **String** | The full URL of the deployment&#39;s output. This parameter replaces &#x60;target_url&#x60;. We will continue to accept &#x60;target_url&#x60; to support legacy uses, but we recommend replacing &#x60;target_url&#x60; with &#x60;log_url&#x60;. Setting &#x60;log_url&#x60; will automatically set &#x60;target_url&#x60; to the same value. Default: &#x60;\&quot;\&quot;&#x60;   **Note:** This parameter requires you to use the [&#x60;application/vnd.github.ant-man-preview+json&#x60;](https://docs.github.com/enterprise-server@2.19/rest/overview/api-previews#enhanced-deployments) custom media type. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the status. Can be one of &#x60;error&#x60;, &#x60;failure&#x60;, &#x60;inactive&#x60;, &#x60;in_progress&#x60;, &#x60;queued&#x60; &#x60;pending&#x60;, or &#x60;success&#x60;. **Note:** To use the &#x60;inactive&#x60; state, you must provide the [&#x60;application/vnd.github.ant-man-preview+json&#x60;](https://docs.github.com/enterprise-server@2.19/rest/overview/api-previews#enhanced-deployments) custom media type. To use the &#x60;in_progress&#x60; and &#x60;queued&#x60; states, you must provide the [&#x60;application/vnd.github.flash-preview+json&#x60;](https://docs.github.com/enterprise-server@2.19/rest/overview/api-previews#deployment-statuses) custom media type. When you set a transient deployment to &#x60;inactive&#x60;, the deployment will be shown as &#x60;destroyed&#x60; in GitHub. |  |
|**targetUrl** | **String** | The target URL to associate with this status. This URL should contain output to keep the user updated while the task is running or serve as historical information for what happened in the deployment. **Note:** It&#39;s recommended to use the &#x60;log_url&#x60; parameter, which replaces &#x60;target_url&#x60;. |  [optional] |



## Enum: EnvironmentEnum

| Name | Value |
|---- | -----|
| PRODUCTION | &quot;production&quot; |
| STAGING | &quot;staging&quot; |
| QA | &quot;qa&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ERROR | &quot;error&quot; |
| FAILURE | &quot;failure&quot; |
| INACTIVE | &quot;inactive&quot; |
| IN_PROGRESS | &quot;in_progress&quot; |
| QUEUED | &quot;queued&quot; |
| PENDING | &quot;pending&quot; |
| SUCCESS | &quot;success&quot; |



