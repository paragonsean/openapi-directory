# DefaultApi

All URIs are relative to *http://jira.local:8080/jira/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**acknowledgeErrors**](DefaultApi.md#acknowledgeErrors) | **POST** /api/2/cluster/zdu/retryUpgrade |  |
| [**addActorUsers**](DefaultApi.md#addActorUsers) | **POST** /api/2/project/{projectIdOrKey}/role/{id} |  |
| [**addAttachment**](DefaultApi.md#addAttachment) | **POST** /api/2/issue/{issueIdOrKey}/attachments |  |
| [**addComment**](DefaultApi.md#addComment) | **POST** /api/2/issue/{issueIdOrKey}/comment |  |
| [**addField**](DefaultApi.md#addField) | **POST** /api/2/screens/{screenId}/tabs/{tabId}/fields |  |
| [**addFieldToDefaultScreen**](DefaultApi.md#addFieldToDefaultScreen) | **POST** /api/2/screens/addToDefault/{fieldId} |  |
| [**addProjectRoleActorsToRole**](DefaultApi.md#addProjectRoleActorsToRole) | **POST** /api/2/role/{id}/actors |  |
| [**addRecord**](DefaultApi.md#addRecord) | **POST** /api/2/auditing/record |  |
| [**addSharePermission**](DefaultApi.md#addSharePermission) | **POST** /api/2/filter/{id}/permission |  |
| [**addTab**](DefaultApi.md#addTab) | **POST** /api/2/screens/{screenId}/tabs |  |
| [**addUserToApplication**](DefaultApi.md#addUserToApplication) | **POST** /api/2/user/application |  |
| [**addUserToGroup**](DefaultApi.md#addUserToGroup) | **POST** /api/2/group/user |  |
| [**addVote**](DefaultApi.md#addVote) | **POST** /api/2/issue/{issueIdOrKey}/votes |  |
| [**addWatcher**](DefaultApi.md#addWatcher) | **POST** /api/2/issue/{issueIdOrKey}/watchers |  |
| [**addWorklog**](DefaultApi.md#addWorklog) | **POST** /api/2/issue/{issueIdOrKey}/worklog |  |
| [**api2ApplicationPropertiesGet**](DefaultApi.md#api2ApplicationPropertiesGet) | **GET** /api/2/application-properties |  |
| [**api2AvatarTypeTemporaryCropPost**](DefaultApi.md#api2AvatarTypeTemporaryCropPost) | **POST** /api/2/avatar/{type}/temporaryCrop |  |
| [**api2CommentCommentIdPropertiesGet**](DefaultApi.md#api2CommentCommentIdPropertiesGet) | **GET** /api/2/comment/{commentId}/properties |  |
| [**api2CommentCommentIdPropertiesPropertyKeyDelete**](DefaultApi.md#api2CommentCommentIdPropertiesPropertyKeyDelete) | **DELETE** /api/2/comment/{commentId}/properties/{propertyKey} |  |
| [**api2CommentCommentIdPropertiesPropertyKeyGet**](DefaultApi.md#api2CommentCommentIdPropertiesPropertyKeyGet) | **GET** /api/2/comment/{commentId}/properties/{propertyKey} |  |
| [**api2CommentCommentIdPropertiesPropertyKeyPut**](DefaultApi.md#api2CommentCommentIdPropertiesPropertyKeyPut) | **PUT** /api/2/comment/{commentId}/properties/{propertyKey} |  |
| [**api2ComponentIdDelete**](DefaultApi.md#api2ComponentIdDelete) | **DELETE** /api/2/component/{id} |  |
| [**api2DashboardDashboardIdItemsItemIdPropertiesGet**](DefaultApi.md#api2DashboardDashboardIdItemsItemIdPropertiesGet) | **GET** /api/2/dashboard/{dashboardId}/items/{itemId}/properties |  |
| [**api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyDelete**](DefaultApi.md#api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyDelete) | **DELETE** /api/2/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey} |  |
| [**api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyGet**](DefaultApi.md#api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyGet) | **GET** /api/2/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey} |  |
| [**api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyPut**](DefaultApi.md#api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyPut) | **PUT** /api/2/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey} |  |
| [**api2FilterIdColumnsDelete**](DefaultApi.md#api2FilterIdColumnsDelete) | **DELETE** /api/2/filter/{id}/columns |  |
| [**api2FilterIdColumnsGet**](DefaultApi.md#api2FilterIdColumnsGet) | **GET** /api/2/filter/{id}/columns |  |
| [**api2FilterIdColumnsPut**](DefaultApi.md#api2FilterIdColumnsPut) | **PUT** /api/2/filter/{id}/columns |  |
| [**api2IssueIssueIdOrKeyPropertiesGet**](DefaultApi.md#api2IssueIssueIdOrKeyPropertiesGet) | **GET** /api/2/issue/{issueIdOrKey}/properties |  |
| [**api2IssueIssueIdOrKeyPropertiesPropertyKeyDelete**](DefaultApi.md#api2IssueIssueIdOrKeyPropertiesPropertyKeyDelete) | **DELETE** /api/2/issue/{issueIdOrKey}/properties/{propertyKey} |  |
| [**api2IssueIssueIdOrKeyPropertiesPropertyKeyGet**](DefaultApi.md#api2IssueIssueIdOrKeyPropertiesPropertyKeyGet) | **GET** /api/2/issue/{issueIdOrKey}/properties/{propertyKey} |  |
| [**api2IssueIssueIdOrKeyPropertiesPropertyKeyPut**](DefaultApi.md#api2IssueIssueIdOrKeyPropertiesPropertyKeyPut) | **PUT** /api/2/issue/{issueIdOrKey}/properties/{propertyKey} |  |
| [**api2IssuesecurityschemesIdGet**](DefaultApi.md#api2IssuesecurityschemesIdGet) | **GET** /api/2/issuesecurityschemes/{id} |  |
| [**api2IssuetypeIdAvatarPost**](DefaultApi.md#api2IssuetypeIdAvatarPost) | **POST** /api/2/issuetype/{id}/avatar |  |
| [**api2IssuetypeIdAvatarTemporaryPost**](DefaultApi.md#api2IssuetypeIdAvatarTemporaryPost) | **POST** /api/2/issuetype/{id}/avatar/temporary |  |
| [**api2IssuetypeIdDelete**](DefaultApi.md#api2IssuetypeIdDelete) | **DELETE** /api/2/issuetype/{id} |  |
| [**api2IssuetypeIdGet**](DefaultApi.md#api2IssuetypeIdGet) | **GET** /api/2/issuetype/{id} |  |
| [**api2IssuetypeIssueTypeIdPropertiesPropertyKeyDelete**](DefaultApi.md#api2IssuetypeIssueTypeIdPropertiesPropertyKeyDelete) | **DELETE** /api/2/issuetype/{issueTypeId}/properties/{propertyKey} |  |
| [**api2IssuetypeIssueTypeIdPropertiesPropertyKeyGet**](DefaultApi.md#api2IssuetypeIssueTypeIdPropertiesPropertyKeyGet) | **GET** /api/2/issuetype/{issueTypeId}/properties/{propertyKey} |  |
| [**api2IssuetypeIssueTypeIdPropertiesPropertyKeyPut**](DefaultApi.md#api2IssuetypeIssueTypeIdPropertiesPropertyKeyPut) | **PUT** /api/2/issuetype/{issueTypeId}/properties/{propertyKey} |  |
| [**api2MyselfGet**](DefaultApi.md#api2MyselfGet) | **GET** /api/2/myself |  |
| [**api2MyselfPut**](DefaultApi.md#api2MyselfPut) | **PUT** /api/2/myself |  |
| [**api2NotificationschemeIdGet**](DefaultApi.md#api2NotificationschemeIdGet) | **GET** /api/2/notificationscheme/{id} |  |
| [**api2ProjectProjectIdOrKeyAvatarIdDelete**](DefaultApi.md#api2ProjectProjectIdOrKeyAvatarIdDelete) | **DELETE** /api/2/project/{projectIdOrKey}/avatar/{id} |  |
| [**api2ProjectProjectIdOrKeyAvatarPost**](DefaultApi.md#api2ProjectProjectIdOrKeyAvatarPost) | **POST** /api/2/project/{projectIdOrKey}/avatar |  |
| [**api2ProjectProjectIdOrKeyAvatarPut**](DefaultApi.md#api2ProjectProjectIdOrKeyAvatarPut) | **PUT** /api/2/project/{projectIdOrKey}/avatar |  |
| [**api2ProjectProjectIdOrKeyAvatarTemporaryPost**](DefaultApi.md#api2ProjectProjectIdOrKeyAvatarTemporaryPost) | **POST** /api/2/project/{projectIdOrKey}/avatar/temporary |  |
| [**api2ProjectProjectIdOrKeyAvatarsGet**](DefaultApi.md#api2ProjectProjectIdOrKeyAvatarsGet) | **GET** /api/2/project/{projectIdOrKey}/avatars |  |
| [**api2ProjectProjectIdOrKeyGet**](DefaultApi.md#api2ProjectProjectIdOrKeyGet) | **GET** /api/2/project/{projectIdOrKey} |  |
| [**api2ProjectProjectIdOrKeyPropertiesGet**](DefaultApi.md#api2ProjectProjectIdOrKeyPropertiesGet) | **GET** /api/2/project/{projectIdOrKey}/properties |  |
| [**api2ProjectProjectIdOrKeyPropertiesPropertyKeyDelete**](DefaultApi.md#api2ProjectProjectIdOrKeyPropertiesPropertyKeyDelete) | **DELETE** /api/2/project/{projectIdOrKey}/properties/{propertyKey} |  |
| [**api2ProjectProjectIdOrKeyPropertiesPropertyKeyGet**](DefaultApi.md#api2ProjectProjectIdOrKeyPropertiesPropertyKeyGet) | **GET** /api/2/project/{projectIdOrKey}/properties/{propertyKey} |  |
| [**api2ProjectProjectIdOrKeyPropertiesPropertyKeyPut**](DefaultApi.md#api2ProjectProjectIdOrKeyPropertiesPropertyKeyPut) | **PUT** /api/2/project/{projectIdOrKey}/properties/{propertyKey} |  |
| [**api2ProjectProjectIdOrKeyRoleGet**](DefaultApi.md#api2ProjectProjectIdOrKeyRoleGet) | **GET** /api/2/project/{projectIdOrKey}/role |  |
| [**api2ProjectProjectKeyOrIdIssuesecuritylevelschemeGet**](DefaultApi.md#api2ProjectProjectKeyOrIdIssuesecuritylevelschemeGet) | **GET** /api/2/project/{projectKeyOrId}/issuesecuritylevelscheme |  |
| [**api2ProjectProjectKeyOrIdNotificationschemeGet**](DefaultApi.md#api2ProjectProjectKeyOrIdNotificationschemeGet) | **GET** /api/2/project/{projectKeyOrId}/notificationscheme |  |
| [**api2ProjectvalidateKeyGet**](DefaultApi.md#api2ProjectvalidateKeyGet) | **GET** /api/2/projectvalidate/key |  |
| [**api2RoleGet**](DefaultApi.md#api2RoleGet) | **GET** /api/2/role |  |
| [**api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarIdDelete**](DefaultApi.md#api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarIdDelete) | **DELETE** /api/2/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id} |  |
| [**api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarPost**](DefaultApi.md#api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarPost) | **POST** /api/2/universal_avatar/type/{type}/owner/{owningObjectId}/avatar |  |
| [**api2UniversalAvatarTypeTypeOwnerOwningObjectIdTempPost**](DefaultApi.md#api2UniversalAvatarTypeTypeOwnerOwningObjectIdTempPost) | **POST** /api/2/universal_avatar/type/{type}/owner/{owningObjectId}/temp |  |
| [**api2UserAvatarIdDelete**](DefaultApi.md#api2UserAvatarIdDelete) | **DELETE** /api/2/user/avatar/{id} |  |
| [**api2UserAvatarPost**](DefaultApi.md#api2UserAvatarPost) | **POST** /api/2/user/avatar |  |
| [**api2UserAvatarPut**](DefaultApi.md#api2UserAvatarPut) | **PUT** /api/2/user/avatar |  |
| [**api2UserAvatarTemporaryPost**](DefaultApi.md#api2UserAvatarTemporaryPost) | **POST** /api/2/user/avatar/temporary |  |
| [**api2UserAvatarsGet**](DefaultApi.md#api2UserAvatarsGet) | **GET** /api/2/user/avatars |  |
| [**api2UserColumnsDelete**](DefaultApi.md#api2UserColumnsDelete) | **DELETE** /api/2/user/columns |  |
| [**api2UserColumnsGet**](DefaultApi.md#api2UserColumnsGet) | **GET** /api/2/user/columns |  |
| [**api2UserColumnsPut**](DefaultApi.md#api2UserColumnsPut) | **PUT** /api/2/user/columns |  |
| [**api2UserGet**](DefaultApi.md#api2UserGet) | **GET** /api/2/user |  |
| [**api2UserPropertiesGet**](DefaultApi.md#api2UserPropertiesGet) | **GET** /api/2/user/properties/ |  |
| [**api2UserPropertiesPropertyKeyDelete**](DefaultApi.md#api2UserPropertiesPropertyKeyDelete) | **DELETE** /api/2/user/properties/{propertyKey} |  |
| [**api2UserPropertiesPropertyKeyGet**](DefaultApi.md#api2UserPropertiesPropertyKeyGet) | **GET** /api/2/user/properties/{propertyKey} |  |
| [**api2UserPropertiesPropertyKeyPut**](DefaultApi.md#api2UserPropertiesPropertyKeyPut) | **PUT** /api/2/user/properties/{propertyKey} |  |
| [**api2UserPut**](DefaultApi.md#api2UserPut) | **PUT** /api/2/user |  |
| [**api2VersionIdDelete**](DefaultApi.md#api2VersionIdDelete) | **DELETE** /api/2/version/{id} |  |
| [**api2VersionIdRemoveAndSwapPost**](DefaultApi.md#api2VersionIdRemoveAndSwapPost) | **POST** /api/2/version/{id}/removeAndSwap |  |
| [**api2VersionVersionIdRemotelinkGlobalIdPost**](DefaultApi.md#api2VersionVersionIdRemotelinkGlobalIdPost) | **POST** /api/2/version/{versionId}/remotelink/{globalId} |  |
| [**api2VersionVersionIdRemotelinkPost**](DefaultApi.md#api2VersionVersionIdRemotelinkPost) | **POST** /api/2/version/{versionId}/remotelink |  |
| [**api2WorkflowApi2TransitionsIdPropertiesDelete**](DefaultApi.md#api2WorkflowApi2TransitionsIdPropertiesDelete) | **DELETE** /api/2/workflow/api/2/transitions/{id}/properties |  |
| [**api2WorkflowschemeIdIssuetypeIssueTypeDelete**](DefaultApi.md#api2WorkflowschemeIdIssuetypeIssueTypeDelete) | **DELETE** /api/2/workflowscheme/{id}/issuetype/{issueType} |  |
| [**api2WorkflowschemeIdIssuetypeIssueTypeGet**](DefaultApi.md#api2WorkflowschemeIdIssuetypeIssueTypeGet) | **GET** /api/2/workflowscheme/{id}/issuetype/{issueType} |  |
| [**approveUpgrade**](DefaultApi.md#approveUpgrade) | **POST** /api/2/cluster/zdu/approve |  |
| [**areMetricsExposed**](DefaultApi.md#areMetricsExposed) | **GET** /api/2/monitoring/jmx/areMetricsExposed |  |
| [**assign**](DefaultApi.md#assign) | **PUT** /api/2/issue/{issueIdOrKey}/assignee |  |
| [**assignPermissionScheme**](DefaultApi.md#assignPermissionScheme) | **PUT** /api/2/project/{projectKeyOrId}/permissionscheme |  |
| [**callList**](DefaultApi.md#callList) | **GET** /api/2/dashboard |  |
| [**canMoveSubTask**](DefaultApi.md#canMoveSubTask) | **GET** /api/2/issue/{issueIdOrKey}/subtask/move |  |
| [**cancelUpgrade**](DefaultApi.md#cancelUpgrade) | **POST** /api/2/cluster/zdu/cancel |  |
| [**changeMyPassword**](DefaultApi.md#changeMyPassword) | **PUT** /api/2/myself/password |  |
| [**changeUserPassword**](DefaultApi.md#changeUserPassword) | **PUT** /api/2/user/password |  |
| [**createComponent**](DefaultApi.md#createComponent) | **POST** /api/2/component |  |
| [**createCustomField**](DefaultApi.md#createCustomField) | **POST** /api/2/field |  |
| [**createDraftForParent**](DefaultApi.md#createDraftForParent) | **POST** /api/2/workflowscheme/{id}/createdraft |  |
| [**createFilter**](DefaultApi.md#createFilter) | **POST** /api/2/filter |  |
| [**createGroup**](DefaultApi.md#createGroup) | **POST** /api/2/group |  |
| [**createIssue**](DefaultApi.md#createIssue) | **POST** /api/2/issue |  |
| [**createIssueLinkType**](DefaultApi.md#createIssueLinkType) | **POST** /api/2/issueLinkType |  |
| [**createIssueType**](DefaultApi.md#createIssueType) | **POST** /api/2/issuetype |  |
| [**createIssues**](DefaultApi.md#createIssues) | **POST** /api/2/issue/bulk |  |
| [**createOrUpdateRemoteIssueLink**](DefaultApi.md#createOrUpdateRemoteIssueLink) | **POST** /api/2/issue/{issueIdOrKey}/remotelink |  |
| [**createPermissionGrant**](DefaultApi.md#createPermissionGrant) | **POST** /api/2/permissionscheme/{schemeId}/permission |  |
| [**createPermissionScheme**](DefaultApi.md#createPermissionScheme) | **POST** /api/2/permissionscheme |  |
| [**createProject**](DefaultApi.md#createProject) | **POST** /api/2/project |  |
| [**createProjectCategory**](DefaultApi.md#createProjectCategory) | **POST** /api/2/projectCategory |  |
| [**createProjectRole**](DefaultApi.md#createProjectRole) | **POST** /api/2/role |  |
| [**createProperty**](DefaultApi.md#createProperty) | **POST** /api/2/workflow/api/2/transitions/{id}/properties |  |
| [**createScheme**](DefaultApi.md#createScheme) | **POST** /api/2/workflowscheme |  |
| [**createUser**](DefaultApi.md#createUser) | **POST** /api/2/user |  |
| [**createVersion**](DefaultApi.md#createVersion) | **POST** /api/2/version |  |
| [**currentUser**](DefaultApi.md#currentUser) | **GET** /auth/1/session |  |
| [**deleteActor**](DefaultApi.md#deleteActor) | **DELETE** /api/2/project/{projectIdOrKey}/role/{id} |  |
| [**deleteComment**](DefaultApi.md#deleteComment) | **DELETE** /api/2/issue/{issueIdOrKey}/comment/{id} |  |
| [**deleteDefault**](DefaultApi.md#deleteDefault) | **DELETE** /api/2/workflowscheme/{id}/default |  |
| [**deleteDraftById**](DefaultApi.md#deleteDraftById) | **DELETE** /api/2/workflowscheme/{id}/draft |  |
| [**deleteDraftDefault**](DefaultApi.md#deleteDraftDefault) | **DELETE** /api/2/workflowscheme/{id}/draft/default |  |
| [**deleteDraftIssueType**](DefaultApi.md#deleteDraftIssueType) | **DELETE** /api/2/workflowscheme/{id}/draft/issuetype/{issueType} |  |
| [**deleteDraftWorkflowMapping**](DefaultApi.md#deleteDraftWorkflowMapping) | **DELETE** /api/2/workflowscheme/{id}/draft/workflow |  |
| [**deleteFilter**](DefaultApi.md#deleteFilter) | **DELETE** /api/2/filter/{id} |  |
| [**deleteIssue**](DefaultApi.md#deleteIssue) | **DELETE** /api/2/issue/{issueIdOrKey} |  |
| [**deleteIssueLink**](DefaultApi.md#deleteIssueLink) | **DELETE** /api/2/issueLink/{linkId} |  |
| [**deleteIssueLinkType**](DefaultApi.md#deleteIssueLinkType) | **DELETE** /api/2/issueLinkType/{issueLinkTypeId} |  |
| [**deletePermissionScheme**](DefaultApi.md#deletePermissionScheme) | **DELETE** /api/2/permissionscheme/{schemeId} |  |
| [**deletePermissionSchemeEntity**](DefaultApi.md#deletePermissionSchemeEntity) | **DELETE** /api/2/permissionscheme/{schemeId}/permission/{permissionId} |  |
| [**deleteProject**](DefaultApi.md#deleteProject) | **DELETE** /api/2/project/{projectIdOrKey} |  |
| [**deleteProjectRole**](DefaultApi.md#deleteProjectRole) | **DELETE** /api/2/role/{id} |  |
| [**deleteProjectRoleActorsFromRole**](DefaultApi.md#deleteProjectRoleActorsFromRole) | **DELETE** /api/2/role/{id}/actors |  |
| [**deleteRemoteIssueLinkByGlobalId**](DefaultApi.md#deleteRemoteIssueLinkByGlobalId) | **DELETE** /api/2/issue/{issueIdOrKey}/remotelink |  |
| [**deleteRemoteIssueLinkById**](DefaultApi.md#deleteRemoteIssueLinkById) | **DELETE** /api/2/issue/{issueIdOrKey}/remotelink/{linkId} |  |
| [**deleteRemoteVersionLink**](DefaultApi.md#deleteRemoteVersionLink) | **DELETE** /api/2/version/{versionId}/remotelink/{globalId} |  |
| [**deleteRemoteVersionLinksByVersionId**](DefaultApi.md#deleteRemoteVersionLinksByVersionId) | **DELETE** /api/2/version/{versionId}/remotelink |  |
| [**deleteScheme**](DefaultApi.md#deleteScheme) | **DELETE** /api/2/workflowscheme/{id} |  |
| [**deleteSharePermission**](DefaultApi.md#deleteSharePermission) | **DELETE** /api/2/filter/{id}/permission/{permission-id} |  |
| [**deleteTab**](DefaultApi.md#deleteTab) | **DELETE** /api/2/screens/{screenId}/tabs/{tabId} |  |
| [**deleteWorkflowMapping**](DefaultApi.md#deleteWorkflowMapping) | **DELETE** /api/2/workflowscheme/{id}/workflow |  |
| [**deleteWorklog**](DefaultApi.md#deleteWorklog) | **DELETE** /api/2/issue/{issueIdOrKey}/worklog/{id} |  |
| [**doTransition**](DefaultApi.md#doTransition) | **POST** /api/2/issue/{issueIdOrKey}/transitions |  |
| [**editFilter**](DefaultApi.md#editFilter) | **PUT** /api/2/filter/{id} |  |
| [**editIssue**](DefaultApi.md#editIssue) | **PUT** /api/2/issue/{issueIdOrKey} |  |
| [**expandForHumans**](DefaultApi.md#expandForHumans) | **GET** /api/2/attachment/{id}/expand/human |  |
| [**expandForMachines**](DefaultApi.md#expandForMachines) | **GET** /api/2/attachment/{id}/expand/raw |  |
| [**findAssignableUsers**](DefaultApi.md#findAssignableUsers) | **GET** /api/2/user/assignable/search |  |
| [**findBulkAssignableUsers**](DefaultApi.md#findBulkAssignableUsers) | **GET** /api/2/user/assignable/multiProjectSearch |  |
| [**findGroups**](DefaultApi.md#findGroups) | **GET** /api/2/groups/picker |  |
| [**findUsers**](DefaultApi.md#findUsers) | **GET** /api/2/user/search |  |
| [**findUsersAndGroups**](DefaultApi.md#findUsersAndGroups) | **GET** /api/2/groupuserpicker |  |
| [**findUsersForPicker**](DefaultApi.md#findUsersForPicker) | **GET** /api/2/user/picker |  |
| [**findUsersWithAllPermissions**](DefaultApi.md#findUsersWithAllPermissions) | **GET** /api/2/user/permission/search |  |
| [**findUsersWithBrowsePermission**](DefaultApi.md#findUsersWithBrowsePermission) | **GET** /api/2/user/viewissue/search |  |
| [**fullyUpdateProjectRole**](DefaultApi.md#fullyUpdateProjectRole) | **PUT** /api/2/role/{id} |  |
| [**get**](DefaultApi.md#get) | **GET** /api/2/applicationrole/{key} |  |
| [**getAccessibleProjectTypeByKey**](DefaultApi.md#getAccessibleProjectTypeByKey) | **GET** /api/2/project/type/{projectTypeKey}/accessible |  |
| [**getAdvancedSettings**](DefaultApi.md#getAdvancedSettings) | **GET** /api/2/application-properties/advanced-settings |  |
| [**getAll**](DefaultApi.md#getAll) | **GET** /api/2/applicationrole |  |
| [**getAllFields**](DefaultApi.md#getAllFields) | **GET** /api/2/screens/{screenId}/tabs/{tabId}/fields |  |
| [**getAllPermissions**](DefaultApi.md#getAllPermissions) | **GET** /api/2/permissions |  |
| [**getAllProjectCategories**](DefaultApi.md#getAllProjectCategories) | **GET** /api/2/projectCategory |  |
| [**getAllProjectTypes**](DefaultApi.md#getAllProjectTypes) | **GET** /api/2/project/type |  |
| [**getAllProjects**](DefaultApi.md#getAllProjects) | **GET** /api/2/project |  |
| [**getAllStatuses**](DefaultApi.md#getAllStatuses) | **GET** /api/2/project/{projectIdOrKey}/statuses |  |
| [**getAllSystemAvatars**](DefaultApi.md#getAllSystemAvatars) | **GET** /api/2/avatar/{type}/system |  |
| [**getAllTabs**](DefaultApi.md#getAllTabs) | **GET** /api/2/screens/{screenId}/tabs |  |
| [**getAllWorkflows**](DefaultApi.md#getAllWorkflows) | **GET** /api/2/workflow |  |
| [**getAlternativeIssueTypes**](DefaultApi.md#getAlternativeIssueTypes) | **GET** /api/2/issuetype/{id}/alternatives |  |
| [**getAssignedPermissionScheme**](DefaultApi.md#getAssignedPermissionScheme) | **GET** /api/2/project/{projectKeyOrId}/permissionscheme |  |
| [**getAttachment**](DefaultApi.md#getAttachment) | **GET** /api/2/attachment/{id} |  |
| [**getAttachmentMeta**](DefaultApi.md#getAttachmentMeta) | **GET** /api/2/attachment/meta |  |
| [**getAutoComplete**](DefaultApi.md#getAutoComplete) | **GET** /api/2/jql/autocompletedata |  |
| [**getAvailableMetrics**](DefaultApi.md#getAvailableMetrics) | **GET** /api/2/monitoring/jmx/getAvailableMetrics |  |
| [**getAvatars**](DefaultApi.md#getAvatars) | **GET** /api/2/universal_avatar/type/{type}/owner/{owningObjectId} |  |
| [**getById**](DefaultApi.md#getById) | **GET** /api/2/workflowscheme/{id} |  |
| [**getComment**](DefaultApi.md#getComment) | **GET** /api/2/issue/{issueIdOrKey}/comment/{id} |  |
| [**getComments**](DefaultApi.md#getComments) | **GET** /api/2/issue/{issueIdOrKey}/comment |  |
| [**getComponent**](DefaultApi.md#getComponent) | **GET** /api/2/component/{id} |  |
| [**getComponentRelatedIssues**](DefaultApi.md#getComponentRelatedIssues) | **GET** /api/2/component/{id}/relatedIssueCounts |  |
| [**getConfiguration**](DefaultApi.md#getConfiguration) | **GET** /api/2/configuration |  |
| [**getCreateIssueMeta**](DefaultApi.md#getCreateIssueMeta) | **GET** /api/2/issue/createmeta |  |
| [**getCustomFieldOption**](DefaultApi.md#getCustomFieldOption) | **GET** /api/2/customFieldOption/{id} |  |
| [**getDashboard**](DefaultApi.md#getDashboard) | **GET** /api/2/dashboard/{id} |  |
| [**getDefault**](DefaultApi.md#getDefault) | **GET** /api/2/workflowscheme/{id}/default |  |
| [**getDefaultShareScope**](DefaultApi.md#getDefaultShareScope) | **GET** /api/2/filter/defaultShareScope |  |
| [**getDraftById**](DefaultApi.md#getDraftById) | **GET** /api/2/workflowscheme/{id}/draft |  |
| [**getDraftDefault**](DefaultApi.md#getDraftDefault) | **GET** /api/2/workflowscheme/{id}/draft/default |  |
| [**getDraftIssueType**](DefaultApi.md#getDraftIssueType) | **GET** /api/2/workflowscheme/{id}/draft/issuetype/{issueType} |  |
| [**getDraftWorkflow**](DefaultApi.md#getDraftWorkflow) | **GET** /api/2/workflowscheme/{id}/draft/workflow |  |
| [**getEditIssueMeta**](DefaultApi.md#getEditIssueMeta) | **GET** /api/2/issue/{issueIdOrKey}/editmeta |  |
| [**getFavouriteFilters**](DefaultApi.md#getFavouriteFilters) | **GET** /api/2/filter/favourite |  |
| [**getFieldAutoCompleteForQueryString**](DefaultApi.md#getFieldAutoCompleteForQueryString) | **GET** /api/2/jql/autocompletedata/suggestions |  |
| [**getFields**](DefaultApi.md#getFields) | **GET** /api/2/field |  |
| [**getFieldsToAdd**](DefaultApi.md#getFieldsToAdd) | **GET** /api/2/screens/{screenId}/availableFields |  |
| [**getFilter**](DefaultApi.md#getFilter) | **GET** /api/2/filter/{id} |  |
| [**getGroup**](DefaultApi.md#getGroup) | **GET** /api/2/group |  |
| [**getIdsOfWorklogsDeletedSince**](DefaultApi.md#getIdsOfWorklogsDeletedSince) | **GET** /api/2/worklog/deleted |  |
| [**getIdsOfWorklogsModifiedSince**](DefaultApi.md#getIdsOfWorklogsModifiedSince) | **GET** /api/2/worklog/updated |  |
| [**getIndexSummary**](DefaultApi.md#getIndexSummary) | **GET** /api/2/index/summary |  |
| [**getIssue**](DefaultApi.md#getIssue) | **GET** /api/2/issue/{issueIdOrKey} |  |
| [**getIssueAllTypes**](DefaultApi.md#getIssueAllTypes) | **GET** /api/2/issuetype |  |
| [**getIssueLink**](DefaultApi.md#getIssueLink) | **GET** /api/2/issueLink/{linkId} |  |
| [**getIssueLinkType**](DefaultApi.md#getIssueLinkType) | **GET** /api/2/issueLinkType/{issueLinkTypeId} |  |
| [**getIssueLinkTypes**](DefaultApi.md#getIssueLinkTypes) | **GET** /api/2/issueLinkType |  |
| [**getIssueNavigatorDefaultColumns**](DefaultApi.md#getIssueNavigatorDefaultColumns) | **GET** /api/2/settings/columns |  |
| [**getIssuePickerResource**](DefaultApi.md#getIssuePickerResource) | **GET** /api/2/issue/picker |  |
| [**getIssueSecuritySchemes**](DefaultApi.md#getIssueSecuritySchemes) | **GET** /api/2/issuesecurityschemes |  |
| [**getIssueWatchers**](DefaultApi.md#getIssueWatchers) | **GET** /api/2/issue/{issueIdOrKey}/watchers |  |
| [**getIssueWorklog**](DefaultApi.md#getIssueWorklog) | **GET** /api/2/issue/{issueIdOrKey}/worklog |  |
| [**getIssuesecuritylevel**](DefaultApi.md#getIssuesecuritylevel) | **GET** /api/2/securitylevel/{id} |  |
| [**getNotificationSchemes**](DefaultApi.md#getNotificationSchemes) | **GET** /api/2/notificationscheme |  |
| [**getPasswordPolicy**](DefaultApi.md#getPasswordPolicy) | **GET** /api/2/password/policy |  |
| [**getPermissionScheme**](DefaultApi.md#getPermissionScheme) | **GET** /api/2/permissionscheme/{schemeId} |  |
| [**getPermissionSchemeGrant**](DefaultApi.md#getPermissionSchemeGrant) | **GET** /api/2/permissionscheme/{schemeId}/permission/{permissionId} |  |
| [**getPermissionSchemeGrants**](DefaultApi.md#getPermissionSchemeGrants) | **GET** /api/2/permissionscheme/{schemeId}/permission |  |
| [**getPermissionSchemes**](DefaultApi.md#getPermissionSchemes) | **GET** /api/2/permissionscheme |  |
| [**getPermissions**](DefaultApi.md#getPermissions) | **GET** /api/2/mypermissions |  |
| [**getPreference**](DefaultApi.md#getPreference) | **GET** /api/2/mypreferences |  |
| [**getPriorities**](DefaultApi.md#getPriorities) | **GET** /api/2/priority |  |
| [**getPriority**](DefaultApi.md#getPriority) | **GET** /api/2/priority/{id} |  |
| [**getProgress**](DefaultApi.md#getProgress) | **GET** /api/2/reindex/request/{requestId} |  |
| [**getProgressBulk**](DefaultApi.md#getProgressBulk) | **GET** /api/2/reindex/request/bulk |  |
| [**getProjectCategoryById**](DefaultApi.md#getProjectCategoryById) | **GET** /api/2/projectCategory/{id} |  |
| [**getProjectComponents**](DefaultApi.md#getProjectComponents) | **GET** /api/2/project/{projectIdOrKey}/components |  |
| [**getProjectRole**](DefaultApi.md#getProjectRole) | **GET** /api/2/project/{projectIdOrKey}/role/{id} |  |
| [**getProjectRoleActorsForRole**](DefaultApi.md#getProjectRoleActorsForRole) | **GET** /api/2/role/{id}/actors |  |
| [**getProjectRolesById**](DefaultApi.md#getProjectRolesById) | **GET** /api/2/role/{id} |  |
| [**getProjectTypeByKey**](DefaultApi.md#getProjectTypeByKey) | **GET** /api/2/project/type/{projectTypeKey} |  |
| [**getProjectVersions**](DefaultApi.md#getProjectVersions) | **GET** /api/2/project/{projectIdOrKey}/versions |  |
| [**getProjectVersionsPaginated**](DefaultApi.md#getProjectVersionsPaginated) | **GET** /api/2/project/{projectIdOrKey}/version |  |
| [**getProperties**](DefaultApi.md#getProperties) | **GET** /api/2/workflow/api/2/transitions/{id}/properties |  |
| [**getPropertyKeys**](DefaultApi.md#getPropertyKeys) | **GET** /api/2/issuetype/{issueTypeId}/properties |  |
| [**getRecords**](DefaultApi.md#getRecords) | **GET** /api/2/auditing/record |  |
| [**getReindexInfo**](DefaultApi.md#getReindexInfo) | **GET** /api/2/reindex |  |
| [**getReindexProgress**](DefaultApi.md#getReindexProgress) | **GET** /api/2/reindex/progress |  |
| [**getRemoteIssueLinkById**](DefaultApi.md#getRemoteIssueLinkById) | **GET** /api/2/issue/{issueIdOrKey}/remotelink/{linkId} |  |
| [**getRemoteIssueLinks**](DefaultApi.md#getRemoteIssueLinks) | **GET** /api/2/issue/{issueIdOrKey}/remotelink |  |
| [**getRemoteVersionLink**](DefaultApi.md#getRemoteVersionLink) | **GET** /api/2/version/{versionId}/remotelink/{globalId} |  |
| [**getRemoteVersionLinks**](DefaultApi.md#getRemoteVersionLinks) | **GET** /api/2/version/remotelink |  |
| [**getRemoteVersionLinksByVersionId**](DefaultApi.md#getRemoteVersionLinksByVersionId) | **GET** /api/2/version/{versionId}/remotelink |  |
| [**getResolution**](DefaultApi.md#getResolution) | **GET** /api/2/resolution/{id} |  |
| [**getResolutions**](DefaultApi.md#getResolutions) | **GET** /api/2/resolution |  |
| [**getSchemeAttribute**](DefaultApi.md#getSchemeAttribute) | **GET** /api/2/permissionscheme/{permissionSchemeId}/attribute/{attributeKey} |  |
| [**getSecurityLevelsForProject**](DefaultApi.md#getSecurityLevelsForProject) | **GET** /api/2/project/{projectKeyOrId}/securitylevel |  |
| [**getServerInfo**](DefaultApi.md#getServerInfo) | **GET** /api/2/serverInfo |  |
| [**getSharePermission**](DefaultApi.md#getSharePermission) | **GET** /api/2/filter/{id}/permission/{permissionId} |  |
| [**getSharePermissions**](DefaultApi.md#getSharePermissions) | **GET** /api/2/filter/{id}/permission |  |
| [**getState**](DefaultApi.md#getState) | **GET** /api/2/cluster/zdu/state |  |
| [**getStatus**](DefaultApi.md#getStatus) | **GET** /api/2/status/{idOrName} |  |
| [**getStatusCategories**](DefaultApi.md#getStatusCategories) | **GET** /api/2/statuscategory |  |
| [**getStatusCategory**](DefaultApi.md#getStatusCategory) | **GET** /api/2/statuscategory/{idOrKey} |  |
| [**getStatuses**](DefaultApi.md#getStatuses) | **GET** /api/2/status |  |
| [**getSubTasks**](DefaultApi.md#getSubTasks) | **GET** /api/2/issue/{issueIdOrKey}/subtask |  |
| [**getTransitions**](DefaultApi.md#getTransitions) | **GET** /api/2/issue/{issueIdOrKey}/transitions |  |
| [**getUpgradeResult**](DefaultApi.md#getUpgradeResult) | **GET** /api/2/upgrade |  |
| [**getUsersFromGroup**](DefaultApi.md#getUsersFromGroup) | **GET** /api/2/group/member |  |
| [**getVersion**](DefaultApi.md#getVersion) | **GET** /api/2/version/{id} |  |
| [**getVersionRelatedIssues**](DefaultApi.md#getVersionRelatedIssues) | **GET** /api/2/version/{id}/relatedIssueCounts |  |
| [**getVersionUnresolvedIssues**](DefaultApi.md#getVersionUnresolvedIssues) | **GET** /api/2/version/{id}/unresolvedIssueCount |  |
| [**getVotes**](DefaultApi.md#getVotes) | **GET** /api/2/issue/{issueIdOrKey}/votes |  |
| [**getWorkflow**](DefaultApi.md#getWorkflow) | **GET** /api/2/workflowscheme/{id}/workflow |  |
| [**getWorklog**](DefaultApi.md#getWorklog) | **GET** /api/2/issue/{issueIdOrKey}/worklog/{id} |  |
| [**getWorklogsForIds**](DefaultApi.md#getWorklogsForIds) | **POST** /api/2/worklog/list |  |
| [**linkIssues**](DefaultApi.md#linkIssues) | **POST** /api/2/issueLink |  |
| [**login**](DefaultApi.md#login) | **POST** /auth/1/session |  |
| [**logout**](DefaultApi.md#logout) | **DELETE** /auth/1/session |  |
| [**merge**](DefaultApi.md#merge) | **PUT** /api/2/version/{id}/mergeto/{moveIssuesTo} |  |
| [**moveField**](DefaultApi.md#moveField) | **POST** /api/2/screens/{screenId}/tabs/{tabId}/fields/{id}/move |  |
| [**moveSubTasks**](DefaultApi.md#moveSubTasks) | **POST** /api/2/issue/{issueIdOrKey}/subtask/move |  |
| [**moveTab**](DefaultApi.md#moveTab) | **POST** /api/2/screens/{screenId}/tabs/{tabId}/move/{pos} |  |
| [**moveVersion**](DefaultApi.md#moveVersion) | **POST** /api/2/version/{id}/move |  |
| [**notify**](DefaultApi.md#notify) | **POST** /api/2/issue/{issueIdOrKey}/notify |  |
| [**partialUpdateProjectRole**](DefaultApi.md#partialUpdateProjectRole) | **POST** /api/2/role/{id} |  |
| [**policyCheckCreateUser**](DefaultApi.md#policyCheckCreateUser) | **POST** /api/2/password/policy/createUser |  |
| [**policyCheckUpdateUser**](DefaultApi.md#policyCheckUpdateUser) | **POST** /api/2/password/policy/updateUser |  |
| [**processRequests**](DefaultApi.md#processRequests) | **POST** /api/2/reindex/request |  |
| [**put**](DefaultApi.md#put) | **PUT** /api/2/applicationrole/{key} |  |
| [**putBulk**](DefaultApi.md#putBulk) | **PUT** /api/2/applicationrole |  |
| [**reindex**](DefaultApi.md#reindex) | **POST** /api/2/reindex |  |
| [**reindexIssues**](DefaultApi.md#reindexIssues) | **POST** /api/2/reindex/issue |  |
| [**release**](DefaultApi.md#release) | **DELETE** /auth/1/websudo |  |
| [**removeAttachment**](DefaultApi.md#removeAttachment) | **DELETE** /api/2/attachment/{id} |  |
| [**removeField**](DefaultApi.md#removeField) | **DELETE** /api/2/screens/{screenId}/tabs/{tabId}/fields/{id} |  |
| [**removeGroup**](DefaultApi.md#removeGroup) | **DELETE** /api/2/group |  |
| [**removePreference**](DefaultApi.md#removePreference) | **DELETE** /api/2/mypreferences |  |
| [**removeProjectCategory**](DefaultApi.md#removeProjectCategory) | **DELETE** /api/2/projectCategory/{id} |  |
| [**removeUser**](DefaultApi.md#removeUser) | **DELETE** /api/2/user |  |
| [**removeUserFromApplication**](DefaultApi.md#removeUserFromApplication) | **DELETE** /api/2/user/application |  |
| [**removeUserFromGroup**](DefaultApi.md#removeUserFromGroup) | **DELETE** /api/2/group/user |  |
| [**removeVote**](DefaultApi.md#removeVote) | **DELETE** /api/2/issue/{issueIdOrKey}/votes |  |
| [**removeWatcher**](DefaultApi.md#removeWatcher) | **DELETE** /api/2/issue/{issueIdOrKey}/watchers |  |
| [**renameTab**](DefaultApi.md#renameTab) | **PUT** /api/2/screens/{screenId}/tabs/{tabId} |  |
| [**runUpgradesNow**](DefaultApi.md#runUpgradesNow) | **POST** /api/2/upgrade |  |
| [**search**](DefaultApi.md#search) | **GET** /api/2/search |  |
| [**searchUsingSearchRequest**](DefaultApi.md#searchUsingSearchRequest) | **POST** /api/2/search |  |
| [**setActors**](DefaultApi.md#setActors) | **PUT** /api/2/project/{projectIdOrKey}/role/{id} |  |
| [**setBaseURL**](DefaultApi.md#setBaseURL) | **PUT** /api/2/settings/baseUrl |  |
| [**setDefaultShareScope**](DefaultApi.md#setDefaultShareScope) | **PUT** /api/2/filter/defaultShareScope |  |
| [**setDraftIssueType**](DefaultApi.md#setDraftIssueType) | **PUT** /api/2/workflowscheme/{id}/draft/issuetype/{issueType} |  |
| [**setIssueNavigatorDefaultColumns**](DefaultApi.md#setIssueNavigatorDefaultColumns) | **PUT** /api/2/settings/columns |  |
| [**setIssueType**](DefaultApi.md#setIssueType) | **PUT** /api/2/workflowscheme/{id}/issuetype/{issueType} |  |
| [**setPreference**](DefaultApi.md#setPreference) | **PUT** /api/2/mypreferences |  |
| [**setPropertyViaRestfulTable**](DefaultApi.md#setPropertyViaRestfulTable) | **PUT** /api/2/application-properties/{id} |  |
| [**setReadyToUpgrade**](DefaultApi.md#setReadyToUpgrade) | **POST** /api/2/cluster/zdu/start |  |
| [**setSchemeAttribute**](DefaultApi.md#setSchemeAttribute) | **PUT** /api/2/permissionscheme/{permissionSchemeId}/attribute/{key} |  |
| [**start**](DefaultApi.md#start) | **GET** /api/2/monitoring/jmx/startExposing |  |
| [**stop**](DefaultApi.md#stop) | **GET** /api/2/monitoring/jmx/stopExposing |  |
| [**storeTemporaryAvatar**](DefaultApi.md#storeTemporaryAvatar) | **POST** /api/2/avatar/{type}/temporary |  |
| [**update**](DefaultApi.md#update) | **PUT** /api/2/workflowscheme/{id} |  |
| [**updateComment**](DefaultApi.md#updateComment) | **PUT** /api/2/issue/{issueIdOrKey}/comment/{id} |  |
| [**updateComponent**](DefaultApi.md#updateComponent) | **PUT** /api/2/component/{id} |  |
| [**updateDefault**](DefaultApi.md#updateDefault) | **PUT** /api/2/workflowscheme/{id}/default |  |
| [**updateDraft**](DefaultApi.md#updateDraft) | **PUT** /api/2/workflowscheme/{id}/draft |  |
| [**updateDraftDefault**](DefaultApi.md#updateDraftDefault) | **PUT** /api/2/workflowscheme/{id}/draft/default |  |
| [**updateDraftWorkflowMapping**](DefaultApi.md#updateDraftWorkflowMapping) | **PUT** /api/2/workflowscheme/{id}/draft/workflow |  |
| [**updateIssueLinkType**](DefaultApi.md#updateIssueLinkType) | **PUT** /api/2/issueLinkType/{issueLinkTypeId} |  |
| [**updateIssueType**](DefaultApi.md#updateIssueType) | **PUT** /api/2/issuetype/{id} |  |
| [**updatePermissionScheme**](DefaultApi.md#updatePermissionScheme) | **PUT** /api/2/permissionscheme/{schemeId} |  |
| [**updateProject**](DefaultApi.md#updateProject) | **PUT** /api/2/project/{projectIdOrKey} |  |
| [**updateProjectCategory**](DefaultApi.md#updateProjectCategory) | **PUT** /api/2/projectCategory/{id} |  |
| [**updateProjectType**](DefaultApi.md#updateProjectType) | **PUT** /api/2/project/{projectIdOrKey}/type/{newProjectTypeKey} |  |
| [**updateProperty**](DefaultApi.md#updateProperty) | **PUT** /api/2/workflow/api/2/transitions/{id}/properties |  |
| [**updateRemoteIssueLink**](DefaultApi.md#updateRemoteIssueLink) | **PUT** /api/2/issue/{issueIdOrKey}/remotelink/{linkId} |  |
| [**updateVersion**](DefaultApi.md#updateVersion) | **PUT** /api/2/version/{id} |  |
| [**updateWorkflowMapping**](DefaultApi.md#updateWorkflowMapping) | **PUT** /api/2/workflowscheme/{id}/workflow |  |
| [**updateWorklog**](DefaultApi.md#updateWorklog) | **PUT** /api/2/issue/{issueIdOrKey}/worklog/{id} |  |
| [**validate**](DefaultApi.md#validate) | **POST** /api/2/licenseValidator |  |


<a id="acknowledgeErrors"></a>
# **acknowledgeErrors**
> acknowledgeErrors()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.acknowledgeErrors();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#acknowledgeErrors");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="addActorUsers"></a>
# **addActorUsers**
> addActorUsers(projectIdOrKey, id)



Adds an actor (user or group) to a project role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
    Long id = 56L; // Long | the project role id
    try {
      apiInstance.addActorUsers(projectIdOrKey, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addActorUsers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| the project id or project key | |
| **id** | **Long**| the project role id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="addAttachment"></a>
# **addAttachment**
> addAttachment(issueIdOrKey)



Add one or more attachments to an issue.  &lt;p&gt;  This resource expects a multipart post. The media-type multipart/form-data is defined in RFC 1867. Most client  libraries have classes that make dealing with multipart posts simple. For instance, in Java the Apache HTTP Components  library provides a  &lt;a href&#x3D;\&quot;http://hc.apache.org/httpcomponents-client-ga/httpmime/apidocs/org/apache/http/entity/mime/MultipartEntity.html\&quot;&gt;MultiPartEntity&lt;/a&gt;  that makes it simple to submit a multipart POST.  &lt;p&gt;  In order to protect against XSRF attacks, because this method accepts multipart/form-data, it has XSRF protection  on it.  This means you must submit a header of X-Atlassian-Token: no-check with the request, otherwise it will be  blocked.  &lt;p&gt;  The name of the multipart/form-data parameter that contains attachments must be \&quot;file\&quot;  &lt;p&gt;  A simple example to upload a file called \&quot;myfile.txt\&quot; to issue REST-123:  &lt;pre&gt;curl -D- -u admin:admin -X POST -H \&quot;X-Atlassian-Token: no-check\&quot; -F \&quot;file&#x3D;@myfile.txt\&quot; http://myhost/rest/api/2/issue/TEST-123/attachments&lt;/pre&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue that you want to add the attachments to
    try {
      apiInstance.addAttachment(issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addAttachment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| the issue that you want to add the attachments to | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="addComment"></a>
# **addComment**
> addComment(issueIdOrKey, expand)



Adds a new comment to an issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | a string containing the issue id or key the comment will be added to
    String expand = "expand_example"; // String | optional flags: renderedBody (provides body rendered in HTML)
    try {
      apiInstance.addComment(issueIdOrKey, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addComment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| a string containing the issue id or key the comment will be added to | |
| **expand** | **String**| optional flags: renderedBody (provides body rendered in HTML) | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="addField"></a>
# **addField**
> addField(screenId, tabId)



Adds field to the given tab.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long screenId = 56L; // Long | id of screen
    Long tabId = 56L; // Long | id of tab
    try {
      apiInstance.addField(screenId, tabId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addField");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **screenId** | **Long**| id of screen | |
| **tabId** | **Long**| id of tab | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="addFieldToDefaultScreen"></a>
# **addFieldToDefaultScreen**
> addFieldToDefaultScreen(fieldId)



Adds field or custom field to the default tab

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String fieldId = "fieldId_example"; // String | id of field / custom field
    try {
      apiInstance.addFieldToDefaultScreen(fieldId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addFieldToDefaultScreen");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fieldId** | **String**| id of field / custom field | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="addProjectRoleActorsToRole"></a>
# **addProjectRoleActorsToRole**
> addProjectRoleActorsToRole(id)



Adds default actors to the given role. The request data should contain a list of usernames or a list of groups to add.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the role id to remove the actors from
    try {
      apiInstance.addProjectRoleActorsToRole(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addProjectRoleActorsToRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the role id to remove the actors from | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="addRecord"></a>
# **addRecord**
> addRecord()



Store a record in Audit Log

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.addRecord();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addRecord");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="addSharePermission"></a>
# **addSharePermission**
> addSharePermission(id)



Adds a share permissions to the given filter. Adding a global permission removes all previous permissions from the filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      apiInstance.addSharePermission(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addSharePermission");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="addTab"></a>
# **addTab**
> addTab(screenId)



Creates tab for given screen

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long screenId = 56L; // Long | id of screen
    try {
      apiInstance.addTab(screenId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addTab");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **screenId** | **Long**| id of screen | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="addUserToApplication"></a>
# **addUserToApplication**
> addUserToApplication(username, applicationKey)



Add user to given application. Admin permission will be required to perform this operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | username
    String applicationKey = "applicationKey_example"; // String | application key
    try {
      apiInstance.addUserToApplication(username, applicationKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addUserToApplication");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| username | [optional] |
| **applicationKey** | **String**| application key | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="addUserToGroup"></a>
# **addUserToGroup**
> addUserToGroup(groupname)



Adds given user to a group.  &lt;p&gt;  Returns the current state of the group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String groupname = "groupname_example"; // String | A name of requested group.
    try {
      apiInstance.addUserToGroup(groupname);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addUserToGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **groupname** | **String**| A name of requested group. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="addVote"></a>
# **addVote**
> addVote(issueIdOrKey)



Cast your vote in favour of an issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue to view voting information for
    try {
      apiInstance.addVote(issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addVote");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| the issue to view voting information for | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="addWatcher"></a>
# **addWatcher**
> addWatcher(issueIdOrKey)



Adds a user to an issue&#39;s watcher list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | a String containing an issue key.
    try {
      apiInstance.addWatcher(issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addWatcher");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| a String containing an issue key. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="addWorklog"></a>
# **addWorklog**
> addWorklog(issueIdOrKey, adjustEstimate, newEstimate, reduceBy)



Adds a new worklog entry to an issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | a string containing the issue id or key the worklog will be added to
    String adjustEstimate = "adjustEstimate_example"; // String | (optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are                        <ul>                        <li>\"new\" - sets the estimate to a specific value</li>                        <li>\"leave\"- leaves the estimate as is</li>                        <li>\"manual\" - specify a specific amount to increase remaining estimate by</li>                        <li>\"auto\"- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog</li> </ul>
    String newEstimate = "newEstimate_example"; // String | (required when \"new\" is selected for adjustEstimate) the new value for the remaining estimate field. e.g. \"2d\"
    String reduceBy = "reduceBy_example"; // String | (required when \"manual\" is selected for adjustEstimate) the amount to reduce the remaining estimate by e.g. \"2d\"
    try {
      apiInstance.addWorklog(issueIdOrKey, adjustEstimate, newEstimate, reduceBy);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addWorklog");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| a string containing the issue id or key the worklog will be added to | |
| **adjustEstimate** | **String**| (optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are                        &lt;ul&gt;                        &lt;li&gt;\&quot;new\&quot; - sets the estimate to a specific value&lt;/li&gt;                        &lt;li&gt;\&quot;leave\&quot;- leaves the estimate as is&lt;/li&gt;                        &lt;li&gt;\&quot;manual\&quot; - specify a specific amount to increase remaining estimate by&lt;/li&gt;                        &lt;li&gt;\&quot;auto\&quot;- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog&lt;/li&gt; &lt;/ul&gt; | [optional] |
| **newEstimate** | **String**| (required when \&quot;new\&quot; is selected for adjustEstimate) the new value for the remaining estimate field. e.g. \&quot;2d\&quot; | [optional] |
| **reduceBy** | **String**| (required when \&quot;manual\&quot; is selected for adjustEstimate) the amount to reduce the remaining estimate by e.g. \&quot;2d\&quot; | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2ApplicationPropertiesGet"></a>
# **api2ApplicationPropertiesGet**
> api2ApplicationPropertiesGet(key, permissionLevel, keyFilter)



Returns an application property.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | a String containing the property key
    String permissionLevel = "permissionLevel_example"; // String | when fetching a list specifies the permission level of all items in the list                         see {@link com.atlassian.jira.bc.admin.ApplicationPropertiesService.EditPermissionLevel}
    String keyFilter = "keyFilter_example"; // String | when fetching a list allows the list to be filtered by the property's start of key                         e.g. \"jira.lf.*\" whould fetch only those permissions that are editable and whose keys start with                         \"jira.lf.\". This is a regex.
    try {
      apiInstance.api2ApplicationPropertiesGet(key, permissionLevel, keyFilter);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2ApplicationPropertiesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **key** | **String**| a String containing the property key | [optional] |
| **permissionLevel** | **String**| when fetching a list specifies the permission level of all items in the list                         see {@link com.atlassian.jira.bc.admin.ApplicationPropertiesService.EditPermissionLevel} | [optional] |
| **keyFilter** | **String**| when fetching a list allows the list to be filtered by the property&#39;s start of key                         e.g. \&quot;jira.lf.*\&quot; whould fetch only those permissions that are editable and whose keys start with                         \&quot;jira.lf.\&quot;. This is a regex. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2AvatarTypeTemporaryCropPost"></a>
# **api2AvatarTypeTemporaryCropPost**
> api2AvatarTypeTemporaryCropPost(type)



Updates the cropping instructions of the temporary avatar.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String type = "type_example"; // String | the avatar type
    try {
      apiInstance.api2AvatarTypeTemporaryCropPost(type);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2AvatarTypeTemporaryCropPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **String**| the avatar type | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2CommentCommentIdPropertiesGet"></a>
# **api2CommentCommentIdPropertiesGet**
> api2CommentCommentIdPropertiesGet(commentId)



Returns the keys of all properties for the comment identified by the key or by the id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String commentId = "commentId_example"; // String | the comment from which keys will be returned.
    try {
      apiInstance.api2CommentCommentIdPropertiesGet(commentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2CommentCommentIdPropertiesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **commentId** | **String**| the comment from which keys will be returned. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2CommentCommentIdPropertiesPropertyKeyDelete"></a>
# **api2CommentCommentIdPropertiesPropertyKeyDelete**
> api2CommentCommentIdPropertiesPropertyKeyDelete(commentId, propertyKey)



Removes the property from the comment identified by the key or by the id. Ths user removing the property is required  to have permissions to administer the comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String commentId = "commentId_example"; // String | the comment from which keys will be returned.
    String propertyKey = "propertyKey_example"; // String | the key of the property to return.
    try {
      apiInstance.api2CommentCommentIdPropertiesPropertyKeyDelete(commentId, propertyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2CommentCommentIdPropertiesPropertyKeyDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **commentId** | **String**| the comment from which keys will be returned. | |
| **propertyKey** | **String**| the key of the property to return. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2CommentCommentIdPropertiesPropertyKeyGet"></a>
# **api2CommentCommentIdPropertiesPropertyKeyGet**
> api2CommentCommentIdPropertiesPropertyKeyGet(commentId, propertyKey)



Returns the value of the property with a given key from the comment identified by the key or by the id. The user who retrieves  the property is required to have permissions to read the comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String commentId = "commentId_example"; // String | the comment from which keys will be returned.
    String propertyKey = "propertyKey_example"; // String | the key of the property to return.
    try {
      apiInstance.api2CommentCommentIdPropertiesPropertyKeyGet(commentId, propertyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2CommentCommentIdPropertiesPropertyKeyGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **commentId** | **String**| the comment from which keys will be returned. | |
| **propertyKey** | **String**| the key of the property to return. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2CommentCommentIdPropertiesPropertyKeyPut"></a>
# **api2CommentCommentIdPropertiesPropertyKeyPut**
> api2CommentCommentIdPropertiesPropertyKeyPut(commentId, propertyKey)



Sets the value of the specified comment&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against the comment identified by the key or by the id. The user  who stores the data is required to have permissions to administer the comment.  &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String commentId = "commentId_example"; // String | the comment from which keys will be returned.
    String propertyKey = "propertyKey_example"; // String | the key of the property to return.
    try {
      apiInstance.api2CommentCommentIdPropertiesPropertyKeyPut(commentId, propertyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2CommentCommentIdPropertiesPropertyKeyPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **commentId** | **String**| the comment from which keys will be returned. | |
| **propertyKey** | **String**| the key of the property to return. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2ComponentIdDelete"></a>
# **api2ComponentIdDelete**
> api2ComponentIdDelete(id, moveIssuesTo)



Delete a project component.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The component to delete.
    String moveIssuesTo = "moveIssuesTo_example"; // String | The new component applied to issues whose 'id' component will be deleted.                      If this value is null, then the 'id' component is simply removed from the related isues.
    try {
      apiInstance.api2ComponentIdDelete(id, moveIssuesTo);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2ComponentIdDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The component to delete. | |
| **moveIssuesTo** | **String**| The new component applied to issues whose &#39;id&#39; component will be deleted.                      If this value is null, then the &#39;id&#39; component is simply removed from the related isues. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2DashboardDashboardIdItemsItemIdPropertiesGet"></a>
# **api2DashboardDashboardIdItemsItemIdPropertiesGet**
> api2DashboardDashboardIdItemsItemIdPropertiesGet(itemId, dashboardId)



Returns the keys of all properties for the dashboard item identified by the id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String itemId = "itemId_example"; // String | the dashboard item from which keys will be returned.
    String dashboardId = "dashboardId_example"; // String | 
    try {
      apiInstance.api2DashboardDashboardIdItemsItemIdPropertiesGet(itemId, dashboardId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2DashboardDashboardIdItemsItemIdPropertiesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **itemId** | **String**| the dashboard item from which keys will be returned. | |
| **dashboardId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyDelete"></a>
# **api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyDelete**
> api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyDelete(itemId, dashboardId, propertyKey)



Removes the property from the dashboard item identified by the key or by the id. Ths user removing the property is required  to have permissions to administer the dashboard item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String itemId = "itemId_example"; // String | the dashboard item from which keys will be returned.
    String dashboardId = "dashboardId_example"; // String | 
    String propertyKey = "propertyKey_example"; // String | the key of the property to return.
    try {
      apiInstance.api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyDelete(itemId, dashboardId, propertyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **itemId** | **String**| the dashboard item from which keys will be returned. | |
| **dashboardId** | **String**|  | |
| **propertyKey** | **String**| the key of the property to return. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyGet"></a>
# **api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyGet**
> api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyGet(itemId, dashboardId, propertyKey)



Returns the value of the property with a given key from the dashboard item identified by the id.  The user who retrieves the property is required to have permissions to read the dashboard item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String itemId = "itemId_example"; // String | the dashboard item from which keys will be returned.
    String dashboardId = "dashboardId_example"; // String | 
    String propertyKey = "propertyKey_example"; // String | the key of the property to return.
    try {
      apiInstance.api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyGet(itemId, dashboardId, propertyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **itemId** | **String**| the dashboard item from which keys will be returned. | |
| **dashboardId** | **String**|  | |
| **propertyKey** | **String**| the key of the property to return. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyPut"></a>
# **api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyPut**
> api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyPut(itemId, dashboardId, propertyKey)



Sets the value of the specified dashboard item&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against the dashboard item identified by the id.  The user who stores the data is required to have permissions to administer the dashboard item.  &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String itemId = "itemId_example"; // String | the dashboard item from which keys will be returned.
    String dashboardId = "dashboardId_example"; // String | 
    String propertyKey = "propertyKey_example"; // String | the key of the property to return.
    try {
      apiInstance.api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyPut(itemId, dashboardId, propertyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **itemId** | **String**| the dashboard item from which keys will be returned. | |
| **dashboardId** | **String**|  | |
| **propertyKey** | **String**| the key of the property to return. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2FilterIdColumnsDelete"></a>
# **api2FilterIdColumnsDelete**
> api2FilterIdColumnsDelete(id)



Resets the columns for the given filter such that the filter no longer has its own column config.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | id of the filter
    try {
      apiInstance.api2FilterIdColumnsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2FilterIdColumnsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| id of the filter | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2FilterIdColumnsGet"></a>
# **api2FilterIdColumnsGet**
> api2FilterIdColumnsGet(id)



Returns the default columns for the given filter. Currently logged in user will be used as  the user making such request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | id of the filter
    try {
      apiInstance.api2FilterIdColumnsGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2FilterIdColumnsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| id of the filter | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2FilterIdColumnsPut"></a>
# **api2FilterIdColumnsPut**
> api2FilterIdColumnsPut(id)



Sets the default columns for the given filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | id of the filter
    try {
      apiInstance.api2FilterIdColumnsPut(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2FilterIdColumnsPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| id of the filter | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2IssueIssueIdOrKeyPropertiesGet"></a>
# **api2IssueIssueIdOrKeyPropertiesGet**
> api2IssueIssueIdOrKeyPropertiesGet(issueIdOrKey)



Returns the keys of all properties for the issue identified by the key or by the id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue from which keys will be returned.
    try {
      apiInstance.api2IssueIssueIdOrKeyPropertiesGet(issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2IssueIssueIdOrKeyPropertiesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| the issue from which keys will be returned. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2IssueIssueIdOrKeyPropertiesPropertyKeyDelete"></a>
# **api2IssueIssueIdOrKeyPropertiesPropertyKeyDelete**
> api2IssueIssueIdOrKeyPropertiesPropertyKeyDelete(issueIdOrKey, propertyKey)



Removes the property from the issue identified by the key or by the id. Ths user removing the property is required  to have permissions to edit the issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue from which keys will be returned.
    String propertyKey = "propertyKey_example"; // String | the key of the property to return.
    try {
      apiInstance.api2IssueIssueIdOrKeyPropertiesPropertyKeyDelete(issueIdOrKey, propertyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2IssueIssueIdOrKeyPropertiesPropertyKeyDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| the issue from which keys will be returned. | |
| **propertyKey** | **String**| the key of the property to return. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2IssueIssueIdOrKeyPropertiesPropertyKeyGet"></a>
# **api2IssueIssueIdOrKeyPropertiesPropertyKeyGet**
> api2IssueIssueIdOrKeyPropertiesPropertyKeyGet(issueIdOrKey, propertyKey)



Returns the value of the property with a given key from the issue identified by the key or by the id. The user who retrieves  the property is required to have permissions to read the issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue from which keys will be returned.
    String propertyKey = "propertyKey_example"; // String | the key of the property to return.
    try {
      apiInstance.api2IssueIssueIdOrKeyPropertiesPropertyKeyGet(issueIdOrKey, propertyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2IssueIssueIdOrKeyPropertiesPropertyKeyGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| the issue from which keys will be returned. | |
| **propertyKey** | **String**| the key of the property to return. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2IssueIssueIdOrKeyPropertiesPropertyKeyPut"></a>
# **api2IssueIssueIdOrKeyPropertiesPropertyKeyPut**
> api2IssueIssueIdOrKeyPropertiesPropertyKeyPut(issueIdOrKey, propertyKey)



Sets the value of the specified issue&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against the issue identified by the key or by the id. The user  who stores the data is required to have permissions to edit the issue.  &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue from which keys will be returned.
    String propertyKey = "propertyKey_example"; // String | the key of the property to return.
    try {
      apiInstance.api2IssueIssueIdOrKeyPropertiesPropertyKeyPut(issueIdOrKey, propertyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2IssueIssueIdOrKeyPropertiesPropertyKeyPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| the issue from which keys will be returned. | |
| **propertyKey** | **String**| the key of the property to return. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2IssuesecurityschemesIdGet"></a>
# **api2IssuesecurityschemesIdGet**
> api2IssuesecurityschemesIdGet(id)



Returns the issue security scheme along with that are defined.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      apiInstance.api2IssuesecurityschemesIdGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2IssuesecurityschemesIdGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2IssuetypeIdAvatarPost"></a>
# **api2IssuetypeIdAvatarPost**
> api2IssuetypeIdAvatarPost(id)



Converts temporary avatar into a real avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the id of the issue type, which avatar is updated.
    try {
      apiInstance.api2IssuetypeIdAvatarPost(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2IssuetypeIdAvatarPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the issue type, which avatar is updated. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2IssuetypeIdAvatarTemporaryPost"></a>
# **api2IssuetypeIdAvatarTemporaryPost**
> api2IssuetypeIdAvatarTemporaryPost(id)



Creates temporary avatar using multipart. The response is sent back as JSON stored in a textarea. This is because  the client uses remote iframing to submit avatars using multipart. So we must send them a valid HTML page back from  which the client parses the JSON from.  &lt;p&gt;  Creating a temporary avatar is part of a 3-step process in uploading a new  avatar for an issue type: upload, crop, confirm. This endpoint allows you to use a multipart upload  instead of sending the image directly as the request body.  &lt;/p&gt;  &lt;p&gt;  You *must* use \&quot;avatar\&quot; as the name of the upload parameter:&lt;/p&gt;  &lt;p&gt;  &lt;pre&gt;  curl -c cookiejar.txt -X POST -u admin:admin -H \&quot;X-Atlassian-Token: no-check\&quot; \\    -F \&quot;avatar&#x3D;@mynewavatar.png;type&#x3D;image/png\&quot; \\    &#39;http://localhost:8090/jira/rest/api/2/issuetype/1/avatar/temporary&#39;  &lt;/pre&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the id of the issue type, which avatar is updated.
    try {
      apiInstance.api2IssuetypeIdAvatarTemporaryPost(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2IssuetypeIdAvatarTemporaryPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the issue type, which avatar is updated. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2IssuetypeIdDelete"></a>
# **api2IssuetypeIdDelete**
> api2IssuetypeIdDelete(id, alternativeIssueTypeId)



Deletes the specified issue type. If the issue type has any associated issues, these issues will be migrated to  the alternative issue type specified in the parameter. You can determine the alternative issue types by calling  the &lt;b&gt;/rest/api/2/issuetype/{id}/alternatives&lt;/b&gt; resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the id of the issue type to update.
    String alternativeIssueTypeId = "alternativeIssueTypeId_example"; // String | the id of an issue type to which issues associated with the removed issue type will be migrated.
    try {
      apiInstance.api2IssuetypeIdDelete(id, alternativeIssueTypeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2IssuetypeIdDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the issue type to update. | |
| **alternativeIssueTypeId** | **String**| the id of an issue type to which issues associated with the removed issue type will be migrated. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2IssuetypeIdGet"></a>
# **api2IssuetypeIdGet**
> api2IssuetypeIdGet(id)



Returns a full representation of the issue type that has the given id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the id of the issue type to update.
    try {
      apiInstance.api2IssuetypeIdGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2IssuetypeIdGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the issue type to update. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2IssuetypeIssueTypeIdPropertiesPropertyKeyDelete"></a>
# **api2IssuetypeIssueTypeIdPropertiesPropertyKeyDelete**
> api2IssuetypeIssueTypeIdPropertiesPropertyKeyDelete(issueTypeId, propertyKey)



Removes the property from the issue type identified by the id. Ths user removing the property is required  to have permissions to edit the issue type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueTypeId = "issueTypeId_example"; // String | the issue type from which the keys will be returned
    String propertyKey = "propertyKey_example"; // String | the key of the property to return
    try {
      apiInstance.api2IssuetypeIssueTypeIdPropertiesPropertyKeyDelete(issueTypeId, propertyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2IssuetypeIssueTypeIdPropertiesPropertyKeyDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueTypeId** | **String**| the issue type from which the keys will be returned | |
| **propertyKey** | **String**| the key of the property to return | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2IssuetypeIssueTypeIdPropertiesPropertyKeyGet"></a>
# **api2IssuetypeIssueTypeIdPropertiesPropertyKeyGet**
> api2IssuetypeIssueTypeIdPropertiesPropertyKeyGet(issueTypeId, propertyKey)



Returns the value of the property with a given key from the issue type identified by the id. The user who retrieves  the property is required to have permissions to view the issue type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueTypeId = "issueTypeId_example"; // String | the issue type from which the keys will be returned
    String propertyKey = "propertyKey_example"; // String | the key of the property to return
    try {
      apiInstance.api2IssuetypeIssueTypeIdPropertiesPropertyKeyGet(issueTypeId, propertyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2IssuetypeIssueTypeIdPropertiesPropertyKeyGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueTypeId** | **String**| the issue type from which the keys will be returned | |
| **propertyKey** | **String**| the key of the property to return | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2IssuetypeIssueTypeIdPropertiesPropertyKeyPut"></a>
# **api2IssuetypeIssueTypeIdPropertiesPropertyKeyPut**
> api2IssuetypeIssueTypeIdPropertiesPropertyKeyPut(issueTypeId, propertyKey)



Sets the value of the specified issue type&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against an issue type identified by the id. The user  who stores the data is required to have permissions to edit an issue type.  &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueTypeId = "issueTypeId_example"; // String | the issue type from which the keys will be returned
    String propertyKey = "propertyKey_example"; // String | the key of the property to return
    try {
      apiInstance.api2IssuetypeIssueTypeIdPropertiesPropertyKeyPut(issueTypeId, propertyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2IssuetypeIssueTypeIdPropertiesPropertyKeyPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueTypeId** | **String**| the issue type from which the keys will be returned | |
| **propertyKey** | **String**| the key of the property to return | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2MyselfGet"></a>
# **api2MyselfGet**
> api2MyselfGet()



Returns currently logged user. This resource cannot be accessed anonymously.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.api2MyselfGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2MyselfGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2MyselfPut"></a>
# **api2MyselfPut**
> api2MyselfPut()



Modify currently logged user. The \&quot;value\&quot; fields present will override the existing value.  Fields skipped in request will not be changed. Only email and display name can be change that way.  Requires user password.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.api2MyselfPut();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2MyselfPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2NotificationschemeIdGet"></a>
# **api2NotificationschemeIdGet**
> api2NotificationschemeIdGet(id, expand)



Returns a full representation of the notification scheme for the given id. This resource will return a  notification scheme containing a list of events and recipient configured to receive notifications for these events. Consumer  should allow events without recipients to appear in response. User accessing  the data is required to have permissions to administer at least one project associated with the requested notification scheme.  &lt;p&gt;  Notification recipients can be:  &lt;ul&gt;  &lt;li&gt;current assignee - the value of the notificationType is CurrentAssignee&lt;/li&gt;  &lt;li&gt;issue reporter - the value of the notificationType is Reporter&lt;/li&gt;  &lt;li&gt;current user - the value of the notificationType is CurrentUser&lt;/li&gt;  &lt;li&gt;project lead - the value of the notificationType is ProjectLead&lt;/li&gt;  &lt;li&gt;component lead - the value of the notificationType is ComponentLead&lt;/li&gt;  &lt;li&gt;all watchers - the value of the notification type is AllWatchers&lt;/li&gt;  &lt;li&gt;configured user - the value of the notification type is User. Parameter will contain key of the user. Information about the user will be provided  if &lt;b&gt;user&lt;/b&gt; expand parameter is used. &lt;/li&gt;  &lt;li&gt;configured group - the value of the notification type is Group. Parameter will contain name of the group. Information about the group will be provided  if &lt;b&gt;group&lt;/b&gt; expand parameter is used. &lt;/li&gt;  &lt;li&gt;configured email address - the value of the notification type is EmailAddress, additionally information about the email will be provided.&lt;/li&gt;  &lt;li&gt;users or users in groups in the configured custom fields - the value of the notification type is UserCustomField or GroupCustomField. Parameter  will contain id of the custom field. Information about the field will be provided if &lt;b&gt;field&lt;/b&gt; expand parameter is used. &lt;/li&gt;  &lt;li&gt;configured project role - the value of the notification type is ProjectRole. Parameter will contain project role id. Information about the project role  will be provided if &lt;b&gt;projectRole&lt;/b&gt; expand parameter is used. &lt;/li&gt;  &lt;/ul&gt;  Please see the example for reference.  &lt;/p&gt;  The events can be JIRA system events or events configured by administrator. In case of the system events, data about theirs  ids, names and descriptions is provided. In case of custom events, the template event is included as well.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | an id of the notification scheme to retrieve
    String expand = "expand_example"; // String | 
    try {
      apiInstance.api2NotificationschemeIdGet(id, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2NotificationschemeIdGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| an id of the notification scheme to retrieve | |
| **expand** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2ProjectProjectIdOrKeyAvatarIdDelete"></a>
# **api2ProjectProjectIdOrKeyAvatarIdDelete**
> api2ProjectProjectIdOrKeyAvatarIdDelete(projectIdOrKey, id)



Deletes avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | Project id or project key
    Long id = 56L; // Long | database id for avatar
    try {
      apiInstance.api2ProjectProjectIdOrKeyAvatarIdDelete(projectIdOrKey, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2ProjectProjectIdOrKeyAvatarIdDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| Project id or project key | |
| **id** | **Long**| database id for avatar | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2ProjectProjectIdOrKeyAvatarPost"></a>
# **api2ProjectProjectIdOrKeyAvatarPost**
> api2ProjectProjectIdOrKeyAvatarPost(projectIdOrKey)



Converts temporary avatar into a real avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | 
    try {
      apiInstance.api2ProjectProjectIdOrKeyAvatarPost(projectIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2ProjectProjectIdOrKeyAvatarPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2ProjectProjectIdOrKeyAvatarPut"></a>
# **api2ProjectProjectIdOrKeyAvatarPut**
> api2ProjectProjectIdOrKeyAvatarPut(projectIdOrKey)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | 
    try {
      apiInstance.api2ProjectProjectIdOrKeyAvatarPut(projectIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2ProjectProjectIdOrKeyAvatarPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2ProjectProjectIdOrKeyAvatarTemporaryPost"></a>
# **api2ProjectProjectIdOrKeyAvatarTemporaryPost**
> api2ProjectProjectIdOrKeyAvatarTemporaryPost(projectIdOrKey)



Creates temporary avatar using multipart. The response is sent back as JSON stored in a textarea. This is because  the client uses remote iframing to submit avatars using multipart. So we must send them a valid HTML page back from  which the client parses the JSON.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | Project id or project key
    try {
      apiInstance.api2ProjectProjectIdOrKeyAvatarTemporaryPost(projectIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2ProjectProjectIdOrKeyAvatarTemporaryPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| Project id or project key | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2ProjectProjectIdOrKeyAvatarsGet"></a>
# **api2ProjectProjectIdOrKeyAvatarsGet**
> api2ProjectProjectIdOrKeyAvatarsGet(projectIdOrKey)



Returns all avatars which are visible for the currently logged in user.  The avatars are grouped into  system and custom.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | project id or project key
    try {
      apiInstance.api2ProjectProjectIdOrKeyAvatarsGet(projectIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2ProjectProjectIdOrKeyAvatarsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| project id or project key | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2ProjectProjectIdOrKeyGet"></a>
# **api2ProjectProjectIdOrKeyGet**
> api2ProjectProjectIdOrKeyGet(projectIdOrKey, expand)



Contains a full representation of a project in JSON format.  &lt;p&gt;  All project keys associated with the project will only be returned if &lt;code&gt;expand&#x3D;projectKeys&lt;/code&gt;.  &lt;p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
    String expand = "expand_example"; // String | the parameters to expand
    try {
      apiInstance.api2ProjectProjectIdOrKeyGet(projectIdOrKey, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2ProjectProjectIdOrKeyGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| the project id or project key | |
| **expand** | **String**| the parameters to expand | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2ProjectProjectIdOrKeyPropertiesGet"></a>
# **api2ProjectProjectIdOrKeyPropertiesGet**
> api2ProjectProjectIdOrKeyPropertiesGet(projectIdOrKey)



Returns the keys of all properties for the project identified by the key or by the id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | the project from which keys will be returned.
    try {
      apiInstance.api2ProjectProjectIdOrKeyPropertiesGet(projectIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2ProjectProjectIdOrKeyPropertiesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| the project from which keys will be returned. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2ProjectProjectIdOrKeyPropertiesPropertyKeyDelete"></a>
# **api2ProjectProjectIdOrKeyPropertiesPropertyKeyDelete**
> api2ProjectProjectIdOrKeyPropertiesPropertyKeyDelete(projectIdOrKey, propertyKey)



Removes the property from the project identified by the key or by the id. Ths user removing the property is required  to have permissions to administer the project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | the project from which keys will be returned.
    String propertyKey = "propertyKey_example"; // String | the key of the property to return.
    try {
      apiInstance.api2ProjectProjectIdOrKeyPropertiesPropertyKeyDelete(projectIdOrKey, propertyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2ProjectProjectIdOrKeyPropertiesPropertyKeyDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| the project from which keys will be returned. | |
| **propertyKey** | **String**| the key of the property to return. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2ProjectProjectIdOrKeyPropertiesPropertyKeyGet"></a>
# **api2ProjectProjectIdOrKeyPropertiesPropertyKeyGet**
> api2ProjectProjectIdOrKeyPropertiesPropertyKeyGet(projectIdOrKey, propertyKey)



Returns the value of the property with a given key from the project identified by the key or by the id. The user who retrieves  the property is required to have permissions to read the project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | the project from which keys will be returned.
    String propertyKey = "propertyKey_example"; // String | the key of the property to return.
    try {
      apiInstance.api2ProjectProjectIdOrKeyPropertiesPropertyKeyGet(projectIdOrKey, propertyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2ProjectProjectIdOrKeyPropertiesPropertyKeyGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| the project from which keys will be returned. | |
| **propertyKey** | **String**| the key of the property to return. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2ProjectProjectIdOrKeyPropertiesPropertyKeyPut"></a>
# **api2ProjectProjectIdOrKeyPropertiesPropertyKeyPut**
> api2ProjectProjectIdOrKeyPropertiesPropertyKeyPut(projectIdOrKey, propertyKey)



Sets the value of the specified project&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against the project identified by the key or by the id. The user  who stores the data is required to have permissions to administer the project.  &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | the project from which keys will be returned.
    String propertyKey = "propertyKey_example"; // String | the key of the property to return.
    try {
      apiInstance.api2ProjectProjectIdOrKeyPropertiesPropertyKeyPut(projectIdOrKey, propertyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2ProjectProjectIdOrKeyPropertiesPropertyKeyPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| the project from which keys will be returned. | |
| **propertyKey** | **String**| the key of the property to return. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2ProjectProjectIdOrKeyRoleGet"></a>
# **api2ProjectProjectIdOrKeyRoleGet**
> api2ProjectProjectIdOrKeyRoleGet(projectIdOrKey)



Returns all roles in the given project Id or key, with links to full details on each role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
    try {
      apiInstance.api2ProjectProjectIdOrKeyRoleGet(projectIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2ProjectProjectIdOrKeyRoleGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| the project id or project key | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2ProjectProjectKeyOrIdIssuesecuritylevelschemeGet"></a>
# **api2ProjectProjectKeyOrIdIssuesecuritylevelschemeGet**
> api2ProjectProjectKeyOrIdIssuesecuritylevelschemeGet(projectKeyOrId)



Returns the issue security scheme for project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectKeyOrId = "projectKeyOrId_example"; // String | 
    try {
      apiInstance.api2ProjectProjectKeyOrIdIssuesecuritylevelschemeGet(projectKeyOrId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2ProjectProjectKeyOrIdIssuesecuritylevelschemeGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectKeyOrId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2ProjectProjectKeyOrIdNotificationschemeGet"></a>
# **api2ProjectProjectKeyOrIdNotificationschemeGet**
> api2ProjectProjectKeyOrIdNotificationschemeGet(projectKeyOrId, expand)



Gets a notification scheme associated with the project.  Follow the documentation of /notificationscheme/{id} resource for all details about returned value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectKeyOrId = "projectKeyOrId_example"; // String | key or id of the project
    String expand = "expand_example"; // String | 
    try {
      apiInstance.api2ProjectProjectKeyOrIdNotificationschemeGet(projectKeyOrId, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2ProjectProjectKeyOrIdNotificationschemeGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectKeyOrId** | **String**| key or id of the project | |
| **expand** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2ProjectvalidateKeyGet"></a>
# **api2ProjectvalidateKeyGet**
> api2ProjectvalidateKeyGet(key)



Validates a project key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | the project key
    try {
      apiInstance.api2ProjectvalidateKeyGet(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2ProjectvalidateKeyGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **key** | **String**| the project key | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2RoleGet"></a>
# **api2RoleGet**
> api2RoleGet()



Get all the ProjectRoles available in JIRA. Currently this list is global.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.api2RoleGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2RoleGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarIdDelete"></a>
# **api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarIdDelete**
> api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarIdDelete(id, type, owningObjectId)



Deletes avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | database id for avatar
    String type = "type_example"; // String | Project id or project key
    String owningObjectId = "owningObjectId_example"; // String | 
    try {
      apiInstance.api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarIdDelete(id, type, owningObjectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarIdDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| database id for avatar | |
| **type** | **String**| Project id or project key | |
| **owningObjectId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarPost"></a>
# **api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarPost**
> api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarPost(type, owningObjectId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String type = "type_example"; // String | 
    String owningObjectId = "owningObjectId_example"; // String | 
    try {
      apiInstance.api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarPost(type, owningObjectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **String**|  | |
| **owningObjectId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2UniversalAvatarTypeTypeOwnerOwningObjectIdTempPost"></a>
# **api2UniversalAvatarTypeTypeOwnerOwningObjectIdTempPost**
> api2UniversalAvatarTypeTypeOwnerOwningObjectIdTempPost(type, owningObjectId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String type = "type_example"; // String | 
    String owningObjectId = "owningObjectId_example"; // String | 
    try {
      apiInstance.api2UniversalAvatarTypeTypeOwnerOwningObjectIdTempPost(type, owningObjectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2UniversalAvatarTypeTypeOwnerOwningObjectIdTempPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **String**|  | |
| **owningObjectId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2UserAvatarIdDelete"></a>
# **api2UserAvatarIdDelete**
> api2UserAvatarIdDelete(id, username)



Deletes avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | database id for avatar
    String username = "username_example"; // String | username
    try {
      apiInstance.api2UserAvatarIdDelete(id, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2UserAvatarIdDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| database id for avatar | |
| **username** | **String**| username | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2UserAvatarPost"></a>
# **api2UserAvatarPost**
> api2UserAvatarPost(username)



Converts temporary avatar into a real avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | username
    try {
      apiInstance.api2UserAvatarPost(username);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2UserAvatarPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| username | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2UserAvatarPut"></a>
# **api2UserAvatarPut**
> api2UserAvatarPut(username)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | 
    try {
      apiInstance.api2UserAvatarPut(username);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2UserAvatarPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2UserAvatarTemporaryPost"></a>
# **api2UserAvatarTemporaryPost**
> api2UserAvatarTemporaryPost(username)



Creates temporary avatar using multipart. The response is sent back as JSON stored in a textarea. This is because  the client uses remote iframing to submit avatars using multipart. So we must send them a valid HTML page back from  which the client parses the JSON from.  &lt;p&gt;  Creating a temporary avatar is part of a 3-step process in uploading a new  avatar for a user: upload, crop, confirm. This endpoint allows you to use a multipart upload  instead of sending the image directly as the request body.  &lt;/p&gt;  &lt;p&gt;  You *must* use \&quot;avatar\&quot; as the name of the upload parameter:&lt;/p&gt;  &lt;p/&gt;  &lt;pre&gt;  curl -c cookiejar.txt -X POST -u admin:admin -H \&quot;X-Atlassian-Token: no-check\&quot; \\    -F \&quot;avatar&#x3D;@mynewavatar.png;type&#x3D;image/png\&quot; \\    &#39;http://localhost:8090/jira/rest/api/2/user/avatar/temporary?username&#x3D;admin&#39;  &lt;/pre&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | Username
    try {
      apiInstance.api2UserAvatarTemporaryPost(username);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2UserAvatarTemporaryPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| Username | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2UserAvatarsGet"></a>
# **api2UserAvatarsGet**
> api2UserAvatarsGet(username)



Returns all avatars which are visible for the currently logged in user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | username
    try {
      apiInstance.api2UserAvatarsGet(username);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2UserAvatarsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| username | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2UserColumnsDelete"></a>
# **api2UserColumnsDelete**
> api2UserColumnsDelete(username)



Reset the default columns for the given user to the system default. Admin permission will be required to get  columns for a user other than the currently logged in user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | username
    try {
      apiInstance.api2UserColumnsDelete(username);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2UserColumnsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| username | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2UserColumnsGet"></a>
# **api2UserColumnsGet**
> api2UserColumnsGet(username)



Returns the default columns for the given user. Admin permission will be required to get columns for a user  other than the currently logged in user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | username
    try {
      apiInstance.api2UserColumnsGet(username);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2UserColumnsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| username | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2UserColumnsPut"></a>
# **api2UserColumnsPut**
> api2UserColumnsPut()



Sets the default columns for the given user.  Admin permission will be required to get columns for a user  other than the currently logged in user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.api2UserColumnsPut();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2UserColumnsPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2UserGet"></a>
# **api2UserGet**
> api2UserGet(username, key)



Returns a user. This resource cannot be accessed anonymously.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | the username
    String key = "key_example"; // String | user key
    try {
      apiInstance.api2UserGet(username, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2UserGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| the username | [optional] |
| **key** | **String**| user key | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2UserPropertiesGet"></a>
# **api2UserPropertiesGet**
> api2UserPropertiesGet(userKey, username)



Returns the keys of all properties for the user identified by the key or by the id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String userKey = "userKey_example"; // String | key of the user whose properties are to be returned
    String username = "username_example"; // String | username of the user whose properties are to be returned
    try {
      apiInstance.api2UserPropertiesGet(userKey, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2UserPropertiesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userKey** | **String**| key of the user whose properties are to be returned | [optional] |
| **username** | **String**| username of the user whose properties are to be returned | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2UserPropertiesPropertyKeyDelete"></a>
# **api2UserPropertiesPropertyKeyDelete**
> api2UserPropertiesPropertyKeyDelete(propertyKey, userKey, username)



Removes the property from the user identified by the key or by the id. Ths user removing the property is required  to have permissions to administer the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String propertyKey = "propertyKey_example"; // String | 
    String userKey = "userKey_example"; // String | key of the user whose property is to be removed
    String username = "username_example"; // String | username of the user whose property is to be removed
    try {
      apiInstance.api2UserPropertiesPropertyKeyDelete(propertyKey, userKey, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2UserPropertiesPropertyKeyDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **propertyKey** | **String**|  | |
| **userKey** | **String**| key of the user whose property is to be removed | [optional] |
| **username** | **String**| username of the user whose property is to be removed | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2UserPropertiesPropertyKeyGet"></a>
# **api2UserPropertiesPropertyKeyGet**
> api2UserPropertiesPropertyKeyGet(propertyKey, userKey, username)



Returns the value of the property with a given key from the user identified by the key or by the id. The user who retrieves  the property is required to have permissions to read the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String propertyKey = "propertyKey_example"; // String | 
    String userKey = "userKey_example"; // String | key of the user whose property is to be returned
    String username = "username_example"; // String | username of the user whose property is to be returned
    try {
      apiInstance.api2UserPropertiesPropertyKeyGet(propertyKey, userKey, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2UserPropertiesPropertyKeyGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **propertyKey** | **String**|  | |
| **userKey** | **String**| key of the user whose property is to be returned | [optional] |
| **username** | **String**| username of the user whose property is to be returned | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2UserPropertiesPropertyKeyPut"></a>
# **api2UserPropertiesPropertyKeyPut**
> api2UserPropertiesPropertyKeyPut(propertyKey, userKey, username)



Sets the value of the specified user&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against the user identified by the key or by the id. The user  who stores the data is required to have permissions to administer the user.  &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String propertyKey = "propertyKey_example"; // String | 
    String userKey = "userKey_example"; // String | key of the user whose property is to be set
    String username = "username_example"; // String | username of the user whose property is to be set
    try {
      apiInstance.api2UserPropertiesPropertyKeyPut(propertyKey, userKey, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2UserPropertiesPropertyKeyPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **propertyKey** | **String**|  | |
| **userKey** | **String**| key of the user whose property is to be set | [optional] |
| **username** | **String**| username of the user whose property is to be set | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2UserPut"></a>
# **api2UserPut**
> api2UserPut(username, key)



Modify user. The \&quot;value\&quot; fields present will override the existing value.  Fields skipped in request will not be changed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | the username
    String key = "key_example"; // String | user key
    try {
      apiInstance.api2UserPut(username, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2UserPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| the username | [optional] |
| **key** | **String**| user key | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2VersionIdDelete"></a>
# **api2VersionIdDelete**
> api2VersionIdDelete(id, moveFixIssuesTo, moveAffectedIssuesTo)



Delete a project version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The version to delete
    String moveFixIssuesTo = "moveFixIssuesTo_example"; // String | The version to set fixVersion to on issues where the deleted version is the fix version,                              If null then the fixVersion is removed.
    String moveAffectedIssuesTo = "moveAffectedIssuesTo_example"; // String | The version to set affectedVersion to on issues where the deleted version is the affected version,                              If null then the affectedVersion is removed.
    try {
      apiInstance.api2VersionIdDelete(id, moveFixIssuesTo, moveAffectedIssuesTo);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2VersionIdDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The version to delete | |
| **moveFixIssuesTo** | **String**| The version to set fixVersion to on issues where the deleted version is the fix version,                              If null then the fixVersion is removed. | [optional] |
| **moveAffectedIssuesTo** | **String**| The version to set affectedVersion to on issues where the deleted version is the affected version,                              If null then the affectedVersion is removed. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2VersionIdRemoveAndSwapPost"></a>
# **api2VersionIdRemoveAndSwapPost**
> api2VersionIdRemoveAndSwapPost(id)



Delete a project version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The version to delete
    try {
      apiInstance.api2VersionIdRemoveAndSwapPost(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2VersionIdRemoveAndSwapPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The version to delete | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2VersionVersionIdRemotelinkGlobalIdPost"></a>
# **api2VersionVersionIdRemotelinkGlobalIdPost**
> api2VersionVersionIdRemotelinkGlobalIdPost(versionId, globalId)



Create a remote version link via POST.  The link&#39;s global ID will be taken from the  JSON payload if provided; otherwise, it will be generated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String versionId = "versionId_example"; // String | The version ID of the remote link
    String globalId = "globalId_example"; // String | The global ID of the remote link
    try {
      apiInstance.api2VersionVersionIdRemotelinkGlobalIdPost(versionId, globalId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2VersionVersionIdRemotelinkGlobalIdPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **versionId** | **String**| The version ID of the remote link | |
| **globalId** | **String**| The global ID of the remote link | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2VersionVersionIdRemotelinkPost"></a>
# **api2VersionVersionIdRemotelinkPost**
> api2VersionVersionIdRemotelinkPost(versionId)



Create a remote version link via POST.  The link&#39;s global ID will be taken from the  JSON payload if provided; otherwise, it will be generated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String versionId = "versionId_example"; // String | The version for which to delete ALL existing remote version links
    try {
      apiInstance.api2VersionVersionIdRemotelinkPost(versionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2VersionVersionIdRemotelinkPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **versionId** | **String**| The version for which to delete ALL existing remote version links | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2WorkflowApi2TransitionsIdPropertiesDelete"></a>
# **api2WorkflowApi2TransitionsIdPropertiesDelete**
> api2WorkflowApi2TransitionsIdPropertiesDelete(id, key, workflowName, workflowMode)



Delete a property from the passed transition on the passed workflow. It is not an error to delete a property that  does not exist.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the ID of the transition within the workflow.
    String key = "key_example"; // String | the name of the property to add.
    String workflowName = "workflowName_example"; // String | the name of the workflow to use.
    String workflowMode = "workflowMode_example"; // String | the type of workflow to use. Can either be \"live\" or \"draft\".
    try {
      apiInstance.api2WorkflowApi2TransitionsIdPropertiesDelete(id, key, workflowName, workflowMode);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2WorkflowApi2TransitionsIdPropertiesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the ID of the transition within the workflow. | |
| **key** | **String**| the name of the property to add. | [optional] |
| **workflowName** | **String**| the name of the workflow to use. | [optional] |
| **workflowMode** | **String**| the type of workflow to use. Can either be \&quot;live\&quot; or \&quot;draft\&quot;. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2WorkflowschemeIdIssuetypeIssueTypeDelete"></a>
# **api2WorkflowschemeIdIssuetypeIssueTypeDelete**
> api2WorkflowschemeIdIssuetypeIssueTypeDelete(issueType, id, updateDraftIfNeeded)



Remove the specified issue type mapping from the scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueType = "issueType_example"; // String | the issue type being set.
    Long id = 56L; // Long | the id of the scheme.
    Boolean updateDraftIfNeeded = true; // Boolean | when true will create and return a draft when the workflow scheme cannot be edited                             (e.g. when it is being used by a project).
    try {
      apiInstance.api2WorkflowschemeIdIssuetypeIssueTypeDelete(issueType, id, updateDraftIfNeeded);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2WorkflowschemeIdIssuetypeIssueTypeDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueType** | **String**| the issue type being set. | |
| **id** | **Long**| the id of the scheme. | |
| **updateDraftIfNeeded** | **Boolean**| when true will create and return a draft when the workflow scheme cannot be edited                             (e.g. when it is being used by a project). | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="api2WorkflowschemeIdIssuetypeIssueTypeGet"></a>
# **api2WorkflowschemeIdIssuetypeIssueTypeGet**
> api2WorkflowschemeIdIssuetypeIssueTypeGet(issueType, id, returnDraftIfExists)



Returns the issue type mapping for the passed workflow scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueType = "issueType_example"; // String | the issue type being set.
    Long id = 56L; // Long | the id of the scheme.
    Boolean returnDraftIfExists = false; // Boolean | when true indicates that a scheme's draft, if it exists, should be queried instead of                             the scheme itself.
    try {
      apiInstance.api2WorkflowschemeIdIssuetypeIssueTypeGet(issueType, id, returnDraftIfExists);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#api2WorkflowschemeIdIssuetypeIssueTypeGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueType** | **String**| the issue type being set. | |
| **id** | **Long**| the id of the scheme. | |
| **returnDraftIfExists** | **Boolean**| when true indicates that a scheme&#39;s draft, if it exists, should be queried instead of                             the scheme itself. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="approveUpgrade"></a>
# **approveUpgrade**
> approveUpgrade()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.approveUpgrade();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#approveUpgrade");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="areMetricsExposed"></a>
# **areMetricsExposed**
> areMetricsExposed()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.areMetricsExposed();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#areMetricsExposed");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="assign"></a>
# **assign**
> assign(issueIdOrKey)



Assigns an issue to a user.  You can use this resource to assign issues when the user submitting the request has the assign permission but not the  edit issue permission.  If the name is \&quot;-1\&quot; automatic assignee is used.  A null name will remove the assignee.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | a String containing an issue key
    try {
      apiInstance.assign(issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assign");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| a String containing an issue key | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="assignPermissionScheme"></a>
# **assignPermissionScheme**
> assignPermissionScheme(projectKeyOrId, expand)



Assigns a permission scheme with a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectKeyOrId = "projectKeyOrId_example"; // String | key or id of the project
    String expand = "expand_example"; // String | 
    try {
      apiInstance.assignPermissionScheme(projectKeyOrId, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assignPermissionScheme");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectKeyOrId** | **String**| key or id of the project | |
| **expand** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="callList"></a>
# **callList**
> callList(filter, startAt, maxResults)



Returns a list of all dashboards, optionally filtering them.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String filter = "filter_example"; // String | an optional filter that is applied to the list of dashboards. Valid values include                         <code>\"favourite\"</code> for returning only favourite dashboards, and <code>\"my\"</code> for returning                         dashboards that are owned by the calling user.
    Integer startAt = 56; // Integer | the index of the first dashboard to return (0-based). must be 0 or a multiple of                         <code>maxResults</code>
    Integer maxResults = 56; // Integer | a hint as to the the maximum number of dashboards to return in each call. Note that the                         JIRA server reserves the right to impose a <code>maxResults</code> limit that is lower than the value that a                         client provides, dues to lack or resources or any other condition. When this happens, your results will be                         truncated. Callers should always check the returned <code>maxResults</code> to determine the value that is                         effectively being used.
    try {
      apiInstance.callList(filter, startAt, maxResults);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#callList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **filter** | **String**| an optional filter that is applied to the list of dashboards. Valid values include                         &lt;code&gt;\&quot;favourite\&quot;&lt;/code&gt; for returning only favourite dashboards, and &lt;code&gt;\&quot;my\&quot;&lt;/code&gt; for returning                         dashboards that are owned by the calling user. | [optional] |
| **startAt** | **Integer**| the index of the first dashboard to return (0-based). must be 0 or a multiple of                         &lt;code&gt;maxResults&lt;/code&gt; | [optional] |
| **maxResults** | **Integer**| a hint as to the the maximum number of dashboards to return in each call. Note that the                         JIRA server reserves the right to impose a &lt;code&gt;maxResults&lt;/code&gt; limit that is lower than the value that a                         client provides, dues to lack or resources or any other condition. When this happens, your results will be                         truncated. Callers should always check the returned &lt;code&gt;maxResults&lt;/code&gt; to determine the value that is                         effectively being used. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="canMoveSubTask"></a>
# **canMoveSubTask**
> canMoveSubTask(issueIdOrKey)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | The parent issue's key or id
    try {
      apiInstance.canMoveSubTask(issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#canMoveSubTask");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| The parent issue&#39;s key or id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="cancelUpgrade"></a>
# **cancelUpgrade**
> cancelUpgrade()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.cancelUpgrade();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cancelUpgrade");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="changeMyPassword"></a>
# **changeMyPassword**
> changeMyPassword()



Modify caller password.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.changeMyPassword();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#changeMyPassword");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="changeUserPassword"></a>
# **changeUserPassword**
> changeUserPassword(username, key)



Modify user password.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | the username
    String key = "key_example"; // String | user key
    try {
      apiInstance.changeUserPassword(username, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#changeUserPassword");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| the username | [optional] |
| **key** | **String**| user key | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createComponent"></a>
# **createComponent**
> createComponent()



Create a component via POST.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.createComponent();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createComponent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createCustomField"></a>
# **createCustomField**
> createCustomField()



Creates a custom field using a definition (object encapsulating custom field data)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.createCustomField();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createCustomField");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createDraftForParent"></a>
# **createDraftForParent**
> createDraftForParent(id)



Create a draft for the passed scheme. The draft will be a copy of the state of the parent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the parent scheme.
    try {
      apiInstance.createDraftForParent(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createDraftForParent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the parent scheme. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createFilter"></a>
# **createFilter**
> createFilter(expand)



Creates a new filter, and returns newly created filter.  Currently sets permissions just using the users default sharing permissions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String expand = "expand_example"; // String | the parameters to expand
    try {
      apiInstance.createFilter(expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createFilter");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **expand** | **String**| the parameters to expand | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createGroup"></a>
# **createGroup**
> createGroup()



Creates a group by given group parameter  &lt;p&gt;  Returns REST representation for the requested group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.createGroup();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createIssue"></a>
# **createIssue**
> createIssue()



Creates an issue or a sub-task from a JSON representation.  &lt;p/&gt;  The fields that can be set on create, in either the fields parameter or the update parameter can be determined  using the &lt;b&gt;/rest/api/2/issue/createmeta&lt;/b&gt; resource.  If a field is not configured to appear on the create screen, then it will not be in the createmeta, and a field  validation error will occur if it is submitted.  &lt;p/&gt;  Creating a sub-task is similar to creating a regular issue, with two important differences:  &lt;ul&gt;  &lt;li&gt;the &lt;code&gt;issueType&lt;/code&gt; field must correspond to a sub-task issue type (you can use  &lt;code&gt;/issue/createmeta&lt;/code&gt; to discover sub-task issue types), and&lt;/li&gt;  &lt;li&gt;you must provide a &lt;code&gt;parent&lt;/code&gt; field in the issue create request containing the id or key of the  parent issue.&lt;/li&gt;  &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.createIssue();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createIssue");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createIssueLinkType"></a>
# **createIssueLinkType**
> createIssueLinkType()



Create a new issue link type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.createIssueLinkType();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createIssueLinkType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createIssueType"></a>
# **createIssueType**
> createIssueType()



Creates an issue type from a JSON representation and adds the issue newly created issue type to the default issue  type scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.createIssueType();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createIssueType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createIssues"></a>
# **createIssues**
> createIssues()



Creates issues or sub-tasks from a JSON representation.  &lt;p/&gt;  Creates many issues in one bulk operation.  &lt;p/&gt;  Creating a sub-task is similar to creating a regular issue. More details can be found in createIssue section:  {@link IssueResource#createIssue(IssueUpdateBean)}}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.createIssues();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createIssues");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createOrUpdateRemoteIssueLink"></a>
# **createOrUpdateRemoteIssueLink**
> createOrUpdateRemoteIssueLink(issueIdOrKey)



Creates or updates a remote issue link from a JSON representation. If a globalId is provided and a remote issue link  exists with that globalId, the remote issue link is updated. Otherwise, the remote issue link is created.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue to create the remote issue link for
    try {
      apiInstance.createOrUpdateRemoteIssueLink(issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createOrUpdateRemoteIssueLink");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| the issue to create the remote issue link for | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createPermissionGrant"></a>
# **createPermissionGrant**
> createPermissionGrant(schemeId, expand)



Creates a permission grant in a permission scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long schemeId = 56L; // Long | 
    String expand = "expand_example"; // String | 
    try {
      apiInstance.createPermissionGrant(schemeId, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createPermissionGrant");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **schemeId** | **Long**|  | |
| **expand** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createPermissionScheme"></a>
# **createPermissionScheme**
> createPermissionScheme(expand)



Create a new permission scheme.  This method can create schemes with a defined permission set, or without.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String expand = "expand_example"; // String | 
    try {
      apiInstance.createPermissionScheme(expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createPermissionScheme");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **expand** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createProject"></a>
# **createProject**
> createProject()



Creates a new project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.createProject();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createProject");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createProjectCategory"></a>
# **createProjectCategory**
> createProjectCategory()



Create a project category via POST.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.createProjectCategory();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createProjectCategory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createProjectRole"></a>
# **createProjectRole**
> createProjectRole()



Creates a new ProjectRole to be available in JIRA.  The created role does not have any default actors assigned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.createProjectRole();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createProjectRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createProperty"></a>
# **createProperty**
> createProperty(id, key, workflowName, workflowMode)



Add a new property to a transition. Trying to add a property that already  exists will fail.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the ID of the transition within the workflow.
    String key = "key_example"; // String | the name of the property to add.
    String workflowName = "workflowName_example"; // String | the name of the workflow to use.
    String workflowMode = "workflowMode_example"; // String | the type of workflow to use. Can either be \"live\" or \"draft\".
    try {
      apiInstance.createProperty(id, key, workflowName, workflowMode);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createProperty");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the ID of the transition within the workflow. | |
| **key** | **String**| the name of the property to add. | [optional] |
| **workflowName** | **String**| the name of the workflow to use. | [optional] |
| **workflowMode** | **String**| the type of workflow to use. Can either be \&quot;live\&quot; or \&quot;draft\&quot;. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createScheme"></a>
# **createScheme**
> createScheme()



Create a new workflow scheme.  &lt;p/&gt;  The body contains a representation of the new scheme. Values not passed are assumed to be set to their defaults.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.createScheme();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createScheme");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createUser"></a>
# **createUser**
> createUser()



Create user. By default created user will not be notified with email.  If password field is not set then password will be randomly generated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.createUser();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="createVersion"></a>
# **createVersion**
> createVersion()



Create a version via POST.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.createVersion();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createVersion");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="currentUser"></a>
# **currentUser**
> currentUser()



Returns information about the currently authenticated user&#39;s session. If the caller is not authenticated they  will get a 401 Unauthorized status code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.currentUser();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#currentUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteActor"></a>
# **deleteActor**
> deleteActor(projectIdOrKey, id, user, group)



Deletes actors (users or groups) from a project role.  &lt;p&gt;  &lt;ul&gt;  &lt;li&gt;Delete a user from the role: &lt;code&gt;/rest/api/2/project/{projectIdOrKey}/role/{roleId}?user&#x3D;{username}&lt;/code&gt;&lt;/li&gt;  &lt;li&gt;Delete a group from the role: &lt;code&gt;/rest/api/2/project/{projectIdOrKey}/role/{roleId}?group&#x3D;{groupname}&lt;/code&gt;&lt;/li&gt;  &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
    Long id = 56L; // Long | the project role id
    String user = "user_example"; // String | the username to remove from the project role
    String group = "group_example"; // String | the groupname to remove from the project role
    try {
      apiInstance.deleteActor(projectIdOrKey, id, user, group);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteActor");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| the project id or project key | |
| **id** | **Long**| the project role id | |
| **user** | **String**| the username to remove from the project role | [optional] |
| **group** | **String**| the groupname to remove from the project role | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteComment"></a>
# **deleteComment**
> deleteComment(issueIdOrKey, id)



Deletes an existing comment .

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | of the issue the comment belongs to
    String id = "id_example"; // String | the ID of the comment to request
    try {
      apiInstance.deleteComment(issueIdOrKey, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteComment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| of the issue the comment belongs to | |
| **id** | **String**| the ID of the comment to request | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteDefault"></a>
# **deleteDefault**
> deleteDefault(id, updateDraftIfNeeded)



Remove the default workflow from the passed workflow scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the scheme.
    Boolean updateDraftIfNeeded = true; // Boolean | when true will create and return a draft when the workflow scheme cannot be edited                             (e.g. when it is being used by a project).
    try {
      apiInstance.deleteDefault(id, updateDraftIfNeeded);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteDefault");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the scheme. | |
| **updateDraftIfNeeded** | **Boolean**| when true will create and return a draft when the workflow scheme cannot be edited                             (e.g. when it is being used by a project). | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteDraftById"></a>
# **deleteDraftById**
> deleteDraftById(id)



Delete the passed draft workflow scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the parent scheme.
    try {
      apiInstance.deleteDraftById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteDraftById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the parent scheme. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteDraftDefault"></a>
# **deleteDraftDefault**
> deleteDraftDefault(id)



Remove the default workflow from the passed draft workflow scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the parent scheme.
    try {
      apiInstance.deleteDraftDefault(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteDraftDefault");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the parent scheme. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteDraftIssueType"></a>
# **deleteDraftIssueType**
> deleteDraftIssueType(issueType, id)



Remove the specified issue type mapping from the draft scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueType = "issueType_example"; // String | the issue type being set.
    Long id = 56L; // Long | the id of the parent scheme.
    try {
      apiInstance.deleteDraftIssueType(issueType, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteDraftIssueType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueType** | **String**| the issue type being set. | |
| **id** | **Long**| the id of the parent scheme. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteDraftWorkflowMapping"></a>
# **deleteDraftWorkflowMapping**
> deleteDraftWorkflowMapping(id, workflowName)



Delete the passed workflow from the draft workflow scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the parent scheme.
    String workflowName = "workflowName_example"; // String | the name of the workflow to delete.
    try {
      apiInstance.deleteDraftWorkflowMapping(id, workflowName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteDraftWorkflowMapping");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the parent scheme. | |
| **workflowName** | **String**| the name of the workflow to delete. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteFilter"></a>
# **deleteFilter**
> deleteFilter(id)



Delete a filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the filter being looked up
    try {
      apiInstance.deleteFilter(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteFilter");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the filter being looked up | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteIssue"></a>
# **deleteIssue**
> deleteIssue(issueIdOrKey, deleteSubtasks)



Delete an issue.  &lt;p/&gt;  If the issue has subtasks you must set the parameter deleteSubtasks&#x3D;true to delete the issue.  You cannot delete an issue without its subtasks also being deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue id or key to update (i.e. JRA-1330)
    String deleteSubtasks = "deleteSubtasks_example"; // String | a String of true or false indicating that any subtasks should also be deleted.  If the                        issue has no subtasks this parameter is ignored.  If the issue has subtasks and this parameter is missing or false,                        then the issue will not be deleted and an error will be returned.
    try {
      apiInstance.deleteIssue(issueIdOrKey, deleteSubtasks);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteIssue");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| the issue id or key to update (i.e. JRA-1330) | |
| **deleteSubtasks** | **String**| a String of true or false indicating that any subtasks should also be deleted.  If the                        issue has no subtasks this parameter is ignored.  If the issue has subtasks and this parameter is missing or false,                        then the issue will not be deleted and an error will be returned. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteIssueLink"></a>
# **deleteIssueLink**
> deleteIssueLink(linkId)



Deletes an issue link with the specified id.  To be able to delete an issue link you must be able to view both issues and must have the link issue permission  for at least one of the issues.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String linkId = "linkId_example"; // String | the issue link id.
    try {
      apiInstance.deleteIssueLink(linkId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteIssueLink");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **linkId** | **String**| the issue link id. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteIssueLinkType"></a>
# **deleteIssueLinkType**
> deleteIssueLinkType(issueLinkTypeId)



Delete the specified issue link type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueLinkTypeId = "issueLinkTypeId_example"; // String | 
    try {
      apiInstance.deleteIssueLinkType(issueLinkTypeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteIssueLinkType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueLinkTypeId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deletePermissionScheme"></a>
# **deletePermissionScheme**
> deletePermissionScheme(schemeId)



Deletes a permission scheme identified by the given id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long schemeId = 56L; // Long | 
    try {
      apiInstance.deletePermissionScheme(schemeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deletePermissionScheme");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **schemeId** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deletePermissionSchemeEntity"></a>
# **deletePermissionSchemeEntity**
> deletePermissionSchemeEntity(permissionId, schemeId)



Deletes a permission grant from a permission scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long permissionId = 56L; // Long | 
    Long schemeId = 56L; // Long | 
    try {
      apiInstance.deletePermissionSchemeEntity(permissionId, schemeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deletePermissionSchemeEntity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **permissionId** | **Long**|  | |
| **schemeId** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteProject"></a>
# **deleteProject**
> deleteProject(projectIdOrKey)



Deletes a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
    try {
      apiInstance.deleteProject(projectIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteProject");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| the project id or project key | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteProjectRole"></a>
# **deleteProjectRole**
> deleteProjectRole(id, swap)



Deletes a role. May return 403 in the future

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | 
    Long swap = 56L; // Long | if given, removes a role even if it is used in scheme by replacing the role with the given one
    try {
      apiInstance.deleteProjectRole(id, swap);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteProjectRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**|  | |
| **swap** | **Long**| if given, removes a role even if it is used in scheme by replacing the role with the given one | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteProjectRoleActorsFromRole"></a>
# **deleteProjectRoleActorsFromRole**
> deleteProjectRoleActorsFromRole(id, user, group)



Removes default actor from the given role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the role id to remove the actors from
    String user = "user_example"; // String | if given, removes an actor from given role
    String group = "group_example"; // String | if given, removes an actor from given role
    try {
      apiInstance.deleteProjectRoleActorsFromRole(id, user, group);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteProjectRoleActorsFromRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the role id to remove the actors from | |
| **user** | **String**| if given, removes an actor from given role | [optional] |
| **group** | **String**| if given, removes an actor from given role | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteRemoteIssueLinkByGlobalId"></a>
# **deleteRemoteIssueLinkByGlobalId**
> deleteRemoteIssueLinkByGlobalId(issueIdOrKey, globalId)



Delete the remote issue link with the given global id on the issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue to create the remote issue link for
    String globalId = "globalId_example"; // String | the global id of the remote issue link
    try {
      apiInstance.deleteRemoteIssueLinkByGlobalId(issueIdOrKey, globalId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteRemoteIssueLinkByGlobalId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| the issue to create the remote issue link for | |
| **globalId** | **String**| the global id of the remote issue link | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteRemoteIssueLinkById"></a>
# **deleteRemoteIssueLinkById**
> deleteRemoteIssueLinkById(linkId, issueIdOrKey)



Delete the remote issue link with the given id on the issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String linkId = "linkId_example"; // String | the id of the remote issue link
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue to create the remote issue link for
    try {
      apiInstance.deleteRemoteIssueLinkById(linkId, issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteRemoteIssueLinkById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **linkId** | **String**| the id of the remote issue link | |
| **issueIdOrKey** | **String**| the issue to create the remote issue link for | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteRemoteVersionLink"></a>
# **deleteRemoteVersionLink**
> deleteRemoteVersionLink(versionId, globalId)



Delete a specific remote version link with the given version ID and global ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String versionId = "versionId_example"; // String | The version ID of the remote link
    String globalId = "globalId_example"; // String | The global ID of the remote link
    try {
      apiInstance.deleteRemoteVersionLink(versionId, globalId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteRemoteVersionLink");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **versionId** | **String**| The version ID of the remote link | |
| **globalId** | **String**| The global ID of the remote link | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteRemoteVersionLinksByVersionId"></a>
# **deleteRemoteVersionLinksByVersionId**
> deleteRemoteVersionLinksByVersionId(versionId)



Delete all remote version links for a given version ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String versionId = "versionId_example"; // String | The version for which to delete ALL existing remote version links
    try {
      apiInstance.deleteRemoteVersionLinksByVersionId(versionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteRemoteVersionLinksByVersionId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **versionId** | **String**| The version for which to delete ALL existing remote version links | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteScheme"></a>
# **deleteScheme**
> deleteScheme(id)



Delete the passed workflow scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the scheme.
    try {
      apiInstance.deleteScheme(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteScheme");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the scheme. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteSharePermission"></a>
# **deleteSharePermission**
> deleteSharePermission(id, permissionId)



Removes a share permissions from the given filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | 
    Long permissionId = 56L; // Long | 
    try {
      apiInstance.deleteSharePermission(id, permissionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteSharePermission");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**|  | |
| **permissionId** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteTab"></a>
# **deleteTab**
> deleteTab(screenId, tabId)



Deletes tab to give screen

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long screenId = 56L; // Long | id of screen
    Long tabId = 56L; // Long | id of tab
    try {
      apiInstance.deleteTab(screenId, tabId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteTab");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **screenId** | **Long**| id of screen | |
| **tabId** | **Long**| id of tab | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteWorkflowMapping"></a>
# **deleteWorkflowMapping**
> deleteWorkflowMapping(id, workflowName, updateDraftIfNeeded)



Delete the passed workflow from the workflow scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the scheme.
    String workflowName = "workflowName_example"; // String | the name of the workflow to delete.
    Boolean updateDraftIfNeeded = true; // Boolean | flag to indicate if a draft should be created if necessary to delete the workflow                             from the scheme.
    try {
      apiInstance.deleteWorkflowMapping(id, workflowName, updateDraftIfNeeded);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteWorkflowMapping");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the scheme. | |
| **workflowName** | **String**| the name of the workflow to delete. | [optional] |
| **updateDraftIfNeeded** | **Boolean**| flag to indicate if a draft should be created if necessary to delete the workflow                             from the scheme. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="deleteWorklog"></a>
# **deleteWorklog**
> deleteWorklog(issueIdOrKey, id, adjustEstimate, newEstimate, increaseBy)



Deletes an existing worklog entry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | a string containing the issue id or key the worklog belongs to
    String id = "id_example"; // String | id of the worklog to be deleted
    String adjustEstimate = "adjustEstimate_example"; // String | (optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are                        <ul>                        <li>\"new\" - sets the estimate to a specific value</li>                        <li>\"leave\"- leaves the estimate as is</li>                        <li>\"manual\" - specify a specific amount to increase remaining estimate by</li>                        <li>\"auto\"- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog</li> </ul>
    String newEstimate = "newEstimate_example"; // String | (required when \"new\" is selected for adjustEstimate) the new value for the remaining estimate field. e.g. \"2d\"
    String increaseBy = "increaseBy_example"; // String | (required when \"manual\" is selected for adjustEstimate) the amount to increase the remaining estimate by e.g. \"2d\"
    try {
      apiInstance.deleteWorklog(issueIdOrKey, id, adjustEstimate, newEstimate, increaseBy);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteWorklog");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| a string containing the issue id or key the worklog belongs to | |
| **id** | **String**| id of the worklog to be deleted | |
| **adjustEstimate** | **String**| (optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are                        &lt;ul&gt;                        &lt;li&gt;\&quot;new\&quot; - sets the estimate to a specific value&lt;/li&gt;                        &lt;li&gt;\&quot;leave\&quot;- leaves the estimate as is&lt;/li&gt;                        &lt;li&gt;\&quot;manual\&quot; - specify a specific amount to increase remaining estimate by&lt;/li&gt;                        &lt;li&gt;\&quot;auto\&quot;- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog&lt;/li&gt; &lt;/ul&gt; | [optional] |
| **newEstimate** | **String**| (required when \&quot;new\&quot; is selected for adjustEstimate) the new value for the remaining estimate field. e.g. \&quot;2d\&quot; | [optional] |
| **increaseBy** | **String**| (required when \&quot;manual\&quot; is selected for adjustEstimate) the amount to increase the remaining estimate by e.g. \&quot;2d\&quot; | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="doTransition"></a>
# **doTransition**
> doTransition(issueIdOrKey)



Perform a transition on an issue.  When performing the transition you can update or set other issue fields.  &lt;p/&gt;  The fields that can be set on transtion, in either the fields parameter or the update parameter can be determined  using the &lt;b&gt;/rest/api/2/issue/{issueIdOrKey}/transitions?expand&#x3D;transitions.fields&lt;/b&gt; resource.  If a field is not configured to appear on the transition screen, then it will not be in the transition metadata, and a field  validation error will occur if it is submitted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue whose transitions you want to view
    try {
      apiInstance.doTransition(issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#doTransition");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| the issue whose transitions you want to view | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="editFilter"></a>
# **editFilter**
> editFilter(id, expand)



Updates an existing filter, and returns its new value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the filter being looked up
    String expand = "expand_example"; // String | the parameters to expand
    try {
      apiInstance.editFilter(id, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#editFilter");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the filter being looked up | |
| **expand** | **String**| the parameters to expand | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="editIssue"></a>
# **editIssue**
> editIssue(issueIdOrKey, notifyUsers)



Edits an issue from a JSON representation.  &lt;p/&gt;  The issue can either be updated by setting explicit the field value(s)  or by using an operation to change the field value.  &lt;p/&gt;  The fields that can be updated, in either the fields parameter or the update parameter, can be determined  using the &lt;b&gt;/rest/api/2/issue/{issueIdOrKey}/editmeta&lt;/b&gt; resource.&lt;br&gt;  If a field is not configured to appear on the edit screen, then it will not be in the editmeta, and a field  validation error will occur if it is submitted.  &lt;p/&gt;  Specifying a \&quot;field_id\&quot;: field_value in the \&quot;fields\&quot; is a shorthand for a \&quot;set\&quot; operation in the \&quot;update\&quot; section.&lt;br&gt;  Field should appear either in \&quot;fields\&quot; or \&quot;update\&quot;, not in both.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue id or key to update (i.e. JRA-1330)
    Boolean notifyUsers = true; // Boolean | send the email with notification that the issue was updated to users that watch it.                     Admin or project admin permissions are required to disable the notification.
    try {
      apiInstance.editIssue(issueIdOrKey, notifyUsers);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#editIssue");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| the issue id or key to update (i.e. JRA-1330) | |
| **notifyUsers** | **Boolean**| send the email with notification that the issue was updated to users that watch it.                     Admin or project admin permissions are required to disable the notification. | [optional] [default to true] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="expandForHumans"></a>
# **expandForHumans**
> expandForHumans(id)



Tries to expand an attachment. Output is human-readable and subject to change.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the id of the attachment to expand.
    try {
      apiInstance.expandForHumans(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#expandForHumans");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the attachment to expand. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="expandForMachines"></a>
# **expandForMachines**
> expandForMachines(id)



Tries to expand an attachment. Output is raw and should be backwards-compatible through the course of time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the id of the attachment to expand.
    try {
      apiInstance.expandForMachines(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#expandForMachines");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the attachment to expand. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="findAssignableUsers"></a>
# **findAssignableUsers**
> findAssignableUsers(username, project, issueKey, startAt, maxResults, actionDescriptorId)



Returns a list of users that match the search string. This resource cannot be accessed anonymously.  Please note that this resource should be called with an issue key when a list of assignable users is retrieved  for editing.  For create only a project key should be supplied.  The list of assignable users may be incorrect  if it&#39;s called with the project key for editing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | the username
    String project = "project_example"; // String | the key of the project we are finding assignable users for
    String issueKey = "issueKey_example"; // String | the issue key for the issue being edited we need to find assignable users for.
    Integer startAt = 56; // Integer | the index of the first user to return (0-based)
    Integer maxResults = 56; // Integer | the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                    If you specify a value that is higher than this number, your search results will be truncated.
    Integer actionDescriptorId = 56; // Integer | 
    try {
      apiInstance.findAssignableUsers(username, project, issueKey, startAt, maxResults, actionDescriptorId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#findAssignableUsers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| the username | [optional] |
| **project** | **String**| the key of the project we are finding assignable users for | [optional] |
| **issueKey** | **String**| the issue key for the issue being edited we need to find assignable users for. | [optional] |
| **startAt** | **Integer**| the index of the first user to return (0-based) | [optional] |
| **maxResults** | **Integer**| the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                    If you specify a value that is higher than this number, your search results will be truncated. | [optional] |
| **actionDescriptorId** | **Integer**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="findBulkAssignableUsers"></a>
# **findBulkAssignableUsers**
> findBulkAssignableUsers(username, projectKeys, startAt, maxResults)



Returns a list of users that match the search string and can be assigned issues for all the given projects.  This resource cannot be accessed anonymously.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | the username
    String projectKeys = "projectKeys_example"; // String | the keys of the projects we are finding assignable users for, comma-separated
    Integer startAt = 56; // Integer | the index of the first user to return (0-based)
    Integer maxResults = 56; // Integer | the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                        If you specify a value that is higher than this number, your search results will be truncated.
    try {
      apiInstance.findBulkAssignableUsers(username, projectKeys, startAt, maxResults);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#findBulkAssignableUsers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| the username | [optional] |
| **projectKeys** | **String**| the keys of the projects we are finding assignable users for, comma-separated | [optional] |
| **startAt** | **Integer**| the index of the first user to return (0-based) | [optional] |
| **maxResults** | **Integer**| the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                        If you specify a value that is higher than this number, your search results will be truncated. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="findGroups"></a>
# **findGroups**
> findGroups(query, exclude, maxResults, userName)



Returns groups with substrings matching a given query. This is mainly for use with  the group picker, so the returned groups contain html to be used as picker suggestions.  The groups are also wrapped in a single response object that also contains a header for  use in the picker, specifically &lt;i&gt;Showing X of Y matching groups&lt;/i&gt;.  &lt;p&gt;  The number of groups returned is limited by the system property \&quot;jira.ajax.autocomplete.limit\&quot;  &lt;p&gt;  The groups will be unique and sorted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String query = "query_example"; // String | a String to match groups agains
    String exclude = "exclude_example"; // String | 
    Integer maxResults = 56; // Integer | 
    String userName = "userName_example"; // String | 
    try {
      apiInstance.findGroups(query, exclude, maxResults, userName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#findGroups");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **query** | **String**| a String to match groups agains | [optional] |
| **exclude** | **String**|  | [optional] |
| **maxResults** | **Integer**|  | [optional] |
| **userName** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="findUsers"></a>
# **findUsers**
> findUsers(username, startAt, maxResults, includeActive, includeInactive)



Returns a list of users that match the search string. This resource cannot be accessed anonymously.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | A query string used to search username, name or e-mail address
    Integer startAt = 56; // Integer | the index of the first user to return (0-based)
    Integer maxResults = 56; // Integer | the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                         If you specify a value that is higher than this number, your search results will be truncated.
    Boolean includeActive = true; // Boolean | If true, then active users are included in the results (default true)
    Boolean includeInactive = true; // Boolean | If true, then inactive users are included in the results (default false)
    try {
      apiInstance.findUsers(username, startAt, maxResults, includeActive, includeInactive);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#findUsers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| A query string used to search username, name or e-mail address | [optional] |
| **startAt** | **Integer**| the index of the first user to return (0-based) | [optional] |
| **maxResults** | **Integer**| the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                         If you specify a value that is higher than this number, your search results will be truncated. | [optional] |
| **includeActive** | **Boolean**| If true, then active users are included in the results (default true) | [optional] |
| **includeInactive** | **Boolean**| If true, then inactive users are included in the results (default false) | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="findUsersAndGroups"></a>
# **findUsersAndGroups**
> findUsersAndGroups(query, maxResults, showAvatar, fieldId, projectId, issueTypeId)



Returns a list of users and groups matching query with highlighting. This resource cannot be accessed  anonymously.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String query = "query_example"; // String | A string used to search username, Name or e-mail address
    Integer maxResults = 56; // Integer | the maximum number of users to return (defaults to 50). The maximum allowed value is 1000. If                     you specify a value that is higher than this number, your search results will be truncated.
    Boolean showAvatar = true; // Boolean | 
    String fieldId = "fieldId_example"; // String | The custom field id, if this request comes from a custom field, such as a user picker. Optional.
    String projectId = "projectId_example"; // String | The list of project ids to further restrict the search                     This parameter can occur multiple times to pass in multiple project ids.                     Comma separated value is not supported.                     This parameter is only used when fieldId is present.
    String issueTypeId = "issueTypeId_example"; // String | The list of issue type ids to further restrict the search.                     This parameter can occur multiple times to pass in multiple issue type ids.                     Comma separated value is not supported.                     Special values such as -1 (all standard issue types), -2 (all subtask issue types) are supported.                     This parameter is only used when fieldId is present.
    try {
      apiInstance.findUsersAndGroups(query, maxResults, showAvatar, fieldId, projectId, issueTypeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#findUsersAndGroups");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **query** | **String**| A string used to search username, Name or e-mail address | [optional] |
| **maxResults** | **Integer**| the maximum number of users to return (defaults to 50). The maximum allowed value is 1000. If                     you specify a value that is higher than this number, your search results will be truncated. | [optional] |
| **showAvatar** | **Boolean**|  | [optional] |
| **fieldId** | **String**| The custom field id, if this request comes from a custom field, such as a user picker. Optional. | [optional] |
| **projectId** | **String**| The list of project ids to further restrict the search                     This parameter can occur multiple times to pass in multiple project ids.                     Comma separated value is not supported.                     This parameter is only used when fieldId is present. | [optional] |
| **issueTypeId** | **String**| The list of issue type ids to further restrict the search.                     This parameter can occur multiple times to pass in multiple issue type ids.                     Comma separated value is not supported.                     Special values such as -1 (all standard issue types), -2 (all subtask issue types) are supported.                     This parameter is only used when fieldId is present. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="findUsersForPicker"></a>
# **findUsersForPicker**
> findUsersForPicker(query, maxResults, showAvatar, exclude)



Returns a list of users matching query with highlighting. This resource cannot be accessed anonymously.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String query = "query_example"; // String | A string used to search username, Name or e-mail address
    Integer maxResults = 56; // Integer | the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                    If you specify a value that is higher than this number, your search results will be truncated.
    Boolean showAvatar = true; // Boolean | 
    String exclude = "exclude_example"; // String | 
    try {
      apiInstance.findUsersForPicker(query, maxResults, showAvatar, exclude);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#findUsersForPicker");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **query** | **String**| A string used to search username, Name or e-mail address | [optional] |
| **maxResults** | **Integer**| the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                    If you specify a value that is higher than this number, your search results will be truncated. | [optional] |
| **showAvatar** | **Boolean**|  | [optional] |
| **exclude** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="findUsersWithAllPermissions"></a>
# **findUsersWithAllPermissions**
> findUsersWithAllPermissions(username, permissions, issueKey, projectKey, startAt, maxResults)



Returns a list of active users that match the search string and have all specified permissions for the project or issue.&lt;br&gt;  This resource can be accessed by users with ADMINISTER_PROJECT permission for the project or global ADMIN or SYSADMIN rights.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | the username filter, list includes all users if unspecified
    String permissions = "permissions_example"; // String | comma separated list of permissions for project or issue returned users must have, see                     <a href=\"https://developer.atlassian.com/static/javadoc/jira/6.0/reference/com/atlassian/jira/security/Permissions.Permission.html\">Permissions</a>                     JavaDoc for the list of all possible permissions.
    String issueKey = "issueKey_example"; // String | the issue key for the issue for which returned users have specified permissions.
    String projectKey = "projectKey_example"; // String | the optional project key to search for users with if no issueKey is supplied.
    Integer startAt = 56; // Integer | the index of the first user to return (0-based)
    Integer maxResults = 56; // Integer | the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                     If you specify a value that is higher than this number, your search results will be truncated.
    try {
      apiInstance.findUsersWithAllPermissions(username, permissions, issueKey, projectKey, startAt, maxResults);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#findUsersWithAllPermissions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| the username filter, list includes all users if unspecified | [optional] |
| **permissions** | **String**| comma separated list of permissions for project or issue returned users must have, see                     &lt;a href&#x3D;\&quot;https://developer.atlassian.com/static/javadoc/jira/6.0/reference/com/atlassian/jira/security/Permissions.Permission.html\&quot;&gt;Permissions&lt;/a&gt;                     JavaDoc for the list of all possible permissions. | [optional] |
| **issueKey** | **String**| the issue key for the issue for which returned users have specified permissions. | [optional] |
| **projectKey** | **String**| the optional project key to search for users with if no issueKey is supplied. | [optional] |
| **startAt** | **Integer**| the index of the first user to return (0-based) | [optional] |
| **maxResults** | **Integer**| the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                     If you specify a value that is higher than this number, your search results will be truncated. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="findUsersWithBrowsePermission"></a>
# **findUsersWithBrowsePermission**
> findUsersWithBrowsePermission(username, issueKey, projectKey, startAt, maxResults)



Returns a list of active users that match the search string. This resource cannot be accessed anonymously   and requires the Browse Users global permission.  Given an issue key this resource will provide a list of users that match the search string and have  the browse issue permission for the issue provided.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | the username filter, no users returned if left blank
    String issueKey = "issueKey_example"; // String | the issue key for the issue being edited we need to find viewable users for.
    String projectKey = "projectKey_example"; // String | the optional project key to search for users with if no issueKey is supplied.
    Integer startAt = 56; // Integer | the index of the first user to return (0-based)
    Integer maxResults = 56; // Integer | the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                    If you specify a value that is higher than this number, your search results will be truncated.
    try {
      apiInstance.findUsersWithBrowsePermission(username, issueKey, projectKey, startAt, maxResults);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#findUsersWithBrowsePermission");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| the username filter, no users returned if left blank | [optional] |
| **issueKey** | **String**| the issue key for the issue being edited we need to find viewable users for. | [optional] |
| **projectKey** | **String**| the optional project key to search for users with if no issueKey is supplied. | [optional] |
| **startAt** | **Integer**| the index of the first user to return (0-based) | [optional] |
| **maxResults** | **Integer**| the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                    If you specify a value that is higher than this number, your search results will be truncated. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="fullyUpdateProjectRole"></a>
# **fullyUpdateProjectRole**
> fullyUpdateProjectRole(id)



Fully updates a roles. Both name and description must be given.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      apiInstance.fullyUpdateProjectRole(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#fullyUpdateProjectRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="get"></a>
# **get**
> get(key)



Returns the ApplicationRole with passed key if it exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | the key of the role to update.
    try {
      apiInstance.get(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#get");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **key** | **String**| the key of the role to update. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAccessibleProjectTypeByKey"></a>
# **getAccessibleProjectTypeByKey**
> getAccessibleProjectTypeByKey(projectTypeKey)



Returns the project type with the given key, if it is accessible to the logged in user.  This takes into account whether the user is licensed on the Application that defines the project type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectTypeKey = "projectTypeKey_example"; // String | 
    try {
      apiInstance.getAccessibleProjectTypeByKey(projectTypeKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAccessibleProjectTypeByKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectTypeKey** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAdvancedSettings"></a>
# **getAdvancedSettings**
> getAdvancedSettings()



Returns the properties that are displayed on the \&quot;General Configuration &gt; Advanced Settings\&quot; page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getAdvancedSettings();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAdvancedSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAll"></a>
# **getAll**
> getAll()



Returns all ApplicationRoles in the system. Will also return an ETag header containing a version hash of the  collection of ApplicationRoles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getAll();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAll");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAllFields"></a>
# **getAllFields**
> getAllFields(screenId, tabId, projectKey)



Gets all fields for a given tab

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long screenId = 56L; // Long | id of screen
    Long tabId = 56L; // Long | id of tab
    String projectKey = "projectKey_example"; // String | the key of the project; this parameter is optional
    try {
      apiInstance.getAllFields(screenId, tabId, projectKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAllFields");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **screenId** | **Long**| id of screen | |
| **tabId** | **Long**| id of tab | |
| **projectKey** | **String**| the key of the project; this parameter is optional | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAllPermissions"></a>
# **getAllPermissions**
> getAllPermissions()



Returns all permissions that are present in the JIRA instance - Global, Project and the global ones added by plugins

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getAllPermissions();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAllPermissions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAllProjectCategories"></a>
# **getAllProjectCategories**
> getAllProjectCategories()



Returns all project categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getAllProjectCategories();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAllProjectCategories");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAllProjectTypes"></a>
# **getAllProjectTypes**
> getAllProjectTypes()



Returns all the project types defined on the JIRA instance, not taking into account whether  the license to use those project types is valid or not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getAllProjectTypes();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAllProjectTypes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAllProjects"></a>
# **getAllProjects**
> getAllProjects(expand, recent)



Returns all projects which are visible for the currently logged in user. If no user is logged in, it returns the  list of projects that are visible when using anonymous access.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String expand = "expand_example"; // String | the parameters to expand
    Integer recent = 56; // Integer | if this parameter is set then only projects recently accessed by the current user (if not logged in then based on HTTP session) will be returned (maximum count limited to the specified number but no more than 20).
    try {
      apiInstance.getAllProjects(expand, recent);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAllProjects");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **expand** | **String**| the parameters to expand | [optional] |
| **recent** | **Integer**| if this parameter is set then only projects recently accessed by the current user (if not logged in then based on HTTP session) will be returned (maximum count limited to the specified number but no more than 20). | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAllStatuses"></a>
# **getAllStatuses**
> getAllStatuses(projectIdOrKey)



Get all issue types with valid status values for a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | Project id or project key
    try {
      apiInstance.getAllStatuses(projectIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAllStatuses");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| Project id or project key | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAllSystemAvatars"></a>
# **getAllSystemAvatars**
> getAllSystemAvatars(type)



Returns all system avatars of the given type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String type = "type_example"; // String | the avatar type
    try {
      apiInstance.getAllSystemAvatars(type);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAllSystemAvatars");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **String**| the avatar type | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAllTabs"></a>
# **getAllTabs**
> getAllTabs(screenId, projectKey)



Returns a list of all tabs for the given screen

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long screenId = 56L; // Long | id of screen
    String projectKey = "projectKey_example"; // String | the key of the project; this parameter is optional
    try {
      apiInstance.getAllTabs(screenId, projectKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAllTabs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **screenId** | **Long**| id of screen | |
| **projectKey** | **String**| the key of the project; this parameter is optional | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAllWorkflows"></a>
# **getAllWorkflows**
> getAllWorkflows(workflowName)



Returns all workflows.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String workflowName = "workflowName_example"; // String | 
    try {
      apiInstance.getAllWorkflows(workflowName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAllWorkflows");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **workflowName** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAlternativeIssueTypes"></a>
# **getAlternativeIssueTypes**
> getAlternativeIssueTypes(id)



Returns a list of all alternative issue types for the given issue type id. The list will contain these issues types, to which  issues assigned to the given issue type can be migrated. The suitable alternatives are issue types which are assigned  to the same workflow, the same field configuration and the same screen scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.getAlternativeIssueTypes(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAlternativeIssueTypes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAssignedPermissionScheme"></a>
# **getAssignedPermissionScheme**
> getAssignedPermissionScheme(projectKeyOrId, expand)



Gets a permission scheme assigned with a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectKeyOrId = "projectKeyOrId_example"; // String | key or id of the project
    String expand = "expand_example"; // String | 
    try {
      apiInstance.getAssignedPermissionScheme(projectKeyOrId, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAssignedPermissionScheme");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectKeyOrId** | **String**| key or id of the project | |
| **expand** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAttachment"></a>
# **getAttachment**
> getAttachment(id)



Returns the meta-data for an attachment, including the URI of the actual attached file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | id of the attachment to remove
    try {
      apiInstance.getAttachment(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAttachment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of the attachment to remove | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAttachmentMeta"></a>
# **getAttachmentMeta**
> getAttachmentMeta()



Returns the meta information for an attachments, specifically if they are enabled and the maximum upload size  allowed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getAttachmentMeta();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAttachmentMeta");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAutoComplete"></a>
# **getAutoComplete**
> getAutoComplete()



Returns the auto complete data required for JQL searches.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getAutoComplete();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAutoComplete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAvailableMetrics"></a>
# **getAvailableMetrics**
> getAvailableMetrics()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getAvailableMetrics();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAvailableMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getAvatars"></a>
# **getAvatars**
> getAvatars(type, owningObjectId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String type = "type_example"; // String | 
    String owningObjectId = "owningObjectId_example"; // String | 
    try {
      apiInstance.getAvatars(type, owningObjectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAvatars");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **String**|  | |
| **owningObjectId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getById"></a>
# **getById**
> getById(id, returnDraftIfExists)



Returns the requested workflow scheme to the caller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the scheme.
    Boolean returnDraftIfExists = false; // Boolean | when true indicates that a scheme's draft, if it exists, should be queried instead of                             the scheme itself.
    try {
      apiInstance.getById(id, returnDraftIfExists);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the scheme. | |
| **returnDraftIfExists** | **Boolean**| when true indicates that a scheme&#39;s draft, if it exists, should be queried instead of                             the scheme itself. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getComment"></a>
# **getComment**
> getComment(issueIdOrKey, id, expand)



Returns a single comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | of the issue the comment belongs to
    String id = "id_example"; // String | the ID of the comment to request
    String expand = "expand_example"; // String | optional flags: renderedBody (provides body rendered in HTML)
    try {
      apiInstance.getComment(issueIdOrKey, id, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getComment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| of the issue the comment belongs to | |
| **id** | **String**| the ID of the comment to request | |
| **expand** | **String**| optional flags: renderedBody (provides body rendered in HTML) | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getComments"></a>
# **getComments**
> getComments(issueIdOrKey, startAt, maxResults, orderBy, expand)



Returns all comments for an issue.  &lt;p&gt;  Results can be ordered by the \&quot;created\&quot; field which means the date a comment was added.  &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | a string containing the issue id or key the comment will be added to
    Long startAt = 56L; // Long | the page offset, if not specified then defaults to 0
    Integer maxResults = 56; // Integer | how many results on the page should be included. Defaults to 50.
    String orderBy = "orderBy_example"; // String | ordering of the results.
    String expand = "expand_example"; // String | optional flags: renderedBody (provides body rendered in HTML)
    try {
      apiInstance.getComments(issueIdOrKey, startAt, maxResults, orderBy, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getComments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| a string containing the issue id or key the comment will be added to | |
| **startAt** | **Long**| the page offset, if not specified then defaults to 0 | [optional] |
| **maxResults** | **Integer**| how many results on the page should be included. Defaults to 50. | [optional] |
| **orderBy** | **String**| ordering of the results. | [optional] |
| **expand** | **String**| optional flags: renderedBody (provides body rendered in HTML) | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getComponent"></a>
# **getComponent**
> getComponent(id)



Returns a project component.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The component to delete.
    try {
      apiInstance.getComponent(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getComponent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The component to delete. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getComponentRelatedIssues"></a>
# **getComponentRelatedIssues**
> getComponentRelatedIssues(id)



Returns counts of issues related to this component.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | a String containing the component id
    try {
      apiInstance.getComponentRelatedIssues(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getComponentRelatedIssues");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| a String containing the component id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getConfiguration"></a>
# **getConfiguration**
> getConfiguration()



Returns the information if the optional features in JIRA are enabled or disabled. If the time tracking is enabled,  it also returns the detailed information about time tracking configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getConfiguration();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getConfiguration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getCreateIssueMeta"></a>
# **getCreateIssueMeta**
> getCreateIssueMeta(projectIds, projectKeys, issuetypeIds, issuetypeNames)



Returns the meta data for creating issues. This includes the available projects, issue types and fields,  including field types and whether or not those fields are required.  Projects will not be returned if the user does not have permission to create issues in that project.  &lt;p/&gt;  The fields in the createmeta correspond to the fields in the create screen for the project/issuetype.  Fields not in the screen will not be in the createmeta.  &lt;p/&gt;  Fields will only be returned if &lt;code&gt;expand&#x3D;projects.issuetypes.fields&lt;/code&gt;.  &lt;p/&gt;  The results can be filtered by project and/or issue type, given by the query params.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIds = "projectIds_example"; // String | combined with the projectKeys param, lists the projects with which to filter the results. If absent, all projects are returned.                        This parameter can be specified multiple times, and/or be a comma-separated list.                        Specifiying a project that does not exist (or that you cannot create issues in) is not an error, but it will not be in the results.
    String projectKeys = "projectKeys_example"; // String | combined with the projectIds param, lists the projects with which to filter the results. If null, all projects are returned.                        This parameter can be specified multiple times, and/or be a comma-separated list.                        Specifiying a project that does not exist (or that you cannot create issues in) is not an error, but it will not be in the results.
    String issuetypeIds = "issuetypeIds_example"; // String | combinded with issuetypeNames, lists the issue types with which to filter the results. If null, all issue types are returned.                        This parameter can be specified multiple times, and/or be a comma-separated list.                        Specifiying an issue type that does not exist is not an error.
    String issuetypeNames = "issuetypeNames_example"; // String | combinded with issuetypeIds, lists the issue types with which to filter the results. If null, all issue types are returned.                        This parameter can be specified multiple times, but is NOT interpreted as a comma-separated list.                        Specifiying an issue type that does not exist is not an error.
    try {
      apiInstance.getCreateIssueMeta(projectIds, projectKeys, issuetypeIds, issuetypeNames);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getCreateIssueMeta");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIds** | **String**| combined with the projectKeys param, lists the projects with which to filter the results. If absent, all projects are returned.                        This parameter can be specified multiple times, and/or be a comma-separated list.                        Specifiying a project that does not exist (or that you cannot create issues in) is not an error, but it will not be in the results. | [optional] |
| **projectKeys** | **String**| combined with the projectIds param, lists the projects with which to filter the results. If null, all projects are returned.                        This parameter can be specified multiple times, and/or be a comma-separated list.                        Specifiying a project that does not exist (or that you cannot create issues in) is not an error, but it will not be in the results. | [optional] |
| **issuetypeIds** | **String**| combinded with issuetypeNames, lists the issue types with which to filter the results. If null, all issue types are returned.                        This parameter can be specified multiple times, and/or be a comma-separated list.                        Specifiying an issue type that does not exist is not an error. | [optional] |
| **issuetypeNames** | **String**| combinded with issuetypeIds, lists the issue types with which to filter the results. If null, all issue types are returned.                        This parameter can be specified multiple times, but is NOT interpreted as a comma-separated list.                        Specifiying an issue type that does not exist is not an error. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getCustomFieldOption"></a>
# **getCustomFieldOption**
> getCustomFieldOption(id)



Returns a full representation of the Custom Field Option that has the given id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | a String containing an Custom Field Option id
    try {
      apiInstance.getCustomFieldOption(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getCustomFieldOption");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| a String containing an Custom Field Option id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getDashboard"></a>
# **getDashboard**
> getDashboard(id)



Returns a single dashboard.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the dashboard id
    try {
      apiInstance.getDashboard(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDashboard");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the dashboard id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getDefault"></a>
# **getDefault**
> getDefault(id, returnDraftIfExists)



Return the default workflow from the passed workflow scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the scheme.
    Boolean returnDraftIfExists = false; // Boolean | when true indicates that a scheme's draft, if it exists, should be queried instead of                             the scheme itself.
    try {
      apiInstance.getDefault(id, returnDraftIfExists);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDefault");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the scheme. | |
| **returnDraftIfExists** | **Boolean**| when true indicates that a scheme&#39;s draft, if it exists, should be queried instead of                             the scheme itself. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getDefaultShareScope"></a>
# **getDefaultShareScope**
> getDefaultShareScope()



Returns the default share scope of the logged-in user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getDefaultShareScope();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDefaultShareScope");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getDraftById"></a>
# **getDraftById**
> getDraftById(id)



Returns the requested draft workflow scheme to the caller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the parent scheme.
    try {
      apiInstance.getDraftById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDraftById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the parent scheme. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getDraftDefault"></a>
# **getDraftDefault**
> getDraftDefault(id)



Return the default workflow from the passed draft workflow scheme to the caller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the parent scheme.
    try {
      apiInstance.getDraftDefault(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDraftDefault");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the parent scheme. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getDraftIssueType"></a>
# **getDraftIssueType**
> getDraftIssueType(issueType, id)



Returns the issue type mapping for the passed draft workflow scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueType = "issueType_example"; // String | the issue type being set.
    Long id = 56L; // Long | the id of the parent scheme.
    try {
      apiInstance.getDraftIssueType(issueType, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDraftIssueType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueType** | **String**| the issue type being set. | |
| **id** | **Long**| the id of the parent scheme. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getDraftWorkflow"></a>
# **getDraftWorkflow**
> getDraftWorkflow(id, workflowName)



Returns the draft workflow mappings or requested mapping to the caller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the parent scheme.
    String workflowName = "workflowName_example"; // String | the workflow mapping to return. Null can be passed to return all mappings. Must be a valid workflow name.
    try {
      apiInstance.getDraftWorkflow(id, workflowName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDraftWorkflow");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the parent scheme. | |
| **workflowName** | **String**| the workflow mapping to return. Null can be passed to return all mappings. Must be a valid workflow name. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getEditIssueMeta"></a>
# **getEditIssueMeta**
> getEditIssueMeta(issueIdOrKey)



Returns the meta data for editing an issue.  &lt;p/&gt;  The fields in the editmeta correspond to the fields in the edit screen for the issue.  Fields not in the screen will not be in the editmeta.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue whose edit meta data you want to view
    try {
      apiInstance.getEditIssueMeta(issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getEditIssueMeta");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| the issue whose edit meta data you want to view | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getFavouriteFilters"></a>
# **getFavouriteFilters**
> getFavouriteFilters(expand, enableSharedUsers)



Returns the favourite filters of the logged-in user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String expand = "expand_example"; // String | the parameters to expand
    Boolean enableSharedUsers = true; // Boolean | enable calculating shared users collection
    try {
      apiInstance.getFavouriteFilters(expand, enableSharedUsers);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFavouriteFilters");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **expand** | **String**| the parameters to expand | [optional] |
| **enableSharedUsers** | **Boolean**| enable calculating shared users collection | [optional] [default to true] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getFieldAutoCompleteForQueryString"></a>
# **getFieldAutoCompleteForQueryString**
> getFieldAutoCompleteForQueryString(fieldName, fieldValue, predicateName, predicateValue)



Returns auto complete suggestions for JQL search.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String fieldName = "fieldName_example"; // String | the field name for which the suggestions are generated.
    String fieldValue = "fieldValue_example"; // String | the portion of the field value that has already been provided by the user.
    String predicateName = "predicateName_example"; // String | the predicate for which the suggestions are generated. Suggestions are generated only for: \"by\", \"from\" and \"to\".
    String predicateValue = "predicateValue_example"; // String | the portion of the predicate value that has already been provided by the user.
    try {
      apiInstance.getFieldAutoCompleteForQueryString(fieldName, fieldValue, predicateName, predicateValue);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFieldAutoCompleteForQueryString");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fieldName** | **String**| the field name for which the suggestions are generated. | [optional] |
| **fieldValue** | **String**| the portion of the field value that has already been provided by the user. | [optional] |
| **predicateName** | **String**| the predicate for which the suggestions are generated. Suggestions are generated only for: \&quot;by\&quot;, \&quot;from\&quot; and \&quot;to\&quot;. | [optional] |
| **predicateValue** | **String**| the portion of the predicate value that has already been provided by the user. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getFields"></a>
# **getFields**
> getFields()



Returns a list of all fields, both System and Custom

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getFields();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFields");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getFieldsToAdd"></a>
# **getFieldsToAdd**
> getFieldsToAdd(screenId)



Gets available fields for screen. i.e ones that haven&#39;t already been added.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long screenId = 56L; // Long | id of screen
    try {
      apiInstance.getFieldsToAdd(screenId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFieldsToAdd");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **screenId** | **Long**| id of screen | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getFilter"></a>
# **getFilter**
> getFilter(id, expand, enableSharedUsers)



Returns a filter given an id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the filter being looked up
    String expand = "expand_example"; // String | the parameters to expand
    Boolean enableSharedUsers = true; // Boolean | enable calculating shared users collection
    try {
      apiInstance.getFilter(id, expand, enableSharedUsers);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFilter");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the filter being looked up | |
| **expand** | **String**| the parameters to expand | [optional] |
| **enableSharedUsers** | **Boolean**| enable calculating shared users collection | [optional] [default to true] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getGroup"></a>
# **getGroup**
> getGroup(groupname, expand)



Returns REST representation for the requested group. Allows to get list of active users belonging to the  specified group and its subgroups if \&quot;users\&quot; expand option is provided. You can page through users list by using  indexes in expand param. For example to get users from index 10 to index 15 use \&quot;users[10:15]\&quot; expand value. This  will return 6 users (if there are at least 16 users in this group). Indexes are 0-based and inclusive.  &lt;p&gt;  This resource is deprecated, please use group/member API instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String groupname = "groupname_example"; // String | A name of requested group.
    String expand = "expand_example"; // String | List of fields to expand. Currently only available expand is \"users\".
    try {
      apiInstance.getGroup(groupname, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **groupname** | **String**| A name of requested group. | [optional] |
| **expand** | **String**| List of fields to expand. Currently only available expand is \&quot;users\&quot;. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getIdsOfWorklogsDeletedSince"></a>
# **getIdsOfWorklogsDeletedSince**
> getIdsOfWorklogsDeletedSince(since)



Returns worklogs id and delete time of worklogs that was deleted since given time.  The returns set of worklogs is limited to 1000 elements.  This API will not return worklogs deleted during last minute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long since = 0L; // Long | a date time in unix timestamp format since when deleted worklogs will be returned.
    try {
      apiInstance.getIdsOfWorklogsDeletedSince(since);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getIdsOfWorklogsDeletedSince");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **since** | **Long**| a date time in unix timestamp format since when deleted worklogs will be returned. | [optional] [default to 0] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getIdsOfWorklogsModifiedSince"></a>
# **getIdsOfWorklogsModifiedSince**
> getIdsOfWorklogsModifiedSince(since)



Returns worklogs id and update time of worklogs that was updated since given time.  The returns set of worklogs is limited to 1000 elements.  This API will not return worklogs updated during last minute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long since = 0L; // Long | a date time in unix timestamp format since when updated worklogs will be returned.
    try {
      apiInstance.getIdsOfWorklogsModifiedSince(since);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getIdsOfWorklogsModifiedSince");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **since** | **Long**| a date time in unix timestamp format since when updated worklogs will be returned. | [optional] [default to 0] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getIndexSummary"></a>
# **getIndexSummary**
> getIndexSummary()



Summarizes index condition of current node.  &lt;p/&gt;  Returned data consists of:  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;nodeId&lt;/code&gt; - Node identifier.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;reportTime&lt;/code&gt; - Time of this report creation.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;issueIndex&lt;/code&gt; - Summary of issue index status.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;replicationQueues&lt;/code&gt; - Map of index replication queues, where  keys represent nodes from which replication operations came from.&lt;/li&gt;  &lt;/ul&gt;  &lt;p/&gt;  &lt;code&gt;issueIndex&lt;/code&gt; can contain:  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;indexReadable&lt;/code&gt; - If &lt;code&gt;false&lt;/code&gt; the end point failed to read data from issue index  (check JIRA logs for detailed stack trace), otherwise &lt;code&gt;true&lt;/code&gt;.  When &lt;code&gt;false&lt;/code&gt; other fields of &lt;code&gt;issueIndex&lt;/code&gt; can be not visible.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;countInDatabase&lt;/code&gt; - Count of issues found in database.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;countInIndex&lt;/code&gt; - Count of issues found while querying index.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastUpdatedInDatabase&lt;/code&gt; - Time of last update of issue found in database.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastUpdatedInIndex&lt;/code&gt; - Time of last update of issue found while querying index.&lt;/li&gt;  &lt;/ul&gt;  &lt;p/&gt;  &lt;code&gt;replicationQueues&lt;/code&gt;&#39;s map values can contain:  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;lastConsumedOperation&lt;/code&gt; - Last executed index replication operation by current node from sending node&#39;s queue.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastConsumedOperation.id&lt;/code&gt; - Identifier of the operation.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastConsumedOperation.replicationTime&lt;/code&gt; - Time when the operation was sent to other nodes.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastOperationInQueue&lt;/code&gt; - Last index replication operation in sending node&#39;s queue.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastOperationInQueue.id&lt;/code&gt; - Identifier of the operation.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastOperationInQueue.replicationTime&lt;/code&gt; - Time when the operation was sent to other nodes.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;queueSize&lt;/code&gt; - Number of operations in queue from sending node to current node.&lt;/li&gt;  &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getIndexSummary();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getIndexSummary");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getIssue"></a>
# **getIssue**
> getIssue(issueIdOrKey, fields, expand, properties)



Returns a full representation of the issue for the given issue key.  &lt;p&gt;  An issue JSON consists of the issue key, a collection of fields,  a link to the workflow transition sub-resource, and (optionally) the HTML rendered values of any fields that support it  (e.g. if wiki syntax is enabled for the description or comments).  &lt;p&gt;  The &lt;code&gt;fields&lt;/code&gt; param (which can be specified multiple times) gives a comma-separated list of fields  to include in the response. This can be used to retrieve a subset of fields.  A particular field can be excluded by prefixing it with a minus.  &lt;p&gt;  By default, all (&lt;code&gt;*all&lt;/code&gt;) fields are returned in this get-issue resource. Note: the default is different  when doing a jql search -- the default there is just navigable fields (&lt;code&gt;*navigable&lt;/code&gt;).  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;*all&lt;/code&gt; - include all fields&lt;/li&gt;  &lt;li&gt;&lt;code&gt;*navigable&lt;/code&gt; - include just navigable fields&lt;/li&gt;  &lt;li&gt;&lt;code&gt;summary,comment&lt;/code&gt; - include just the summary and comments&lt;/li&gt;  &lt;li&gt;&lt;code&gt;-comment&lt;/code&gt; - include everything except comments (the default is &lt;code&gt;*all&lt;/code&gt; for get-issue)&lt;/li&gt;  &lt;li&gt;&lt;code&gt;*all,-comment&lt;/code&gt; - include everything except comments&lt;/li&gt;  &lt;/ul&gt;  &lt;p&gt;  The {@code properties} param is similar to {@code fields} and specifies a comma-separated list of issue  properties to include. Unlike {@code fields}, properties are not included by default. To include them all  send {@code ?properties&#x3D;*all}. You can also include only specified properties or exclude some properties  with a minus (-) sign.  &lt;p&gt;  &lt;ul&gt;  &lt;li&gt;{@code *all} - include all properties&lt;/li&gt;  &lt;li&gt;{@code *all, -prop1} - include all properties except {@code prop1} &lt;/li&gt;  &lt;li&gt;{@code prop1, prop1} - include {@code prop1} and {@code prop2} properties &lt;/li&gt;  &lt;/ul&gt;  &lt;/p&gt;  &lt;p/&gt;  JIRA will attempt to identify the issue by the &lt;code&gt;issueIdOrKey&lt;/code&gt; path parameter. This can be an issue id,  or an issue key. If the issue cannot be found via an exact match, JIRA will also look for the issue in a case-insensitive way, or  by looking to see if the issue was moved. In either of these cases, the request will proceed as normal (a 302 or other redirect  will &lt;b&gt;not&lt;/b&gt; be returned). The issue key contained in the response will indicate the current value of issue&#39;s key.  &lt;p/&gt;  The &lt;code&gt;expand&lt;/code&gt; param is used to include, hidden by default, parts of response. This can be used to include:  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;renderedFields&lt;/code&gt; - field values in HTML format&lt;/li&gt;  &lt;li&gt;&lt;code&gt;names&lt;/code&gt; - display name of each field&lt;/li&gt;  &lt;li&gt;&lt;code&gt;schema&lt;/code&gt; - schema for each field which describes a type of the field&lt;/li&gt;  &lt;li&gt;&lt;code&gt;transitions&lt;/code&gt; - all possible transitions for the given issue&lt;/li&gt;  &lt;li&gt;&lt;code&gt;operations&lt;/code&gt; - all possibles operations which may be applied on issue&lt;/li&gt;  &lt;li&gt;&lt;code&gt;editmeta&lt;/code&gt; - information about how each field may be edited. It contains field&#39;s schema as well.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;changelog&lt;/code&gt; - history of all changes of the given issue&lt;/li&gt;  &lt;li&gt;&lt;code&gt;versionedRepresentations&lt;/code&gt; -  REST representations of all fields. Some field may contain more recent versions. RESET representations are numbered.  The greatest number always represents the most recent version. It is recommended that the most recent version is used.  version for these fields which provide a more recent REST representation.  After including &lt;code&gt;versionedRepresentations&lt;/code&gt; \&quot;fields\&quot; field become hidden.&lt;/li&gt;  &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue id or key to update (i.e. JRA-1330)
    String fields = "fields_example"; // String | the list of fields to return for the issue. By default, all fields are returned.
    String expand = "expand_example"; // String | 
    String properties = "properties_example"; // String | the list of properties to return for the issue. By default no properties are returned.
    try {
      apiInstance.getIssue(issueIdOrKey, fields, expand, properties);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getIssue");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| the issue id or key to update (i.e. JRA-1330) | |
| **fields** | **String**| the list of fields to return for the issue. By default, all fields are returned. | [optional] |
| **expand** | **String**|  | [optional] |
| **properties** | **String**| the list of properties to return for the issue. By default no properties are returned. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getIssueAllTypes"></a>
# **getIssueAllTypes**
> getIssueAllTypes()



Returns a list of all issue types visible to the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getIssueAllTypes();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getIssueAllTypes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getIssueLink"></a>
# **getIssueLink**
> getIssueLink(linkId)



Returns an issue link with the specified id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String linkId = "linkId_example"; // String | the issue link id.
    try {
      apiInstance.getIssueLink(linkId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getIssueLink");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **linkId** | **String**| the issue link id. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getIssueLinkType"></a>
# **getIssueLinkType**
> getIssueLinkType(issueLinkTypeId)



Returns for a given issue link type id all information about this issue link type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueLinkTypeId = "issueLinkTypeId_example"; // String | 
    try {
      apiInstance.getIssueLinkType(issueLinkTypeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getIssueLinkType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueLinkTypeId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getIssueLinkTypes"></a>
# **getIssueLinkTypes**
> getIssueLinkTypes()



Returns a list of available issue link types, if issue linking is enabled.  Each issue link type has an id, a name and a label for the outward and inward link relationship.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getIssueLinkTypes();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getIssueLinkTypes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getIssueNavigatorDefaultColumns"></a>
# **getIssueNavigatorDefaultColumns**
> getIssueNavigatorDefaultColumns()



Returns the default system columns for issue navigator. Admin permission will be required.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getIssueNavigatorDefaultColumns();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getIssueNavigatorDefaultColumns");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getIssuePickerResource"></a>
# **getIssuePickerResource**
> getIssuePickerResource(query, currentJQL, currentIssueKey, currentProjectId, showSubTasks, showSubTaskParent)



Returns suggested issues which match the auto-completion query for the user which executes this request. This REST  method will check the user&#39;s history and the user&#39;s browsing context and select this issues, which match the query.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String query = "query_example"; // String | the query.
    String currentJQL = "currentJQL_example"; // String | the JQL in context of which the request is executed. Only issues which match this JQL query will be included in results.
    String currentIssueKey = "currentIssueKey_example"; // String | the key of the issue in context of which the request is executed. The issue which is in context will not be included in the auto-completion result, even if it matches the query.
    String currentProjectId = "currentProjectId_example"; // String | the id of the project in context of which the request is executed. Suggested issues will be only from this project.
    Boolean showSubTasks = true; // Boolean | if set to false, subtasks will not be included in the list.
    Boolean showSubTaskParent = true; // Boolean | if set to false and request is executed in context of a subtask, the parent issue will not be included in the auto-completion result, even if it matches the query.
    try {
      apiInstance.getIssuePickerResource(query, currentJQL, currentIssueKey, currentProjectId, showSubTasks, showSubTaskParent);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getIssuePickerResource");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **query** | **String**| the query. | [optional] |
| **currentJQL** | **String**| the JQL in context of which the request is executed. Only issues which match this JQL query will be included in results. | [optional] |
| **currentIssueKey** | **String**| the key of the issue in context of which the request is executed. The issue which is in context will not be included in the auto-completion result, even if it matches the query. | [optional] |
| **currentProjectId** | **String**| the id of the project in context of which the request is executed. Suggested issues will be only from this project. | [optional] |
| **showSubTasks** | **Boolean**| if set to false, subtasks will not be included in the list. | [optional] |
| **showSubTaskParent** | **Boolean**| if set to false and request is executed in context of a subtask, the parent issue will not be included in the auto-completion result, even if it matches the query. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getIssueSecuritySchemes"></a>
# **getIssueSecuritySchemes**
> getIssueSecuritySchemes()



Returns all issue security schemes that are defined.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getIssueSecuritySchemes();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getIssueSecuritySchemes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getIssueWatchers"></a>
# **getIssueWatchers**
> getIssueWatchers(issueIdOrKey)



Returns the list of watchers for the issue with the given key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | a String containing an issue key.
    try {
      apiInstance.getIssueWatchers(issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getIssueWatchers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| a String containing an issue key. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getIssueWorklog"></a>
# **getIssueWorklog**
> getIssueWorklog(issueIdOrKey)



Returns all work logs for an issue. &lt;br/&gt;  &lt;strong&gt;Note:&lt;/strong&gt; Work logs won&#39;t be returned if the Log work field is hidden for the project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | a string containing the issue id or key the worklog will be added to
    try {
      apiInstance.getIssueWorklog(issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getIssueWorklog");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| a string containing the issue id or key the worklog will be added to | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getIssuesecuritylevel"></a>
# **getIssuesecuritylevel**
> getIssuesecuritylevel(id)



Returns a full representation of the security level that has the given id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | a String containing an issue security level id
    try {
      apiInstance.getIssuesecuritylevel(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getIssuesecuritylevel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| a String containing an issue security level id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getNotificationSchemes"></a>
# **getNotificationSchemes**
> getNotificationSchemes(startAt, maxResults, expand)



Returns a &lt;a href&#x3D;\&quot;#pagination\&quot;&gt;paginated&lt;/a&gt; list of notification schemes. In order to access notification scheme, the calling user is  required to have permissions to administer at least one project associated with the requested notification scheme. Each scheme contains  a list of events and recipient configured to receive notifications for these events. Consumer should allow events without recipients to appear in response.  The list is ordered by the scheme&#39;s name.  Follow the documentation of /notificationscheme/{id} resource for all details about returned value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long startAt = 56L; // Long | the index of the first notification scheme to return (0 based).
    Integer maxResults = 56; // Integer | the maximum number of notification schemes to return (max 50).
    String expand = "expand_example"; // String | 
    try {
      apiInstance.getNotificationSchemes(startAt, maxResults, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getNotificationSchemes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **startAt** | **Long**| the index of the first notification scheme to return (0 based). | [optional] |
| **maxResults** | **Integer**| the maximum number of notification schemes to return (max 50). | [optional] |
| **expand** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getPasswordPolicy"></a>
# **getPasswordPolicy**
> getPasswordPolicy(hasOldPassword)



Returns the list of requirements for the current password policy. For example, \&quot;The password must have at least 10 characters.\&quot;,  \&quot;The password must not be similar to the user&#39;s name or email address.\&quot;, etc.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Boolean hasOldPassword = false; // Boolean | whether or not the user will be required to enter their current password.  Use                        {@code false} (the default) if this is a new user or if an administrator is forcibly changing                        another user's password.
    try {
      apiInstance.getPasswordPolicy(hasOldPassword);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPasswordPolicy");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **hasOldPassword** | **Boolean**| whether or not the user will be required to enter their current password.  Use                        {@code false} (the default) if this is a new user or if an administrator is forcibly changing                        another user&#39;s password. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getPermissionScheme"></a>
# **getPermissionScheme**
> getPermissionScheme(schemeId, expand)



Returns a permission scheme identified by the given id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long schemeId = 56L; // Long | 
    String expand = "expand_example"; // String | 
    try {
      apiInstance.getPermissionScheme(schemeId, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPermissionScheme");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **schemeId** | **Long**|  | |
| **expand** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getPermissionSchemeGrant"></a>
# **getPermissionSchemeGrant**
> getPermissionSchemeGrant(permissionId, schemeId, expand)



Returns a permission grant identified by the given id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long permissionId = 56L; // Long | 
    Long schemeId = 56L; // Long | 
    String expand = "expand_example"; // String | 
    try {
      apiInstance.getPermissionSchemeGrant(permissionId, schemeId, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPermissionSchemeGrant");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **permissionId** | **Long**|  | |
| **schemeId** | **Long**|  | |
| **expand** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getPermissionSchemeGrants"></a>
# **getPermissionSchemeGrants**
> getPermissionSchemeGrants(schemeId, expand)



Returns all permission grants of the given permission scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long schemeId = 56L; // Long | 
    String expand = "expand_example"; // String | 
    try {
      apiInstance.getPermissionSchemeGrants(schemeId, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPermissionSchemeGrants");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **schemeId** | **Long**|  | |
| **expand** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getPermissionSchemes"></a>
# **getPermissionSchemes**
> getPermissionSchemes(expand)



Returns a list of all permission schemes.  &lt;p&gt;  By default only shortened beans are returned. If you want to include permissions of all the schemes,  then specify the &lt;b&gt;permissions&lt;/b&gt; expand parameter. Permissions will be included also if you specify  any other expand parameter.  &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String expand = "expand_example"; // String | 
    try {
      apiInstance.getPermissionSchemes(expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPermissionSchemes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **expand** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getPermissions"></a>
# **getPermissions**
> getPermissions(projectKey, projectId, issueKey, issueId)



Returns all permissions in the system and whether the currently logged in user has them. You can optionally provide a specific context to get permissions for  (projectKey OR projectId OR issueKey OR issueId)  &lt;ul&gt;  &lt;li&gt; When no context supplied the project related permissions will return true if the user has that permission in ANY project &lt;/li&gt;  &lt;li&gt; If a project context is provided, project related permissions will return true if the user has the permissions in the specified project.  For permissions that are determined using issue data (e.g Current Assignee), true will be returned if the user meets the permission criteria in ANY issue in that project &lt;/li&gt;  &lt;li&gt; If an issue context is provided, it will return whether or not the user has each permission in that specific issue&lt;/li&gt;  &lt;/ul&gt;  &lt;p&gt;  NB: The above means that for issue-level permissions (EDIT_ISSUE for example), hasPermission may be true when no context is provided, or when a project context is provided,  &lt;b&gt;but&lt;/b&gt; may be false for any given (or all) issues. This would occur (for example) if Reporters were given the EDIT_ISSUE permission. This is because  any user could be a reporter, except in the context of a concrete issue, where the reporter is known.  &lt;/p&gt;  &lt;p&gt;  Global permissions will still be returned for all scopes.  &lt;/p&gt;  &lt;p&gt;  Prior to version 6.4 this service returned project permissions with keys corresponding to com.atlassian.jira.security.Permissions.Permission constants.  Since 6.4 those keys are considered deprecated and this service returns system project permission keys corresponding to constants defined in com.atlassian.jira.permission.ProjectPermissions.  Permissions with legacy keys are still also returned for backwards compatibility, they are marked with an attribute deprecatedKey&#x3D;true.  The attribute is missing for project permissions with the current keys.  &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectKey = "projectKey_example"; // String | - key of project to scope returned permissions for.
    String projectId = "projectId_example"; // String | - id of project to scope returned permissions for.
    String issueKey = "issueKey_example"; // String | - key of the issue to scope returned permissions for.
    String issueId = "issueId_example"; // String | - id of the issue to scope returned permissions for.
    try {
      apiInstance.getPermissions(projectKey, projectId, issueKey, issueId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPermissions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectKey** | **String**| - key of project to scope returned permissions for. | [optional] |
| **projectId** | **String**| - id of project to scope returned permissions for. | [optional] |
| **issueKey** | **String**| - key of the issue to scope returned permissions for. | [optional] |
| **issueId** | **String**| - id of the issue to scope returned permissions for. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getPreference"></a>
# **getPreference**
> getPreference(key)



Returns preference of the currently logged in user. Preference key must be provided as input parameter (key). The  value is returned exactly as it is. If key parameter is not provided or wrong - status code 404. If value is  found  - status code 200.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | - key of the preference to be returned.
    try {
      apiInstance.getPreference(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPreference");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **key** | **String**| - key of the preference to be returned. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getPriorities"></a>
# **getPriorities**
> getPriorities()



Returns a list of all issue priorities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getPriorities();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPriorities");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getPriority"></a>
# **getPriority**
> getPriority(id)



Returns an issue priority.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | a String containing the priority id
    try {
      apiInstance.getPriority(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPriority");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| a String containing the priority id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getProgress"></a>
# **getProgress**
> getProgress(requestId)



Retrieves the progress of a single reindex request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long requestId = 56L; // Long | the reindex request ID.
    try {
      apiInstance.getProgress(requestId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getProgress");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **requestId** | **Long**| the reindex request ID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getProgressBulk"></a>
# **getProgressBulk**
> getProgressBulk(requestId)



Retrieves the progress of a multiple reindex requests.  Only reindex requests that actually exist will be returned  in the results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String requestId = "requestId_example"; // String | the reindex request IDs.
    try {
      apiInstance.getProgressBulk(requestId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getProgressBulk");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **requestId** | **String**| the reindex request IDs. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getProjectCategoryById"></a>
# **getProjectCategoryById**
> getProjectCategoryById(id)



Contains a representation of a project category in JSON format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      apiInstance.getProjectCategoryById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getProjectCategoryById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getProjectComponents"></a>
# **getProjectComponents**
> getProjectComponents(projectIdOrKey)



Contains a full representation of a the specified project&#39;s components.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
    try {
      apiInstance.getProjectComponents(projectIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getProjectComponents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| the project id or project key | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getProjectRole"></a>
# **getProjectRole**
> getProjectRole(projectIdOrKey, id)



Returns the details for a given project role in a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
    Long id = 56L; // Long | the project role id
    try {
      apiInstance.getProjectRole(projectIdOrKey, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getProjectRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| the project id or project key | |
| **id** | **Long**| the project role id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getProjectRoleActorsForRole"></a>
# **getProjectRoleActorsForRole**
> getProjectRoleActorsForRole(id)



Gets default actors for the given role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the role id to remove the actors from
    try {
      apiInstance.getProjectRoleActorsForRole(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getProjectRoleActorsForRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the role id to remove the actors from | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getProjectRolesById"></a>
# **getProjectRolesById**
> getProjectRolesById(id)



Get a specific ProjectRole available in JIRA.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      apiInstance.getProjectRolesById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getProjectRolesById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getProjectTypeByKey"></a>
# **getProjectTypeByKey**
> getProjectTypeByKey(projectTypeKey)



Returns the project type with the given key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectTypeKey = "projectTypeKey_example"; // String | 
    try {
      apiInstance.getProjectTypeByKey(projectTypeKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getProjectTypeByKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectTypeKey** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getProjectVersions"></a>
# **getProjectVersions**
> getProjectVersions(projectIdOrKey, expand)



Contains a full representation of a the specified project&#39;s versions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
    String expand = "expand_example"; // String | the parameters to expand
    try {
      apiInstance.getProjectVersions(projectIdOrKey, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getProjectVersions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| the project id or project key | |
| **expand** | **String**| the parameters to expand | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getProjectVersionsPaginated"></a>
# **getProjectVersionsPaginated**
> getProjectVersionsPaginated(projectIdOrKey, startAt, maxResults, orderBy, expand)



Returns all versions for the specified project. Results are &lt;a href&#x3D;\&quot;#pagination\&quot;&gt;paginated&lt;/a&gt;.  &lt;p&gt;  Results can be ordered by the following fields:  &lt;ul&gt;  &lt;li&gt;sequence&lt;/li&gt;  &lt;li&gt;name&lt;/li&gt;  &lt;li&gt;startDate&lt;/li&gt;  &lt;li&gt;releaseDate&lt;/li&gt;  &lt;/ul&gt;  &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
    Long startAt = 56L; // Long | the page offset, if not specified then defaults to 0
    Integer maxResults = 56; // Integer | how many results on the page should be included. Defaults to 50.
    String orderBy = "orderBy_example"; // String | ordering of the results.
    String expand = "expand_example"; // String | the parameters to expand
    try {
      apiInstance.getProjectVersionsPaginated(projectIdOrKey, startAt, maxResults, orderBy, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getProjectVersionsPaginated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| the project id or project key | |
| **startAt** | **Long**| the page offset, if not specified then defaults to 0 | [optional] |
| **maxResults** | **Integer**| how many results on the page should be included. Defaults to 50. | [optional] |
| **orderBy** | **String**| ordering of the results. | [optional] |
| **expand** | **String**| the parameters to expand | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getProperties"></a>
# **getProperties**
> getProperties(id, includeReservedKeys, key, workflowName, workflowMode)



Return the property or properties associated with a transition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the ID of the transition within the workflow.
    Boolean includeReservedKeys = true; // Boolean | some keys under the \"jira.\" prefix are editable, some are not. Set this to true                             in order to include the non-editable keys in the response.
    String key = "key_example"; // String | the name of the property key to query. Can be left off the query to return all properties.
    String workflowName = "workflowName_example"; // String | the name of the workflow to use.
    String workflowMode = "workflowMode_example"; // String | the type of workflow to use. Can either be \"live\" or \"draft\".
    try {
      apiInstance.getProperties(id, includeReservedKeys, key, workflowName, workflowMode);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getProperties");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the ID of the transition within the workflow. | |
| **includeReservedKeys** | **Boolean**| some keys under the \&quot;jira.\&quot; prefix are editable, some are not. Set this to true                             in order to include the non-editable keys in the response. | [optional] |
| **key** | **String**| the name of the property key to query. Can be left off the query to return all properties. | [optional] |
| **workflowName** | **String**| the name of the workflow to use. | [optional] |
| **workflowMode** | **String**| the type of workflow to use. Can either be \&quot;live\&quot; or \&quot;draft\&quot;. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getPropertyKeys"></a>
# **getPropertyKeys**
> getPropertyKeys(issueTypeId)



Returns the keys of all properties for the issue type identified by the id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueTypeId = "issueTypeId_example"; // String | the issue type from which the keys will be returned
    try {
      apiInstance.getPropertyKeys(issueTypeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPropertyKeys");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueTypeId** | **String**| the issue type from which the keys will be returned | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRecords"></a>
# **getRecords**
> getRecords(offset, limit, filter, from, to, projectIds, userIds)



Returns auditing records filtered using provided parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer offset = 56; // Integer | - the number of record from which search starts
    Integer limit = 56; // Integer | - maximum number of returned results (if is limit is <= 0 or > 1000, it will be set do default value: 1000)
    String filter = "filter_example"; // String | - text query; each record that will be returned must contain the provided text in one of its fields
    String from = "from_example"; // String | - timestamp in past; 'from' must be less or equal 'to', otherwise the result set will be empty                only records that where created in the same moment or after the 'from' timestamp will be provided in response
    String to = "to_example"; // String | - timestamp in past; 'from' must be less or equal 'to', otherwise the result set will be empty                only records that where created in the same moment or earlier than the 'to' timestamp will be provided in response
    String projectIds = "projectIds_example"; // String | - list of project ids to look for
    String userIds = "userIds_example"; // String | - list of user ids to look for
    try {
      apiInstance.getRecords(offset, limit, filter, from, to, projectIds, userIds);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRecords");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **offset** | **Integer**| - the number of record from which search starts | [optional] |
| **limit** | **Integer**| - maximum number of returned results (if is limit is &lt;&#x3D; 0 or &gt; 1000, it will be set do default value: 1000) | [optional] |
| **filter** | **String**| - text query; each record that will be returned must contain the provided text in one of its fields | [optional] |
| **from** | **String**| - timestamp in past; &#39;from&#39; must be less or equal &#39;to&#39;, otherwise the result set will be empty                only records that where created in the same moment or after the &#39;from&#39; timestamp will be provided in response | [optional] |
| **to** | **String**| - timestamp in past; &#39;from&#39; must be less or equal &#39;to&#39;, otherwise the result set will be empty                only records that where created in the same moment or earlier than the &#39;to&#39; timestamp will be provided in response | [optional] |
| **projectIds** | **String**| - list of project ids to look for | [optional] |
| **userIds** | **String**| - list of user ids to look for | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getReindexInfo"></a>
# **getReindexInfo**
> getReindexInfo(taskId)



Returns information on the system reindexes.  If a reindex is currently taking place then information about this reindex is returned.  If there is no active index task, then returns information about the latest reindex task run, otherwise returns a 404  indicating that no reindex has taken place.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long taskId = 56L; // Long | the id of an indexing task you wish to obtain details on.  If omitted, then defaults to the standard behaviour and                returns information on the active reindex task, or the last task to run if no reindex is taking place. .  If there is no                reindexing task with that id then a 404 is returned.
    try {
      apiInstance.getReindexInfo(taskId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReindexInfo");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **taskId** | **Long**| the id of an indexing task you wish to obtain details on.  If omitted, then defaults to the standard behaviour and                returns information on the active reindex task, or the last task to run if no reindex is taking place. .  If there is no                reindexing task with that id then a 404 is returned. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getReindexProgress"></a>
# **getReindexProgress**
> getReindexProgress(taskId)



Returns information on the system reindexes.  If a reindex is currently taking place then information about this reindex is returned.  If there is no active index task, then returns information about the latest reindex task run, otherwise returns a 404  indicating that no reindex has taken place.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long taskId = 56L; // Long | the id of an indexing task you wish to obtain details on.  If omitted, then defaults to the standard behaviour and                returns information on the active reindex task, or the last task to run if no reindex is taking place. .  If there is no                reindexing task with that id then a 404 is returned.
    try {
      apiInstance.getReindexProgress(taskId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReindexProgress");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **taskId** | **Long**| the id of an indexing task you wish to obtain details on.  If omitted, then defaults to the standard behaviour and                returns information on the active reindex task, or the last task to run if no reindex is taking place. .  If there is no                reindexing task with that id then a 404 is returned. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRemoteIssueLinkById"></a>
# **getRemoteIssueLinkById**
> getRemoteIssueLinkById(linkId, issueIdOrKey)



Get the remote issue link with the given id on the issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String linkId = "linkId_example"; // String | the id of the remote issue link
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue to create the remote issue link for
    try {
      apiInstance.getRemoteIssueLinkById(linkId, issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRemoteIssueLinkById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **linkId** | **String**| the id of the remote issue link | |
| **issueIdOrKey** | **String**| the issue to create the remote issue link for | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRemoteIssueLinks"></a>
# **getRemoteIssueLinks**
> getRemoteIssueLinks(issueIdOrKey, globalId)



A REST sub-resource representing the remote issue links on the issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue to create the remote issue link for
    String globalId = "globalId_example"; // String | The id of the remote issue link to be returned.  If null (not provided) all remote links for the                      issue are returned.                      <p>For a fullexplanation of Issue Link fields please refer to                      <a href=\"https://developer.atlassian.com/display/JIRADEV/Fields+in+Remote+Issue+Links\">https://developer.atlassian.com/display/JIRADEV/Fields+in+Remote+Issue+Links</a></p>
    try {
      apiInstance.getRemoteIssueLinks(issueIdOrKey, globalId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRemoteIssueLinks");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| the issue to create the remote issue link for | |
| **globalId** | **String**| The id of the remote issue link to be returned.  If null (not provided) all remote links for the                      issue are returned.                      &lt;p&gt;For a fullexplanation of Issue Link fields please refer to                      &lt;a href&#x3D;\&quot;https://developer.atlassian.com/display/JIRADEV/Fields+in+Remote+Issue+Links\&quot;&gt;https://developer.atlassian.com/display/JIRADEV/Fields+in+Remote+Issue+Links&lt;/a&gt;&lt;/p&gt; | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRemoteVersionLink"></a>
# **getRemoteVersionLink**
> getRemoteVersionLink(versionId, globalId)



A REST sub-resource representing a remote version link

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String versionId = "versionId_example"; // String | The version ID of the remote link
    String globalId = "globalId_example"; // String | The global ID of the remote link
    try {
      apiInstance.getRemoteVersionLink(versionId, globalId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRemoteVersionLink");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **versionId** | **String**| The version ID of the remote link | |
| **globalId** | **String**| The global ID of the remote link | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRemoteVersionLinks"></a>
# **getRemoteVersionLinks**
> getRemoteVersionLinks(globalId)



Returns the remote version links for a given global ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String globalId = "globalId_example"; // String | the global ID of the remote resource that is linked to the versions
    try {
      apiInstance.getRemoteVersionLinks(globalId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRemoteVersionLinks");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **globalId** | **String**| the global ID of the remote resource that is linked to the versions | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRemoteVersionLinksByVersionId"></a>
# **getRemoteVersionLinksByVersionId**
> getRemoteVersionLinksByVersionId(versionId)



Returns the remote version links associated with the given version ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String versionId = "versionId_example"; // String | The version for which to delete ALL existing remote version links
    try {
      apiInstance.getRemoteVersionLinksByVersionId(versionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRemoteVersionLinksByVersionId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **versionId** | **String**| The version for which to delete ALL existing remote version links | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getResolution"></a>
# **getResolution**
> getResolution(id)



Returns a resolution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | a String containing the resolution id
    try {
      apiInstance.getResolution(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getResolution");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| a String containing the resolution id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getResolutions"></a>
# **getResolutions**
> getResolutions()



Returns a list of all resolutions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getResolutions();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getResolutions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getSchemeAttribute"></a>
# **getSchemeAttribute**
> getSchemeAttribute(permissionSchemeId, attributeKey)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long permissionSchemeId = 56L; // Long | permission scheme id
    String attributeKey = "attributeKey_example"; // String | permission scheme attribute key
    try {
      apiInstance.getSchemeAttribute(permissionSchemeId, attributeKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSchemeAttribute");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **permissionSchemeId** | **Long**| permission scheme id | |
| **attributeKey** | **String**| permission scheme attribute key | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getSecurityLevelsForProject"></a>
# **getSecurityLevelsForProject**
> getSecurityLevelsForProject(projectKeyOrId)



Returns all security levels for the project that the current logged in user has access to.  If the user does not have the Set Issue Security permission, the list will be empty.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectKeyOrId = "projectKeyOrId_example"; // String | - key or id of project to list the security levels for
    try {
      apiInstance.getSecurityLevelsForProject(projectKeyOrId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSecurityLevelsForProject");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectKeyOrId** | **String**| - key or id of project to list the security levels for | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getServerInfo"></a>
# **getServerInfo**
> getServerInfo(doHealthCheck)



Returns general information about the current JIRA server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Boolean doHealthCheck = true; // Boolean | 
    try {
      apiInstance.getServerInfo(doHealthCheck);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getServerInfo");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **doHealthCheck** | **Boolean**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getSharePermission"></a>
# **getSharePermission**
> getSharePermission(permissionId, id)



Returns a single share permission of the given filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long permissionId = 56L; // Long | 
    Long id = 56L; // Long | 
    try {
      apiInstance.getSharePermission(permissionId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSharePermission");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **permissionId** | **Long**|  | |
| **id** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getSharePermissions"></a>
# **getSharePermissions**
> getSharePermissions(id)



Returns all share permissions of the given filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      apiInstance.getSharePermissions(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSharePermissions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getState"></a>
# **getState**
> getState()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getState();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getState");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getStatus"></a>
# **getStatus**
> getStatus(idOrName)



Returns a full representation of the Status having the given id or name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String idOrName = "idOrName_example"; // String | a numeric Status id or a status name
    try {
      apiInstance.getStatus(idOrName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getStatus");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **idOrName** | **String**| a numeric Status id or a status name | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getStatusCategories"></a>
# **getStatusCategories**
> getStatusCategories()



Returns a list of all status categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getStatusCategories();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getStatusCategories");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getStatusCategory"></a>
# **getStatusCategory**
> getStatusCategory(idOrKey)



Returns a full representation of the StatusCategory having the given id or key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String idOrKey = "idOrKey_example"; // String | a numeric StatusCategory id or a status category key
    try {
      apiInstance.getStatusCategory(idOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getStatusCategory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **idOrKey** | **String**| a numeric StatusCategory id or a status category key | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getStatuses"></a>
# **getStatuses**
> getStatuses()



Returns a list of all statuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getStatuses();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getStatuses");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getSubTasks"></a>
# **getSubTasks**
> getSubTasks(issueIdOrKey)



Returns an issue&#39;s subtask list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | The parent issue's key or id
    try {
      apiInstance.getSubTasks(issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSubTasks");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| The parent issue&#39;s key or id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getTransitions"></a>
# **getTransitions**
> getTransitions(issueIdOrKey, transitionId)



Get a list of the transitions possible for this issue by the current user, along with fields that are required and their types.  &lt;p/&gt;  Fields will only be returned if &lt;code&gt;expand&#x3D;transitions.fields&lt;/code&gt;.  &lt;p/&gt;  The fields in the metadata correspond to the fields in the transition screen for that transition.  Fields not in the screen will not be in the metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue whose transitions you want to view
    String transitionId = "transitionId_example"; // String | 
    try {
      apiInstance.getTransitions(issueIdOrKey, transitionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getTransitions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| the issue whose transitions you want to view | |
| **transitionId** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getUpgradeResult"></a>
# **getUpgradeResult**
> getUpgradeResult()



Returns the result of the last upgrade task.   Returns {@link javax.ws.rs.core.Response#seeOther(java.net.URI)} if still running.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getUpgradeResult();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getUpgradeResult");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getUsersFromGroup"></a>
# **getUsersFromGroup**
> getUsersFromGroup(groupname, includeInactiveUsers, startAt, maxResults)



This resource returns a &lt;a href&#x3D;\&quot;#pagination\&quot;&gt;paginated&lt;/a&gt; list of users who are members of the specified group and its subgroups.  Users in the page are ordered by user names. User of this resource is required to have sysadmin or admin permissions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String groupname = "groupname_example"; // String | a name of the group for which members will be returned.
    Boolean includeInactiveUsers = false; // Boolean | inactive users will be included in the response if set to true.
    Long startAt = 0L; // Long | the index of the first user in group to return (0 based).
    Integer maxResults = 50; // Integer | the maximum number of users to return (max 50).
    try {
      apiInstance.getUsersFromGroup(groupname, includeInactiveUsers, startAt, maxResults);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getUsersFromGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **groupname** | **String**| a name of the group for which members will be returned. | [optional] |
| **includeInactiveUsers** | **Boolean**| inactive users will be included in the response if set to true. | [optional] [default to false] |
| **startAt** | **Long**| the index of the first user in group to return (0 based). | [optional] [default to 0] |
| **maxResults** | **Integer**| the maximum number of users to return (max 50). | [optional] [default to 50] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getVersion"></a>
# **getVersion**
> getVersion(id, expand)



Returns a project version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The version to delete
    String expand = "expand_example"; // String | 
    try {
      apiInstance.getVersion(id, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVersion");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The version to delete | |
| **expand** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getVersionRelatedIssues"></a>
# **getVersionRelatedIssues**
> getVersionRelatedIssues(id)



Returns a bean containing the number of fixed in and affected issues for the given version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | a String containing the version id
    try {
      apiInstance.getVersionRelatedIssues(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVersionRelatedIssues");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| a String containing the version id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getVersionUnresolvedIssues"></a>
# **getVersionUnresolvedIssues**
> getVersionUnresolvedIssues(id)



Returns the number of unresolved issues for the given version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | a String containing the version id
    try {
      apiInstance.getVersionUnresolvedIssues(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVersionUnresolvedIssues");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| a String containing the version id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getVotes"></a>
# **getVotes**
> getVotes(issueIdOrKey)



A REST sub-resource representing the voters on the issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue to view voting information for
    try {
      apiInstance.getVotes(issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVotes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| the issue to view voting information for | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getWorkflow"></a>
# **getWorkflow**
> getWorkflow(id, workflowName, returnDraftIfExists)



Returns the workflow mappings or requested mapping to the caller for the passed scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the scheme.
    String workflowName = "workflowName_example"; // String | the workflow mapping to return. Null can be passed to return all mappings. Must be a valid workflow name.
    Boolean returnDraftIfExists = false; // Boolean | when true indicates that a scheme's draft, if it exists, should be queried instead of                             the scheme itself.
    try {
      apiInstance.getWorkflow(id, workflowName, returnDraftIfExists);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getWorkflow");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the scheme. | |
| **workflowName** | **String**| the workflow mapping to return. Null can be passed to return all mappings. Must be a valid workflow name. | [optional] |
| **returnDraftIfExists** | **Boolean**| when true indicates that a scheme&#39;s draft, if it exists, should be queried instead of                             the scheme itself. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getWorklog"></a>
# **getWorklog**
> getWorklog(issueIdOrKey, id)



Returns a specific worklog. &lt;br/&gt;  &lt;strong&gt;Note:&lt;/strong&gt; The work log won&#39;t be returned if the Log work field is hidden for the project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | a string containing the issue id or key the worklog belongs to
    String id = "id_example"; // String | id of the worklog to be deleted
    try {
      apiInstance.getWorklog(issueIdOrKey, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getWorklog");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| a string containing the issue id or key the worklog belongs to | |
| **id** | **String**| id of the worklog to be deleted | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getWorklogsForIds"></a>
# **getWorklogsForIds**
> getWorklogsForIds()



Returns worklogs for given worklog ids. Only worklogs to which the calling user has permissions, will be included in the result.  The returns set of worklogs is limited to 1000 elements.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getWorklogsForIds();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getWorklogsForIds");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="linkIssues"></a>
# **linkIssues**
> linkIssues()



Creates an issue link between two issues.  The user requires the link issue permission for the issue which will be linked to another issue.  The specified link type in the request is used to create the link and will create a link from the first issue  to the second issue using the outward description. It also create a link from the second issue to the first issue using the  inward description of the issue link type.  It will add the supplied comment to the first issue. The comment can have a restriction who can view it.  If group is specified, only users of this group can view this comment, if roleLevel is specified only users who have the specified role can view this comment.  The user who creates the issue link needs to belong to the specified group or have the specified role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.linkIssues();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#linkIssues");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="login"></a>
# **login**
> login()



Creates a new session for a user in JIRA. Once a session has been successfully created it can be used to access  any of JIRA&#39;s remote APIs and also the web UI by passing the appropriate HTTP Cookie header.  &lt;p&gt;  Note that it is generally preferrable to use HTTP BASIC authentication with the REST API. However, this resource  may be used to mimic the behaviour of JIRA&#39;s log-in page (e.g. to display log-in errors to a user).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.login();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#login");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="logout"></a>
# **logout**
> logout()



Logs the current user out of JIRA, destroying the existing session, if any.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.logout();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#logout");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="merge"></a>
# **merge**
> merge(moveIssuesTo, id)



Merge versions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String moveIssuesTo = "moveIssuesTo_example"; // String | The version to set fixVersion to on issues where the deleted version is the fix version,                      If null then the fixVersion is removed.
    String id = "id_example"; // String | The version that will be merged to version {@code moveIssuesTo} and removed
    try {
      apiInstance.merge(moveIssuesTo, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#merge");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **moveIssuesTo** | **String**| The version to set fixVersion to on issues where the deleted version is the fix version,                      If null then the fixVersion is removed. | |
| **id** | **String**| The version that will be merged to version {@code moveIssuesTo} and removed | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="moveField"></a>
# **moveField**
> moveField(screenId, tabId, id)



Moves field on the given tab

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long screenId = 56L; // Long | id of screen
    Long tabId = 56L; // Long | id of tab
    String id = "id_example"; // String | 
    try {
      apiInstance.moveField(screenId, tabId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#moveField");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **screenId** | **Long**| id of screen | |
| **tabId** | **Long**| id of tab | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="moveSubTasks"></a>
# **moveSubTasks**
> moveSubTasks(issueIdOrKey)



Reorders an issue&#39;s subtasks by moving the subtask at index \&quot;from\&quot;  to index \&quot;to\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | The parent issue's key or id
    try {
      apiInstance.moveSubTasks(issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#moveSubTasks");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| The parent issue&#39;s key or id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="moveTab"></a>
# **moveTab**
> moveTab(screenId, tabId, pos)



Moves tab position

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long screenId = 56L; // Long | id of screen
    Long tabId = 56L; // Long | id of tab
    Integer pos = 56; // Integer | position of tab
    try {
      apiInstance.moveTab(screenId, tabId, pos);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#moveTab");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **screenId** | **Long**| id of screen | |
| **tabId** | **Long**| id of tab | |
| **pos** | **Integer**| position of tab | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="moveVersion"></a>
# **moveVersion**
> moveVersion(id)



Modify a version&#39;s sequence within a project.  &lt;p/&gt;  The move version bean has 2 alternative field value pairs:  &lt;dl&gt;  &lt;dt&gt;position&lt;/dt&gt;&lt;dd&gt;An absolute position, which may have a value of &#39;First&#39;, &#39;Last&#39;, &#39;Earlier&#39; or &#39;Later&#39;&lt;/dd&gt;  &lt;dt&gt;after&lt;/dt&gt;&lt;dd&gt;A version to place this version after.  The value should be the self link of another version&lt;/dd&gt;  &lt;/dl&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | a String containing the version id
    try {
      apiInstance.moveVersion(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#moveVersion");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| a String containing the version id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="notify"></a>
# **notify**
> notify(issueIdOrKey)



Sends a notification (email) to the list or recipients defined in the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | a string containing the issue id or key the comment will be added to
    try {
      apiInstance.notify(issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#notify");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| a string containing the issue id or key the comment will be added to | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="partialUpdateProjectRole"></a>
# **partialUpdateProjectRole**
> partialUpdateProjectRole(id)



Partially updates a roles name or description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      apiInstance.partialUpdateProjectRole(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#partialUpdateProjectRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="policyCheckCreateUser"></a>
# **policyCheckCreateUser**
> policyCheckCreateUser()



Returns a list of statements explaining why the password policy would disallow a proposed password for a new user.  &lt;p&gt;  You can use this method to test the password policy validation. This could be done prior to an action   where a new user and related password are created, using methods like the ones in   &lt;a href&#x3D;\&quot;https://docs.atlassian.com/jira/latest/com/atlassian/jira/bc/user/UserService.html\&quot;&gt;UserService&lt;/a&gt;.        For example, you could use this to validate a password in a create user form in the user interface, as the user enters it.&lt;br/&gt;  The username and new password must be not empty to perform the validation.&lt;br/&gt;  Note, this method will help you validate against the policy only. It won&#39;t check any other validations that might be performed   when creating a new user, e.g. checking whether a user with the same name already exists.  &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.policyCheckCreateUser();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyCheckCreateUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="policyCheckUpdateUser"></a>
# **policyCheckUpdateUser**
> policyCheckUpdateUser()



Returns a list of statements explaining why the password policy would disallow a proposed new password for a user with an existing password.  &lt;p&gt;  You can use this method to test the password policy validation. This could be done prior to an action where the password   is actually updated, using methods like &lt;a href&#x3D;\&quot;https://docs.atlassian.com/jira/latest/com/atlassian/jira/web/action/user/ChangePassword.html\&quot;&gt;ChangePassword&lt;/a&gt;        or &lt;a href&#x3D;\&quot;https://docs.atlassian.com/jira/latest/com/atlassian/jira/web/action/user/ResetPassword.html\&quot;&gt;ResetPassword&lt;/a&gt;.   For example, you could use this to validate a password in a change password form in the user interface, as the user enters it.&lt;br/&gt;  The user must exist and the username and new password must be not empty, to perform the validation.&lt;br/&gt;  Note, this method will help you validate against the policy only. It won&#39;t check any other validations that might be performed   when submitting a password change/reset request, e.g. verifying whether the old password is valid.  &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.policyCheckUpdateUser();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyCheckUpdateUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="processRequests"></a>
# **processRequests**
> processRequests()



Executes any pending reindex requests.  Returns a JSON array containing the IDs of the reindex requests  that are being processed.  Execution is asynchronous - progress of the returned tasks can be monitored through  other REST calls.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.processRequests();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#processRequests");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="put"></a>
# **put**
> put(key, ifMatch)



Updates the ApplicationRole with the passed data. Only the groups and default groups setting of the  role may be updated. Requests to change the key or the name of the role will be silently ignored.  &lt;p&gt;  Optional: If versionHash is passed through the If-Match header the request will be rejected if not the  same as server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | the key of the role to update.
    String ifMatch = "ifMatch_example"; // String | the hash of the version to update. Optional Param
    try {
      apiInstance.put(key, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#put");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **key** | **String**| the key of the role to update. | |
| **ifMatch** | **String**| the hash of the version to update. Optional Param | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="putBulk"></a>
# **putBulk**
> putBulk(ifMatch)



Updates the ApplicationRoles with the passed data if the version hash is the same as the server.  Only the groups and default groups setting of the role may be updated. Requests to change the key  or the name of the role will be silently ignored. It is acceptable to pass only the roles that are updated  as roles that are present in the server but not in data to update with, will not be deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ifMatch = "ifMatch_example"; // String | 
    try {
      apiInstance.putBulk(ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putBulk");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ifMatch** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="reindex"></a>
# **reindex**
> reindex(type, indexComments, indexChangeHistory, indexWorklogs)



Kicks off a reindex.  Need Admin permissions to perform this reindex.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String type = "type_example"; // String | Case insensitive String indicating type of reindex.  If omitted, then defaults to BACKGROUND_PREFERRED.
    Boolean indexComments = false; // Boolean | Indicates that comments should also be reindexed. Not relevant for foreground reindex, where comments are always reindexed.
    Boolean indexChangeHistory = false; // Boolean | Indicates that changeHistory should also be reindexed. Not relevant for foreground reindex, where changeHistory is always reindexed.
    Boolean indexWorklogs = false; // Boolean | Indicates that changeHistory should also be reindexed. Not relevant for foreground reindex, where changeHistory is always reindexed.
    try {
      apiInstance.reindex(type, indexComments, indexChangeHistory, indexWorklogs);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#reindex");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **String**| Case insensitive String indicating type of reindex.  If omitted, then defaults to BACKGROUND_PREFERRED. | [optional] |
| **indexComments** | **Boolean**| Indicates that comments should also be reindexed. Not relevant for foreground reindex, where comments are always reindexed. | [optional] [default to false] |
| **indexChangeHistory** | **Boolean**| Indicates that changeHistory should also be reindexed. Not relevant for foreground reindex, where changeHistory is always reindexed. | [optional] [default to false] |
| **indexWorklogs** | **Boolean**| Indicates that changeHistory should also be reindexed. Not relevant for foreground reindex, where changeHistory is always reindexed. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="reindexIssues"></a>
# **reindexIssues**
> reindexIssues(issueId, indexComments, indexChangeHistory, indexWorklogs)



Reindexes one or more individual issues.  Indexing is performed synchronously - the call returns when indexing of  the issues has completed or a failure occurs.  &lt;p&gt;  Use either explicitly specified issue IDs or a JQL query to select issues to reindex.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueId = "issueId_example"; // String | the IDs or keys of one or more issues to reindex.
    Boolean indexComments = false; // Boolean | Indicates that comments should also be reindexed.
    Boolean indexChangeHistory = false; // Boolean | Indicates that changeHistory should also be reindexed.
    Boolean indexWorklogs = false; // Boolean | Indicates that changeHistory should also be reindexed.
    try {
      apiInstance.reindexIssues(issueId, indexComments, indexChangeHistory, indexWorklogs);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#reindexIssues");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueId** | **String**| the IDs or keys of one or more issues to reindex. | [optional] |
| **indexComments** | **Boolean**| Indicates that comments should also be reindexed. | [optional] [default to false] |
| **indexChangeHistory** | **Boolean**| Indicates that changeHistory should also be reindexed. | [optional] [default to false] |
| **indexWorklogs** | **Boolean**| Indicates that changeHistory should also be reindexed. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="release"></a>
# **release**
> release()



This method invalidates the any current WebSudo session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.release();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#release");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="removeAttachment"></a>
# **removeAttachment**
> removeAttachment(id)



Remove an attachment from an issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | id of the attachment to remove
    try {
      apiInstance.removeAttachment(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeAttachment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| id of the attachment to remove | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="removeField"></a>
# **removeField**
> removeField(screenId, tabId, id)



Removes field from given tab

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long screenId = 56L; // Long | id of screen
    Long tabId = 56L; // Long | id of tab
    String id = "id_example"; // String | 
    try {
      apiInstance.removeField(screenId, tabId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeField");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **screenId** | **Long**| id of screen | |
| **tabId** | **Long**| id of tab | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="removeGroup"></a>
# **removeGroup**
> removeGroup(groupname, swapGroup)



Deletes a group by given group parameter.  &lt;p&gt;  Returns no content

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String groupname = "groupname_example"; // String | (mandatory) The name of the group to delete.
    String swapGroup = "swapGroup_example"; // String | If you delete a group and content is restricted to that group, the content will be hidden from all users.   To prevent this, use this parameter to specify a different group to transfer the restrictions (comments and worklogs only) to.
    try {
      apiInstance.removeGroup(groupname, swapGroup);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **groupname** | **String**| (mandatory) The name of the group to delete. | [optional] |
| **swapGroup** | **String**| If you delete a group and content is restricted to that group, the content will be hidden from all users.   To prevent this, use this parameter to specify a different group to transfer the restrictions (comments and worklogs only) to. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="removePreference"></a>
# **removePreference**
> removePreference(key)



Removes preference of the currently logged in user. Preference key must be provided as input parameters (key). If  key parameter is not provided or wrong - status code 404. If preference is unset - status code 204.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | - key of the preference to be removed.
    try {
      apiInstance.removePreference(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removePreference");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **key** | **String**| - key of the preference to be removed. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="removeProjectCategory"></a>
# **removeProjectCategory**
> removeProjectCategory(id)



Delete a project category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      apiInstance.removeProjectCategory(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeProjectCategory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="removeUser"></a>
# **removeUser**
> removeUser(username, key)



Removes user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | the username
    String key = "key_example"; // String | user key
    try {
      apiInstance.removeUser(username, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| the username | [optional] |
| **key** | **String**| user key | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="removeUserFromApplication"></a>
# **removeUserFromApplication**
> removeUserFromApplication(username, applicationKey)



Remove user from given application. Admin permission will be required to perform this operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | username
    String applicationKey = "applicationKey_example"; // String | application key
    try {
      apiInstance.removeUserFromApplication(username, applicationKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeUserFromApplication");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| username | [optional] |
| **applicationKey** | **String**| application key | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="removeUserFromGroup"></a>
# **removeUserFromGroup**
> removeUserFromGroup(groupname, username)



Removes given user from a group.  &lt;p&gt;  Returns no content

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String groupname = "groupname_example"; // String | A name of requested group.
    String username = "username_example"; // String | User to remove from a group
    try {
      apiInstance.removeUserFromGroup(groupname, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeUserFromGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **groupname** | **String**| A name of requested group. | [optional] |
| **username** | **String**| User to remove from a group | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="removeVote"></a>
# **removeVote**
> removeVote(issueIdOrKey)



Remove your vote from an issue. (i.e. \&quot;unvote\&quot;)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue to view voting information for
    try {
      apiInstance.removeVote(issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeVote");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| the issue to view voting information for | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="removeWatcher"></a>
# **removeWatcher**
> removeWatcher(issueIdOrKey, username)



Removes a user from an issue&#39;s watcher list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | a String containing an issue key.
    String username = "username_example"; // String | a String containing the name of the user to remove from the watcher list. Must not be null.
    try {
      apiInstance.removeWatcher(issueIdOrKey, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeWatcher");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| a String containing an issue key. | |
| **username** | **String**| a String containing the name of the user to remove from the watcher list. Must not be null. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="renameTab"></a>
# **renameTab**
> renameTab(screenId, tabId)



Renames tab on given screen

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long screenId = 56L; // Long | id of screen
    Long tabId = 56L; // Long | id of tab
    try {
      apiInstance.renameTab(screenId, tabId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#renameTab");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **screenId** | **Long**| id of screen | |
| **tabId** | **Long**| id of tab | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="runUpgradesNow"></a>
# **runUpgradesNow**
> runUpgradesNow()



Runs any pending delayed upgrade tasks.  Need Admin permissions to do this.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.runUpgradesNow();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#runUpgradesNow");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="search"></a>
# **search**
> search(jql, startAt, maxResults, validateQuery, fields, expand)



Searches for issues using JQL.  &lt;p&gt;  &lt;b&gt;Sorting&lt;/b&gt;  the &lt;code&gt;jql&lt;/code&gt; parameter is a full &lt;a href&#x3D;\&quot;http://confluence.atlassian.com/display/JIRA/Advanced+Searching\&quot;&gt;JQL&lt;/a&gt;  expression, and includes an &lt;code&gt;ORDER BY&lt;/code&gt; clause.  &lt;/p&gt;  &lt;p&gt;  The &lt;code&gt;fields&lt;/code&gt; param (which can be specified multiple times) gives a comma-separated list of fields  to include in the response. This can be used to retrieve a subset of fields.  A particular field can be excluded by prefixing it with a minus.  &lt;p&gt;  By default, only navigable (&lt;code&gt;*navigable&lt;/code&gt;) fields are returned in this search resource. Note: the default is different  in the get-issue resource -- the default there all fields (&lt;code&gt;*all&lt;/code&gt;).  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;*all&lt;/code&gt; - include all fields&lt;/li&gt;  &lt;li&gt;&lt;code&gt;*navigable&lt;/code&gt; - include just navigable fields&lt;/li&gt;  &lt;li&gt;&lt;code&gt;summary,comment&lt;/code&gt; - include just the summary and comments&lt;/li&gt;  &lt;li&gt;&lt;code&gt;-description&lt;/code&gt; - include navigable fields except the description (the default is &lt;code&gt;*navigable&lt;/code&gt; for search)&lt;/li&gt;  &lt;li&gt;&lt;code&gt;*all,-comment&lt;/code&gt; - include everything except comments&lt;/li&gt;  &lt;/ul&gt;  &lt;p&gt;  &lt;/p&gt;  &lt;p&gt;&lt;b&gt;GET vs POST:&lt;/b&gt;  If the JQL query is too large to be encoded as a query param you should instead  POST to this resource.  &lt;/p&gt;  &lt;p&gt;  &lt;b&gt;Expanding Issues in the Search Result:&lt;/b&gt;  It is possible to expand the issues returned by directly specifying the expansion on the expand parameter passed  in to this resources.  &lt;/p&gt;  &lt;p&gt;  For instance, to expand the &amp;quot;changelog&amp;quot; for all the issues on the search result, it is neccesary to  specify &amp;quot;changelog&amp;quot; as one of the values to expand.  &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String jql = "jql_example"; // String | a JQL query string
    Integer startAt = 56; // Integer | the index of the first issue to return (0-based)
    Integer maxResults = 56; // Integer | the maximum number of issues to return (defaults to 50). The maximum allowable value is                       dictated by the JIRA property 'jira.search.views.default.max'. If you specify a value that is higher than this                       number, your search results will be truncated.
    Boolean validateQuery = true; // Boolean | whether to validate the JQL query
    String fields = "fields_example"; // String | the list of fields to return for each issue. By default, all navigable fields are returned.
    String expand = "expand_example"; // String | A comma-separated list of the parameters to expand.
    try {
      apiInstance.search(jql, startAt, maxResults, validateQuery, fields, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#search");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **jql** | **String**| a JQL query string | [optional] |
| **startAt** | **Integer**| the index of the first issue to return (0-based) | [optional] |
| **maxResults** | **Integer**| the maximum number of issues to return (defaults to 50). The maximum allowable value is                       dictated by the JIRA property &#39;jira.search.views.default.max&#39;. If you specify a value that is higher than this                       number, your search results will be truncated. | [optional] |
| **validateQuery** | **Boolean**| whether to validate the JQL query | [optional] [default to true] |
| **fields** | **String**| the list of fields to return for each issue. By default, all navigable fields are returned. | [optional] |
| **expand** | **String**| A comma-separated list of the parameters to expand. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="searchUsingSearchRequest"></a>
# **searchUsingSearchRequest**
> searchUsingSearchRequest()



Performs a search using JQL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.searchUsingSearchRequest();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#searchUsingSearchRequest");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="setActors"></a>
# **setActors**
> setActors(projectIdOrKey, id)



Updates a project role to include the specified actors (users or groups).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
    Long id = 56L; // Long | the project role id
    try {
      apiInstance.setActors(projectIdOrKey, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#setActors");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| the project id or project key | |
| **id** | **Long**| the project role id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="setBaseURL"></a>
# **setBaseURL**
> setBaseURL()



Sets the base URL that is configured for this JIRA instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.setBaseURL();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#setBaseURL");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="setDefaultShareScope"></a>
# **setDefaultShareScope**
> setDefaultShareScope()



Sets the default share scope of the logged-in user. Available values are GLOBAL and PRIVATE.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.setDefaultShareScope();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#setDefaultShareScope");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="setDraftIssueType"></a>
# **setDraftIssueType**
> setDraftIssueType(issueType, id)



Set the issue type mapping for the passed draft scheme.  &lt;p/&gt;  The passed representation can have its updateDraftIfNeeded flag set to true to indicate that  the draft should be created/updated when the actual scheme cannot be edited.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueType = "issueType_example"; // String | the issue type being set.
    Long id = 56L; // Long | the id of the parent scheme.
    try {
      apiInstance.setDraftIssueType(issueType, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#setDraftIssueType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueType** | **String**| the issue type being set. | |
| **id** | **Long**| the id of the parent scheme. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="setIssueNavigatorDefaultColumns"></a>
# **setIssueNavigatorDefaultColumns**
> setIssueNavigatorDefaultColumns()



Sets the default system columns for issue navigator. Admin permission will be required.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.setIssueNavigatorDefaultColumns();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#setIssueNavigatorDefaultColumns");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="setIssueType"></a>
# **setIssueType**
> setIssueType(issueType, id)



Set the issue type mapping for the passed scheme.  &lt;p/&gt;  The passed representation can have its updateDraftIfNeeded flag set to true to indicate that  the draft should be created/updated when the actual scheme cannot be edited.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueType = "issueType_example"; // String | the issue type being set.
    Long id = 56L; // Long | the id of the scheme.
    try {
      apiInstance.setIssueType(issueType, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#setIssueType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueType** | **String**| the issue type being set. | |
| **id** | **Long**| the id of the scheme. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="setPreference"></a>
# **setPreference**
> setPreference(key)



Sets preference of the currently logged in user. Preference key must be provided as input parameters (key). Value  must be provided as post body. If key or value parameter is not provided - status code 404. If preference is set  - status code 204.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | - key of the preference to be set.
    try {
      apiInstance.setPreference(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#setPreference");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **key** | **String**| - key of the preference to be set. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="setPropertyViaRestfulTable"></a>
# **setPropertyViaRestfulTable**
> setPropertyViaRestfulTable(id)



Modify an application property via PUT. The \&quot;value\&quot; field present in the PUT will override the existing value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.setPropertyViaRestfulTable(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#setPropertyViaRestfulTable");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="setReadyToUpgrade"></a>
# **setReadyToUpgrade**
> setReadyToUpgrade()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.setReadyToUpgrade();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#setReadyToUpgrade");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="setSchemeAttribute"></a>
# **setSchemeAttribute**
> setSchemeAttribute(permissionSchemeId, key)



Updates or inserts the attribute for a permission scheme specified by permission scheme id.  The attribute consists of the key and the value. The value will be converted to Boolean using Boolean#valueOf.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long permissionSchemeId = 56L; // Long | permission scheme id
    String key = "key_example"; // String | permission scheme attribute key
    try {
      apiInstance.setSchemeAttribute(permissionSchemeId, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#setSchemeAttribute");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **permissionSchemeId** | **Long**| permission scheme id | |
| **key** | **String**| permission scheme attribute key | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="start"></a>
# **start**
> start()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.start();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#start");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="stop"></a>
# **stop**
> stop()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.stop();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#stop");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="storeTemporaryAvatar"></a>
# **storeTemporaryAvatar**
> storeTemporaryAvatar(type, filename, size)



Creates temporary avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String type = "type_example"; // String | the avatar type
    String filename = "filename_example"; // String | name of file being uploaded
    Long size = 56L; // Long | size of file
    try {
      apiInstance.storeTemporaryAvatar(type, filename, size);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#storeTemporaryAvatar");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **String**| the avatar type | |
| **filename** | **String**| name of file being uploaded | [optional] |
| **size** | **Long**| size of file | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="update"></a>
# **update**
> update(id)



Update the passed workflow scheme.  &lt;p/&gt;  The body of the request is a representation of the workflow scheme. Values not passed are assumed to indicate  no change for that field.  &lt;p/&gt;  The passed representation can have its updateDraftIfNeeded flag set to true to indicate that the draft  should be created and/or updated when the actual scheme cannot be edited (e.g. when the scheme is being used by  a project). Values not appearing the body will not be touched.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the scheme.
    try {
      apiInstance.update(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#update");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the scheme. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updateComment"></a>
# **updateComment**
> updateComment(issueIdOrKey, id, expand)



Updates an existing comment using its JSON representation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | of the issue the comment belongs to
    String id = "id_example"; // String | the ID of the comment to request
    String expand = "expand_example"; // String | optional flags: renderedBody (provides body rendered in HTML)
    try {
      apiInstance.updateComment(issueIdOrKey, id, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateComment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| of the issue the comment belongs to | |
| **id** | **String**| the ID of the comment to request | |
| **expand** | **String**| optional flags: renderedBody (provides body rendered in HTML) | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updateComponent"></a>
# **updateComponent**
> updateComponent(id)



Modify a component via PUT. Any fields present in the PUT will override existing values. As a convenience, if a field  is not present, it is silently ignored.  &lt;p&gt;  If leadUserName is an empty string (\&quot;\&quot;) the component lead will be removed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The component to delete.
    try {
      apiInstance.updateComponent(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateComponent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The component to delete. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updateDefault"></a>
# **updateDefault**
> updateDefault(id)



Set the default workflow for the passed workflow scheme.  &lt;p/&gt;  The passed representation can have its  updateDraftIfNeeded flag set to true to indicate that the draft should be created/updated when the actual scheme  cannot be edited.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the scheme.
    try {
      apiInstance.updateDefault(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateDefault");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the scheme. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updateDraft"></a>
# **updateDraft**
> updateDraft(id)



Update a draft workflow scheme. The draft will created if necessary.  &lt;p/&gt;  The body is a representation of the workflow scheme. Values not passed are assumed to indicate no change for that field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the parent scheme.
    try {
      apiInstance.updateDraft(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateDraft");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the parent scheme. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updateDraftDefault"></a>
# **updateDraftDefault**
> updateDraftDefault(id)



Set the default workflow for the passed draft workflow scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the parent scheme.
    try {
      apiInstance.updateDraftDefault(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateDraftDefault");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the parent scheme. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updateDraftWorkflowMapping"></a>
# **updateDraftWorkflowMapping**
> updateDraftWorkflowMapping(id, workflowName)



Update the draft scheme to include the passed mapping.  &lt;p/&gt;  The body is a representation of the workflow mapping.  Values not passed are assumed to indicate no change for that field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the parent scheme.
    String workflowName = "workflowName_example"; // String | the name of the workflow mapping to update.
    try {
      apiInstance.updateDraftWorkflowMapping(id, workflowName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateDraftWorkflowMapping");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the parent scheme. | |
| **workflowName** | **String**| the name of the workflow mapping to update. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updateIssueLinkType"></a>
# **updateIssueLinkType**
> updateIssueLinkType(issueLinkTypeId)



Update the specified issue link type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueLinkTypeId = "issueLinkTypeId_example"; // String | 
    try {
      apiInstance.updateIssueLinkType(issueLinkTypeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateIssueLinkType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueLinkTypeId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updateIssueType"></a>
# **updateIssueType**
> updateIssueType(id)



Updates the specified issue type from a JSON representation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the id of the issue type to update.
    try {
      apiInstance.updateIssueType(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateIssueType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the issue type to update. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updatePermissionScheme"></a>
# **updatePermissionScheme**
> updatePermissionScheme(schemeId, expand)



Updates a permission scheme.  &lt;p&gt;  If the permissions list is present then it will be set in the permission scheme, which basically means it will overwrite any permission grants that  existed in the permission scheme. Sending an empty list will remove all permission grants from the permission scheme.  &lt;/p&gt;  &lt;p&gt;  To update just the name and description, do not send permissions list at all.  &lt;/p&gt;  &lt;p&gt;  To add or remove a single permission grant instead of updating the whole list at once use the &lt;b&gt;{schemeId}/permission/&lt;/b&gt; resource.  &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long schemeId = 56L; // Long | 
    String expand = "expand_example"; // String | 
    try {
      apiInstance.updatePermissionScheme(schemeId, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updatePermissionScheme");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **schemeId** | **Long**|  | |
| **expand** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updateProject"></a>
# **updateProject**
> updateProject(projectIdOrKey, expand)



Updates a project.  &lt;p&gt;  Only non null values sent in JSON will be updated in the project.&lt;/p&gt;  &lt;p&gt;  Values available for the assigneeType field are: \&quot;PROJECT_LEAD\&quot; and \&quot;UNASSIGNED\&quot;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
    String expand = "expand_example"; // String | the parameters to expand in returned project
    try {
      apiInstance.updateProject(projectIdOrKey, expand);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateProject");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| the project id or project key | |
| **expand** | **String**| the parameters to expand in returned project | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updateProjectCategory"></a>
# **updateProjectCategory**
> updateProjectCategory(id)



Modify a project category via PUT. Any fields present in the PUT will override existing values. As a convenience, if a field  is not present, it is silently ignored.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | 
    try {
      apiInstance.updateProjectCategory(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateProjectCategory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updateProjectType"></a>
# **updateProjectType**
> updateProjectType(projectIdOrKey, newProjectTypeKey)



Updates the type of a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String projectIdOrKey = "projectIdOrKey_example"; // String | identity of the project to update
    String newProjectTypeKey = "newProjectTypeKey_example"; // String | The key of the new project type
    try {
      apiInstance.updateProjectType(projectIdOrKey, newProjectTypeKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateProjectType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **projectIdOrKey** | **String**| identity of the project to update | |
| **newProjectTypeKey** | **String**| The key of the new project type | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updateProperty"></a>
# **updateProperty**
> updateProperty(id, key, workflowName, workflowMode)



Update/add new property to a transition. Trying to update a property that does  not exist will result in a new property being added.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the ID of the transition within the workflow.
    String key = "key_example"; // String | the name of the property to add.
    String workflowName = "workflowName_example"; // String | the name of the workflow to use.
    String workflowMode = "workflowMode_example"; // String | the type of workflow to use. Can either be \"live\" or \"draft\".
    try {
      apiInstance.updateProperty(id, key, workflowName, workflowMode);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateProperty");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the ID of the transition within the workflow. | |
| **key** | **String**| the name of the property to add. | [optional] |
| **workflowName** | **String**| the name of the workflow to use. | [optional] |
| **workflowMode** | **String**| the type of workflow to use. Can either be \&quot;live\&quot; or \&quot;draft\&quot;. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updateRemoteIssueLink"></a>
# **updateRemoteIssueLink**
> updateRemoteIssueLink(linkId, issueIdOrKey)



Updates a remote issue link from a JSON representation. Any fields not provided are set to null.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String linkId = "linkId_example"; // String | the id of the remote issue link
    String issueIdOrKey = "issueIdOrKey_example"; // String | the issue to create the remote issue link for
    try {
      apiInstance.updateRemoteIssueLink(linkId, issueIdOrKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateRemoteIssueLink");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **linkId** | **String**| the id of the remote issue link | |
| **issueIdOrKey** | **String**| the issue to create the remote issue link for | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updateVersion"></a>
# **updateVersion**
> updateVersion(id)



Modify a version via PUT. Any fields present in the PUT will override existing values. As a convenience, if a field  is not present, it is silently ignored.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The version to delete
    try {
      apiInstance.updateVersion(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateVersion");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The version to delete | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updateWorkflowMapping"></a>
# **updateWorkflowMapping**
> updateWorkflowMapping(id, workflowName)



Update the scheme to include the passed mapping.  &lt;p/&gt;  The body is a representation of the workflow mapping.  Values not passed are assumed to indicate no change for that field.  &lt;p/&gt;  The passed representation can have its updateDraftIfNeeded flag set to true to indicate that the draft  should be created/updated when the actual scheme cannot be edited.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | the id of the scheme.
    String workflowName = "workflowName_example"; // String | the name of the workflow mapping to update.
    try {
      apiInstance.updateWorkflowMapping(id, workflowName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateWorkflowMapping");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| the id of the scheme. | |
| **workflowName** | **String**| the name of the workflow mapping to update. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updateWorklog"></a>
# **updateWorklog**
> updateWorklog(issueIdOrKey, id, adjustEstimate, newEstimate)



Updates an existing worklog entry.  &lt;p&gt;Note that:&lt;/p&gt;   &lt;ul&gt;       &lt;li&gt;Fields possible for editing are: comment, visibility, started, timeSpent and timeSpentSeconds.&lt;/li&gt;       &lt;li&gt;Either timeSpent or timeSpentSeconds can be set.&lt;/li&gt;       &lt;li&gt;Fields which are not set will not be updated.&lt;/li&gt;       &lt;li&gt;For a request to be valid, it has to have at least one field change.&lt;/li&gt;   &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String issueIdOrKey = "issueIdOrKey_example"; // String | a string containing the issue id or key the worklog belongs to
    String id = "id_example"; // String | id of the worklog to be deleted
    String adjustEstimate = "adjustEstimate_example"; // String | (optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are                        <ul>                        <li>\"new\" - sets the estimate to a specific value</li>                        <li>\"leave\"- leaves the estimate as is</li>                        <li>\"auto\"- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog</li> </ul>
    String newEstimate = "newEstimate_example"; // String | (required when \"new\" is selected for adjustEstimate) the new value for the remaining estimate field.
    try {
      apiInstance.updateWorklog(issueIdOrKey, id, adjustEstimate, newEstimate);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateWorklog");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **issueIdOrKey** | **String**| a string containing the issue id or key the worklog belongs to | |
| **id** | **String**| id of the worklog to be deleted | |
| **adjustEstimate** | **String**| (optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are                        &lt;ul&gt;                        &lt;li&gt;\&quot;new\&quot; - sets the estimate to a specific value&lt;/li&gt;                        &lt;li&gt;\&quot;leave\&quot;- leaves the estimate as is&lt;/li&gt;                        &lt;li&gt;\&quot;auto\&quot;- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog&lt;/li&gt; &lt;/ul&gt; | [optional] |
| **newEstimate** | **String**| (required when \&quot;new\&quot; is selected for adjustEstimate) the new value for the remaining estimate field. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="validate"></a>
# **validate**
> validate()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://jira.local:8080/jira/rest");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.validate();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#validate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

