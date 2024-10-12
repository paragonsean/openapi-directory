

# ProjectInSearch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**averageScores** | **Map&lt;String, Float&gt;** |  |  [optional] |
|**budgetCode** | **String** |  |  [optional] |
|**callbackUrl** | **String** | Callback URL to notify when project status changed. |  [optional] |
|**canPamManage** | **Boolean** |  |  [optional] |
|**client** | [**User**](User.md) |  |  [optional] |
|**cmId** | **Long** | Assigned admin&#39;s id |  [optional] |
|**completedOn** | **OffsetDateTime** | the date-time notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z |  [optional] |
|**continuousProjectType** | **String** |  |  [optional] |
|**createdAt** | **Long** | Unix epoch time |  [optional] |
|**custom** | **Object** | Custom data provided while creating a new project. |  [optional] |
|**deliveryAt** | **Long** | Unix epoch time |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | A list of errors. Visible when creating a project and uploading your documents at the same time, in case of multiple errors. |  [optional] |
|**id** | **Long** |  |  [optional] |
|**isApiProject** | **Boolean** |  |  [optional] |
|**isCertified** | **Boolean** |  |  [optional] |
|**isContinuous** | **Boolean** |  |  [optional] |
|**isManual** | **Boolean** |  |  [optional] |
|**links** | [**ProjectLinks**](ProjectLinks.md) |  |  [optional] |
|**pairs** | [**List&lt;VendorProjectPair&gt;**](VendorProjectPair.md) | Currently authed vendor&#39;s available working language pairs in this project. Includes rates per language pair. Includes complex pair logic such as bilingualism, project reverse pair enforcement etc. |  [optional] |
|**pivotedProjects** | **List&lt;Long&gt;** | Quote IDs of pivots |  [optional] |
|**price** | [**ProjectPrice**](ProjectPrice.md) |  |  [optional] |
|**priceWithoutDiscount** | [**ProjectPrice**](ProjectPrice.md) |  |  [optional] |
|**role** | **VendorProjectRole** |  |  [optional] |
|**shouldSendClientSurvey** | **Boolean** |  |  [optional] |
|**source** | **ProjectSource** |  |  [optional] |
|**sourceLanguage** | **String** |  |  [optional] |
|**status** | **ProjectStatus** |  |  [optional] |
|**subjects** | **List&lt;String&gt;** |  |  [optional] |
|**targetLanguages** | **List&lt;String&gt;** |  |  [optional] |
|**tmsName** | **String** | TMS project name for this MW project. Requires privileged scope. |  [optional] |
|**validUntil** | **Long** | Unix epoch time. Available only if status is &#x60;pending&#x60;. |  [optional] |
|**vendorWordCount** | **Long** |  |  [optional] |
|**wordCount** | **Long** |  |  [optional] |
|**wordCountAnalysis** | [**ProjectWordCountAnalysis**](ProjectWordCountAnalysis.md) |  |  [optional] |
|**searchResultReason** | **String** |  |  [optional] |



