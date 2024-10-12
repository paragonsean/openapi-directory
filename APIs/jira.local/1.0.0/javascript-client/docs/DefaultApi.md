# Jira761.DefaultApi

All URIs are relative to *http://jira.local:8080/jira/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledgeErrors**](DefaultApi.md#acknowledgeErrors) | **POST** /api/2/cluster/zdu/retryUpgrade | 
[**addActorUsers**](DefaultApi.md#addActorUsers) | **POST** /api/2/project/{projectIdOrKey}/role/{id} | 
[**addAttachment**](DefaultApi.md#addAttachment) | **POST** /api/2/issue/{issueIdOrKey}/attachments | 
[**addComment**](DefaultApi.md#addComment) | **POST** /api/2/issue/{issueIdOrKey}/comment | 
[**addField**](DefaultApi.md#addField) | **POST** /api/2/screens/{screenId}/tabs/{tabId}/fields | 
[**addFieldToDefaultScreen**](DefaultApi.md#addFieldToDefaultScreen) | **POST** /api/2/screens/addToDefault/{fieldId} | 
[**addProjectRoleActorsToRole**](DefaultApi.md#addProjectRoleActorsToRole) | **POST** /api/2/role/{id}/actors | 
[**addRecord**](DefaultApi.md#addRecord) | **POST** /api/2/auditing/record | 
[**addSharePermission**](DefaultApi.md#addSharePermission) | **POST** /api/2/filter/{id}/permission | 
[**addTab**](DefaultApi.md#addTab) | **POST** /api/2/screens/{screenId}/tabs | 
[**addUserToApplication**](DefaultApi.md#addUserToApplication) | **POST** /api/2/user/application | 
[**addUserToGroup**](DefaultApi.md#addUserToGroup) | **POST** /api/2/group/user | 
[**addVote**](DefaultApi.md#addVote) | **POST** /api/2/issue/{issueIdOrKey}/votes | 
[**addWatcher**](DefaultApi.md#addWatcher) | **POST** /api/2/issue/{issueIdOrKey}/watchers | 
[**addWorklog**](DefaultApi.md#addWorklog) | **POST** /api/2/issue/{issueIdOrKey}/worklog | 
[**api2ApplicationPropertiesGet**](DefaultApi.md#api2ApplicationPropertiesGet) | **GET** /api/2/application-properties | 
[**api2AvatarTypeTemporaryCropPost**](DefaultApi.md#api2AvatarTypeTemporaryCropPost) | **POST** /api/2/avatar/{type}/temporaryCrop | 
[**api2CommentCommentIdPropertiesGet**](DefaultApi.md#api2CommentCommentIdPropertiesGet) | **GET** /api/2/comment/{commentId}/properties | 
[**api2CommentCommentIdPropertiesPropertyKeyDelete**](DefaultApi.md#api2CommentCommentIdPropertiesPropertyKeyDelete) | **DELETE** /api/2/comment/{commentId}/properties/{propertyKey} | 
[**api2CommentCommentIdPropertiesPropertyKeyGet**](DefaultApi.md#api2CommentCommentIdPropertiesPropertyKeyGet) | **GET** /api/2/comment/{commentId}/properties/{propertyKey} | 
[**api2CommentCommentIdPropertiesPropertyKeyPut**](DefaultApi.md#api2CommentCommentIdPropertiesPropertyKeyPut) | **PUT** /api/2/comment/{commentId}/properties/{propertyKey} | 
[**api2ComponentIdDelete**](DefaultApi.md#api2ComponentIdDelete) | **DELETE** /api/2/component/{id} | 
[**api2DashboardDashboardIdItemsItemIdPropertiesGet**](DefaultApi.md#api2DashboardDashboardIdItemsItemIdPropertiesGet) | **GET** /api/2/dashboard/{dashboardId}/items/{itemId}/properties | 
[**api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyDelete**](DefaultApi.md#api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyDelete) | **DELETE** /api/2/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey} | 
[**api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyGet**](DefaultApi.md#api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyGet) | **GET** /api/2/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey} | 
[**api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyPut**](DefaultApi.md#api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyPut) | **PUT** /api/2/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey} | 
[**api2FilterIdColumnsDelete**](DefaultApi.md#api2FilterIdColumnsDelete) | **DELETE** /api/2/filter/{id}/columns | 
[**api2FilterIdColumnsGet**](DefaultApi.md#api2FilterIdColumnsGet) | **GET** /api/2/filter/{id}/columns | 
[**api2FilterIdColumnsPut**](DefaultApi.md#api2FilterIdColumnsPut) | **PUT** /api/2/filter/{id}/columns | 
[**api2IssueIssueIdOrKeyPropertiesGet**](DefaultApi.md#api2IssueIssueIdOrKeyPropertiesGet) | **GET** /api/2/issue/{issueIdOrKey}/properties | 
[**api2IssueIssueIdOrKeyPropertiesPropertyKeyDelete**](DefaultApi.md#api2IssueIssueIdOrKeyPropertiesPropertyKeyDelete) | **DELETE** /api/2/issue/{issueIdOrKey}/properties/{propertyKey} | 
[**api2IssueIssueIdOrKeyPropertiesPropertyKeyGet**](DefaultApi.md#api2IssueIssueIdOrKeyPropertiesPropertyKeyGet) | **GET** /api/2/issue/{issueIdOrKey}/properties/{propertyKey} | 
[**api2IssueIssueIdOrKeyPropertiesPropertyKeyPut**](DefaultApi.md#api2IssueIssueIdOrKeyPropertiesPropertyKeyPut) | **PUT** /api/2/issue/{issueIdOrKey}/properties/{propertyKey} | 
[**api2IssuesecurityschemesIdGet**](DefaultApi.md#api2IssuesecurityschemesIdGet) | **GET** /api/2/issuesecurityschemes/{id} | 
[**api2IssuetypeIdAvatarPost**](DefaultApi.md#api2IssuetypeIdAvatarPost) | **POST** /api/2/issuetype/{id}/avatar | 
[**api2IssuetypeIdAvatarTemporaryPost**](DefaultApi.md#api2IssuetypeIdAvatarTemporaryPost) | **POST** /api/2/issuetype/{id}/avatar/temporary | 
[**api2IssuetypeIdDelete**](DefaultApi.md#api2IssuetypeIdDelete) | **DELETE** /api/2/issuetype/{id} | 
[**api2IssuetypeIdGet**](DefaultApi.md#api2IssuetypeIdGet) | **GET** /api/2/issuetype/{id} | 
[**api2IssuetypeIssueTypeIdPropertiesPropertyKeyDelete**](DefaultApi.md#api2IssuetypeIssueTypeIdPropertiesPropertyKeyDelete) | **DELETE** /api/2/issuetype/{issueTypeId}/properties/{propertyKey} | 
[**api2IssuetypeIssueTypeIdPropertiesPropertyKeyGet**](DefaultApi.md#api2IssuetypeIssueTypeIdPropertiesPropertyKeyGet) | **GET** /api/2/issuetype/{issueTypeId}/properties/{propertyKey} | 
[**api2IssuetypeIssueTypeIdPropertiesPropertyKeyPut**](DefaultApi.md#api2IssuetypeIssueTypeIdPropertiesPropertyKeyPut) | **PUT** /api/2/issuetype/{issueTypeId}/properties/{propertyKey} | 
[**api2MyselfGet**](DefaultApi.md#api2MyselfGet) | **GET** /api/2/myself | 
[**api2MyselfPut**](DefaultApi.md#api2MyselfPut) | **PUT** /api/2/myself | 
[**api2NotificationschemeIdGet**](DefaultApi.md#api2NotificationschemeIdGet) | **GET** /api/2/notificationscheme/{id} | 
[**api2ProjectProjectIdOrKeyAvatarIdDelete**](DefaultApi.md#api2ProjectProjectIdOrKeyAvatarIdDelete) | **DELETE** /api/2/project/{projectIdOrKey}/avatar/{id} | 
[**api2ProjectProjectIdOrKeyAvatarPost**](DefaultApi.md#api2ProjectProjectIdOrKeyAvatarPost) | **POST** /api/2/project/{projectIdOrKey}/avatar | 
[**api2ProjectProjectIdOrKeyAvatarPut**](DefaultApi.md#api2ProjectProjectIdOrKeyAvatarPut) | **PUT** /api/2/project/{projectIdOrKey}/avatar | 
[**api2ProjectProjectIdOrKeyAvatarTemporaryPost**](DefaultApi.md#api2ProjectProjectIdOrKeyAvatarTemporaryPost) | **POST** /api/2/project/{projectIdOrKey}/avatar/temporary | 
[**api2ProjectProjectIdOrKeyAvatarsGet**](DefaultApi.md#api2ProjectProjectIdOrKeyAvatarsGet) | **GET** /api/2/project/{projectIdOrKey}/avatars | 
[**api2ProjectProjectIdOrKeyGet**](DefaultApi.md#api2ProjectProjectIdOrKeyGet) | **GET** /api/2/project/{projectIdOrKey} | 
[**api2ProjectProjectIdOrKeyPropertiesGet**](DefaultApi.md#api2ProjectProjectIdOrKeyPropertiesGet) | **GET** /api/2/project/{projectIdOrKey}/properties | 
[**api2ProjectProjectIdOrKeyPropertiesPropertyKeyDelete**](DefaultApi.md#api2ProjectProjectIdOrKeyPropertiesPropertyKeyDelete) | **DELETE** /api/2/project/{projectIdOrKey}/properties/{propertyKey} | 
[**api2ProjectProjectIdOrKeyPropertiesPropertyKeyGet**](DefaultApi.md#api2ProjectProjectIdOrKeyPropertiesPropertyKeyGet) | **GET** /api/2/project/{projectIdOrKey}/properties/{propertyKey} | 
[**api2ProjectProjectIdOrKeyPropertiesPropertyKeyPut**](DefaultApi.md#api2ProjectProjectIdOrKeyPropertiesPropertyKeyPut) | **PUT** /api/2/project/{projectIdOrKey}/properties/{propertyKey} | 
[**api2ProjectProjectIdOrKeyRoleGet**](DefaultApi.md#api2ProjectProjectIdOrKeyRoleGet) | **GET** /api/2/project/{projectIdOrKey}/role | 
[**api2ProjectProjectKeyOrIdIssuesecuritylevelschemeGet**](DefaultApi.md#api2ProjectProjectKeyOrIdIssuesecuritylevelschemeGet) | **GET** /api/2/project/{projectKeyOrId}/issuesecuritylevelscheme | 
[**api2ProjectProjectKeyOrIdNotificationschemeGet**](DefaultApi.md#api2ProjectProjectKeyOrIdNotificationschemeGet) | **GET** /api/2/project/{projectKeyOrId}/notificationscheme | 
[**api2ProjectvalidateKeyGet**](DefaultApi.md#api2ProjectvalidateKeyGet) | **GET** /api/2/projectvalidate/key | 
[**api2RoleGet**](DefaultApi.md#api2RoleGet) | **GET** /api/2/role | 
[**api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarIdDelete**](DefaultApi.md#api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarIdDelete) | **DELETE** /api/2/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id} | 
[**api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarPost**](DefaultApi.md#api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarPost) | **POST** /api/2/universal_avatar/type/{type}/owner/{owningObjectId}/avatar | 
[**api2UniversalAvatarTypeTypeOwnerOwningObjectIdTempPost**](DefaultApi.md#api2UniversalAvatarTypeTypeOwnerOwningObjectIdTempPost) | **POST** /api/2/universal_avatar/type/{type}/owner/{owningObjectId}/temp | 
[**api2UserAvatarIdDelete**](DefaultApi.md#api2UserAvatarIdDelete) | **DELETE** /api/2/user/avatar/{id} | 
[**api2UserAvatarPost**](DefaultApi.md#api2UserAvatarPost) | **POST** /api/2/user/avatar | 
[**api2UserAvatarPut**](DefaultApi.md#api2UserAvatarPut) | **PUT** /api/2/user/avatar | 
[**api2UserAvatarTemporaryPost**](DefaultApi.md#api2UserAvatarTemporaryPost) | **POST** /api/2/user/avatar/temporary | 
[**api2UserAvatarsGet**](DefaultApi.md#api2UserAvatarsGet) | **GET** /api/2/user/avatars | 
[**api2UserColumnsDelete**](DefaultApi.md#api2UserColumnsDelete) | **DELETE** /api/2/user/columns | 
[**api2UserColumnsGet**](DefaultApi.md#api2UserColumnsGet) | **GET** /api/2/user/columns | 
[**api2UserColumnsPut**](DefaultApi.md#api2UserColumnsPut) | **PUT** /api/2/user/columns | 
[**api2UserGet**](DefaultApi.md#api2UserGet) | **GET** /api/2/user | 
[**api2UserPropertiesGet**](DefaultApi.md#api2UserPropertiesGet) | **GET** /api/2/user/properties/ | 
[**api2UserPropertiesPropertyKeyDelete**](DefaultApi.md#api2UserPropertiesPropertyKeyDelete) | **DELETE** /api/2/user/properties/{propertyKey} | 
[**api2UserPropertiesPropertyKeyGet**](DefaultApi.md#api2UserPropertiesPropertyKeyGet) | **GET** /api/2/user/properties/{propertyKey} | 
[**api2UserPropertiesPropertyKeyPut**](DefaultApi.md#api2UserPropertiesPropertyKeyPut) | **PUT** /api/2/user/properties/{propertyKey} | 
[**api2UserPut**](DefaultApi.md#api2UserPut) | **PUT** /api/2/user | 
[**api2VersionIdDelete**](DefaultApi.md#api2VersionIdDelete) | **DELETE** /api/2/version/{id} | 
[**api2VersionIdRemoveAndSwapPost**](DefaultApi.md#api2VersionIdRemoveAndSwapPost) | **POST** /api/2/version/{id}/removeAndSwap | 
[**api2VersionVersionIdRemotelinkGlobalIdPost**](DefaultApi.md#api2VersionVersionIdRemotelinkGlobalIdPost) | **POST** /api/2/version/{versionId}/remotelink/{globalId} | 
[**api2VersionVersionIdRemotelinkPost**](DefaultApi.md#api2VersionVersionIdRemotelinkPost) | **POST** /api/2/version/{versionId}/remotelink | 
[**api2WorkflowApi2TransitionsIdPropertiesDelete**](DefaultApi.md#api2WorkflowApi2TransitionsIdPropertiesDelete) | **DELETE** /api/2/workflow/api/2/transitions/{id}/properties | 
[**api2WorkflowschemeIdIssuetypeIssueTypeDelete**](DefaultApi.md#api2WorkflowschemeIdIssuetypeIssueTypeDelete) | **DELETE** /api/2/workflowscheme/{id}/issuetype/{issueType} | 
[**api2WorkflowschemeIdIssuetypeIssueTypeGet**](DefaultApi.md#api2WorkflowschemeIdIssuetypeIssueTypeGet) | **GET** /api/2/workflowscheme/{id}/issuetype/{issueType} | 
[**approveUpgrade**](DefaultApi.md#approveUpgrade) | **POST** /api/2/cluster/zdu/approve | 
[**areMetricsExposed**](DefaultApi.md#areMetricsExposed) | **GET** /api/2/monitoring/jmx/areMetricsExposed | 
[**assign**](DefaultApi.md#assign) | **PUT** /api/2/issue/{issueIdOrKey}/assignee | 
[**assignPermissionScheme**](DefaultApi.md#assignPermissionScheme) | **PUT** /api/2/project/{projectKeyOrId}/permissionscheme | 
[**canMoveSubTask**](DefaultApi.md#canMoveSubTask) | **GET** /api/2/issue/{issueIdOrKey}/subtask/move | 
[**cancelUpgrade**](DefaultApi.md#cancelUpgrade) | **POST** /api/2/cluster/zdu/cancel | 
[**changeMyPassword**](DefaultApi.md#changeMyPassword) | **PUT** /api/2/myself/password | 
[**changeUserPassword**](DefaultApi.md#changeUserPassword) | **PUT** /api/2/user/password | 
[**createComponent**](DefaultApi.md#createComponent) | **POST** /api/2/component | 
[**createCustomField**](DefaultApi.md#createCustomField) | **POST** /api/2/field | 
[**createDraftForParent**](DefaultApi.md#createDraftForParent) | **POST** /api/2/workflowscheme/{id}/createdraft | 
[**createFilter**](DefaultApi.md#createFilter) | **POST** /api/2/filter | 
[**createGroup**](DefaultApi.md#createGroup) | **POST** /api/2/group | 
[**createIssue**](DefaultApi.md#createIssue) | **POST** /api/2/issue | 
[**createIssueLinkType**](DefaultApi.md#createIssueLinkType) | **POST** /api/2/issueLinkType | 
[**createIssueType**](DefaultApi.md#createIssueType) | **POST** /api/2/issuetype | 
[**createIssues**](DefaultApi.md#createIssues) | **POST** /api/2/issue/bulk | 
[**createOrUpdateRemoteIssueLink**](DefaultApi.md#createOrUpdateRemoteIssueLink) | **POST** /api/2/issue/{issueIdOrKey}/remotelink | 
[**createPermissionGrant**](DefaultApi.md#createPermissionGrant) | **POST** /api/2/permissionscheme/{schemeId}/permission | 
[**createPermissionScheme**](DefaultApi.md#createPermissionScheme) | **POST** /api/2/permissionscheme | 
[**createProject**](DefaultApi.md#createProject) | **POST** /api/2/project | 
[**createProjectCategory**](DefaultApi.md#createProjectCategory) | **POST** /api/2/projectCategory | 
[**createProjectRole**](DefaultApi.md#createProjectRole) | **POST** /api/2/role | 
[**createProperty**](DefaultApi.md#createProperty) | **POST** /api/2/workflow/api/2/transitions/{id}/properties | 
[**createScheme**](DefaultApi.md#createScheme) | **POST** /api/2/workflowscheme | 
[**createUser**](DefaultApi.md#createUser) | **POST** /api/2/user | 
[**createVersion**](DefaultApi.md#createVersion) | **POST** /api/2/version | 
[**currentUser**](DefaultApi.md#currentUser) | **GET** /auth/1/session | 
[**deleteActor**](DefaultApi.md#deleteActor) | **DELETE** /api/2/project/{projectIdOrKey}/role/{id} | 
[**deleteComment**](DefaultApi.md#deleteComment) | **DELETE** /api/2/issue/{issueIdOrKey}/comment/{id} | 
[**deleteDefault**](DefaultApi.md#deleteDefault) | **DELETE** /api/2/workflowscheme/{id}/default | 
[**deleteDraftById**](DefaultApi.md#deleteDraftById) | **DELETE** /api/2/workflowscheme/{id}/draft | 
[**deleteDraftDefault**](DefaultApi.md#deleteDraftDefault) | **DELETE** /api/2/workflowscheme/{id}/draft/default | 
[**deleteDraftIssueType**](DefaultApi.md#deleteDraftIssueType) | **DELETE** /api/2/workflowscheme/{id}/draft/issuetype/{issueType} | 
[**deleteDraftWorkflowMapping**](DefaultApi.md#deleteDraftWorkflowMapping) | **DELETE** /api/2/workflowscheme/{id}/draft/workflow | 
[**deleteFilter**](DefaultApi.md#deleteFilter) | **DELETE** /api/2/filter/{id} | 
[**deleteIssue**](DefaultApi.md#deleteIssue) | **DELETE** /api/2/issue/{issueIdOrKey} | 
[**deleteIssueLink**](DefaultApi.md#deleteIssueLink) | **DELETE** /api/2/issueLink/{linkId} | 
[**deleteIssueLinkType**](DefaultApi.md#deleteIssueLinkType) | **DELETE** /api/2/issueLinkType/{issueLinkTypeId} | 
[**deletePermissionScheme**](DefaultApi.md#deletePermissionScheme) | **DELETE** /api/2/permissionscheme/{schemeId} | 
[**deletePermissionSchemeEntity**](DefaultApi.md#deletePermissionSchemeEntity) | **DELETE** /api/2/permissionscheme/{schemeId}/permission/{permissionId} | 
[**deleteProject**](DefaultApi.md#deleteProject) | **DELETE** /api/2/project/{projectIdOrKey} | 
[**deleteProjectRole**](DefaultApi.md#deleteProjectRole) | **DELETE** /api/2/role/{id} | 
[**deleteProjectRoleActorsFromRole**](DefaultApi.md#deleteProjectRoleActorsFromRole) | **DELETE** /api/2/role/{id}/actors | 
[**deleteRemoteIssueLinkByGlobalId**](DefaultApi.md#deleteRemoteIssueLinkByGlobalId) | **DELETE** /api/2/issue/{issueIdOrKey}/remotelink | 
[**deleteRemoteIssueLinkById**](DefaultApi.md#deleteRemoteIssueLinkById) | **DELETE** /api/2/issue/{issueIdOrKey}/remotelink/{linkId} | 
[**deleteRemoteVersionLink**](DefaultApi.md#deleteRemoteVersionLink) | **DELETE** /api/2/version/{versionId}/remotelink/{globalId} | 
[**deleteRemoteVersionLinksByVersionId**](DefaultApi.md#deleteRemoteVersionLinksByVersionId) | **DELETE** /api/2/version/{versionId}/remotelink | 
[**deleteScheme**](DefaultApi.md#deleteScheme) | **DELETE** /api/2/workflowscheme/{id} | 
[**deleteSharePermission**](DefaultApi.md#deleteSharePermission) | **DELETE** /api/2/filter/{id}/permission/{permission-id} | 
[**deleteTab**](DefaultApi.md#deleteTab) | **DELETE** /api/2/screens/{screenId}/tabs/{tabId} | 
[**deleteWorkflowMapping**](DefaultApi.md#deleteWorkflowMapping) | **DELETE** /api/2/workflowscheme/{id}/workflow | 
[**deleteWorklog**](DefaultApi.md#deleteWorklog) | **DELETE** /api/2/issue/{issueIdOrKey}/worklog/{id} | 
[**doTransition**](DefaultApi.md#doTransition) | **POST** /api/2/issue/{issueIdOrKey}/transitions | 
[**editFilter**](DefaultApi.md#editFilter) | **PUT** /api/2/filter/{id} | 
[**editIssue**](DefaultApi.md#editIssue) | **PUT** /api/2/issue/{issueIdOrKey} | 
[**expandForHumans**](DefaultApi.md#expandForHumans) | **GET** /api/2/attachment/{id}/expand/human | 
[**expandForMachines**](DefaultApi.md#expandForMachines) | **GET** /api/2/attachment/{id}/expand/raw | 
[**findAssignableUsers**](DefaultApi.md#findAssignableUsers) | **GET** /api/2/user/assignable/search | 
[**findBulkAssignableUsers**](DefaultApi.md#findBulkAssignableUsers) | **GET** /api/2/user/assignable/multiProjectSearch | 
[**findGroups**](DefaultApi.md#findGroups) | **GET** /api/2/groups/picker | 
[**findUsers**](DefaultApi.md#findUsers) | **GET** /api/2/user/search | 
[**findUsersAndGroups**](DefaultApi.md#findUsersAndGroups) | **GET** /api/2/groupuserpicker | 
[**findUsersForPicker**](DefaultApi.md#findUsersForPicker) | **GET** /api/2/user/picker | 
[**findUsersWithAllPermissions**](DefaultApi.md#findUsersWithAllPermissions) | **GET** /api/2/user/permission/search | 
[**findUsersWithBrowsePermission**](DefaultApi.md#findUsersWithBrowsePermission) | **GET** /api/2/user/viewissue/search | 
[**fullyUpdateProjectRole**](DefaultApi.md#fullyUpdateProjectRole) | **PUT** /api/2/role/{id} | 
[**get**](DefaultApi.md#get) | **GET** /api/2/applicationrole/{key} | 
[**getAccessibleProjectTypeByKey**](DefaultApi.md#getAccessibleProjectTypeByKey) | **GET** /api/2/project/type/{projectTypeKey}/accessible | 
[**getAdvancedSettings**](DefaultApi.md#getAdvancedSettings) | **GET** /api/2/application-properties/advanced-settings | 
[**getAll**](DefaultApi.md#getAll) | **GET** /api/2/applicationrole | 
[**getAllFields**](DefaultApi.md#getAllFields) | **GET** /api/2/screens/{screenId}/tabs/{tabId}/fields | 
[**getAllPermissions**](DefaultApi.md#getAllPermissions) | **GET** /api/2/permissions | 
[**getAllProjectCategories**](DefaultApi.md#getAllProjectCategories) | **GET** /api/2/projectCategory | 
[**getAllProjectTypes**](DefaultApi.md#getAllProjectTypes) | **GET** /api/2/project/type | 
[**getAllProjects**](DefaultApi.md#getAllProjects) | **GET** /api/2/project | 
[**getAllStatuses**](DefaultApi.md#getAllStatuses) | **GET** /api/2/project/{projectIdOrKey}/statuses | 
[**getAllSystemAvatars**](DefaultApi.md#getAllSystemAvatars) | **GET** /api/2/avatar/{type}/system | 
[**getAllTabs**](DefaultApi.md#getAllTabs) | **GET** /api/2/screens/{screenId}/tabs | 
[**getAllWorkflows**](DefaultApi.md#getAllWorkflows) | **GET** /api/2/workflow | 
[**getAlternativeIssueTypes**](DefaultApi.md#getAlternativeIssueTypes) | **GET** /api/2/issuetype/{id}/alternatives | 
[**getAssignedPermissionScheme**](DefaultApi.md#getAssignedPermissionScheme) | **GET** /api/2/project/{projectKeyOrId}/permissionscheme | 
[**getAttachment**](DefaultApi.md#getAttachment) | **GET** /api/2/attachment/{id} | 
[**getAttachmentMeta**](DefaultApi.md#getAttachmentMeta) | **GET** /api/2/attachment/meta | 
[**getAutoComplete**](DefaultApi.md#getAutoComplete) | **GET** /api/2/jql/autocompletedata | 
[**getAvailableMetrics**](DefaultApi.md#getAvailableMetrics) | **GET** /api/2/monitoring/jmx/getAvailableMetrics | 
[**getAvatars**](DefaultApi.md#getAvatars) | **GET** /api/2/universal_avatar/type/{type}/owner/{owningObjectId} | 
[**getById**](DefaultApi.md#getById) | **GET** /api/2/workflowscheme/{id} | 
[**getComment**](DefaultApi.md#getComment) | **GET** /api/2/issue/{issueIdOrKey}/comment/{id} | 
[**getComments**](DefaultApi.md#getComments) | **GET** /api/2/issue/{issueIdOrKey}/comment | 
[**getComponent**](DefaultApi.md#getComponent) | **GET** /api/2/component/{id} | 
[**getComponentRelatedIssues**](DefaultApi.md#getComponentRelatedIssues) | **GET** /api/2/component/{id}/relatedIssueCounts | 
[**getConfiguration**](DefaultApi.md#getConfiguration) | **GET** /api/2/configuration | 
[**getCreateIssueMeta**](DefaultApi.md#getCreateIssueMeta) | **GET** /api/2/issue/createmeta | 
[**getCustomFieldOption**](DefaultApi.md#getCustomFieldOption) | **GET** /api/2/customFieldOption/{id} | 
[**getDashboard**](DefaultApi.md#getDashboard) | **GET** /api/2/dashboard/{id} | 
[**getDefault**](DefaultApi.md#getDefault) | **GET** /api/2/workflowscheme/{id}/default | 
[**getDefaultShareScope**](DefaultApi.md#getDefaultShareScope) | **GET** /api/2/filter/defaultShareScope | 
[**getDraftById**](DefaultApi.md#getDraftById) | **GET** /api/2/workflowscheme/{id}/draft | 
[**getDraftDefault**](DefaultApi.md#getDraftDefault) | **GET** /api/2/workflowscheme/{id}/draft/default | 
[**getDraftIssueType**](DefaultApi.md#getDraftIssueType) | **GET** /api/2/workflowscheme/{id}/draft/issuetype/{issueType} | 
[**getDraftWorkflow**](DefaultApi.md#getDraftWorkflow) | **GET** /api/2/workflowscheme/{id}/draft/workflow | 
[**getEditIssueMeta**](DefaultApi.md#getEditIssueMeta) | **GET** /api/2/issue/{issueIdOrKey}/editmeta | 
[**getFavouriteFilters**](DefaultApi.md#getFavouriteFilters) | **GET** /api/2/filter/favourite | 
[**getFieldAutoCompleteForQueryString**](DefaultApi.md#getFieldAutoCompleteForQueryString) | **GET** /api/2/jql/autocompletedata/suggestions | 
[**getFields**](DefaultApi.md#getFields) | **GET** /api/2/field | 
[**getFieldsToAdd**](DefaultApi.md#getFieldsToAdd) | **GET** /api/2/screens/{screenId}/availableFields | 
[**getFilter**](DefaultApi.md#getFilter) | **GET** /api/2/filter/{id} | 
[**getGroup**](DefaultApi.md#getGroup) | **GET** /api/2/group | 
[**getIdsOfWorklogsDeletedSince**](DefaultApi.md#getIdsOfWorklogsDeletedSince) | **GET** /api/2/worklog/deleted | 
[**getIdsOfWorklogsModifiedSince**](DefaultApi.md#getIdsOfWorklogsModifiedSince) | **GET** /api/2/worklog/updated | 
[**getIndexSummary**](DefaultApi.md#getIndexSummary) | **GET** /api/2/index/summary | 
[**getIssue**](DefaultApi.md#getIssue) | **GET** /api/2/issue/{issueIdOrKey} | 
[**getIssueAllTypes**](DefaultApi.md#getIssueAllTypes) | **GET** /api/2/issuetype | 
[**getIssueLink**](DefaultApi.md#getIssueLink) | **GET** /api/2/issueLink/{linkId} | 
[**getIssueLinkType**](DefaultApi.md#getIssueLinkType) | **GET** /api/2/issueLinkType/{issueLinkTypeId} | 
[**getIssueLinkTypes**](DefaultApi.md#getIssueLinkTypes) | **GET** /api/2/issueLinkType | 
[**getIssueNavigatorDefaultColumns**](DefaultApi.md#getIssueNavigatorDefaultColumns) | **GET** /api/2/settings/columns | 
[**getIssuePickerResource**](DefaultApi.md#getIssuePickerResource) | **GET** /api/2/issue/picker | 
[**getIssueSecuritySchemes**](DefaultApi.md#getIssueSecuritySchemes) | **GET** /api/2/issuesecurityschemes | 
[**getIssueWatchers**](DefaultApi.md#getIssueWatchers) | **GET** /api/2/issue/{issueIdOrKey}/watchers | 
[**getIssueWorklog**](DefaultApi.md#getIssueWorklog) | **GET** /api/2/issue/{issueIdOrKey}/worklog | 
[**getIssuesecuritylevel**](DefaultApi.md#getIssuesecuritylevel) | **GET** /api/2/securitylevel/{id} | 
[**getNotificationSchemes**](DefaultApi.md#getNotificationSchemes) | **GET** /api/2/notificationscheme | 
[**getPasswordPolicy**](DefaultApi.md#getPasswordPolicy) | **GET** /api/2/password/policy | 
[**getPermissionScheme**](DefaultApi.md#getPermissionScheme) | **GET** /api/2/permissionscheme/{schemeId} | 
[**getPermissionSchemeGrant**](DefaultApi.md#getPermissionSchemeGrant) | **GET** /api/2/permissionscheme/{schemeId}/permission/{permissionId} | 
[**getPermissionSchemeGrants**](DefaultApi.md#getPermissionSchemeGrants) | **GET** /api/2/permissionscheme/{schemeId}/permission | 
[**getPermissionSchemes**](DefaultApi.md#getPermissionSchemes) | **GET** /api/2/permissionscheme | 
[**getPermissions**](DefaultApi.md#getPermissions) | **GET** /api/2/mypermissions | 
[**getPreference**](DefaultApi.md#getPreference) | **GET** /api/2/mypreferences | 
[**getPriorities**](DefaultApi.md#getPriorities) | **GET** /api/2/priority | 
[**getPriority**](DefaultApi.md#getPriority) | **GET** /api/2/priority/{id} | 
[**getProgress**](DefaultApi.md#getProgress) | **GET** /api/2/reindex/request/{requestId} | 
[**getProgressBulk**](DefaultApi.md#getProgressBulk) | **GET** /api/2/reindex/request/bulk | 
[**getProjectCategoryById**](DefaultApi.md#getProjectCategoryById) | **GET** /api/2/projectCategory/{id} | 
[**getProjectComponents**](DefaultApi.md#getProjectComponents) | **GET** /api/2/project/{projectIdOrKey}/components | 
[**getProjectRole**](DefaultApi.md#getProjectRole) | **GET** /api/2/project/{projectIdOrKey}/role/{id} | 
[**getProjectRoleActorsForRole**](DefaultApi.md#getProjectRoleActorsForRole) | **GET** /api/2/role/{id}/actors | 
[**getProjectRolesById**](DefaultApi.md#getProjectRolesById) | **GET** /api/2/role/{id} | 
[**getProjectTypeByKey**](DefaultApi.md#getProjectTypeByKey) | **GET** /api/2/project/type/{projectTypeKey} | 
[**getProjectVersions**](DefaultApi.md#getProjectVersions) | **GET** /api/2/project/{projectIdOrKey}/versions | 
[**getProjectVersionsPaginated**](DefaultApi.md#getProjectVersionsPaginated) | **GET** /api/2/project/{projectIdOrKey}/version | 
[**getProperties**](DefaultApi.md#getProperties) | **GET** /api/2/workflow/api/2/transitions/{id}/properties | 
[**getPropertyKeys**](DefaultApi.md#getPropertyKeys) | **GET** /api/2/issuetype/{issueTypeId}/properties | 
[**getRecords**](DefaultApi.md#getRecords) | **GET** /api/2/auditing/record | 
[**getReindexInfo**](DefaultApi.md#getReindexInfo) | **GET** /api/2/reindex | 
[**getReindexProgress**](DefaultApi.md#getReindexProgress) | **GET** /api/2/reindex/progress | 
[**getRemoteIssueLinkById**](DefaultApi.md#getRemoteIssueLinkById) | **GET** /api/2/issue/{issueIdOrKey}/remotelink/{linkId} | 
[**getRemoteIssueLinks**](DefaultApi.md#getRemoteIssueLinks) | **GET** /api/2/issue/{issueIdOrKey}/remotelink | 
[**getRemoteVersionLink**](DefaultApi.md#getRemoteVersionLink) | **GET** /api/2/version/{versionId}/remotelink/{globalId} | 
[**getRemoteVersionLinks**](DefaultApi.md#getRemoteVersionLinks) | **GET** /api/2/version/remotelink | 
[**getRemoteVersionLinksByVersionId**](DefaultApi.md#getRemoteVersionLinksByVersionId) | **GET** /api/2/version/{versionId}/remotelink | 
[**getResolution**](DefaultApi.md#getResolution) | **GET** /api/2/resolution/{id} | 
[**getResolutions**](DefaultApi.md#getResolutions) | **GET** /api/2/resolution | 
[**getSchemeAttribute**](DefaultApi.md#getSchemeAttribute) | **GET** /api/2/permissionscheme/{permissionSchemeId}/attribute/{attributeKey} | 
[**getSecurityLevelsForProject**](DefaultApi.md#getSecurityLevelsForProject) | **GET** /api/2/project/{projectKeyOrId}/securitylevel | 
[**getServerInfo**](DefaultApi.md#getServerInfo) | **GET** /api/2/serverInfo | 
[**getSharePermission**](DefaultApi.md#getSharePermission) | **GET** /api/2/filter/{id}/permission/{permissionId} | 
[**getSharePermissions**](DefaultApi.md#getSharePermissions) | **GET** /api/2/filter/{id}/permission | 
[**getState**](DefaultApi.md#getState) | **GET** /api/2/cluster/zdu/state | 
[**getStatus**](DefaultApi.md#getStatus) | **GET** /api/2/status/{idOrName} | 
[**getStatusCategories**](DefaultApi.md#getStatusCategories) | **GET** /api/2/statuscategory | 
[**getStatusCategory**](DefaultApi.md#getStatusCategory) | **GET** /api/2/statuscategory/{idOrKey} | 
[**getStatuses**](DefaultApi.md#getStatuses) | **GET** /api/2/status | 
[**getSubTasks**](DefaultApi.md#getSubTasks) | **GET** /api/2/issue/{issueIdOrKey}/subtask | 
[**getTransitions**](DefaultApi.md#getTransitions) | **GET** /api/2/issue/{issueIdOrKey}/transitions | 
[**getUpgradeResult**](DefaultApi.md#getUpgradeResult) | **GET** /api/2/upgrade | 
[**getUsersFromGroup**](DefaultApi.md#getUsersFromGroup) | **GET** /api/2/group/member | 
[**getVersion**](DefaultApi.md#getVersion) | **GET** /api/2/version/{id} | 
[**getVersionRelatedIssues**](DefaultApi.md#getVersionRelatedIssues) | **GET** /api/2/version/{id}/relatedIssueCounts | 
[**getVersionUnresolvedIssues**](DefaultApi.md#getVersionUnresolvedIssues) | **GET** /api/2/version/{id}/unresolvedIssueCount | 
[**getVotes**](DefaultApi.md#getVotes) | **GET** /api/2/issue/{issueIdOrKey}/votes | 
[**getWorkflow**](DefaultApi.md#getWorkflow) | **GET** /api/2/workflowscheme/{id}/workflow | 
[**getWorklog**](DefaultApi.md#getWorklog) | **GET** /api/2/issue/{issueIdOrKey}/worklog/{id} | 
[**getWorklogsForIds**](DefaultApi.md#getWorklogsForIds) | **POST** /api/2/worklog/list | 
[**linkIssues**](DefaultApi.md#linkIssues) | **POST** /api/2/issueLink | 
[**list**](DefaultApi.md#list) | **GET** /api/2/dashboard | 
[**login**](DefaultApi.md#login) | **POST** /auth/1/session | 
[**logout**](DefaultApi.md#logout) | **DELETE** /auth/1/session | 
[**merge**](DefaultApi.md#merge) | **PUT** /api/2/version/{id}/mergeto/{moveIssuesTo} | 
[**moveField**](DefaultApi.md#moveField) | **POST** /api/2/screens/{screenId}/tabs/{tabId}/fields/{id}/move | 
[**moveSubTasks**](DefaultApi.md#moveSubTasks) | **POST** /api/2/issue/{issueIdOrKey}/subtask/move | 
[**moveTab**](DefaultApi.md#moveTab) | **POST** /api/2/screens/{screenId}/tabs/{tabId}/move/{pos} | 
[**moveVersion**](DefaultApi.md#moveVersion) | **POST** /api/2/version/{id}/move | 
[**notify**](DefaultApi.md#notify) | **POST** /api/2/issue/{issueIdOrKey}/notify | 
[**partialUpdateProjectRole**](DefaultApi.md#partialUpdateProjectRole) | **POST** /api/2/role/{id} | 
[**policyCheckCreateUser**](DefaultApi.md#policyCheckCreateUser) | **POST** /api/2/password/policy/createUser | 
[**policyCheckUpdateUser**](DefaultApi.md#policyCheckUpdateUser) | **POST** /api/2/password/policy/updateUser | 
[**processRequests**](DefaultApi.md#processRequests) | **POST** /api/2/reindex/request | 
[**put**](DefaultApi.md#put) | **PUT** /api/2/applicationrole/{key} | 
[**putBulk**](DefaultApi.md#putBulk) | **PUT** /api/2/applicationrole | 
[**reindex**](DefaultApi.md#reindex) | **POST** /api/2/reindex | 
[**reindexIssues**](DefaultApi.md#reindexIssues) | **POST** /api/2/reindex/issue | 
[**release**](DefaultApi.md#release) | **DELETE** /auth/1/websudo | 
[**removeAttachment**](DefaultApi.md#removeAttachment) | **DELETE** /api/2/attachment/{id} | 
[**removeField**](DefaultApi.md#removeField) | **DELETE** /api/2/screens/{screenId}/tabs/{tabId}/fields/{id} | 
[**removeGroup**](DefaultApi.md#removeGroup) | **DELETE** /api/2/group | 
[**removePreference**](DefaultApi.md#removePreference) | **DELETE** /api/2/mypreferences | 
[**removeProjectCategory**](DefaultApi.md#removeProjectCategory) | **DELETE** /api/2/projectCategory/{id} | 
[**removeUser**](DefaultApi.md#removeUser) | **DELETE** /api/2/user | 
[**removeUserFromApplication**](DefaultApi.md#removeUserFromApplication) | **DELETE** /api/2/user/application | 
[**removeUserFromGroup**](DefaultApi.md#removeUserFromGroup) | **DELETE** /api/2/group/user | 
[**removeVote**](DefaultApi.md#removeVote) | **DELETE** /api/2/issue/{issueIdOrKey}/votes | 
[**removeWatcher**](DefaultApi.md#removeWatcher) | **DELETE** /api/2/issue/{issueIdOrKey}/watchers | 
[**renameTab**](DefaultApi.md#renameTab) | **PUT** /api/2/screens/{screenId}/tabs/{tabId} | 
[**runUpgradesNow**](DefaultApi.md#runUpgradesNow) | **POST** /api/2/upgrade | 
[**search**](DefaultApi.md#search) | **GET** /api/2/search | 
[**searchUsingSearchRequest**](DefaultApi.md#searchUsingSearchRequest) | **POST** /api/2/search | 
[**setActors**](DefaultApi.md#setActors) | **PUT** /api/2/project/{projectIdOrKey}/role/{id} | 
[**setBaseURL**](DefaultApi.md#setBaseURL) | **PUT** /api/2/settings/baseUrl | 
[**setDefaultShareScope**](DefaultApi.md#setDefaultShareScope) | **PUT** /api/2/filter/defaultShareScope | 
[**setDraftIssueType**](DefaultApi.md#setDraftIssueType) | **PUT** /api/2/workflowscheme/{id}/draft/issuetype/{issueType} | 
[**setIssueNavigatorDefaultColumns**](DefaultApi.md#setIssueNavigatorDefaultColumns) | **PUT** /api/2/settings/columns | 
[**setIssueType**](DefaultApi.md#setIssueType) | **PUT** /api/2/workflowscheme/{id}/issuetype/{issueType} | 
[**setPreference**](DefaultApi.md#setPreference) | **PUT** /api/2/mypreferences | 
[**setPropertyViaRestfulTable**](DefaultApi.md#setPropertyViaRestfulTable) | **PUT** /api/2/application-properties/{id} | 
[**setReadyToUpgrade**](DefaultApi.md#setReadyToUpgrade) | **POST** /api/2/cluster/zdu/start | 
[**setSchemeAttribute**](DefaultApi.md#setSchemeAttribute) | **PUT** /api/2/permissionscheme/{permissionSchemeId}/attribute/{key} | 
[**start**](DefaultApi.md#start) | **GET** /api/2/monitoring/jmx/startExposing | 
[**stop**](DefaultApi.md#stop) | **GET** /api/2/monitoring/jmx/stopExposing | 
[**storeTemporaryAvatar**](DefaultApi.md#storeTemporaryAvatar) | **POST** /api/2/avatar/{type}/temporary | 
[**update**](DefaultApi.md#update) | **PUT** /api/2/workflowscheme/{id} | 
[**updateComment**](DefaultApi.md#updateComment) | **PUT** /api/2/issue/{issueIdOrKey}/comment/{id} | 
[**updateComponent**](DefaultApi.md#updateComponent) | **PUT** /api/2/component/{id} | 
[**updateDefault**](DefaultApi.md#updateDefault) | **PUT** /api/2/workflowscheme/{id}/default | 
[**updateDraft**](DefaultApi.md#updateDraft) | **PUT** /api/2/workflowscheme/{id}/draft | 
[**updateDraftDefault**](DefaultApi.md#updateDraftDefault) | **PUT** /api/2/workflowscheme/{id}/draft/default | 
[**updateDraftWorkflowMapping**](DefaultApi.md#updateDraftWorkflowMapping) | **PUT** /api/2/workflowscheme/{id}/draft/workflow | 
[**updateIssueLinkType**](DefaultApi.md#updateIssueLinkType) | **PUT** /api/2/issueLinkType/{issueLinkTypeId} | 
[**updateIssueType**](DefaultApi.md#updateIssueType) | **PUT** /api/2/issuetype/{id} | 
[**updatePermissionScheme**](DefaultApi.md#updatePermissionScheme) | **PUT** /api/2/permissionscheme/{schemeId} | 
[**updateProject**](DefaultApi.md#updateProject) | **PUT** /api/2/project/{projectIdOrKey} | 
[**updateProjectCategory**](DefaultApi.md#updateProjectCategory) | **PUT** /api/2/projectCategory/{id} | 
[**updateProjectType**](DefaultApi.md#updateProjectType) | **PUT** /api/2/project/{projectIdOrKey}/type/{newProjectTypeKey} | 
[**updateProperty**](DefaultApi.md#updateProperty) | **PUT** /api/2/workflow/api/2/transitions/{id}/properties | 
[**updateRemoteIssueLink**](DefaultApi.md#updateRemoteIssueLink) | **PUT** /api/2/issue/{issueIdOrKey}/remotelink/{linkId} | 
[**updateVersion**](DefaultApi.md#updateVersion) | **PUT** /api/2/version/{id} | 
[**updateWorkflowMapping**](DefaultApi.md#updateWorkflowMapping) | **PUT** /api/2/workflowscheme/{id}/workflow | 
[**updateWorklog**](DefaultApi.md#updateWorklog) | **PUT** /api/2/issue/{issueIdOrKey}/worklog/{id} | 
[**validate**](DefaultApi.md#validate) | **POST** /api/2/licenseValidator | 



## acknowledgeErrors

> acknowledgeErrors()



### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.acknowledgeErrors((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## addActorUsers

> addActorUsers(projectIdOrKey, id)



Adds an actor (user or group) to a project role.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
let id = 789; // Number | the project role id
apiInstance.addActorUsers(projectIdOrKey, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| the project id or project key | 
 **id** | **Number**| the project role id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addAttachment

> addAttachment(issueIdOrKey)



Add one or more attachments to an issue.  &lt;p&gt;  This resource expects a multipart post. The media-type multipart/form-data is defined in RFC 1867. Most client  libraries have classes that make dealing with multipart posts simple. For instance, in Java the Apache HTTP Components  library provides a  &lt;a href&#x3D;\&quot;http://hc.apache.org/httpcomponents-client-ga/httpmime/apidocs/org/apache/http/entity/mime/MultipartEntity.html\&quot;&gt;MultiPartEntity&lt;/a&gt;  that makes it simple to submit a multipart POST.  &lt;p&gt;  In order to protect against XSRF attacks, because this method accepts multipart/form-data, it has XSRF protection  on it.  This means you must submit a header of X-Atlassian-Token: no-check with the request, otherwise it will be  blocked.  &lt;p&gt;  The name of the multipart/form-data parameter that contains attachments must be \&quot;file\&quot;  &lt;p&gt;  A simple example to upload a file called \&quot;myfile.txt\&quot; to issue REST-123:  &lt;pre&gt;curl -D- -u admin:admin -X POST -H \&quot;X-Atlassian-Token: no-check\&quot; -F \&quot;file&#x3D;@myfile.txt\&quot; http://myhost/rest/api/2/issue/TEST-123/attachments&lt;/pre&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue that you want to add the attachments to
apiInstance.addAttachment(issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| the issue that you want to add the attachments to | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addComment

> addComment(issueIdOrKey, opts)



Adds a new comment to an issue.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | a string containing the issue id or key the comment will be added to
let opts = {
  'expand': "expand_example" // String | optional flags: renderedBody (provides body rendered in HTML)
};
apiInstance.addComment(issueIdOrKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| a string containing the issue id or key the comment will be added to | 
 **expand** | **String**| optional flags: renderedBody (provides body rendered in HTML) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addField

> addField(screenId, tabId)



Adds field to the given tab.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let screenId = 789; // Number | id of screen
let tabId = 789; // Number | id of tab
apiInstance.addField(screenId, tabId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screenId** | **Number**| id of screen | 
 **tabId** | **Number**| id of tab | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addFieldToDefaultScreen

> addFieldToDefaultScreen(fieldId)



Adds field or custom field to the default tab

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let fieldId = "fieldId_example"; // String | id of field / custom field
apiInstance.addFieldToDefaultScreen(fieldId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fieldId** | **String**| id of field / custom field | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addProjectRoleActorsToRole

> addProjectRoleActorsToRole(id)



Adds default actors to the given role. The request data should contain a list of usernames or a list of groups to add.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the role id to remove the actors from
apiInstance.addProjectRoleActorsToRole(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the role id to remove the actors from | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addRecord

> addRecord()



Store a record in Audit Log

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.addRecord((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## addSharePermission

> addSharePermission(id)



Adds a share permissions to the given filter. Adding a global permission removes all previous permissions from the filter.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | 
apiInstance.addSharePermission(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addTab

> addTab(screenId)



Creates tab for given screen

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let screenId = 789; // Number | id of screen
apiInstance.addTab(screenId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screenId** | **Number**| id of screen | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addUserToApplication

> addUserToApplication(opts)



Add user to given application. Admin permission will be required to perform this operation.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'username': "username_example", // String | username
  'applicationKey': "applicationKey_example" // String | application key
};
apiInstance.addUserToApplication(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| username | [optional] 
 **applicationKey** | **String**| application key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addUserToGroup

> addUserToGroup(opts)



Adds given user to a group.  &lt;p&gt;  Returns the current state of the group.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'groupname': "groupname_example" // String | A name of requested group.
};
apiInstance.addUserToGroup(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupname** | **String**| A name of requested group. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addVote

> addVote(issueIdOrKey)



Cast your vote in favour of an issue.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue to view voting information for
apiInstance.addVote(issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| the issue to view voting information for | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addWatcher

> addWatcher(issueIdOrKey)



Adds a user to an issue&#39;s watcher list.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | a String containing an issue key.
apiInstance.addWatcher(issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| a String containing an issue key. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addWorklog

> addWorklog(issueIdOrKey, opts)



Adds a new worklog entry to an issue.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | a string containing the issue id or key the worklog will be added to
let opts = {
  'adjustEstimate': "adjustEstimate_example", // String | (optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are                        <ul>                        <li>\"new\" - sets the estimate to a specific value</li>                        <li>\"leave\"- leaves the estimate as is</li>                        <li>\"manual\" - specify a specific amount to increase remaining estimate by</li>                        <li>\"auto\"- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog</li> </ul>
  'newEstimate': "newEstimate_example", // String | (required when \"new\" is selected for adjustEstimate) the new value for the remaining estimate field. e.g. \"2d\"
  'reduceBy': "reduceBy_example" // String | (required when \"manual\" is selected for adjustEstimate) the amount to reduce the remaining estimate by e.g. \"2d\"
};
apiInstance.addWorklog(issueIdOrKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| a string containing the issue id or key the worklog will be added to | 
 **adjustEstimate** | **String**| (optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are                        &lt;ul&gt;                        &lt;li&gt;\&quot;new\&quot; - sets the estimate to a specific value&lt;/li&gt;                        &lt;li&gt;\&quot;leave\&quot;- leaves the estimate as is&lt;/li&gt;                        &lt;li&gt;\&quot;manual\&quot; - specify a specific amount to increase remaining estimate by&lt;/li&gt;                        &lt;li&gt;\&quot;auto\&quot;- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog&lt;/li&gt; &lt;/ul&gt; | [optional] 
 **newEstimate** | **String**| (required when \&quot;new\&quot; is selected for adjustEstimate) the new value for the remaining estimate field. e.g. \&quot;2d\&quot; | [optional] 
 **reduceBy** | **String**| (required when \&quot;manual\&quot; is selected for adjustEstimate) the amount to reduce the remaining estimate by e.g. \&quot;2d\&quot; | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2ApplicationPropertiesGet

> api2ApplicationPropertiesGet(opts)



Returns an application property.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'key': "key_example", // String | a String containing the property key
  'permissionLevel': "permissionLevel_example", // String | when fetching a list specifies the permission level of all items in the list                         see {@link com.atlassian.jira.bc.admin.ApplicationPropertiesService.EditPermissionLevel}
  'keyFilter': "keyFilter_example" // String | when fetching a list allows the list to be filtered by the property's start of key                         e.g. \"jira.lf.*\" whould fetch only those permissions that are editable and whose keys start with                         \"jira.lf.\". This is a regex.
};
apiInstance.api2ApplicationPropertiesGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| a String containing the property key | [optional] 
 **permissionLevel** | **String**| when fetching a list specifies the permission level of all items in the list                         see {@link com.atlassian.jira.bc.admin.ApplicationPropertiesService.EditPermissionLevel} | [optional] 
 **keyFilter** | **String**| when fetching a list allows the list to be filtered by the property&#39;s start of key                         e.g. \&quot;jira.lf.*\&quot; whould fetch only those permissions that are editable and whose keys start with                         \&quot;jira.lf.\&quot;. This is a regex. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2AvatarTypeTemporaryCropPost

> api2AvatarTypeTemporaryCropPost(type)



Updates the cropping instructions of the temporary avatar.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let type = "type_example"; // String | the avatar type
apiInstance.api2AvatarTypeTemporaryCropPost(type, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **String**| the avatar type | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2CommentCommentIdPropertiesGet

> api2CommentCommentIdPropertiesGet(commentId)



Returns the keys of all properties for the comment identified by the key or by the id.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let commentId = "commentId_example"; // String | the comment from which keys will be returned.
apiInstance.api2CommentCommentIdPropertiesGet(commentId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commentId** | **String**| the comment from which keys will be returned. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2CommentCommentIdPropertiesPropertyKeyDelete

> api2CommentCommentIdPropertiesPropertyKeyDelete(commentId, propertyKey)



Removes the property from the comment identified by the key or by the id. Ths user removing the property is required  to have permissions to administer the comment.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let commentId = "commentId_example"; // String | the comment from which keys will be returned.
let propertyKey = "propertyKey_example"; // String | the key of the property to return.
apiInstance.api2CommentCommentIdPropertiesPropertyKeyDelete(commentId, propertyKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commentId** | **String**| the comment from which keys will be returned. | 
 **propertyKey** | **String**| the key of the property to return. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2CommentCommentIdPropertiesPropertyKeyGet

> api2CommentCommentIdPropertiesPropertyKeyGet(commentId, propertyKey)



Returns the value of the property with a given key from the comment identified by the key or by the id. The user who retrieves  the property is required to have permissions to read the comment.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let commentId = "commentId_example"; // String | the comment from which keys will be returned.
let propertyKey = "propertyKey_example"; // String | the key of the property to return.
apiInstance.api2CommentCommentIdPropertiesPropertyKeyGet(commentId, propertyKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commentId** | **String**| the comment from which keys will be returned. | 
 **propertyKey** | **String**| the key of the property to return. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2CommentCommentIdPropertiesPropertyKeyPut

> api2CommentCommentIdPropertiesPropertyKeyPut(commentId, propertyKey)



Sets the value of the specified comment&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against the comment identified by the key or by the id. The user  who stores the data is required to have permissions to administer the comment.  &lt;/p&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let commentId = "commentId_example"; // String | the comment from which keys will be returned.
let propertyKey = "propertyKey_example"; // String | the key of the property to return.
apiInstance.api2CommentCommentIdPropertiesPropertyKeyPut(commentId, propertyKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commentId** | **String**| the comment from which keys will be returned. | 
 **propertyKey** | **String**| the key of the property to return. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2ComponentIdDelete

> api2ComponentIdDelete(id, opts)



Delete a project component.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | The component to delete.
let opts = {
  'moveIssuesTo': "moveIssuesTo_example" // String | The new component applied to issues whose 'id' component will be deleted.                      If this value is null, then the 'id' component is simply removed from the related isues.
};
apiInstance.api2ComponentIdDelete(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The component to delete. | 
 **moveIssuesTo** | **String**| The new component applied to issues whose &#39;id&#39; component will be deleted.                      If this value is null, then the &#39;id&#39; component is simply removed from the related isues. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2DashboardDashboardIdItemsItemIdPropertiesGet

> api2DashboardDashboardIdItemsItemIdPropertiesGet(itemId, dashboardId)



Returns the keys of all properties for the dashboard item identified by the id.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let itemId = "itemId_example"; // String | the dashboard item from which keys will be returned.
let dashboardId = "dashboardId_example"; // String | 
apiInstance.api2DashboardDashboardIdItemsItemIdPropertiesGet(itemId, dashboardId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemId** | **String**| the dashboard item from which keys will be returned. | 
 **dashboardId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyDelete

> api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyDelete(itemId, dashboardId, propertyKey)



Removes the property from the dashboard item identified by the key or by the id. Ths user removing the property is required  to have permissions to administer the dashboard item.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let itemId = "itemId_example"; // String | the dashboard item from which keys will be returned.
let dashboardId = "dashboardId_example"; // String | 
let propertyKey = "propertyKey_example"; // String | the key of the property to return.
apiInstance.api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyDelete(itemId, dashboardId, propertyKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemId** | **String**| the dashboard item from which keys will be returned. | 
 **dashboardId** | **String**|  | 
 **propertyKey** | **String**| the key of the property to return. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyGet

> api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyGet(itemId, dashboardId, propertyKey)



Returns the value of the property with a given key from the dashboard item identified by the id.  The user who retrieves the property is required to have permissions to read the dashboard item.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let itemId = "itemId_example"; // String | the dashboard item from which keys will be returned.
let dashboardId = "dashboardId_example"; // String | 
let propertyKey = "propertyKey_example"; // String | the key of the property to return.
apiInstance.api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyGet(itemId, dashboardId, propertyKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemId** | **String**| the dashboard item from which keys will be returned. | 
 **dashboardId** | **String**|  | 
 **propertyKey** | **String**| the key of the property to return. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyPut

> api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyPut(itemId, dashboardId, propertyKey)



Sets the value of the specified dashboard item&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against the dashboard item identified by the id.  The user who stores the data is required to have permissions to administer the dashboard item.  &lt;/p&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let itemId = "itemId_example"; // String | the dashboard item from which keys will be returned.
let dashboardId = "dashboardId_example"; // String | 
let propertyKey = "propertyKey_example"; // String | the key of the property to return.
apiInstance.api2DashboardDashboardIdItemsItemIdPropertiesPropertyKeyPut(itemId, dashboardId, propertyKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemId** | **String**| the dashboard item from which keys will be returned. | 
 **dashboardId** | **String**|  | 
 **propertyKey** | **String**| the key of the property to return. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2FilterIdColumnsDelete

> api2FilterIdColumnsDelete(id)



Resets the columns for the given filter such that the filter no longer has its own column config.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | id of the filter
apiInstance.api2FilterIdColumnsDelete(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| id of the filter | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2FilterIdColumnsGet

> api2FilterIdColumnsGet(id)



Returns the default columns for the given filter. Currently logged in user will be used as  the user making such request.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | id of the filter
apiInstance.api2FilterIdColumnsGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| id of the filter | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2FilterIdColumnsPut

> api2FilterIdColumnsPut(id)



Sets the default columns for the given filter.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | id of the filter
apiInstance.api2FilterIdColumnsPut(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| id of the filter | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2IssueIssueIdOrKeyPropertiesGet

> api2IssueIssueIdOrKeyPropertiesGet(issueIdOrKey)



Returns the keys of all properties for the issue identified by the key or by the id.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue from which keys will be returned.
apiInstance.api2IssueIssueIdOrKeyPropertiesGet(issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| the issue from which keys will be returned. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2IssueIssueIdOrKeyPropertiesPropertyKeyDelete

> api2IssueIssueIdOrKeyPropertiesPropertyKeyDelete(issueIdOrKey, propertyKey)



Removes the property from the issue identified by the key or by the id. Ths user removing the property is required  to have permissions to edit the issue.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue from which keys will be returned.
let propertyKey = "propertyKey_example"; // String | the key of the property to return.
apiInstance.api2IssueIssueIdOrKeyPropertiesPropertyKeyDelete(issueIdOrKey, propertyKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| the issue from which keys will be returned. | 
 **propertyKey** | **String**| the key of the property to return. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2IssueIssueIdOrKeyPropertiesPropertyKeyGet

> api2IssueIssueIdOrKeyPropertiesPropertyKeyGet(issueIdOrKey, propertyKey)



Returns the value of the property with a given key from the issue identified by the key or by the id. The user who retrieves  the property is required to have permissions to read the issue.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue from which keys will be returned.
let propertyKey = "propertyKey_example"; // String | the key of the property to return.
apiInstance.api2IssueIssueIdOrKeyPropertiesPropertyKeyGet(issueIdOrKey, propertyKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| the issue from which keys will be returned. | 
 **propertyKey** | **String**| the key of the property to return. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2IssueIssueIdOrKeyPropertiesPropertyKeyPut

> api2IssueIssueIdOrKeyPropertiesPropertyKeyPut(issueIdOrKey, propertyKey)



Sets the value of the specified issue&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against the issue identified by the key or by the id. The user  who stores the data is required to have permissions to edit the issue.  &lt;/p&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue from which keys will be returned.
let propertyKey = "propertyKey_example"; // String | the key of the property to return.
apiInstance.api2IssueIssueIdOrKeyPropertiesPropertyKeyPut(issueIdOrKey, propertyKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| the issue from which keys will be returned. | 
 **propertyKey** | **String**| the key of the property to return. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2IssuesecurityschemesIdGet

> api2IssuesecurityschemesIdGet(id)



Returns the issue security scheme along with that are defined.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | 
apiInstance.api2IssuesecurityschemesIdGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2IssuetypeIdAvatarPost

> api2IssuetypeIdAvatarPost(id)



Converts temporary avatar into a real avatar

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | the id of the issue type, which avatar is updated.
apiInstance.api2IssuetypeIdAvatarPost(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| the id of the issue type, which avatar is updated. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2IssuetypeIdAvatarTemporaryPost

> api2IssuetypeIdAvatarTemporaryPost(id)



Creates temporary avatar using multipart. The response is sent back as JSON stored in a textarea. This is because  the client uses remote iframing to submit avatars using multipart. So we must send them a valid HTML page back from  which the client parses the JSON from.  &lt;p&gt;  Creating a temporary avatar is part of a 3-step process in uploading a new  avatar for an issue type: upload, crop, confirm. This endpoint allows you to use a multipart upload  instead of sending the image directly as the request body.  &lt;/p&gt;  &lt;p&gt;  You *must* use \&quot;avatar\&quot; as the name of the upload parameter:&lt;/p&gt;  &lt;p&gt;  &lt;pre&gt;  curl -c cookiejar.txt -X POST -u admin:admin -H \&quot;X-Atlassian-Token: no-check\&quot; \\    -F \&quot;avatar&#x3D;@mynewavatar.png;type&#x3D;image/png\&quot; \\    &#39;http://localhost:8090/jira/rest/api/2/issuetype/1/avatar/temporary&#39;  &lt;/pre&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | the id of the issue type, which avatar is updated.
apiInstance.api2IssuetypeIdAvatarTemporaryPost(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| the id of the issue type, which avatar is updated. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2IssuetypeIdDelete

> api2IssuetypeIdDelete(id, opts)



Deletes the specified issue type. If the issue type has any associated issues, these issues will be migrated to  the alternative issue type specified in the parameter. You can determine the alternative issue types by calling  the &lt;b&gt;/rest/api/2/issuetype/{id}/alternatives&lt;/b&gt; resource.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | the id of the issue type to update.
let opts = {
  'alternativeIssueTypeId': "alternativeIssueTypeId_example" // String | the id of an issue type to which issues associated with the removed issue type will be migrated.
};
apiInstance.api2IssuetypeIdDelete(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| the id of the issue type to update. | 
 **alternativeIssueTypeId** | **String**| the id of an issue type to which issues associated with the removed issue type will be migrated. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2IssuetypeIdGet

> api2IssuetypeIdGet(id)



Returns a full representation of the issue type that has the given id.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | the id of the issue type to update.
apiInstance.api2IssuetypeIdGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| the id of the issue type to update. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2IssuetypeIssueTypeIdPropertiesPropertyKeyDelete

> api2IssuetypeIssueTypeIdPropertiesPropertyKeyDelete(issueTypeId, propertyKey)



Removes the property from the issue type identified by the id. Ths user removing the property is required  to have permissions to edit the issue type.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueTypeId = "issueTypeId_example"; // String | the issue type from which the keys will be returned
let propertyKey = "propertyKey_example"; // String | the key of the property to return
apiInstance.api2IssuetypeIssueTypeIdPropertiesPropertyKeyDelete(issueTypeId, propertyKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueTypeId** | **String**| the issue type from which the keys will be returned | 
 **propertyKey** | **String**| the key of the property to return | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2IssuetypeIssueTypeIdPropertiesPropertyKeyGet

> api2IssuetypeIssueTypeIdPropertiesPropertyKeyGet(issueTypeId, propertyKey)



Returns the value of the property with a given key from the issue type identified by the id. The user who retrieves  the property is required to have permissions to view the issue type.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueTypeId = "issueTypeId_example"; // String | the issue type from which the keys will be returned
let propertyKey = "propertyKey_example"; // String | the key of the property to return
apiInstance.api2IssuetypeIssueTypeIdPropertiesPropertyKeyGet(issueTypeId, propertyKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueTypeId** | **String**| the issue type from which the keys will be returned | 
 **propertyKey** | **String**| the key of the property to return | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2IssuetypeIssueTypeIdPropertiesPropertyKeyPut

> api2IssuetypeIssueTypeIdPropertiesPropertyKeyPut(issueTypeId, propertyKey)



Sets the value of the specified issue type&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against an issue type identified by the id. The user  who stores the data is required to have permissions to edit an issue type.  &lt;/p&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueTypeId = "issueTypeId_example"; // String | the issue type from which the keys will be returned
let propertyKey = "propertyKey_example"; // String | the key of the property to return
apiInstance.api2IssuetypeIssueTypeIdPropertiesPropertyKeyPut(issueTypeId, propertyKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueTypeId** | **String**| the issue type from which the keys will be returned | 
 **propertyKey** | **String**| the key of the property to return | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2MyselfGet

> api2MyselfGet()



Returns currently logged user. This resource cannot be accessed anonymously.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.api2MyselfGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## api2MyselfPut

> api2MyselfPut()



Modify currently logged user. The \&quot;value\&quot; fields present will override the existing value.  Fields skipped in request will not be changed. Only email and display name can be change that way.  Requires user password.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.api2MyselfPut((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## api2NotificationschemeIdGet

> api2NotificationschemeIdGet(id, opts)



Returns a full representation of the notification scheme for the given id. This resource will return a  notification scheme containing a list of events and recipient configured to receive notifications for these events. Consumer  should allow events without recipients to appear in response. User accessing  the data is required to have permissions to administer at least one project associated with the requested notification scheme.  &lt;p&gt;  Notification recipients can be:  &lt;ul&gt;  &lt;li&gt;current assignee - the value of the notificationType is CurrentAssignee&lt;/li&gt;  &lt;li&gt;issue reporter - the value of the notificationType is Reporter&lt;/li&gt;  &lt;li&gt;current user - the value of the notificationType is CurrentUser&lt;/li&gt;  &lt;li&gt;project lead - the value of the notificationType is ProjectLead&lt;/li&gt;  &lt;li&gt;component lead - the value of the notificationType is ComponentLead&lt;/li&gt;  &lt;li&gt;all watchers - the value of the notification type is AllWatchers&lt;/li&gt;  &lt;li&gt;configured user - the value of the notification type is User. Parameter will contain key of the user. Information about the user will be provided  if &lt;b&gt;user&lt;/b&gt; expand parameter is used. &lt;/li&gt;  &lt;li&gt;configured group - the value of the notification type is Group. Parameter will contain name of the group. Information about the group will be provided  if &lt;b&gt;group&lt;/b&gt; expand parameter is used. &lt;/li&gt;  &lt;li&gt;configured email address - the value of the notification type is EmailAddress, additionally information about the email will be provided.&lt;/li&gt;  &lt;li&gt;users or users in groups in the configured custom fields - the value of the notification type is UserCustomField or GroupCustomField. Parameter  will contain id of the custom field. Information about the field will be provided if &lt;b&gt;field&lt;/b&gt; expand parameter is used. &lt;/li&gt;  &lt;li&gt;configured project role - the value of the notification type is ProjectRole. Parameter will contain project role id. Information about the project role  will be provided if &lt;b&gt;projectRole&lt;/b&gt; expand parameter is used. &lt;/li&gt;  &lt;/ul&gt;  Please see the example for reference.  &lt;/p&gt;  The events can be JIRA system events or events configured by administrator. In case of the system events, data about theirs  ids, names and descriptions is provided. In case of custom events, the template event is included as well.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | an id of the notification scheme to retrieve
let opts = {
  'expand': "expand_example" // String | 
};
apiInstance.api2NotificationschemeIdGet(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| an id of the notification scheme to retrieve | 
 **expand** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2ProjectProjectIdOrKeyAvatarIdDelete

> api2ProjectProjectIdOrKeyAvatarIdDelete(projectIdOrKey, id)



Deletes avatar

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | Project id or project key
let id = 789; // Number | database id for avatar
apiInstance.api2ProjectProjectIdOrKeyAvatarIdDelete(projectIdOrKey, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| Project id or project key | 
 **id** | **Number**| database id for avatar | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2ProjectProjectIdOrKeyAvatarPost

> api2ProjectProjectIdOrKeyAvatarPost(projectIdOrKey)



Converts temporary avatar into a real avatar

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | 
apiInstance.api2ProjectProjectIdOrKeyAvatarPost(projectIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2ProjectProjectIdOrKeyAvatarPut

> api2ProjectProjectIdOrKeyAvatarPut(projectIdOrKey)



### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | 
apiInstance.api2ProjectProjectIdOrKeyAvatarPut(projectIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2ProjectProjectIdOrKeyAvatarTemporaryPost

> api2ProjectProjectIdOrKeyAvatarTemporaryPost(projectIdOrKey)



Creates temporary avatar using multipart. The response is sent back as JSON stored in a textarea. This is because  the client uses remote iframing to submit avatars using multipart. So we must send them a valid HTML page back from  which the client parses the JSON.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | Project id or project key
apiInstance.api2ProjectProjectIdOrKeyAvatarTemporaryPost(projectIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| Project id or project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2ProjectProjectIdOrKeyAvatarsGet

> api2ProjectProjectIdOrKeyAvatarsGet(projectIdOrKey)



Returns all avatars which are visible for the currently logged in user.  The avatars are grouped into  system and custom.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | project id or project key
apiInstance.api2ProjectProjectIdOrKeyAvatarsGet(projectIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| project id or project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2ProjectProjectIdOrKeyGet

> api2ProjectProjectIdOrKeyGet(projectIdOrKey, opts)



Contains a full representation of a project in JSON format.  &lt;p&gt;  All project keys associated with the project will only be returned if &lt;code&gt;expand&#x3D;projectKeys&lt;/code&gt;.  &lt;p&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
let opts = {
  'expand': "expand_example" // String | the parameters to expand
};
apiInstance.api2ProjectProjectIdOrKeyGet(projectIdOrKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| the project id or project key | 
 **expand** | **String**| the parameters to expand | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2ProjectProjectIdOrKeyPropertiesGet

> api2ProjectProjectIdOrKeyPropertiesGet(projectIdOrKey)



Returns the keys of all properties for the project identified by the key or by the id.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | the project from which keys will be returned.
apiInstance.api2ProjectProjectIdOrKeyPropertiesGet(projectIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| the project from which keys will be returned. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2ProjectProjectIdOrKeyPropertiesPropertyKeyDelete

> api2ProjectProjectIdOrKeyPropertiesPropertyKeyDelete(projectIdOrKey, propertyKey)



Removes the property from the project identified by the key or by the id. Ths user removing the property is required  to have permissions to administer the project.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | the project from which keys will be returned.
let propertyKey = "propertyKey_example"; // String | the key of the property to return.
apiInstance.api2ProjectProjectIdOrKeyPropertiesPropertyKeyDelete(projectIdOrKey, propertyKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| the project from which keys will be returned. | 
 **propertyKey** | **String**| the key of the property to return. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2ProjectProjectIdOrKeyPropertiesPropertyKeyGet

> api2ProjectProjectIdOrKeyPropertiesPropertyKeyGet(projectIdOrKey, propertyKey)



Returns the value of the property with a given key from the project identified by the key or by the id. The user who retrieves  the property is required to have permissions to read the project.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | the project from which keys will be returned.
let propertyKey = "propertyKey_example"; // String | the key of the property to return.
apiInstance.api2ProjectProjectIdOrKeyPropertiesPropertyKeyGet(projectIdOrKey, propertyKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| the project from which keys will be returned. | 
 **propertyKey** | **String**| the key of the property to return. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2ProjectProjectIdOrKeyPropertiesPropertyKeyPut

> api2ProjectProjectIdOrKeyPropertiesPropertyKeyPut(projectIdOrKey, propertyKey)



Sets the value of the specified project&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against the project identified by the key or by the id. The user  who stores the data is required to have permissions to administer the project.  &lt;/p&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | the project from which keys will be returned.
let propertyKey = "propertyKey_example"; // String | the key of the property to return.
apiInstance.api2ProjectProjectIdOrKeyPropertiesPropertyKeyPut(projectIdOrKey, propertyKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| the project from which keys will be returned. | 
 **propertyKey** | **String**| the key of the property to return. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2ProjectProjectIdOrKeyRoleGet

> api2ProjectProjectIdOrKeyRoleGet(projectIdOrKey)



Returns all roles in the given project Id or key, with links to full details on each role.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
apiInstance.api2ProjectProjectIdOrKeyRoleGet(projectIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| the project id or project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2ProjectProjectKeyOrIdIssuesecuritylevelschemeGet

> api2ProjectProjectKeyOrIdIssuesecuritylevelschemeGet(projectKeyOrId)



Returns the issue security scheme for project.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectKeyOrId = "projectKeyOrId_example"; // String | 
apiInstance.api2ProjectProjectKeyOrIdIssuesecuritylevelschemeGet(projectKeyOrId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectKeyOrId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2ProjectProjectKeyOrIdNotificationschemeGet

> api2ProjectProjectKeyOrIdNotificationschemeGet(projectKeyOrId, opts)



Gets a notification scheme associated with the project.  Follow the documentation of /notificationscheme/{id} resource for all details about returned value.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectKeyOrId = "projectKeyOrId_example"; // String | key or id of the project
let opts = {
  'expand': "expand_example" // String | 
};
apiInstance.api2ProjectProjectKeyOrIdNotificationschemeGet(projectKeyOrId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectKeyOrId** | **String**| key or id of the project | 
 **expand** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2ProjectvalidateKeyGet

> api2ProjectvalidateKeyGet(opts)



Validates a project key.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'key': "key_example" // String | the project key
};
apiInstance.api2ProjectvalidateKeyGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| the project key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2RoleGet

> api2RoleGet()



Get all the ProjectRoles available in JIRA. Currently this list is global.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.api2RoleGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarIdDelete

> api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarIdDelete(id, type, owningObjectId)



Deletes avatar

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | database id for avatar
let type = "type_example"; // String | Project id or project key
let owningObjectId = "owningObjectId_example"; // String | 
apiInstance.api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarIdDelete(id, type, owningObjectId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| database id for avatar | 
 **type** | **String**| Project id or project key | 
 **owningObjectId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarPost

> api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarPost(type, owningObjectId)



### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let type = "type_example"; // String | 
let owningObjectId = "owningObjectId_example"; // String | 
apiInstance.api2UniversalAvatarTypeTypeOwnerOwningObjectIdAvatarPost(type, owningObjectId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **String**|  | 
 **owningObjectId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2UniversalAvatarTypeTypeOwnerOwningObjectIdTempPost

> api2UniversalAvatarTypeTypeOwnerOwningObjectIdTempPost(type, owningObjectId)



### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let type = "type_example"; // String | 
let owningObjectId = "owningObjectId_example"; // String | 
apiInstance.api2UniversalAvatarTypeTypeOwnerOwningObjectIdTempPost(type, owningObjectId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **String**|  | 
 **owningObjectId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2UserAvatarIdDelete

> api2UserAvatarIdDelete(id, opts)



Deletes avatar

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | database id for avatar
let opts = {
  'username': "username_example" // String | username
};
apiInstance.api2UserAvatarIdDelete(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| database id for avatar | 
 **username** | **String**| username | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2UserAvatarPost

> api2UserAvatarPost(opts)



Converts temporary avatar into a real avatar

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'username': "username_example" // String | username
};
apiInstance.api2UserAvatarPost(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| username | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2UserAvatarPut

> api2UserAvatarPut(opts)



### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'username': "username_example" // String | 
};
apiInstance.api2UserAvatarPut(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2UserAvatarTemporaryPost

> api2UserAvatarTemporaryPost(opts)



Creates temporary avatar using multipart. The response is sent back as JSON stored in a textarea. This is because  the client uses remote iframing to submit avatars using multipart. So we must send them a valid HTML page back from  which the client parses the JSON from.  &lt;p&gt;  Creating a temporary avatar is part of a 3-step process in uploading a new  avatar for a user: upload, crop, confirm. This endpoint allows you to use a multipart upload  instead of sending the image directly as the request body.  &lt;/p&gt;  &lt;p&gt;  You *must* use \&quot;avatar\&quot; as the name of the upload parameter:&lt;/p&gt;  &lt;p/&gt;  &lt;pre&gt;  curl -c cookiejar.txt -X POST -u admin:admin -H \&quot;X-Atlassian-Token: no-check\&quot; \\    -F \&quot;avatar&#x3D;@mynewavatar.png;type&#x3D;image/png\&quot; \\    &#39;http://localhost:8090/jira/rest/api/2/user/avatar/temporary?username&#x3D;admin&#39;  &lt;/pre&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'username': "username_example" // String | Username
};
apiInstance.api2UserAvatarTemporaryPost(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| Username | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2UserAvatarsGet

> api2UserAvatarsGet(opts)



Returns all avatars which are visible for the currently logged in user.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'username': "username_example" // String | username
};
apiInstance.api2UserAvatarsGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| username | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2UserColumnsDelete

> api2UserColumnsDelete(opts)



Reset the default columns for the given user to the system default. Admin permission will be required to get  columns for a user other than the currently logged in user.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'username': "username_example" // String | username
};
apiInstance.api2UserColumnsDelete(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| username | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2UserColumnsGet

> api2UserColumnsGet(opts)



Returns the default columns for the given user. Admin permission will be required to get columns for a user  other than the currently logged in user.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'username': "username_example" // String | username
};
apiInstance.api2UserColumnsGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| username | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2UserColumnsPut

> api2UserColumnsPut()



Sets the default columns for the given user.  Admin permission will be required to get columns for a user  other than the currently logged in user.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.api2UserColumnsPut((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## api2UserGet

> api2UserGet(opts)



Returns a user. This resource cannot be accessed anonymously.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'username': "username_example", // String | the username
  'key': "key_example" // String | user key
};
apiInstance.api2UserGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| the username | [optional] 
 **key** | **String**| user key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2UserPropertiesGet

> api2UserPropertiesGet(opts)



Returns the keys of all properties for the user identified by the key or by the id.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'userKey': "userKey_example", // String | key of the user whose properties are to be returned
  'username': "username_example" // String | username of the user whose properties are to be returned
};
apiInstance.api2UserPropertiesGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userKey** | **String**| key of the user whose properties are to be returned | [optional] 
 **username** | **String**| username of the user whose properties are to be returned | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2UserPropertiesPropertyKeyDelete

> api2UserPropertiesPropertyKeyDelete(propertyKey, opts)



Removes the property from the user identified by the key or by the id. Ths user removing the property is required  to have permissions to administer the user.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let propertyKey = "propertyKey_example"; // String | 
let opts = {
  'userKey': "userKey_example", // String | key of the user whose property is to be removed
  'username': "username_example" // String | username of the user whose property is to be removed
};
apiInstance.api2UserPropertiesPropertyKeyDelete(propertyKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **propertyKey** | **String**|  | 
 **userKey** | **String**| key of the user whose property is to be removed | [optional] 
 **username** | **String**| username of the user whose property is to be removed | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2UserPropertiesPropertyKeyGet

> api2UserPropertiesPropertyKeyGet(propertyKey, opts)



Returns the value of the property with a given key from the user identified by the key or by the id. The user who retrieves  the property is required to have permissions to read the user.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let propertyKey = "propertyKey_example"; // String | 
let opts = {
  'userKey': "userKey_example", // String | key of the user whose property is to be returned
  'username': "username_example" // String | username of the user whose property is to be returned
};
apiInstance.api2UserPropertiesPropertyKeyGet(propertyKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **propertyKey** | **String**|  | 
 **userKey** | **String**| key of the user whose property is to be returned | [optional] 
 **username** | **String**| username of the user whose property is to be returned | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2UserPropertiesPropertyKeyPut

> api2UserPropertiesPropertyKeyPut(propertyKey, opts)



Sets the value of the specified user&#39;s property.  &lt;p&gt;  You can use this resource to store a custom data against the user identified by the key or by the id. The user  who stores the data is required to have permissions to administer the user.  &lt;/p&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let propertyKey = "propertyKey_example"; // String | 
let opts = {
  'userKey': "userKey_example", // String | key of the user whose property is to be set
  'username': "username_example" // String | username of the user whose property is to be set
};
apiInstance.api2UserPropertiesPropertyKeyPut(propertyKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **propertyKey** | **String**|  | 
 **userKey** | **String**| key of the user whose property is to be set | [optional] 
 **username** | **String**| username of the user whose property is to be set | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2UserPut

> api2UserPut(opts)



Modify user. The \&quot;value\&quot; fields present will override the existing value.  Fields skipped in request will not be changed.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'username': "username_example", // String | the username
  'key': "key_example" // String | user key
};
apiInstance.api2UserPut(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| the username | [optional] 
 **key** | **String**| user key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2VersionIdDelete

> api2VersionIdDelete(id, opts)



Delete a project version.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | The version to delete
let opts = {
  'moveFixIssuesTo': "moveFixIssuesTo_example", // String | The version to set fixVersion to on issues where the deleted version is the fix version,                              If null then the fixVersion is removed.
  'moveAffectedIssuesTo': "moveAffectedIssuesTo_example" // String | The version to set affectedVersion to on issues where the deleted version is the affected version,                              If null then the affectedVersion is removed.
};
apiInstance.api2VersionIdDelete(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The version to delete | 
 **moveFixIssuesTo** | **String**| The version to set fixVersion to on issues where the deleted version is the fix version,                              If null then the fixVersion is removed. | [optional] 
 **moveAffectedIssuesTo** | **String**| The version to set affectedVersion to on issues where the deleted version is the affected version,                              If null then the affectedVersion is removed. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2VersionIdRemoveAndSwapPost

> api2VersionIdRemoveAndSwapPost(id)



Delete a project version.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | The version to delete
apiInstance.api2VersionIdRemoveAndSwapPost(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The version to delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2VersionVersionIdRemotelinkGlobalIdPost

> api2VersionVersionIdRemotelinkGlobalIdPost(versionId, globalId)



Create a remote version link via POST.  The link&#39;s global ID will be taken from the  JSON payload if provided; otherwise, it will be generated.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let versionId = "versionId_example"; // String | The version ID of the remote link
let globalId = "globalId_example"; // String | The global ID of the remote link
apiInstance.api2VersionVersionIdRemotelinkGlobalIdPost(versionId, globalId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionId** | **String**| The version ID of the remote link | 
 **globalId** | **String**| The global ID of the remote link | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2VersionVersionIdRemotelinkPost

> api2VersionVersionIdRemotelinkPost(versionId)



Create a remote version link via POST.  The link&#39;s global ID will be taken from the  JSON payload if provided; otherwise, it will be generated.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let versionId = "versionId_example"; // String | The version for which to delete ALL existing remote version links
apiInstance.api2VersionVersionIdRemotelinkPost(versionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionId** | **String**| The version for which to delete ALL existing remote version links | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2WorkflowApi2TransitionsIdPropertiesDelete

> api2WorkflowApi2TransitionsIdPropertiesDelete(id, opts)



Delete a property from the passed transition on the passed workflow. It is not an error to delete a property that  does not exist.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the ID of the transition within the workflow.
let opts = {
  'key': "key_example", // String | the name of the property to add.
  'workflowName': "workflowName_example", // String | the name of the workflow to use.
  'workflowMode': "workflowMode_example" // String | the type of workflow to use. Can either be \"live\" or \"draft\".
};
apiInstance.api2WorkflowApi2TransitionsIdPropertiesDelete(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the ID of the transition within the workflow. | 
 **key** | **String**| the name of the property to add. | [optional] 
 **workflowName** | **String**| the name of the workflow to use. | [optional] 
 **workflowMode** | **String**| the type of workflow to use. Can either be \&quot;live\&quot; or \&quot;draft\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2WorkflowschemeIdIssuetypeIssueTypeDelete

> api2WorkflowschemeIdIssuetypeIssueTypeDelete(issueType, id, opts)



Remove the specified issue type mapping from the scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueType = "issueType_example"; // String | the issue type being set.
let id = 789; // Number | the id of the scheme.
let opts = {
  'updateDraftIfNeeded': true // Boolean | when true will create and return a draft when the workflow scheme cannot be edited                             (e.g. when it is being used by a project).
};
apiInstance.api2WorkflowschemeIdIssuetypeIssueTypeDelete(issueType, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueType** | **String**| the issue type being set. | 
 **id** | **Number**| the id of the scheme. | 
 **updateDraftIfNeeded** | **Boolean**| when true will create and return a draft when the workflow scheme cannot be edited                             (e.g. when it is being used by a project). | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## api2WorkflowschemeIdIssuetypeIssueTypeGet

> api2WorkflowschemeIdIssuetypeIssueTypeGet(issueType, id, opts)



Returns the issue type mapping for the passed workflow scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueType = "issueType_example"; // String | the issue type being set.
let id = 789; // Number | the id of the scheme.
let opts = {
  'returnDraftIfExists': false // Boolean | when true indicates that a scheme's draft, if it exists, should be queried instead of                             the scheme itself.
};
apiInstance.api2WorkflowschemeIdIssuetypeIssueTypeGet(issueType, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueType** | **String**| the issue type being set. | 
 **id** | **Number**| the id of the scheme. | 
 **returnDraftIfExists** | **Boolean**| when true indicates that a scheme&#39;s draft, if it exists, should be queried instead of                             the scheme itself. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## approveUpgrade

> approveUpgrade()



### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.approveUpgrade((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## areMetricsExposed

> areMetricsExposed()



### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.areMetricsExposed((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## assign

> assign(issueIdOrKey)



Assigns an issue to a user.  You can use this resource to assign issues when the user submitting the request has the assign permission but not the  edit issue permission.  If the name is \&quot;-1\&quot; automatic assignee is used.  A null name will remove the assignee.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | a String containing an issue key
apiInstance.assign(issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| a String containing an issue key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## assignPermissionScheme

> assignPermissionScheme(projectKeyOrId, opts)



Assigns a permission scheme with a project.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectKeyOrId = "projectKeyOrId_example"; // String | key or id of the project
let opts = {
  'expand': "expand_example" // String | 
};
apiInstance.assignPermissionScheme(projectKeyOrId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectKeyOrId** | **String**| key or id of the project | 
 **expand** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## canMoveSubTask

> canMoveSubTask(issueIdOrKey)



### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | The parent issue's key or id
apiInstance.canMoveSubTask(issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| The parent issue&#39;s key or id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## cancelUpgrade

> cancelUpgrade()



### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.cancelUpgrade((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## changeMyPassword

> changeMyPassword()



Modify caller password.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.changeMyPassword((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## changeUserPassword

> changeUserPassword(opts)



Modify user password.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'username': "username_example", // String | the username
  'key': "key_example" // String | user key
};
apiInstance.changeUserPassword(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| the username | [optional] 
 **key** | **String**| user key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createComponent

> createComponent()



Create a component via POST.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.createComponent((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## createCustomField

> createCustomField()



Creates a custom field using a definition (object encapsulating custom field data)

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.createCustomField((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## createDraftForParent

> createDraftForParent(id)



Create a draft for the passed scheme. The draft will be a copy of the state of the parent.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the parent scheme.
apiInstance.createDraftForParent(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the parent scheme. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createFilter

> createFilter(opts)



Creates a new filter, and returns newly created filter.  Currently sets permissions just using the users default sharing permissions

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'expand': "expand_example" // String | the parameters to expand
};
apiInstance.createFilter(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **String**| the parameters to expand | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createGroup

> createGroup()



Creates a group by given group parameter  &lt;p&gt;  Returns REST representation for the requested group.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.createGroup((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## createIssue

> createIssue()



Creates an issue or a sub-task from a JSON representation.  &lt;p/&gt;  The fields that can be set on create, in either the fields parameter or the update parameter can be determined  using the &lt;b&gt;/rest/api/2/issue/createmeta&lt;/b&gt; resource.  If a field is not configured to appear on the create screen, then it will not be in the createmeta, and a field  validation error will occur if it is submitted.  &lt;p/&gt;  Creating a sub-task is similar to creating a regular issue, with two important differences:  &lt;ul&gt;  &lt;li&gt;the &lt;code&gt;issueType&lt;/code&gt; field must correspond to a sub-task issue type (you can use  &lt;code&gt;/issue/createmeta&lt;/code&gt; to discover sub-task issue types), and&lt;/li&gt;  &lt;li&gt;you must provide a &lt;code&gt;parent&lt;/code&gt; field in the issue create request containing the id or key of the  parent issue.&lt;/li&gt;  &lt;/ul&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.createIssue((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## createIssueLinkType

> createIssueLinkType()



Create a new issue link type.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.createIssueLinkType((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## createIssueType

> createIssueType()



Creates an issue type from a JSON representation and adds the issue newly created issue type to the default issue  type scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.createIssueType((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## createIssues

> createIssues()



Creates issues or sub-tasks from a JSON representation.  &lt;p/&gt;  Creates many issues in one bulk operation.  &lt;p/&gt;  Creating a sub-task is similar to creating a regular issue. More details can be found in createIssue section:  {@link IssueResource#createIssue(IssueUpdateBean)}}

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.createIssues((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## createOrUpdateRemoteIssueLink

> createOrUpdateRemoteIssueLink(issueIdOrKey)



Creates or updates a remote issue link from a JSON representation. If a globalId is provided and a remote issue link  exists with that globalId, the remote issue link is updated. Otherwise, the remote issue link is created.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue to create the remote issue link for
apiInstance.createOrUpdateRemoteIssueLink(issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| the issue to create the remote issue link for | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createPermissionGrant

> createPermissionGrant(schemeId, opts)



Creates a permission grant in a permission scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let schemeId = 789; // Number | 
let opts = {
  'expand': "expand_example" // String | 
};
apiInstance.createPermissionGrant(schemeId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schemeId** | **Number**|  | 
 **expand** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createPermissionScheme

> createPermissionScheme(opts)



Create a new permission scheme.  This method can create schemes with a defined permission set, or without.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'expand': "expand_example" // String | 
};
apiInstance.createPermissionScheme(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createProject

> createProject()



Creates a new project.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.createProject((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## createProjectCategory

> createProjectCategory()



Create a project category via POST.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.createProjectCategory((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## createProjectRole

> createProjectRole()



Creates a new ProjectRole to be available in JIRA.  The created role does not have any default actors assigned.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.createProjectRole((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## createProperty

> createProperty(id, opts)



Add a new property to a transition. Trying to add a property that already  exists will fail.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the ID of the transition within the workflow.
let opts = {
  'key': "key_example", // String | the name of the property to add.
  'workflowName': "workflowName_example", // String | the name of the workflow to use.
  'workflowMode': "workflowMode_example" // String | the type of workflow to use. Can either be \"live\" or \"draft\".
};
apiInstance.createProperty(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the ID of the transition within the workflow. | 
 **key** | **String**| the name of the property to add. | [optional] 
 **workflowName** | **String**| the name of the workflow to use. | [optional] 
 **workflowMode** | **String**| the type of workflow to use. Can either be \&quot;live\&quot; or \&quot;draft\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createScheme

> createScheme()



Create a new workflow scheme.  &lt;p/&gt;  The body contains a representation of the new scheme. Values not passed are assumed to be set to their defaults.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.createScheme((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## createUser

> createUser()



Create user. By default created user will not be notified with email.  If password field is not set then password will be randomly generated.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.createUser((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## createVersion

> createVersion()



Create a version via POST.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.createVersion((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## currentUser

> currentUser()



Returns information about the currently authenticated user&#39;s session. If the caller is not authenticated they  will get a 401 Unauthorized status code.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.currentUser((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## deleteActor

> deleteActor(projectIdOrKey, id, opts)



Deletes actors (users or groups) from a project role.  &lt;p&gt;  &lt;ul&gt;  &lt;li&gt;Delete a user from the role: &lt;code&gt;/rest/api/2/project/{projectIdOrKey}/role/{roleId}?user&#x3D;{username}&lt;/code&gt;&lt;/li&gt;  &lt;li&gt;Delete a group from the role: &lt;code&gt;/rest/api/2/project/{projectIdOrKey}/role/{roleId}?group&#x3D;{groupname}&lt;/code&gt;&lt;/li&gt;  &lt;/ul&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
let id = 789; // Number | the project role id
let opts = {
  'user': "user_example", // String | the username to remove from the project role
  'group': "group_example" // String | the groupname to remove from the project role
};
apiInstance.deleteActor(projectIdOrKey, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| the project id or project key | 
 **id** | **Number**| the project role id | 
 **user** | **String**| the username to remove from the project role | [optional] 
 **group** | **String**| the groupname to remove from the project role | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteComment

> deleteComment(issueIdOrKey, id)



Deletes an existing comment .

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | of the issue the comment belongs to
let id = "id_example"; // String | the ID of the comment to request
apiInstance.deleteComment(issueIdOrKey, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| of the issue the comment belongs to | 
 **id** | **String**| the ID of the comment to request | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteDefault

> deleteDefault(id, opts)



Remove the default workflow from the passed workflow scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the scheme.
let opts = {
  'updateDraftIfNeeded': true // Boolean | when true will create and return a draft when the workflow scheme cannot be edited                             (e.g. when it is being used by a project).
};
apiInstance.deleteDefault(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the scheme. | 
 **updateDraftIfNeeded** | **Boolean**| when true will create and return a draft when the workflow scheme cannot be edited                             (e.g. when it is being used by a project). | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteDraftById

> deleteDraftById(id)



Delete the passed draft workflow scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the parent scheme.
apiInstance.deleteDraftById(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the parent scheme. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteDraftDefault

> deleteDraftDefault(id)



Remove the default workflow from the passed draft workflow scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the parent scheme.
apiInstance.deleteDraftDefault(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the parent scheme. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteDraftIssueType

> deleteDraftIssueType(issueType, id)



Remove the specified issue type mapping from the draft scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueType = "issueType_example"; // String | the issue type being set.
let id = 789; // Number | the id of the parent scheme.
apiInstance.deleteDraftIssueType(issueType, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueType** | **String**| the issue type being set. | 
 **id** | **Number**| the id of the parent scheme. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteDraftWorkflowMapping

> deleteDraftWorkflowMapping(id, opts)



Delete the passed workflow from the draft workflow scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the parent scheme.
let opts = {
  'workflowName': "workflowName_example" // String | the name of the workflow to delete.
};
apiInstance.deleteDraftWorkflowMapping(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the parent scheme. | 
 **workflowName** | **String**| the name of the workflow to delete. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteFilter

> deleteFilter(id)



Delete a filter.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the filter being looked up
apiInstance.deleteFilter(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the filter being looked up | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteIssue

> deleteIssue(issueIdOrKey, opts)



Delete an issue.  &lt;p/&gt;  If the issue has subtasks you must set the parameter deleteSubtasks&#x3D;true to delete the issue.  You cannot delete an issue without its subtasks also being deleted.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue id or key to update (i.e. JRA-1330)
let opts = {
  'deleteSubtasks': "deleteSubtasks_example" // String | a String of true or false indicating that any subtasks should also be deleted.  If the                        issue has no subtasks this parameter is ignored.  If the issue has subtasks and this parameter is missing or false,                        then the issue will not be deleted and an error will be returned.
};
apiInstance.deleteIssue(issueIdOrKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| the issue id or key to update (i.e. JRA-1330) | 
 **deleteSubtasks** | **String**| a String of true or false indicating that any subtasks should also be deleted.  If the                        issue has no subtasks this parameter is ignored.  If the issue has subtasks and this parameter is missing or false,                        then the issue will not be deleted and an error will be returned. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteIssueLink

> deleteIssueLink(linkId)



Deletes an issue link with the specified id.  To be able to delete an issue link you must be able to view both issues and must have the link issue permission  for at least one of the issues.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let linkId = "linkId_example"; // String | the issue link id.
apiInstance.deleteIssueLink(linkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkId** | **String**| the issue link id. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteIssueLinkType

> deleteIssueLinkType(issueLinkTypeId)



Delete the specified issue link type.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueLinkTypeId = "issueLinkTypeId_example"; // String | 
apiInstance.deleteIssueLinkType(issueLinkTypeId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueLinkTypeId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deletePermissionScheme

> deletePermissionScheme(schemeId)



Deletes a permission scheme identified by the given id.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let schemeId = 789; // Number | 
apiInstance.deletePermissionScheme(schemeId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schemeId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deletePermissionSchemeEntity

> deletePermissionSchemeEntity(permissionId, schemeId)



Deletes a permission grant from a permission scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let permissionId = 789; // Number | 
let schemeId = 789; // Number | 
apiInstance.deletePermissionSchemeEntity(permissionId, schemeId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permissionId** | **Number**|  | 
 **schemeId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteProject

> deleteProject(projectIdOrKey)



Deletes a project.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
apiInstance.deleteProject(projectIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| the project id or project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteProjectRole

> deleteProjectRole(id, opts)



Deletes a role. May return 403 in the future

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | 
let opts = {
  'swap': 789 // Number | if given, removes a role even if it is used in scheme by replacing the role with the given one
};
apiInstance.deleteProjectRole(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **swap** | **Number**| if given, removes a role even if it is used in scheme by replacing the role with the given one | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteProjectRoleActorsFromRole

> deleteProjectRoleActorsFromRole(id, opts)



Removes default actor from the given role.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the role id to remove the actors from
let opts = {
  'user': "user_example", // String | if given, removes an actor from given role
  'group': "group_example" // String | if given, removes an actor from given role
};
apiInstance.deleteProjectRoleActorsFromRole(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the role id to remove the actors from | 
 **user** | **String**| if given, removes an actor from given role | [optional] 
 **group** | **String**| if given, removes an actor from given role | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteRemoteIssueLinkByGlobalId

> deleteRemoteIssueLinkByGlobalId(issueIdOrKey, opts)



Delete the remote issue link with the given global id on the issue.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue to create the remote issue link for
let opts = {
  'globalId': "globalId_example" // String | the global id of the remote issue link
};
apiInstance.deleteRemoteIssueLinkByGlobalId(issueIdOrKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| the issue to create the remote issue link for | 
 **globalId** | **String**| the global id of the remote issue link | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteRemoteIssueLinkById

> deleteRemoteIssueLinkById(linkId, issueIdOrKey)



Delete the remote issue link with the given id on the issue.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let linkId = "linkId_example"; // String | the id of the remote issue link
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue to create the remote issue link for
apiInstance.deleteRemoteIssueLinkById(linkId, issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkId** | **String**| the id of the remote issue link | 
 **issueIdOrKey** | **String**| the issue to create the remote issue link for | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteRemoteVersionLink

> deleteRemoteVersionLink(versionId, globalId)



Delete a specific remote version link with the given version ID and global ID.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let versionId = "versionId_example"; // String | The version ID of the remote link
let globalId = "globalId_example"; // String | The global ID of the remote link
apiInstance.deleteRemoteVersionLink(versionId, globalId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionId** | **String**| The version ID of the remote link | 
 **globalId** | **String**| The global ID of the remote link | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteRemoteVersionLinksByVersionId

> deleteRemoteVersionLinksByVersionId(versionId)



Delete all remote version links for a given version ID.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let versionId = "versionId_example"; // String | The version for which to delete ALL existing remote version links
apiInstance.deleteRemoteVersionLinksByVersionId(versionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionId** | **String**| The version for which to delete ALL existing remote version links | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteScheme

> deleteScheme(id)



Delete the passed workflow scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the scheme.
apiInstance.deleteScheme(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the scheme. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSharePermission

> deleteSharePermission(id, permissionId)



Removes a share permissions from the given filter.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | 
let permissionId = 789; // Number | 
apiInstance.deleteSharePermission(id, permissionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **permissionId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteTab

> deleteTab(screenId, tabId)



Deletes tab to give screen

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let screenId = 789; // Number | id of screen
let tabId = 789; // Number | id of tab
apiInstance.deleteTab(screenId, tabId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screenId** | **Number**| id of screen | 
 **tabId** | **Number**| id of tab | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteWorkflowMapping

> deleteWorkflowMapping(id, opts)



Delete the passed workflow from the workflow scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the scheme.
let opts = {
  'workflowName': "workflowName_example", // String | the name of the workflow to delete.
  'updateDraftIfNeeded': true // Boolean | flag to indicate if a draft should be created if necessary to delete the workflow                             from the scheme.
};
apiInstance.deleteWorkflowMapping(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the scheme. | 
 **workflowName** | **String**| the name of the workflow to delete. | [optional] 
 **updateDraftIfNeeded** | **Boolean**| flag to indicate if a draft should be created if necessary to delete the workflow                             from the scheme. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteWorklog

> deleteWorklog(issueIdOrKey, id, opts)



Deletes an existing worklog entry.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | a string containing the issue id or key the worklog belongs to
let id = "id_example"; // String | id of the worklog to be deleted
let opts = {
  'adjustEstimate': "adjustEstimate_example", // String | (optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are                        <ul>                        <li>\"new\" - sets the estimate to a specific value</li>                        <li>\"leave\"- leaves the estimate as is</li>                        <li>\"manual\" - specify a specific amount to increase remaining estimate by</li>                        <li>\"auto\"- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog</li> </ul>
  'newEstimate': "newEstimate_example", // String | (required when \"new\" is selected for adjustEstimate) the new value for the remaining estimate field. e.g. \"2d\"
  'increaseBy': "increaseBy_example" // String | (required when \"manual\" is selected for adjustEstimate) the amount to increase the remaining estimate by e.g. \"2d\"
};
apiInstance.deleteWorklog(issueIdOrKey, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| a string containing the issue id or key the worklog belongs to | 
 **id** | **String**| id of the worklog to be deleted | 
 **adjustEstimate** | **String**| (optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are                        &lt;ul&gt;                        &lt;li&gt;\&quot;new\&quot; - sets the estimate to a specific value&lt;/li&gt;                        &lt;li&gt;\&quot;leave\&quot;- leaves the estimate as is&lt;/li&gt;                        &lt;li&gt;\&quot;manual\&quot; - specify a specific amount to increase remaining estimate by&lt;/li&gt;                        &lt;li&gt;\&quot;auto\&quot;- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog&lt;/li&gt; &lt;/ul&gt; | [optional] 
 **newEstimate** | **String**| (required when \&quot;new\&quot; is selected for adjustEstimate) the new value for the remaining estimate field. e.g. \&quot;2d\&quot; | [optional] 
 **increaseBy** | **String**| (required when \&quot;manual\&quot; is selected for adjustEstimate) the amount to increase the remaining estimate by e.g. \&quot;2d\&quot; | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## doTransition

> doTransition(issueIdOrKey)



Perform a transition on an issue.  When performing the transition you can update or set other issue fields.  &lt;p/&gt;  The fields that can be set on transtion, in either the fields parameter or the update parameter can be determined  using the &lt;b&gt;/rest/api/2/issue/{issueIdOrKey}/transitions?expand&#x3D;transitions.fields&lt;/b&gt; resource.  If a field is not configured to appear on the transition screen, then it will not be in the transition metadata, and a field  validation error will occur if it is submitted.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue whose transitions you want to view
apiInstance.doTransition(issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| the issue whose transitions you want to view | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## editFilter

> editFilter(id, opts)



Updates an existing filter, and returns its new value.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the filter being looked up
let opts = {
  'expand': "expand_example" // String | the parameters to expand
};
apiInstance.editFilter(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the filter being looked up | 
 **expand** | **String**| the parameters to expand | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## editIssue

> editIssue(issueIdOrKey, opts)



Edits an issue from a JSON representation.  &lt;p/&gt;  The issue can either be updated by setting explicit the field value(s)  or by using an operation to change the field value.  &lt;p/&gt;  The fields that can be updated, in either the fields parameter or the update parameter, can be determined  using the &lt;b&gt;/rest/api/2/issue/{issueIdOrKey}/editmeta&lt;/b&gt; resource.&lt;br&gt;  If a field is not configured to appear on the edit screen, then it will not be in the editmeta, and a field  validation error will occur if it is submitted.  &lt;p/&gt;  Specifying a \&quot;field_id\&quot;: field_value in the \&quot;fields\&quot; is a shorthand for a \&quot;set\&quot; operation in the \&quot;update\&quot; section.&lt;br&gt;  Field should appear either in \&quot;fields\&quot; or \&quot;update\&quot;, not in both.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue id or key to update (i.e. JRA-1330)
let opts = {
  'notifyUsers': true // Boolean | send the email with notification that the issue was updated to users that watch it.                     Admin or project admin permissions are required to disable the notification.
};
apiInstance.editIssue(issueIdOrKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| the issue id or key to update (i.e. JRA-1330) | 
 **notifyUsers** | **Boolean**| send the email with notification that the issue was updated to users that watch it.                     Admin or project admin permissions are required to disable the notification. | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## expandForHumans

> expandForHumans(id)



Tries to expand an attachment. Output is human-readable and subject to change.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | the id of the attachment to expand.
apiInstance.expandForHumans(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| the id of the attachment to expand. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## expandForMachines

> expandForMachines(id)



Tries to expand an attachment. Output is raw and should be backwards-compatible through the course of time.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | the id of the attachment to expand.
apiInstance.expandForMachines(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| the id of the attachment to expand. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## findAssignableUsers

> findAssignableUsers(opts)



Returns a list of users that match the search string. This resource cannot be accessed anonymously.  Please note that this resource should be called with an issue key when a list of assignable users is retrieved  for editing.  For create only a project key should be supplied.  The list of assignable users may be incorrect  if it&#39;s called with the project key for editing.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'username': "username_example", // String | the username
  'project': "project_example", // String | the key of the project we are finding assignable users for
  'issueKey': "issueKey_example", // String | the issue key for the issue being edited we need to find assignable users for.
  'startAt': 56, // Number | the index of the first user to return (0-based)
  'maxResults': 56, // Number | the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                    If you specify a value that is higher than this number, your search results will be truncated.
  'actionDescriptorId': 56 // Number | 
};
apiInstance.findAssignableUsers(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| the username | [optional] 
 **project** | **String**| the key of the project we are finding assignable users for | [optional] 
 **issueKey** | **String**| the issue key for the issue being edited we need to find assignable users for. | [optional] 
 **startAt** | **Number**| the index of the first user to return (0-based) | [optional] 
 **maxResults** | **Number**| the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                    If you specify a value that is higher than this number, your search results will be truncated. | [optional] 
 **actionDescriptorId** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## findBulkAssignableUsers

> findBulkAssignableUsers(opts)



Returns a list of users that match the search string and can be assigned issues for all the given projects.  This resource cannot be accessed anonymously.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'username': "username_example", // String | the username
  'projectKeys': "projectKeys_example", // String | the keys of the projects we are finding assignable users for, comma-separated
  'startAt': 56, // Number | the index of the first user to return (0-based)
  'maxResults': 56 // Number | the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                        If you specify a value that is higher than this number, your search results will be truncated.
};
apiInstance.findBulkAssignableUsers(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| the username | [optional] 
 **projectKeys** | **String**| the keys of the projects we are finding assignable users for, comma-separated | [optional] 
 **startAt** | **Number**| the index of the first user to return (0-based) | [optional] 
 **maxResults** | **Number**| the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                        If you specify a value that is higher than this number, your search results will be truncated. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## findGroups

> findGroups(opts)



Returns groups with substrings matching a given query. This is mainly for use with  the group picker, so the returned groups contain html to be used as picker suggestions.  The groups are also wrapped in a single response object that also contains a header for  use in the picker, specifically &lt;i&gt;Showing X of Y matching groups&lt;/i&gt;.  &lt;p&gt;  The number of groups returned is limited by the system property \&quot;jira.ajax.autocomplete.limit\&quot;  &lt;p&gt;  The groups will be unique and sorted.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'query': "query_example", // String | a String to match groups agains
  'exclude': "exclude_example", // String | 
  'maxResults': 56, // Number | 
  'userName': "userName_example" // String | 
};
apiInstance.findGroups(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **String**| a String to match groups agains | [optional] 
 **exclude** | **String**|  | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **userName** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## findUsers

> findUsers(opts)



Returns a list of users that match the search string. This resource cannot be accessed anonymously.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'username': "username_example", // String | A query string used to search username, name or e-mail address
  'startAt': 56, // Number | the index of the first user to return (0-based)
  'maxResults': 56, // Number | the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                         If you specify a value that is higher than this number, your search results will be truncated.
  'includeActive': true, // Boolean | If true, then active users are included in the results (default true)
  'includeInactive': true // Boolean | If true, then inactive users are included in the results (default false)
};
apiInstance.findUsers(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| A query string used to search username, name or e-mail address | [optional] 
 **startAt** | **Number**| the index of the first user to return (0-based) | [optional] 
 **maxResults** | **Number**| the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                         If you specify a value that is higher than this number, your search results will be truncated. | [optional] 
 **includeActive** | **Boolean**| If true, then active users are included in the results (default true) | [optional] 
 **includeInactive** | **Boolean**| If true, then inactive users are included in the results (default false) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## findUsersAndGroups

> findUsersAndGroups(opts)



Returns a list of users and groups matching query with highlighting. This resource cannot be accessed  anonymously.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'query': "query_example", // String | A string used to search username, Name or e-mail address
  'maxResults': 56, // Number | the maximum number of users to return (defaults to 50). The maximum allowed value is 1000. If                     you specify a value that is higher than this number, your search results will be truncated.
  'showAvatar': true, // Boolean | 
  'fieldId': "fieldId_example", // String | The custom field id, if this request comes from a custom field, such as a user picker. Optional.
  'projectId': "projectId_example", // String | The list of project ids to further restrict the search                     This parameter can occur multiple times to pass in multiple project ids.                     Comma separated value is not supported.                     This parameter is only used when fieldId is present.
  'issueTypeId': "issueTypeId_example" // String | The list of issue type ids to further restrict the search.                     This parameter can occur multiple times to pass in multiple issue type ids.                     Comma separated value is not supported.                     Special values such as -1 (all standard issue types), -2 (all subtask issue types) are supported.                     This parameter is only used when fieldId is present.
};
apiInstance.findUsersAndGroups(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **String**| A string used to search username, Name or e-mail address | [optional] 
 **maxResults** | **Number**| the maximum number of users to return (defaults to 50). The maximum allowed value is 1000. If                     you specify a value that is higher than this number, your search results will be truncated. | [optional] 
 **showAvatar** | **Boolean**|  | [optional] 
 **fieldId** | **String**| The custom field id, if this request comes from a custom field, such as a user picker. Optional. | [optional] 
 **projectId** | **String**| The list of project ids to further restrict the search                     This parameter can occur multiple times to pass in multiple project ids.                     Comma separated value is not supported.                     This parameter is only used when fieldId is present. | [optional] 
 **issueTypeId** | **String**| The list of issue type ids to further restrict the search.                     This parameter can occur multiple times to pass in multiple issue type ids.                     Comma separated value is not supported.                     Special values such as -1 (all standard issue types), -2 (all subtask issue types) are supported.                     This parameter is only used when fieldId is present. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## findUsersForPicker

> findUsersForPicker(opts)



Returns a list of users matching query with highlighting. This resource cannot be accessed anonymously.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'query': "query_example", // String | A string used to search username, Name or e-mail address
  'maxResults': 56, // Number | the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                    If you specify a value that is higher than this number, your search results will be truncated.
  'showAvatar': true, // Boolean | 
  'exclude': "exclude_example" // String | 
};
apiInstance.findUsersForPicker(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **String**| A string used to search username, Name or e-mail address | [optional] 
 **maxResults** | **Number**| the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                    If you specify a value that is higher than this number, your search results will be truncated. | [optional] 
 **showAvatar** | **Boolean**|  | [optional] 
 **exclude** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## findUsersWithAllPermissions

> findUsersWithAllPermissions(opts)



Returns a list of active users that match the search string and have all specified permissions for the project or issue.&lt;br&gt;  This resource can be accessed by users with ADMINISTER_PROJECT permission for the project or global ADMIN or SYSADMIN rights.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'username': "username_example", // String | the username filter, list includes all users if unspecified
  'permissions': "permissions_example", // String | comma separated list of permissions for project or issue returned users must have, see                     <a href=\"https://developer.atlassian.com/static/javadoc/jira/6.0/reference/com/atlassian/jira/security/Permissions.Permission.html\">Permissions</a>                     JavaDoc for the list of all possible permissions.
  'issueKey': "issueKey_example", // String | the issue key for the issue for which returned users have specified permissions.
  'projectKey': "projectKey_example", // String | the optional project key to search for users with if no issueKey is supplied.
  'startAt': 56, // Number | the index of the first user to return (0-based)
  'maxResults': 56 // Number | the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                     If you specify a value that is higher than this number, your search results will be truncated.
};
apiInstance.findUsersWithAllPermissions(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| the username filter, list includes all users if unspecified | [optional] 
 **permissions** | **String**| comma separated list of permissions for project or issue returned users must have, see                     &lt;a href&#x3D;\&quot;https://developer.atlassian.com/static/javadoc/jira/6.0/reference/com/atlassian/jira/security/Permissions.Permission.html\&quot;&gt;Permissions&lt;/a&gt;                     JavaDoc for the list of all possible permissions. | [optional] 
 **issueKey** | **String**| the issue key for the issue for which returned users have specified permissions. | [optional] 
 **projectKey** | **String**| the optional project key to search for users with if no issueKey is supplied. | [optional] 
 **startAt** | **Number**| the index of the first user to return (0-based) | [optional] 
 **maxResults** | **Number**| the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                     If you specify a value that is higher than this number, your search results will be truncated. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## findUsersWithBrowsePermission

> findUsersWithBrowsePermission(opts)



Returns a list of active users that match the search string. This resource cannot be accessed anonymously   and requires the Browse Users global permission.  Given an issue key this resource will provide a list of users that match the search string and have  the browse issue permission for the issue provided.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'username': "username_example", // String | the username filter, no users returned if left blank
  'issueKey': "issueKey_example", // String | the issue key for the issue being edited we need to find viewable users for.
  'projectKey': "projectKey_example", // String | the optional project key to search for users with if no issueKey is supplied.
  'startAt': 56, // Number | the index of the first user to return (0-based)
  'maxResults': 56 // Number | the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                    If you specify a value that is higher than this number, your search results will be truncated.
};
apiInstance.findUsersWithBrowsePermission(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| the username filter, no users returned if left blank | [optional] 
 **issueKey** | **String**| the issue key for the issue being edited we need to find viewable users for. | [optional] 
 **projectKey** | **String**| the optional project key to search for users with if no issueKey is supplied. | [optional] 
 **startAt** | **Number**| the index of the first user to return (0-based) | [optional] 
 **maxResults** | **Number**| the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.                    If you specify a value that is higher than this number, your search results will be truncated. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fullyUpdateProjectRole

> fullyUpdateProjectRole(id)



Fully updates a roles. Both name and description must be given.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | 
apiInstance.fullyUpdateProjectRole(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## get

> get(key)



Returns the ApplicationRole with passed key if it exists.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let key = "key_example"; // String | the key of the role to update.
apiInstance.get(key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| the key of the role to update. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAccessibleProjectTypeByKey

> getAccessibleProjectTypeByKey(projectTypeKey)



Returns the project type with the given key, if it is accessible to the logged in user.  This takes into account whether the user is licensed on the Application that defines the project type.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectTypeKey = "projectTypeKey_example"; // String | 
apiInstance.getAccessibleProjectTypeByKey(projectTypeKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectTypeKey** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAdvancedSettings

> getAdvancedSettings()



Returns the properties that are displayed on the \&quot;General Configuration &gt; Advanced Settings\&quot; page.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getAdvancedSettings((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getAll

> getAll()



Returns all ApplicationRoles in the system. Will also return an ETag header containing a version hash of the  collection of ApplicationRoles.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getAll((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getAllFields

> getAllFields(screenId, tabId, opts)



Gets all fields for a given tab

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let screenId = 789; // Number | id of screen
let tabId = 789; // Number | id of tab
let opts = {
  'projectKey': "projectKey_example" // String | the key of the project; this parameter is optional
};
apiInstance.getAllFields(screenId, tabId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screenId** | **Number**| id of screen | 
 **tabId** | **Number**| id of tab | 
 **projectKey** | **String**| the key of the project; this parameter is optional | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllPermissions

> getAllPermissions()



Returns all permissions that are present in the JIRA instance - Global, Project and the global ones added by plugins

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getAllPermissions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getAllProjectCategories

> getAllProjectCategories()



Returns all project categories

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getAllProjectCategories((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getAllProjectTypes

> getAllProjectTypes()



Returns all the project types defined on the JIRA instance, not taking into account whether  the license to use those project types is valid or not.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getAllProjectTypes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getAllProjects

> getAllProjects(opts)



Returns all projects which are visible for the currently logged in user. If no user is logged in, it returns the  list of projects that are visible when using anonymous access.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'expand': "expand_example", // String | the parameters to expand
  'recent': 56 // Number | if this parameter is set then only projects recently accessed by the current user (if not logged in then based on HTTP session) will be returned (maximum count limited to the specified number but no more than 20).
};
apiInstance.getAllProjects(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **String**| the parameters to expand | [optional] 
 **recent** | **Number**| if this parameter is set then only projects recently accessed by the current user (if not logged in then based on HTTP session) will be returned (maximum count limited to the specified number but no more than 20). | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllStatuses

> getAllStatuses(projectIdOrKey)



Get all issue types with valid status values for a project

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | Project id or project key
apiInstance.getAllStatuses(projectIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| Project id or project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllSystemAvatars

> getAllSystemAvatars(type)



Returns all system avatars of the given type.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let type = "type_example"; // String | the avatar type
apiInstance.getAllSystemAvatars(type, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **String**| the avatar type | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllTabs

> getAllTabs(screenId, opts)



Returns a list of all tabs for the given screen

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let screenId = 789; // Number | id of screen
let opts = {
  'projectKey': "projectKey_example" // String | the key of the project; this parameter is optional
};
apiInstance.getAllTabs(screenId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screenId** | **Number**| id of screen | 
 **projectKey** | **String**| the key of the project; this parameter is optional | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllWorkflows

> getAllWorkflows(opts)



Returns all workflows.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'workflowName': "workflowName_example" // String | 
};
apiInstance.getAllWorkflows(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflowName** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAlternativeIssueTypes

> getAlternativeIssueTypes(id)



Returns a list of all alternative issue types for the given issue type id. The list will contain these issues types, to which  issues assigned to the given issue type can be migrated. The suitable alternatives are issue types which are assigned  to the same workflow, the same field configuration and the same screen scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | 
apiInstance.getAlternativeIssueTypes(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAssignedPermissionScheme

> getAssignedPermissionScheme(projectKeyOrId, opts)



Gets a permission scheme assigned with a project.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectKeyOrId = "projectKeyOrId_example"; // String | key or id of the project
let opts = {
  'expand': "expand_example" // String | 
};
apiInstance.getAssignedPermissionScheme(projectKeyOrId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectKeyOrId** | **String**| key or id of the project | 
 **expand** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAttachment

> getAttachment(id)



Returns the meta-data for an attachment, including the URI of the actual attached file.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | id of the attachment to remove
apiInstance.getAttachment(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| id of the attachment to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAttachmentMeta

> getAttachmentMeta()



Returns the meta information for an attachments, specifically if they are enabled and the maximum upload size  allowed.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getAttachmentMeta((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getAutoComplete

> getAutoComplete()



Returns the auto complete data required for JQL searches.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getAutoComplete((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getAvailableMetrics

> getAvailableMetrics()



### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getAvailableMetrics((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getAvatars

> getAvatars(type, owningObjectId)



### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let type = "type_example"; // String | 
let owningObjectId = "owningObjectId_example"; // String | 
apiInstance.getAvatars(type, owningObjectId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **String**|  | 
 **owningObjectId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getById

> getById(id, opts)



Returns the requested workflow scheme to the caller.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the scheme.
let opts = {
  'returnDraftIfExists': false // Boolean | when true indicates that a scheme's draft, if it exists, should be queried instead of                             the scheme itself.
};
apiInstance.getById(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the scheme. | 
 **returnDraftIfExists** | **Boolean**| when true indicates that a scheme&#39;s draft, if it exists, should be queried instead of                             the scheme itself. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getComment

> getComment(issueIdOrKey, id, opts)



Returns a single comment.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | of the issue the comment belongs to
let id = "id_example"; // String | the ID of the comment to request
let opts = {
  'expand': "expand_example" // String | optional flags: renderedBody (provides body rendered in HTML)
};
apiInstance.getComment(issueIdOrKey, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| of the issue the comment belongs to | 
 **id** | **String**| the ID of the comment to request | 
 **expand** | **String**| optional flags: renderedBody (provides body rendered in HTML) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getComments

> getComments(issueIdOrKey, opts)



Returns all comments for an issue.  &lt;p&gt;  Results can be ordered by the \&quot;created\&quot; field which means the date a comment was added.  &lt;/p&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | a string containing the issue id or key the comment will be added to
let opts = {
  'startAt': 789, // Number | the page offset, if not specified then defaults to 0
  'maxResults': 56, // Number | how many results on the page should be included. Defaults to 50.
  'orderBy': "orderBy_example", // String | ordering of the results.
  'expand': "expand_example" // String | optional flags: renderedBody (provides body rendered in HTML)
};
apiInstance.getComments(issueIdOrKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| a string containing the issue id or key the comment will be added to | 
 **startAt** | **Number**| the page offset, if not specified then defaults to 0 | [optional] 
 **maxResults** | **Number**| how many results on the page should be included. Defaults to 50. | [optional] 
 **orderBy** | **String**| ordering of the results. | [optional] 
 **expand** | **String**| optional flags: renderedBody (provides body rendered in HTML) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getComponent

> getComponent(id)



Returns a project component.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | The component to delete.
apiInstance.getComponent(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The component to delete. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getComponentRelatedIssues

> getComponentRelatedIssues(id)



Returns counts of issues related to this component.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | a String containing the component id
apiInstance.getComponentRelatedIssues(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| a String containing the component id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getConfiguration

> getConfiguration()



Returns the information if the optional features in JIRA are enabled or disabled. If the time tracking is enabled,  it also returns the detailed information about time tracking configuration.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getConfiguration((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getCreateIssueMeta

> getCreateIssueMeta(opts)



Returns the meta data for creating issues. This includes the available projects, issue types and fields,  including field types and whether or not those fields are required.  Projects will not be returned if the user does not have permission to create issues in that project.  &lt;p/&gt;  The fields in the createmeta correspond to the fields in the create screen for the project/issuetype.  Fields not in the screen will not be in the createmeta.  &lt;p/&gt;  Fields will only be returned if &lt;code&gt;expand&#x3D;projects.issuetypes.fields&lt;/code&gt;.  &lt;p/&gt;  The results can be filtered by project and/or issue type, given by the query params.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'projectIds': "projectIds_example", // String | combined with the projectKeys param, lists the projects with which to filter the results. If absent, all projects are returned.                        This parameter can be specified multiple times, and/or be a comma-separated list.                        Specifiying a project that does not exist (or that you cannot create issues in) is not an error, but it will not be in the results.
  'projectKeys': "projectKeys_example", // String | combined with the projectIds param, lists the projects with which to filter the results. If null, all projects are returned.                        This parameter can be specified multiple times, and/or be a comma-separated list.                        Specifiying a project that does not exist (or that you cannot create issues in) is not an error, but it will not be in the results.
  'issuetypeIds': "issuetypeIds_example", // String | combinded with issuetypeNames, lists the issue types with which to filter the results. If null, all issue types are returned.                        This parameter can be specified multiple times, and/or be a comma-separated list.                        Specifiying an issue type that does not exist is not an error.
  'issuetypeNames': "issuetypeNames_example" // String | combinded with issuetypeIds, lists the issue types with which to filter the results. If null, all issue types are returned.                        This parameter can be specified multiple times, but is NOT interpreted as a comma-separated list.                        Specifiying an issue type that does not exist is not an error.
};
apiInstance.getCreateIssueMeta(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIds** | **String**| combined with the projectKeys param, lists the projects with which to filter the results. If absent, all projects are returned.                        This parameter can be specified multiple times, and/or be a comma-separated list.                        Specifiying a project that does not exist (or that you cannot create issues in) is not an error, but it will not be in the results. | [optional] 
 **projectKeys** | **String**| combined with the projectIds param, lists the projects with which to filter the results. If null, all projects are returned.                        This parameter can be specified multiple times, and/or be a comma-separated list.                        Specifiying a project that does not exist (or that you cannot create issues in) is not an error, but it will not be in the results. | [optional] 
 **issuetypeIds** | **String**| combinded with issuetypeNames, lists the issue types with which to filter the results. If null, all issue types are returned.                        This parameter can be specified multiple times, and/or be a comma-separated list.                        Specifiying an issue type that does not exist is not an error. | [optional] 
 **issuetypeNames** | **String**| combinded with issuetypeIds, lists the issue types with which to filter the results. If null, all issue types are returned.                        This parameter can be specified multiple times, but is NOT interpreted as a comma-separated list.                        Specifiying an issue type that does not exist is not an error. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCustomFieldOption

> getCustomFieldOption(id)



Returns a full representation of the Custom Field Option that has the given id.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | a String containing an Custom Field Option id
apiInstance.getCustomFieldOption(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| a String containing an Custom Field Option id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDashboard

> getDashboard(id)



Returns a single dashboard.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | the dashboard id
apiInstance.getDashboard(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| the dashboard id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDefault

> getDefault(id, opts)



Return the default workflow from the passed workflow scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the scheme.
let opts = {
  'returnDraftIfExists': false // Boolean | when true indicates that a scheme's draft, if it exists, should be queried instead of                             the scheme itself.
};
apiInstance.getDefault(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the scheme. | 
 **returnDraftIfExists** | **Boolean**| when true indicates that a scheme&#39;s draft, if it exists, should be queried instead of                             the scheme itself. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDefaultShareScope

> getDefaultShareScope()



Returns the default share scope of the logged-in user.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getDefaultShareScope((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getDraftById

> getDraftById(id)



Returns the requested draft workflow scheme to the caller.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the parent scheme.
apiInstance.getDraftById(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the parent scheme. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDraftDefault

> getDraftDefault(id)



Return the default workflow from the passed draft workflow scheme to the caller.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the parent scheme.
apiInstance.getDraftDefault(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the parent scheme. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDraftIssueType

> getDraftIssueType(issueType, id)



Returns the issue type mapping for the passed draft workflow scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueType = "issueType_example"; // String | the issue type being set.
let id = 789; // Number | the id of the parent scheme.
apiInstance.getDraftIssueType(issueType, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueType** | **String**| the issue type being set. | 
 **id** | **Number**| the id of the parent scheme. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDraftWorkflow

> getDraftWorkflow(id, opts)



Returns the draft workflow mappings or requested mapping to the caller.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the parent scheme.
let opts = {
  'workflowName': "workflowName_example" // String | the workflow mapping to return. Null can be passed to return all mappings. Must be a valid workflow name.
};
apiInstance.getDraftWorkflow(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the parent scheme. | 
 **workflowName** | **String**| the workflow mapping to return. Null can be passed to return all mappings. Must be a valid workflow name. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getEditIssueMeta

> getEditIssueMeta(issueIdOrKey)



Returns the meta data for editing an issue.  &lt;p/&gt;  The fields in the editmeta correspond to the fields in the edit screen for the issue.  Fields not in the screen will not be in the editmeta.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue whose edit meta data you want to view
apiInstance.getEditIssueMeta(issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| the issue whose edit meta data you want to view | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFavouriteFilters

> getFavouriteFilters(opts)



Returns the favourite filters of the logged-in user.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'expand': "expand_example", // String | the parameters to expand
  'enableSharedUsers': true // Boolean | enable calculating shared users collection
};
apiInstance.getFavouriteFilters(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **String**| the parameters to expand | [optional] 
 **enableSharedUsers** | **Boolean**| enable calculating shared users collection | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFieldAutoCompleteForQueryString

> getFieldAutoCompleteForQueryString(opts)



Returns auto complete suggestions for JQL search.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'fieldName': "fieldName_example", // String | the field name for which the suggestions are generated.
  'fieldValue': "fieldValue_example", // String | the portion of the field value that has already been provided by the user.
  'predicateName': "predicateName_example", // String | the predicate for which the suggestions are generated. Suggestions are generated only for: \"by\", \"from\" and \"to\".
  'predicateValue': "predicateValue_example" // String | the portion of the predicate value that has already been provided by the user.
};
apiInstance.getFieldAutoCompleteForQueryString(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fieldName** | **String**| the field name for which the suggestions are generated. | [optional] 
 **fieldValue** | **String**| the portion of the field value that has already been provided by the user. | [optional] 
 **predicateName** | **String**| the predicate for which the suggestions are generated. Suggestions are generated only for: \&quot;by\&quot;, \&quot;from\&quot; and \&quot;to\&quot;. | [optional] 
 **predicateValue** | **String**| the portion of the predicate value that has already been provided by the user. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFields

> getFields()



Returns a list of all fields, both System and Custom

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getFields((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getFieldsToAdd

> getFieldsToAdd(screenId)



Gets available fields for screen. i.e ones that haven&#39;t already been added.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let screenId = 789; // Number | id of screen
apiInstance.getFieldsToAdd(screenId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screenId** | **Number**| id of screen | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFilter

> getFilter(id, opts)



Returns a filter given an id

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the filter being looked up
let opts = {
  'expand': "expand_example", // String | the parameters to expand
  'enableSharedUsers': true // Boolean | enable calculating shared users collection
};
apiInstance.getFilter(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the filter being looked up | 
 **expand** | **String**| the parameters to expand | [optional] 
 **enableSharedUsers** | **Boolean**| enable calculating shared users collection | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGroup

> getGroup(opts)



Returns REST representation for the requested group. Allows to get list of active users belonging to the  specified group and its subgroups if \&quot;users\&quot; expand option is provided. You can page through users list by using  indexes in expand param. For example to get users from index 10 to index 15 use \&quot;users[10:15]\&quot; expand value. This  will return 6 users (if there are at least 16 users in this group). Indexes are 0-based and inclusive.  &lt;p&gt;  This resource is deprecated, please use group/member API instead.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'groupname': "groupname_example", // String | A name of requested group.
  'expand': "expand_example" // String | List of fields to expand. Currently only available expand is \"users\".
};
apiInstance.getGroup(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupname** | **String**| A name of requested group. | [optional] 
 **expand** | **String**| List of fields to expand. Currently only available expand is \&quot;users\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getIdsOfWorklogsDeletedSince

> getIdsOfWorklogsDeletedSince(opts)



Returns worklogs id and delete time of worklogs that was deleted since given time.  The returns set of worklogs is limited to 1000 elements.  This API will not return worklogs deleted during last minute.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'since': 0 // Number | a date time in unix timestamp format since when deleted worklogs will be returned.
};
apiInstance.getIdsOfWorklogsDeletedSince(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **Number**| a date time in unix timestamp format since when deleted worklogs will be returned. | [optional] [default to 0]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getIdsOfWorklogsModifiedSince

> getIdsOfWorklogsModifiedSince(opts)



Returns worklogs id and update time of worklogs that was updated since given time.  The returns set of worklogs is limited to 1000 elements.  This API will not return worklogs updated during last minute.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'since': 0 // Number | a date time in unix timestamp format since when updated worklogs will be returned.
};
apiInstance.getIdsOfWorklogsModifiedSince(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **Number**| a date time in unix timestamp format since when updated worklogs will be returned. | [optional] [default to 0]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getIndexSummary

> getIndexSummary()



Summarizes index condition of current node.  &lt;p/&gt;  Returned data consists of:  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;nodeId&lt;/code&gt; - Node identifier.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;reportTime&lt;/code&gt; - Time of this report creation.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;issueIndex&lt;/code&gt; - Summary of issue index status.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;replicationQueues&lt;/code&gt; - Map of index replication queues, where  keys represent nodes from which replication operations came from.&lt;/li&gt;  &lt;/ul&gt;  &lt;p/&gt;  &lt;code&gt;issueIndex&lt;/code&gt; can contain:  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;indexReadable&lt;/code&gt; - If &lt;code&gt;false&lt;/code&gt; the end point failed to read data from issue index  (check JIRA logs for detailed stack trace), otherwise &lt;code&gt;true&lt;/code&gt;.  When &lt;code&gt;false&lt;/code&gt; other fields of &lt;code&gt;issueIndex&lt;/code&gt; can be not visible.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;countInDatabase&lt;/code&gt; - Count of issues found in database.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;countInIndex&lt;/code&gt; - Count of issues found while querying index.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastUpdatedInDatabase&lt;/code&gt; - Time of last update of issue found in database.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastUpdatedInIndex&lt;/code&gt; - Time of last update of issue found while querying index.&lt;/li&gt;  &lt;/ul&gt;  &lt;p/&gt;  &lt;code&gt;replicationQueues&lt;/code&gt;&#39;s map values can contain:  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;lastConsumedOperation&lt;/code&gt; - Last executed index replication operation by current node from sending node&#39;s queue.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastConsumedOperation.id&lt;/code&gt; - Identifier of the operation.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastConsumedOperation.replicationTime&lt;/code&gt; - Time when the operation was sent to other nodes.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastOperationInQueue&lt;/code&gt; - Last index replication operation in sending node&#39;s queue.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastOperationInQueue.id&lt;/code&gt; - Identifier of the operation.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;lastOperationInQueue.replicationTime&lt;/code&gt; - Time when the operation was sent to other nodes.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;queueSize&lt;/code&gt; - Number of operations in queue from sending node to current node.&lt;/li&gt;  &lt;/ul&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getIndexSummary((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getIssue

> getIssue(issueIdOrKey, opts)



Returns a full representation of the issue for the given issue key.  &lt;p&gt;  An issue JSON consists of the issue key, a collection of fields,  a link to the workflow transition sub-resource, and (optionally) the HTML rendered values of any fields that support it  (e.g. if wiki syntax is enabled for the description or comments).  &lt;p&gt;  The &lt;code&gt;fields&lt;/code&gt; param (which can be specified multiple times) gives a comma-separated list of fields  to include in the response. This can be used to retrieve a subset of fields.  A particular field can be excluded by prefixing it with a minus.  &lt;p&gt;  By default, all (&lt;code&gt;*all&lt;/code&gt;) fields are returned in this get-issue resource. Note: the default is different  when doing a jql search -- the default there is just navigable fields (&lt;code&gt;*navigable&lt;/code&gt;).  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;*all&lt;/code&gt; - include all fields&lt;/li&gt;  &lt;li&gt;&lt;code&gt;*navigable&lt;/code&gt; - include just navigable fields&lt;/li&gt;  &lt;li&gt;&lt;code&gt;summary,comment&lt;/code&gt; - include just the summary and comments&lt;/li&gt;  &lt;li&gt;&lt;code&gt;-comment&lt;/code&gt; - include everything except comments (the default is &lt;code&gt;*all&lt;/code&gt; for get-issue)&lt;/li&gt;  &lt;li&gt;&lt;code&gt;*all,-comment&lt;/code&gt; - include everything except comments&lt;/li&gt;  &lt;/ul&gt;  &lt;p&gt;  The {@code properties} param is similar to {@code fields} and specifies a comma-separated list of issue  properties to include. Unlike {@code fields}, properties are not included by default. To include them all  send {@code ?properties&#x3D;*all}. You can also include only specified properties or exclude some properties  with a minus (-) sign.  &lt;p&gt;  &lt;ul&gt;  &lt;li&gt;{@code *all} - include all properties&lt;/li&gt;  &lt;li&gt;{@code *all, -prop1} - include all properties except {@code prop1} &lt;/li&gt;  &lt;li&gt;{@code prop1, prop1} - include {@code prop1} and {@code prop2} properties &lt;/li&gt;  &lt;/ul&gt;  &lt;/p&gt;  &lt;p/&gt;  JIRA will attempt to identify the issue by the &lt;code&gt;issueIdOrKey&lt;/code&gt; path parameter. This can be an issue id,  or an issue key. If the issue cannot be found via an exact match, JIRA will also look for the issue in a case-insensitive way, or  by looking to see if the issue was moved. In either of these cases, the request will proceed as normal (a 302 or other redirect  will &lt;b&gt;not&lt;/b&gt; be returned). The issue key contained in the response will indicate the current value of issue&#39;s key.  &lt;p/&gt;  The &lt;code&gt;expand&lt;/code&gt; param is used to include, hidden by default, parts of response. This can be used to include:  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;renderedFields&lt;/code&gt; - field values in HTML format&lt;/li&gt;  &lt;li&gt;&lt;code&gt;names&lt;/code&gt; - display name of each field&lt;/li&gt;  &lt;li&gt;&lt;code&gt;schema&lt;/code&gt; - schema for each field which describes a type of the field&lt;/li&gt;  &lt;li&gt;&lt;code&gt;transitions&lt;/code&gt; - all possible transitions for the given issue&lt;/li&gt;  &lt;li&gt;&lt;code&gt;operations&lt;/code&gt; - all possibles operations which may be applied on issue&lt;/li&gt;  &lt;li&gt;&lt;code&gt;editmeta&lt;/code&gt; - information about how each field may be edited. It contains field&#39;s schema as well.&lt;/li&gt;  &lt;li&gt;&lt;code&gt;changelog&lt;/code&gt; - history of all changes of the given issue&lt;/li&gt;  &lt;li&gt;&lt;code&gt;versionedRepresentations&lt;/code&gt; -  REST representations of all fields. Some field may contain more recent versions. RESET representations are numbered.  The greatest number always represents the most recent version. It is recommended that the most recent version is used.  version for these fields which provide a more recent REST representation.  After including &lt;code&gt;versionedRepresentations&lt;/code&gt; \&quot;fields\&quot; field become hidden.&lt;/li&gt;  &lt;/ul&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue id or key to update (i.e. JRA-1330)
let opts = {
  'fields': "fields_example", // String | the list of fields to return for the issue. By default, all fields are returned.
  'expand': "expand_example", // String | 
  'properties': "properties_example" // String | the list of properties to return for the issue. By default no properties are returned.
};
apiInstance.getIssue(issueIdOrKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| the issue id or key to update (i.e. JRA-1330) | 
 **fields** | **String**| the list of fields to return for the issue. By default, all fields are returned. | [optional] 
 **expand** | **String**|  | [optional] 
 **properties** | **String**| the list of properties to return for the issue. By default no properties are returned. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getIssueAllTypes

> getIssueAllTypes()



Returns a list of all issue types visible to the user

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getIssueAllTypes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getIssueLink

> getIssueLink(linkId)



Returns an issue link with the specified id.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let linkId = "linkId_example"; // String | the issue link id.
apiInstance.getIssueLink(linkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkId** | **String**| the issue link id. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getIssueLinkType

> getIssueLinkType(issueLinkTypeId)



Returns for a given issue link type id all information about this issue link type.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueLinkTypeId = "issueLinkTypeId_example"; // String | 
apiInstance.getIssueLinkType(issueLinkTypeId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueLinkTypeId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getIssueLinkTypes

> getIssueLinkTypes()



Returns a list of available issue link types, if issue linking is enabled.  Each issue link type has an id, a name and a label for the outward and inward link relationship.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getIssueLinkTypes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getIssueNavigatorDefaultColumns

> getIssueNavigatorDefaultColumns()



Returns the default system columns for issue navigator. Admin permission will be required.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getIssueNavigatorDefaultColumns((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getIssuePickerResource

> getIssuePickerResource(opts)



Returns suggested issues which match the auto-completion query for the user which executes this request. This REST  method will check the user&#39;s history and the user&#39;s browsing context and select this issues, which match the query.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'query': "query_example", // String | the query.
  'currentJQL': "currentJQL_example", // String | the JQL in context of which the request is executed. Only issues which match this JQL query will be included in results.
  'currentIssueKey': "currentIssueKey_example", // String | the key of the issue in context of which the request is executed. The issue which is in context will not be included in the auto-completion result, even if it matches the query.
  'currentProjectId': "currentProjectId_example", // String | the id of the project in context of which the request is executed. Suggested issues will be only from this project.
  'showSubTasks': true, // Boolean | if set to false, subtasks will not be included in the list.
  'showSubTaskParent': true // Boolean | if set to false and request is executed in context of a subtask, the parent issue will not be included in the auto-completion result, even if it matches the query.
};
apiInstance.getIssuePickerResource(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **String**| the query. | [optional] 
 **currentJQL** | **String**| the JQL in context of which the request is executed. Only issues which match this JQL query will be included in results. | [optional] 
 **currentIssueKey** | **String**| the key of the issue in context of which the request is executed. The issue which is in context will not be included in the auto-completion result, even if it matches the query. | [optional] 
 **currentProjectId** | **String**| the id of the project in context of which the request is executed. Suggested issues will be only from this project. | [optional] 
 **showSubTasks** | **Boolean**| if set to false, subtasks will not be included in the list. | [optional] 
 **showSubTaskParent** | **Boolean**| if set to false and request is executed in context of a subtask, the parent issue will not be included in the auto-completion result, even if it matches the query. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getIssueSecuritySchemes

> getIssueSecuritySchemes()



Returns all issue security schemes that are defined.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getIssueSecuritySchemes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getIssueWatchers

> getIssueWatchers(issueIdOrKey)



Returns the list of watchers for the issue with the given key.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | a String containing an issue key.
apiInstance.getIssueWatchers(issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| a String containing an issue key. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getIssueWorklog

> getIssueWorklog(issueIdOrKey)



Returns all work logs for an issue. &lt;br/&gt;  &lt;strong&gt;Note:&lt;/strong&gt; Work logs won&#39;t be returned if the Log work field is hidden for the project.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | a string containing the issue id or key the worklog will be added to
apiInstance.getIssueWorklog(issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| a string containing the issue id or key the worklog will be added to | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getIssuesecuritylevel

> getIssuesecuritylevel(id)



Returns a full representation of the security level that has the given id.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | a String containing an issue security level id
apiInstance.getIssuesecuritylevel(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| a String containing an issue security level id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNotificationSchemes

> getNotificationSchemes(opts)



Returns a &lt;a href&#x3D;\&quot;#pagination\&quot;&gt;paginated&lt;/a&gt; list of notification schemes. In order to access notification scheme, the calling user is  required to have permissions to administer at least one project associated with the requested notification scheme. Each scheme contains  a list of events and recipient configured to receive notifications for these events. Consumer should allow events without recipients to appear in response.  The list is ordered by the scheme&#39;s name.  Follow the documentation of /notificationscheme/{id} resource for all details about returned value.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'startAt': 789, // Number | the index of the first notification scheme to return (0 based).
  'maxResults': 56, // Number | the maximum number of notification schemes to return (max 50).
  'expand': "expand_example" // String | 
};
apiInstance.getNotificationSchemes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startAt** | **Number**| the index of the first notification scheme to return (0 based). | [optional] 
 **maxResults** | **Number**| the maximum number of notification schemes to return (max 50). | [optional] 
 **expand** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPasswordPolicy

> getPasswordPolicy(opts)



Returns the list of requirements for the current password policy. For example, \&quot;The password must have at least 10 characters.\&quot;,  \&quot;The password must not be similar to the user&#39;s name or email address.\&quot;, etc.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'hasOldPassword': false // Boolean | whether or not the user will be required to enter their current password.  Use                        {@code false} (the default) if this is a new user or if an administrator is forcibly changing                        another user's password.
};
apiInstance.getPasswordPolicy(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hasOldPassword** | **Boolean**| whether or not the user will be required to enter their current password.  Use                        {@code false} (the default) if this is a new user or if an administrator is forcibly changing                        another user&#39;s password. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPermissionScheme

> getPermissionScheme(schemeId, opts)



Returns a permission scheme identified by the given id.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let schemeId = 789; // Number | 
let opts = {
  'expand': "expand_example" // String | 
};
apiInstance.getPermissionScheme(schemeId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schemeId** | **Number**|  | 
 **expand** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPermissionSchemeGrant

> getPermissionSchemeGrant(permissionId, schemeId, opts)



Returns a permission grant identified by the given id.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let permissionId = 789; // Number | 
let schemeId = 789; // Number | 
let opts = {
  'expand': "expand_example" // String | 
};
apiInstance.getPermissionSchemeGrant(permissionId, schemeId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permissionId** | **Number**|  | 
 **schemeId** | **Number**|  | 
 **expand** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPermissionSchemeGrants

> getPermissionSchemeGrants(schemeId, opts)



Returns all permission grants of the given permission scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let schemeId = 789; // Number | 
let opts = {
  'expand': "expand_example" // String | 
};
apiInstance.getPermissionSchemeGrants(schemeId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schemeId** | **Number**|  | 
 **expand** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPermissionSchemes

> getPermissionSchemes(opts)



Returns a list of all permission schemes.  &lt;p&gt;  By default only shortened beans are returned. If you want to include permissions of all the schemes,  then specify the &lt;b&gt;permissions&lt;/b&gt; expand parameter. Permissions will be included also if you specify  any other expand parameter.  &lt;/p&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'expand': "expand_example" // String | 
};
apiInstance.getPermissionSchemes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPermissions

> getPermissions(opts)



Returns all permissions in the system and whether the currently logged in user has them. You can optionally provide a specific context to get permissions for  (projectKey OR projectId OR issueKey OR issueId)  &lt;ul&gt;  &lt;li&gt; When no context supplied the project related permissions will return true if the user has that permission in ANY project &lt;/li&gt;  &lt;li&gt; If a project context is provided, project related permissions will return true if the user has the permissions in the specified project.  For permissions that are determined using issue data (e.g Current Assignee), true will be returned if the user meets the permission criteria in ANY issue in that project &lt;/li&gt;  &lt;li&gt; If an issue context is provided, it will return whether or not the user has each permission in that specific issue&lt;/li&gt;  &lt;/ul&gt;  &lt;p&gt;  NB: The above means that for issue-level permissions (EDIT_ISSUE for example), hasPermission may be true when no context is provided, or when a project context is provided,  &lt;b&gt;but&lt;/b&gt; may be false for any given (or all) issues. This would occur (for example) if Reporters were given the EDIT_ISSUE permission. This is because  any user could be a reporter, except in the context of a concrete issue, where the reporter is known.  &lt;/p&gt;  &lt;p&gt;  Global permissions will still be returned for all scopes.  &lt;/p&gt;  &lt;p&gt;  Prior to version 6.4 this service returned project permissions with keys corresponding to com.atlassian.jira.security.Permissions.Permission constants.  Since 6.4 those keys are considered deprecated and this service returns system project permission keys corresponding to constants defined in com.atlassian.jira.permission.ProjectPermissions.  Permissions with legacy keys are still also returned for backwards compatibility, they are marked with an attribute deprecatedKey&#x3D;true.  The attribute is missing for project permissions with the current keys.  &lt;/p&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'projectKey': "projectKey_example", // String | - key of project to scope returned permissions for.
  'projectId': "projectId_example", // String | - id of project to scope returned permissions for.
  'issueKey': "issueKey_example", // String | - key of the issue to scope returned permissions for.
  'issueId': "issueId_example" // String | - id of the issue to scope returned permissions for.
};
apiInstance.getPermissions(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectKey** | **String**| - key of project to scope returned permissions for. | [optional] 
 **projectId** | **String**| - id of project to scope returned permissions for. | [optional] 
 **issueKey** | **String**| - key of the issue to scope returned permissions for. | [optional] 
 **issueId** | **String**| - id of the issue to scope returned permissions for. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPreference

> getPreference(opts)



Returns preference of the currently logged in user. Preference key must be provided as input parameter (key). The  value is returned exactly as it is. If key parameter is not provided or wrong - status code 404. If value is  found  - status code 200.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'key': "key_example" // String | - key of the preference to be returned.
};
apiInstance.getPreference(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| - key of the preference to be returned. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPriorities

> getPriorities()



Returns a list of all issue priorities.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getPriorities((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getPriority

> getPriority(id)



Returns an issue priority.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | a String containing the priority id
apiInstance.getPriority(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| a String containing the priority id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProgress

> getProgress(requestId)



Retrieves the progress of a single reindex request.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let requestId = 789; // Number | the reindex request ID.
apiInstance.getProgress(requestId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestId** | **Number**| the reindex request ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProgressBulk

> getProgressBulk(opts)



Retrieves the progress of a multiple reindex requests.  Only reindex requests that actually exist will be returned  in the results.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'requestId': "requestId_example" // String | the reindex request IDs.
};
apiInstance.getProgressBulk(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestId** | **String**| the reindex request IDs. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProjectCategoryById

> getProjectCategoryById(id)



Contains a representation of a project category in JSON format.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | 
apiInstance.getProjectCategoryById(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProjectComponents

> getProjectComponents(projectIdOrKey)



Contains a full representation of a the specified project&#39;s components.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
apiInstance.getProjectComponents(projectIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| the project id or project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProjectRole

> getProjectRole(projectIdOrKey, id)



Returns the details for a given project role in a project.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
let id = 789; // Number | the project role id
apiInstance.getProjectRole(projectIdOrKey, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| the project id or project key | 
 **id** | **Number**| the project role id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProjectRoleActorsForRole

> getProjectRoleActorsForRole(id)



Gets default actors for the given role.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the role id to remove the actors from
apiInstance.getProjectRoleActorsForRole(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the role id to remove the actors from | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProjectRolesById

> getProjectRolesById(id)



Get a specific ProjectRole available in JIRA.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | 
apiInstance.getProjectRolesById(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProjectTypeByKey

> getProjectTypeByKey(projectTypeKey)



Returns the project type with the given key.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectTypeKey = "projectTypeKey_example"; // String | 
apiInstance.getProjectTypeByKey(projectTypeKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectTypeKey** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProjectVersions

> getProjectVersions(projectIdOrKey, opts)



Contains a full representation of a the specified project&#39;s versions.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
let opts = {
  'expand': "expand_example" // String | the parameters to expand
};
apiInstance.getProjectVersions(projectIdOrKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| the project id or project key | 
 **expand** | **String**| the parameters to expand | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProjectVersionsPaginated

> getProjectVersionsPaginated(projectIdOrKey, opts)



Returns all versions for the specified project. Results are &lt;a href&#x3D;\&quot;#pagination\&quot;&gt;paginated&lt;/a&gt;.  &lt;p&gt;  Results can be ordered by the following fields:  &lt;ul&gt;  &lt;li&gt;sequence&lt;/li&gt;  &lt;li&gt;name&lt;/li&gt;  &lt;li&gt;startDate&lt;/li&gt;  &lt;li&gt;releaseDate&lt;/li&gt;  &lt;/ul&gt;  &lt;/p&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
let opts = {
  'startAt': 789, // Number | the page offset, if not specified then defaults to 0
  'maxResults': 56, // Number | how many results on the page should be included. Defaults to 50.
  'orderBy': "orderBy_example", // String | ordering of the results.
  'expand': "expand_example" // String | the parameters to expand
};
apiInstance.getProjectVersionsPaginated(projectIdOrKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| the project id or project key | 
 **startAt** | **Number**| the page offset, if not specified then defaults to 0 | [optional] 
 **maxResults** | **Number**| how many results on the page should be included. Defaults to 50. | [optional] 
 **orderBy** | **String**| ordering of the results. | [optional] 
 **expand** | **String**| the parameters to expand | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProperties

> getProperties(id, opts)



Return the property or properties associated with a transition.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the ID of the transition within the workflow.
let opts = {
  'includeReservedKeys': true, // Boolean | some keys under the \"jira.\" prefix are editable, some are not. Set this to true                             in order to include the non-editable keys in the response.
  'key': "key_example", // String | the name of the property key to query. Can be left off the query to return all properties.
  'workflowName': "workflowName_example", // String | the name of the workflow to use.
  'workflowMode': "workflowMode_example" // String | the type of workflow to use. Can either be \"live\" or \"draft\".
};
apiInstance.getProperties(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the ID of the transition within the workflow. | 
 **includeReservedKeys** | **Boolean**| some keys under the \&quot;jira.\&quot; prefix are editable, some are not. Set this to true                             in order to include the non-editable keys in the response. | [optional] 
 **key** | **String**| the name of the property key to query. Can be left off the query to return all properties. | [optional] 
 **workflowName** | **String**| the name of the workflow to use. | [optional] 
 **workflowMode** | **String**| the type of workflow to use. Can either be \&quot;live\&quot; or \&quot;draft\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPropertyKeys

> getPropertyKeys(issueTypeId)



Returns the keys of all properties for the issue type identified by the id.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueTypeId = "issueTypeId_example"; // String | the issue type from which the keys will be returned
apiInstance.getPropertyKeys(issueTypeId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueTypeId** | **String**| the issue type from which the keys will be returned | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRecords

> getRecords(opts)



Returns auditing records filtered using provided parameters

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'offset': 56, // Number | - the number of record from which search starts
  'limit': 56, // Number | - maximum number of returned results (if is limit is <= 0 or > 1000, it will be set do default value: 1000)
  'filter': "filter_example", // String | - text query; each record that will be returned must contain the provided text in one of its fields
  'from': "from_example", // String | - timestamp in past; 'from' must be less or equal 'to', otherwise the result set will be empty                only records that where created in the same moment or after the 'from' timestamp will be provided in response
  'to': "to_example", // String | - timestamp in past; 'from' must be less or equal 'to', otherwise the result set will be empty                only records that where created in the same moment or earlier than the 'to' timestamp will be provided in response
  'projectIds': "projectIds_example", // String | - list of project ids to look for
  'userIds': "userIds_example" // String | - list of user ids to look for
};
apiInstance.getRecords(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **Number**| - the number of record from which search starts | [optional] 
 **limit** | **Number**| - maximum number of returned results (if is limit is &lt;&#x3D; 0 or &gt; 1000, it will be set do default value: 1000) | [optional] 
 **filter** | **String**| - text query; each record that will be returned must contain the provided text in one of its fields | [optional] 
 **from** | **String**| - timestamp in past; &#39;from&#39; must be less or equal &#39;to&#39;, otherwise the result set will be empty                only records that where created in the same moment or after the &#39;from&#39; timestamp will be provided in response | [optional] 
 **to** | **String**| - timestamp in past; &#39;from&#39; must be less or equal &#39;to&#39;, otherwise the result set will be empty                only records that where created in the same moment or earlier than the &#39;to&#39; timestamp will be provided in response | [optional] 
 **projectIds** | **String**| - list of project ids to look for | [optional] 
 **userIds** | **String**| - list of user ids to look for | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getReindexInfo

> getReindexInfo(opts)



Returns information on the system reindexes.  If a reindex is currently taking place then information about this reindex is returned.  If there is no active index task, then returns information about the latest reindex task run, otherwise returns a 404  indicating that no reindex has taken place.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'taskId': 789 // Number | the id of an indexing task you wish to obtain details on.  If omitted, then defaults to the standard behaviour and                returns information on the active reindex task, or the last task to run if no reindex is taking place. .  If there is no                reindexing task with that id then a 404 is returned.
};
apiInstance.getReindexInfo(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskId** | **Number**| the id of an indexing task you wish to obtain details on.  If omitted, then defaults to the standard behaviour and                returns information on the active reindex task, or the last task to run if no reindex is taking place. .  If there is no                reindexing task with that id then a 404 is returned. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getReindexProgress

> getReindexProgress(opts)



Returns information on the system reindexes.  If a reindex is currently taking place then information about this reindex is returned.  If there is no active index task, then returns information about the latest reindex task run, otherwise returns a 404  indicating that no reindex has taken place.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'taskId': 789 // Number | the id of an indexing task you wish to obtain details on.  If omitted, then defaults to the standard behaviour and                returns information on the active reindex task, or the last task to run if no reindex is taking place. .  If there is no                reindexing task with that id then a 404 is returned.
};
apiInstance.getReindexProgress(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskId** | **Number**| the id of an indexing task you wish to obtain details on.  If omitted, then defaults to the standard behaviour and                returns information on the active reindex task, or the last task to run if no reindex is taking place. .  If there is no                reindexing task with that id then a 404 is returned. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRemoteIssueLinkById

> getRemoteIssueLinkById(linkId, issueIdOrKey)



Get the remote issue link with the given id on the issue.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let linkId = "linkId_example"; // String | the id of the remote issue link
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue to create the remote issue link for
apiInstance.getRemoteIssueLinkById(linkId, issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkId** | **String**| the id of the remote issue link | 
 **issueIdOrKey** | **String**| the issue to create the remote issue link for | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRemoteIssueLinks

> getRemoteIssueLinks(issueIdOrKey, opts)



A REST sub-resource representing the remote issue links on the issue.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue to create the remote issue link for
let opts = {
  'globalId': "globalId_example" // String | The id of the remote issue link to be returned.  If null (not provided) all remote links for the                      issue are returned.                      <p>For a fullexplanation of Issue Link fields please refer to                      <a href=\"https://developer.atlassian.com/display/JIRADEV/Fields+in+Remote+Issue+Links\">https://developer.atlassian.com/display/JIRADEV/Fields+in+Remote+Issue+Links</a></p>
};
apiInstance.getRemoteIssueLinks(issueIdOrKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| the issue to create the remote issue link for | 
 **globalId** | **String**| The id of the remote issue link to be returned.  If null (not provided) all remote links for the                      issue are returned.                      &lt;p&gt;For a fullexplanation of Issue Link fields please refer to                      &lt;a href&#x3D;\&quot;https://developer.atlassian.com/display/JIRADEV/Fields+in+Remote+Issue+Links\&quot;&gt;https://developer.atlassian.com/display/JIRADEV/Fields+in+Remote+Issue+Links&lt;/a&gt;&lt;/p&gt; | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRemoteVersionLink

> getRemoteVersionLink(versionId, globalId)



A REST sub-resource representing a remote version link

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let versionId = "versionId_example"; // String | The version ID of the remote link
let globalId = "globalId_example"; // String | The global ID of the remote link
apiInstance.getRemoteVersionLink(versionId, globalId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionId** | **String**| The version ID of the remote link | 
 **globalId** | **String**| The global ID of the remote link | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRemoteVersionLinks

> getRemoteVersionLinks(opts)



Returns the remote version links for a given global ID.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'globalId': "globalId_example" // String | the global ID of the remote resource that is linked to the versions
};
apiInstance.getRemoteVersionLinks(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **globalId** | **String**| the global ID of the remote resource that is linked to the versions | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRemoteVersionLinksByVersionId

> getRemoteVersionLinksByVersionId(versionId)



Returns the remote version links associated with the given version ID.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let versionId = "versionId_example"; // String | The version for which to delete ALL existing remote version links
apiInstance.getRemoteVersionLinksByVersionId(versionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionId** | **String**| The version for which to delete ALL existing remote version links | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getResolution

> getResolution(id)



Returns a resolution.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | a String containing the resolution id
apiInstance.getResolution(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| a String containing the resolution id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getResolutions

> getResolutions()



Returns a list of all resolutions.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getResolutions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getSchemeAttribute

> getSchemeAttribute(permissionSchemeId, attributeKey)



### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let permissionSchemeId = 789; // Number | permission scheme id
let attributeKey = "attributeKey_example"; // String | permission scheme attribute key
apiInstance.getSchemeAttribute(permissionSchemeId, attributeKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permissionSchemeId** | **Number**| permission scheme id | 
 **attributeKey** | **String**| permission scheme attribute key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSecurityLevelsForProject

> getSecurityLevelsForProject(projectKeyOrId)



Returns all security levels for the project that the current logged in user has access to.  If the user does not have the Set Issue Security permission, the list will be empty.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectKeyOrId = "projectKeyOrId_example"; // String | - key or id of project to list the security levels for
apiInstance.getSecurityLevelsForProject(projectKeyOrId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectKeyOrId** | **String**| - key or id of project to list the security levels for | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getServerInfo

> getServerInfo(opts)



Returns general information about the current JIRA server.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'doHealthCheck': true // Boolean | 
};
apiInstance.getServerInfo(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doHealthCheck** | **Boolean**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSharePermission

> getSharePermission(permissionId, id)



Returns a single share permission of the given filter.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let permissionId = 789; // Number | 
let id = 789; // Number | 
apiInstance.getSharePermission(permissionId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permissionId** | **Number**|  | 
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSharePermissions

> getSharePermissions(id)



Returns all share permissions of the given filter.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | 
apiInstance.getSharePermissions(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getState

> getState()



### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getState((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getStatus

> getStatus(idOrName)



Returns a full representation of the Status having the given id or name.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let idOrName = "idOrName_example"; // String | a numeric Status id or a status name
apiInstance.getStatus(idOrName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idOrName** | **String**| a numeric Status id or a status name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getStatusCategories

> getStatusCategories()



Returns a list of all status categories

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getStatusCategories((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getStatusCategory

> getStatusCategory(idOrKey)



Returns a full representation of the StatusCategory having the given id or key

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let idOrKey = "idOrKey_example"; // String | a numeric StatusCategory id or a status category key
apiInstance.getStatusCategory(idOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idOrKey** | **String**| a numeric StatusCategory id or a status category key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getStatuses

> getStatuses()



Returns a list of all statuses

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getStatuses((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getSubTasks

> getSubTasks(issueIdOrKey)



Returns an issue&#39;s subtask list

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | The parent issue's key or id
apiInstance.getSubTasks(issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| The parent issue&#39;s key or id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getTransitions

> getTransitions(issueIdOrKey, opts)



Get a list of the transitions possible for this issue by the current user, along with fields that are required and their types.  &lt;p/&gt;  Fields will only be returned if &lt;code&gt;expand&#x3D;transitions.fields&lt;/code&gt;.  &lt;p/&gt;  The fields in the metadata correspond to the fields in the transition screen for that transition.  Fields not in the screen will not be in the metadata.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue whose transitions you want to view
let opts = {
  'transitionId': "transitionId_example" // String | 
};
apiInstance.getTransitions(issueIdOrKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| the issue whose transitions you want to view | 
 **transitionId** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getUpgradeResult

> getUpgradeResult()



Returns the result of the last upgrade task.   Returns {@link javax.ws.rs.core.Response#seeOther(java.net.URI)} if still running.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getUpgradeResult((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getUsersFromGroup

> getUsersFromGroup(opts)



This resource returns a &lt;a href&#x3D;\&quot;#pagination\&quot;&gt;paginated&lt;/a&gt; list of users who are members of the specified group and its subgroups.  Users in the page are ordered by user names. User of this resource is required to have sysadmin or admin permissions.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'groupname': "groupname_example", // String | a name of the group for which members will be returned.
  'includeInactiveUsers': false, // Boolean | inactive users will be included in the response if set to true.
  'startAt': 0, // Number | the index of the first user in group to return (0 based).
  'maxResults': 50 // Number | the maximum number of users to return (max 50).
};
apiInstance.getUsersFromGroup(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupname** | **String**| a name of the group for which members will be returned. | [optional] 
 **includeInactiveUsers** | **Boolean**| inactive users will be included in the response if set to true. | [optional] [default to false]
 **startAt** | **Number**| the index of the first user in group to return (0 based). | [optional] [default to 0]
 **maxResults** | **Number**| the maximum number of users to return (max 50). | [optional] [default to 50]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVersion

> getVersion(id, opts)



Returns a project version.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | The version to delete
let opts = {
  'expand': "expand_example" // String | 
};
apiInstance.getVersion(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The version to delete | 
 **expand** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVersionRelatedIssues

> getVersionRelatedIssues(id)



Returns a bean containing the number of fixed in and affected issues for the given version.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | a String containing the version id
apiInstance.getVersionRelatedIssues(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| a String containing the version id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVersionUnresolvedIssues

> getVersionUnresolvedIssues(id)



Returns the number of unresolved issues for the given version

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | a String containing the version id
apiInstance.getVersionUnresolvedIssues(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| a String containing the version id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVotes

> getVotes(issueIdOrKey)



A REST sub-resource representing the voters on the issue.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue to view voting information for
apiInstance.getVotes(issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| the issue to view voting information for | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getWorkflow

> getWorkflow(id, opts)



Returns the workflow mappings or requested mapping to the caller for the passed scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the scheme.
let opts = {
  'workflowName': "workflowName_example", // String | the workflow mapping to return. Null can be passed to return all mappings. Must be a valid workflow name.
  'returnDraftIfExists': false // Boolean | when true indicates that a scheme's draft, if it exists, should be queried instead of                             the scheme itself.
};
apiInstance.getWorkflow(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the scheme. | 
 **workflowName** | **String**| the workflow mapping to return. Null can be passed to return all mappings. Must be a valid workflow name. | [optional] 
 **returnDraftIfExists** | **Boolean**| when true indicates that a scheme&#39;s draft, if it exists, should be queried instead of                             the scheme itself. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getWorklog

> getWorklog(issueIdOrKey, id)



Returns a specific worklog. &lt;br/&gt;  &lt;strong&gt;Note:&lt;/strong&gt; The work log won&#39;t be returned if the Log work field is hidden for the project.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | a string containing the issue id or key the worklog belongs to
let id = "id_example"; // String | id of the worklog to be deleted
apiInstance.getWorklog(issueIdOrKey, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| a string containing the issue id or key the worklog belongs to | 
 **id** | **String**| id of the worklog to be deleted | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getWorklogsForIds

> getWorklogsForIds()



Returns worklogs for given worklog ids. Only worklogs to which the calling user has permissions, will be included in the result.  The returns set of worklogs is limited to 1000 elements.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.getWorklogsForIds((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## linkIssues

> linkIssues()



Creates an issue link between two issues.  The user requires the link issue permission for the issue which will be linked to another issue.  The specified link type in the request is used to create the link and will create a link from the first issue  to the second issue using the outward description. It also create a link from the second issue to the first issue using the  inward description of the issue link type.  It will add the supplied comment to the first issue. The comment can have a restriction who can view it.  If group is specified, only users of this group can view this comment, if roleLevel is specified only users who have the specified role can view this comment.  The user who creates the issue link needs to belong to the specified group or have the specified role.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.linkIssues((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## list

> list(opts)



Returns a list of all dashboards, optionally filtering them.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'filter': "filter_example", // String | an optional filter that is applied to the list of dashboards. Valid values include                         <code>\"favourite\"</code> for returning only favourite dashboards, and <code>\"my\"</code> for returning                         dashboards that are owned by the calling user.
  'startAt': 56, // Number | the index of the first dashboard to return (0-based). must be 0 or a multiple of                         <code>maxResults</code>
  'maxResults': 56 // Number | a hint as to the the maximum number of dashboards to return in each call. Note that the                         JIRA server reserves the right to impose a <code>maxResults</code> limit that is lower than the value that a                         client provides, dues to lack or resources or any other condition. When this happens, your results will be                         truncated. Callers should always check the returned <code>maxResults</code> to determine the value that is                         effectively being used.
};
apiInstance.list(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **String**| an optional filter that is applied to the list of dashboards. Valid values include                         &lt;code&gt;\&quot;favourite\&quot;&lt;/code&gt; for returning only favourite dashboards, and &lt;code&gt;\&quot;my\&quot;&lt;/code&gt; for returning                         dashboards that are owned by the calling user. | [optional] 
 **startAt** | **Number**| the index of the first dashboard to return (0-based). must be 0 or a multiple of                         &lt;code&gt;maxResults&lt;/code&gt; | [optional] 
 **maxResults** | **Number**| a hint as to the the maximum number of dashboards to return in each call. Note that the                         JIRA server reserves the right to impose a &lt;code&gt;maxResults&lt;/code&gt; limit that is lower than the value that a                         client provides, dues to lack or resources or any other condition. When this happens, your results will be                         truncated. Callers should always check the returned &lt;code&gt;maxResults&lt;/code&gt; to determine the value that is                         effectively being used. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## login

> login()



Creates a new session for a user in JIRA. Once a session has been successfully created it can be used to access  any of JIRA&#39;s remote APIs and also the web UI by passing the appropriate HTTP Cookie header.  &lt;p&gt;  Note that it is generally preferrable to use HTTP BASIC authentication with the REST API. However, this resource  may be used to mimic the behaviour of JIRA&#39;s log-in page (e.g. to display log-in errors to a user).

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.login((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## logout

> logout()



Logs the current user out of JIRA, destroying the existing session, if any.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.logout((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## merge

> merge(moveIssuesTo, id)



Merge versions

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let moveIssuesTo = "moveIssuesTo_example"; // String | The version to set fixVersion to on issues where the deleted version is the fix version,                      If null then the fixVersion is removed.
let id = "id_example"; // String | The version that will be merged to version {@code moveIssuesTo} and removed
apiInstance.merge(moveIssuesTo, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moveIssuesTo** | **String**| The version to set fixVersion to on issues where the deleted version is the fix version,                      If null then the fixVersion is removed. | 
 **id** | **String**| The version that will be merged to version {@code moveIssuesTo} and removed | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## moveField

> moveField(screenId, tabId, id)



Moves field on the given tab

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let screenId = 789; // Number | id of screen
let tabId = 789; // Number | id of tab
let id = "id_example"; // String | 
apiInstance.moveField(screenId, tabId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screenId** | **Number**| id of screen | 
 **tabId** | **Number**| id of tab | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## moveSubTasks

> moveSubTasks(issueIdOrKey)



Reorders an issue&#39;s subtasks by moving the subtask at index \&quot;from\&quot;  to index \&quot;to\&quot;.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | The parent issue's key or id
apiInstance.moveSubTasks(issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| The parent issue&#39;s key or id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## moveTab

> moveTab(screenId, tabId, pos)



Moves tab position

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let screenId = 789; // Number | id of screen
let tabId = 789; // Number | id of tab
let pos = 56; // Number | position of tab
apiInstance.moveTab(screenId, tabId, pos, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screenId** | **Number**| id of screen | 
 **tabId** | **Number**| id of tab | 
 **pos** | **Number**| position of tab | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## moveVersion

> moveVersion(id)



Modify a version&#39;s sequence within a project.  &lt;p/&gt;  The move version bean has 2 alternative field value pairs:  &lt;dl&gt;  &lt;dt&gt;position&lt;/dt&gt;&lt;dd&gt;An absolute position, which may have a value of &#39;First&#39;, &#39;Last&#39;, &#39;Earlier&#39; or &#39;Later&#39;&lt;/dd&gt;  &lt;dt&gt;after&lt;/dt&gt;&lt;dd&gt;A version to place this version after.  The value should be the self link of another version&lt;/dd&gt;  &lt;/dl&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | a String containing the version id
apiInstance.moveVersion(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| a String containing the version id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## notify

> notify(issueIdOrKey)



Sends a notification (email) to the list or recipients defined in the request.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | a string containing the issue id or key the comment will be added to
apiInstance.notify(issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| a string containing the issue id or key the comment will be added to | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## partialUpdateProjectRole

> partialUpdateProjectRole(id)



Partially updates a roles name or description.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | 
apiInstance.partialUpdateProjectRole(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## policyCheckCreateUser

> policyCheckCreateUser()



Returns a list of statements explaining why the password policy would disallow a proposed password for a new user.  &lt;p&gt;  You can use this method to test the password policy validation. This could be done prior to an action   where a new user and related password are created, using methods like the ones in   &lt;a href&#x3D;\&quot;https://docs.atlassian.com/jira/latest/com/atlassian/jira/bc/user/UserService.html\&quot;&gt;UserService&lt;/a&gt;.        For example, you could use this to validate a password in a create user form in the user interface, as the user enters it.&lt;br/&gt;  The username and new password must be not empty to perform the validation.&lt;br/&gt;  Note, this method will help you validate against the policy only. It won&#39;t check any other validations that might be performed   when creating a new user, e.g. checking whether a user with the same name already exists.  &lt;/p&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.policyCheckCreateUser((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## policyCheckUpdateUser

> policyCheckUpdateUser()



Returns a list of statements explaining why the password policy would disallow a proposed new password for a user with an existing password.  &lt;p&gt;  You can use this method to test the password policy validation. This could be done prior to an action where the password   is actually updated, using methods like &lt;a href&#x3D;\&quot;https://docs.atlassian.com/jira/latest/com/atlassian/jira/web/action/user/ChangePassword.html\&quot;&gt;ChangePassword&lt;/a&gt;        or &lt;a href&#x3D;\&quot;https://docs.atlassian.com/jira/latest/com/atlassian/jira/web/action/user/ResetPassword.html\&quot;&gt;ResetPassword&lt;/a&gt;.   For example, you could use this to validate a password in a change password form in the user interface, as the user enters it.&lt;br/&gt;  The user must exist and the username and new password must be not empty, to perform the validation.&lt;br/&gt;  Note, this method will help you validate against the policy only. It won&#39;t check any other validations that might be performed   when submitting a password change/reset request, e.g. verifying whether the old password is valid.  &lt;/p&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.policyCheckUpdateUser((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## processRequests

> processRequests()



Executes any pending reindex requests.  Returns a JSON array containing the IDs of the reindex requests  that are being processed.  Execution is asynchronous - progress of the returned tasks can be monitored through  other REST calls.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.processRequests((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## put

> put(key, opts)



Updates the ApplicationRole with the passed data. Only the groups and default groups setting of the  role may be updated. Requests to change the key or the name of the role will be silently ignored.  &lt;p&gt;  Optional: If versionHash is passed through the If-Match header the request will be rejected if not the  same as server

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let key = "key_example"; // String | the key of the role to update.
let opts = {
  'ifMatch': "ifMatch_example" // String | the hash of the version to update. Optional Param
};
apiInstance.put(key, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| the key of the role to update. | 
 **ifMatch** | **String**| the hash of the version to update. Optional Param | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## putBulk

> putBulk(opts)



Updates the ApplicationRoles with the passed data if the version hash is the same as the server.  Only the groups and default groups setting of the role may be updated. Requests to change the key  or the name of the role will be silently ignored. It is acceptable to pass only the roles that are updated  as roles that are present in the server but not in data to update with, will not be deleted.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'ifMatch': "ifMatch_example" // String | 
};
apiInstance.putBulk(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ifMatch** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reindex

> reindex(opts)



Kicks off a reindex.  Need Admin permissions to perform this reindex.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'type': "type_example", // String | Case insensitive String indicating type of reindex.  If omitted, then defaults to BACKGROUND_PREFERRED.
  'indexComments': false, // Boolean | Indicates that comments should also be reindexed. Not relevant for foreground reindex, where comments are always reindexed.
  'indexChangeHistory': false, // Boolean | Indicates that changeHistory should also be reindexed. Not relevant for foreground reindex, where changeHistory is always reindexed.
  'indexWorklogs': false // Boolean | Indicates that changeHistory should also be reindexed. Not relevant for foreground reindex, where changeHistory is always reindexed.
};
apiInstance.reindex(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **String**| Case insensitive String indicating type of reindex.  If omitted, then defaults to BACKGROUND_PREFERRED. | [optional] 
 **indexComments** | **Boolean**| Indicates that comments should also be reindexed. Not relevant for foreground reindex, where comments are always reindexed. | [optional] [default to false]
 **indexChangeHistory** | **Boolean**| Indicates that changeHistory should also be reindexed. Not relevant for foreground reindex, where changeHistory is always reindexed. | [optional] [default to false]
 **indexWorklogs** | **Boolean**| Indicates that changeHistory should also be reindexed. Not relevant for foreground reindex, where changeHistory is always reindexed. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reindexIssues

> reindexIssues(opts)



Reindexes one or more individual issues.  Indexing is performed synchronously - the call returns when indexing of  the issues has completed or a failure occurs.  &lt;p&gt;  Use either explicitly specified issue IDs or a JQL query to select issues to reindex.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'issueId': "issueId_example", // String | the IDs or keys of one or more issues to reindex.
  'indexComments': false, // Boolean | Indicates that comments should also be reindexed.
  'indexChangeHistory': false, // Boolean | Indicates that changeHistory should also be reindexed.
  'indexWorklogs': false // Boolean | Indicates that changeHistory should also be reindexed.
};
apiInstance.reindexIssues(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueId** | **String**| the IDs or keys of one or more issues to reindex. | [optional] 
 **indexComments** | **Boolean**| Indicates that comments should also be reindexed. | [optional] [default to false]
 **indexChangeHistory** | **Boolean**| Indicates that changeHistory should also be reindexed. | [optional] [default to false]
 **indexWorklogs** | **Boolean**| Indicates that changeHistory should also be reindexed. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## release

> release()



This method invalidates the any current WebSudo session.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.release((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## removeAttachment

> removeAttachment(id)



Remove an attachment from an issue.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | id of the attachment to remove
apiInstance.removeAttachment(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| id of the attachment to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeField

> removeField(screenId, tabId, id)



Removes field from given tab

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let screenId = 789; // Number | id of screen
let tabId = 789; // Number | id of tab
let id = "id_example"; // String | 
apiInstance.removeField(screenId, tabId, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screenId** | **Number**| id of screen | 
 **tabId** | **Number**| id of tab | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeGroup

> removeGroup(opts)



Deletes a group by given group parameter.  &lt;p&gt;  Returns no content

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'groupname': "groupname_example", // String | (mandatory) The name of the group to delete.
  'swapGroup': "swapGroup_example" // String | If you delete a group and content is restricted to that group, the content will be hidden from all users.   To prevent this, use this parameter to specify a different group to transfer the restrictions (comments and worklogs only) to.
};
apiInstance.removeGroup(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupname** | **String**| (mandatory) The name of the group to delete. | [optional] 
 **swapGroup** | **String**| If you delete a group and content is restricted to that group, the content will be hidden from all users.   To prevent this, use this parameter to specify a different group to transfer the restrictions (comments and worklogs only) to. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removePreference

> removePreference(opts)



Removes preference of the currently logged in user. Preference key must be provided as input parameters (key). If  key parameter is not provided or wrong - status code 404. If preference is unset - status code 204.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'key': "key_example" // String | - key of the preference to be removed.
};
apiInstance.removePreference(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| - key of the preference to be removed. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeProjectCategory

> removeProjectCategory(id)



Delete a project category.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | 
apiInstance.removeProjectCategory(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeUser

> removeUser(opts)



Removes user.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'username': "username_example", // String | the username
  'key': "key_example" // String | user key
};
apiInstance.removeUser(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| the username | [optional] 
 **key** | **String**| user key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeUserFromApplication

> removeUserFromApplication(opts)



Remove user from given application. Admin permission will be required to perform this operation.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'username': "username_example", // String | username
  'applicationKey': "applicationKey_example" // String | application key
};
apiInstance.removeUserFromApplication(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| username | [optional] 
 **applicationKey** | **String**| application key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeUserFromGroup

> removeUserFromGroup(opts)



Removes given user from a group.  &lt;p&gt;  Returns no content

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'groupname': "groupname_example", // String | A name of requested group.
  'username': "username_example" // String | User to remove from a group
};
apiInstance.removeUserFromGroup(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupname** | **String**| A name of requested group. | [optional] 
 **username** | **String**| User to remove from a group | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeVote

> removeVote(issueIdOrKey)



Remove your vote from an issue. (i.e. \&quot;unvote\&quot;)

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue to view voting information for
apiInstance.removeVote(issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| the issue to view voting information for | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeWatcher

> removeWatcher(issueIdOrKey, opts)



Removes a user from an issue&#39;s watcher list.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | a String containing an issue key.
let opts = {
  'username': "username_example" // String | a String containing the name of the user to remove from the watcher list. Must not be null.
};
apiInstance.removeWatcher(issueIdOrKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| a String containing an issue key. | 
 **username** | **String**| a String containing the name of the user to remove from the watcher list. Must not be null. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## renameTab

> renameTab(screenId, tabId)



Renames tab on given screen

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let screenId = 789; // Number | id of screen
let tabId = 789; // Number | id of tab
apiInstance.renameTab(screenId, tabId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screenId** | **Number**| id of screen | 
 **tabId** | **Number**| id of tab | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## runUpgradesNow

> runUpgradesNow()



Runs any pending delayed upgrade tasks.  Need Admin permissions to do this.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.runUpgradesNow((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## search

> search(opts)



Searches for issues using JQL.  &lt;p&gt;  &lt;b&gt;Sorting&lt;/b&gt;  the &lt;code&gt;jql&lt;/code&gt; parameter is a full &lt;a href&#x3D;\&quot;http://confluence.atlassian.com/display/JIRA/Advanced+Searching\&quot;&gt;JQL&lt;/a&gt;  expression, and includes an &lt;code&gt;ORDER BY&lt;/code&gt; clause.  &lt;/p&gt;  &lt;p&gt;  The &lt;code&gt;fields&lt;/code&gt; param (which can be specified multiple times) gives a comma-separated list of fields  to include in the response. This can be used to retrieve a subset of fields.  A particular field can be excluded by prefixing it with a minus.  &lt;p&gt;  By default, only navigable (&lt;code&gt;*navigable&lt;/code&gt;) fields are returned in this search resource. Note: the default is different  in the get-issue resource -- the default there all fields (&lt;code&gt;*all&lt;/code&gt;).  &lt;ul&gt;  &lt;li&gt;&lt;code&gt;*all&lt;/code&gt; - include all fields&lt;/li&gt;  &lt;li&gt;&lt;code&gt;*navigable&lt;/code&gt; - include just navigable fields&lt;/li&gt;  &lt;li&gt;&lt;code&gt;summary,comment&lt;/code&gt; - include just the summary and comments&lt;/li&gt;  &lt;li&gt;&lt;code&gt;-description&lt;/code&gt; - include navigable fields except the description (the default is &lt;code&gt;*navigable&lt;/code&gt; for search)&lt;/li&gt;  &lt;li&gt;&lt;code&gt;*all,-comment&lt;/code&gt; - include everything except comments&lt;/li&gt;  &lt;/ul&gt;  &lt;p&gt;  &lt;/p&gt;  &lt;p&gt;&lt;b&gt;GET vs POST:&lt;/b&gt;  If the JQL query is too large to be encoded as a query param you should instead  POST to this resource.  &lt;/p&gt;  &lt;p&gt;  &lt;b&gt;Expanding Issues in the Search Result:&lt;/b&gt;  It is possible to expand the issues returned by directly specifying the expansion on the expand parameter passed  in to this resources.  &lt;/p&gt;  &lt;p&gt;  For instance, to expand the &amp;quot;changelog&amp;quot; for all the issues on the search result, it is neccesary to  specify &amp;quot;changelog&amp;quot; as one of the values to expand.  &lt;/p&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'jql': "jql_example", // String | a JQL query string
  'startAt': 56, // Number | the index of the first issue to return (0-based)
  'maxResults': 56, // Number | the maximum number of issues to return (defaults to 50). The maximum allowable value is                       dictated by the JIRA property 'jira.search.views.default.max'. If you specify a value that is higher than this                       number, your search results will be truncated.
  'validateQuery': true, // Boolean | whether to validate the JQL query
  'fields': "fields_example", // String | the list of fields to return for each issue. By default, all navigable fields are returned.
  'expand': "expand_example" // String | A comma-separated list of the parameters to expand.
};
apiInstance.search(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jql** | **String**| a JQL query string | [optional] 
 **startAt** | **Number**| the index of the first issue to return (0-based) | [optional] 
 **maxResults** | **Number**| the maximum number of issues to return (defaults to 50). The maximum allowable value is                       dictated by the JIRA property &#39;jira.search.views.default.max&#39;. If you specify a value that is higher than this                       number, your search results will be truncated. | [optional] 
 **validateQuery** | **Boolean**| whether to validate the JQL query | [optional] [default to true]
 **fields** | **String**| the list of fields to return for each issue. By default, all navigable fields are returned. | [optional] 
 **expand** | **String**| A comma-separated list of the parameters to expand. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## searchUsingSearchRequest

> searchUsingSearchRequest()



Performs a search using JQL.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.searchUsingSearchRequest((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## setActors

> setActors(projectIdOrKey, id)



Updates a project role to include the specified actors (users or groups).

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
let id = 789; // Number | the project role id
apiInstance.setActors(projectIdOrKey, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| the project id or project key | 
 **id** | **Number**| the project role id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setBaseURL

> setBaseURL()



Sets the base URL that is configured for this JIRA instance.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.setBaseURL((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## setDefaultShareScope

> setDefaultShareScope()



Sets the default share scope of the logged-in user. Available values are GLOBAL and PRIVATE.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.setDefaultShareScope((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## setDraftIssueType

> setDraftIssueType(issueType, id)



Set the issue type mapping for the passed draft scheme.  &lt;p/&gt;  The passed representation can have its updateDraftIfNeeded flag set to true to indicate that  the draft should be created/updated when the actual scheme cannot be edited.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueType = "issueType_example"; // String | the issue type being set.
let id = 789; // Number | the id of the parent scheme.
apiInstance.setDraftIssueType(issueType, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueType** | **String**| the issue type being set. | 
 **id** | **Number**| the id of the parent scheme. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setIssueNavigatorDefaultColumns

> setIssueNavigatorDefaultColumns()



Sets the default system columns for issue navigator. Admin permission will be required.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.setIssueNavigatorDefaultColumns((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## setIssueType

> setIssueType(issueType, id)



Set the issue type mapping for the passed scheme.  &lt;p/&gt;  The passed representation can have its updateDraftIfNeeded flag set to true to indicate that  the draft should be created/updated when the actual scheme cannot be edited.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueType = "issueType_example"; // String | the issue type being set.
let id = 789; // Number | the id of the scheme.
apiInstance.setIssueType(issueType, id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueType** | **String**| the issue type being set. | 
 **id** | **Number**| the id of the scheme. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setPreference

> setPreference(opts)



Sets preference of the currently logged in user. Preference key must be provided as input parameters (key). Value  must be provided as post body. If key or value parameter is not provided - status code 404. If preference is set  - status code 204.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let opts = {
  'key': "key_example" // String | - key of the preference to be set.
};
apiInstance.setPreference(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| - key of the preference to be set. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setPropertyViaRestfulTable

> setPropertyViaRestfulTable(id)



Modify an application property via PUT. The \&quot;value\&quot; field present in the PUT will override the existing value.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | 
apiInstance.setPropertyViaRestfulTable(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setReadyToUpgrade

> setReadyToUpgrade()



### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.setReadyToUpgrade((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## setSchemeAttribute

> setSchemeAttribute(permissionSchemeId, key)



Updates or inserts the attribute for a permission scheme specified by permission scheme id.  The attribute consists of the key and the value. The value will be converted to Boolean using Boolean#valueOf.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let permissionSchemeId = 789; // Number | permission scheme id
let key = "key_example"; // String | permission scheme attribute key
apiInstance.setSchemeAttribute(permissionSchemeId, key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permissionSchemeId** | **Number**| permission scheme id | 
 **key** | **String**| permission scheme attribute key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## start

> start()



### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.start((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## stop

> stop()



### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.stop((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## storeTemporaryAvatar

> storeTemporaryAvatar(type, opts)



Creates temporary avatar

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let type = "type_example"; // String | the avatar type
let opts = {
  'filename': "filename_example", // String | name of file being uploaded
  'size': 789 // Number | size of file
};
apiInstance.storeTemporaryAvatar(type, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **String**| the avatar type | 
 **filename** | **String**| name of file being uploaded | [optional] 
 **size** | **Number**| size of file | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## update

> update(id)



Update the passed workflow scheme.  &lt;p/&gt;  The body of the request is a representation of the workflow scheme. Values not passed are assumed to indicate  no change for that field.  &lt;p/&gt;  The passed representation can have its updateDraftIfNeeded flag set to true to indicate that the draft  should be created and/or updated when the actual scheme cannot be edited (e.g. when the scheme is being used by  a project). Values not appearing the body will not be touched.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the scheme.
apiInstance.update(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the scheme. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateComment

> updateComment(issueIdOrKey, id, opts)



Updates an existing comment using its JSON representation.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | of the issue the comment belongs to
let id = "id_example"; // String | the ID of the comment to request
let opts = {
  'expand': "expand_example" // String | optional flags: renderedBody (provides body rendered in HTML)
};
apiInstance.updateComment(issueIdOrKey, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| of the issue the comment belongs to | 
 **id** | **String**| the ID of the comment to request | 
 **expand** | **String**| optional flags: renderedBody (provides body rendered in HTML) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateComponent

> updateComponent(id)



Modify a component via PUT. Any fields present in the PUT will override existing values. As a convenience, if a field  is not present, it is silently ignored.  &lt;p&gt;  If leadUserName is an empty string (\&quot;\&quot;) the component lead will be removed.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | The component to delete.
apiInstance.updateComponent(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The component to delete. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateDefault

> updateDefault(id)



Set the default workflow for the passed workflow scheme.  &lt;p/&gt;  The passed representation can have its  updateDraftIfNeeded flag set to true to indicate that the draft should be created/updated when the actual scheme  cannot be edited.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the scheme.
apiInstance.updateDefault(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the scheme. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateDraft

> updateDraft(id)



Update a draft workflow scheme. The draft will created if necessary.  &lt;p/&gt;  The body is a representation of the workflow scheme. Values not passed are assumed to indicate no change for that field.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the parent scheme.
apiInstance.updateDraft(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the parent scheme. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateDraftDefault

> updateDraftDefault(id)



Set the default workflow for the passed draft workflow scheme.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the parent scheme.
apiInstance.updateDraftDefault(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the parent scheme. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateDraftWorkflowMapping

> updateDraftWorkflowMapping(id, opts)



Update the draft scheme to include the passed mapping.  &lt;p/&gt;  The body is a representation of the workflow mapping.  Values not passed are assumed to indicate no change for that field.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the parent scheme.
let opts = {
  'workflowName': "workflowName_example" // String | the name of the workflow mapping to update.
};
apiInstance.updateDraftWorkflowMapping(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the parent scheme. | 
 **workflowName** | **String**| the name of the workflow mapping to update. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateIssueLinkType

> updateIssueLinkType(issueLinkTypeId)



Update the specified issue link type.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueLinkTypeId = "issueLinkTypeId_example"; // String | 
apiInstance.updateIssueLinkType(issueLinkTypeId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueLinkTypeId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateIssueType

> updateIssueType(id)



Updates the specified issue type from a JSON representation.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | the id of the issue type to update.
apiInstance.updateIssueType(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| the id of the issue type to update. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updatePermissionScheme

> updatePermissionScheme(schemeId, opts)



Updates a permission scheme.  &lt;p&gt;  If the permissions list is present then it will be set in the permission scheme, which basically means it will overwrite any permission grants that  existed in the permission scheme. Sending an empty list will remove all permission grants from the permission scheme.  &lt;/p&gt;  &lt;p&gt;  To update just the name and description, do not send permissions list at all.  &lt;/p&gt;  &lt;p&gt;  To add or remove a single permission grant instead of updating the whole list at once use the &lt;b&gt;{schemeId}/permission/&lt;/b&gt; resource.  &lt;/p&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let schemeId = 789; // Number | 
let opts = {
  'expand': "expand_example" // String | 
};
apiInstance.updatePermissionScheme(schemeId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schemeId** | **Number**|  | 
 **expand** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateProject

> updateProject(projectIdOrKey, opts)



Updates a project.  &lt;p&gt;  Only non null values sent in JSON will be updated in the project.&lt;/p&gt;  &lt;p&gt;  Values available for the assigneeType field are: \&quot;PROJECT_LEAD\&quot; and \&quot;UNASSIGNED\&quot;.&lt;/p&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | the project id or project key
let opts = {
  'expand': "expand_example" // String | the parameters to expand in returned project
};
apiInstance.updateProject(projectIdOrKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| the project id or project key | 
 **expand** | **String**| the parameters to expand in returned project | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateProjectCategory

> updateProjectCategory(id)



Modify a project category via PUT. Any fields present in the PUT will override existing values. As a convenience, if a field  is not present, it is silently ignored.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | 
apiInstance.updateProjectCategory(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateProjectType

> updateProjectType(projectIdOrKey, newProjectTypeKey)



Updates the type of a project.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let projectIdOrKey = "projectIdOrKey_example"; // String | identity of the project to update
let newProjectTypeKey = "newProjectTypeKey_example"; // String | The key of the new project type
apiInstance.updateProjectType(projectIdOrKey, newProjectTypeKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectIdOrKey** | **String**| identity of the project to update | 
 **newProjectTypeKey** | **String**| The key of the new project type | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateProperty

> updateProperty(id, opts)



Update/add new property to a transition. Trying to update a property that does  not exist will result in a new property being added.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the ID of the transition within the workflow.
let opts = {
  'key': "key_example", // String | the name of the property to add.
  'workflowName': "workflowName_example", // String | the name of the workflow to use.
  'workflowMode': "workflowMode_example" // String | the type of workflow to use. Can either be \"live\" or \"draft\".
};
apiInstance.updateProperty(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the ID of the transition within the workflow. | 
 **key** | **String**| the name of the property to add. | [optional] 
 **workflowName** | **String**| the name of the workflow to use. | [optional] 
 **workflowMode** | **String**| the type of workflow to use. Can either be \&quot;live\&quot; or \&quot;draft\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateRemoteIssueLink

> updateRemoteIssueLink(linkId, issueIdOrKey)



Updates a remote issue link from a JSON representation. Any fields not provided are set to null.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let linkId = "linkId_example"; // String | the id of the remote issue link
let issueIdOrKey = "issueIdOrKey_example"; // String | the issue to create the remote issue link for
apiInstance.updateRemoteIssueLink(linkId, issueIdOrKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkId** | **String**| the id of the remote issue link | 
 **issueIdOrKey** | **String**| the issue to create the remote issue link for | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateVersion

> updateVersion(id)



Modify a version via PUT. Any fields present in the PUT will override existing values. As a convenience, if a field  is not present, it is silently ignored.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = "id_example"; // String | The version to delete
apiInstance.updateVersion(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The version to delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateWorkflowMapping

> updateWorkflowMapping(id, opts)



Update the scheme to include the passed mapping.  &lt;p/&gt;  The body is a representation of the workflow mapping.  Values not passed are assumed to indicate no change for that field.  &lt;p/&gt;  The passed representation can have its updateDraftIfNeeded flag set to true to indicate that the draft  should be created/updated when the actual scheme cannot be edited.

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let id = 789; // Number | the id of the scheme.
let opts = {
  'workflowName': "workflowName_example" // String | the name of the workflow mapping to update.
};
apiInstance.updateWorkflowMapping(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| the id of the scheme. | 
 **workflowName** | **String**| the name of the workflow mapping to update. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateWorklog

> updateWorklog(issueIdOrKey, id, opts)



Updates an existing worklog entry.  &lt;p&gt;Note that:&lt;/p&gt;   &lt;ul&gt;       &lt;li&gt;Fields possible for editing are: comment, visibility, started, timeSpent and timeSpentSeconds.&lt;/li&gt;       &lt;li&gt;Either timeSpent or timeSpentSeconds can be set.&lt;/li&gt;       &lt;li&gt;Fields which are not set will not be updated.&lt;/li&gt;       &lt;li&gt;For a request to be valid, it has to have at least one field change.&lt;/li&gt;   &lt;/ul&gt;

### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | a string containing the issue id or key the worklog belongs to
let id = "id_example"; // String | id of the worklog to be deleted
let opts = {
  'adjustEstimate': "adjustEstimate_example", // String | (optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are                        <ul>                        <li>\"new\" - sets the estimate to a specific value</li>                        <li>\"leave\"- leaves the estimate as is</li>                        <li>\"auto\"- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog</li> </ul>
  'newEstimate': "newEstimate_example" // String | (required when \"new\" is selected for adjustEstimate) the new value for the remaining estimate field.
};
apiInstance.updateWorklog(issueIdOrKey, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issueIdOrKey** | **String**| a string containing the issue id or key the worklog belongs to | 
 **id** | **String**| id of the worklog to be deleted | 
 **adjustEstimate** | **String**| (optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are                        &lt;ul&gt;                        &lt;li&gt;\&quot;new\&quot; - sets the estimate to a specific value&lt;/li&gt;                        &lt;li&gt;\&quot;leave\&quot;- leaves the estimate as is&lt;/li&gt;                        &lt;li&gt;\&quot;auto\&quot;- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog&lt;/li&gt; &lt;/ul&gt; | [optional] 
 **newEstimate** | **String**| (required when \&quot;new\&quot; is selected for adjustEstimate) the new value for the remaining estimate field. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## validate

> validate()



### Example

```javascript
import Jira761 from 'jira_7_6_1';

let apiInstance = new Jira761.DefaultApi();
apiInstance.validate((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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

