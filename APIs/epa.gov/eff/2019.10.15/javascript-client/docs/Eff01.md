# USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting.Eff01

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dMREventId** | **String** | The sequence ID identifying the DMR Event. | 
**dMRFormValueId** | **String** | The sequence ID identifying the DMR Form Value. | 
**dMRUnitCode** | **String** | The code representing the unit of measure applicable to quantity or concentration limits and measurements as entered into ICIS-NPDES | 
**dMRUnitDesc** | **String** | The short description of the unit of measure applicable to limit or DMR values | 
**dMRValueId** | **String** | The unique identifier for the DMR value generated in ICIS-NPDES | 
**dMRValueNmbr** | **String** | The DMR value number reported on the DMR Form | 
**dMRValueQualifierCode** | **String** | The unique code identifying the DMR value operator (i.e., &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, T, E, &#x3D;). E indicates an estimated value. T indicates too numerous to count | 
**dMRValueStdUnits** | **String** | The DMR value expressed in standard units, as calculated in ICIS-NPDES | 
**daysLate** | **String** | The number of days the DMR value is late, as generated in ICIS-NPDES | 
**exceedencePct** | **String** | The percent by which the DMR value (or adjusted value) exceeded its limit (or stay) value, as generated in ICIS-NPDES | 
**limitBeginDate** | **String** | The date on which a limit becomes in effect for a particular parameter in a limit set | 
**limitEndDate** | **String** | The date on which a limit stops being in effect for a particular parameter in a limit set | 
**limitId** | **String** | The unique identifier for a limit parameter record | 
**limitSetId** | **String** | The unique identifier for a limit set, generated in ICIS-NPDES | 
**limitSetScheduleId** | **String** | The unique identifier of the Limit Set Schedule, generated in ICIS-NPDES | 
**limitTypeCode** | **String** |  | 
**limitUnitCode** | **String** | The code representing the unit of measure applicable to quantity or concentration limits and measurements as entered by the user | 
**limitUnitDesc** | **String** | The short description of the unit of measure applicable to limit or DMR values | 
**limitValueId** | **String** | The unique identifier in ICIS-NPDES for the Limit Value | 
**limitValueNmbr** | **String** | The numerical limit for a given parameter | 
**limitValueQualifierCode** | **String** | The unique code identifying the limit value operator (i.e., &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, T, E, &#x3D;). E indicates an estimated value. T indicates too numerous to count | 
**limitValueStdUnits** | **String** | The limit value expressed in standard units, as calculated in ICIS-NPDES | 
**limitValueTypeCode** | **String** | The code indicating the type of value the limit is given as (i.e., Q1, Q2, C1, C2, C3) | 
**limitValueTypeDesc** | **String** | The description indicating the type of value the limit is given as (e.g., Concentration, Quantity) | 
**monitoringPeriodEndDate** | **String** | The date that the monitoring period for the values covered by the DMR Form ends | 
**nODEDesc** | **String** |  | 
**nODICode** | **String** | The unique code indicating why no DMR Value was submitted by the permittee for a Monitoring Period End Date | 
**nPDESViolations** | [**[Eff02]**](Eff02.md) |  | [optional] 
**nmbrOfSubmission** | **String** | The number of months of discharges represented on each DMR for the limit set (e.g., monthly &#x3D; 1, bi-monthly &#x3D; 2, quarterly &#x3D; 3, triannual &#x3D; 4, semi-annual &#x3D; 6, annual &#x3D; 12). This data element will be blank for Unscheduled Limit Sets | 
**permFeatureId** | **String** | The unique identifier in ICIS-NPDES of a permitted feature or outfall | 
**statisticalBaseCode** | **String** | The code representing the unit of measure applicable to the limit and DMR values entered by the user (e.g., 30-day average, daily maximum) | 
**statisticalBaseDesc** | **String** |  | 
**statisticalBaseTypeCode** | **String** | The code indicating whether the statistical base code is a minimum, average, or maximum for purposes of calculating compliance against the limit value | 
**statisticalBaseTypeDesc** | **String** | A short description for indicating whether the statistical base code is a minimum, average, or maximum for purposes of calculating compliance against the limit value | 
**stayValueNmbr** | **String** | The numeric limit value imposed during the period of the stay for the limit; if entered, during the stay period, ICIS-NPDES will use this limit value for calculating compliance rather than the actual limit value | 
**stdUnitCode** | **String** | The code representing the standard unit of measure applicable to quantity or concentration limits and measurements as entered by the user | 
**stdUnitDesc** | **String** | The short description of the standard unit of measure applicable to limit or DMR values | 
**valueReceivedDate** | **String** | The date the DMR value was received by the regulatory authority | 
**valueTypeCode** | **String** | The indication of the limit value type (e.g., Quantity 1, Concentration 2) | 
**valueTypeDesc** | **String** | The type of value the measured number is given as (e.g., Concentration, Quantity) | 
**versionNmbr** | **String** | The version of the permit when a modification or reissuance is applied to the permit. Version &#x3D; 0 indicates the original permit issuance | 


