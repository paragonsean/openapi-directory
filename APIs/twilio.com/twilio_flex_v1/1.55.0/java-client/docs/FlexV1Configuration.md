

# FlexV1Configuration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Configuration resource. |  [optional] |
|**agentConvEndMethods** | **Object** | Agent conversation end methods. |  [optional] |
|**attributes** | **Object** | An object that contains application-specific data. |  [optional] |
|**callRecordingEnabled** | **Boolean** | Whether call recording is enabled. |  [optional] |
|**callRecordingWebhookUrl** | **URI** | The call recording webhook URL. |  [optional] |
|**channelConfigs** | **List&lt;Object&gt;** | Settings for different limits for Flex Conversations channels attachments. |  [optional] |
|**chatServiceInstanceSid** | **String** | The SID of the chat service this user belongs to. |  [optional] |
|**citrixVoiceVdi** | **Object** | Citrix voice vdi configuration and settings. |  [optional] |
|**crmAttributes** | **Object** | An object that contains the CRM attributes. |  [optional] |
|**crmCallbackUrl** | **URI** | The CRM Callback URL. |  [optional] |
|**crmEnabled** | **Boolean** | Whether CRM is present for Flex. |  [optional] |
|**crmFallbackUrl** | **URI** | The CRM Fallback URL. |  [optional] |
|**crmType** | **String** | The CRM type. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the Configuration resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the Configuration resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**debuggerIntegration** | **Object** | Configurable parameters for Debugger Integration. |  [optional] |
|**flexInsightsDrilldown** | **Boolean** | Setting this to true will redirect Flex UI to the URL set in flex_url |  [optional] |
|**flexInsightsHr** | **Object** | Object with enabled/disabled flag with list of workspaces. |  [optional] |
|**flexInstanceSid** | **String** | The SID of the Flex instance. |  [optional] |
|**flexServiceInstanceSid** | **String** | The SID of the Flex service instance. |  [optional] |
|**flexUiStatusReport** | **Object** | Configurable parameters for Flex UI Status report. |  [optional] |
|**flexUrl** | **URI** | URL to redirect to in case drilldown is enabled. |  [optional] |
|**integrations** | **List&lt;Object&gt;** | A list of objects that contain the configurations for the Integrations supported in this configuration. |  [optional] |
|**markdown** | **Object** | Configurable parameters for Markdown. |  [optional] |
|**messagingServiceInstanceSid** | **String** | The SID of the Messaging service instance. |  [optional] |
|**notifications** | **Object** | Configurable parameters for Notifications. |  [optional] |
|**offlineConfig** | **Object** | Presence and presence ttl configuration |  [optional] |
|**outboundCallFlows** | **Object** | The list of outbound call flows. |  [optional] |
|**pluginServiceAttributes** | **Object** | The plugin service attributes. |  [optional] |
|**pluginServiceEnabled** | **Boolean** | Whether the plugin service enabled. |  [optional] |
|**publicAttributes** | **Object** | The list of public attributes, which are visible to unauthenticated clients. |  [optional] |
|**queueStatsConfiguration** | **Object** | Configurable parameters for Queues Statistics. |  [optional] |
|**runtimeDomain** | **URI** | The URL where the Flex instance is hosted. |  [optional] |
|**serverlessServiceSids** | **List&lt;String&gt;** | The list of serverless service SIDs. |  [optional] |
|**serviceVersion** | **String** | The Flex Service version. |  [optional] |
|**status** | **ConfigurationEnumStatus** |  |  [optional] |
|**taskrouterOfflineActivitySid** | **String** | The TaskRouter SID of the offline activity. |  [optional] |
|**taskrouterSkills** | **List&lt;Object&gt;** | The Skill description for TaskRouter workers. |  [optional] |
|**taskrouterTargetTaskqueueSid** | **String** | The SID of the TaskRouter Target TaskQueue. |  [optional] |
|**taskrouterTargetWorkflowSid** | **String** | The SID of the TaskRouter target Workflow. |  [optional] |
|**taskrouterTaskqueues** | **List&lt;Object&gt;** | The list of TaskRouter TaskQueues. |  [optional] |
|**taskrouterWorkerAttributes** | **Object** | The TaskRouter Worker attributes. |  [optional] |
|**taskrouterWorkerChannels** | **Object** | The TaskRouter default channel capacities and availability for workers. |  [optional] |
|**taskrouterWorkspaceSid** | **String** | The SID of the TaskRouter Workspace. |  [optional] |
|**uiAttributes** | **Object** | The object that describes Flex UI characteristics and settings. |  [optional] |
|**uiDependencies** | **Object** | The object that defines the NPM packages and versions to be used in Hosted Flex. |  [optional] |
|**uiLanguage** | **String** | The primary language of the Flex UI. |  [optional] |
|**uiVersion** | **String** | The Pinned UI version. |  [optional] |
|**url** | **URI** | The absolute URL of the Configuration resource. |  [optional] |



