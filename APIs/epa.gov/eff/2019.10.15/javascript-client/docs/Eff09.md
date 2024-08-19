# USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting.Eff09

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cWPCity** | **String** | City in which the facility is located. | 
**cWPCurrentSNCStatus** | **String** | The type of noncompliance when a major source is in significant violation or a minor source has a Category 1 violation. | 
**cWPMajorMinorStatusFlag** | **String** | Facilities marked \&quot;M\&quot; for major refers to CWA major permittees. - M &#x3D; Major - N &#x3D; Minor | 
**cWPName** | **String** | Facility or permit holder name, as maintained in ICIS-NPDES. | 
**cWPPermitStatusDesc** | **String** | The current stage/status in the NPDES permit life cycle. | 
**cWPPermitTypeDesc** | **String** | NPDES facility permit classification: - NPDES Individual Permit - General Permit Covered Facility - NPDES Master General Permit - Associated Permit Record - Individual Industrial User Permit - Individual State Issued Permit - State Issued Master General Permit - Unpermitted Facility | 
**cWPState** | **String** | Facility location - two-digit state abbreviation. | 
**cWPStreet** | **String** | Facility street address | 
**cWPZip** | **String** | Facility ZIP code | 
**ePASystem** | **String** | The EPA data system in which permit and facility records are kept. EPA&#39;s Facility Registry System (FRS) links all program database records (such as permit IDs and IDs facilities use in reporting to EPA) together. The following list describes the individual data systems that are linked to from the detailed facility report:   - AFS: Air Facility System for Clean Air Act stationary source programs. - ICP: Integrated Compliance Information System for Clean Water Act programs monitoring National Pollutant Discharge Elimination System (NPDES) permits. - RCR: Resource Conservation and Recovery Act Information System (RCRAInfo) for tracking the Resource Conservation and Recovery Act (RCRA) programs. - NCDB: National Compliance Database System for monitoring national performance of the Toxic Substance Control Act (TSCA); the Emergency Planning and Right-to-Know Act, Section 313 (EPCRA); the Asbestos Hazard Emergency Response (AHERA); and the Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA). - TRI: Toxics Release Inventory for Emergency Planning and Community Right-to-Know Act, Section 313 submissions. - NEI: National Emissions Inventory database contains information on stationary and mobile sources that emit criteria air pollutants and their precursors, as well as hazardous air pollutants (HAPs). The database includes estimates of annual emissions, by source, of air pollutants in each area of the country, on an annual basis. - TSCA: Toxic Substances Control Act addressing the production, importation, use, and disposal of specific chemicals. | 
**endDate** | **String** | End date for the date range of interest. Formatted as mm/dd/yyyy | 
**linkedPermits** | [**[Eff06]**](Eff06.md) |  | [optional] 
**message** | **String** | Field to record messages (typically performance-related) about packet processing | 
**permFeatures** | [**[Eff08]**](Eff08.md) |  | [optional] 
**registryId** | **String** | 12-digit Facility Registry Service (FRS) identification number.  FRS uniquely identifies a facility by assigning an identification number (FRS ID), and uses this FRS ID to link together all EPA regulatory program database records | 
**sourceId** | **String** | Unique Identifier assigned by EPA. | 
**startDate** | **String** | Starting date for the date range of interest. Formatted as mm/dd/yyyy | 
**statute** | **String** | The name of the statute associated with each of the permits and identifiers linked to the facility:  - CAA &#x3D; the Clean Air Act - CWA &#x3D; the Clean Water Act - RCRA &#x3D; the Resource Conservation and Recovery Act - EP313 &#x3D; the Emergency Planning and Community Right-to-Know Act, Section 313 (also known as the Toxics Release Inventory Program) - TSCA &#x3D; the Toxic Substances Control Act - SDWA &#x3D; the Safe Drinking Water Act | 


