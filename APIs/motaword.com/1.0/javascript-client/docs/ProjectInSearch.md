# MotaWordApi.ProjectInSearch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**averageScores** | **{String: Number}** |  | [optional] 
**budgetCode** | **String** |  | [optional] 
**callbackUrl** | **String** | Callback URL to notify when project status changed. | [optional] 
**canPamManage** | **Boolean** |  | [optional] 
**client** | [**User**](User.md) |  | [optional] 
**cmId** | **Number** | Assigned admin&#39;s id | [optional] 
**completedOn** | **Date** | the date-time notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z | [optional] 
**continuousProjectType** | **String** |  | [optional] 
**createdAt** | **Number** | Unix epoch time | [optional] 
**custom** | **Object** | Custom data provided while creating a new project. | [optional] 
**deliveryAt** | **Number** | Unix epoch time | [optional] 
**errors** | [**[Error]**](Error.md) | A list of errors. Visible when creating a project and uploading your documents at the same time, in case of multiple errors. | [optional] 
**id** | **Number** |  | [optional] 
**isApiProject** | **Boolean** |  | [optional] 
**isCertified** | **Boolean** |  | [optional] 
**isContinuous** | **Boolean** |  | [optional] 
**isManual** | **Boolean** |  | [optional] 
**links** | [**ProjectLinks**](ProjectLinks.md) |  | [optional] 
**pairs** | [**[VendorProjectPair]**](VendorProjectPair.md) | Currently authed vendor&#39;s available working language pairs in this project. Includes rates per language pair. Includes complex pair logic such as bilingualism, project reverse pair enforcement etc. | [optional] 
**pivotedProjects** | **[Number]** | Quote IDs of pivots | [optional] 
**price** | [**ProjectPrice**](ProjectPrice.md) |  | [optional] 
**priceWithoutDiscount** | [**ProjectPrice**](ProjectPrice.md) |  | [optional] 
**role** | [**VendorProjectRole**](VendorProjectRole.md) |  | [optional] 
**shouldSendClientSurvey** | **Boolean** |  | [optional] 
**source** | [**ProjectSource**](ProjectSource.md) |  | [optional] 
**sourceLanguage** | **String** |  | [optional] 
**status** | [**ProjectStatus**](ProjectStatus.md) |  | [optional] 
**subjects** | **[String]** |  | [optional] 
**targetLanguages** | **[String]** |  | [optional] 
**tmsName** | **String** | TMS project name for this MW project. Requires privileged scope. | [optional] 
**validUntil** | **Number** | Unix epoch time. Available only if status is &#x60;pending&#x60;. | [optional] 
**vendorWordCount** | **Number** |  | [optional] 
**wordCount** | **Number** |  | [optional] 
**wordCountAnalysis** | [**ProjectWordCountAnalysis**](ProjectWordCountAnalysis.md) |  | [optional] 
**searchResultReason** | **String** |  | [optional] 


