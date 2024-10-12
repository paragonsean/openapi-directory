# DefaultApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appsAdd**](DefaultApi.md#appsAdd) | **POST** /apps/ |  |
| [**appsAddCustomPrebuiltDomain**](DefaultApi.md#appsAddCustomPrebuiltDomain) | **POST** /apps/customprebuiltdomains |  |
| [**appsDelete**](DefaultApi.md#appsDelete) | **DELETE** /apps/{appId} |  |
| [**appsDownloadQueryLogs**](DefaultApi.md#appsDownloadQueryLogs) | **GET** /apps/{appId}/querylogs |  |
| [**appsGet**](DefaultApi.md#appsGet) | **GET** /apps/{appId} |  |
| [**appsGetPublishSettings**](DefaultApi.md#appsGetPublishSettings) | **GET** /apps/{appId}/publishsettings |  |
| [**appsGetSettings**](DefaultApi.md#appsGetSettings) | **GET** /apps/{appId}/settings |  |
| [**appsImport**](DefaultApi.md#appsImport) | **POST** /apps/import |  |
| [**appsList**](DefaultApi.md#appsList) | **GET** /apps/ |  |
| [**appsListAvailableCustomPrebuiltDomains**](DefaultApi.md#appsListAvailableCustomPrebuiltDomains) | **GET** /apps/customprebuiltdomains |  |
| [**appsListAvailableCustomPrebuiltDomainsForCulture**](DefaultApi.md#appsListAvailableCustomPrebuiltDomainsForCulture) | **GET** /apps/customprebuiltdomains/{culture} |  |
| [**appsListCortanaEndpoints**](DefaultApi.md#appsListCortanaEndpoints) | **GET** /apps/assistants |  |
| [**appsListDomains**](DefaultApi.md#appsListDomains) | **GET** /apps/domains |  |
| [**appsListEndpoints**](DefaultApi.md#appsListEndpoints) | **GET** /apps/{appId}/endpoints |  |
| [**appsListSupportedCultures**](DefaultApi.md#appsListSupportedCultures) | **GET** /apps/cultures |  |
| [**appsListUsageScenarios**](DefaultApi.md#appsListUsageScenarios) | **GET** /apps/usagescenarios |  |
| [**appsPackagePublishedApplicationAsGzip**](DefaultApi.md#appsPackagePublishedApplicationAsGzip) | **GET** /package/{appId}/slot/{slotName}/gzip | package - Gets published LUIS application package in binary stream GZip format |
| [**appsPackageTrainedApplicationAsGzip**](DefaultApi.md#appsPackageTrainedApplicationAsGzip) | **GET** /package/{appId}/versions/{versionId}/gzip | package - Gets trained LUIS application package in binary stream GZip format |
| [**appsPublish**](DefaultApi.md#appsPublish) | **POST** /apps/{appId}/publish |  |
| [**appsUpdate**](DefaultApi.md#appsUpdate) | **PUT** /apps/{appId} |  |
| [**appsUpdatePublishSettings**](DefaultApi.md#appsUpdatePublishSettings) | **PUT** /apps/{appId}/publishsettings |  |
| [**appsUpdateSettings**](DefaultApi.md#appsUpdateSettings) | **PUT** /apps/{appId}/settings |  |
| [**azureAccountsAssignToApp**](DefaultApi.md#azureAccountsAssignToApp) | **POST** /apps/{appId}/azureaccounts | apps - Assign a LUIS Azure account to an application |
| [**azureAccountsGetAssigned**](DefaultApi.md#azureAccountsGetAssigned) | **GET** /apps/{appId}/azureaccounts | apps - Get LUIS Azure accounts assigned to the application |
| [**azureAccountsListUserLUISAccounts**](DefaultApi.md#azureAccountsListUserLUISAccounts) | **GET** /azureaccounts | user - Get LUIS Azure accounts |
| [**azureAccountsRemoveFromApp**](DefaultApi.md#azureAccountsRemoveFromApp) | **DELETE** /apps/{appId}/azureaccounts | apps - Removes an assigned LUIS Azure account from an application |
| [**examplesAdd**](DefaultApi.md#examplesAdd) | **POST** /apps/{appId}/versions/{versionId}/example |  |
| [**examplesBatch**](DefaultApi.md#examplesBatch) | **POST** /apps/{appId}/versions/{versionId}/examples |  |
| [**examplesDelete**](DefaultApi.md#examplesDelete) | **DELETE** /apps/{appId}/versions/{versionId}/examples/{exampleId} |  |
| [**examplesList**](DefaultApi.md#examplesList) | **GET** /apps/{appId}/versions/{versionId}/examples |  |
| [**featuresAddPhraseList**](DefaultApi.md#featuresAddPhraseList) | **POST** /apps/{appId}/versions/{versionId}/phraselists |  |
| [**featuresCreatePatternFeature**](DefaultApi.md#featuresCreatePatternFeature) | **POST** /apps/{appId}/versions/{versionId}/patterns |  |
| [**featuresDeletePatternFeature**](DefaultApi.md#featuresDeletePatternFeature) | **DELETE** /apps/{appId}/versions/{versionId}/patterns/{patternId} |  |
| [**featuresDeletePhraseList**](DefaultApi.md#featuresDeletePhraseList) | **DELETE** /apps/{appId}/versions/{versionId}/phraselists/{phraselistId} |  |
| [**featuresGetPatternFeatureInfo**](DefaultApi.md#featuresGetPatternFeatureInfo) | **GET** /apps/{appId}/versions/{versionId}/patterns/{patternId} |  |
| [**featuresGetPhraseList**](DefaultApi.md#featuresGetPhraseList) | **GET** /apps/{appId}/versions/{versionId}/phraselists/{phraselistId} |  |
| [**featuresList**](DefaultApi.md#featuresList) | **GET** /apps/{appId}/versions/{versionId}/features |  |
| [**featuresListApplicationVersionPatternFeatures**](DefaultApi.md#featuresListApplicationVersionPatternFeatures) | **GET** /apps/{appId}/versions/{versionId}/patterns |  |
| [**featuresListPhraseLists**](DefaultApi.md#featuresListPhraseLists) | **GET** /apps/{appId}/versions/{versionId}/phraselists |  |
| [**featuresUpdatePatternFeature**](DefaultApi.md#featuresUpdatePatternFeature) | **PUT** /apps/{appId}/versions/{versionId}/patterns/{patternId} |  |
| [**featuresUpdatePhraseList**](DefaultApi.md#featuresUpdatePhraseList) | **PUT** /apps/{appId}/versions/{versionId}/phraselists/{phraselistId} |  |
| [**modelAddClosedList**](DefaultApi.md#modelAddClosedList) | **POST** /apps/{appId}/versions/{versionId}/closedlists |  |
| [**modelAddCompositeEntity**](DefaultApi.md#modelAddCompositeEntity) | **POST** /apps/{appId}/versions/{versionId}/compositeentities |  |
| [**modelAddCompositeEntityChild**](DefaultApi.md#modelAddCompositeEntityChild) | **POST** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId}/children |  |
| [**modelAddCustomPrebuiltDomain**](DefaultApi.md#modelAddCustomPrebuiltDomain) | **POST** /apps/{appId}/versions/{versionId}/customprebuiltdomains |  |
| [**modelAddCustomPrebuiltEntity**](DefaultApi.md#modelAddCustomPrebuiltEntity) | **POST** /apps/{appId}/versions/{versionId}/customprebuiltentities |  |
| [**modelAddCustomPrebuiltIntent**](DefaultApi.md#modelAddCustomPrebuiltIntent) | **POST** /apps/{appId}/versions/{versionId}/customprebuiltintents |  |
| [**modelAddEntity**](DefaultApi.md#modelAddEntity) | **POST** /apps/{appId}/versions/{versionId}/entities |  |
| [**modelAddExplicitListItem**](DefaultApi.md#modelAddExplicitListItem) | **POST** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/explicitlist | Add a new exception to the explicit list for the Pattern.Any entity in a version of the application. |
| [**modelAddHierarchicalEntity**](DefaultApi.md#modelAddHierarchicalEntity) | **POST** /apps/{appId}/versions/{versionId}/hierarchicalentities |  |
| [**modelAddHierarchicalEntityChild**](DefaultApi.md#modelAddHierarchicalEntityChild) | **POST** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId}/children |  |
| [**modelAddIntent**](DefaultApi.md#modelAddIntent) | **POST** /apps/{appId}/versions/{versionId}/intents |  |
| [**modelAddPrebuilt**](DefaultApi.md#modelAddPrebuilt) | **POST** /apps/{appId}/versions/{versionId}/prebuilts |  |
| [**modelAddSubList**](DefaultApi.md#modelAddSubList) | **POST** /apps/{appId}/versions/{versionId}/closedlists/{clEntityId}/sublists |  |
| [**modelCreateClosedListEntityRole**](DefaultApi.md#modelCreateClosedListEntityRole) | **POST** /apps/{appId}/versions/{versionId}/closedlists/{entityId}/roles | Create a role for a list entity in a version of the application. |
| [**modelCreateCompositeEntityRole**](DefaultApi.md#modelCreateCompositeEntityRole) | **POST** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId}/roles | Create a role for a composite entity in a version of the application. |
| [**modelCreateCustomPrebuiltEntityRole**](DefaultApi.md#modelCreateCustomPrebuiltEntityRole) | **POST** /apps/{appId}/versions/{versionId}/customprebuiltentities/{entityId}/roles | Create a role for a prebuilt entity in a version of the application. |
| [**modelCreateEntityRole**](DefaultApi.md#modelCreateEntityRole) | **POST** /apps/{appId}/versions/{versionId}/entities/{entityId}/roles | Create an entity role in a version of the application. |
| [**modelCreateHierarchicalEntityRole**](DefaultApi.md#modelCreateHierarchicalEntityRole) | **POST** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId}/roles | Create a role for an hierarchical entity in a version of the application. |
| [**modelCreatePatternAnyEntityModel**](DefaultApi.md#modelCreatePatternAnyEntityModel) | **POST** /apps/{appId}/versions/{versionId}/patternanyentities | Adds a pattern.any entity extractor to a version of the application. |
| [**modelCreatePatternAnyEntityRole**](DefaultApi.md#modelCreatePatternAnyEntityRole) | **POST** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/roles | Create a role for an Pattern.any entity in a version of the application. |
| [**modelCreatePrebuiltEntityRole**](DefaultApi.md#modelCreatePrebuiltEntityRole) | **POST** /apps/{appId}/versions/{versionId}/prebuilts/{entityId}/roles | Create a role for a prebuilt entity in a version of the application. |
| [**modelCreateRegexEntityModel**](DefaultApi.md#modelCreateRegexEntityModel) | **POST** /apps/{appId}/versions/{versionId}/regexentities | Adds a regular expression entity model to a version of the application. |
| [**modelCreateRegexEntityRole**](DefaultApi.md#modelCreateRegexEntityRole) | **POST** /apps/{appId}/versions/{versionId}/regexentities/{entityId}/roles | Create a role for an regular expression entity in a version of the application. |
| [**modelDeleteClosedList**](DefaultApi.md#modelDeleteClosedList) | **DELETE** /apps/{appId}/versions/{versionId}/closedlists/{clEntityId} |  |
| [**modelDeleteClosedListEntityRole**](DefaultApi.md#modelDeleteClosedListEntityRole) | **DELETE** /apps/{appId}/versions/{versionId}/closedlists/{entityId}/roles/{roleId} | Delete a role for a given list entity in a version of the application. |
| [**modelDeleteCompositeEntity**](DefaultApi.md#modelDeleteCompositeEntity) | **DELETE** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId} |  |
| [**modelDeleteCompositeEntityChild**](DefaultApi.md#modelDeleteCompositeEntityChild) | **DELETE** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId}/children/{cChildId} |  |
| [**modelDeleteCompositeEntityRole**](DefaultApi.md#modelDeleteCompositeEntityRole) | **DELETE** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId}/roles/{roleId} | Delete a role for a given composite entity in a version of the application. |
| [**modelDeleteCustomEntityRole**](DefaultApi.md#modelDeleteCustomEntityRole) | **DELETE** /apps/{appId}/versions/{versionId}/customprebuiltentities/{entityId}/roles/{roleId} | Delete a role for a given prebuilt entity in a version of the application. |
| [**modelDeleteCustomPrebuiltDomain**](DefaultApi.md#modelDeleteCustomPrebuiltDomain) | **DELETE** /apps/{appId}/versions/{versionId}/customprebuiltdomains/{domainName} |  |
| [**modelDeleteEntity**](DefaultApi.md#modelDeleteEntity) | **DELETE** /apps/{appId}/versions/{versionId}/entities/{entityId} |  |
| [**modelDeleteEntityRole**](DefaultApi.md#modelDeleteEntityRole) | **DELETE** /apps/{appId}/versions/{versionId}/entities/{entityId}/roles/{roleId} | Delete an entity role in a version of the application. |
| [**modelDeleteExplicitListItem**](DefaultApi.md#modelDeleteExplicitListItem) | **DELETE** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/explicitlist/{itemId} | Delete an item from the explicit (exception) list for a Pattern.any entity in a version of the application. |
| [**modelDeleteHierarchicalEntity**](DefaultApi.md#modelDeleteHierarchicalEntity) | **DELETE** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId} |  |
| [**modelDeleteHierarchicalEntityChild**](DefaultApi.md#modelDeleteHierarchicalEntityChild) | **DELETE** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId}/children/{hChildId} |  |
| [**modelDeleteHierarchicalEntityRole**](DefaultApi.md#modelDeleteHierarchicalEntityRole) | **DELETE** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId}/roles/{roleId} | Delete a role for a given hierarchical role in a version of the application. |
| [**modelDeleteIntent**](DefaultApi.md#modelDeleteIntent) | **DELETE** /apps/{appId}/versions/{versionId}/intents/{intentId} |  |
| [**modelDeletePatternAnyEntityModel**](DefaultApi.md#modelDeletePatternAnyEntityModel) | **DELETE** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId} | Deletes a Pattern.Any entity extractor from a version of the application. |
| [**modelDeletePatternAnyEntityRole**](DefaultApi.md#modelDeletePatternAnyEntityRole) | **DELETE** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/roles/{roleId} | Delete a role for a given Pattern.any entity in a version of the application. |
| [**modelDeletePrebuilt**](DefaultApi.md#modelDeletePrebuilt) | **DELETE** /apps/{appId}/versions/{versionId}/prebuilts/{prebuiltId} |  |
| [**modelDeletePrebuiltEntityRole**](DefaultApi.md#modelDeletePrebuiltEntityRole) | **DELETE** /apps/{appId}/versions/{versionId}/prebuilts/{entityId}/roles/{roleId} | Delete a role in a prebuilt entity in a version of the application. |
| [**modelDeleteRegexEntityModel**](DefaultApi.md#modelDeleteRegexEntityModel) | **DELETE** /apps/{appId}/versions/{versionId}/regexentities/{regexEntityId} | Deletes a regular expression entity from a version of the application. |
| [**modelDeleteRegexEntityRole**](DefaultApi.md#modelDeleteRegexEntityRole) | **DELETE** /apps/{appId}/versions/{versionId}/regexentities/{entityId}/roles/{roleId} | Delete a role for a given regular expression in a version of the application. |
| [**modelDeleteSubList**](DefaultApi.md#modelDeleteSubList) | **DELETE** /apps/{appId}/versions/{versionId}/closedlists/{clEntityId}/sublists/{subListId} |  |
| [**modelExamples**](DefaultApi.md#modelExamples) | **GET** /apps/{appId}/versions/{versionId}/models/{modelId}/examples |  |
| [**modelGetClosedList**](DefaultApi.md#modelGetClosedList) | **GET** /apps/{appId}/versions/{versionId}/closedlists/{clEntityId} |  |
| [**modelGetClosedListEntityRole**](DefaultApi.md#modelGetClosedListEntityRole) | **GET** /apps/{appId}/versions/{versionId}/closedlists/{entityId}/roles/{roleId} | Get one role for a given list entity in a version of the application. |
| [**modelGetCompositeEntity**](DefaultApi.md#modelGetCompositeEntity) | **GET** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId} |  |
| [**modelGetCompositeEntityRole**](DefaultApi.md#modelGetCompositeEntityRole) | **GET** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId}/roles/{roleId} | Get one role for a given composite entity in a version of the application |
| [**modelGetCustomEntityRole**](DefaultApi.md#modelGetCustomEntityRole) | **GET** /apps/{appId}/versions/{versionId}/customprebuiltentities/{entityId}/roles/{roleId} | Get one role for a given prebuilt entity in a version of the application. |
| [**modelGetEntity**](DefaultApi.md#modelGetEntity) | **GET** /apps/{appId}/versions/{versionId}/entities/{entityId} |  |
| [**modelGetEntityRole**](DefaultApi.md#modelGetEntityRole) | **GET** /apps/{appId}/versions/{versionId}/entities/{entityId}/roles/{roleId} | Get one role for a given entity in a version of the application |
| [**modelGetExplicitList**](DefaultApi.md#modelGetExplicitList) | **GET** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/explicitlist | Get the explicit (exception) list of the pattern.any entity in a version of the application. |
| [**modelGetExplicitListItem**](DefaultApi.md#modelGetExplicitListItem) | **GET** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/explicitlist/{itemId} | Get the explicit (exception) list of the pattern.any entity in a version of the application. |
| [**modelGetHierarchicalEntity**](DefaultApi.md#modelGetHierarchicalEntity) | **GET** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId} |  |
| [**modelGetHierarchicalEntityChild**](DefaultApi.md#modelGetHierarchicalEntityChild) | **GET** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId}/children/{hChildId} |  |
| [**modelGetHierarchicalEntityRole**](DefaultApi.md#modelGetHierarchicalEntityRole) | **GET** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId}/roles/{roleId} | Get one role for a given hierarchical entity in a version of the application. |
| [**modelGetIntent**](DefaultApi.md#modelGetIntent) | **GET** /apps/{appId}/versions/{versionId}/intents/{intentId} |  |
| [**modelGetPatternAnyEntityInfo**](DefaultApi.md#modelGetPatternAnyEntityInfo) | **GET** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId} | Gets information about the Pattern.Any model in a version of the application. |
| [**modelGetPatternAnyEntityRole**](DefaultApi.md#modelGetPatternAnyEntityRole) | **GET** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/roles/{roleId} | Get one role for a given Pattern.any entity in a version of the application. |
| [**modelGetPrebuilt**](DefaultApi.md#modelGetPrebuilt) | **GET** /apps/{appId}/versions/{versionId}/prebuilts/{prebuiltId} |  |
| [**modelGetPrebuiltEntityRole**](DefaultApi.md#modelGetPrebuiltEntityRole) | **GET** /apps/{appId}/versions/{versionId}/prebuilts/{entityId}/roles/{roleId} | Get one role for a given prebuilt entity in a version of the application |
| [**modelGetRegexEntityEntityInfo**](DefaultApi.md#modelGetRegexEntityEntityInfo) | **GET** /apps/{appId}/versions/{versionId}/regexentities/{regexEntityId} | Gets information about a regular expression entity in a version of the application. |
| [**modelGetRegexEntityRole**](DefaultApi.md#modelGetRegexEntityRole) | **GET** /apps/{appId}/versions/{versionId}/regexentities/{entityId}/roles/{roleId} | Get one role for a given regular expression entity in a version of the application. |
| [**modelListClosedListEntityRoles**](DefaultApi.md#modelListClosedListEntityRoles) | **GET** /apps/{appId}/versions/{versionId}/closedlists/{entityId}/roles | Get all roles for a list entity in a version of the application. |
| [**modelListClosedLists**](DefaultApi.md#modelListClosedLists) | **GET** /apps/{appId}/versions/{versionId}/closedlists |  |
| [**modelListCompositeEntities**](DefaultApi.md#modelListCompositeEntities) | **GET** /apps/{appId}/versions/{versionId}/compositeentities |  |
| [**modelListCompositeEntityRoles**](DefaultApi.md#modelListCompositeEntityRoles) | **GET** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId}/roles | Get all roles for a composite entity in a version of the application |
| [**modelListCustomPrebuiltEntities**](DefaultApi.md#modelListCustomPrebuiltEntities) | **GET** /apps/{appId}/versions/{versionId}/customprebuiltentities |  |
| [**modelListCustomPrebuiltEntityRoles**](DefaultApi.md#modelListCustomPrebuiltEntityRoles) | **GET** /apps/{appId}/versions/{versionId}/customprebuiltentities/{entityId}/roles | Get all roles for a prebuilt entity in a version of the application |
| [**modelListCustomPrebuiltIntents**](DefaultApi.md#modelListCustomPrebuiltIntents) | **GET** /apps/{appId}/versions/{versionId}/customprebuiltintents |  |
| [**modelListCustomPrebuiltModels**](DefaultApi.md#modelListCustomPrebuiltModels) | **GET** /apps/{appId}/versions/{versionId}/customprebuiltmodels |  |
| [**modelListEntities**](DefaultApi.md#modelListEntities) | **GET** /apps/{appId}/versions/{versionId}/entities |  |
| [**modelListEntityRoles**](DefaultApi.md#modelListEntityRoles) | **GET** /apps/{appId}/versions/{versionId}/entities/{entityId}/roles | Get all roles for an entity in a version of the application |
| [**modelListEntitySuggestions**](DefaultApi.md#modelListEntitySuggestions) | **GET** /apps/{appId}/versions/{versionId}/entities/{entityId}/suggest |  |
| [**modelListHierarchicalEntities**](DefaultApi.md#modelListHierarchicalEntities) | **GET** /apps/{appId}/versions/{versionId}/hierarchicalentities |  |
| [**modelListHierarchicalEntityRoles**](DefaultApi.md#modelListHierarchicalEntityRoles) | **GET** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId}/roles | Get all roles for a hierarchical entity in a version of the application |
| [**modelListIntentSuggestions**](DefaultApi.md#modelListIntentSuggestions) | **GET** /apps/{appId}/versions/{versionId}/intents/{intentId}/suggest |  |
| [**modelListIntents**](DefaultApi.md#modelListIntents) | **GET** /apps/{appId}/versions/{versionId}/intents |  |
| [**modelListModels**](DefaultApi.md#modelListModels) | **GET** /apps/{appId}/versions/{versionId}/models |  |
| [**modelListPatternAnyEntityInfos**](DefaultApi.md#modelListPatternAnyEntityInfos) | **GET** /apps/{appId}/versions/{versionId}/patternanyentities | Get information about the Pattern.Any entity models in a version of the application. |
| [**modelListPatternAnyEntityRoles**](DefaultApi.md#modelListPatternAnyEntityRoles) | **GET** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/roles | Get all roles for a Pattern.any entity in a version of the application |
| [**modelListPrebuiltEntities**](DefaultApi.md#modelListPrebuiltEntities) | **GET** /apps/{appId}/versions/{versionId}/listprebuilts |  |
| [**modelListPrebuiltEntityRoles**](DefaultApi.md#modelListPrebuiltEntityRoles) | **GET** /apps/{appId}/versions/{versionId}/prebuilts/{entityId}/roles | Get a prebuilt entity&#39;s roles in a version of the application. |
| [**modelListPrebuilts**](DefaultApi.md#modelListPrebuilts) | **GET** /apps/{appId}/versions/{versionId}/prebuilts |  |
| [**modelListRegexEntityInfos**](DefaultApi.md#modelListRegexEntityInfos) | **GET** /apps/{appId}/versions/{versionId}/regexentities | Gets information about the regular expression entity models in a version of the application. |
| [**modelListRegexEntityRoles**](DefaultApi.md#modelListRegexEntityRoles) | **GET** /apps/{appId}/versions/{versionId}/regexentities/{entityId}/roles | Get all roles for a regular expression entity in a version of the application. |
| [**modelPatchClosedList**](DefaultApi.md#modelPatchClosedList) | **PATCH** /apps/{appId}/versions/{versionId}/closedlists/{clEntityId} |  |
| [**modelUpdateClosedList**](DefaultApi.md#modelUpdateClosedList) | **PUT** /apps/{appId}/versions/{versionId}/closedlists/{clEntityId} |  |
| [**modelUpdateClosedListEntityRole**](DefaultApi.md#modelUpdateClosedListEntityRole) | **PUT** /apps/{appId}/versions/{versionId}/closedlists/{entityId}/roles/{roleId} | Update a role for a given list entity in a version of the application. |
| [**modelUpdateCompositeEntity**](DefaultApi.md#modelUpdateCompositeEntity) | **PUT** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId} |  |
| [**modelUpdateCompositeEntityRole**](DefaultApi.md#modelUpdateCompositeEntityRole) | **PUT** /apps/{appId}/versions/{versionId}/compositeentities/{cEntityId}/roles/{roleId} | Update a role for a given composite entity in a version of the application |
| [**modelUpdateCustomPrebuiltEntityRole**](DefaultApi.md#modelUpdateCustomPrebuiltEntityRole) | **PUT** /apps/{appId}/versions/{versionId}/customprebuiltentities/{entityId}/roles/{roleId} | Update a role for a given prebuilt entity in a version of the application. |
| [**modelUpdateEntity**](DefaultApi.md#modelUpdateEntity) | **PUT** /apps/{appId}/versions/{versionId}/entities/{entityId} |  |
| [**modelUpdateEntityRole**](DefaultApi.md#modelUpdateEntityRole) | **PUT** /apps/{appId}/versions/{versionId}/entities/{entityId}/roles/{roleId} | Update a role for a given entity in a version of the application. |
| [**modelUpdateExplicitListItem**](DefaultApi.md#modelUpdateExplicitListItem) | **PUT** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/explicitlist/{itemId} | Updates an explicit (exception) list item for a Pattern.Any entity in a version of the application. |
| [**modelUpdateHierarchicalEntity**](DefaultApi.md#modelUpdateHierarchicalEntity) | **PUT** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId} |  |
| [**modelUpdateHierarchicalEntityChild**](DefaultApi.md#modelUpdateHierarchicalEntityChild) | **PUT** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId}/children/{hChildId} |  |
| [**modelUpdateHierarchicalEntityRole**](DefaultApi.md#modelUpdateHierarchicalEntityRole) | **PUT** /apps/{appId}/versions/{versionId}/hierarchicalentities/{hEntityId}/roles/{roleId} | Update a role for a given hierarchical entity in a version of the application. |
| [**modelUpdateIntent**](DefaultApi.md#modelUpdateIntent) | **PUT** /apps/{appId}/versions/{versionId}/intents/{intentId} |  |
| [**modelUpdatePatternAnyEntityModel**](DefaultApi.md#modelUpdatePatternAnyEntityModel) | **PUT** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId} | Updates the name and explicit (exception) list of a Pattern.Any entity model in a version of the application. |
| [**modelUpdatePatternAnyEntityRole**](DefaultApi.md#modelUpdatePatternAnyEntityRole) | **PUT** /apps/{appId}/versions/{versionId}/patternanyentities/{entityId}/roles/{roleId} | Update a role for a given Pattern.any entity in a version of the application. |
| [**modelUpdatePrebuiltEntityRole**](DefaultApi.md#modelUpdatePrebuiltEntityRole) | **PUT** /apps/{appId}/versions/{versionId}/prebuilts/{entityId}/roles/{roleId} | Update a role for a given prebuilt entity in a version of the application |
| [**modelUpdateRegexEntityModel**](DefaultApi.md#modelUpdateRegexEntityModel) | **PUT** /apps/{appId}/versions/{versionId}/regexentities/{regexEntityId} | Updates the regular expression entity in a version of the application. |
| [**modelUpdateRegexEntityRole**](DefaultApi.md#modelUpdateRegexEntityRole) | **PUT** /apps/{appId}/versions/{versionId}/regexentities/{entityId}/roles/{roleId} | Update a role for a given regular expression entity in a version of the application |
| [**modelUpdateSubList**](DefaultApi.md#modelUpdateSubList) | **PUT** /apps/{appId}/versions/{versionId}/closedlists/{clEntityId}/sublists/{subListId} |  |
| [**patternAddPattern**](DefaultApi.md#patternAddPattern) | **POST** /apps/{appId}/versions/{versionId}/patternrule | Adds a pattern to a version of the application. |
| [**patternBatchAddPatterns**](DefaultApi.md#patternBatchAddPatterns) | **POST** /apps/{appId}/versions/{versionId}/patternrules | Adds a batch of patterns in a version of the application. |
| [**patternDeletePattern**](DefaultApi.md#patternDeletePattern) | **DELETE** /apps/{appId}/versions/{versionId}/patternrules/{patternId} | Deletes the pattern with the specified ID from a version of the application.. |
| [**patternDeletePatterns**](DefaultApi.md#patternDeletePatterns) | **DELETE** /apps/{appId}/versions/{versionId}/patternrules | Deletes a list of patterns in a version of the application. |
| [**patternListIntentPatterns**](DefaultApi.md#patternListIntentPatterns) | **GET** /apps/{appId}/versions/{versionId}/intents/{intentId}/patternrules | Returns patterns for the specific intent in a version of the application. |
| [**patternListPatterns**](DefaultApi.md#patternListPatterns) | **GET** /apps/{appId}/versions/{versionId}/patternrules | Gets patterns in a version of the application. |
| [**patternUpdatePattern**](DefaultApi.md#patternUpdatePattern) | **PUT** /apps/{appId}/versions/{versionId}/patternrules/{patternId} | Updates a pattern in a version of the application. |
| [**patternUpdatePatterns**](DefaultApi.md#patternUpdatePatterns) | **PUT** /apps/{appId}/versions/{versionId}/patternrules | Updates patterns in a version of the application. |
| [**permissionsAdd**](DefaultApi.md#permissionsAdd) | **POST** /apps/{appId}/permissions |  |
| [**permissionsDelete**](DefaultApi.md#permissionsDelete) | **DELETE** /apps/{appId}/permissions |  |
| [**permissionsList**](DefaultApi.md#permissionsList) | **GET** /apps/{appId}/permissions |  |
| [**permissionsUpdate**](DefaultApi.md#permissionsUpdate) | **PUT** /apps/{appId}/permissions |  |
| [**settingsList**](DefaultApi.md#settingsList) | **GET** /apps/{appId}/versions/{versionId}/settings |  |
| [**settingsUpdate**](DefaultApi.md#settingsUpdate) | **PUT** /apps/{appId}/versions/{versionId}/settings |  |
| [**trainGetStatus**](DefaultApi.md#trainGetStatus) | **GET** /apps/{appId}/versions/{versionId}/train |  |
| [**trainTrainVersion**](DefaultApi.md#trainTrainVersion) | **POST** /apps/{appId}/versions/{versionId}/train |  |
| [**versionsClone**](DefaultApi.md#versionsClone) | **POST** /apps/{appId}/versions/{versionId}/clone |  |
| [**versionsDelete**](DefaultApi.md#versionsDelete) | **DELETE** /apps/{appId}/versions/{versionId}/ |  |
| [**versionsDeleteUnlabelledUtterance**](DefaultApi.md#versionsDeleteUnlabelledUtterance) | **DELETE** /apps/{appId}/versions/{versionId}/suggest |  |
| [**versionsExport**](DefaultApi.md#versionsExport) | **GET** /apps/{appId}/versions/{versionId}/export |  |
| [**versionsGet**](DefaultApi.md#versionsGet) | **GET** /apps/{appId}/versions/{versionId}/ |  |
| [**versionsImport**](DefaultApi.md#versionsImport) | **POST** /apps/{appId}/versions/import |  |
| [**versionsList**](DefaultApi.md#versionsList) | **GET** /apps/{appId}/versions |  |
| [**versionsUpdate**](DefaultApi.md#versionsUpdate) | **PUT** /apps/{appId}/versions/{versionId}/ |  |


<a id="appsAdd"></a>
# **appsAdd**
> UUID appsAdd(applicationCreateObject)



Creates a new LUIS app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ApplicationCreateObject applicationCreateObject = new ApplicationCreateObject(); // ApplicationCreateObject | An application containing Name, Description (optional), Culture, Usage Scenario (optional), Domain (optional) and initial version ID (optional) of the application. Default value for the version ID is \"0.1\". Note: the culture cannot be changed after the app is created.
    try {
      UUID result = apiInstance.appsAdd(applicationCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsAdd");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **applicationCreateObject** | [**ApplicationCreateObject**](ApplicationCreateObject.md)| An application containing Name, Description (optional), Culture, Usage Scenario (optional), Domain (optional) and initial version ID (optional) of the application. Default value for the version ID is \&quot;0.1\&quot;. Note: the culture cannot be changed after the app is created. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created application. |  -  |
| **0** | Error Response. |  -  |

<a id="appsAddCustomPrebuiltDomain"></a>
# **appsAddCustomPrebuiltDomain**
> UUID appsAddCustomPrebuiltDomain(prebuiltDomainCreateObject)



Adds a prebuilt domain along with its intent and entity models as a new application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    PrebuiltDomainCreateObject prebuiltDomainCreateObject = new PrebuiltDomainCreateObject(); // PrebuiltDomainCreateObject | A prebuilt domain create object containing the name and culture of the domain.
    try {
      UUID result = apiInstance.appsAddCustomPrebuiltDomain(prebuiltDomainCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsAddCustomPrebuiltDomain");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **prebuiltDomainCreateObject** | [**PrebuiltDomainCreateObject**](PrebuiltDomainCreateObject.md)| A prebuilt domain create object containing the name and culture of the domain. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created application. |  -  |
| **0** | Error Response. |  -  |

<a id="appsDelete"></a>
# **appsDelete**
> OperationStatus appsDelete(appId, force)



Deletes an application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    Boolean force = false; // Boolean | A flag to indicate whether to force an operation.
    try {
      OperationStatus result = apiInstance.appsDelete(appId, force);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **force** | **Boolean**| A flag to indicate whether to force an operation. | [optional] [default to false] |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted application. |  -  |
| **0** | Error Response. |  -  |

<a id="appsDownloadQueryLogs"></a>
# **appsDownloadQueryLogs**
> Object appsDownloadQueryLogs(appId)



Gets the logs of the past month&#39;s endpoint queries for the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    try {
      Object result = apiInstance.appsDownloadQueryLogs(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsDownloadQueryLogs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |

### Return type

**Object**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A CSV file containing the query logs for the past month. |  -  |
| **0** | Error Response. |  -  |

<a id="appsGet"></a>
# **appsGet**
> ApplicationInfoResponse appsGet(appId)



Gets the application info.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    try {
      ApplicationInfoResponse result = apiInstance.appsGet(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |

### Return type

[**ApplicationInfoResponse**](ApplicationInfoResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The application info. |  -  |
| **0** | Error Response. |  -  |

<a id="appsGetPublishSettings"></a>
# **appsGetPublishSettings**
> PublishSettings appsGetPublishSettings(appId)



Get the application publish settings including &#39;UseAllTrainingData&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    try {
      PublishSettings result = apiInstance.appsGetPublishSettings(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsGetPublishSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |

### Return type

[**PublishSettings**](PublishSettings.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The application publish settings. |  -  |
| **0** | Error Response. |  -  |

<a id="appsGetSettings"></a>
# **appsGetSettings**
> ApplicationSettings appsGetSettings(appId)



Get the application settings including &#39;UseAllTrainingData&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    try {
      ApplicationSettings result = apiInstance.appsGetSettings(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsGetSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |

### Return type

[**ApplicationSettings**](ApplicationSettings.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The application settings. |  -  |
| **0** | Error Response. |  -  |

<a id="appsImport"></a>
# **appsImport**
> UUID appsImport(luisApp, appName)



Imports an application to LUIS, the application&#39;s structure is included in the request body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    LuisApp luisApp = new LuisApp(); // LuisApp | A LUIS application structure.
    String appName = "appName_example"; // String | The application name to create. If not specified, the application name will be read from the imported object. If the application name already exists, an error is returned.
    try {
      UUID result = apiInstance.appsImport(luisApp, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsImport");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **luisApp** | [**LuisApp**](LuisApp.md)| A LUIS application structure. | |
| **appName** | **String**| The application name to create. If not specified, the application name will be read from the imported object. If the application name already exists, an error is returned. | [optional] |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the imported application. |  -  |
| **0** | Error Response. |  -  |

<a id="appsList"></a>
# **appsList**
> List&lt;ApplicationInfoResponse&gt; appsList(skip, take)



Lists all of the user&#39;s applications.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<ApplicationInfoResponse> result = apiInstance.appsList(skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;ApplicationInfoResponse&gt;**](ApplicationInfoResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of the user applications. |  -  |
| **0** | Error Response. |  -  |

<a id="appsListAvailableCustomPrebuiltDomains"></a>
# **appsListAvailableCustomPrebuiltDomains**
> List&lt;PrebuiltDomain&gt; appsListAvailableCustomPrebuiltDomains()



Gets all the available custom prebuilt domains for all cultures.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<PrebuiltDomain> result = apiInstance.appsListAvailableCustomPrebuiltDomains();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsListAvailableCustomPrebuiltDomains");
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

[**List&lt;PrebuiltDomain&gt;**](PrebuiltDomain.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of all custom prebuilt domains and their intents/entities representation. |  -  |
| **0** | Error Response. |  -  |

<a id="appsListAvailableCustomPrebuiltDomainsForCulture"></a>
# **appsListAvailableCustomPrebuiltDomainsForCulture**
> List&lt;PrebuiltDomain&gt; appsListAvailableCustomPrebuiltDomainsForCulture(culture)



Gets all the available prebuilt domains for a specific culture.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String culture = "culture_example"; // String | Culture.
    try {
      List<PrebuiltDomain> result = apiInstance.appsListAvailableCustomPrebuiltDomainsForCulture(culture);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsListAvailableCustomPrebuiltDomainsForCulture");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **culture** | **String**| Culture. | |

### Return type

[**List&lt;PrebuiltDomain&gt;**](PrebuiltDomain.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of all domains and their intents and entities for a specific culture. |  -  |
| **0** | Error Response. |  -  |

<a id="appsListCortanaEndpoints"></a>
# **appsListCortanaEndpoints**
> PersonalAssistantsResponse appsListCortanaEndpoints()



Gets the endpoint URLs for the prebuilt Cortana applications.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      PersonalAssistantsResponse result = apiInstance.appsListCortanaEndpoints();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsListCortanaEndpoints");
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

[**PersonalAssistantsResponse**](PersonalAssistantsResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A personal assistant apps JSON object containing the endpoint URLs for Cortana applications and the user&#39;s endpoint keys. |  -  |
| **0** | Error Response. |  -  |

<a id="appsListDomains"></a>
# **appsListDomains**
> List&lt;String&gt; appsListDomains()



Gets the available application domains.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<String> result = apiInstance.appsListDomains();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsListDomains");
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

**List&lt;String&gt;**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list object containing the available application domains. |  -  |
| **0** | Error Response. |  -  |

<a id="appsListEndpoints"></a>
# **appsListEndpoints**
> Map&lt;String, String&gt; appsListEndpoints(appId)



Returns the available endpoint deployment regions and URLs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    try {
      Map<String, String> result = apiInstance.appsListEndpoints(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsListEndpoints");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of endpoints regions and their corresponding endpoint URL. |  -  |
| **0** | Error Response. |  -  |

<a id="appsListSupportedCultures"></a>
# **appsListSupportedCultures**
> List&lt;AvailableCulture&gt; appsListSupportedCultures()



Gets a list of supported cultures. Cultures are equivalent to the written language and locale. For example,\&quot;en-us\&quot; represents the U.S. variation of English.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<AvailableCulture> result = apiInstance.appsListSupportedCultures();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsListSupportedCultures");
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

[**List&lt;AvailableCulture&gt;**](AvailableCulture.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list object containing the supported application cultures. |  -  |
| **0** | Error Response. |  -  |

<a id="appsListUsageScenarios"></a>
# **appsListUsageScenarios**
> List&lt;String&gt; appsListUsageScenarios()



Gets the application available usage scenarios.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<String> result = apiInstance.appsListUsageScenarios();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsListUsageScenarios");
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

**List&lt;String&gt;**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list object containing the available application usage scenarios. |  -  |
| **0** | Error Response. |  -  |

<a id="appsPackagePublishedApplicationAsGzip"></a>
# **appsPackagePublishedApplicationAsGzip**
> File appsPackagePublishedApplicationAsGzip(appId, slotName)

package - Gets published LUIS application package in binary stream GZip format

Packages a published LUIS application as a GZip file to be used in the LUIS container.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String slotName = "slotName_example"; // String | The publishing slot name.
    try {
      File result = apiInstance.appsPackagePublishedApplicationAsGzip(appId, slotName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsPackagePublishedApplicationAsGzip");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **slotName** | **String**| The publishing slot name. | |

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The GZip binary stream of the published application package. |  -  |
| **0** | Error Response. |  -  |

<a id="appsPackageTrainedApplicationAsGzip"></a>
# **appsPackageTrainedApplicationAsGzip**
> File appsPackageTrainedApplicationAsGzip(appId, versionId)

package - Gets trained LUIS application package in binary stream GZip format

Packages trained LUIS application as GZip file to be used in the LUIS container.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    try {
      File result = apiInstance.appsPackageTrainedApplicationAsGzip(appId, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsPackageTrainedApplicationAsGzip");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The GZip binary stream of the trained application package. |  -  |
| **0** | Error Response. |  -  |

<a id="appsPublish"></a>
# **appsPublish**
> ProductionOrStagingEndpointInfo appsPublish(appId, applicationPublishObject)



Publishes a specific version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    ApplicationPublishObject applicationPublishObject = new ApplicationPublishObject(); // ApplicationPublishObject | The application publish object. The region is the target region that the application is published to.
    try {
      ProductionOrStagingEndpointInfo result = apiInstance.appsPublish(appId, applicationPublishObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsPublish");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **applicationPublishObject** | [**ApplicationPublishObject**](ApplicationPublishObject.md)| The application publish object. The region is the target region that the application is published to. | |

### Return type

[**ProductionOrStagingEndpointInfo**](ProductionOrStagingEndpointInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | An object containing the application endpoint URL, its assigned endpoint key and publishing status. |  -  |
| **207** | An object containing the application endpoint URL, its assigned endpoint key and publishing status in case that publishing one or more regions failed. |  -  |
| **0** | Error Response. |  -  |

<a id="appsUpdate"></a>
# **appsUpdate**
> OperationStatus appsUpdate(appId, applicationUpdateObject)



Updates the name or description of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    ApplicationUpdateObject applicationUpdateObject = new ApplicationUpdateObject(); // ApplicationUpdateObject | A model containing Name and Description of the application.
    try {
      OperationStatus result = apiInstance.appsUpdate(appId, applicationUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **applicationUpdateObject** | [**ApplicationUpdateObject**](ApplicationUpdateObject.md)| A model containing Name and Description of the application. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated application name and description. |  -  |
| **0** | Error Response. |  -  |

<a id="appsUpdatePublishSettings"></a>
# **appsUpdatePublishSettings**
> OperationStatus appsUpdatePublishSettings(appId, publishSettingUpdateObject)



Updates the application publish settings including &#39;UseAllTrainingData&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    PublishSettingUpdateObject publishSettingUpdateObject = new PublishSettingUpdateObject(); // PublishSettingUpdateObject | An object containing the new publish application settings.
    try {
      OperationStatus result = apiInstance.appsUpdatePublishSettings(appId, publishSettingUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsUpdatePublishSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **publishSettingUpdateObject** | [**PublishSettingUpdateObject**](PublishSettingUpdateObject.md)| An object containing the new publish application settings. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated application settings. |  -  |
| **0** | Error Response. |  -  |

<a id="appsUpdateSettings"></a>
# **appsUpdateSettings**
> OperationStatus appsUpdateSettings(appId, applicationSettingUpdateObject)



Updates the application settings including &#39;UseAllTrainingData&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    ApplicationSettingUpdateObject applicationSettingUpdateObject = new ApplicationSettingUpdateObject(); // ApplicationSettingUpdateObject | An object containing the new application settings.
    try {
      OperationStatus result = apiInstance.appsUpdateSettings(appId, applicationSettingUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appsUpdateSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **applicationSettingUpdateObject** | [**ApplicationSettingUpdateObject**](ApplicationSettingUpdateObject.md)| An object containing the new application settings. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated application settings. |  -  |
| **0** | Error Response. |  -  |

<a id="azureAccountsAssignToApp"></a>
# **azureAccountsAssignToApp**
> OperationStatus azureAccountsAssignToApp(appId, authorization, azureAccountInfoObject)

apps - Assign a LUIS Azure account to an application

Assigns an Azure account to the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String authorization = "authorization_example"; // String | The bearer authorization header to use; containing the user's ARM token used to validate Azure accounts information.
    AzureAccountInfoObject azureAccountInfoObject = new AzureAccountInfoObject(); // AzureAccountInfoObject | The Azure account information object.
    try {
      OperationStatus result = apiInstance.azureAccountsAssignToApp(appId, authorization, azureAccountInfoObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#azureAccountsAssignToApp");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **authorization** | **String**| The bearer authorization header to use; containing the user&#39;s ARM token used to validate Azure accounts information. | |
| **azureAccountInfoObject** | [**AzureAccountInfoObject**](AzureAccountInfoObject.md)| The Azure account information object. | [optional] |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation. |  -  |
| **0** | Error Response. |  -  |

<a id="azureAccountsGetAssigned"></a>
# **azureAccountsGetAssigned**
> List&lt;AzureAccountInfoObject&gt; azureAccountsGetAssigned(appId, authorization)

apps - Get LUIS Azure accounts assigned to the application

Gets the LUIS Azure accounts assigned to the application for the user using his ARM token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String authorization = "authorization_example"; // String | The bearer authorization header to use; containing the user's ARM token used to validate Azure accounts information.
    try {
      List<AzureAccountInfoObject> result = apiInstance.azureAccountsGetAssigned(appId, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#azureAccountsGetAssigned");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **authorization** | **String**| The bearer authorization header to use; containing the user&#39;s ARM token used to validate Azure accounts information. | |

### Return type

[**List&lt;AzureAccountInfoObject&gt;**](AzureAccountInfoObject.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of azure account information objects. |  -  |
| **0** | Error Response. |  -  |

<a id="azureAccountsListUserLUISAccounts"></a>
# **azureAccountsListUserLUISAccounts**
> List&lt;AzureAccountInfoObject&gt; azureAccountsListUserLUISAccounts(authorization)

user - Get LUIS Azure accounts

Gets the LUIS Azure accounts for the user using his ARM token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String authorization = "authorization_example"; // String | The bearer authorization header to use; containing the user's ARM token used to validate Azure accounts information.
    try {
      List<AzureAccountInfoObject> result = apiInstance.azureAccountsListUserLUISAccounts(authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#azureAccountsListUserLUISAccounts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **authorization** | **String**| The bearer authorization header to use; containing the user&#39;s ARM token used to validate Azure accounts information. | |

### Return type

[**List&lt;AzureAccountInfoObject&gt;**](AzureAccountInfoObject.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Azure account information objects. |  -  |
| **0** | Error Response. |  -  |

<a id="azureAccountsRemoveFromApp"></a>
# **azureAccountsRemoveFromApp**
> OperationStatus azureAccountsRemoveFromApp(appId, authorization, azureAccountInfoObject)

apps - Removes an assigned LUIS Azure account from an application

Removes assigned Azure account from the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String authorization = "authorization_example"; // String | The bearer authorization header to use; containing the user's ARM token used to validate Azure accounts information.
    AzureAccountInfoObject azureAccountInfoObject = new AzureAccountInfoObject(); // AzureAccountInfoObject | The Azure account information object.
    try {
      OperationStatus result = apiInstance.azureAccountsRemoveFromApp(appId, authorization, azureAccountInfoObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#azureAccountsRemoveFromApp");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **authorization** | **String**| The bearer authorization header to use; containing the user&#39;s ARM token used to validate Azure accounts information. | |
| **azureAccountInfoObject** | [**AzureAccountInfoObject**](AzureAccountInfoObject.md)| The Azure account information object. | [optional] |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  -  |
| **0** | Error Response. |  -  |

<a id="examplesAdd"></a>
# **examplesAdd**
> LabelExampleResponse examplesAdd(appId, versionId, exampleLabelObject)



Adds a labeled example utterance in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    ExampleLabelObject exampleLabelObject = new ExampleLabelObject(); // ExampleLabelObject | A labeled example utterance with the expected intent and entities.
    try {
      LabelExampleResponse result = apiInstance.examplesAdd(appId, versionId, exampleLabelObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#examplesAdd");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **exampleLabelObject** | [**ExampleLabelObject**](ExampleLabelObject.md)| A labeled example utterance with the expected intent and entities. | |

### Return type

[**LabelExampleResponse**](LabelExampleResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created example utterance. |  -  |
| **0** | Error Response. |  -  |

<a id="examplesBatch"></a>
# **examplesBatch**
> List&lt;BatchLabelExample&gt; examplesBatch(appId, versionId, exampleLabelObjectArray)



Adds a batch of labeled example utterances to a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    List<ExampleLabelObject> exampleLabelObjectArray = Arrays.asList(); // List<ExampleLabelObject> | Array of example utterances.
    try {
      List<BatchLabelExample> result = apiInstance.examplesBatch(appId, versionId, exampleLabelObjectArray);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#examplesBatch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **exampleLabelObjectArray** | [**List&lt;ExampleLabelObject&gt;**](ExampleLabelObject.md)| Array of example utterances. | |

### Return type

[**List&lt;BatchLabelExample&gt;**](BatchLabelExample.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A string array determining which labeled example utterances were added successfully. |  -  |
| **207** | Indicates that the request was partially successful. The response contains a string array indicating the status of each of the added labeled example utterances. |  -  |
| **0** | Error Response. |  -  |

<a id="examplesDelete"></a>
# **examplesDelete**
> OperationStatus examplesDelete(appId, versionId, exampleId)



Deletes the labeled example utterances with the specified ID from a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer exampleId = 56; // Integer | The example ID.
    try {
      OperationStatus result = apiInstance.examplesDelete(appId, versionId, exampleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#examplesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **exampleId** | **Integer**| The example ID. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted example utterance. |  -  |
| **0** | Error Response. |  -  |

<a id="examplesList"></a>
# **examplesList**
> List&lt;LabeledUtterance&gt; examplesList(appId, versionId, skip, take)



Returns example utterances to be reviewed from a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<LabeledUtterance> result = apiInstance.examplesList(appId, versionId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#examplesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;LabeledUtterance&gt;**](LabeledUtterance.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of predictions and label pairs for every example utterance in the application. |  -  |
| **0** | Error Response. |  -  |

<a id="featuresAddPhraseList"></a>
# **featuresAddPhraseList**
> Integer featuresAddPhraseList(appId, versionId, phraselistCreateObject)



Creates a new phraselist feature in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    PhraselistCreateObject phraselistCreateObject = new PhraselistCreateObject(); // PhraselistCreateObject | A Phraselist object containing Name, comma-separated Phrases and the isExchangeable boolean. Default value for isExchangeable is true.
    try {
      Integer result = apiInstance.featuresAddPhraseList(appId, versionId, phraselistCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#featuresAddPhraseList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **phraselistCreateObject** | [**PhraselistCreateObject**](PhraselistCreateObject.md)| A Phraselist object containing Name, comma-separated Phrases and the isExchangeable boolean. Default value for isExchangeable is true. | |

### Return type

**Integer**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created feature. |  -  |
| **0** | Error Response. |  -  |

<a id="featuresCreatePatternFeature"></a>
# **featuresCreatePatternFeature**
> Integer featuresCreatePatternFeature(appId, versionId, patternCreateObject)



[DEPRECATED NOTICE: This operation will soon be removed] Creates a new pattern feature in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    PatternCreateObject patternCreateObject = new PatternCreateObject(); // PatternCreateObject | The Name and Pattern of the feature.
    try {
      Integer result = apiInstance.featuresCreatePatternFeature(appId, versionId, patternCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#featuresCreatePatternFeature");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **patternCreateObject** | [**PatternCreateObject**](PatternCreateObject.md)| The Name and Pattern of the feature. | |

### Return type

**Integer**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created feature. |  -  |
| **0** | Error Response. |  -  |

<a id="featuresDeletePatternFeature"></a>
# **featuresDeletePatternFeature**
> OperationStatus featuresDeletePatternFeature(appId, versionId, patternId)



[DEPRECATED NOTICE: This operation will soon be removed] Deletes a pattern feature in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer patternId = 56; // Integer | The pattern feature ID.
    try {
      OperationStatus result = apiInstance.featuresDeletePatternFeature(appId, versionId, patternId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#featuresDeletePatternFeature");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **patternId** | **Integer**| The pattern feature ID. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  -  |
| **0** | Error Response. |  -  |

<a id="featuresDeletePhraseList"></a>
# **featuresDeletePhraseList**
> OperationStatus featuresDeletePhraseList(appId, versionId, phraselistId)



Deletes a phraselist feature from a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer phraselistId = 56; // Integer | The ID of the feature to be deleted.
    try {
      OperationStatus result = apiInstance.featuresDeletePhraseList(appId, versionId, phraselistId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#featuresDeletePhraseList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **phraselistId** | **Integer**| The ID of the feature to be deleted. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted phraselist. |  -  |
| **0** | Error Response. |  -  |

<a id="featuresGetPatternFeatureInfo"></a>
# **featuresGetPatternFeatureInfo**
> PatternFeatureInfo featuresGetPatternFeatureInfo(appId, versionId, patternId)



[DEPRECATED NOTICE: This operation will soon be removed] Gets the specified pattern feature&#39;s info in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer patternId = 56; // Integer | The pattern feature ID.
    try {
      PatternFeatureInfo result = apiInstance.featuresGetPatternFeatureInfo(appId, versionId, patternId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#featuresGetPatternFeatureInfo");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **patternId** | **Integer**| The pattern feature ID. | |

### Return type

[**PatternFeatureInfo**](PatternFeatureInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The pattern feature info. |  -  |
| **0** | Error Response. |  -  |

<a id="featuresGetPhraseList"></a>
# **featuresGetPhraseList**
> PhraseListFeatureInfo featuresGetPhraseList(appId, versionId, phraselistId)



Gets phraselist feature info in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer phraselistId = 56; // Integer | The ID of the feature to be retrieved.
    try {
      PhraseListFeatureInfo result = apiInstance.featuresGetPhraseList(appId, versionId, phraselistId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#featuresGetPhraseList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **phraselistId** | **Integer**| The ID of the feature to be retrieved. | |

### Return type

[**PhraseListFeatureInfo**](PhraseListFeatureInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A phraselist feature info. |  -  |
| **0** | Error Response. |  -  |

<a id="featuresList"></a>
# **featuresList**
> FeaturesResponseObject featuresList(appId, versionId, skip, take)



Gets all the extraction phraselist and pattern features in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      FeaturesResponseObject result = apiInstance.featuresList(appId, versionId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#featuresList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**FeaturesResponseObject**](FeaturesResponseObject.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of all phraselist features and a list of all pattern features. |  -  |
| **0** | Error Response. |  -  |

<a id="featuresListApplicationVersionPatternFeatures"></a>
# **featuresListApplicationVersionPatternFeatures**
> List&lt;PatternFeatureInfo&gt; featuresListApplicationVersionPatternFeatures(appId, versionId, skip, take)



[DEPRECATED NOTICE: This operation will soon be removed] Gets all the pattern features.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<PatternFeatureInfo> result = apiInstance.featuresListApplicationVersionPatternFeatures(appId, versionId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#featuresListApplicationVersionPatternFeatures");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;PatternFeatureInfo&gt;**](PatternFeatureInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of pattern features. |  -  |
| **0** | Error Response. |  -  |

<a id="featuresListPhraseLists"></a>
# **featuresListPhraseLists**
> List&lt;PhraseListFeatureInfo&gt; featuresListPhraseLists(appId, versionId, skip, take)



Gets all the phraselist features in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<PhraseListFeatureInfo> result = apiInstance.featuresListPhraseLists(appId, versionId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#featuresListPhraseLists");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;PhraseListFeatureInfo&gt;**](PhraseListFeatureInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of all phraselist features. |  -  |
| **0** | Error Response. |  -  |

<a id="featuresUpdatePatternFeature"></a>
# **featuresUpdatePatternFeature**
> OperationStatus featuresUpdatePatternFeature(appId, versionId, patternId, patternUpdateObject)



[DEPRECATED NOTICE: This operation will soon be removed] Updates the pattern, the name and the state of the pattern feature in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer patternId = 56; // Integer | The pattern feature ID.
    PatternUpdateObject patternUpdateObject = new PatternUpdateObject(); // PatternUpdateObject | The new values for: - Just a boolean called IsActive, in which case the status of the feature will be changed. - Name, Pattern and a boolean called IsActive to update the feature.
    try {
      OperationStatus result = apiInstance.featuresUpdatePatternFeature(appId, versionId, patternId, patternUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#featuresUpdatePatternFeature");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **patternId** | **Integer**| The pattern feature ID. | |
| **patternUpdateObject** | [**PatternUpdateObject**](PatternUpdateObject.md)| The new values for: - Just a boolean called IsActive, in which case the status of the feature will be changed. - Name, Pattern and a boolean called IsActive to update the feature. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  -  |
| **0** | Error Response. |  -  |

<a id="featuresUpdatePhraseList"></a>
# **featuresUpdatePhraseList**
> OperationStatus featuresUpdatePhraseList(appId, versionId, phraselistId, phraselistUpdateObject)



Updates the phrases, the state and the name of the phraselist feature in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer phraselistId = 56; // Integer | The ID of the feature to be updated.
    PhraselistUpdateObject phraselistUpdateObject = new PhraselistUpdateObject(); // PhraselistUpdateObject | The new values for: - Just a boolean called IsActive, in which case the status of the feature will be changed. - Name, Pattern, Mode, and a boolean called IsActive to update the feature.
    try {
      OperationStatus result = apiInstance.featuresUpdatePhraseList(appId, versionId, phraselistId, phraselistUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#featuresUpdatePhraseList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **phraselistId** | **Integer**| The ID of the feature to be updated. | |
| **phraselistUpdateObject** | [**PhraselistUpdateObject**](PhraselistUpdateObject.md)| The new values for: - Just a boolean called IsActive, in which case the status of the feature will be changed. - Name, Pattern, Mode, and a boolean called IsActive to update the feature. | [optional] |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated phraselist. |  -  |
| **0** | Error Response. |  -  |

<a id="modelAddClosedList"></a>
# **modelAddClosedList**
> UUID modelAddClosedList(appId, versionId, closedListModelCreateObject)



Adds a list entity model to a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    ClosedListModelCreateObject closedListModelCreateObject = new ClosedListModelCreateObject(); // ClosedListModelCreateObject | A model containing the name and words for the new list entity extractor.
    try {
      UUID result = apiInstance.modelAddClosedList(appId, versionId, closedListModelCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelAddClosedList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **closedListModelCreateObject** | [**ClosedListModelCreateObject**](ClosedListModelCreateObject.md)| A model containing the name and words for the new list entity extractor. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created model. |  -  |
| **0** | Error Response. |  -  |

<a id="modelAddCompositeEntity"></a>
# **modelAddCompositeEntity**
> UUID modelAddCompositeEntity(appId, versionId, compositeModelCreateObject)



Adds a composite entity extractor to a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    CompositeEntityModel compositeModelCreateObject = new CompositeEntityModel(); // CompositeEntityModel | A model containing the name and children of the new entity extractor.
    try {
      UUID result = apiInstance.modelAddCompositeEntity(appId, versionId, compositeModelCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelAddCompositeEntity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **compositeModelCreateObject** | [**CompositeEntityModel**](CompositeEntityModel.md)| A model containing the name and children of the new entity extractor. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created Model. |  -  |
| **0** | Error Response. |  -  |

<a id="modelAddCompositeEntityChild"></a>
# **modelAddCompositeEntityChild**
> UUID modelAddCompositeEntityChild(appId, versionId, cEntityId, compositeChildModelCreateObject)



Creates a single child in an existing composite entity model in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID cEntityId = UUID.randomUUID(); // UUID | The composite entity extractor ID.
    ModelAddCompositeEntityChildRequest compositeChildModelCreateObject = new ModelAddCompositeEntityChildRequest(); // ModelAddCompositeEntityChildRequest | A model object containing the name of the new composite child model.
    try {
      UUID result = apiInstance.modelAddCompositeEntityChild(appId, versionId, cEntityId, compositeChildModelCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelAddCompositeEntityChild");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **cEntityId** | **UUID**| The composite entity extractor ID. | |
| **compositeChildModelCreateObject** | [**ModelAddCompositeEntityChildRequest**](ModelAddCompositeEntityChildRequest.md)| A model object containing the name of the new composite child model. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created model. |  -  |
| **0** | Error Response. |  -  |

<a id="modelAddCustomPrebuiltDomain"></a>
# **modelAddCustomPrebuiltDomain**
> List&lt;UUID&gt; modelAddCustomPrebuiltDomain(appId, versionId, prebuiltDomainObject)



Adds a customizable prebuilt domain along with all of its intent and entity models in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    PrebuiltDomainCreateBaseObject prebuiltDomainObject = new PrebuiltDomainCreateBaseObject(); // PrebuiltDomainCreateBaseObject | A prebuilt domain create object containing the name of the domain.
    try {
      List<UUID> result = apiInstance.modelAddCustomPrebuiltDomain(appId, versionId, prebuiltDomainObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelAddCustomPrebuiltDomain");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **prebuiltDomainObject** | [**PrebuiltDomainCreateBaseObject**](PrebuiltDomainCreateBaseObject.md)| A prebuilt domain create object containing the name of the domain. | |

### Return type

[**List&lt;UUID&gt;**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | An array of the created customizable prebuilt domain intent and entity model Ids. |  -  |
| **0** | Error Response. |  -  |

<a id="modelAddCustomPrebuiltEntity"></a>
# **modelAddCustomPrebuiltEntity**
> UUID modelAddCustomPrebuiltEntity(appId, versionId, prebuiltDomainModelCreateObject)



Adds a prebuilt entity model to a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    PrebuiltDomainModelCreateObject prebuiltDomainModelCreateObject = new PrebuiltDomainModelCreateObject(); // PrebuiltDomainModelCreateObject | A model object containing the name of the prebuilt entity and the name of the domain to which this model belongs.
    try {
      UUID result = apiInstance.modelAddCustomPrebuiltEntity(appId, versionId, prebuiltDomainModelCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelAddCustomPrebuiltEntity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **prebuiltDomainModelCreateObject** | [**PrebuiltDomainModelCreateObject**](PrebuiltDomainModelCreateObject.md)| A model object containing the name of the prebuilt entity and the name of the domain to which this model belongs. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created prebuilt model. |  -  |
| **0** | Error Response. |  -  |

<a id="modelAddCustomPrebuiltIntent"></a>
# **modelAddCustomPrebuiltIntent**
> UUID modelAddCustomPrebuiltIntent(appId, versionId, prebuiltDomainModelCreateObject)



Adds a customizable prebuilt intent model to a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    PrebuiltDomainModelCreateObject prebuiltDomainModelCreateObject = new PrebuiltDomainModelCreateObject(); // PrebuiltDomainModelCreateObject | A model object containing the name of the customizable prebuilt intent and the name of the domain to which this model belongs.
    try {
      UUID result = apiInstance.modelAddCustomPrebuiltIntent(appId, versionId, prebuiltDomainModelCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelAddCustomPrebuiltIntent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **prebuiltDomainModelCreateObject** | [**PrebuiltDomainModelCreateObject**](PrebuiltDomainModelCreateObject.md)| A model object containing the name of the customizable prebuilt intent and the name of the domain to which this model belongs. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created intent model. |  -  |
| **0** | Error Response. |  -  |

<a id="modelAddEntity"></a>
# **modelAddEntity**
> UUID modelAddEntity(appId, versionId, modelCreateObject)



Adds a simple entity extractor to a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    ModelCreateObject modelCreateObject = new ModelCreateObject(); // ModelCreateObject | A model object containing the name for the new simple entity extractor.
    try {
      UUID result = apiInstance.modelAddEntity(appId, versionId, modelCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelAddEntity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **modelCreateObject** | [**ModelCreateObject**](ModelCreateObject.md)| A model object containing the name for the new simple entity extractor. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created model. |  -  |
| **0** | Error Response. |  -  |

<a id="modelAddExplicitListItem"></a>
# **modelAddExplicitListItem**
> Integer modelAddExplicitListItem(appId, versionId, entityId, item)

Add a new exception to the explicit list for the Pattern.Any entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The Pattern.Any entity extractor ID.
    ExplicitListItemCreateObject item = new ExplicitListItemCreateObject(); // ExplicitListItemCreateObject | The new explicit list item.
    try {
      Integer result = apiInstance.modelAddExplicitListItem(appId, versionId, entityId, item);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelAddExplicitListItem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The Pattern.Any entity extractor ID. | |
| **item** | [**ExplicitListItemCreateObject**](ExplicitListItemCreateObject.md)| The new explicit list item. | |

### Return type

**Integer**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created explicit list item. |  -  |
| **0** | Error Response. |  -  |

<a id="modelAddHierarchicalEntity"></a>
# **modelAddHierarchicalEntity**
> UUID modelAddHierarchicalEntity(appId, versionId, hierarchicalModelCreateObject)



Adds a hierarchical entity extractor to a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    HierarchicalEntityModel hierarchicalModelCreateObject = new HierarchicalEntityModel(); // HierarchicalEntityModel | A model containing the name and children of the new entity extractor.
    try {
      UUID result = apiInstance.modelAddHierarchicalEntity(appId, versionId, hierarchicalModelCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelAddHierarchicalEntity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **hierarchicalModelCreateObject** | [**HierarchicalEntityModel**](HierarchicalEntityModel.md)| A model containing the name and children of the new entity extractor. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created model. |  -  |
| **0** | Error Response. |  -  |

<a id="modelAddHierarchicalEntityChild"></a>
# **modelAddHierarchicalEntityChild**
> UUID modelAddHierarchicalEntityChild(appId, versionId, hEntityId, hierarchicalChildModelCreateObject)



Creates a single child in an existing hierarchical entity model in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID hEntityId = UUID.randomUUID(); // UUID | The hierarchical entity extractor ID.
    ModelAddCompositeEntityChildRequest hierarchicalChildModelCreateObject = new ModelAddCompositeEntityChildRequest(); // ModelAddCompositeEntityChildRequest | A model object containing the name of the new hierarchical child model.
    try {
      UUID result = apiInstance.modelAddHierarchicalEntityChild(appId, versionId, hEntityId, hierarchicalChildModelCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelAddHierarchicalEntityChild");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **hEntityId** | **UUID**| The hierarchical entity extractor ID. | |
| **hierarchicalChildModelCreateObject** | [**ModelAddCompositeEntityChildRequest**](ModelAddCompositeEntityChildRequest.md)| A model object containing the name of the new hierarchical child model. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created model. |  -  |
| **0** | Error Response. |  -  |

<a id="modelAddIntent"></a>
# **modelAddIntent**
> UUID modelAddIntent(appId, versionId, intentCreateObject)



Adds an intent to a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    ModelCreateObject intentCreateObject = new ModelCreateObject(); // ModelCreateObject | A model object containing the name of the new intent.
    try {
      UUID result = apiInstance.modelAddIntent(appId, versionId, intentCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelAddIntent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **intentCreateObject** | [**ModelCreateObject**](ModelCreateObject.md)| A model object containing the name of the new intent. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created intent model. |  -  |
| **0** | Error Response. |  -  |

<a id="modelAddPrebuilt"></a>
# **modelAddPrebuilt**
> List&lt;PrebuiltEntityExtractor&gt; modelAddPrebuilt(appId, versionId, prebuiltExtractorNames)



Adds a list of prebuilt entities to a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    List<String> prebuiltExtractorNames = Arrays.asList(); // List<String> | An array of prebuilt entity extractor names.
    try {
      List<PrebuiltEntityExtractor> result = apiInstance.modelAddPrebuilt(appId, versionId, prebuiltExtractorNames);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelAddPrebuilt");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **prebuiltExtractorNames** | [**List&lt;String&gt;**](String.md)| An array of prebuilt entity extractor names. | |

### Return type

[**List&lt;PrebuiltEntityExtractor&gt;**](PrebuiltEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | An array of the created prebuilt extractor infos. |  -  |
| **0** | Error Response. |  -  |

<a id="modelAddSubList"></a>
# **modelAddSubList**
> Long modelAddSubList(appId, versionId, clEntityId, wordListCreateObject)



Adds a sublist to an existing list entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID clEntityId = UUID.randomUUID(); // UUID | The list entity extractor ID.
    WordListObject wordListCreateObject = new WordListObject(); // WordListObject | Words list.
    try {
      Long result = apiInstance.modelAddSubList(appId, versionId, clEntityId, wordListCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelAddSubList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **clEntityId** | **UUID**| The list entity extractor ID. | |
| **wordListCreateObject** | [**WordListObject**](WordListObject.md)| Words list. | |

### Return type

**Long**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the newly created sublist. |  -  |
| **0** | Error Response. |  -  |

<a id="modelCreateClosedListEntityRole"></a>
# **modelCreateClosedListEntityRole**
> UUID modelCreateClosedListEntityRole(appId, versionId, entityId, entityRoleCreateObject)

Create a role for a list entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity model ID.
    EntityRoleCreateObject entityRoleCreateObject = new EntityRoleCreateObject(); // EntityRoleCreateObject | An entity role object containing the name of role.
    try {
      UUID result = apiInstance.modelCreateClosedListEntityRole(appId, versionId, entityId, entityRoleCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelCreateClosedListEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity model ID. | |
| **entityRoleCreateObject** | [**EntityRoleCreateObject**](EntityRoleCreateObject.md)| An entity role object containing the name of role. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created entity role |  -  |
| **0** | Error Response. |  -  |

<a id="modelCreateCompositeEntityRole"></a>
# **modelCreateCompositeEntityRole**
> UUID modelCreateCompositeEntityRole(appId, versionId, cEntityId, entityRoleCreateObject)

Create a role for a composite entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID cEntityId = UUID.randomUUID(); // UUID | The composite entity extractor ID.
    EntityRoleCreateObject entityRoleCreateObject = new EntityRoleCreateObject(); // EntityRoleCreateObject | An entity role object containing the name of role.
    try {
      UUID result = apiInstance.modelCreateCompositeEntityRole(appId, versionId, cEntityId, entityRoleCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelCreateCompositeEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **cEntityId** | **UUID**| The composite entity extractor ID. | |
| **entityRoleCreateObject** | [**EntityRoleCreateObject**](EntityRoleCreateObject.md)| An entity role object containing the name of role. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created entity role |  -  |
| **0** | Error Response. |  -  |

<a id="modelCreateCustomPrebuiltEntityRole"></a>
# **modelCreateCustomPrebuiltEntityRole**
> UUID modelCreateCustomPrebuiltEntityRole(appId, versionId, entityId, entityRoleCreateObject)

Create a role for a prebuilt entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity model ID.
    EntityRoleCreateObject entityRoleCreateObject = new EntityRoleCreateObject(); // EntityRoleCreateObject | An entity role object containing the name of role.
    try {
      UUID result = apiInstance.modelCreateCustomPrebuiltEntityRole(appId, versionId, entityId, entityRoleCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelCreateCustomPrebuiltEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity model ID. | |
| **entityRoleCreateObject** | [**EntityRoleCreateObject**](EntityRoleCreateObject.md)| An entity role object containing the name of role. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created entity role |  -  |
| **0** | Error Response. |  -  |

<a id="modelCreateEntityRole"></a>
# **modelCreateEntityRole**
> UUID modelCreateEntityRole(appId, versionId, entityId, entityRoleCreateObject)

Create an entity role in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity model ID.
    EntityRoleCreateObject entityRoleCreateObject = new EntityRoleCreateObject(); // EntityRoleCreateObject | An entity role object containing the name of role.
    try {
      UUID result = apiInstance.modelCreateEntityRole(appId, versionId, entityId, entityRoleCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelCreateEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity model ID. | |
| **entityRoleCreateObject** | [**EntityRoleCreateObject**](EntityRoleCreateObject.md)| An entity role object containing the name of role. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created entity role |  -  |
| **0** | Error Response. |  -  |

<a id="modelCreateHierarchicalEntityRole"></a>
# **modelCreateHierarchicalEntityRole**
> UUID modelCreateHierarchicalEntityRole(appId, versionId, hEntityId, entityRoleCreateObject)

Create a role for an hierarchical entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID hEntityId = UUID.randomUUID(); // UUID | The hierarchical entity extractor ID.
    EntityRoleCreateObject entityRoleCreateObject = new EntityRoleCreateObject(); // EntityRoleCreateObject | An entity role object containing the name of role.
    try {
      UUID result = apiInstance.modelCreateHierarchicalEntityRole(appId, versionId, hEntityId, entityRoleCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelCreateHierarchicalEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **hEntityId** | **UUID**| The hierarchical entity extractor ID. | |
| **entityRoleCreateObject** | [**EntityRoleCreateObject**](EntityRoleCreateObject.md)| An entity role object containing the name of role. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created entity role |  -  |
| **0** | Error Response. |  -  |

<a id="modelCreatePatternAnyEntityModel"></a>
# **modelCreatePatternAnyEntityModel**
> UUID modelCreatePatternAnyEntityModel(appId, versionId, extractorCreateObject)

Adds a pattern.any entity extractor to a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    PatternAnyModelCreateObject extractorCreateObject = new PatternAnyModelCreateObject(); // PatternAnyModelCreateObject | A model object containing the name and explicit list for the new Pattern.Any entity extractor.
    try {
      UUID result = apiInstance.modelCreatePatternAnyEntityModel(appId, versionId, extractorCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelCreatePatternAnyEntityModel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **extractorCreateObject** | [**PatternAnyModelCreateObject**](PatternAnyModelCreateObject.md)| A model object containing the name and explicit list for the new Pattern.Any entity extractor. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created Pattern.Any entity model. |  -  |
| **0** | Error Response. |  -  |

<a id="modelCreatePatternAnyEntityRole"></a>
# **modelCreatePatternAnyEntityRole**
> UUID modelCreatePatternAnyEntityRole(appId, versionId, entityId, entityRoleCreateObject)

Create a role for an Pattern.any entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity model ID.
    EntityRoleCreateObject entityRoleCreateObject = new EntityRoleCreateObject(); // EntityRoleCreateObject | An entity role object containing the name of role.
    try {
      UUID result = apiInstance.modelCreatePatternAnyEntityRole(appId, versionId, entityId, entityRoleCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelCreatePatternAnyEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity model ID. | |
| **entityRoleCreateObject** | [**EntityRoleCreateObject**](EntityRoleCreateObject.md)| An entity role object containing the name of role. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created entity role |  -  |
| **0** | Error Response. |  -  |

<a id="modelCreatePrebuiltEntityRole"></a>
# **modelCreatePrebuiltEntityRole**
> UUID modelCreatePrebuiltEntityRole(appId, versionId, entityId, entityRoleCreateObject)

Create a role for a prebuilt entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity model ID.
    EntityRoleCreateObject entityRoleCreateObject = new EntityRoleCreateObject(); // EntityRoleCreateObject | An entity role object containing the name of role.
    try {
      UUID result = apiInstance.modelCreatePrebuiltEntityRole(appId, versionId, entityId, entityRoleCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelCreatePrebuiltEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity model ID. | |
| **entityRoleCreateObject** | [**EntityRoleCreateObject**](EntityRoleCreateObject.md)| An entity role object containing the name of role. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created entity role |  -  |
| **0** | Error Response. |  -  |

<a id="modelCreateRegexEntityModel"></a>
# **modelCreateRegexEntityModel**
> UUID modelCreateRegexEntityModel(appId, versionId, regexEntityExtractorCreateObj)

Adds a regular expression entity model to a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    RegexModelCreateObject regexEntityExtractorCreateObj = new RegexModelCreateObject(); // RegexModelCreateObject | A model object containing the name and regex pattern for the new regular expression entity extractor.
    try {
      UUID result = apiInstance.modelCreateRegexEntityModel(appId, versionId, regexEntityExtractorCreateObj);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelCreateRegexEntityModel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **regexEntityExtractorCreateObj** | [**RegexModelCreateObject**](RegexModelCreateObject.md)| A model object containing the name and regex pattern for the new regular expression entity extractor. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created model. |  -  |
| **0** | Error Response. |  -  |

<a id="modelCreateRegexEntityRole"></a>
# **modelCreateRegexEntityRole**
> UUID modelCreateRegexEntityRole(appId, versionId, entityId, entityRoleCreateObject)

Create a role for an regular expression entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity model ID.
    EntityRoleCreateObject entityRoleCreateObject = new EntityRoleCreateObject(); // EntityRoleCreateObject | An entity role object containing the name of role.
    try {
      UUID result = apiInstance.modelCreateRegexEntityRole(appId, versionId, entityId, entityRoleCreateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelCreateRegexEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity model ID. | |
| **entityRoleCreateObject** | [**EntityRoleCreateObject**](EntityRoleCreateObject.md)| An entity role object containing the name of role. | |

### Return type

[**UUID**](UUID.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ID of the created entity role |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeleteClosedList"></a>
# **modelDeleteClosedList**
> OperationStatus modelDeleteClosedList(appId, versionId, clEntityId)



Deletes a list entity model from a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID clEntityId = UUID.randomUUID(); // UUID | The list entity model ID.
    try {
      OperationStatus result = apiInstance.modelDeleteClosedList(appId, versionId, clEntityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeleteClosedList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **clEntityId** | **UUID**| The list entity model ID. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully delete list entity from a version of application. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeleteClosedListEntityRole"></a>
# **modelDeleteClosedListEntityRole**
> OperationStatus modelDeleteClosedListEntityRole(appId, versionId, entityId, roleId)

Delete a role for a given list entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | The entity role Id.
    try {
      OperationStatus result = apiInstance.modelDeleteClosedListEntityRole(appId, versionId, entityId, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeleteClosedListEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity ID. | |
| **roleId** | **UUID**| The entity role Id. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully operation. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeleteCompositeEntity"></a>
# **modelDeleteCompositeEntity**
> OperationStatus modelDeleteCompositeEntity(appId, versionId, cEntityId)



Deletes a composite entity from a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID cEntityId = UUID.randomUUID(); // UUID | The composite entity extractor ID.
    try {
      OperationStatus result = apiInstance.modelDeleteCompositeEntity(appId, versionId, cEntityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeleteCompositeEntity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **cEntityId** | **UUID**| The composite entity extractor ID. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted composite entity. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeleteCompositeEntityChild"></a>
# **modelDeleteCompositeEntityChild**
> OperationStatus modelDeleteCompositeEntityChild(appId, versionId, cEntityId, cChildId)



Deletes a composite entity extractor child from a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID cEntityId = UUID.randomUUID(); // UUID | The composite entity extractor ID.
    UUID cChildId = UUID.randomUUID(); // UUID | The hierarchical entity extractor child ID.
    try {
      OperationStatus result = apiInstance.modelDeleteCompositeEntityChild(appId, versionId, cEntityId, cChildId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeleteCompositeEntityChild");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **cEntityId** | **UUID**| The composite entity extractor ID. | |
| **cChildId** | **UUID**| The hierarchical entity extractor child ID. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted entity. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeleteCompositeEntityRole"></a>
# **modelDeleteCompositeEntityRole**
> OperationStatus modelDeleteCompositeEntityRole(appId, versionId, cEntityId, roleId)

Delete a role for a given composite entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID cEntityId = UUID.randomUUID(); // UUID | The composite entity extractor ID.
    UUID roleId = UUID.randomUUID(); // UUID | The entity role Id.
    try {
      OperationStatus result = apiInstance.modelDeleteCompositeEntityRole(appId, versionId, cEntityId, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeleteCompositeEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **cEntityId** | **UUID**| The composite entity extractor ID. | |
| **roleId** | **UUID**| The entity role Id. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully operation. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeleteCustomEntityRole"></a>
# **modelDeleteCustomEntityRole**
> OperationStatus modelDeleteCustomEntityRole(appId, versionId, entityId, roleId)

Delete a role for a given prebuilt entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | The entity role Id.
    try {
      OperationStatus result = apiInstance.modelDeleteCustomEntityRole(appId, versionId, entityId, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeleteCustomEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity ID. | |
| **roleId** | **UUID**| The entity role Id. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully operation. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeleteCustomPrebuiltDomain"></a>
# **modelDeleteCustomPrebuiltDomain**
> OperationStatus modelDeleteCustomPrebuiltDomain(appId, versionId, domainName)



Deletes a prebuilt domain&#39;s models in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    String domainName = "domainName_example"; // String | Domain name.
    try {
      OperationStatus result = apiInstance.modelDeleteCustomPrebuiltDomain(appId, versionId, domainName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeleteCustomPrebuiltDomain");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **domainName** | **String**| Domain name. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeleteEntity"></a>
# **modelDeleteEntity**
> OperationStatus modelDeleteEntity(appId, versionId, entityId)



Deletes an entity from a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity extractor ID.
    try {
      OperationStatus result = apiInstance.modelDeleteEntity(appId, versionId, entityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeleteEntity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity extractor ID. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted entity. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeleteEntityRole"></a>
# **modelDeleteEntityRole**
> OperationStatus modelDeleteEntityRole(appId, versionId, entityId, roleId)

Delete an entity role in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | The entity role Id.
    try {
      OperationStatus result = apiInstance.modelDeleteEntityRole(appId, versionId, entityId, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeleteEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity ID. | |
| **roleId** | **UUID**| The entity role Id. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully operation. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeleteExplicitListItem"></a>
# **modelDeleteExplicitListItem**
> OperationStatus modelDeleteExplicitListItem(appId, versionId, entityId, itemId)

Delete an item from the explicit (exception) list for a Pattern.any entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The pattern.any entity id.
    Long itemId = 56L; // Long | The explicit list item which will be deleted.
    try {
      OperationStatus result = apiInstance.modelDeleteExplicitListItem(appId, versionId, entityId, itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeleteExplicitListItem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The pattern.any entity id. | |
| **itemId** | **Long**| The explicit list item which will be deleted. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully operation. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeleteHierarchicalEntity"></a>
# **modelDeleteHierarchicalEntity**
> OperationStatus modelDeleteHierarchicalEntity(appId, versionId, hEntityId)



Deletes a hierarchical entity from a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID hEntityId = UUID.randomUUID(); // UUID | The hierarchical entity extractor ID.
    try {
      OperationStatus result = apiInstance.modelDeleteHierarchicalEntity(appId, versionId, hEntityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeleteHierarchicalEntity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **hEntityId** | **UUID**| The hierarchical entity extractor ID. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted entity. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeleteHierarchicalEntityChild"></a>
# **modelDeleteHierarchicalEntityChild**
> OperationStatus modelDeleteHierarchicalEntityChild(appId, versionId, hEntityId, hChildId)



Deletes a hierarchical entity extractor child in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID hEntityId = UUID.randomUUID(); // UUID | The hierarchical entity extractor ID.
    UUID hChildId = UUID.randomUUID(); // UUID | The hierarchical entity extractor child ID.
    try {
      OperationStatus result = apiInstance.modelDeleteHierarchicalEntityChild(appId, versionId, hEntityId, hChildId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeleteHierarchicalEntityChild");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **hEntityId** | **UUID**| The hierarchical entity extractor ID. | |
| **hChildId** | **UUID**| The hierarchical entity extractor child ID. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted entity. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeleteHierarchicalEntityRole"></a>
# **modelDeleteHierarchicalEntityRole**
> OperationStatus modelDeleteHierarchicalEntityRole(appId, versionId, hEntityId, roleId)

Delete a role for a given hierarchical role in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID hEntityId = UUID.randomUUID(); // UUID | The hierarchical entity extractor ID.
    UUID roleId = UUID.randomUUID(); // UUID | The entity role Id.
    try {
      OperationStatus result = apiInstance.modelDeleteHierarchicalEntityRole(appId, versionId, hEntityId, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeleteHierarchicalEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **hEntityId** | **UUID**| The hierarchical entity extractor ID. | |
| **roleId** | **UUID**| The entity role Id. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully operation. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeleteIntent"></a>
# **modelDeleteIntent**
> OperationStatus modelDeleteIntent(appId, versionId, intentId, deleteUtterances)



Deletes an intent from a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID intentId = UUID.randomUUID(); // UUID | The intent classifier ID.
    Boolean deleteUtterances = false; // Boolean | If true, deletes the intent's example utterances. If false, moves the example utterances to the None intent. The default value is false.
    try {
      OperationStatus result = apiInstance.modelDeleteIntent(appId, versionId, intentId, deleteUtterances);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeleteIntent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **intentId** | **UUID**| The intent classifier ID. | |
| **deleteUtterances** | **Boolean**| If true, deletes the intent&#39;s example utterances. If false, moves the example utterances to the None intent. The default value is false. | [optional] [default to false] |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeletePatternAnyEntityModel"></a>
# **modelDeletePatternAnyEntityModel**
> OperationStatus modelDeletePatternAnyEntityModel(appId, versionId, entityId)

Deletes a Pattern.Any entity extractor from a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The Pattern.Any entity extractor ID.
    try {
      OperationStatus result = apiInstance.modelDeletePatternAnyEntityModel(appId, versionId, entityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeletePatternAnyEntityModel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The Pattern.Any entity extractor ID. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully operation. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeletePatternAnyEntityRole"></a>
# **modelDeletePatternAnyEntityRole**
> OperationStatus modelDeletePatternAnyEntityRole(appId, versionId, entityId, roleId)

Delete a role for a given Pattern.any entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | The entity role Id.
    try {
      OperationStatus result = apiInstance.modelDeletePatternAnyEntityRole(appId, versionId, entityId, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeletePatternAnyEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity ID. | |
| **roleId** | **UUID**| The entity role Id. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully operation. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeletePrebuilt"></a>
# **modelDeletePrebuilt**
> OperationStatus modelDeletePrebuilt(appId, versionId, prebuiltId)



Deletes a prebuilt entity extractor from a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID prebuiltId = UUID.randomUUID(); // UUID | The prebuilt entity extractor ID.
    try {
      OperationStatus result = apiInstance.modelDeletePrebuilt(appId, versionId, prebuiltId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeletePrebuilt");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **prebuiltId** | **UUID**| The prebuilt entity extractor ID. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeletePrebuiltEntityRole"></a>
# **modelDeletePrebuiltEntityRole**
> OperationStatus modelDeletePrebuiltEntityRole(appId, versionId, entityId, roleId)

Delete a role in a prebuilt entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | The entity role Id.
    try {
      OperationStatus result = apiInstance.modelDeletePrebuiltEntityRole(appId, versionId, entityId, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeletePrebuiltEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity ID. | |
| **roleId** | **UUID**| The entity role Id. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully operation. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeleteRegexEntityModel"></a>
# **modelDeleteRegexEntityModel**
> OperationStatus modelDeleteRegexEntityModel(appId, versionId, regexEntityId)

Deletes a regular expression entity from a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID regexEntityId = UUID.randomUUID(); // UUID | The regular expression entity extractor ID.
    try {
      OperationStatus result = apiInstance.modelDeleteRegexEntityModel(appId, versionId, regexEntityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeleteRegexEntityModel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **regexEntityId** | **UUID**| The regular expression entity extractor ID. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully operation. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeleteRegexEntityRole"></a>
# **modelDeleteRegexEntityRole**
> OperationStatus modelDeleteRegexEntityRole(appId, versionId, entityId, roleId)

Delete a role for a given regular expression in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | The entity role Id.
    try {
      OperationStatus result = apiInstance.modelDeleteRegexEntityRole(appId, versionId, entityId, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeleteRegexEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity ID. | |
| **roleId** | **UUID**| The entity role Id. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully operation. |  -  |
| **0** | Error Response. |  -  |

<a id="modelDeleteSubList"></a>
# **modelDeleteSubList**
> OperationStatus modelDeleteSubList(appId, versionId, clEntityId, subListId)



Deletes a sublist of a specific list entity model from a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID clEntityId = UUID.randomUUID(); // UUID | The list entity extractor ID.
    Long subListId = 56L; // Long | The sublist ID.
    try {
      OperationStatus result = apiInstance.modelDeleteSubList(appId, versionId, clEntityId, subListId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelDeleteSubList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **clEntityId** | **UUID**| The list entity extractor ID. | |
| **subListId** | **Long**| The sublist ID. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted sublist. |  -  |
| **0** | Error Response. |  -  |

<a id="modelExamples"></a>
# **modelExamples**
> List&lt;LabelTextObject&gt; modelExamples(appId, versionId, modelId, skip, take)



Gets the example utterances for the given intent or entity model in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    String modelId = "modelId_example"; // String | The ID (GUID) of the model.
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<LabelTextObject> result = apiInstance.modelExamples(appId, versionId, modelId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelExamples");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **modelId** | **String**| The ID (GUID) of the model. | |
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;LabelTextObject&gt;**](LabelTextObject.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of example utterances for the model. |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetClosedList"></a>
# **modelGetClosedList**
> ClosedListEntityExtractor modelGetClosedList(appId, versionId, clEntityId)



Gets information about a list entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID clEntityId = UUID.randomUUID(); // UUID | The list model ID.
    try {
      ClosedListEntityExtractor result = apiInstance.modelGetClosedList(appId, versionId, clEntityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetClosedList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **clEntityId** | **UUID**| The list model ID. | |

### Return type

[**ClosedListEntityExtractor**](ClosedListEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list model info. |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetClosedListEntityRole"></a>
# **modelGetClosedListEntityRole**
> EntityRole modelGetClosedListEntityRole(appId, versionId, entityId, roleId)

Get one role for a given list entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | entity role ID.
    try {
      EntityRole result = apiInstance.modelGetClosedListEntityRole(appId, versionId, entityId, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetClosedListEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| entity ID. | |
| **roleId** | **UUID**| entity role ID. | |

### Return type

[**EntityRole**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An entity role |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetCompositeEntity"></a>
# **modelGetCompositeEntity**
> CompositeEntityExtractor modelGetCompositeEntity(appId, versionId, cEntityId)



Gets information about a composite entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID cEntityId = UUID.randomUUID(); // UUID | The composite entity extractor ID.
    try {
      CompositeEntityExtractor result = apiInstance.modelGetCompositeEntity(appId, versionId, cEntityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetCompositeEntity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **cEntityId** | **UUID**| The composite entity extractor ID. | |

### Return type

[**CompositeEntityExtractor**](CompositeEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The composite entity model info. |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetCompositeEntityRole"></a>
# **modelGetCompositeEntityRole**
> EntityRole modelGetCompositeEntityRole(appId, versionId, cEntityId, roleId)

Get one role for a given composite entity in a version of the application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID cEntityId = UUID.randomUUID(); // UUID | The composite entity extractor ID.
    UUID roleId = UUID.randomUUID(); // UUID | entity role ID.
    try {
      EntityRole result = apiInstance.modelGetCompositeEntityRole(appId, versionId, cEntityId, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetCompositeEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **cEntityId** | **UUID**| The composite entity extractor ID. | |
| **roleId** | **UUID**| entity role ID. | |

### Return type

[**EntityRole**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An entity role |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetCustomEntityRole"></a>
# **modelGetCustomEntityRole**
> EntityRole modelGetCustomEntityRole(appId, versionId, entityId, roleId)

Get one role for a given prebuilt entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | entity role ID.
    try {
      EntityRole result = apiInstance.modelGetCustomEntityRole(appId, versionId, entityId, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetCustomEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| entity ID. | |
| **roleId** | **UUID**| entity role ID. | |

### Return type

[**EntityRole**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An entity role |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetEntity"></a>
# **modelGetEntity**
> EntityExtractor modelGetEntity(appId, versionId, entityId)



Gets information about an entity model in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity extractor ID.
    try {
      EntityExtractor result = apiInstance.modelGetEntity(appId, versionId, entityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetEntity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity extractor ID. | |

### Return type

[**EntityExtractor**](EntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An entity model info. |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetEntityRole"></a>
# **modelGetEntityRole**
> EntityRole modelGetEntityRole(appId, versionId, entityId, roleId)

Get one role for a given entity in a version of the application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | entity role ID.
    try {
      EntityRole result = apiInstance.modelGetEntityRole(appId, versionId, entityId, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| entity ID. | |
| **roleId** | **UUID**| entity role ID. | |

### Return type

[**EntityRole**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An entity role |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetExplicitList"></a>
# **modelGetExplicitList**
> List&lt;ExplicitListItem&gt; modelGetExplicitList(appId, versionId, entityId)

Get the explicit (exception) list of the pattern.any entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The Pattern.Any entity id.
    try {
      List<ExplicitListItem> result = apiInstance.modelGetExplicitList(appId, versionId, entityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetExplicitList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The Pattern.Any entity id. | |

### Return type

[**List&lt;ExplicitListItem&gt;**](ExplicitListItem.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of the explicit list items |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetExplicitListItem"></a>
# **modelGetExplicitListItem**
> ExplicitListItem modelGetExplicitListItem(appId, versionId, entityId, itemId)

Get the explicit (exception) list of the pattern.any entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The Pattern.Any entity Id.
    Long itemId = 56L; // Long | The explicit list item Id.
    try {
      ExplicitListItem result = apiInstance.modelGetExplicitListItem(appId, versionId, entityId, itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetExplicitListItem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The Pattern.Any entity Id. | |
| **itemId** | **Long**| The explicit list item Id. | |

### Return type

[**ExplicitListItem**](ExplicitListItem.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An explicit list item info. |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetHierarchicalEntity"></a>
# **modelGetHierarchicalEntity**
> HierarchicalEntityExtractor modelGetHierarchicalEntity(appId, versionId, hEntityId)



Gets information about a hierarchical entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID hEntityId = UUID.randomUUID(); // UUID | The hierarchical entity extractor ID.
    try {
      HierarchicalEntityExtractor result = apiInstance.modelGetHierarchicalEntity(appId, versionId, hEntityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetHierarchicalEntity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **hEntityId** | **UUID**| The hierarchical entity extractor ID. | |

### Return type

[**HierarchicalEntityExtractor**](HierarchicalEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A hierarchical entity model info. |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetHierarchicalEntityChild"></a>
# **modelGetHierarchicalEntityChild**
> HierarchicalChildEntity modelGetHierarchicalEntityChild(appId, versionId, hEntityId, hChildId)



Gets information about the child&#39;s model contained in an hierarchical entity child model in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID hEntityId = UUID.randomUUID(); // UUID | The hierarchical entity extractor ID.
    UUID hChildId = UUID.randomUUID(); // UUID | The hierarchical entity extractor child ID.
    try {
      HierarchicalChildEntity result = apiInstance.modelGetHierarchicalEntityChild(appId, versionId, hEntityId, hChildId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetHierarchicalEntityChild");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **hEntityId** | **UUID**| The hierarchical entity extractor ID. | |
| **hChildId** | **UUID**| The hierarchical entity extractor child ID. | |

### Return type

[**HierarchicalChildEntity**](HierarchicalChildEntity.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The hierarchical entity child model info. |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetHierarchicalEntityRole"></a>
# **modelGetHierarchicalEntityRole**
> EntityRole modelGetHierarchicalEntityRole(appId, versionId, hEntityId, roleId)

Get one role for a given hierarchical entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID hEntityId = UUID.randomUUID(); // UUID | The hierarchical entity extractor ID.
    UUID roleId = UUID.randomUUID(); // UUID | entity role ID.
    try {
      EntityRole result = apiInstance.modelGetHierarchicalEntityRole(appId, versionId, hEntityId, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetHierarchicalEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **hEntityId** | **UUID**| The hierarchical entity extractor ID. | |
| **roleId** | **UUID**| entity role ID. | |

### Return type

[**EntityRole**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An entity role |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetIntent"></a>
# **modelGetIntent**
> IntentClassifier modelGetIntent(appId, versionId, intentId)



Gets information about the intent model in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID intentId = UUID.randomUUID(); // UUID | The intent classifier ID.
    try {
      IntentClassifier result = apiInstance.modelGetIntent(appId, versionId, intentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetIntent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **intentId** | **UUID**| The intent classifier ID. | |

### Return type

[**IntentClassifier**](IntentClassifier.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An intent model info. |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetPatternAnyEntityInfo"></a>
# **modelGetPatternAnyEntityInfo**
> PatternAnyEntityExtractor modelGetPatternAnyEntityInfo(appId, versionId, entityId)

Gets information about the Pattern.Any model in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity extractor ID.
    try {
      PatternAnyEntityExtractor result = apiInstance.modelGetPatternAnyEntityInfo(appId, versionId, entityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetPatternAnyEntityInfo");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity extractor ID. | |

### Return type

[**PatternAnyEntityExtractor**](PatternAnyEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A regular expression entity model info. |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetPatternAnyEntityRole"></a>
# **modelGetPatternAnyEntityRole**
> EntityRole modelGetPatternAnyEntityRole(appId, versionId, entityId, roleId)

Get one role for a given Pattern.any entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | entity role ID.
    try {
      EntityRole result = apiInstance.modelGetPatternAnyEntityRole(appId, versionId, entityId, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetPatternAnyEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| entity ID. | |
| **roleId** | **UUID**| entity role ID. | |

### Return type

[**EntityRole**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An entity role |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetPrebuilt"></a>
# **modelGetPrebuilt**
> PrebuiltEntityExtractor modelGetPrebuilt(appId, versionId, prebuiltId)



Gets information about a prebuilt entity model in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID prebuiltId = UUID.randomUUID(); // UUID | The prebuilt entity extractor ID.
    try {
      PrebuiltEntityExtractor result = apiInstance.modelGetPrebuilt(appId, versionId, prebuiltId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetPrebuilt");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **prebuiltId** | **UUID**| The prebuilt entity extractor ID. | |

### Return type

[**PrebuiltEntityExtractor**](PrebuiltEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A prebuilt entity models info. |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetPrebuiltEntityRole"></a>
# **modelGetPrebuiltEntityRole**
> EntityRole modelGetPrebuiltEntityRole(appId, versionId, entityId, roleId)

Get one role for a given prebuilt entity in a version of the application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | entity role ID.
    try {
      EntityRole result = apiInstance.modelGetPrebuiltEntityRole(appId, versionId, entityId, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetPrebuiltEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| entity ID. | |
| **roleId** | **UUID**| entity role ID. | |

### Return type

[**EntityRole**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An entity role |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetRegexEntityEntityInfo"></a>
# **modelGetRegexEntityEntityInfo**
> RegexEntityExtractor modelGetRegexEntityEntityInfo(appId, versionId, regexEntityId)

Gets information about a regular expression entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID regexEntityId = UUID.randomUUID(); // UUID | The regular expression entity model ID.
    try {
      RegexEntityExtractor result = apiInstance.modelGetRegexEntityEntityInfo(appId, versionId, regexEntityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetRegexEntityEntityInfo");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **regexEntityId** | **UUID**| The regular expression entity model ID. | |

### Return type

[**RegexEntityExtractor**](RegexEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A regular expression entity model info. |  -  |
| **0** | Error Response. |  -  |

<a id="modelGetRegexEntityRole"></a>
# **modelGetRegexEntityRole**
> EntityRole modelGetRegexEntityRole(appId, versionId, entityId, roleId)

Get one role for a given regular expression entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | entity role ID.
    try {
      EntityRole result = apiInstance.modelGetRegexEntityRole(appId, versionId, entityId, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelGetRegexEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| entity ID. | |
| **roleId** | **UUID**| entity role ID. | |

### Return type

[**EntityRole**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An entity role |  -  |
| **0** | Error Response. |  -  |

<a id="modelListClosedListEntityRoles"></a>
# **modelListClosedListEntityRoles**
> List&lt;EntityRole&gt; modelListClosedListEntityRoles(appId, versionId, entityId)

Get all roles for a list entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | entity Id
    try {
      List<EntityRole> result = apiInstance.modelListClosedListEntityRoles(appId, versionId, entityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListClosedListEntityRoles");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| entity Id | |

### Return type

[**List&lt;EntityRole&gt;**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of the entity roles |  -  |
| **0** | Error Response. |  -  |

<a id="modelListClosedLists"></a>
# **modelListClosedLists**
> List&lt;ClosedListEntityExtractor&gt; modelListClosedLists(appId, versionId, skip, take)



Gets information about all the list entity models in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<ClosedListEntityExtractor> result = apiInstance.modelListClosedLists(appId, versionId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListClosedLists");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;ClosedListEntityExtractor&gt;**](ClosedListEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of list entity model infos. |  -  |
| **0** | Error Response. |  -  |

<a id="modelListCompositeEntities"></a>
# **modelListCompositeEntities**
> List&lt;CompositeEntityExtractor&gt; modelListCompositeEntities(appId, versionId, skip, take)



Gets information about all the composite entity models in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<CompositeEntityExtractor> result = apiInstance.modelListCompositeEntities(appId, versionId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListCompositeEntities");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;CompositeEntityExtractor&gt;**](CompositeEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of composite entity model infos. |  -  |
| **0** | Error Response. |  -  |

<a id="modelListCompositeEntityRoles"></a>
# **modelListCompositeEntityRoles**
> List&lt;EntityRole&gt; modelListCompositeEntityRoles(appId, versionId, cEntityId)

Get all roles for a composite entity in a version of the application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID cEntityId = UUID.randomUUID(); // UUID | The composite entity extractor ID.
    try {
      List<EntityRole> result = apiInstance.modelListCompositeEntityRoles(appId, versionId, cEntityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListCompositeEntityRoles");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **cEntityId** | **UUID**| The composite entity extractor ID. | |

### Return type

[**List&lt;EntityRole&gt;**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of the entity roles |  -  |
| **0** | Error Response. |  -  |

<a id="modelListCustomPrebuiltEntities"></a>
# **modelListCustomPrebuiltEntities**
> List&lt;EntityExtractor&gt; modelListCustomPrebuiltEntities(appId, versionId)



Gets all prebuilt entities used in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    try {
      List<EntityExtractor> result = apiInstance.modelListCustomPrebuiltEntities(appId, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListCustomPrebuiltEntities");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |

### Return type

[**List&lt;EntityExtractor&gt;**](EntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of all prebuilt entities and their representations. |  -  |
| **0** | Error Response. |  -  |

<a id="modelListCustomPrebuiltEntityRoles"></a>
# **modelListCustomPrebuiltEntityRoles**
> List&lt;EntityRole&gt; modelListCustomPrebuiltEntityRoles(appId, versionId, entityId)

Get all roles for a prebuilt entity in a version of the application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | entity Id
    try {
      List<EntityRole> result = apiInstance.modelListCustomPrebuiltEntityRoles(appId, versionId, entityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListCustomPrebuiltEntityRoles");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| entity Id | |

### Return type

[**List&lt;EntityRole&gt;**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of the entity roles |  -  |
| **0** | Error Response. |  -  |

<a id="modelListCustomPrebuiltIntents"></a>
# **modelListCustomPrebuiltIntents**
> List&lt;IntentClassifier&gt; modelListCustomPrebuiltIntents(appId, versionId)



Gets information about customizable prebuilt intents added to a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    try {
      List<IntentClassifier> result = apiInstance.modelListCustomPrebuiltIntents(appId, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListCustomPrebuiltIntents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |

### Return type

[**List&lt;IntentClassifier&gt;**](IntentClassifier.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of all customizable prebuilt intents and their representations in a version of the application. |  -  |
| **0** | Error Response. |  -  |

<a id="modelListCustomPrebuiltModels"></a>
# **modelListCustomPrebuiltModels**
> List&lt;CustomPrebuiltModel&gt; modelListCustomPrebuiltModels(appId, versionId)



Gets all prebuilt intent and entity model information used in a version of this application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    try {
      List<CustomPrebuiltModel> result = apiInstance.modelListCustomPrebuiltModels(appId, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListCustomPrebuiltModels");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |

### Return type

[**List&lt;CustomPrebuiltModel&gt;**](CustomPrebuiltModel.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of all prebuilt models and their representations. |  -  |
| **0** | Error Response. |  -  |

<a id="modelListEntities"></a>
# **modelListEntities**
> List&lt;EntityExtractor&gt; modelListEntities(appId, versionId, skip, take)



Gets information about all the simple entity models in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<EntityExtractor> result = apiInstance.modelListEntities(appId, versionId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListEntities");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;EntityExtractor&gt;**](EntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of entity model infos. |  -  |
| **0** | Error Response. |  -  |

<a id="modelListEntityRoles"></a>
# **modelListEntityRoles**
> List&lt;EntityRole&gt; modelListEntityRoles(appId, versionId, entityId)

Get all roles for an entity in a version of the application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | entity Id
    try {
      List<EntityRole> result = apiInstance.modelListEntityRoles(appId, versionId, entityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListEntityRoles");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| entity Id | |

### Return type

[**List&lt;EntityRole&gt;**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of the entity roles |  -  |
| **0** | Error Response. |  -  |

<a id="modelListEntitySuggestions"></a>
# **modelListEntitySuggestions**
> List&lt;EntitiesSuggestionExample&gt; modelListEntitySuggestions(appId, versionId, entityId, take)



Get suggested example utterances that would improve the accuracy of the entity model in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The target entity extractor model to enhance.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<EntitiesSuggestionExample> result = apiInstance.modelListEntitySuggestions(appId, versionId, entityId, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListEntitySuggestions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The target entity extractor model to enhance. | |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;EntitiesSuggestionExample&gt;**](EntitiesSuggestionExample.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If there&#39;s no trained entity model, nothing is returned in the response. If there&#39;s a trained model and active learning finds any relevant queries, they are returned with the entity model predictions. If there&#39;s a trained model but active learning didn&#39;t find any relevant queries, an empty list is returned in the response. |  -  |
| **0** | Error Response. |  -  |

<a id="modelListHierarchicalEntities"></a>
# **modelListHierarchicalEntities**
> List&lt;HierarchicalEntityExtractor&gt; modelListHierarchicalEntities(appId, versionId, skip, take)



Gets information about all the hierarchical entity models in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<HierarchicalEntityExtractor> result = apiInstance.modelListHierarchicalEntities(appId, versionId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListHierarchicalEntities");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;HierarchicalEntityExtractor&gt;**](HierarchicalEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of hierarchical entity model infos. |  -  |
| **0** | Error Response. |  -  |

<a id="modelListHierarchicalEntityRoles"></a>
# **modelListHierarchicalEntityRoles**
> List&lt;EntityRole&gt; modelListHierarchicalEntityRoles(appId, versionId, hEntityId)

Get all roles for a hierarchical entity in a version of the application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID hEntityId = UUID.randomUUID(); // UUID | The hierarchical entity extractor ID.
    try {
      List<EntityRole> result = apiInstance.modelListHierarchicalEntityRoles(appId, versionId, hEntityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListHierarchicalEntityRoles");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **hEntityId** | **UUID**| The hierarchical entity extractor ID. | |

### Return type

[**List&lt;EntityRole&gt;**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of the entity roles |  -  |
| **0** | Error Response. |  -  |

<a id="modelListIntentSuggestions"></a>
# **modelListIntentSuggestions**
> List&lt;IntentsSuggestionExample&gt; modelListIntentSuggestions(appId, versionId, intentId, take)



Suggests example utterances that would improve the accuracy of the intent model in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID intentId = UUID.randomUUID(); // UUID | The intent classifier ID.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<IntentsSuggestionExample> result = apiInstance.modelListIntentSuggestions(appId, versionId, intentId, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListIntentSuggestions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **intentId** | **UUID**| The intent classifier ID. | |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;IntentsSuggestionExample&gt;**](IntentsSuggestionExample.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If there&#39;s no trained intent model, nothing is returned in the response. If there&#39;s a trained model and active learning finds any relevant queries, they are returned with the intent model predictions. If there&#39;s a trained model but active learning didn&#39;t find any relevant queries, an empty list is returned in the response. |  -  |
| **0** | Error Response. |  -  |

<a id="modelListIntents"></a>
# **modelListIntents**
> List&lt;IntentClassifier&gt; modelListIntents(appId, versionId, skip, take)



Gets information about the intent models in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<IntentClassifier> result = apiInstance.modelListIntents(appId, versionId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListIntents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;IntentClassifier&gt;**](IntentClassifier.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of intent model infos. |  -  |
| **0** | Error Response. |  -  |

<a id="modelListModels"></a>
# **modelListModels**
> List&lt;ModelInfoResponse&gt; modelListModels(appId, versionId, skip, take)



Gets information about all the intent and entity models in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<ModelInfoResponse> result = apiInstance.modelListModels(appId, versionId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListModels");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;ModelInfoResponse&gt;**](ModelInfoResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of application model infos. |  -  |
| **0** | Error Response. |  -  |

<a id="modelListPatternAnyEntityInfos"></a>
# **modelListPatternAnyEntityInfos**
> List&lt;PatternAnyEntityExtractor&gt; modelListPatternAnyEntityInfos(appId, versionId, skip, take)

Get information about the Pattern.Any entity models in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<PatternAnyEntityExtractor> result = apiInstance.modelListPatternAnyEntityInfos(appId, versionId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListPatternAnyEntityInfos");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;PatternAnyEntityExtractor&gt;**](PatternAnyEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Pattern.Any entity model infos. |  -  |
| **0** | Error Response. |  -  |

<a id="modelListPatternAnyEntityRoles"></a>
# **modelListPatternAnyEntityRoles**
> List&lt;EntityRole&gt; modelListPatternAnyEntityRoles(appId, versionId, entityId)

Get all roles for a Pattern.any entity in a version of the application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | entity Id
    try {
      List<EntityRole> result = apiInstance.modelListPatternAnyEntityRoles(appId, versionId, entityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListPatternAnyEntityRoles");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| entity Id | |

### Return type

[**List&lt;EntityRole&gt;**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of the entity roles |  -  |
| **0** | Error Response. |  -  |

<a id="modelListPrebuiltEntities"></a>
# **modelListPrebuiltEntities**
> List&lt;AvailablePrebuiltEntityModel&gt; modelListPrebuiltEntities(appId, versionId)



Gets all the available prebuilt entities in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    try {
      List<AvailablePrebuiltEntityModel> result = apiInstance.modelListPrebuiltEntities(appId, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListPrebuiltEntities");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |

### Return type

[**List&lt;AvailablePrebuiltEntityModel&gt;**](AvailablePrebuiltEntityModel.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of the possible prebuilt entity extractors. |  -  |
| **0** | Error Response. |  -  |

<a id="modelListPrebuiltEntityRoles"></a>
# **modelListPrebuiltEntityRoles**
> List&lt;EntityRole&gt; modelListPrebuiltEntityRoles(appId, versionId, entityId)

Get a prebuilt entity&#39;s roles in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | entity Id
    try {
      List<EntityRole> result = apiInstance.modelListPrebuiltEntityRoles(appId, versionId, entityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListPrebuiltEntityRoles");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| entity Id | |

### Return type

[**List&lt;EntityRole&gt;**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of the entity roles |  -  |
| **0** | Error Response. |  -  |

<a id="modelListPrebuilts"></a>
# **modelListPrebuilts**
> List&lt;PrebuiltEntityExtractor&gt; modelListPrebuilts(appId, versionId, skip, take)



Gets information about all the prebuilt entities in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<PrebuiltEntityExtractor> result = apiInstance.modelListPrebuilts(appId, versionId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListPrebuilts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;PrebuiltEntityExtractor&gt;**](PrebuiltEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of prebuilt entity models infos. |  -  |
| **0** | Error Response. |  -  |

<a id="modelListRegexEntityInfos"></a>
# **modelListRegexEntityInfos**
> List&lt;RegexEntityExtractor&gt; modelListRegexEntityInfos(appId, versionId, skip, take)

Gets information about the regular expression entity models in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<RegexEntityExtractor> result = apiInstance.modelListRegexEntityInfos(appId, versionId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListRegexEntityInfos");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;RegexEntityExtractor&gt;**](RegexEntityExtractor.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of regular expression entity model infos. |  -  |
| **0** | Error Response. |  -  |

<a id="modelListRegexEntityRoles"></a>
# **modelListRegexEntityRoles**
> List&lt;EntityRole&gt; modelListRegexEntityRoles(appId, versionId, entityId)

Get all roles for a regular expression entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | entity Id
    try {
      List<EntityRole> result = apiInstance.modelListRegexEntityRoles(appId, versionId, entityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelListRegexEntityRoles");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| entity Id | |

### Return type

[**List&lt;EntityRole&gt;**](EntityRole.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of the entity roles |  -  |
| **0** | Error Response. |  -  |

<a id="modelPatchClosedList"></a>
# **modelPatchClosedList**
> OperationStatus modelPatchClosedList(appId, versionId, clEntityId, closedListModelPatchObject)



Adds a batch of sublists to an existing list entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID clEntityId = UUID.randomUUID(); // UUID | The list entity model ID.
    ClosedListModelPatchObject closedListModelPatchObject = new ClosedListModelPatchObject(); // ClosedListModelPatchObject | A words list batch.
    try {
      OperationStatus result = apiInstance.modelPatchClosedList(appId, versionId, clEntityId, closedListModelPatchObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelPatchClosedList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **clEntityId** | **UUID**| The list entity model ID. | |
| **closedListModelPatchObject** | [**ClosedListModelPatchObject**](ClosedListModelPatchObject.md)| A words list batch. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully added sublists to the list entity. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdateClosedList"></a>
# **modelUpdateClosedList**
> OperationStatus modelUpdateClosedList(appId, versionId, clEntityId, closedListModelUpdateObject)



Updates the list entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID clEntityId = UUID.randomUUID(); // UUID | The list model ID.
    ClosedListModelUpdateObject closedListModelUpdateObject = new ClosedListModelUpdateObject(); // ClosedListModelUpdateObject | The new list entity name and words list.
    try {
      OperationStatus result = apiInstance.modelUpdateClosedList(appId, versionId, clEntityId, closedListModelUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdateClosedList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **clEntityId** | **UUID**| The list model ID. | |
| **closedListModelUpdateObject** | [**ClosedListModelUpdateObject**](ClosedListModelUpdateObject.md)| The new list entity name and words list. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated list entity name and words list. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdateClosedListEntityRole"></a>
# **modelUpdateClosedListEntityRole**
> OperationStatus modelUpdateClosedListEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject)

Update a role for a given list entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | The entity role ID.
    EntityRoleUpdateObject entityRoleUpdateObject = new EntityRoleUpdateObject(); // EntityRoleUpdateObject | The new entity role.
    try {
      OperationStatus result = apiInstance.modelUpdateClosedListEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdateClosedListEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity ID. | |
| **roleId** | **UUID**| The entity role ID. | |
| **entityRoleUpdateObject** | [**EntityRoleUpdateObject**](EntityRoleUpdateObject.md)| The new entity role. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the entity role. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdateCompositeEntity"></a>
# **modelUpdateCompositeEntity**
> OperationStatus modelUpdateCompositeEntity(appId, versionId, cEntityId, compositeModelUpdateObject)



Updates a composite entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID cEntityId = UUID.randomUUID(); // UUID | The composite entity extractor ID.
    CompositeEntityModel compositeModelUpdateObject = new CompositeEntityModel(); // CompositeEntityModel | A model object containing the new entity extractor name and children.
    try {
      OperationStatus result = apiInstance.modelUpdateCompositeEntity(appId, versionId, cEntityId, compositeModelUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdateCompositeEntity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **cEntityId** | **UUID**| The composite entity extractor ID. | |
| **compositeModelUpdateObject** | [**CompositeEntityModel**](CompositeEntityModel.md)| A model object containing the new entity extractor name and children. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated composite entity. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdateCompositeEntityRole"></a>
# **modelUpdateCompositeEntityRole**
> OperationStatus modelUpdateCompositeEntityRole(appId, versionId, cEntityId, roleId, entityRoleUpdateObject)

Update a role for a given composite entity in a version of the application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID cEntityId = UUID.randomUUID(); // UUID | The composite entity extractor ID.
    UUID roleId = UUID.randomUUID(); // UUID | The entity role ID.
    EntityRoleUpdateObject entityRoleUpdateObject = new EntityRoleUpdateObject(); // EntityRoleUpdateObject | The new entity role.
    try {
      OperationStatus result = apiInstance.modelUpdateCompositeEntityRole(appId, versionId, cEntityId, roleId, entityRoleUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdateCompositeEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **cEntityId** | **UUID**| The composite entity extractor ID. | |
| **roleId** | **UUID**| The entity role ID. | |
| **entityRoleUpdateObject** | [**EntityRoleUpdateObject**](EntityRoleUpdateObject.md)| The new entity role. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the entity role. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdateCustomPrebuiltEntityRole"></a>
# **modelUpdateCustomPrebuiltEntityRole**
> OperationStatus modelUpdateCustomPrebuiltEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject)

Update a role for a given prebuilt entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | The entity role ID.
    EntityRoleUpdateObject entityRoleUpdateObject = new EntityRoleUpdateObject(); // EntityRoleUpdateObject | The new entity role.
    try {
      OperationStatus result = apiInstance.modelUpdateCustomPrebuiltEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdateCustomPrebuiltEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity ID. | |
| **roleId** | **UUID**| The entity role ID. | |
| **entityRoleUpdateObject** | [**EntityRoleUpdateObject**](EntityRoleUpdateObject.md)| The new entity role. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the entity role. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdateEntity"></a>
# **modelUpdateEntity**
> OperationStatus modelUpdateEntity(appId, versionId, entityId, modelUpdateObject)



Updates the name of an entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity extractor ID.
    ModelUpdateObject modelUpdateObject = new ModelUpdateObject(); // ModelUpdateObject | A model object containing the new entity extractor name.
    try {
      OperationStatus result = apiInstance.modelUpdateEntity(appId, versionId, entityId, modelUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdateEntity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity extractor ID. | |
| **modelUpdateObject** | [**ModelUpdateObject**](ModelUpdateObject.md)| A model object containing the new entity extractor name. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated entity extractor name. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdateEntityRole"></a>
# **modelUpdateEntityRole**
> OperationStatus modelUpdateEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject)

Update a role for a given entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | The entity role ID.
    EntityRoleUpdateObject entityRoleUpdateObject = new EntityRoleUpdateObject(); // EntityRoleUpdateObject | The new entity role.
    try {
      OperationStatus result = apiInstance.modelUpdateEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdateEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity ID. | |
| **roleId** | **UUID**| The entity role ID. | |
| **entityRoleUpdateObject** | [**EntityRoleUpdateObject**](EntityRoleUpdateObject.md)| The new entity role. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the entity role. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdateExplicitListItem"></a>
# **modelUpdateExplicitListItem**
> OperationStatus modelUpdateExplicitListItem(appId, versionId, entityId, itemId, item)

Updates an explicit (exception) list item for a Pattern.Any entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The Pattern.Any entity extractor ID.
    Long itemId = 56L; // Long | The explicit list item ID.
    ExplicitListItemUpdateObject item = new ExplicitListItemUpdateObject(); // ExplicitListItemUpdateObject | The new explicit list item.
    try {
      OperationStatus result = apiInstance.modelUpdateExplicitListItem(appId, versionId, entityId, itemId, item);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdateExplicitListItem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The Pattern.Any entity extractor ID. | |
| **itemId** | **Long**| The explicit list item ID. | |
| **item** | [**ExplicitListItemUpdateObject**](ExplicitListItemUpdateObject.md)| The new explicit list item. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the explicit list item. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdateHierarchicalEntity"></a>
# **modelUpdateHierarchicalEntity**
> OperationStatus modelUpdateHierarchicalEntity(appId, versionId, hEntityId, hierarchicalModelUpdateObject)



Updates the name and children of a hierarchical entity model in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID hEntityId = UUID.randomUUID(); // UUID | The hierarchical entity extractor ID.
    HierarchicalEntityModel hierarchicalModelUpdateObject = new HierarchicalEntityModel(); // HierarchicalEntityModel | Model containing names of the children of the hierarchical entity.
    try {
      OperationStatus result = apiInstance.modelUpdateHierarchicalEntity(appId, versionId, hEntityId, hierarchicalModelUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdateHierarchicalEntity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **hEntityId** | **UUID**| The hierarchical entity extractor ID. | |
| **hierarchicalModelUpdateObject** | [**HierarchicalEntityModel**](HierarchicalEntityModel.md)| Model containing names of the children of the hierarchical entity. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdateHierarchicalEntityChild"></a>
# **modelUpdateHierarchicalEntityChild**
> OperationStatus modelUpdateHierarchicalEntityChild(appId, versionId, hEntityId, hChildId, hierarchicalChildModelUpdateObject)



Renames a single child in an existing hierarchical entity model in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID hEntityId = UUID.randomUUID(); // UUID | The hierarchical entity extractor ID.
    UUID hChildId = UUID.randomUUID(); // UUID | The hierarchical entity extractor child ID.
    ModelAddCompositeEntityChildRequest hierarchicalChildModelUpdateObject = new ModelAddCompositeEntityChildRequest(); // ModelAddCompositeEntityChildRequest | Model object containing new name of the hierarchical entity child.
    try {
      OperationStatus result = apiInstance.modelUpdateHierarchicalEntityChild(appId, versionId, hEntityId, hChildId, hierarchicalChildModelUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdateHierarchicalEntityChild");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **hEntityId** | **UUID**| The hierarchical entity extractor ID. | |
| **hChildId** | **UUID**| The hierarchical entity extractor child ID. | |
| **hierarchicalChildModelUpdateObject** | [**ModelAddCompositeEntityChildRequest**](ModelAddCompositeEntityChildRequest.md)| Model object containing new name of the hierarchical entity child. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated entity child. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdateHierarchicalEntityRole"></a>
# **modelUpdateHierarchicalEntityRole**
> OperationStatus modelUpdateHierarchicalEntityRole(appId, versionId, hEntityId, roleId, entityRoleUpdateObject)

Update a role for a given hierarchical entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID hEntityId = UUID.randomUUID(); // UUID | The hierarchical entity extractor ID.
    UUID roleId = UUID.randomUUID(); // UUID | The entity role ID.
    EntityRoleUpdateObject entityRoleUpdateObject = new EntityRoleUpdateObject(); // EntityRoleUpdateObject | The new entity role.
    try {
      OperationStatus result = apiInstance.modelUpdateHierarchicalEntityRole(appId, versionId, hEntityId, roleId, entityRoleUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdateHierarchicalEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **hEntityId** | **UUID**| The hierarchical entity extractor ID. | |
| **roleId** | **UUID**| The entity role ID. | |
| **entityRoleUpdateObject** | [**EntityRoleUpdateObject**](EntityRoleUpdateObject.md)| The new entity role. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the entity role. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdateIntent"></a>
# **modelUpdateIntent**
> OperationStatus modelUpdateIntent(appId, versionId, intentId, modelUpdateObject)



Updates the name of an intent in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID intentId = UUID.randomUUID(); // UUID | The intent classifier ID.
    ModelUpdateObject modelUpdateObject = new ModelUpdateObject(); // ModelUpdateObject | A model object containing the new intent name.
    try {
      OperationStatus result = apiInstance.modelUpdateIntent(appId, versionId, intentId, modelUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdateIntent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **intentId** | **UUID**| The intent classifier ID. | |
| **modelUpdateObject** | [**ModelUpdateObject**](ModelUpdateObject.md)| A model object containing the new intent name. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdatePatternAnyEntityModel"></a>
# **modelUpdatePatternAnyEntityModel**
> OperationStatus modelUpdatePatternAnyEntityModel(appId, versionId, entityId, patternAnyUpdateObject)

Updates the name and explicit (exception) list of a Pattern.Any entity model in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The Pattern.Any entity extractor ID.
    PatternAnyModelUpdateObject patternAnyUpdateObject = new PatternAnyModelUpdateObject(); // PatternAnyModelUpdateObject | An object containing the explicit list of the Pattern.Any entity.
    try {
      OperationStatus result = apiInstance.modelUpdatePatternAnyEntityModel(appId, versionId, entityId, patternAnyUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdatePatternAnyEntityModel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The Pattern.Any entity extractor ID. | |
| **patternAnyUpdateObject** | [**PatternAnyModelUpdateObject**](PatternAnyModelUpdateObject.md)| An object containing the explicit list of the Pattern.Any entity. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the Pattern.Any entity extractor. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdatePatternAnyEntityRole"></a>
# **modelUpdatePatternAnyEntityRole**
> OperationStatus modelUpdatePatternAnyEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject)

Update a role for a given Pattern.any entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | The entity role ID.
    EntityRoleUpdateObject entityRoleUpdateObject = new EntityRoleUpdateObject(); // EntityRoleUpdateObject | The new entity role.
    try {
      OperationStatus result = apiInstance.modelUpdatePatternAnyEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdatePatternAnyEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity ID. | |
| **roleId** | **UUID**| The entity role ID. | |
| **entityRoleUpdateObject** | [**EntityRoleUpdateObject**](EntityRoleUpdateObject.md)| The new entity role. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the entity role. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdatePrebuiltEntityRole"></a>
# **modelUpdatePrebuiltEntityRole**
> OperationStatus modelUpdatePrebuiltEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject)

Update a role for a given prebuilt entity in a version of the application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | The entity role ID.
    EntityRoleUpdateObject entityRoleUpdateObject = new EntityRoleUpdateObject(); // EntityRoleUpdateObject | The new entity role.
    try {
      OperationStatus result = apiInstance.modelUpdatePrebuiltEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdatePrebuiltEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity ID. | |
| **roleId** | **UUID**| The entity role ID. | |
| **entityRoleUpdateObject** | [**EntityRoleUpdateObject**](EntityRoleUpdateObject.md)| The new entity role. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the entity role. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdateRegexEntityModel"></a>
# **modelUpdateRegexEntityModel**
> OperationStatus modelUpdateRegexEntityModel(appId, versionId, regexEntityId, regexEntityUpdateObject)

Updates the regular expression entity in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID regexEntityId = UUID.randomUUID(); // UUID | The regular expression entity extractor ID.
    RegexModelUpdateObject regexEntityUpdateObject = new RegexModelUpdateObject(); // RegexModelUpdateObject | An object containing the new entity name and regex pattern.
    try {
      OperationStatus result = apiInstance.modelUpdateRegexEntityModel(appId, versionId, regexEntityId, regexEntityUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdateRegexEntityModel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **regexEntityId** | **UUID**| The regular expression entity extractor ID. | |
| **regexEntityUpdateObject** | [**RegexModelUpdateObject**](RegexModelUpdateObject.md)| An object containing the new entity name and regex pattern. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the regular expression entity extractor. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdateRegexEntityRole"></a>
# **modelUpdateRegexEntityRole**
> OperationStatus modelUpdateRegexEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject)

Update a role for a given regular expression entity in a version of the application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID entityId = UUID.randomUUID(); // UUID | The entity ID.
    UUID roleId = UUID.randomUUID(); // UUID | The entity role ID.
    EntityRoleUpdateObject entityRoleUpdateObject = new EntityRoleUpdateObject(); // EntityRoleUpdateObject | The new entity role.
    try {
      OperationStatus result = apiInstance.modelUpdateRegexEntityRole(appId, versionId, entityId, roleId, entityRoleUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdateRegexEntityRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **entityId** | **UUID**| The entity ID. | |
| **roleId** | **UUID**| The entity role ID. | |
| **entityRoleUpdateObject** | [**EntityRoleUpdateObject**](EntityRoleUpdateObject.md)| The new entity role. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the entity role. |  -  |
| **0** | Error Response. |  -  |

<a id="modelUpdateSubList"></a>
# **modelUpdateSubList**
> OperationStatus modelUpdateSubList(appId, versionId, clEntityId, subListId, wordListBaseUpdateObject)



Updates one of the list entity&#39;s sublists in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID clEntityId = UUID.randomUUID(); // UUID | The list entity extractor ID.
    Long subListId = 56L; // Long | The sublist ID.
    WordListBaseUpdateObject wordListBaseUpdateObject = new WordListBaseUpdateObject(); // WordListBaseUpdateObject | A sublist update object containing the new canonical form and the list of words.
    try {
      OperationStatus result = apiInstance.modelUpdateSubList(appId, versionId, clEntityId, subListId, wordListBaseUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#modelUpdateSubList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **clEntityId** | **UUID**| The list entity extractor ID. | |
| **subListId** | **Long**| The sublist ID. | |
| **wordListBaseUpdateObject** | [**WordListBaseUpdateObject**](WordListBaseUpdateObject.md)| A sublist update object containing the new canonical form and the list of words. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated sublist. |  -  |
| **0** | Error Response. |  -  |

<a id="patternAddPattern"></a>
# **patternAddPattern**
> PatternRuleInfo patternAddPattern(appId, versionId, pattern)

Adds a pattern to a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    PatternRuleCreateObject pattern = new PatternRuleCreateObject(); // PatternRuleCreateObject | The input pattern.
    try {
      PatternRuleInfo result = apiInstance.patternAddPattern(appId, versionId, pattern);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#patternAddPattern");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **pattern** | [**PatternRuleCreateObject**](PatternRuleCreateObject.md)| The input pattern. | |

### Return type

[**PatternRuleInfo**](PatternRuleInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created pattern |  -  |
| **0** | Error Response. |  -  |

<a id="patternBatchAddPatterns"></a>
# **patternBatchAddPatterns**
> List&lt;PatternRuleInfo&gt; patternBatchAddPatterns(appId, versionId, patterns)

Adds a batch of patterns in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    List<PatternRuleCreateObject> patterns = Arrays.asList(); // List<PatternRuleCreateObject> | A JSON array containing patterns.
    try {
      List<PatternRuleInfo> result = apiInstance.patternBatchAddPatterns(appId, versionId, patterns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#patternBatchAddPatterns");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **patterns** | [**List&lt;PatternRuleCreateObject&gt;**](PatternRuleCreateObject.md)| A JSON array containing patterns. | |

### Return type

[**List&lt;PatternRuleInfo&gt;**](PatternRuleInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created patterns |  -  |
| **0** | Error Response. |  -  |

<a id="patternDeletePattern"></a>
# **patternDeletePattern**
> OperationStatus patternDeletePattern(appId, versionId, patternId)

Deletes the pattern with the specified ID from a version of the application..

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID patternId = UUID.randomUUID(); // UUID | The pattern ID.
    try {
      OperationStatus result = apiInstance.patternDeletePattern(appId, versionId, patternId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#patternDeletePattern");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **patternId** | **UUID**| The pattern ID. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully operation. |  -  |
| **0** | Error Response. |  -  |

<a id="patternDeletePatterns"></a>
# **patternDeletePatterns**
> OperationStatus patternDeletePatterns(appId, versionId, patternIds)

Deletes a list of patterns in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    List<UUID> patternIds = Arrays.asList(); // List<UUID> | The patterns IDs.
    try {
      OperationStatus result = apiInstance.patternDeletePatterns(appId, versionId, patternIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#patternDeletePatterns");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **patternIds** | [**List&lt;UUID&gt;**](UUID.md)| The patterns IDs. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully operation. |  -  |
| **0** | Error Response. |  -  |

<a id="patternListIntentPatterns"></a>
# **patternListIntentPatterns**
> List&lt;PatternRuleInfo&gt; patternListIntentPatterns(appId, versionId, intentId, skip, take)

Returns patterns for the specific intent in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID intentId = UUID.randomUUID(); // UUID | The intent classifier ID.
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<PatternRuleInfo> result = apiInstance.patternListIntentPatterns(appId, versionId, intentId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#patternListIntentPatterns");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **intentId** | **UUID**| The intent classifier ID. | |
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;PatternRuleInfo&gt;**](PatternRuleInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved patterns |  -  |
| **0** | Error Response. |  -  |

<a id="patternListPatterns"></a>
# **patternListPatterns**
> List&lt;PatternRuleInfo&gt; patternListPatterns(appId, versionId, skip, take)

Gets patterns in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<PatternRuleInfo> result = apiInstance.patternListPatterns(appId, versionId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#patternListPatterns");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;PatternRuleInfo&gt;**](PatternRuleInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved patterns |  -  |
| **0** | Error Response. |  -  |

<a id="patternUpdatePattern"></a>
# **patternUpdatePattern**
> PatternRuleInfo patternUpdatePattern(appId, versionId, patternId, pattern)

Updates a pattern in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    UUID patternId = UUID.randomUUID(); // UUID | The pattern ID.
    PatternRuleUpdateObject pattern = new PatternRuleUpdateObject(); // PatternRuleUpdateObject | An object representing a pattern.
    try {
      PatternRuleInfo result = apiInstance.patternUpdatePattern(appId, versionId, patternId, pattern);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#patternUpdatePattern");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **patternId** | **UUID**| The pattern ID. | |
| **pattern** | [**PatternRuleUpdateObject**](PatternRuleUpdateObject.md)| An object representing a pattern. | |

### Return type

[**PatternRuleInfo**](PatternRuleInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated pattern |  -  |
| **0** | Error Response. |  -  |

<a id="patternUpdatePatterns"></a>
# **patternUpdatePatterns**
> List&lt;PatternRuleInfo&gt; patternUpdatePatterns(appId, versionId, patterns)

Updates patterns in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    List<PatternRuleUpdateObject> patterns = Arrays.asList(); // List<PatternRuleUpdateObject> | An array represents the patterns.
    try {
      List<PatternRuleInfo> result = apiInstance.patternUpdatePatterns(appId, versionId, patterns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#patternUpdatePatterns");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **patterns** | [**List&lt;PatternRuleUpdateObject&gt;**](PatternRuleUpdateObject.md)| An array represents the patterns. | |

### Return type

[**List&lt;PatternRuleInfo&gt;**](PatternRuleInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated patterns |  -  |
| **0** | Error Response. |  -  |

<a id="permissionsAdd"></a>
# **permissionsAdd**
> OperationStatus permissionsAdd(appId, userToAdd)



Adds a user to the allowed list of users to access this LUIS application. Users are added using their email address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    UserCollaborator userToAdd = new UserCollaborator(); // UserCollaborator | A model containing the user's email address.
    try {
      OperationStatus result = apiInstance.permissionsAdd(appId, userToAdd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#permissionsAdd");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **userToAdd** | [**UserCollaborator**](UserCollaborator.md)| A model containing the user&#39;s email address. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  -  |
| **0** | Error Response. |  -  |

<a id="permissionsDelete"></a>
# **permissionsDelete**
> OperationStatus permissionsDelete(appId, userToDelete)



Removes a user from the allowed list of users to access this LUIS application. Users are removed using their email address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    UserCollaborator userToDelete = new UserCollaborator(); // UserCollaborator | A model containing the user's email address.
    try {
      OperationStatus result = apiInstance.permissionsDelete(appId, userToDelete);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#permissionsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **userToDelete** | [**UserCollaborator**](UserCollaborator.md)| A model containing the user&#39;s email address. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  -  |
| **0** | Error Response. |  -  |

<a id="permissionsList"></a>
# **permissionsList**
> UserAccessList permissionsList(appId)



Gets the list of user emails that have permissions to access your application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    try {
      UserAccessList result = apiInstance.permissionsList(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#permissionsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |

### Return type

[**UserAccessList**](UserAccessList.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list includes a single owner. All collaborators are listed in the emails array. |  -  |
| **0** | Error Response. |  -  |

<a id="permissionsUpdate"></a>
# **permissionsUpdate**
> OperationStatus permissionsUpdate(appId, collaborators)



Replaces the current user access list with the new list sent in the body. If an empty list is sent, all access to other users will be removed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    CollaboratorsArray collaborators = new CollaboratorsArray(); // CollaboratorsArray | A model containing a list of user email addresses.
    try {
      OperationStatus result = apiInstance.permissionsUpdate(appId, collaborators);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#permissionsUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **collaborators** | [**CollaboratorsArray**](CollaboratorsArray.md)| A model containing a list of user email addresses. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  -  |
| **0** | Error Response. |  -  |

<a id="settingsList"></a>
# **settingsList**
> List&lt;AppVersionSettingObject&gt; settingsList(appId, versionId)



Gets the settings in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    try {
      List<AppVersionSettingObject> result = apiInstance.settingsList(appId, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#settingsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |

### Return type

[**List&lt;AppVersionSettingObject&gt;**](AppVersionSettingObject.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of the application version settings. |  -  |
| **0** | Error Response. |  -  |

<a id="settingsUpdate"></a>
# **settingsUpdate**
> OperationStatus settingsUpdate(appId, versionId, listOfAppVersionSettingObject)



Updates the settings in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    List<AppVersionSettingObject> listOfAppVersionSettingObject = Arrays.asList(); // List<AppVersionSettingObject> | A list of the updated application version settings.
    try {
      OperationStatus result = apiInstance.settingsUpdate(appId, versionId, listOfAppVersionSettingObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#settingsUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **listOfAppVersionSettingObject** | [**List&lt;AppVersionSettingObject&gt;**](AppVersionSettingObject.md)| A list of the updated application version settings. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  -  |
| **0** | Error Response. |  -  |

<a id="trainGetStatus"></a>
# **trainGetStatus**
> List&lt;ModelTrainingInfo&gt; trainGetStatus(appId, versionId)



Gets the training status of all models (intents and entities) for the specified LUIS app. You must call the train API to train the LUIS app before you call this API to get training status. \&quot;appID\&quot; specifies the LUIS app ID. \&quot;versionId\&quot; specifies the version number of the LUIS app. For example, \&quot;0.1\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    try {
      List<ModelTrainingInfo> result = apiInstance.trainGetStatus(appId, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#trainGetStatus");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |

### Return type

[**List&lt;ModelTrainingInfo&gt;**](ModelTrainingInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, JSON

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response provides an array of training status details for a LUIS app that you submitted for training. Each element in the response array provides training status for a model (intent or entity) in the LUIS app. Note: Training status is not provided for prebuilt entities because they are pretrained. The \&quot;modelId\&quot; property identifies which intent or entity the training status corresponds to. To get the name and type of each model, use the models API which has a request URL in this format: https://westus.api.cognitive.microsoft.com/luis/api/v2.0/apps/{appId}/versions/{versionId}/models The details property for each model can contain the following fields: \&quot;statusId\&quot;: An integer from 0 to 3 that corresponds to the value of the status field. \&quot;status\&quot;: A string with one of the following values: \&quot;Success\&quot;, \&quot;UpToDate\&quot;, \&quot;InProgress\&quot;, \&quot;Fail\&quot;. If the status is \&quot;Fail\&quot;, the \&quot;failureReason\&quot; property provides the reason for failure. \&quot;exampleCount\&quot;: The number of examples used for training. In the case of the None intent or prebuilt domain intents and entities, this number includes example provided internally by the system as well as examples you added to your LUIS app. \&quot;failureReason\&quot;: A string that indicates the reason training failed.  The value \&quot;FewLabels\&quot; means that no labeled example utterances were provided for training. \&quot;trainingDateTime\&quot;: A string indicating the time the model was last trained. The value uses the ISO 8601 format for representing times in UTC (Coordinated Universal Time) with a UTC designator (\&quot;Z\&quot;), for example: \&quot;2017-08-10T01:08:34Z\&quot;. |  -  |
| **0** | Error Response. |  -  |

<a id="trainTrainVersion"></a>
# **trainTrainVersion**
> EnqueueTrainingResponse trainTrainVersion(appId, versionId)



Sends a training request for a version of a specified LUIS app. This POST request initiates a request asynchronously. To determine whether the training request is successful, submit a GET request to get training status. Note: The application version is not fully trained unless all the models (intents and entities) are trained successfully or are up to date. To verify training success, get the training status at least once after training is complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    try {
      EnqueueTrainingResponse result = apiInstance.trainTrainVersion(appId, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#trainTrainVersion");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |

### Return type

[**EnqueueTrainingResponse**](EnqueueTrainingResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | This response indicates the initial training status. |  -  |
| **0** | Error Response. |  -  |

<a id="versionsClone"></a>
# **versionsClone**
> String versionsClone(appId, versionId, versionCloneObject)



Creates a new version from the selected version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    TaskUpdateObject versionCloneObject = new TaskUpdateObject(); // TaskUpdateObject | A model containing the new version ID.
    try {
      String result = apiInstance.versionsClone(appId, versionId, versionCloneObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#versionsClone");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **versionCloneObject** | [**TaskUpdateObject**](TaskUpdateObject.md)| A model containing the new version ID. | |

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The new version ID. |  -  |
| **0** | Error Response. |  -  |

<a id="versionsDelete"></a>
# **versionsDelete**
> OperationStatus versionsDelete(appId, versionId)



Deletes an application version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    try {
      OperationStatus result = apiInstance.versionsDelete(appId, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#versionsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  -  |
| **0** | Error Response. |  -  |

<a id="versionsDeleteUnlabelledUtterance"></a>
# **versionsDeleteUnlabelledUtterance**
> OperationStatus versionsDeleteUnlabelledUtterance(appId, versionId, utterance)



Deleted an unlabelled utterance in a version of the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    String utterance = "utterance_example"; // String | The utterance text to delete.
    try {
      OperationStatus result = apiInstance.versionsDeleteUnlabelledUtterance(appId, versionId, utterance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#versionsDeleteUnlabelledUtterance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **utterance** | **String**| The utterance text to delete. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  -  |
| **0** | Error Response. |  -  |

<a id="versionsExport"></a>
# **versionsExport**
> LuisApp versionsExport(appId, versionId)



Exports a LUIS application to JSON format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    try {
      LuisApp result = apiInstance.versionsExport(appId, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#versionsExport");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |

### Return type

[**LuisApp**](LuisApp.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The LUIS application structure in JSON format. |  -  |
| **0** | Error Response. |  -  |

<a id="versionsGet"></a>
# **versionsGet**
> VersionInfo versionsGet(appId, versionId)



Gets the version information such as date created, last modified date, endpoint URL, count of intents and entities, training and publishing status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    try {
      VersionInfo result = apiInstance.versionsGet(appId, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#versionsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |

### Return type

[**VersionInfo**](VersionInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A model containing the version info. |  -  |
| **0** | Error Response. |  -  |

<a id="versionsImport"></a>
# **versionsImport**
> String versionsImport(appId, luisApp, versionId)



Imports a new version into a LUIS application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    LuisApp luisApp = new LuisApp(); // LuisApp | A LUIS application structure.
    String versionId = "versionId_example"; // String | The new versionId to import. If not specified, the versionId will be read from the imported object.
    try {
      String result = apiInstance.versionsImport(appId, luisApp, versionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#versionsImport");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **luisApp** | [**LuisApp**](LuisApp.md)| A LUIS application structure. | |
| **versionId** | **String**| The new versionId to import. If not specified, the versionId will be read from the imported object. | [optional] |

### Return type

**String**

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created application version. |  -  |
| **0** | Error Response. |  -  |

<a id="versionsList"></a>
# **versionsList**
> List&lt;VersionInfo&gt; versionsList(appId, skip, take)



Gets a list of versions for this application ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    Integer skip = 0; // Integer | The number of entries to skip. Default value is 0.
    Integer take = 100; // Integer | The number of entries to return. Maximum page size is 500. Default is 100.
    try {
      List<VersionInfo> result = apiInstance.versionsList(appId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#versionsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **skip** | **Integer**| The number of entries to skip. Default value is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of entries to return. Maximum page size is 500. Default is 100. | [optional] [default to 100] |

### Return type

[**List&lt;VersionInfo&gt;**](VersionInfo.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of all versions of the application. |  -  |
| **0** | Error Response. |  -  |

<a id="versionsUpdate"></a>
# **versionsUpdate**
> OperationStatus versionsUpdate(appId, versionId, versionUpdateObject)



Updates the name or description of the application version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID appId = UUID.randomUUID(); // UUID | The application ID.
    String versionId = "versionId_example"; // String | The version ID.
    TaskUpdateObject versionUpdateObject = new TaskUpdateObject(); // TaskUpdateObject | A model containing Name and Description of the application.
    try {
      OperationStatus result = apiInstance.versionsUpdate(appId, versionId, versionUpdateObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#versionsUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appId** | **UUID**| The application ID. | |
| **versionId** | **String**| The version ID. | |
| **versionUpdateObject** | [**TaskUpdateObject**](TaskUpdateObject.md)| A model containing Name and Description of the application. | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation. |  -  |
| **0** | Error Response. |  -  |

