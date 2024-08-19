

# Dfr0GetD80d90sDetailsD80D90sDetailsSources

Sources Object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**daysLate** | **String** | The number of days the DMR value is late, as generated in ICIS-NPDES |  |
|**dmrDueDate** | **String** | The due date for the DMR to the NPDES program authority (e.g., EPA or state environmental agency) (MM/DD/YYYY).� |  |
|**limitBeginDate** | **String** | The date on which a limit becomes in effect for a particular parameter in a limit set |  |
|**limitEndDate** | **String** | The date on which a limit stops being in effect for a particular parameter in a limit set |  |
|**limitId** | **String** | The unique identifier for a limit parameter record |  |
|**limitSetName** | **String** | The name associated with a group of parameter permit limits. |  |
|**missingLate** | **String** | Indicates if the permitted facility submitted missing or late DMRS to the NPDES permitting authority within the past three years. |  |
|**monitoringLocationCode** | **String** | The code that the monitoring location at which the monitoring requirement (and effluent limit if limited) applies. One parameter may have several monitoring location codes pertaining to the same permitted feature |  |
|**monitoringLocationDesc** | **String** | The name of the monitoring location at which the monitoring requirement (and effluent limit if limited) applies |  |
|**monitoringPeriodEndDate** | **String** | The date that the monitoring period for the values covered by the DMR Form ends |  |
|**npDESId** | **String** | A unique ID assigned for each record/permit/site/facility within ICIS-NPDES. |  |
|**nodiCode** | **String** | The no data indicator code for DMRs where no measurements are reported. |  |
|**nodiDesc** | **String** | The description of the NODI code explaining why no data are reported (e.g., no discharge, not quantifiable, conditional monitoring). |  |
|**nodiValidationFlag** | **String** | Indicates whether the NODI is considered valid (Y) or invalid (N) for compliance determination purposes. |  |
|**npdesViolationId** | **String** | The unique identifier for the violation related to a particular site. |  |
|**parameterCode** | **String** | The unique 5 digit numeric code identifying the parameter. If the code is less than 5 digits in the .CSV, append zeros to the beginning of the number (e.g., 100 is equivalent to 00100) |  |
|**parameterDesc** | **String** | The pollutant name and form (e.g., dissolved, suspended) associated with the parameter code |  |
|**permFeatureNmbr** | **String** | A three-character code in ICIS-NPDES that identifies the point of discharge (e.g., outfall) for a facility. A NPDES permit may have multiple points of discharge. If the code is less than three characters in the .CSV, append zeros to the beginning of the number (e.g., 1 is equivalent to 001) |  |
|**rncDetectionCode** | **String** | The reportable noncompliance detection code. |  |
|**rncDetectionDate** | **String** | The date that RNC was detected. It can be entered manually or automatically. In cases in which RNC is detected by ICIS-NPDES, the detection date entered will vary according to the type of violation detected (MM/DD/YYY). |  |
|**rncDetectionDesc** | **String** | The reportable noncompliance detection description. |  |
|**rncResolutionCode** | **String** | The reportable noncompliance resolution code. |  |
|**rncResolutionDate** | **String** | The reportable noncompliance resolution date. |  |
|**rncResolutionDesc** | **String** | The reportable noncompliance resolution description. |  |
|**statisticalBaseMonthlyAvg** | **String** |  |  |
|**valueReceivedDate** | **String** | The date the DMR value was received by the regulatory authority |  |
|**valueTypeCode** | **String** | The indication of the limit value type (e.g., Quantity 1, Concentration 2) |  |
|**versionNmbr** | **String** | The version of the permit when a modification or reissuance is applied to the permit. Version &#x3D; 0 indicates the original permit issuance |  |
|**violationCode** | **String** | The code identifying which type of Violation has occurred (e.g., D80 &#x3D; Required Monitoring DMR Value Non-Receipt, E90 &#x3D; Effluent Violation, C20 &#x3D; Schedule Event Achieved Late) |  |



