# USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct.Sdw04

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**citiesServed** | **String** | County | 
**countiesServed** | **String** | City | 
**cuAle** | **String** | The count of occurrences when 90th percentile sample concentrations of copper exceeded the copper action level of 1.3 mg/L in the past five years. | 
**cuViol** | **String** | The number of copper violations in the last five years. | 
**currVioFlag** | **String** | Indicates if the facility has a current violation. 1 &#x3D; Yes | 
**dateLastSansurvey** | **String** |  | 
**dfrUrl** | **String** | The URL to the facility&#39;s Detailed Facility Report. | 
**ePARegion** | **String** | The EPA region in which the facility is located | 
**fIPSCodes** | **String** | Five-character Federal Information Processing Standards (FIPS) value: 2-character state || 3-character county | 
**feaFlag** | **String** | Number of formal enforcement responses during the past 5 years (20 most recent quarters) as of the last quarterly refresh.  Formal enforcement actions compel a PWS to take specific actions by specific dates to return to compliance | 
**feas** | **String** | Number of formal enforcement responses during the past 5 years (20 most recent quarters) as of the last quarterly refresh.  Formal enforcement actions compel a PWS to take specific actions by specific dates to return to compliance. | 
**gwSwCode** | **String** | Returns \&quot;GW\&quot; if the system�source water type is ground water. Returns \&quot;SW\&quot; if the system source water type is surface water. | 
**healthFlag** | **String** | Indicates whether system has violations of health-based drinking water standards | 
**ieaFlag** | **String** | Returns 0 if the system does not have informal enforcement actions in the past five years. Returns 1 if the system does have informal enforcement actions in the past five years. | 
**ifea** | **String** | Number of informal enforcement responses during the past 5 years (20 most recent quarters) as of the last quarterly refresh.  Informal enforcement actions do not specify actions and deadlines for returning to compliance. | 
**indianCountry** | **String** | Indicates whether the facility is located in Indian Country | 
**insp5yrFlag** | **String** | Indicates if the facility has an inspection within the last 5 years. 1 &#x3D; Yes | 
**leadAndCopperViol** | **String** | The number of lead and copper violations. | 
**maxScore** | **String** | A sorting score for internal use. | 
**mrFlag** | **String** | Indicates whether system has monitoring and reporting violations | 
**newVioFlg** | **String** | Violations that have been reported to SDWA since end of the last official quarter. These violations are considered draft and do not reflect the official compliance status for the facility. | 
**otherFlag** | **String** | Indicates whether system has other violations, such as failing to issue annual consumer confidence reports or maintain required records | 
**ownerDesc** | **String** | Description of Owner code | 
**ownerTypeCode** | **String** | Owner/Operator: - P &#x3D; Private - F &#x3D; Federal Government - S &#x3D; State Government - L &#x3D; Local Government | 
**pWSActivityCode** | **String** | Indicates whether systems have an active or inactive designation. | 
**pWSActivityDesc** | **String** | Description of activity status code (ACT), e.g., active, inactive. | 
**pWSId** | **String** | Unique identifying code for a public water system, consisting of a two-letter state or region code, followed by seven digits | 
**pWSName** | **String** | Name of the system regulated under the Safe Drinking Water Act (SDWA) | 
**pWSTypeCode** | **String** | Type of public water system: - CWS   &#x3D; Community water system - NCWS  &#x3D; Non-community water system - NTCWS &#x3D; Non-transient non-community water system - TNCWS &#x3D; Transient non-community water system | 
**pWSTypeDesc** | **String** | The type of public water system (PWS) and description of corresponding SystemType code. A public water system is a system for the provision to the public of piped water for human consumption, which has at least 15 service connections or regularly serves a | 
**pbAle** | **String** | The count of occurrences when 90th percentile sample concentrations of lead exceeded the lead action level of 0.015 mg/L in the past five years. | 
**pbViol** | **String** | The number of lead violations in the last five years. | 
**pnFlag** | **String** | Indicates whether system has Public Notice Violations (failure to immediately alert consumers of serious problem with drinking water) | 
**populationServedCount** | **String** | Estimated average daily population served by a system | 
**primarySourceCode** | **String** | The source water type: Surface water (SW) - Water pumped and treated from sources open to the atmosphere, such as rivers, lakes, and reservoirs. Ground water (GW) - Water pumped and treated from aquifers (natural reservoirs below the earth&#39;s surface). Ground water under direct influence of surface water (GU) - Any water pumped from natural reservoirs below the earth&#39;s surface that has been determined to be under the direct influence of surface water. Purchased (Surface, Ground, Ground UDI Surface) Water - Water purchased from a wholesaler who pumps and treats water. | 
**primarySourceDesc** | **String** | The source water type: Surface water (SW) - Water pumped and treated from sources open to the atmosphere, such as rivers, lakes, and reservoirs. Ground water (GW) - Water pumped and treated from aquifers (natural reservoirs below the earth&#39;s surface). Ground water under direct influence of surface water (GU) - Any water pumped from natural reservoirs below the earth&#39;s surface that has been determined to be under the direct influence of surface water. Purchased (Surface, Ground, Ground UDI Surface) Water - Water purchased from a wholesaler who pumps and treats water. | 
**qtrsWithSNC** | **String** | The number of quarters the system was designated by EPA as a serious violator over the past 3 years (12 most recent quarters). | 
**qtrsWithVio** | **String** | The number of quarters the system was in violation over the past three years. This includes the 12 most recent official quarters and new violations reported after the end of the last official quarter. | 
**rc350Viol** | **String** | The count of open health-based lead violations in the past five years. These include violations of maximum contaminant levels (MCLs), maximum residual disinfectant levels (MRDLs), or treatment technique (TT) rules. This count includes new violations that have been reported since the end of the last official quarter. | 
**registryID** | **String** | An internal 12-digit Facility Registry Service (FRS) tracking number used to tie all facility data together in EPA regulatory program databases. | 
**rulesVio** | **String** | The count of rules the system is violating as of the latest official quarter of data in the source system, SDWIS, which may lag by 3-6 months. This includes violations in the most recent official quarter and new violations reported after the end of the last official quarter. | 
**rulesVio3yr** | **String** | The count of rules the system was in violation of over the past three years. This includes the 12 most recent official quarters and new violations reported after the end of the last official quarter. | 
**sDWA3yrComplQtrsHistory** | **String** | The system&#39;s 3-year compliance status history by quarter (3-month period). Each character represents a quarter of compliance, going from oldest to most recent. Character values correspond to the following compliance statuses: _ - No Violation Identified V - Noncompliance S - Significant Noncompliance U - Undetermined | 
**sDWAContaminants** | **String** | All unresolved violation contaminants or violation contaminants that have been resolved in the last 5 years. | 
**sDWAContaminantsInCurViol** | **String** | The contaminant name and code (in SDWIS) in violation of a SDWA regulation. This includes violations in the most recent official quarter and new violations that have been reported since the end of the last official quarter. | 
**sDWAContaminantsInViol3yr** | **String** | The contaminant name and code in violation of a SDWA regulation in the past three years | 
**sDWDateLastFea** | **String** | Indicates the effective date of the most recent listed formal enforcement action taken against the PWS within the last five years. | 
**sDWDateLastFeaEPA** | **String** | Indicates the effective date of the most recent listed formal enforcement action taken against the PWS by EPA within the last five years. | 
**sDWDateLastFeaSt** | **String** | Indicates the effective date of the most recent listed formal enforcement action taken against the PWS by a state environmental agency within the last five years. | 
**sDWDateLastIea** | **String** | Indicates the effective date of the most recent listed informal enforcement action taken against the PWS within the last five years. | 
**sDWDateLastIeaEPA** | **String** | Indicates the effective date of the most recent listed informal enforcement action taken against the PWS by EPA within the last five years. | 
**sDWDateLastIeaSt** | **String** | Indicates the effective date of the most recent listed informal enforcement action taken against the PWS by a state environmental agency within the last five years. | 
**sDWDateLastVisit** | **String** | The date of the last system visit. | 
**sDWDateLastVisitEPA** | **String** | The date of the last system visit by EPA. | 
**sDWDateLastVisitLocal** | **String** | The date of the last system visit by a local agency. | 
**sDWDateLastVisitState** | **String** | The date of the last system visit by a state agency. | 
**SNC** | **String** | Indicates the system&#39;s compliance status: No Violation,�In Violation, Signficant Noncompliance, or Unknown. | 
**sNCFlag** | **String** | Returns 1 if the system is in significant noncompliance (SNC); returns 0 if not. | 
**sansurvey5yr** | **String** | The number of sanitary surveys completed within the past five years. A sanitary survey is an on-site review of a system&#39;s water source, facilities, equipment, operation, and maintenance, intended to point out sanitary deficiencies and assess the system&#39;s capability to supply safe drinking water. | 
**seriousViolator** | **String** | Indicates whether system is a Serious Violator (has unresolved serious, multiple, and/or continuing violations that is designated as a priority candidate for formal enforcement) | 
**serviceAreaTypeCode** | **String** |  | 
**serviceAreaTypeDesc** | **String** |  | 
**significantDeficiencyCount** | **String** | The number of significant deficiencies found from a sanitary survey within the past five years. | 
**significantDeficiencyCountIls** | **String** |  | 
**siteVisits5yrAll** | **String** |  | 
**siteVisits5yrInspections** | **String** |  | 
**siteVisits5yrOther** | **String** |  | 
**stateCode** | **String** | The state in which the system is located. | 
**tRIbalFlag** | **String** | A flag indicating that the facility is within a tribal area. | 
**vioFlag** | **String** | Indicates whether the system has been in violation in the past five years (1 if yes, 0 if no). | 
**viofeanot** | **String** | Sum of violation points accrued during past five years (20 most recent quarters) that are under formal enforcement but not yet returned to compliance, as of the last quarterly refresh | 
**violationCategories** | **String** |  | 
**viopaccr** | **String** | Sum of all violation points for violations reported during the past five years (20 most recent quarters), as of the last quarterly refresh | 
**vioremain** | **String** | Sum of violation points that were not returned to compliance as of the last quarterly refresh.  Includes points that have received formal enforcement but have not returned to compliance | 
**viortcfea** | **String** | Sum of violation points during past 5 years (20 most recent quarters) that received formal enforcement and returned to compliance, as of the last quarterly refresh | 
**viortcnofea** | **String** | Sum of violation points during past 5 years (20 most recent quarters) that did not receive formal enforcement but did return to compliance, as of the last quarterly refresh | 
**zipCodesServed** | **String** | ZIP code | 


