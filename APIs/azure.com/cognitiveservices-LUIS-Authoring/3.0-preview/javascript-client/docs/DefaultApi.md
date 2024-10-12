# LuisAuthoringClient.DefaultApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsAdd**](DefaultApi.md#appsAdd) | **POST** /apps/ | 
[**appsAddCustomPrebuiltDomain**](DefaultApi.md#appsAddCustomPrebuiltDomain) | **POST** /apps/customprebuiltdomains | 
[**appsDelete**](DefaultApi.md#appsDelete) | **DELETE** /apps/{appId} | 
[**appsDownloadQueryLogs**](DefaultApi.md#appsDownloadQueryLogs) | **GET** /apps/{appId}/querylogs | 
[**appsGet**](DefaultApi.md#appsGet) | **GET** /apps/{appId} | 
[**appsGetPublishSettings**](DefaultApi.md#appsGetPublishSettings) | **GET** /apps/{appId}/publishsettings | 
[**appsGetSettings**](DefaultApi.md#appsGetSettings) | **GET** /apps/{appId}/settings | 
[**appsImport**](DefaultApi.md#appsImport) | **POST** /apps/import | 
[**appsList**](DefaultApi.md#appsList) | **GET** /apps/ | 
[**appsListAvailableCustomPrebuiltDomains**](DefaultApi.md#appsListAvailableCustomPrebuiltDomains) | **GET** /apps/customprebuiltdomains | 
[**appsListAvailableCustomPrebuiltDomainsForCulture**](DefaultApi.md#appsListAvailableCustomPrebuiltDomainsForCulture) | **GET** /apps/customprebuiltdomains/{culture} | 
[**appsListCortanaEndpoints**](DefaultApi.md#appsListCortanaEndpoints) | **GET** /apps/assistants | 
[**appsListDomains**](DefaultApi.md#appsListDomains) | **GET** /apps/domains | 
[**appsListEndpoints**](DefaultApi.md#appsListEndpoints) | **GET** /apps/{appId}/endpoints | 
[**appsListSupportedCultures**](DefaultApi.md#appsListSupportedCultures) | **GET** /apps/cultures | 
[**appsListUsageScenarios**](DefaultApi.md#appsListUsageScenarios) | **GET** /apps/usagescenarios | 
[**appsPackagePublishedApplicationAsGzip**](DefaultApi.md#appsPackagePublishedApplicationAsGzip) | **GET** /package/{appId}/slot/{slotName}/gzip | package - Gets published LUIS application package in binary stream GZip format
[**appsPackageTrainedApplicationAsGzip**](DefaultApi.md#appsPackageTrainedApplicationAsGzip) | **GET** /package/{appId}/versions/{versionId}/gzip | package - Gets trained LUIS application package in binary stream GZip format
[**appsPublish**](DefaultApi.md#appsPublish) | **POST** /apps/{appId}/publish | 
[**appsUpdate**](DefaultApi.md#appsUpdate) | **PUT** /apps/{appId} | 
[**appsUpdatePublishSettings**](DefaultApi.md#appsUpdatePublishSettings) | **PUT** /apps/{appId}/publishsettings | 
[**appsUpdateSettings**](DefaultApi.md#appsUpdateSettings) | **PUT** /apps/{appId}/settings | 
[**azureAccountsAssignToApp**](DefaultApi.md#azureAccountsAssignToApp) | **POST** /apps/{appId}/azureaccounts | apps - Assign a LUIS Azure account to an application
[**azureAccountsGetAssigned**](DefaultApi.md#azureAccountsGetAssigned) | **GET** /apps/{appId}/azureaccounts | apps - Get LUIS Azure accounts assigned to the application
[**azureAccountsListUserLUISAccounts**](DefaultApi.md#azureAccountsListUserLUISAccounts) | **GET** /azureaccounts | user - Get LUIS Azure accounts
[**azureAccountsRemoveFromApp**](DefaultApi.md#azureAccountsRemoveFromApp) | **DELETE** /apps/{appId}/azureaccounts | apps - Removes an assigned LUIS Azure account from an application
[**examplesAdd**](DefaultApi.md#examplesAdd) | **POST** /apps/{appId}/versions/{versionId}/example | 
[**examplesBatch**](DefaultApi.md#examplesBatch) | **POST** /apps/{appId}/versions/{versionId}/examples | 
[**examplesDelete**](DefaultApi.md#examplesDelete) | **DELETE** /apps/{appId}/versions/{versionId}/examples/{exampleId} | 
[**examplesList**](DefaultApi.md#examplesList) | **GET** /apps/{appId}/versions/{versionId}/examples | 
[**featuresAddEntityFeature**](DefaultApi.md#featuresAddEntityFeature) | **POST** /apps/{appId}/versions/{versionId}/entities/{entityId}/features | 
[**featuresAddIntentFeature**](DefaultApi.md#featuresAddIntentFeature) | **POST** /apps/{appId}/versions/{versionId}/intents/{intentId}/features | 
[**featuresAddPhraseList**](DefaultApi.md#featuresAddPhraseList) | **POST** /apps/{appId}/versions/{versionId}/phraselists | 
[**featuresDeletePhraseList**](DefaultApi.md#featuresDeletePhraseList) | **DELETE** /apps/{appId}/versions/{versionId}/phraselists/{phraselistId} | 
[**featuresGetPhraseList**](DefaultApi.md#featuresGetPhraseList) | **GET** /apps/{appId}/versions/{versionId}/phraselists/{phraselistId} | 
[**featuresList**](DefaultApi.md#featuresList) | **GET** /apps/{appId}/versions/{versionId}/features | 
[**featuresListPhraseLists**](DefaultApi.md#featuresListPhraseLists) | **GET** /apps/{appId}/versions/{versionId}/phraselists | 
[**featuresUpdatePhraseList**](DefaultApi.md#featuresUpdatePhraseList) | **PUT** /apps/{appId}/versions/{versionId}/phraselists/{phraselistId} | 
[**modelAddClosedList**](DefaultApi.md#modelAddClosedList) | **POST** /apps/{appId}/versions/{versionId}/closedlists | 
[**modelAddCompositeEntityChild**](DefaultApi.md#modelAddCompositeEntityChild) | **POST** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId}/children | 
[**modelAddCustomPrebuiltDomain**](DefaultApi.md#modelAddCustomPrebuiltDomain) | **POST** /apps/{appId}/versions/{versionId}/customprebuiltdomains | 
[**modelAddCustomPrebuiltEntity**](DefaultApi.md#modelAddCustomPrebuiltEntity) | **POST** /apps/{appId}/versions/{versionId}/customprebuiltentities | 
[**modelAddCustomPrebuiltIntent**](DefaultApi.md#modelAddCustomPrebuiltIntent) | **POST** /apps/{appId}/versions/{versionId}/customprebuiltintents | 
[**modelAddEntity**](DefaultApi.md#modelAddEntity) | **POST** /apps/{appId}/versions/{versionId}/entities | 
[**modelAddEntityChild**](DefaultApi.md#modelAddEntityChild) | **POST** /apps/{appId}/versions/{versionId}/entities/{entityId}/children | 
[**modelAddExplicitListItem**](DefaultApi.md#modelAddExplicitListItem) | **POST** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/explicitlist | Add a new exception to the explicit list for the Pattern.Any entity in a version of the application.
[**modelAddIntent**](DefaultApi.md#modelAddIntent) | **POST** /apps/{appId}/versions/{versionId}/intents | 
[**modelAddPrebuilt**](DefaultApi.md#modelAddPrebuilt) | **POST** /apps/{appId}/versions/{versionId}/prebuilts | 
[**modelAddSubList**](DefaultApi.md#modelAddSubList) | **POST** /apps/{appId}/versions/{versionId}/closedlists/{clEntityId}/sublists | 
[**modelCreateClosedListEntityRole**](DefaultApi.md#modelCreateClosedListEntityRole) | **POST** /apps/{appId}/versions/{versionId}/closedlists/{entityId}/roles | Create a role for a list entity in a version of the application.
[**modelCreateCompositeEntityRole**](DefaultApi.md#modelCreateCompositeEntityRole) | **POST** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId}/roles | Create a role for a composite entity in a version of the application.
[**modelCreateCustomPrebuiltEntityRole**](DefaultApi.md#modelCreateCustomPrebuiltEntityRole) | **POST** /apps/{appId}/versions/{versionId}/customprebuiltentities/{entityId}/roles | Create a role for a prebuilt entity in a version of the application.
[**modelCreateEntityRole**](DefaultApi.md#modelCreateEntityRole) | **POST** /apps/{appId}/versions/{versionId}/entities/{entityId}/roles | Create an entity role in a version of the application.
[**modelCreateHierarchicalEntityRole**](DefaultApi.md#modelCreateHierarchicalEntityRole) | **POST** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId}/roles | Create a role for an hierarchical entity in a version of the application.
[**modelCreatePatternAnyEntityModel**](DefaultApi.md#modelCreatePatternAnyEntityModel) | **POST** /apps/{appId}/versions/{versionId}/patternanyentities | Adds a pattern.any entity extractor to a version of the application.
[**modelCreatePatternAnyEntityRole**](DefaultApi.md#modelCreatePatternAnyEntityRole) | **POST** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/roles | Create a role for an Pattern.any entity in a version of the application.
[**modelCreatePrebuiltEntityRole**](DefaultApi.md#modelCreatePrebuiltEntityRole) | **POST** /apps/{appId}/versions/{versionId}/prebuilts/{entityId}/roles | Create a role for a prebuilt entity in a version of the application.
[**modelCreateRegexEntityModel**](DefaultApi.md#modelCreateRegexEntityModel) | **POST** /apps/{appId}/versions/{versionId}/regexentities | Adds a regular expression entity model to a version of the application.
[**modelCreateRegexEntityRole**](DefaultApi.md#modelCreateRegexEntityRole) | **POST** /apps/{appId}/versions/{versionId}/regexentities/{entityId}/roles | Create a role for an regular expression entity in a version of the application.
[**modelDeleteClosedList**](DefaultApi.md#modelDeleteClosedList) | **DELETE** /apps/{appId}/versions/{versionId}/closedlists/{clEntityId} | 
[**modelDeleteClosedListEntityRole**](DefaultApi.md#modelDeleteClosedListEntityRole) | **DELETE** /apps/{appId}/versions/{versionId}/closedlists/{entityId}/roles/{roleId} | Delete a role for a given list entity in a version of the application.
[**modelDeleteCompositeEntity**](DefaultApi.md#modelDeleteCompositeEntity) | **DELETE** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId} | 
[**modelDeleteCompositeEntityChild**](DefaultApi.md#modelDeleteCompositeEntityChild) | **DELETE** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId}/children/{cChildId} | 
[**modelDeleteCompositeEntityRole**](DefaultApi.md#modelDeleteCompositeEntityRole) | **DELETE** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId}/roles/{roleId} | Delete a role for a given composite entity in a version of the application.
[**modelDeleteCustomEntityRole**](DefaultApi.md#modelDeleteCustomEntityRole) | **DELETE** /apps/{appId}/versions/{versionId}/customprebuiltentities/{entityId}/roles/{roleId} | Delete a role for a given prebuilt entity in a version of the application.
[**modelDeleteCustomPrebuiltDomain**](DefaultApi.md#modelDeleteCustomPrebuiltDomain) | **DELETE** /apps/{appId}/versions/{versionId}/customprebuiltdomains/{domainName} | 
[**modelDeleteEntity**](DefaultApi.md#modelDeleteEntity) | **DELETE** /apps/{appId}/versions/{versionId}/entities/{entityId} | 
[**modelDeleteEntityFeature**](DefaultApi.md#modelDeleteEntityFeature) | **DELETE** /apps/{appId}/versions/{versionId}/entities/{entityId}/features | 
[**modelDeleteEntityRole**](DefaultApi.md#modelDeleteEntityRole) | **DELETE** /apps/{appId}/versions/{versionId}/entities/{entityId}/roles/{roleId} | Delete an entity role in a version of the application.
[**modelDeleteExplicitListItem**](DefaultApi.md#modelDeleteExplicitListItem) | **DELETE** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/explicitlist/{itemId} | Delete an item from the explicit (exception) list for a Pattern.any entity in a version of the application.
[**modelDeleteHierarchicalEntity**](DefaultApi.md#modelDeleteHierarchicalEntity) | **DELETE** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId} | 
[**modelDeleteHierarchicalEntityChild**](DefaultApi.md#modelDeleteHierarchicalEntityChild) | **DELETE** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId}/children/{hChildId} | 
[**modelDeleteHierarchicalEntityRole**](DefaultApi.md#modelDeleteHierarchicalEntityRole) | **DELETE** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId}/roles/{roleId} | Delete a role for a given hierarchical role in a version of the application.
[**modelDeleteIntent**](DefaultApi.md#modelDeleteIntent) | **DELETE** /apps/{appId}/versions/{versionId}/intents/{intentId} | 
[**modelDeleteIntentFeature**](DefaultApi.md#modelDeleteIntentFeature) | **DELETE** /apps/{appId}/versions/{versionId}/intents/{intentId}/features | 
[**modelDeletePatternAnyEntityModel**](DefaultApi.md#modelDeletePatternAnyEntityModel) | **DELETE** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId} | Deletes a Pattern.Any entity extractor from a version of the application.
[**modelDeletePatternAnyEntityRole**](DefaultApi.md#modelDeletePatternAnyEntityRole) | **DELETE** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/roles/{roleId} | Delete a role for a given Pattern.any entity in a version of the application.
[**modelDeletePrebuilt**](DefaultApi.md#modelDeletePrebuilt) | **DELETE** /apps/{appId}/versions/{versionId}/prebuilts/{prebuiltId} | 
[**modelDeletePrebuiltEntityRole**](DefaultApi.md#modelDeletePrebuiltEntityRole) | **DELETE** /apps/{appId}/versions/{versionId}/prebuilts/{entityId}/roles/{roleId} | Delete a role in a prebuilt entity in a version of the application.
[**modelDeleteRegexEntityModel**](DefaultApi.md#modelDeleteRegexEntityModel) | **DELETE** /apps/{appId}/versions/{versionId}/regexentities/{regexEntityId} | Deletes a regular expression entity from a version of the application.
[**modelDeleteRegexEntityRole**](DefaultApi.md#modelDeleteRegexEntityRole) | **DELETE** /apps/{appId}/versions/{versionId}/regexentities/{entityId}/roles/{roleId} | Delete a role for a given regular expression in a version of the application.
[**modelDeleteSubList**](DefaultApi.md#modelDeleteSubList) | **DELETE** /apps/{appId}/versions/{versionId}/closedlists/{clEntityId}/sublists/{subListId} | 
[**modelExamples**](DefaultApi.md#modelExamples) | **GET** /apps/{appId}/versions/{versionId}/models/{modelId}/examples | 
[**modelGetClosedList**](DefaultApi.md#modelGetClosedList) | **GET** /apps/{appId}/versions/{versionId}/closedlists/{clEntityId} | 
[**modelGetClosedListEntityRole**](DefaultApi.md#modelGetClosedListEntityRole) | **GET** /apps/{appId}/versions/{versionId}/closedlists/{entityId}/roles/{roleId} | Get one role for a given list entity in a version of the application.
[**modelGetCompositeEntity**](DefaultApi.md#modelGetCompositeEntity) | **GET** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId} | 
[**modelGetCompositeEntityRole**](DefaultApi.md#modelGetCompositeEntityRole) | **GET** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId}/roles/{roleId} | Get one role for a given composite entity in a version of the application
[**modelGetCustomEntityRole**](DefaultApi.md#modelGetCustomEntityRole) | **GET** /apps/{appId}/versions/{versionId}/customprebuiltentities/{entityId}/roles/{roleId} | Get one role for a given prebuilt entity in a version of the application.
[**modelGetEntity**](DefaultApi.md#modelGetEntity) | **GET** /apps/{appId}/versions/{versionId}/entities/{entityId} | 
[**modelGetEntityFeatures**](DefaultApi.md#modelGetEntityFeatures) | **GET** /apps/{appId}/versions/{versionId}/entities/{entityId}/features | 
[**modelGetEntityRole**](DefaultApi.md#modelGetEntityRole) | **GET** /apps/{appId}/versions/{versionId}/entities/{entityId}/roles/{roleId} | Get one role for a given entity in a version of the application
[**modelGetExplicitList**](DefaultApi.md#modelGetExplicitList) | **GET** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/explicitlist | Get the explicit (exception) list of the pattern.any entity in a version of the application.
[**modelGetExplicitListItem**](DefaultApi.md#modelGetExplicitListItem) | **GET** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/explicitlist/{itemId} | Get the explicit (exception) list of the pattern.any entity in a version of the application.
[**modelGetHierarchicalEntity**](DefaultApi.md#modelGetHierarchicalEntity) | **GET** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId} | 
[**modelGetHierarchicalEntityChild**](DefaultApi.md#modelGetHierarchicalEntityChild) | **GET** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId}/children/{hChildId} | 
[**modelGetHierarchicalEntityRole**](DefaultApi.md#modelGetHierarchicalEntityRole) | **GET** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId}/roles/{roleId} | Get one role for a given hierarchical entity in a version of the application.
[**modelGetIntent**](DefaultApi.md#modelGetIntent) | **GET** /apps/{appId}/versions/{versionId}/intents/{intentId} | 
[**modelGetIntentFeatures**](DefaultApi.md#modelGetIntentFeatures) | **GET** /apps/{appId}/versions/{versionId}/intents/{intentId}/features | 
[**modelGetPatternAnyEntityInfo**](DefaultApi.md#modelGetPatternAnyEntityInfo) | **GET** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId} | Gets information about the Pattern.Any model in a version of the application.
[**modelGetPatternAnyEntityRole**](DefaultApi.md#modelGetPatternAnyEntityRole) | **GET** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/roles/{roleId} | Get one role for a given Pattern.any entity in a version of the application.
[**modelGetPrebuilt**](DefaultApi.md#modelGetPrebuilt) | **GET** /apps/{appId}/versions/{versionId}/prebuilts/{prebuiltId} | 
[**modelGetPrebuiltEntityRole**](DefaultApi.md#modelGetPrebuiltEntityRole) | **GET** /apps/{appId}/versions/{versionId}/prebuilts/{entityId}/roles/{roleId} | Get one role for a given prebuilt entity in a version of the application
[**modelGetRegexEntityEntityInfo**](DefaultApi.md#modelGetRegexEntityEntityInfo) | **GET** /apps/{appId}/versions/{versionId}/regexentities/{regexEntityId} | Gets information about a regular expression entity in a version of the application.
[**modelGetRegexEntityRole**](DefaultApi.md#modelGetRegexEntityRole) | **GET** /apps/{appId}/versions/{versionId}/regexentities/{entityId}/roles/{roleId} | Get one role for a given regular expression entity in a version of the application.
[**modelListClosedListEntityRoles**](DefaultApi.md#modelListClosedListEntityRoles) | **GET** /apps/{appId}/versions/{versionId}/closedlists/{entityId}/roles | Get all roles for a list entity in a version of the application.
[**modelListClosedLists**](DefaultApi.md#modelListClosedLists) | **GET** /apps/{appId}/versions/{versionId}/closedlists | 
[**modelListCompositeEntities**](DefaultApi.md#modelListCompositeEntities) | **GET** /apps/{appId}/versions/{versionId}/compositeentities | 
[**modelListCompositeEntityRoles**](DefaultApi.md#modelListCompositeEntityRoles) | **GET** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId}/roles | Get all roles for a composite entity in a version of the application
[**modelListCustomPrebuiltEntities**](DefaultApi.md#modelListCustomPrebuiltEntities) | **GET** /apps/{appId}/versions/{versionId}/customprebuiltentities | 
[**modelListCustomPrebuiltEntityRoles**](DefaultApi.md#modelListCustomPrebuiltEntityRoles) | **GET** /apps/{appId}/versions/{versionId}/customprebuiltentities/{entityId}/roles | Get all roles for a prebuilt entity in a version of the application
[**modelListCustomPrebuiltIntents**](DefaultApi.md#modelListCustomPrebuiltIntents) | **GET** /apps/{appId}/versions/{versionId}/customprebuiltintents | 
[**modelListCustomPrebuiltModels**](DefaultApi.md#modelListCustomPrebuiltModels) | **GET** /apps/{appId}/versions/{versionId}/customprebuiltmodels | 
[**modelListEntities**](DefaultApi.md#modelListEntities) | **GET** /apps/{appId}/versions/{versionId}/entities | 
[**modelListEntityRoles**](DefaultApi.md#modelListEntityRoles) | **GET** /apps/{appId}/versions/{versionId}/entities/{entityId}/roles | Get all roles for an entity in a version of the application
[**modelListEntitySuggestions**](DefaultApi.md#modelListEntitySuggestions) | **GET** /apps/{appId}/versions/{versionId}/entities/{entityId}/suggest | 
[**modelListHierarchicalEntities**](DefaultApi.md#modelListHierarchicalEntities) | **GET** /apps/{appId}/versions/{versionId}/hierarchicalentities | 
[**modelListHierarchicalEntityRoles**](DefaultApi.md#modelListHierarchicalEntityRoles) | **GET** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId}/roles | Get all roles for a hierarchical entity in a version of the application
[**modelListIntentSuggestions**](DefaultApi.md#modelListIntentSuggestions) | **GET** /apps/{appId}/versions/{versionId}/intents/{intentId}/suggest | 
[**modelListIntents**](DefaultApi.md#modelListIntents) | **GET** /apps/{appId}/versions/{versionId}/intents | 
[**modelListModels**](DefaultApi.md#modelListModels) | **GET** /apps/{appId}/versions/{versionId}/models | 
[**modelListPatternAnyEntityInfos**](DefaultApi.md#modelListPatternAnyEntityInfos) | **GET** /apps/{appId}/versions/{versionId}/patternanyentities | Get information about the Pattern.Any entity models in a version of the application.
[**modelListPatternAnyEntityRoles**](DefaultApi.md#modelListPatternAnyEntityRoles) | **GET** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/roles | Get all roles for a Pattern.any entity in a version of the application
[**modelListPrebuiltEntities**](DefaultApi.md#modelListPrebuiltEntities) | **GET** /apps/{appId}/versions/{versionId}/listprebuilts | 
[**modelListPrebuiltEntityRoles**](DefaultApi.md#modelListPrebuiltEntityRoles) | **GET** /apps/{appId}/versions/{versionId}/prebuilts/{entityId}/roles | Get a prebuilt entity&#39;s roles in a version of the application.
[**modelListPrebuilts**](DefaultApi.md#modelListPrebuilts) | **GET** /apps/{appId}/versions/{versionId}/prebuilts | 
[**modelListRegexEntityInfos**](DefaultApi.md#modelListRegexEntityInfos) | **GET** /apps/{appId}/versions/{versionId}/regexentities | Gets information about the regular expression entity models in a version of the application.
[**modelListRegexEntityRoles**](DefaultApi.md#modelListRegexEntityRoles) | **GET** /apps/{appId}/versions/{versionId}/regexentities/{entityId}/roles | Get all roles for a regular expression entity in a version of the application.
[**modelPatchClosedList**](DefaultApi.md#modelPatchClosedList) | **PATCH** /apps/{appId}/versions/{versionId}/closedlists/{clEntityId} | 
[**modelReplaceEntityFeatures**](DefaultApi.md#modelReplaceEntityFeatures) | **PUT** /apps/{appId}/versions/{versionId}/entities/{entityId}/features | 
[**modelReplaceIntentFeatures**](DefaultApi.md#modelReplaceIntentFeatures) | **PUT** /apps/{appId}/versions/{versionId}/intents/{intentId}/features | 
[**modelUpdateClosedList**](DefaultApi.md#modelUpdateClosedList) | **PUT** /apps/{appId}/versions/{versionId}/closedlists/{clEntityId} | 
[**modelUpdateClosedListEntityRole**](DefaultApi.md#modelUpdateClosedListEntityRole) | **PUT** /apps/{appId}/versions/{versionId}/closedlists/{entityId}/roles/{roleId} | Update a role for a given list entity in a version of the application.
[**modelUpdateCompositeEntity**](DefaultApi.md#modelUpdateCompositeEntity) | **PUT** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId} | 
[**modelUpdateCompositeEntityRole**](DefaultApi.md#modelUpdateCompositeEntityRole) | **PUT** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId}/roles/{roleId} | Update a role for a given composite entity in a version of the application
[**modelUpdateCustomPrebuiltEntityRole**](DefaultApi.md#modelUpdateCustomPrebuiltEntityRole) | **PUT** /apps/{appId}/versions/{versionId}/customprebuiltentities/{entityId}/roles/{roleId} | Update a role for a given prebuilt entity in a version of the application.
[**modelUpdateEntityChild**](DefaultApi.md#modelUpdateEntityChild) | **PATCH** /apps/{appId}/versions/{versionId}/entities/{entityId} | 
[**modelUpdateEntityRole**](DefaultApi.md#modelUpdateEntityRole) | **PUT** /apps/{appId}/versions/{versionId}/entities/{entityId}/roles/{roleId} | Update a role for a given entity in a version of the application.
[**modelUpdateExplicitListItem**](DefaultApi.md#modelUpdateExplicitListItem) | **PUT** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/explicitlist/{itemId} | Updates an explicit (exception) list item for a Pattern.Any entity in a version of the application.
[**modelUpdateHierarchicalEntity**](DefaultApi.md#modelUpdateHierarchicalEntity) | **PATCH** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId} | 
[**modelUpdateHierarchicalEntityChild**](DefaultApi.md#modelUpdateHierarchicalEntityChild) | **PATCH** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId}/children/{hChildId} | 
[**modelUpdateHierarchicalEntityRole**](DefaultApi.md#modelUpdateHierarchicalEntityRole) | **PUT** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId}/roles/{roleId} | Update a role for a given hierarchical entity in a version of the application.
[**modelUpdateIntent**](DefaultApi.md#modelUpdateIntent) | **PUT** /apps/{appId}/versions/{versionId}/intents/{intentId} | 
[**modelUpdatePatternAnyEntityModel**](DefaultApi.md#modelUpdatePatternAnyEntityModel) | **PUT** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId} | Updates the name and explicit (exception) list of a Pattern.Any entity model in a version of the application.
[**modelUpdatePatternAnyEntityRole**](DefaultApi.md#modelUpdatePatternAnyEntityRole) | **PUT** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/roles/{roleId} | Update a role for a given Pattern.any entity in a version of the application.
[**modelUpdatePrebuiltEntityRole**](DefaultApi.md#modelUpdatePrebuiltEntityRole) | **PUT** /apps/{appId}/versions/{versionId}/prebuilts/{entityId}/roles/{roleId} | Update a role for a given prebuilt entity in a version of the application
[**modelUpdateRegexEntityModel**](DefaultApi.md#modelUpdateRegexEntityModel) | **PUT** /apps/{appId}/versions/{versionId}/regexentities/{regexEntityId} | Updates the regular expression entity in a version of the application.
[**modelUpdateRegexEntityRole**](DefaultApi.md#modelUpdateRegexEntityRole) | **PUT** /apps/{appId}/versions/{versionId}/regexentities/{entityId}/roles/{roleId} | Update a role for a given regular expression entity in a version of the application
[**modelUpdateSubList**](DefaultApi.md#modelUpdateSubList) | **PUT** /apps/{appId}/versions/{versionId}/closedlists/{clEntityId}/sublists/{subListId} | 
[**patternAddPattern**](DefaultApi.md#patternAddPattern) | **POST** /apps/{appId}/versions/{versionId}/patternrule | Adds a pattern to a version of the application.
[**patternBatchAddPatterns**](DefaultApi.md#patternBatchAddPatterns) | **POST** /apps/{appId}/versions/{versionId}/patternrules | Adds a batch of patterns in a version of the application.
[**patternDeletePattern**](DefaultApi.md#patternDeletePattern) | **DELETE** /apps/{appId}/versions/{versionId}/patternrules/{patternId} | Deletes the pattern with the specified ID from a version of the application..
[**patternDeletePatterns**](DefaultApi.md#patternDeletePatterns) | **DELETE** /apps/{appId}/versions/{versionId}/patternrules | Deletes a list of patterns in a version of the application.
[**patternListIntentPatterns**](DefaultApi.md#patternListIntentPatterns) | **GET** /apps/{appId}/versions/{versionId}/intents/{intentId}/patternrules | Returns patterns for the specific intent in a version of the application.
[**patternListPatterns**](DefaultApi.md#patternListPatterns) | **GET** /apps/{appId}/versions/{versionId}/patternrules | Gets patterns in a version of the application.
[**patternUpdatePattern**](DefaultApi.md#patternUpdatePattern) | **PUT** /apps/{appId}/versions/{versionId}/patternrules/{patternId} | Updates a pattern in a version of the application.
[**patternUpdatePatterns**](DefaultApi.md#patternUpdatePatterns) | **PUT** /apps/{appId}/versions/{versionId}/patternrules | Updates patterns in a version of the application.
[**permissionsAdd**](DefaultApi.md#permissionsAdd) | **POST** /apps/{appId}/permissions | 
[**permissionsDelete**](DefaultApi.md#permissionsDelete) | **DELETE** /apps/{appId}/permissions | 
[**permissionsList**](DefaultApi.md#permissionsList) | **GET** /apps/{appId}/permissions | 
[**permissionsUpdate**](DefaultApi.md#permissionsUpdate) | **PUT** /apps/{appId}/permissions | 
[**settingsList**](DefaultApi.md#settingsList) | **GET** /apps/{appId}/versions/{versionId}/settings | 
[**settingsUpdate**](DefaultApi.md#settingsUpdate) | **PUT** /apps/{appId}/versions/{versionId}/settings | 
[**trainGetStatus**](DefaultApi.md#trainGetStatus) | **GET** /apps/{appId}/versions/{versionId}/train | 
[**trainTrainVersion**](DefaultApi.md#trainTrainVersion) | **POST** /apps/{appId}/versions/{versionId}/train | 
[**versionsClone**](DefaultApi.md#versionsClone) | **POST** /apps/{appId}/versions/{versionId}/clone | 
[**versionsDelete**](DefaultApi.md#versionsDelete) | **DELETE** /apps/{appId}/versions/{versionId}/ | 
[**versionsDeleteUnlabelledUtterance**](DefaultApi.md#versionsDeleteUnlabelledUtterance) | **DELETE** /apps/{appId}/versions/{versionId}/suggest | 
[**versionsExport**](DefaultApi.md#versionsExport) | **GET** /apps/{appId}/versions/{versionId}/export | 
[**versionsGet**](DefaultApi.md#versionsGet) | **GET** /apps/{appId}/versions/{versionId}/ | 
[**versionsImport**](DefaultApi.md#versionsImport) | **POST** /apps/{appId}/versions/import | 
[**versionsList**](DefaultApi.md#versionsList) | **GET** /apps/{appId}/versions | 
[**versionsUpdate**](DefaultApi.md#versionsUpdate) | **PUT** /apps/{appId}/versions/{versionId}/ | 



## appsAdd

> String appsAdd(applicationCreateObject)



Creates a new LUIS app.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let applicationCreateObject = new LuisAuthoringClient.ApplicationCreateObject(); // ApplicationCreateObject | An application containing Name, Description (optional), Culture, Usage Scenario (optional), Domain (optional) and initial version ID (optional) of the application. Default value for the version ID is \"0.1\". Note: the culture cannot be changed after the app is created.
apiInstance.appsAdd(applicationCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationCreateObject** | [**ApplicationCreateObject**](ApplicationCreateObject.md)| An application containing Name, Description (optional), Culture, Usage Scenario (optional), Domain (optional) and initial version ID (optional) of the application. Default value for the version ID is \&quot;0.1\&quot;. Note: the culture cannot be changed after the app is created. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsAddCustomPrebuiltDomain

> String appsAddCustomPrebuiltDomain(prebuiltDomainCreateObject)



Adds a prebuilt domain along with its intent and entity models as a new application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let prebuiltDomainCreateObject = new LuisAuthoringClient.PrebuiltDomainCreateObject(); // PrebuiltDomainCreateObject | A prebuilt domain create object containing the name and culture of the domain.
apiInstance.appsAddCustomPrebuiltDomain(prebuiltDomainCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prebuiltDomainCreateObject** | [**PrebuiltDomainCreateObject**](PrebuiltDomainCreateObject.md)| A prebuilt domain create object containing the name and culture of the domain. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsDelete

> OperationStatus appsDelete(appId, opts)



Deletes an application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let opts = {
  'force': false // Boolean | A flag to indicate whether to force an operation.
};
apiInstance.appsDelete(appId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **force** | **Boolean**| A flag to indicate whether to force an operation. | [optional] [default to false]

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsDownloadQueryLogs

> Object appsDownloadQueryLogs(appId)



Gets the logs of the past month&#39;s endpoint queries for the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
apiInstance.appsDownloadQueryLogs(appId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 

### Return type

**Object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## appsGet

> ApplicationInfoResponse appsGet(appId)



Gets the application info.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
apiInstance.appsGet(appId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 

### Return type

[**ApplicationInfoResponse**](ApplicationInfoResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGetPublishSettings

> PublishSettings appsGetPublishSettings(appId)



Get the application publish settings including &#39;UseAllTrainingData&#39;.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
apiInstance.appsGetPublishSettings(appId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 

### Return type

[**PublishSettings**](PublishSettings.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGetSettings

> ApplicationSettings appsGetSettings(appId)



Get the application settings including &#39;UseAllTrainingData&#39;.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
apiInstance.appsGetSettings(appId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 

### Return type

[**ApplicationSettings**](ApplicationSettings.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsImport

> String appsImport(luisApp, opts)



Imports an application to LUIS, the application&#39;s structure is included in the request body.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let luisApp = new LuisAuthoringClient.LuisApp(); // LuisApp | A LUIS application structure.
let opts = {
  'appName': "appName_example" // String | The application name to create. If not specified, the application name will be read from the imported object. If the application name already exists, an error is returned.
};
apiInstance.appsImport(luisApp, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **luisApp** | [**LuisApp**](LuisApp.md)| A LUIS application structure. | 
 **appName** | **String**| The application name to create. If not specified, the application name will be read from the imported object. If the application name already exists, an error is returned. | [optional] 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsList

> [ApplicationInfoResponse] appsList(opts)



Lists all of the user&#39;s applications.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let opts = {
  'skip': 0, // Number | The number of entries to skip. Default value is 0.
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.appsList(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **Number**| The number of entries to skip. Default value is 0. | [optional] [default to 0]
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[ApplicationInfoResponse]**](ApplicationInfoResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListAvailableCustomPrebuiltDomains

> [PrebuiltDomain] appsListAvailableCustomPrebuiltDomains()



Gets all the available custom prebuilt domains for all cultures.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
apiInstance.appsListAvailableCustomPrebuiltDomains((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[PrebuiltDomain]**](PrebuiltDomain.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListAvailableCustomPrebuiltDomainsForCulture

> [PrebuiltDomain] appsListAvailableCustomPrebuiltDomainsForCulture(culture)



Gets all the available prebuilt domains for a specific culture.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let culture = "culture_example"; // String | Culture.
apiInstance.appsListAvailableCustomPrebuiltDomainsForCulture(culture, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **culture** | **String**| Culture. | 

### Return type

[**[PrebuiltDomain]**](PrebuiltDomain.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListCortanaEndpoints

> PersonalAssistantsResponse appsListCortanaEndpoints()



Gets the endpoint URLs for the prebuilt Cortana applications.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
apiInstance.appsListCortanaEndpoints((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**PersonalAssistantsResponse**](PersonalAssistantsResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListDomains

> [String] appsListDomains()



Gets the available application domains.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
apiInstance.appsListDomains((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListEndpoints

> {String: String} appsListEndpoints(appId)



Returns the available endpoint deployment regions and URLs.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
apiInstance.appsListEndpoints(appId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 

### Return type

**{String: String}**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListSupportedCultures

> [AvailableCulture] appsListSupportedCultures()



Gets a list of supported cultures. Cultures are equivalent to the written language and locale. For example,\&quot;en-us\&quot; represents the U.S. variation of English.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
apiInstance.appsListSupportedCultures((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[AvailableCulture]**](AvailableCulture.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListUsageScenarios

> [String] appsListUsageScenarios()



Gets the application available usage scenarios.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
apiInstance.appsListUsageScenarios((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsPackagePublishedApplicationAsGzip

> File appsPackagePublishedApplicationAsGzip(appId, slotName)

package - Gets published LUIS application package in binary stream GZip format

Packages a published LUIS application as a GZip file to be used in the LUIS container.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let slotName = "slotName_example"; // String | The publishing slot name.
apiInstance.appsPackagePublishedApplicationAsGzip(appId, slotName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **slotName** | **String**| The publishing slot name. | 

### Return type

**File**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json


## appsPackageTrainedApplicationAsGzip

> File appsPackageTrainedApplicationAsGzip(appId, versionId)

package - Gets trained LUIS application package in binary stream GZip format

Packages trained LUIS application as GZip file to be used in the LUIS container.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
apiInstance.appsPackageTrainedApplicationAsGzip(appId, versionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 

### Return type

**File**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json


## appsPublish

> ProductionOrStagingEndpointInfo appsPublish(appId, applicationPublishObject)



Publishes a specific version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let applicationPublishObject = new LuisAuthoringClient.ApplicationPublishObject(); // ApplicationPublishObject | The application publish object. The region is the target region that the application is published to.
apiInstance.appsPublish(appId, applicationPublishObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **applicationPublishObject** | [**ApplicationPublishObject**](ApplicationPublishObject.md)| The application publish object. The region is the target region that the application is published to. | 

### Return type

[**ProductionOrStagingEndpointInfo**](ProductionOrStagingEndpointInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsUpdate

> OperationStatus appsUpdate(appId, applicationUpdateObject)



Updates the name or description of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let applicationUpdateObject = new LuisAuthoringClient.ApplicationUpdateObject(); // ApplicationUpdateObject | A model containing Name and Description of the application.
apiInstance.appsUpdate(appId, applicationUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **applicationUpdateObject** | [**ApplicationUpdateObject**](ApplicationUpdateObject.md)| A model containing Name and Description of the application. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsUpdatePublishSettings

> OperationStatus appsUpdatePublishSettings(appId, publishSettingUpdateObject)



Updates the application publish settings including &#39;UseAllTrainingData&#39;.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let publishSettingUpdateObject = new LuisAuthoringClient.PublishSettingUpdateObject(); // PublishSettingUpdateObject | An object containing the new publish application settings.
apiInstance.appsUpdatePublishSettings(appId, publishSettingUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **publishSettingUpdateObject** | [**PublishSettingUpdateObject**](PublishSettingUpdateObject.md)| An object containing the new publish application settings. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsUpdateSettings

> OperationStatus appsUpdateSettings(appId, applicationSettingUpdateObject)



Updates the application settings including &#39;UseAllTrainingData&#39;.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let applicationSettingUpdateObject = new LuisAuthoringClient.ApplicationSettingUpdateObject(); // ApplicationSettingUpdateObject | An object containing the new application settings.
apiInstance.appsUpdateSettings(appId, applicationSettingUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **applicationSettingUpdateObject** | [**ApplicationSettingUpdateObject**](ApplicationSettingUpdateObject.md)| An object containing the new application settings. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## azureAccountsAssignToApp

> OperationStatus azureAccountsAssignToApp(appId, authorization, opts)

apps - Assign a LUIS Azure account to an application

Assigns an Azure account to the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let authorization = "authorization_example"; // String | The bearer authorization header to use; containing the user's ARM token used to validate Azure accounts information.
let opts = {
  'azureAccountInfoObject': new LuisAuthoringClient.AzureAccountInfoObject() // AzureAccountInfoObject | The Azure account information object.
};
apiInstance.azureAccountsAssignToApp(appId, authorization, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **authorization** | **String**| The bearer authorization header to use; containing the user&#39;s ARM token used to validate Azure accounts information. | 
 **azureAccountInfoObject** | [**AzureAccountInfoObject**](AzureAccountInfoObject.md)| The Azure account information object. | [optional] 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## azureAccountsGetAssigned

> [AzureAccountInfoObject] azureAccountsGetAssigned(appId, authorization)

apps - Get LUIS Azure accounts assigned to the application

Gets the LUIS Azure accounts assigned to the application for the user using his ARM token.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let authorization = "authorization_example"; // String | The bearer authorization header to use; containing the user's ARM token used to validate Azure accounts information.
apiInstance.azureAccountsGetAssigned(appId, authorization, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **authorization** | **String**| The bearer authorization header to use; containing the user&#39;s ARM token used to validate Azure accounts information. | 

### Return type

[**[AzureAccountInfoObject]**](AzureAccountInfoObject.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## azureAccountsListUserLUISAccounts

> [AzureAccountInfoObject] azureAccountsListUserLUISAccounts(authorization)

user - Get LUIS Azure accounts

Gets the LUIS Azure accounts for the user using his ARM token.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let authorization = "authorization_example"; // String | The bearer authorization header to use; containing the user's ARM token used to validate Azure accounts information.
apiInstance.azureAccountsListUserLUISAccounts(authorization, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **String**| The bearer authorization header to use; containing the user&#39;s ARM token used to validate Azure accounts information. | 

### Return type

[**[AzureAccountInfoObject]**](AzureAccountInfoObject.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## azureAccountsRemoveFromApp

> OperationStatus azureAccountsRemoveFromApp(appId, authorization, opts)

apps - Removes an assigned LUIS Azure account from an application

Removes assigned Azure account from the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let authorization = "authorization_example"; // String | The bearer authorization header to use; containing the user's ARM token used to validate Azure accounts information.
let opts = {
  'azureAccountInfoObject': new LuisAuthoringClient.AzureAccountInfoObject() // AzureAccountInfoObject | The Azure account information object.
};
apiInstance.azureAccountsRemoveFromApp(appId, authorization, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **authorization** | **String**| The bearer authorization header to use; containing the user&#39;s ARM token used to validate Azure accounts information. | 
 **azureAccountInfoObject** | [**AzureAccountInfoObject**](AzureAccountInfoObject.md)| The Azure account information object. | [optional] 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## examplesAdd

> LabelExampleResponse examplesAdd(appId, versionId, exampleLabelObject)



Adds a labeled example utterance in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let exampleLabelObject = new LuisAuthoringClient.ExampleLabelObject(); // ExampleLabelObject | A labeled example utterance with the expected intent and entities.
apiInstance.examplesAdd(appId, versionId, exampleLabelObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **exampleLabelObject** | [**ExampleLabelObject**](ExampleLabelObject.md)| A labeled example utterance with the expected intent and entities. | 

### Return type

[**LabelExampleResponse**](LabelExampleResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## examplesBatch

> [BatchLabelExample] examplesBatch(appId, versionId, exampleLabelObjectArray)



Adds a batch of labeled example utterances to a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let exampleLabelObjectArray = [new LuisAuthoringClient.ExampleLabelObject()]; // [ExampleLabelObject] | Array of example utterances.
apiInstance.examplesBatch(appId, versionId, exampleLabelObjectArray, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **exampleLabelObjectArray** | [**[ExampleLabelObject]**](ExampleLabelObject.md)| Array of example utterances. | 

### Return type

[**[BatchLabelExample]**](BatchLabelExample.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## examplesDelete

> OperationStatus examplesDelete(appId, versionId, exampleId)



Deletes the labeled example utterances with the specified ID from a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let exampleId = 56; // Number | The example ID.
apiInstance.examplesDelete(appId, versionId, exampleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **exampleId** | **Number**| The example ID. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## examplesList

> [LabeledUtterance] examplesList(appId, versionId, opts)



Returns example utterances to be reviewed from a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let opts = {
  'skip': 0, // Number | The number of entries to skip. Default value is 0.
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.examplesList(appId, versionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **skip** | **Number**| The number of entries to skip. Default value is 0. | [optional] [default to 0]
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[LabeledUtterance]**](LabeledUtterance.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## featuresAddEntityFeature

> OperationStatus featuresAddEntityFeature(appId, versionId, entityId, featureRelationCreateObject)



Adds a new feature relation to be used by the entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity extractor ID.
let featureRelationCreateObject = new LuisAuthoringClient.ModelFeatureInformation(); // ModelFeatureInformation | A Feature relation information object.
apiInstance.featuresAddEntityFeature(appId, versionId, entityId, featureRelationCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity extractor ID. | 
 **featureRelationCreateObject** | [**ModelFeatureInformation**](ModelFeatureInformation.md)| A Feature relation information object. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## featuresAddIntentFeature

> OperationStatus featuresAddIntentFeature(appId, versionId, intentId, featureRelationCreateObject)



Adds a new feature relation to be used by the intent in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let intentId = "intentId_example"; // String | The intent classifier ID.
let featureRelationCreateObject = new LuisAuthoringClient.ModelFeatureInformation(); // ModelFeatureInformation | A Feature relation information object.
apiInstance.featuresAddIntentFeature(appId, versionId, intentId, featureRelationCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **intentId** | **String**| The intent classifier ID. | 
 **featureRelationCreateObject** | [**ModelFeatureInformation**](ModelFeatureInformation.md)| A Feature relation information object. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## featuresAddPhraseList

> Number featuresAddPhraseList(appId, versionId, phraselistCreateObject)



Creates a new phraselist feature in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let phraselistCreateObject = new LuisAuthoringClient.PhraselistCreateObject(); // PhraselistCreateObject | A Phraselist object containing Name, comma-separated Phrases and the isExchangeable boolean. Default value for isExchangeable is true.
apiInstance.featuresAddPhraseList(appId, versionId, phraselistCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **phraselistCreateObject** | [**PhraselistCreateObject**](PhraselistCreateObject.md)| A Phraselist object containing Name, comma-separated Phrases and the isExchangeable boolean. Default value for isExchangeable is true. | 

### Return type

**Number**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## featuresDeletePhraseList

> OperationStatus featuresDeletePhraseList(appId, versionId, phraselistId)



Deletes a phraselist feature from a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let phraselistId = 56; // Number | The ID of the feature to be deleted.
apiInstance.featuresDeletePhraseList(appId, versionId, phraselistId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **phraselistId** | **Number**| The ID of the feature to be deleted. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## featuresGetPhraseList

> PhraseListFeatureInfo featuresGetPhraseList(appId, versionId, phraselistId)



Gets phraselist feature info in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let phraselistId = 56; // Number | The ID of the feature to be retrieved.
apiInstance.featuresGetPhraseList(appId, versionId, phraselistId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **phraselistId** | **Number**| The ID of the feature to be retrieved. | 

### Return type

[**PhraseListFeatureInfo**](PhraseListFeatureInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## featuresList

> FeaturesResponseObject featuresList(appId, versionId, opts)



Gets all the extraction phraselist and pattern features in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let opts = {
  'skip': 0, // Number | The number of entries to skip. Default value is 0.
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.featuresList(appId, versionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **skip** | **Number**| The number of entries to skip. Default value is 0. | [optional] [default to 0]
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**FeaturesResponseObject**](FeaturesResponseObject.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## featuresListPhraseLists

> [PhraseListFeatureInfo] featuresListPhraseLists(appId, versionId, opts)



Gets all the phraselist features in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let opts = {
  'skip': 0, // Number | The number of entries to skip. Default value is 0.
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.featuresListPhraseLists(appId, versionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **skip** | **Number**| The number of entries to skip. Default value is 0. | [optional] [default to 0]
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[PhraseListFeatureInfo]**](PhraseListFeatureInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## featuresUpdatePhraseList

> OperationStatus featuresUpdatePhraseList(appId, versionId, phraselistId, opts)



Updates the phrases, the state and the name of the phraselist feature in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let phraselistId = 56; // Number | The ID of the feature to be updated.
let opts = {
  'phraselistUpdateObject': new LuisAuthoringClient.PhraselistUpdateObject() // PhraselistUpdateObject | The new values for: - Just a boolean called IsActive, in which case the status of the feature will be changed. - Name, Pattern, Mode, and a boolean called IsActive to update the feature.
};
apiInstance.featuresUpdatePhraseList(appId, versionId, phraselistId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **phraselistId** | **Number**| The ID of the feature to be updated. | 
 **phraselistUpdateObject** | [**PhraselistUpdateObject**](PhraselistUpdateObject.md)| The new values for: - Just a boolean called IsActive, in which case the status of the feature will be changed. - Name, Pattern, Mode, and a boolean called IsActive to update the feature. | [optional] 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelAddClosedList

> String modelAddClosedList(appId, versionId, closedListModelCreateObject)



Adds a list entity model to a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let closedListModelCreateObject = new LuisAuthoringClient.ClosedListModelCreateObject(); // ClosedListModelCreateObject | A model containing the name and words for the new list entity extractor.
apiInstance.modelAddClosedList(appId, versionId, closedListModelCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **closedListModelCreateObject** | [**ClosedListModelCreateObject**](ClosedListModelCreateObject.md)| A model containing the name and words for the new list entity extractor. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelAddCompositeEntityChild

> String modelAddCompositeEntityChild(appId, versionId, cEntityId, compositeChildModelCreateObject)



Creates a single child in an existing composite entity model in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let cEntityId = "cEntityId_example"; // String | The composite entity extractor ID.
let compositeChildModelCreateObject = new LuisAuthoringClient.ModelAddCompositeEntityChildRequest(); // ModelAddCompositeEntityChildRequest | A model object containing the name of the new composite child model.
apiInstance.modelAddCompositeEntityChild(appId, versionId, cEntityId, compositeChildModelCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **cEntityId** | **String**| The composite entity extractor ID. | 
 **compositeChildModelCreateObject** | [**ModelAddCompositeEntityChildRequest**](ModelAddCompositeEntityChildRequest.md)| A model object containing the name of the new composite child model. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelAddCustomPrebuiltDomain

> [String] modelAddCustomPrebuiltDomain(appId, versionId, prebuiltDomainObject)



Adds a customizable prebuilt domain along with all of its intent and entity models in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let prebuiltDomainObject = new LuisAuthoringClient.PrebuiltDomainCreateBaseObject(); // PrebuiltDomainCreateBaseObject | A prebuilt domain create object containing the name of the domain.
apiInstance.modelAddCustomPrebuiltDomain(appId, versionId, prebuiltDomainObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **prebuiltDomainObject** | [**PrebuiltDomainCreateBaseObject**](PrebuiltDomainCreateBaseObject.md)| A prebuilt domain create object containing the name of the domain. | 

### Return type

**[String]**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelAddCustomPrebuiltEntity

> String modelAddCustomPrebuiltEntity(appId, versionId, prebuiltDomainModelCreateObject)



Adds a prebuilt entity model to a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let prebuiltDomainModelCreateObject = new LuisAuthoringClient.PrebuiltDomainModelCreateObject(); // PrebuiltDomainModelCreateObject | A model object containing the name of the prebuilt entity and the name of the domain to which this model belongs.
apiInstance.modelAddCustomPrebuiltEntity(appId, versionId, prebuiltDomainModelCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **prebuiltDomainModelCreateObject** | [**PrebuiltDomainModelCreateObject**](PrebuiltDomainModelCreateObject.md)| A model object containing the name of the prebuilt entity and the name of the domain to which this model belongs. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelAddCustomPrebuiltIntent

> String modelAddCustomPrebuiltIntent(appId, versionId, prebuiltDomainModelCreateObject)



Adds a customizable prebuilt intent model to a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let prebuiltDomainModelCreateObject = new LuisAuthoringClient.PrebuiltDomainModelCreateObject(); // PrebuiltDomainModelCreateObject | A model object containing the name of the customizable prebuilt intent and the name of the domain to which this model belongs.
apiInstance.modelAddCustomPrebuiltIntent(appId, versionId, prebuiltDomainModelCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **prebuiltDomainModelCreateObject** | [**PrebuiltDomainModelCreateObject**](PrebuiltDomainModelCreateObject.md)| A model object containing the name of the customizable prebuilt intent and the name of the domain to which this model belongs. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelAddEntity

> String modelAddEntity(appId, versionId, entityModelCreateObject)



Adds an entity extractor to a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityModelCreateObject = new LuisAuthoringClient.EntityModelCreateObject(); // EntityModelCreateObject | A model object containing the name of the new entity extractor and its children.
apiInstance.modelAddEntity(appId, versionId, entityModelCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityModelCreateObject** | [**EntityModelCreateObject**](EntityModelCreateObject.md)| A model object containing the name of the new entity extractor and its children. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelAddEntityChild

> String modelAddEntityChild(appId, versionId, entityId, childEntityModelCreateObject)



Creates a single child in an existing entity model hierarchy in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity extractor ID.
let childEntityModelCreateObject = new LuisAuthoringClient.ChildEntityModelCreateObject(); // ChildEntityModelCreateObject | A model object containing the name of the new child model and its children.
apiInstance.modelAddEntityChild(appId, versionId, entityId, childEntityModelCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity extractor ID. | 
 **childEntityModelCreateObject** | [**ChildEntityModelCreateObject**](ChildEntityModelCreateObject.md)| A model object containing the name of the new child model and its children. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelAddExplicitListItem

> Number modelAddExplicitListItem(appId, versionId, entityId, item)

Add a new exception to the explicit list for the Pattern.Any entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The Pattern.Any entity extractor ID.
let item = new LuisAuthoringClient.ExplicitListItemCreateObject(); // ExplicitListItemCreateObject | The new explicit list item.
apiInstance.modelAddExplicitListItem(appId, versionId, entityId, item, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The Pattern.Any entity extractor ID. | 
 **item** | [**ExplicitListItemCreateObject**](ExplicitListItemCreateObject.md)| The new explicit list item. | 

### Return type

**Number**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelAddIntent

> String modelAddIntent(appId, versionId, intentCreateObject)



Adds an intent to a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let intentCreateObject = new LuisAuthoringClient.ModelCreateObject(); // ModelCreateObject | A model object containing the name of the new intent.
apiInstance.modelAddIntent(appId, versionId, intentCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **intentCreateObject** | [**ModelCreateObject**](ModelCreateObject.md)| A model object containing the name of the new intent. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelAddPrebuilt

> [PrebuiltEntityExtractor] modelAddPrebuilt(appId, versionId, prebuiltExtractorNames)



Adds a list of prebuilt entities to a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let prebuiltExtractorNames = ["null"]; // [String] | An array of prebuilt entity extractor names.
apiInstance.modelAddPrebuilt(appId, versionId, prebuiltExtractorNames, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **prebuiltExtractorNames** | [**[String]**](String.md)| An array of prebuilt entity extractor names. | 

### Return type

[**[PrebuiltEntityExtractor]**](PrebuiltEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelAddSubList

> Number modelAddSubList(appId, versionId, clEntityId, wordListCreateObject)



Adds a sublist to an existing list entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let clEntityId = "clEntityId_example"; // String | The list entity extractor ID.
let wordListCreateObject = new LuisAuthoringClient.WordListObject(); // WordListObject | Words list.
apiInstance.modelAddSubList(appId, versionId, clEntityId, wordListCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **clEntityId** | **String**| The list entity extractor ID. | 
 **wordListCreateObject** | [**WordListObject**](WordListObject.md)| Words list. | 

### Return type

**Number**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelCreateClosedListEntityRole

> String modelCreateClosedListEntityRole(appId, versionId, entityId, entityRoleCreateObject)

Create a role for a list entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity model ID.
let entityRoleCreateObject = new LuisAuthoringClient.EntityRoleCreateObject(); // EntityRoleCreateObject | An entity role object containing the name of role.
apiInstance.modelCreateClosedListEntityRole(appId, versionId, entityId, entityRoleCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity model ID. | 
 **entityRoleCreateObject** | [**EntityRoleCreateObject**](EntityRoleCreateObject.md)| An entity role object containing the name of role. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelCreateCompositeEntityRole

> String modelCreateCompositeEntityRole(appId, versionId, cEntityId, entityRoleCreateObject)

Create a role for a composite entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let cEntityId = "cEntityId_example"; // String | The composite entity extractor ID.
let entityRoleCreateObject = new LuisAuthoringClient.EntityRoleCreateObject(); // EntityRoleCreateObject | An entity role object containing the name of role.
apiInstance.modelCreateCompositeEntityRole(appId, versionId, cEntityId, entityRoleCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **cEntityId** | **String**| The composite entity extractor ID. | 
 **entityRoleCreateObject** | [**EntityRoleCreateObject**](EntityRoleCreateObject.md)| An entity role object containing the name of role. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelCreateCustomPrebuiltEntityRole

> String modelCreateCustomPrebuiltEntityRole(appId, versionId, entityId, entityRoleCreateObject)

Create a role for a prebuilt entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity model ID.
let entityRoleCreateObject = new LuisAuthoringClient.EntityRoleCreateObject(); // EntityRoleCreateObject | An entity role object containing the name of role.
apiInstance.modelCreateCustomPrebuiltEntityRole(appId, versionId, entityId, entityRoleCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity model ID. | 
 **entityRoleCreateObject** | [**EntityRoleCreateObject**](EntityRoleCreateObject.md)| An entity role object containing the name of role. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelCreateEntityRole

> String modelCreateEntityRole(appId, versionId, entityId, entityRoleCreateObject)

Create an entity role in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity model ID.
let entityRoleCreateObject = new LuisAuthoringClient.EntityRoleCreateObject(); // EntityRoleCreateObject | An entity role object containing the name of role.
apiInstance.modelCreateEntityRole(appId, versionId, entityId, entityRoleCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity model ID. | 
 **entityRoleCreateObject** | [**EntityRoleCreateObject**](EntityRoleCreateObject.md)| An entity role object containing the name of role. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelCreateHierarchicalEntityRole

> String modelCreateHierarchicalEntityRole(appId, versionId, hEntityId, entityRoleCreateObject)

Create a role for an hierarchical entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let hEntityId = "hEntityId_example"; // String | The hierarchical entity extractor ID.
let entityRoleCreateObject = new LuisAuthoringClient.EntityRoleCreateObject(); // EntityRoleCreateObject | An entity role object containing the name of role.
apiInstance.modelCreateHierarchicalEntityRole(appId, versionId, hEntityId, entityRoleCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **hEntityId** | **String**| The hierarchical entity extractor ID. | 
 **entityRoleCreateObject** | [**EntityRoleCreateObject**](EntityRoleCreateObject.md)| An entity role object containing the name of role. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelCreatePatternAnyEntityModel

> String modelCreatePatternAnyEntityModel(appId, versionId, extractorCreateObject)

Adds a pattern.any entity extractor to a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let extractorCreateObject = new LuisAuthoringClient.PatternAnyModelCreateObject(); // PatternAnyModelCreateObject | A model object containing the name and explicit list for the new Pattern.Any entity extractor.
apiInstance.modelCreatePatternAnyEntityModel(appId, versionId, extractorCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **extractorCreateObject** | [**PatternAnyModelCreateObject**](PatternAnyModelCreateObject.md)| A model object containing the name and explicit list for the new Pattern.Any entity extractor. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelCreatePatternAnyEntityRole

> String modelCreatePatternAnyEntityRole(appId, versionId, entityId, entityRoleCreateObject)

Create a role for an Pattern.any entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity model ID.
let entityRoleCreateObject = new LuisAuthoringClient.EntityRoleCreateObject(); // EntityRoleCreateObject | An entity role object containing the name of role.
apiInstance.modelCreatePatternAnyEntityRole(appId, versionId, entityId, entityRoleCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity model ID. | 
 **entityRoleCreateObject** | [**EntityRoleCreateObject**](EntityRoleCreateObject.md)| An entity role object containing the name of role. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelCreatePrebuiltEntityRole

> String modelCreatePrebuiltEntityRole(appId, versionId, entityId, entityRoleCreateObject)

Create a role for a prebuilt entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity model ID.
let entityRoleCreateObject = new LuisAuthoringClient.EntityRoleCreateObject(); // EntityRoleCreateObject | An entity role object containing the name of role.
apiInstance.modelCreatePrebuiltEntityRole(appId, versionId, entityId, entityRoleCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity model ID. | 
 **entityRoleCreateObject** | [**EntityRoleCreateObject**](EntityRoleCreateObject.md)| An entity role object containing the name of role. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelCreateRegexEntityModel

> String modelCreateRegexEntityModel(appId, versionId, regexEntityExtractorCreateObj)

Adds a regular expression entity model to a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let regexEntityExtractorCreateObj = new LuisAuthoringClient.RegexModelCreateObject(); // RegexModelCreateObject | A model object containing the name and regex pattern for the new regular expression entity extractor.
apiInstance.modelCreateRegexEntityModel(appId, versionId, regexEntityExtractorCreateObj, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **regexEntityExtractorCreateObj** | [**RegexModelCreateObject**](RegexModelCreateObject.md)| A model object containing the name and regex pattern for the new regular expression entity extractor. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelCreateRegexEntityRole

> String modelCreateRegexEntityRole(appId, versionId, entityId, entityRoleCreateObject)

Create a role for an regular expression entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity model ID.
let entityRoleCreateObject = new LuisAuthoringClient.EntityRoleCreateObject(); // EntityRoleCreateObject | An entity role object containing the name of role.
apiInstance.modelCreateRegexEntityRole(appId, versionId, entityId, entityRoleCreateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity model ID. | 
 **entityRoleCreateObject** | [**EntityRoleCreateObject**](EntityRoleCreateObject.md)| An entity role object containing the name of role. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelDeleteClosedList

> OperationStatus modelDeleteClosedList(appId, versionId, clEntityId)



Deletes a list entity model from a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let clEntityId = "clEntityId_example"; // String | The list entity model ID.
apiInstance.modelDeleteClosedList(appId, versionId, clEntityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **clEntityId** | **String**| The list entity model ID. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteClosedListEntityRole

> OperationStatus modelDeleteClosedListEntityRole(appId, versionId, entityId, roleId)

Delete a role for a given list entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity ID.
let roleId = "roleId_example"; // String | The entity role Id.
apiInstance.modelDeleteClosedListEntityRole(appId, versionId, entityId, roleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity ID. | 
 **roleId** | **String**| The entity role Id. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteCompositeEntity

> OperationStatus modelDeleteCompositeEntity(appId, versionId, cEntityId)



Deletes a composite entity from a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let cEntityId = "cEntityId_example"; // String | The composite entity extractor ID.
apiInstance.modelDeleteCompositeEntity(appId, versionId, cEntityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **cEntityId** | **String**| The composite entity extractor ID. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteCompositeEntityChild

> OperationStatus modelDeleteCompositeEntityChild(appId, versionId, cEntityId, cChildId)



Deletes a composite entity extractor child from a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let cEntityId = "cEntityId_example"; // String | The composite entity extractor ID.
let cChildId = "cChildId_example"; // String | The hierarchical entity extractor child ID.
apiInstance.modelDeleteCompositeEntityChild(appId, versionId, cEntityId, cChildId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **cEntityId** | **String**| The composite entity extractor ID. | 
 **cChildId** | **String**| The hierarchical entity extractor child ID. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteCompositeEntityRole

> OperationStatus modelDeleteCompositeEntityRole(appId, versionId, cEntityId, roleId)

Delete a role for a given composite entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let cEntityId = "cEntityId_example"; // String | The composite entity extractor ID.
let roleId = "roleId_example"; // String | The entity role Id.
apiInstance.modelDeleteCompositeEntityRole(appId, versionId, cEntityId, roleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **cEntityId** | **String**| The composite entity extractor ID. | 
 **roleId** | **String**| The entity role Id. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteCustomEntityRole

> OperationStatus modelDeleteCustomEntityRole(appId, versionId, entityId, roleId)

Delete a role for a given prebuilt entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity ID.
let roleId = "roleId_example"; // String | The entity role Id.
apiInstance.modelDeleteCustomEntityRole(appId, versionId, entityId, roleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity ID. | 
 **roleId** | **String**| The entity role Id. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteCustomPrebuiltDomain

> OperationStatus modelDeleteCustomPrebuiltDomain(appId, versionId, domainName)



Deletes a prebuilt domain&#39;s models in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let domainName = "domainName_example"; // String | Domain name.
apiInstance.modelDeleteCustomPrebuiltDomain(appId, versionId, domainName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **domainName** | **String**| Domain name. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteEntity

> OperationStatus modelDeleteEntity(appId, versionId, entityId)



Deletes an entity or a child from a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity extractor or the child entity extractor ID.
apiInstance.modelDeleteEntity(appId, versionId, entityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity extractor or the child entity extractor ID. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteEntityFeature

> OperationStatus modelDeleteEntityFeature(appId, versionId, entityId, featureRelationDeleteObject)



Deletes a relation from the feature relations used by the entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity extractor ID.
let featureRelationDeleteObject = new LuisAuthoringClient.ModelFeatureInformation(); // ModelFeatureInformation | A feature information object containing the feature relation to delete.
apiInstance.modelDeleteEntityFeature(appId, versionId, entityId, featureRelationDeleteObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity extractor ID. | 
 **featureRelationDeleteObject** | [**ModelFeatureInformation**](ModelFeatureInformation.md)| A feature information object containing the feature relation to delete. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteEntityRole

> OperationStatus modelDeleteEntityRole(appId, versionId, entityId, roleId)

Delete an entity role in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity ID.
let roleId = "roleId_example"; // String | The entity role Id.
apiInstance.modelDeleteEntityRole(appId, versionId, entityId, roleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity ID. | 
 **roleId** | **String**| The entity role Id. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteExplicitListItem

> OperationStatus modelDeleteExplicitListItem(appId, versionId, entityId, itemId)

Delete an item from the explicit (exception) list for a Pattern.any entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The pattern.any entity id.
let itemId = 789; // Number | The explicit list item which will be deleted.
apiInstance.modelDeleteExplicitListItem(appId, versionId, entityId, itemId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The pattern.any entity id. | 
 **itemId** | **Number**| The explicit list item which will be deleted. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteHierarchicalEntity

> OperationStatus modelDeleteHierarchicalEntity(appId, versionId, hEntityId)



Deletes a hierarchical entity from a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let hEntityId = "hEntityId_example"; // String | The hierarchical entity extractor ID.
apiInstance.modelDeleteHierarchicalEntity(appId, versionId, hEntityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **hEntityId** | **String**| The hierarchical entity extractor ID. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteHierarchicalEntityChild

> OperationStatus modelDeleteHierarchicalEntityChild(appId, versionId, hEntityId, hChildId)



Deletes a hierarchical entity extractor child in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let hEntityId = "hEntityId_example"; // String | The hierarchical entity extractor ID.
let hChildId = "hChildId_example"; // String | The hierarchical entity extractor child ID.
apiInstance.modelDeleteHierarchicalEntityChild(appId, versionId, hEntityId, hChildId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **hEntityId** | **String**| The hierarchical entity extractor ID. | 
 **hChildId** | **String**| The hierarchical entity extractor child ID. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteHierarchicalEntityRole

> OperationStatus modelDeleteHierarchicalEntityRole(appId, versionId, hEntityId, roleId)

Delete a role for a given hierarchical role in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let hEntityId = "hEntityId_example"; // String | The hierarchical entity extractor ID.
let roleId = "roleId_example"; // String | The entity role Id.
apiInstance.modelDeleteHierarchicalEntityRole(appId, versionId, hEntityId, roleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **hEntityId** | **String**| The hierarchical entity extractor ID. | 
 **roleId** | **String**| The entity role Id. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteIntent

> OperationStatus modelDeleteIntent(appId, versionId, intentId, opts)



Deletes an intent from a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let intentId = "intentId_example"; // String | The intent classifier ID.
let opts = {
  'deleteUtterances': false // Boolean | If true, deletes the intent's example utterances. If false, moves the example utterances to the None intent. The default value is false.
};
apiInstance.modelDeleteIntent(appId, versionId, intentId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **intentId** | **String**| The intent classifier ID. | 
 **deleteUtterances** | **Boolean**| If true, deletes the intent&#39;s example utterances. If false, moves the example utterances to the None intent. The default value is false. | [optional] [default to false]

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteIntentFeature

> OperationStatus modelDeleteIntentFeature(appId, versionId, intentId, featureRelationDeleteObject)



Deletes a relation from the feature relations used by the intent in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let intentId = "intentId_example"; // String | The intent classifier ID.
let featureRelationDeleteObject = new LuisAuthoringClient.ModelFeatureInformation(); // ModelFeatureInformation | A feature information object containing the feature relation to delete.
apiInstance.modelDeleteIntentFeature(appId, versionId, intentId, featureRelationDeleteObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **intentId** | **String**| The intent classifier ID. | 
 **featureRelationDeleteObject** | [**ModelFeatureInformation**](ModelFeatureInformation.md)| A feature information object containing the feature relation to delete. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeletePatternAnyEntityModel

> OperationStatus modelDeletePatternAnyEntityModel(appId, versionId, entityId)

Deletes a Pattern.Any entity extractor from a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The Pattern.Any entity extractor ID.
apiInstance.modelDeletePatternAnyEntityModel(appId, versionId, entityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The Pattern.Any entity extractor ID. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeletePatternAnyEntityRole

> OperationStatus modelDeletePatternAnyEntityRole(appId, versionId, entityId, roleId)

Delete a role for a given Pattern.any entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity ID.
let roleId = "roleId_example"; // String | The entity role Id.
apiInstance.modelDeletePatternAnyEntityRole(appId, versionId, entityId, roleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity ID. | 
 **roleId** | **String**| The entity role Id. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeletePrebuilt

> OperationStatus modelDeletePrebuilt(appId, versionId, prebuiltId)



Deletes a prebuilt entity extractor from a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let prebuiltId = "prebuiltId_example"; // String | The prebuilt entity extractor ID.
apiInstance.modelDeletePrebuilt(appId, versionId, prebuiltId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **prebuiltId** | **String**| The prebuilt entity extractor ID. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeletePrebuiltEntityRole

> OperationStatus modelDeletePrebuiltEntityRole(appId, versionId, entityId, roleId)

Delete a role in a prebuilt entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity ID.
let roleId = "roleId_example"; // String | The entity role Id.
apiInstance.modelDeletePrebuiltEntityRole(appId, versionId, entityId, roleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity ID. | 
 **roleId** | **String**| The entity role Id. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteRegexEntityModel

> OperationStatus modelDeleteRegexEntityModel(appId, versionId, regexEntityId)

Deletes a regular expression entity from a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let regexEntityId = "regexEntityId_example"; // String | The regular expression entity extractor ID.
apiInstance.modelDeleteRegexEntityModel(appId, versionId, regexEntityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **regexEntityId** | **String**| The regular expression entity extractor ID. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteRegexEntityRole

> OperationStatus modelDeleteRegexEntityRole(appId, versionId, entityId, roleId)

Delete a role for a given regular expression in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity ID.
let roleId = "roleId_example"; // String | The entity role Id.
apiInstance.modelDeleteRegexEntityRole(appId, versionId, entityId, roleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity ID. | 
 **roleId** | **String**| The entity role Id. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelDeleteSubList

> OperationStatus modelDeleteSubList(appId, versionId, clEntityId, subListId)



Deletes a sublist of a specific list entity model from a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let clEntityId = "clEntityId_example"; // String | The list entity extractor ID.
let subListId = 789; // Number | The sublist ID.
apiInstance.modelDeleteSubList(appId, versionId, clEntityId, subListId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **clEntityId** | **String**| The list entity extractor ID. | 
 **subListId** | **Number**| The sublist ID. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelExamples

> [LabelTextObject] modelExamples(appId, versionId, modelId, opts)



Gets the example utterances for the given intent or entity model in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let modelId = "modelId_example"; // String | The ID (GUID) of the model.
let opts = {
  'skip': 0, // Number | The number of entries to skip. Default value is 0.
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.modelExamples(appId, versionId, modelId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **modelId** | **String**| The ID (GUID) of the model. | 
 **skip** | **Number**| The number of entries to skip. Default value is 0. | [optional] [default to 0]
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[LabelTextObject]**](LabelTextObject.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetClosedList

> ClosedListEntityExtractor modelGetClosedList(appId, versionId, clEntityId)



Gets information about a list entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let clEntityId = "clEntityId_example"; // String | The list model ID.
apiInstance.modelGetClosedList(appId, versionId, clEntityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **clEntityId** | **String**| The list model ID. | 

### Return type

[**ClosedListEntityExtractor**](ClosedListEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetClosedListEntityRole

> EntityRole modelGetClosedListEntityRole(appId, versionId, entityId, roleId)

Get one role for a given list entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | entity ID.
let roleId = "roleId_example"; // String | entity role ID.
apiInstance.modelGetClosedListEntityRole(appId, versionId, entityId, roleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| entity ID. | 
 **roleId** | **String**| entity role ID. | 

### Return type

[**EntityRole**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetCompositeEntity

> CompositeEntityExtractor modelGetCompositeEntity(appId, versionId, cEntityId)



Gets information about a composite entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let cEntityId = "cEntityId_example"; // String | The composite entity extractor ID.
apiInstance.modelGetCompositeEntity(appId, versionId, cEntityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **cEntityId** | **String**| The composite entity extractor ID. | 

### Return type

[**CompositeEntityExtractor**](CompositeEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetCompositeEntityRole

> EntityRole modelGetCompositeEntityRole(appId, versionId, cEntityId, roleId)

Get one role for a given composite entity in a version of the application

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let cEntityId = "cEntityId_example"; // String | The composite entity extractor ID.
let roleId = "roleId_example"; // String | entity role ID.
apiInstance.modelGetCompositeEntityRole(appId, versionId, cEntityId, roleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **cEntityId** | **String**| The composite entity extractor ID. | 
 **roleId** | **String**| entity role ID. | 

### Return type

[**EntityRole**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetCustomEntityRole

> EntityRole modelGetCustomEntityRole(appId, versionId, entityId, roleId)

Get one role for a given prebuilt entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | entity ID.
let roleId = "roleId_example"; // String | entity role ID.
apiInstance.modelGetCustomEntityRole(appId, versionId, entityId, roleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| entity ID. | 
 **roleId** | **String**| entity role ID. | 

### Return type

[**EntityRole**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetEntity

> NDepthEntityExtractor modelGetEntity(appId, versionId, entityId)



Gets information about an entity model in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity extractor ID.
apiInstance.modelGetEntity(appId, versionId, entityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity extractor ID. | 

### Return type

[**NDepthEntityExtractor**](NDepthEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetEntityFeatures

> [ModelFeatureInformation] modelGetEntityFeatures(appId, versionId, entityId)



Gets the information of the features used by the entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity extractor ID.
apiInstance.modelGetEntityFeatures(appId, versionId, entityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity extractor ID. | 

### Return type

[**[ModelFeatureInformation]**](ModelFeatureInformation.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetEntityRole

> EntityRole modelGetEntityRole(appId, versionId, entityId, roleId)

Get one role for a given entity in a version of the application

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | entity ID.
let roleId = "roleId_example"; // String | entity role ID.
apiInstance.modelGetEntityRole(appId, versionId, entityId, roleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| entity ID. | 
 **roleId** | **String**| entity role ID. | 

### Return type

[**EntityRole**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetExplicitList

> [ExplicitListItem] modelGetExplicitList(appId, versionId, entityId)

Get the explicit (exception) list of the pattern.any entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The Pattern.Any entity id.
apiInstance.modelGetExplicitList(appId, versionId, entityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The Pattern.Any entity id. | 

### Return type

[**[ExplicitListItem]**](ExplicitListItem.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetExplicitListItem

> ExplicitListItem modelGetExplicitListItem(appId, versionId, entityId, itemId)

Get the explicit (exception) list of the pattern.any entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The Pattern.Any entity Id.
let itemId = 789; // Number | The explicit list item Id.
apiInstance.modelGetExplicitListItem(appId, versionId, entityId, itemId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The Pattern.Any entity Id. | 
 **itemId** | **Number**| The explicit list item Id. | 

### Return type

[**ExplicitListItem**](ExplicitListItem.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetHierarchicalEntity

> HierarchicalEntityExtractor modelGetHierarchicalEntity(appId, versionId, hEntityId)



Gets information about a hierarchical entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let hEntityId = "hEntityId_example"; // String | The hierarchical entity extractor ID.
apiInstance.modelGetHierarchicalEntity(appId, versionId, hEntityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **hEntityId** | **String**| The hierarchical entity extractor ID. | 

### Return type

[**HierarchicalEntityExtractor**](HierarchicalEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetHierarchicalEntityChild

> HierarchicalChildEntity modelGetHierarchicalEntityChild(appId, versionId, hEntityId, hChildId)



Gets information about the child&#39;s model contained in an hierarchical entity child model in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let hEntityId = "hEntityId_example"; // String | The hierarchical entity extractor ID.
let hChildId = "hChildId_example"; // String | The hierarchical entity extractor child ID.
apiInstance.modelGetHierarchicalEntityChild(appId, versionId, hEntityId, hChildId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **hEntityId** | **String**| The hierarchical entity extractor ID. | 
 **hChildId** | **String**| The hierarchical entity extractor child ID. | 

### Return type

[**HierarchicalChildEntity**](HierarchicalChildEntity.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetHierarchicalEntityRole

> EntityRole modelGetHierarchicalEntityRole(appId, versionId, hEntityId, roleId)

Get one role for a given hierarchical entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let hEntityId = "hEntityId_example"; // String | The hierarchical entity extractor ID.
let roleId = "roleId_example"; // String | entity role ID.
apiInstance.modelGetHierarchicalEntityRole(appId, versionId, hEntityId, roleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **hEntityId** | **String**| The hierarchical entity extractor ID. | 
 **roleId** | **String**| entity role ID. | 

### Return type

[**EntityRole**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetIntent

> IntentClassifier modelGetIntent(appId, versionId, intentId)



Gets information about the intent model in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let intentId = "intentId_example"; // String | The intent classifier ID.
apiInstance.modelGetIntent(appId, versionId, intentId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **intentId** | **String**| The intent classifier ID. | 

### Return type

[**IntentClassifier**](IntentClassifier.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetIntentFeatures

> [ModelFeatureInformation] modelGetIntentFeatures(appId, versionId, intentId)



Gets the information of the features used by the intent in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let intentId = "intentId_example"; // String | The intent classifier ID.
apiInstance.modelGetIntentFeatures(appId, versionId, intentId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **intentId** | **String**| The intent classifier ID. | 

### Return type

[**[ModelFeatureInformation]**](ModelFeatureInformation.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetPatternAnyEntityInfo

> PatternAnyEntityExtractor modelGetPatternAnyEntityInfo(appId, versionId, entityId)

Gets information about the Pattern.Any model in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity extractor ID.
apiInstance.modelGetPatternAnyEntityInfo(appId, versionId, entityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity extractor ID. | 

### Return type

[**PatternAnyEntityExtractor**](PatternAnyEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetPatternAnyEntityRole

> EntityRole modelGetPatternAnyEntityRole(appId, versionId, entityId, roleId)

Get one role for a given Pattern.any entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | entity ID.
let roleId = "roleId_example"; // String | entity role ID.
apiInstance.modelGetPatternAnyEntityRole(appId, versionId, entityId, roleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| entity ID. | 
 **roleId** | **String**| entity role ID. | 

### Return type

[**EntityRole**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetPrebuilt

> PrebuiltEntityExtractor modelGetPrebuilt(appId, versionId, prebuiltId)



Gets information about a prebuilt entity model in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let prebuiltId = "prebuiltId_example"; // String | The prebuilt entity extractor ID.
apiInstance.modelGetPrebuilt(appId, versionId, prebuiltId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **prebuiltId** | **String**| The prebuilt entity extractor ID. | 

### Return type

[**PrebuiltEntityExtractor**](PrebuiltEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetPrebuiltEntityRole

> EntityRole modelGetPrebuiltEntityRole(appId, versionId, entityId, roleId)

Get one role for a given prebuilt entity in a version of the application

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | entity ID.
let roleId = "roleId_example"; // String | entity role ID.
apiInstance.modelGetPrebuiltEntityRole(appId, versionId, entityId, roleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| entity ID. | 
 **roleId** | **String**| entity role ID. | 

### Return type

[**EntityRole**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetRegexEntityEntityInfo

> RegexEntityExtractor modelGetRegexEntityEntityInfo(appId, versionId, regexEntityId)

Gets information about a regular expression entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let regexEntityId = "regexEntityId_example"; // String | The regular expression entity model ID.
apiInstance.modelGetRegexEntityEntityInfo(appId, versionId, regexEntityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **regexEntityId** | **String**| The regular expression entity model ID. | 

### Return type

[**RegexEntityExtractor**](RegexEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelGetRegexEntityRole

> EntityRole modelGetRegexEntityRole(appId, versionId, entityId, roleId)

Get one role for a given regular expression entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | entity ID.
let roleId = "roleId_example"; // String | entity role ID.
apiInstance.modelGetRegexEntityRole(appId, versionId, entityId, roleId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| entity ID. | 
 **roleId** | **String**| entity role ID. | 

### Return type

[**EntityRole**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListClosedListEntityRoles

> [EntityRole] modelListClosedListEntityRoles(appId, versionId, entityId)

Get all roles for a list entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | entity Id
apiInstance.modelListClosedListEntityRoles(appId, versionId, entityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| entity Id | 

### Return type

[**[EntityRole]**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListClosedLists

> [ClosedListEntityExtractor] modelListClosedLists(appId, versionId, opts)



Gets information about all the list entity models in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let opts = {
  'skip': 0, // Number | The number of entries to skip. Default value is 0.
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.modelListClosedLists(appId, versionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **skip** | **Number**| The number of entries to skip. Default value is 0. | [optional] [default to 0]
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[ClosedListEntityExtractor]**](ClosedListEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListCompositeEntities

> [CompositeEntityExtractor] modelListCompositeEntities(appId, versionId, opts)



Gets information about all the composite entity models in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let opts = {
  'skip': 0, // Number | The number of entries to skip. Default value is 0.
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.modelListCompositeEntities(appId, versionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **skip** | **Number**| The number of entries to skip. Default value is 0. | [optional] [default to 0]
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[CompositeEntityExtractor]**](CompositeEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListCompositeEntityRoles

> [EntityRole] modelListCompositeEntityRoles(appId, versionId, cEntityId)

Get all roles for a composite entity in a version of the application

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let cEntityId = "cEntityId_example"; // String | The composite entity extractor ID.
apiInstance.modelListCompositeEntityRoles(appId, versionId, cEntityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **cEntityId** | **String**| The composite entity extractor ID. | 

### Return type

[**[EntityRole]**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListCustomPrebuiltEntities

> [EntityExtractor] modelListCustomPrebuiltEntities(appId, versionId)



Gets all prebuilt entities used in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
apiInstance.modelListCustomPrebuiltEntities(appId, versionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 

### Return type

[**[EntityExtractor]**](EntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListCustomPrebuiltEntityRoles

> [EntityRole] modelListCustomPrebuiltEntityRoles(appId, versionId, entityId)

Get all roles for a prebuilt entity in a version of the application

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | entity Id
apiInstance.modelListCustomPrebuiltEntityRoles(appId, versionId, entityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| entity Id | 

### Return type

[**[EntityRole]**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListCustomPrebuiltIntents

> [IntentClassifier] modelListCustomPrebuiltIntents(appId, versionId)



Gets information about customizable prebuilt intents added to a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
apiInstance.modelListCustomPrebuiltIntents(appId, versionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 

### Return type

[**[IntentClassifier]**](IntentClassifier.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListCustomPrebuiltModels

> [CustomPrebuiltModel] modelListCustomPrebuiltModels(appId, versionId)



Gets all prebuilt intent and entity model information used in a version of this application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
apiInstance.modelListCustomPrebuiltModels(appId, versionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 

### Return type

[**[CustomPrebuiltModel]**](CustomPrebuiltModel.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListEntities

> [NDepthEntityExtractor] modelListEntities(appId, versionId, opts)



Gets information about all the simple entity models in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let opts = {
  'skip': 0, // Number | The number of entries to skip. Default value is 0.
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.modelListEntities(appId, versionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **skip** | **Number**| The number of entries to skip. Default value is 0. | [optional] [default to 0]
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[NDepthEntityExtractor]**](NDepthEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListEntityRoles

> [EntityRole] modelListEntityRoles(appId, versionId, entityId)

Get all roles for an entity in a version of the application

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | entity Id
apiInstance.modelListEntityRoles(appId, versionId, entityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| entity Id | 

### Return type

[**[EntityRole]**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListEntitySuggestions

> [EntitiesSuggestionExample] modelListEntitySuggestions(appId, versionId, entityId, opts)



Get suggested example utterances that would improve the accuracy of the entity model in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The target entity extractor model to enhance.
let opts = {
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.modelListEntitySuggestions(appId, versionId, entityId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The target entity extractor model to enhance. | 
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[EntitiesSuggestionExample]**](EntitiesSuggestionExample.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListHierarchicalEntities

> [HierarchicalEntityExtractor] modelListHierarchicalEntities(appId, versionId, opts)



Gets information about all the hierarchical entity models in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let opts = {
  'skip': 0, // Number | The number of entries to skip. Default value is 0.
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.modelListHierarchicalEntities(appId, versionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **skip** | **Number**| The number of entries to skip. Default value is 0. | [optional] [default to 0]
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[HierarchicalEntityExtractor]**](HierarchicalEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListHierarchicalEntityRoles

> [EntityRole] modelListHierarchicalEntityRoles(appId, versionId, hEntityId)

Get all roles for a hierarchical entity in a version of the application

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let hEntityId = "hEntityId_example"; // String | The hierarchical entity extractor ID.
apiInstance.modelListHierarchicalEntityRoles(appId, versionId, hEntityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **hEntityId** | **String**| The hierarchical entity extractor ID. | 

### Return type

[**[EntityRole]**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListIntentSuggestions

> [IntentsSuggestionExample] modelListIntentSuggestions(appId, versionId, intentId, opts)



Suggests example utterances that would improve the accuracy of the intent model in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let intentId = "intentId_example"; // String | The intent classifier ID.
let opts = {
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.modelListIntentSuggestions(appId, versionId, intentId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **intentId** | **String**| The intent classifier ID. | 
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[IntentsSuggestionExample]**](IntentsSuggestionExample.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListIntents

> [IntentClassifier] modelListIntents(appId, versionId, opts)



Gets information about the intent models in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let opts = {
  'skip': 0, // Number | The number of entries to skip. Default value is 0.
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.modelListIntents(appId, versionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **skip** | **Number**| The number of entries to skip. Default value is 0. | [optional] [default to 0]
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[IntentClassifier]**](IntentClassifier.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListModels

> [ModelInfoResponse] modelListModels(appId, versionId, opts)



Gets information about all the intent and entity models in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let opts = {
  'skip': 0, // Number | The number of entries to skip. Default value is 0.
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.modelListModels(appId, versionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **skip** | **Number**| The number of entries to skip. Default value is 0. | [optional] [default to 0]
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[ModelInfoResponse]**](ModelInfoResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListPatternAnyEntityInfos

> [PatternAnyEntityExtractor] modelListPatternAnyEntityInfos(appId, versionId, opts)

Get information about the Pattern.Any entity models in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let opts = {
  'skip': 0, // Number | The number of entries to skip. Default value is 0.
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.modelListPatternAnyEntityInfos(appId, versionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **skip** | **Number**| The number of entries to skip. Default value is 0. | [optional] [default to 0]
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[PatternAnyEntityExtractor]**](PatternAnyEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListPatternAnyEntityRoles

> [EntityRole] modelListPatternAnyEntityRoles(appId, versionId, entityId)

Get all roles for a Pattern.any entity in a version of the application

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | entity Id
apiInstance.modelListPatternAnyEntityRoles(appId, versionId, entityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| entity Id | 

### Return type

[**[EntityRole]**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListPrebuiltEntities

> [AvailablePrebuiltEntityModel] modelListPrebuiltEntities(appId, versionId)



Gets all the available prebuilt entities in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
apiInstance.modelListPrebuiltEntities(appId, versionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 

### Return type

[**[AvailablePrebuiltEntityModel]**](AvailablePrebuiltEntityModel.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListPrebuiltEntityRoles

> [EntityRole] modelListPrebuiltEntityRoles(appId, versionId, entityId)

Get a prebuilt entity&#39;s roles in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | entity Id
apiInstance.modelListPrebuiltEntityRoles(appId, versionId, entityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| entity Id | 

### Return type

[**[EntityRole]**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListPrebuilts

> [PrebuiltEntityExtractor] modelListPrebuilts(appId, versionId, opts)



Gets information about all the prebuilt entities in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let opts = {
  'skip': 0, // Number | The number of entries to skip. Default value is 0.
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.modelListPrebuilts(appId, versionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **skip** | **Number**| The number of entries to skip. Default value is 0. | [optional] [default to 0]
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[PrebuiltEntityExtractor]**](PrebuiltEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListRegexEntityInfos

> [RegexEntityExtractor] modelListRegexEntityInfos(appId, versionId, opts)

Gets information about the regular expression entity models in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let opts = {
  'skip': 0, // Number | The number of entries to skip. Default value is 0.
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.modelListRegexEntityInfos(appId, versionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **skip** | **Number**| The number of entries to skip. Default value is 0. | [optional] [default to 0]
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[RegexEntityExtractor]**](RegexEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelListRegexEntityRoles

> [EntityRole] modelListRegexEntityRoles(appId, versionId, entityId)

Get all roles for a regular expression entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | entity Id
apiInstance.modelListRegexEntityRoles(appId, versionId, entityId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| entity Id | 

### Return type

[**[EntityRole]**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelPatchClosedList

> OperationStatus modelPatchClosedList(appId, versionId, clEntityId, closedListModelPatchObject)



Adds a batch of sublists to an existing list entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let clEntityId = "clEntityId_example"; // String | The list entity model ID.
let closedListModelPatchObject = new LuisAuthoringClient.ClosedListModelPatchObject(); // ClosedListModelPatchObject | A words list batch.
apiInstance.modelPatchClosedList(appId, versionId, clEntityId, closedListModelPatchObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **clEntityId** | **String**| The list entity model ID. | 
 **closedListModelPatchObject** | [**ClosedListModelPatchObject**](ClosedListModelPatchObject.md)| A words list batch. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelReplaceEntityFeatures

> OperationStatus modelReplaceEntityFeatures(appId, versionId, entityId, featureRelationsUpdateObject)



Updates the information of the features used by the entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity extractor ID.
let featureRelationsUpdateObject = [new LuisAuthoringClient.ModelFeatureInformation()]; // [ModelFeatureInformation] | A list of feature information objects containing the new feature relations.
apiInstance.modelReplaceEntityFeatures(appId, versionId, entityId, featureRelationsUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity extractor ID. | 
 **featureRelationsUpdateObject** | [**[ModelFeatureInformation]**](ModelFeatureInformation.md)| A list of feature information objects containing the new feature relations. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelReplaceIntentFeatures

> OperationStatus modelReplaceIntentFeatures(appId, versionId, intentId, featureRelationsUpdateObject)



Updates the information of the features used by the intent in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let intentId = "intentId_example"; // String | The intent classifier ID.
let featureRelationsUpdateObject = [new LuisAuthoringClient.ModelFeatureInformation()]; // [ModelFeatureInformation] | A list of feature information objects containing the new feature relations.
apiInstance.modelReplaceIntentFeatures(appId, versionId, intentId, featureRelationsUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **intentId** | **String**| The intent classifier ID. | 
 **featureRelationsUpdateObject** | [**[ModelFeatureInformation]**](ModelFeatureInformation.md)| A list of feature information objects containing the new feature relations. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdateClosedList

> OperationStatus modelUpdateClosedList(appId, versionId, clEntityId, closedListModelUpdateObject)



Updates the list entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let clEntityId = "clEntityId_example"; // String | The list model ID.
let closedListModelUpdateObject = new LuisAuthoringClient.ClosedListModelUpdateObject(); // ClosedListModelUpdateObject | The new list entity name and words list.
apiInstance.modelUpdateClosedList(appId, versionId, clEntityId, closedListModelUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **clEntityId** | **String**| The list model ID. | 
 **closedListModelUpdateObject** | [**ClosedListModelUpdateObject**](ClosedListModelUpdateObject.md)| The new list entity name and words list. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdateClosedListEntityRole

> OperationStatus modelUpdateClosedListEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject)

Update a role for a given list entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity ID.
let roleId = "roleId_example"; // String | The entity role ID.
let entityRoleUpdateObject = new LuisAuthoringClient.EntityRoleUpdateObject(); // EntityRoleUpdateObject | The new entity role.
apiInstance.modelUpdateClosedListEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity ID. | 
 **roleId** | **String**| The entity role ID. | 
 **entityRoleUpdateObject** | [**EntityRoleUpdateObject**](EntityRoleUpdateObject.md)| The new entity role. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdateCompositeEntity

> OperationStatus modelUpdateCompositeEntity(appId, versionId, cEntityId, compositeModelUpdateObject)



Updates a composite entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let cEntityId = "cEntityId_example"; // String | The composite entity extractor ID.
let compositeModelUpdateObject = new LuisAuthoringClient.CompositeEntityModel(); // CompositeEntityModel | A model object containing the new entity extractor name and children.
apiInstance.modelUpdateCompositeEntity(appId, versionId, cEntityId, compositeModelUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **cEntityId** | **String**| The composite entity extractor ID. | 
 **compositeModelUpdateObject** | [**CompositeEntityModel**](CompositeEntityModel.md)| A model object containing the new entity extractor name and children. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdateCompositeEntityRole

> OperationStatus modelUpdateCompositeEntityRole(appId, versionId, cEntityId, roleId, entityRoleUpdateObject)

Update a role for a given composite entity in a version of the application

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let cEntityId = "cEntityId_example"; // String | The composite entity extractor ID.
let roleId = "roleId_example"; // String | The entity role ID.
let entityRoleUpdateObject = new LuisAuthoringClient.EntityRoleUpdateObject(); // EntityRoleUpdateObject | The new entity role.
apiInstance.modelUpdateCompositeEntityRole(appId, versionId, cEntityId, roleId, entityRoleUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **cEntityId** | **String**| The composite entity extractor ID. | 
 **roleId** | **String**| The entity role ID. | 
 **entityRoleUpdateObject** | [**EntityRoleUpdateObject**](EntityRoleUpdateObject.md)| The new entity role. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdateCustomPrebuiltEntityRole

> OperationStatus modelUpdateCustomPrebuiltEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject)

Update a role for a given prebuilt entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity ID.
let roleId = "roleId_example"; // String | The entity role ID.
let entityRoleUpdateObject = new LuisAuthoringClient.EntityRoleUpdateObject(); // EntityRoleUpdateObject | The new entity role.
apiInstance.modelUpdateCustomPrebuiltEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity ID. | 
 **roleId** | **String**| The entity role ID. | 
 **entityRoleUpdateObject** | [**EntityRoleUpdateObject**](EntityRoleUpdateObject.md)| The new entity role. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdateEntityChild

> OperationStatus modelUpdateEntityChild(appId, versionId, entityId, entityModelUpdateObject)



Updates the name of an entity extractor or the name and instanceOf model of a child entity extractor.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity extractor or the child entity extractor ID.
let entityModelUpdateObject = new LuisAuthoringClient.EntityModelUpdateObject(); // EntityModelUpdateObject | A model object containing the name new entity extractor or the name and instance of model of a child entity extractor 
apiInstance.modelUpdateEntityChild(appId, versionId, entityId, entityModelUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity extractor or the child entity extractor ID. | 
 **entityModelUpdateObject** | [**EntityModelUpdateObject**](EntityModelUpdateObject.md)| A model object containing the name new entity extractor or the name and instance of model of a child entity extractor  | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdateEntityRole

> OperationStatus modelUpdateEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject)

Update a role for a given entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity ID.
let roleId = "roleId_example"; // String | The entity role ID.
let entityRoleUpdateObject = new LuisAuthoringClient.EntityRoleUpdateObject(); // EntityRoleUpdateObject | The new entity role.
apiInstance.modelUpdateEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity ID. | 
 **roleId** | **String**| The entity role ID. | 
 **entityRoleUpdateObject** | [**EntityRoleUpdateObject**](EntityRoleUpdateObject.md)| The new entity role. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdateExplicitListItem

> OperationStatus modelUpdateExplicitListItem(appId, versionId, entityId, itemId, item)

Updates an explicit (exception) list item for a Pattern.Any entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The Pattern.Any entity extractor ID.
let itemId = 789; // Number | The explicit list item ID.
let item = new LuisAuthoringClient.ExplicitListItemUpdateObject(); // ExplicitListItemUpdateObject | The new explicit list item.
apiInstance.modelUpdateExplicitListItem(appId, versionId, entityId, itemId, item, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The Pattern.Any entity extractor ID. | 
 **itemId** | **Number**| The explicit list item ID. | 
 **item** | [**ExplicitListItemUpdateObject**](ExplicitListItemUpdateObject.md)| The new explicit list item. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdateHierarchicalEntity

> OperationStatus modelUpdateHierarchicalEntity(appId, versionId, hEntityId, modelUpdateObject)



Updates the name of a hierarchical entity model in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let hEntityId = "hEntityId_example"; // String | The hierarchical entity extractor ID.
let modelUpdateObject = new LuisAuthoringClient.ModelUpdateObject(); // ModelUpdateObject | Model containing names of the hierarchical entity.
apiInstance.modelUpdateHierarchicalEntity(appId, versionId, hEntityId, modelUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **hEntityId** | **String**| The hierarchical entity extractor ID. | 
 **modelUpdateObject** | [**ModelUpdateObject**](ModelUpdateObject.md)| Model containing names of the hierarchical entity. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdateHierarchicalEntityChild

> OperationStatus modelUpdateHierarchicalEntityChild(appId, versionId, hEntityId, hChildId, hierarchicalChildModelUpdateObject)



Renames a single child in an existing hierarchical entity model in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let hEntityId = "hEntityId_example"; // String | The hierarchical entity extractor ID.
let hChildId = "hChildId_example"; // String | The hierarchical entity extractor child ID.
let hierarchicalChildModelUpdateObject = new LuisAuthoringClient.ModelAddCompositeEntityChildRequest(); // ModelAddCompositeEntityChildRequest | Model object containing new name of the hierarchical entity child.
apiInstance.modelUpdateHierarchicalEntityChild(appId, versionId, hEntityId, hChildId, hierarchicalChildModelUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **hEntityId** | **String**| The hierarchical entity extractor ID. | 
 **hChildId** | **String**| The hierarchical entity extractor child ID. | 
 **hierarchicalChildModelUpdateObject** | [**ModelAddCompositeEntityChildRequest**](ModelAddCompositeEntityChildRequest.md)| Model object containing new name of the hierarchical entity child. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdateHierarchicalEntityRole

> OperationStatus modelUpdateHierarchicalEntityRole(appId, versionId, hEntityId, roleId, entityRoleUpdateObject)

Update a role for a given hierarchical entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let hEntityId = "hEntityId_example"; // String | The hierarchical entity extractor ID.
let roleId = "roleId_example"; // String | The entity role ID.
let entityRoleUpdateObject = new LuisAuthoringClient.EntityRoleUpdateObject(); // EntityRoleUpdateObject | The new entity role.
apiInstance.modelUpdateHierarchicalEntityRole(appId, versionId, hEntityId, roleId, entityRoleUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **hEntityId** | **String**| The hierarchical entity extractor ID. | 
 **roleId** | **String**| The entity role ID. | 
 **entityRoleUpdateObject** | [**EntityRoleUpdateObject**](EntityRoleUpdateObject.md)| The new entity role. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdateIntent

> OperationStatus modelUpdateIntent(appId, versionId, intentId, modelUpdateObject)



Updates the name of an intent in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let intentId = "intentId_example"; // String | The intent classifier ID.
let modelUpdateObject = new LuisAuthoringClient.ModelUpdateObject(); // ModelUpdateObject | A model object containing the new intent name.
apiInstance.modelUpdateIntent(appId, versionId, intentId, modelUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **intentId** | **String**| The intent classifier ID. | 
 **modelUpdateObject** | [**ModelUpdateObject**](ModelUpdateObject.md)| A model object containing the new intent name. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdatePatternAnyEntityModel

> OperationStatus modelUpdatePatternAnyEntityModel(appId, versionId, entityId, patternAnyUpdateObject)

Updates the name and explicit (exception) list of a Pattern.Any entity model in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The Pattern.Any entity extractor ID.
let patternAnyUpdateObject = new LuisAuthoringClient.PatternAnyModelUpdateObject(); // PatternAnyModelUpdateObject | An object containing the explicit list of the Pattern.Any entity.
apiInstance.modelUpdatePatternAnyEntityModel(appId, versionId, entityId, patternAnyUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The Pattern.Any entity extractor ID. | 
 **patternAnyUpdateObject** | [**PatternAnyModelUpdateObject**](PatternAnyModelUpdateObject.md)| An object containing the explicit list of the Pattern.Any entity. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdatePatternAnyEntityRole

> OperationStatus modelUpdatePatternAnyEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject)

Update a role for a given Pattern.any entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity ID.
let roleId = "roleId_example"; // String | The entity role ID.
let entityRoleUpdateObject = new LuisAuthoringClient.EntityRoleUpdateObject(); // EntityRoleUpdateObject | The new entity role.
apiInstance.modelUpdatePatternAnyEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity ID. | 
 **roleId** | **String**| The entity role ID. | 
 **entityRoleUpdateObject** | [**EntityRoleUpdateObject**](EntityRoleUpdateObject.md)| The new entity role. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdatePrebuiltEntityRole

> OperationStatus modelUpdatePrebuiltEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject)

Update a role for a given prebuilt entity in a version of the application

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity ID.
let roleId = "roleId_example"; // String | The entity role ID.
let entityRoleUpdateObject = new LuisAuthoringClient.EntityRoleUpdateObject(); // EntityRoleUpdateObject | The new entity role.
apiInstance.modelUpdatePrebuiltEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity ID. | 
 **roleId** | **String**| The entity role ID. | 
 **entityRoleUpdateObject** | [**EntityRoleUpdateObject**](EntityRoleUpdateObject.md)| The new entity role. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdateRegexEntityModel

> OperationStatus modelUpdateRegexEntityModel(appId, versionId, regexEntityId, regexEntityUpdateObject)

Updates the regular expression entity in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let regexEntityId = "regexEntityId_example"; // String | The regular expression entity extractor ID.
let regexEntityUpdateObject = new LuisAuthoringClient.RegexModelUpdateObject(); // RegexModelUpdateObject | An object containing the new entity name and regex pattern.
apiInstance.modelUpdateRegexEntityModel(appId, versionId, regexEntityId, regexEntityUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **regexEntityId** | **String**| The regular expression entity extractor ID. | 
 **regexEntityUpdateObject** | [**RegexModelUpdateObject**](RegexModelUpdateObject.md)| An object containing the new entity name and regex pattern. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdateRegexEntityRole

> OperationStatus modelUpdateRegexEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject)

Update a role for a given regular expression entity in a version of the application

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let entityId = "entityId_example"; // String | The entity ID.
let roleId = "roleId_example"; // String | The entity role ID.
let entityRoleUpdateObject = new LuisAuthoringClient.EntityRoleUpdateObject(); // EntityRoleUpdateObject | The new entity role.
apiInstance.modelUpdateRegexEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **entityId** | **String**| The entity ID. | 
 **roleId** | **String**| The entity role ID. | 
 **entityRoleUpdateObject** | [**EntityRoleUpdateObject**](EntityRoleUpdateObject.md)| The new entity role. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modelUpdateSubList

> OperationStatus modelUpdateSubList(appId, versionId, clEntityId, subListId, wordListBaseUpdateObject)



Updates one of the list entity&#39;s sublists in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let clEntityId = "clEntityId_example"; // String | The list entity extractor ID.
let subListId = 789; // Number | The sublist ID.
let wordListBaseUpdateObject = new LuisAuthoringClient.WordListBaseUpdateObject(); // WordListBaseUpdateObject | A sublist update object containing the new canonical form and the list of words.
apiInstance.modelUpdateSubList(appId, versionId, clEntityId, subListId, wordListBaseUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **clEntityId** | **String**| The list entity extractor ID. | 
 **subListId** | **Number**| The sublist ID. | 
 **wordListBaseUpdateObject** | [**WordListBaseUpdateObject**](WordListBaseUpdateObject.md)| A sublist update object containing the new canonical form and the list of words. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patternAddPattern

> PatternRuleInfo patternAddPattern(appId, versionId, pattern)

Adds a pattern to a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let pattern = new LuisAuthoringClient.PatternRuleCreateObject(); // PatternRuleCreateObject | The input pattern.
apiInstance.patternAddPattern(appId, versionId, pattern, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **pattern** | [**PatternRuleCreateObject**](PatternRuleCreateObject.md)| The input pattern. | 

### Return type

[**PatternRuleInfo**](PatternRuleInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patternBatchAddPatterns

> [PatternRuleInfo] patternBatchAddPatterns(appId, versionId, patterns)

Adds a batch of patterns in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let patterns = [new LuisAuthoringClient.PatternRuleCreateObject()]; // [PatternRuleCreateObject] | A JSON array containing patterns.
apiInstance.patternBatchAddPatterns(appId, versionId, patterns, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **patterns** | [**[PatternRuleCreateObject]**](PatternRuleCreateObject.md)| A JSON array containing patterns. | 

### Return type

[**[PatternRuleInfo]**](PatternRuleInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patternDeletePattern

> OperationStatus patternDeletePattern(appId, versionId, patternId)

Deletes the pattern with the specified ID from a version of the application..

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let patternId = "patternId_example"; // String | The pattern ID.
apiInstance.patternDeletePattern(appId, versionId, patternId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **patternId** | **String**| The pattern ID. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patternDeletePatterns

> OperationStatus patternDeletePatterns(appId, versionId, patternIds)

Deletes a list of patterns in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let patternIds = ["null"]; // [String] | The patterns IDs.
apiInstance.patternDeletePatterns(appId, versionId, patternIds, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **patternIds** | [**[String]**](String.md)| The patterns IDs. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patternListIntentPatterns

> [PatternRuleInfo] patternListIntentPatterns(appId, versionId, intentId, opts)

Returns patterns for the specific intent in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let intentId = "intentId_example"; // String | The intent classifier ID.
let opts = {
  'skip': 0, // Number | The number of entries to skip. Default value is 0.
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.patternListIntentPatterns(appId, versionId, intentId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **intentId** | **String**| The intent classifier ID. | 
 **skip** | **Number**| The number of entries to skip. Default value is 0. | [optional] [default to 0]
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[PatternRuleInfo]**](PatternRuleInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patternListPatterns

> [PatternRuleInfo] patternListPatterns(appId, versionId, opts)

Gets patterns in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let opts = {
  'skip': 0, // Number | The number of entries to skip. Default value is 0.
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.patternListPatterns(appId, versionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **skip** | **Number**| The number of entries to skip. Default value is 0. | [optional] [default to 0]
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[PatternRuleInfo]**](PatternRuleInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patternUpdatePattern

> PatternRuleInfo patternUpdatePattern(appId, versionId, patternId, pattern)

Updates a pattern in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let patternId = "patternId_example"; // String | The pattern ID.
let pattern = new LuisAuthoringClient.PatternRuleUpdateObject(); // PatternRuleUpdateObject | An object representing a pattern.
apiInstance.patternUpdatePattern(appId, versionId, patternId, pattern, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **patternId** | **String**| The pattern ID. | 
 **pattern** | [**PatternRuleUpdateObject**](PatternRuleUpdateObject.md)| An object representing a pattern. | 

### Return type

[**PatternRuleInfo**](PatternRuleInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patternUpdatePatterns

> [PatternRuleInfo] patternUpdatePatterns(appId, versionId, patterns)

Updates patterns in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let patterns = [new LuisAuthoringClient.PatternRuleUpdateObject()]; // [PatternRuleUpdateObject] | An array represents the patterns.
apiInstance.patternUpdatePatterns(appId, versionId, patterns, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **patterns** | [**[PatternRuleUpdateObject]**](PatternRuleUpdateObject.md)| An array represents the patterns. | 

### Return type

[**[PatternRuleInfo]**](PatternRuleInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## permissionsAdd

> OperationStatus permissionsAdd(appId, userToAdd)



Adds a user to the allowed list of users to access this LUIS application. Users are added using their email address.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let userToAdd = new LuisAuthoringClient.UserCollaborator(); // UserCollaborator | A model containing the user's email address.
apiInstance.permissionsAdd(appId, userToAdd, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **userToAdd** | [**UserCollaborator**](UserCollaborator.md)| A model containing the user&#39;s email address. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## permissionsDelete

> OperationStatus permissionsDelete(appId, userToDelete)



Removes a user from the allowed list of users to access this LUIS application. Users are removed using their email address.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let userToDelete = new LuisAuthoringClient.UserCollaborator(); // UserCollaborator | A model containing the user's email address.
apiInstance.permissionsDelete(appId, userToDelete, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **userToDelete** | [**UserCollaborator**](UserCollaborator.md)| A model containing the user&#39;s email address. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## permissionsList

> UserAccessList permissionsList(appId)



Gets the list of user emails that have permissions to access your application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
apiInstance.permissionsList(appId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 

### Return type

[**UserAccessList**](UserAccessList.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## permissionsUpdate

> OperationStatus permissionsUpdate(appId, collaborators)



Replaces the current user access list with the new list sent in the body. If an empty list is sent, all access to other users will be removed.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let collaborators = new LuisAuthoringClient.CollaboratorsArray(); // CollaboratorsArray | A model containing a list of user email addresses.
apiInstance.permissionsUpdate(appId, collaborators, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **collaborators** | [**CollaboratorsArray**](CollaboratorsArray.md)| A model containing a list of user email addresses. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## settingsList

> [AppVersionSettingObject] settingsList(appId, versionId)



Gets the settings in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
apiInstance.settingsList(appId, versionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 

### Return type

[**[AppVersionSettingObject]**](AppVersionSettingObject.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## settingsUpdate

> OperationStatus settingsUpdate(appId, versionId, listOfAppVersionSettingObject)



Updates the settings in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let listOfAppVersionSettingObject = [new LuisAuthoringClient.AppVersionSettingObject()]; // [AppVersionSettingObject] | A list of the updated application version settings.
apiInstance.settingsUpdate(appId, versionId, listOfAppVersionSettingObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **listOfAppVersionSettingObject** | [**[AppVersionSettingObject]**](AppVersionSettingObject.md)| A list of the updated application version settings. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## trainGetStatus

> [ModelTrainingInfo] trainGetStatus(appId, versionId)



Gets the training status of all models (intents and entities) for the specified LUIS app. You must call the train API to train the LUIS app before you call this API to get training status. \&quot;appID\&quot; specifies the LUIS app ID. \&quot;versionId\&quot; specifies the version number of the LUIS app. For example, \&quot;0.1\&quot;.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
apiInstance.trainGetStatus(appId, versionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 

### Return type

[**[ModelTrainingInfo]**](ModelTrainingInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, JSON


## trainTrainVersion

> EnqueueTrainingResponse trainTrainVersion(appId, versionId)



Sends a training request for a version of a specified LUIS app. This POST request initiates a request asynchronously. To determine whether the training request is successful, submit a GET request to get training status. Note: The application version is not fully trained unless all the models (intents and entities) are trained successfully or are up to date. To verify training success, get the training status at least once after training is complete.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
apiInstance.trainTrainVersion(appId, versionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 

### Return type

[**EnqueueTrainingResponse**](EnqueueTrainingResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## versionsClone

> String versionsClone(appId, versionId, versionCloneObject)



Creates a new version from the selected version.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let versionCloneObject = new LuisAuthoringClient.TaskUpdateObject(); // TaskUpdateObject | A model containing the new version ID.
apiInstance.versionsClone(appId, versionId, versionCloneObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **versionCloneObject** | [**TaskUpdateObject**](TaskUpdateObject.md)| A model containing the new version ID. | 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## versionsDelete

> OperationStatus versionsDelete(appId, versionId)



Deletes an application version.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
apiInstance.versionsDelete(appId, versionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## versionsDeleteUnlabelledUtterance

> OperationStatus versionsDeleteUnlabelledUtterance(appId, versionId, utterance)



Deleted an unlabelled utterance in a version of the application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let utterance = "utterance_example"; // String | The utterance text to delete.
apiInstance.versionsDeleteUnlabelledUtterance(appId, versionId, utterance, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **utterance** | **String**| The utterance text to delete. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## versionsExport

> LuisApp versionsExport(appId, versionId)



Exports a LUIS application to JSON format.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
apiInstance.versionsExport(appId, versionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 

### Return type

[**LuisApp**](LuisApp.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## versionsGet

> VersionInfo versionsGet(appId, versionId)



Gets the version information such as date created, last modified date, endpoint URL, count of intents and entities, training and publishing status.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
apiInstance.versionsGet(appId, versionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 

### Return type

[**VersionInfo**](VersionInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## versionsImport

> String versionsImport(appId, luisApp, opts)



Imports a new version into a LUIS application.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let luisApp = new LuisAuthoringClient.LuisApp(); // LuisApp | A LUIS application structure.
let opts = {
  'versionId': "versionId_example" // String | The new versionId to import. If not specified, the versionId will be read from the imported object.
};
apiInstance.versionsImport(appId, luisApp, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **luisApp** | [**LuisApp**](LuisApp.md)| A LUIS application structure. | 
 **versionId** | **String**| The new versionId to import. If not specified, the versionId will be read from the imported object. | [optional] 

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## versionsList

> [VersionInfo] versionsList(appId, opts)



Gets a list of versions for this application ID.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let opts = {
  'skip': 0, // Number | The number of entries to skip. Default value is 0.
  'take': 100 // Number | The number of entries to return. Maximum page size is 500. Default is 100.
};
apiInstance.versionsList(appId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **skip** | **Number**| The number of entries to skip. Default value is 0. | [optional] [default to 0]
 **take** | **Number**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100]

### Return type

[**[VersionInfo]**](VersionInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## versionsUpdate

> OperationStatus versionsUpdate(appId, versionId, versionUpdateObject)



Updates the name or description of the application version.

### Example

```javascript
import LuisAuthoringClient from 'luis_authoring_client';
let defaultClient = LuisAuthoringClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new LuisAuthoringClient.DefaultApi();
let appId = "appId_example"; // String | The application ID.
let versionId = "versionId_example"; // String | The version ID.
let versionUpdateObject = new LuisAuthoringClient.TaskUpdateObject(); // TaskUpdateObject | A model containing Name and Description of the application.
apiInstance.versionsUpdate(appId, versionId, versionUpdateObject, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appId** | **String**| The application ID. | 
 **versionId** | **String**| The version ID. | 
 **versionUpdateObject** | [**TaskUpdateObject**](TaskUpdateObject.md)| A model containing Name and Description of the application. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

