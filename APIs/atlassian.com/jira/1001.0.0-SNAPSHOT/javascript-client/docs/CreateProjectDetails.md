# TheJiraCloudPlatformRestApi.CreateProjectDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigneeType** | **String** | The default assignee when creating issues for this project. | [optional] 
**avatarId** | **Number** | An integer value for the project&#39;s avatar. | [optional] 
**categoryId** | **Number** | The ID of the project&#39;s category. A complete list of category IDs is found using the [Get all project categories](#api-rest-api-3-projectCategory-get) operation. | [optional] 
**description** | **String** | A brief description of the project. | [optional] 
**fieldConfigurationScheme** | **Number** | The ID of the field configuration scheme for the project. Use the [Get all field configuration schemes](#api-rest-api-3-fieldconfigurationscheme-get) operation to get a list of field configuration scheme IDs. If you specify the field configuration scheme you cannot specify the project template key. | [optional] 
**issueSecurityScheme** | **Number** | The ID of the issue security scheme for the project, which enables you to control who can and cannot view issues. Use the [Get issue security schemes](#api-rest-api-3-issuesecurityschemes-get) resource to get all issue security scheme IDs. | [optional] 
**issueTypeScheme** | **Number** | The ID of the issue type scheme for the project. Use the [Get all issue type schemes](#api-rest-api-3-issuetypescheme-get) operation to get a list of issue type scheme IDs. If you specify the issue type scheme you cannot specify the project template key. | [optional] 
**issueTypeScreenScheme** | **Number** | The ID of the issue type screen scheme for the project. Use the [Get all issue type screen schemes](#api-rest-api-3-issuetypescreenscheme-get) operation to get a list of issue type screen scheme IDs. If you specify the issue type screen scheme you cannot specify the project template key. | [optional] 
**key** | **String** | Project keys must be unique and start with an uppercase letter followed by one or more uppercase alphanumeric characters. The maximum length is 10 characters. | 
**lead** | **String** | This parameter is deprecated because of privacy changes. Use &#x60;leadAccountId&#x60; instead. See the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) for details. The user name of the project lead. Either &#x60;lead&#x60; or &#x60;leadAccountId&#x60; must be set when creating a project. Cannot be provided with &#x60;leadAccountId&#x60;. | [optional] 
**leadAccountId** | **String** | The account ID of the project lead. Either &#x60;lead&#x60; or &#x60;leadAccountId&#x60; must be set when creating a project. Cannot be provided with &#x60;lead&#x60;. | [optional] 
**name** | **String** | The name of the project. | 
**notificationScheme** | **Number** | The ID of the notification scheme for the project. Use the [Get notification schemes](#api-rest-api-3-notificationscheme-get) resource to get a list of notification scheme IDs. | [optional] 
**permissionScheme** | **Number** | The ID of the permission scheme for the project. Use the [Get all permission schemes](#api-rest-api-3-permissionscheme-get) resource to see a list of all permission scheme IDs. | [optional] 
**projectTemplateKey** | **String** | A predefined configuration for a project. The type of the &#x60;projectTemplateKey&#x60; must match with the type of the &#x60;projectTypeKey&#x60;. | [optional] 
**projectTypeKey** | **String** | The [project type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes), which defines the application-specific feature set. If you don&#39;t specify the project template you have to specify the project type. | [optional] 
**url** | **String** | A link to information about this project, such as project documentation | [optional] 
**workflowScheme** | **Number** | The ID of the workflow scheme for the project. Use the [Get all workflow schemes](#api-rest-api-3-workflowscheme-get) operation to get a list of workflow scheme IDs. If you specify the workflow scheme you cannot specify the project template key. | [optional] 



## Enum: AssigneeTypeEnum


* `PROJECT_LEAD` (value: `"PROJECT_LEAD"`)

* `UNASSIGNED` (value: `"UNASSIGNED"`)





## Enum: ProjectTemplateKeyEnum


* `pyxis.greenhopper.jira:gh-simplified-agility-kanban` (value: `"com.pyxis.greenhopper.jira:gh-simplified-agility-kanban"`)

* `pyxis.greenhopper.jira:gh-simplified-agility-scrum` (value: `"com.pyxis.greenhopper.jira:gh-simplified-agility-scrum"`)

* `pyxis.greenhopper.jira:gh-simplified-basic` (value: `"com.pyxis.greenhopper.jira:gh-simplified-basic"`)

* `pyxis.greenhopper.jira:gh-simplified-kanban-classic` (value: `"com.pyxis.greenhopper.jira:gh-simplified-kanban-classic"`)

* `pyxis.greenhopper.jira:gh-simplified-scrum-classic` (value: `"com.pyxis.greenhopper.jira:gh-simplified-scrum-classic"`)

* `atlassian.servicedesk:simplified-it-service-management` (value: `"com.atlassian.servicedesk:simplified-it-service-management"`)

* `atlassian.servicedesk:simplified-general-service-desk` (value: `"com.atlassian.servicedesk:simplified-general-service-desk"`)

* `atlassian.servicedesk:simplified-general-service-desk-it` (value: `"com.atlassian.servicedesk:simplified-general-service-desk-it"`)

* `atlassian.servicedesk:simplified-general-service-desk-business` (value: `"com.atlassian.servicedesk:simplified-general-service-desk-business"`)

* `atlassian.servicedesk:simplified-internal-service-desk` (value: `"com.atlassian.servicedesk:simplified-internal-service-desk"`)

* `atlassian.servicedesk:simplified-external-service-desk` (value: `"com.atlassian.servicedesk:simplified-external-service-desk"`)

* `atlassian.servicedesk:simplified-hr-service-desk` (value: `"com.atlassian.servicedesk:simplified-hr-service-desk"`)

* `atlassian.servicedesk:simplified-facilities-service-desk` (value: `"com.atlassian.servicedesk:simplified-facilities-service-desk"`)

* `atlassian.servicedesk:simplified-legal-service-desk` (value: `"com.atlassian.servicedesk:simplified-legal-service-desk"`)

* `atlassian.servicedesk:simplified-marketing-service-desk` (value: `"com.atlassian.servicedesk:simplified-marketing-service-desk"`)

* `atlassian.servicedesk:simplified-finance-service-desk` (value: `"com.atlassian.servicedesk:simplified-finance-service-desk"`)

* `atlassian.servicedesk:simplified-analytics-service-desk` (value: `"com.atlassian.servicedesk:simplified-analytics-service-desk"`)

* `atlassian.servicedesk:simplified-design-service-desk` (value: `"com.atlassian.servicedesk:simplified-design-service-desk"`)

* `atlassian.servicedesk:simplified-sales-service-desk` (value: `"com.atlassian.servicedesk:simplified-sales-service-desk"`)

* `atlassian.servicedesk:simplified-halp-service-desk` (value: `"com.atlassian.servicedesk:simplified-halp-service-desk"`)

* `atlassian.servicedesk:simplified-custom-project-service-desk` (value: `"com.atlassian.servicedesk:simplified-custom-project-service-desk"`)

* `atlassian.jira-core-project-templates:jira-core-simplified-content-management` (value: `"com.atlassian.jira-core-project-templates:jira-core-simplified-content-management"`)

* `atlassian.jira-core-project-templates:jira-core-simplified-document-approval` (value: `"com.atlassian.jira-core-project-templates:jira-core-simplified-document-approval"`)

* `atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking` (value: `"com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking"`)

* `atlassian.jira-core-project-templates:jira-core-simplified-process-control` (value: `"com.atlassian.jira-core-project-templates:jira-core-simplified-process-control"`)

* `atlassian.jira-core-project-templates:jira-core-simplified-procurement` (value: `"com.atlassian.jira-core-project-templates:jira-core-simplified-procurement"`)

* `atlassian.jira-core-project-templates:jira-core-simplified-project-management` (value: `"com.atlassian.jira-core-project-templates:jira-core-simplified-project-management"`)

* `atlassian.jira-core-project-templates:jira-core-simplified-recruitment` (value: `"com.atlassian.jira-core-project-templates:jira-core-simplified-recruitment"`)

* `atlassian.jira-core-project-templates:jira-core-simplified-task-` (value: `"com.atlassian.jira-core-project-templates:jira-core-simplified-task-"`)





## Enum: ProjectTypeKeyEnum


* `software` (value: `"software"`)

* `service_desk` (value: `"service_desk"`)

* `business` (value: `"business"`)




