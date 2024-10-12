# USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.Cwa08

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badSystemIDs** | **String** | Identifies which passed query system identifiers are invalid. | 
**bioCVRows** | **String** | Number of facilities with current biosolid-related violations. | 
**bioV3Rows** | **String** | Number of facilities having one or more quarters of biosolid-related non-compliance in the last three years. | 
**cVRows** | **String** | Summary count of the number of CWA facilities or SDWA public drinking water systems with current violations. | 
**clusterOutput** | [**Cwa06**](Cwa06.md) |  | [optional] 
**clusterRecords** | **String** | Number of clusters returned. | [optional] 
**fEARows** | **String** | Summary count of the number of facilities with a formal enforcement action in the past five years | 
**facilities** | [**[Cwa07]**](Cwa07.md) | A complex array of facility information. | [optional] 
**iNSPRows** | **String** | Number of facilities with insp_5yr_flag populated (CWP_DATE_LAST_INSPECTION) | 
**iconBaseURL** | **String** | URL where all the icons are located | 
**indianCountryRows** | **String** | Number of facilities with tribal_flag populated | 
**infFEARows** | **String** | Number of facilities with infea_5yr_flag populated (INFORMAL_ENF_ACT_COUNT &gt; 0) | 
**message** | **String** | Field to record messages (typically performance-related) about packet processing | 
**popUpBaseURL** | **String** | Combine this URL with the PUC to get popup info | 
**queryID** | **String** | Sequential number assigned to entire search result | 
**queryParameters** | [**[Qp0]**](Qp0.md) | A list of submitted query parameters and their values. | 
**queryRows** | **String** | Number of query results returned | 
**sVRows** | **String** | Number of facilities with curr_sv_flag populated (CWP_STATUS &#x3D; \&quot;Significant Violation\&quot;) | 
**serviceBaseURL** | **String** | The base service URL. | 
**totalPenalties** | **String** | The total dollar amount of either assessed or final penalties within the five year time period | 
**v3Rows** | **String** | Number of facilities having one or more quarters in non-compliance (QNC) in the last three years | 
**vioLast4QRows** | **String** | The number of facilities with a violation in the last year. | 


