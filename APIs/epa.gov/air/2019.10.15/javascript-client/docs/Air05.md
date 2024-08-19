# USEpaEnforcementAndComplianceHistoryOnlineEchoCleanAirAct.Air05

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badSystemIDs** | **String** | Identifies which passed query system identifiers are invalid. | 
**cVRows** | **String** | Summary count of the number of CWA facilities or SDWA public drinking water systems with current violations. | 
**fEARows** | **String** | Summary count of the number of facilities with a formal enforcement action in the past five years | 
**facilities** | [**[Air03]**](Air03.md) | A complex array of facility information. | [optional] 
**iNSPRows** | **String** | Number of facilities with insp_5yr_flag populated (CWP_DATE_LAST_INSPECTION) | 
**indianCountryRows** | **String** | Number of facilities with tribal_flag populated | 
**infFEARows** | **String** | Number of facilities with infea_5yr_flag populated (INFORMAL_ENF_ACT_COUNT &gt; 0) | 
**mapOutput** | [**Air04**](Air04.md) |  | [optional] 
**message** | **String** | Field to record messages (typically performance-related) about packet processing | 
**pageNo** | **String** | The number of pages of results returned | 
**queryID** | **String** | Sequential number assigned to entire search result | 
**queryRows** | **String** | Number of query results returned | 
**sVRows** | **String** | Number of facilities with curr_sv_flag populated (CWP_STATUS &#x3D; \&quot;Significant Violation\&quot;) | 
**totalPenalties** | **String** | The total dollar amount of either assessed or final penalties within the five year time period | 
**v3Rows** | **String** | Number of facilities having one or more quarters in non-compliance (QNC) in the last three years | 


