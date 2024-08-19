# USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.Echo07

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aIRFlag** | **String** | Indicates whether the facility has a Clean Air Act (CAA) permit. | 
**aIRIDs** | **String** | Air Facility System (AFS) ID. | 
**activeLower48** | **String** | A Y/N indicator indicating that the facility is active and located within the lower 48 contiguous US States. | 
**biosolidsFlag** | **String** | A Yes/No field to indicate permits with biosolids management and compliance information. | 
**cAA3yrComplQtrsHistory** | **String** | The facility&#39;s 3-year compliance status history by quarter (3-month period) entered in the CAA program database. Each character represents a quarter of compliance, going from oldest to most recent. Character values correspond to the following compliance statuses: _ -�No Violation Identified V -�Violation Identified S -�High Priority Violation U - Undetermined | 
**cAAComplianceStatus** | **String** | An indication of the facility&#39;s compliance status under the Clean Air Act. When a source has a high priority violation (HPV), the specific type of HPV will be displayed. If more than one type applies to a source, this order of priority is used to determine which type appears: Violation Unaddressed, EPA has Lead Enforcement Violation Unaddressed, State has Lead Enforcement Violation Unaddressed, Local has Lead Enforcement Violation Addressed, EPA has Lead Enforcement Violation Addressed, State has Lead Enforcement Violation Addressed, Local has Lead Enforcement When there is no Federally-Reportable Violation determination date in the past year and no open High Priority Violation in the most recent quarter in the data system of record, “Not Available” is displayed. | 
**cAADateLastFormalAction** | **String** | The effective date of the most recent listed enforcement action entered into the CAA program database. | 
**cAADaysLastEvaluation** | **String** | The number of days since a CAA Full Compliance Evaluation (FCE) was completed. | 
**cAAEvaluationCount** | **String** | The number of inspections/compliance evaluations under the Clean Air Act, occurring at the facility within the last five years | 
**cAAFormalActionCount** | **String** | Indicates the number of enforcement actions taken against the facility within the last five years under the Clean Air Act. | 
**cAAHpvFlag** | **String** | The High Priority Violator (HPV) status for the facility during the most recent quarter reflects the time the records were extracted from the program data system. \&quot;Y\&quot; indicates the facility is in HPV for the permit or site in question and may pose a more severe level of environmental threat. \&quot;N\&quot; indicates the permit or site is not considered in HPV. | 
**cAAInformalCount** | **String** | Indicates the number of informal enforcement actions/notices of violations (NOVs) taken against the facility within the last five years under the Clean Air Act. | 
**cAALastPenaltyAmt** | **String** | The amount of the most recent penalty entered into the CAA program database. | 
**cAALastPenaltyDate** | **String** | The effective date of the most recent penalty entered into the CAA program database. | 
**CAANAICS** | **String** | The CAA permit&#39;s primary North American Industry Classification System (NAICS) Codes. | 
**cAAPenalties** | **String** | The total dollar amount of assessed (or final) penalties taken against the facility within the last five years under the Clean Air Act. | 
**cAAPermitTypes** | **String** | ICIS AIR Permit Types associated with the FRS Facility: - Major - Federally Reportable Minor - Other Minor - Synthetic Minor - NULL | 
**cAAQtrsWithNC** | **String** | The number of quarters, out of the last twelve quarters, in which the CAA permit is considered in violation. | 
**cAASICs** | **String** | The CAA permit&#39;s primary Standard Industrial Classification (SIC) Codes. | 
**cWA13qtrsComplHistory** | **String** | The facility&#39;s 3-year compliance status history by quarter (3-month period) entered in the CWA program database. Each character represents a quarter of compliance, going from oldest to most recent. Character values correspond to the following compliance statuses: _ -�No Violation V -�Violation S -�Significant Violation U - Undetermined | 
**cWA13qtrsEfflntExceedances** | **String** | The number of effluent violations at the facility in the past 13 quarters. | 
**cWA3YrQncrCodes** | **String** | No longer used.  Will be deleted in nthe future. | 
**cWAComplianceStatus** | **String** | An indication of the facility&#39;s compliance status under the Clean Water Act. When a major source is in significant noncompliance (SNC) or a non-major source has a Category I violation, the specific type of SNC/Category I will be displayed. If more than one type applies to a facility, this order of priority is used to determine which code appears: S(CSchVio) - an enforcement action has been issued, and the facility is not meeting its compliance schedule E(EffViol) - effluent violations of monthly average limits X(EffNMth) - effluent violations of non-monthly average limits T(CSchRpt) - compliance schedule reporting violation D(DMR NR) - non-receipt of discharge monitoring report | 
**cWAComplianceTracking** | **String** | The Compliance Tracking classifications which can assist in interpreting the facility&#39;s compliance status, particularly for non-major standard permittees. | 
**cWADateLastFormalAction** | **String** | The effective date of the most recent listed enforcement action entered into the CWA program database. | 
**cWADaysLastInspection** | **String** | The number of days since a CWA inspection was completed. | 
**cWAFormalActionCount** | **String** | Indicates the number of enforcement actions taken against the facility within the last five years under the Clean Water Act. | 
**cWAInformalCount** | **String** | Indicates the number of informal enforcement actions/notices of violations (NOVs) taken against the facility within the last five years under the Clean Water Act. | 
**cWAInspectionCount** | **String** | The number of inspections/compliance evaluations under the Clean Water Act, occurring at the facility within the last five years. | 
**cWALastPenaltyAmt** | **String** | The amount of the most recent penalty entered into the CWA program database. | 
**cWALastPenaltyDate** | **String** | The effective date of the most recent penalty entered into the CWA program database. | 
**CWANAICS** | **String** | The CWA permit&#39;s primary North American Industry Classification System (NAICS) Codes. | 
**cWAPenalties** | **String** | The total dollar amount of assessed (or final) penalties taken against the facility within the last five years under the Clean Water Act. | 
**cWAPermitTypes** | **String** | Indicates the facility&#39;s permit type or designation. - Major - Minor | 
**cWAQtrsWithNC** | **String** | The number of quarters, out of the last twelve quarters, in which the CWA permit is considered in violation. | 
**cWASICs** | **String** | The CWA permit&#39;s primary Standard Industrial Classification (SIC) Codes. | 
**cWASNCFlag** | **String** | The CWA Significant Non-compliance (SNC) status for the facility during the most recent quarter reflects the time the records were extracted from the program data systems. \&quot;Y\&quot; indicates the facility is in SNC for the permit or site in question and may pose a more severe level of environmental threat. \&quot;N\&quot; indicates the permit or site is not considered in SNC. | 
**camdIDs** | **String** | Facility identifiers for the Clean Air Markets Division database. | 
**censusBlockGroup** | **String** | A geographic unit used by the United States Census Bureau, generally defined to contain between 600 and 3,000 people. | 
**currSvFlag** | **String** | Indicates if the facility has a current significant violation. 1 &#x3D; Yes | 
**currVioFlag** | **String** | Indicates if the facility has a current violation. 1 &#x3D; Yes | 
**dfrUrl** | **String** | The URL to the facility&#39;s Detailed Facility Report. | 
**ea5yrFlag** | **String** | Indicates if the facility has a formal enforcement action within the last 5 years. 1 &#x3D; Yes | 
**effChartsFlag** | **String** |  | 
**eisFlag** | **String** | Indicates whether the facility reports to the Emissions Inventory System (EIS). | 
**eisIDs** | **String** | A unique ID assigned for each facility within EPA’s Emissions Inventory System (EIS) Database. | 
**ejscreenFlag** | **String** | A Y/N indicator identifying whether or not the facility is within an Environmental Justice area. | 
**ejscreenFlagUs** | **String** | A Y/N indicator identifying whether or not the facility is within an Environmental Justice area. | 
**epcraInspections5yr** | **String** | From ICIS FE&amp;C, the number of EPCRA inspections at the facility in the past five years. | 
**fac3yrComplianceHistory** | **String** | The system&#39;s 3-year compliance status history by quarter (3-month period). Each character represents a quarter of compliance, going from oldest to most recent. Character values correspond to the following compliance statuses: _ -�No Violation V -�Violation S -�Significant Violation U - Undetermined | 
**facAccuracyMeters** | **String** | The estimate of accuracy, in meters, based on provided spatial metadata and quality assurance routines for the provided facility coordinate. | 
**facActiveFlag** | **String** | Indicates whether any of the associated ICIS-Air, ICIS-NPDES, RCRAInfo or SDWIS permits/facilities are in an active status. | 
**facChesapeakeBayFlg** | **String** | Indicates whether the facility, based on the facility spatial coordinate, is within the Chesapeake Bay watershed. | 
**facCity** | **String** | The city where the facility is located. | 
**facCollectionMethod** | **String** | Indicates the collection method used (GPS, Photo Interpolation, Address Geocode, etc) to determine a facility&#39;s spatial coodinate. | 
**facComplianceStatus** | **String** | An indication of the facility&#39;s known overall compliance status. Status codes include: SNC/Serious Viol [significant noncompliance (SNC), high priority violation (HPV), or serious violator, depending on statute] In Violation (in violation of an environmental regulation) No Violation (no violations recorded in the national systems of record) Not Available Unknown | 
**facCounty** | **String** | The county where the facility is located. | 
**facDateLastFormalActEPA** | **String** | Indicates the effective date of the most recent listed formal enforcement action taken against the facility. | 
**facDateLastFormalActSt** | **String** | The effective date of the most recent listed formal enforcement action taken against the facility by a state agency. | 
**facDateLastFormalAction** | **String** | Indicates the effective date of the most recent listed enforcement action taken against the facility. | 
**facDateLastInformalActEPA** | **String** | Indicates the effective date of the most recent listed informal enforcement action taken against the facility. | 
**facDateLastInformalActSt** | **String** | The effective date of the most recent listed informal enforcement action taken against the facility by a state agency. | 
**facDateLastInformalAction** | **String** | The date of the most recent informal action or NOV taken recorded in AFS, ICIS-NPDES, RCRA Info or SDWIS. | 
**facDateLastInspection** | **String** | The date on which most recent inspection of the facility took place. For the Clean Air Act, the date on which a Full Inspection (FCE) was completed. This date may or may not correspond to an actual site visit. A series of partial on- or off-site inspections may have been conducted during the fiscal year as part of this FCE. | 
**facDateLastInspectionEPA** | **String** | The date of the facility&#39;s last inspection. | 
**facDateLastInspectionState** | **String** | The date on which the most recent \&quot;olfficial\&quot;  inspection of the facility by a state agency took place. | 
**facDateLastPenalty** | **String** | Indicates the date on which the most recent assessed (or final) penalty was taken against the facility. | 
**facDaysLastInspection** | **String** | The number of days from the last ECHO refresh to the date on which the most recent inspection of the facility took place based on data recorded into AFS, ICIS-NPDES, or RCRA Info. | 
**facDerivedCb2010** | **String** | The 2010 Census Block derived from the facility coordinate. | 
**facDerivedCd113** | **String** | The 113th Congressional District derived from the facility coordinate. | 
**facDerivedHuc** | **String** | The 8-digit Hydrologic Unit Code (HUC) of the watershed in which the facility resides. A HUC number is assigned to every watershed in the nation and uniquely identifies the watershed. | 
**facDerivedRadWBDHu12** | **String** | The 12-digit Watershed Boundary Dataset code derived from Reach Indexing the facility&#39;s spatial coordinate against the 12 digit Watershed Boundary Dataset from USGS. | 
**facDerivedRadWBDHu12Name** | **String** | The 12 digit Watershed Boundary Dataset name derived from Reach Indexing the facility&#39;s spatial coordinate against the 12 digit Watershed Boundary Dataset from USGS. | 
**facDerivedRadWBDHu8** | **String** | The 8-digit Watershed Hydrologic Unit Code (HUC) derived from Reach Indexing the facility&#39;s spatial coordinate against the 12 digit Watershed Boundary Dataset from USGS. | 
**facDerivedRadWBDHu8Name** | **String** | The 8 digit watershed name derived from Reach Indexing the facility&#39;s spatial coordinate against the 12 digit Watershed Boundary Dataset from USGS. | 
**facDerivedStctyFIPS** | **String** | The Federal Information Processing Standard (FIPS) code which uniquely identifies the state and county in which the facility is located. | 
**facDerivedTRIbes** | **String** | The tribes or tribal territories located within 25 miles of the facility&#39;s location. | 
**facDerivedWBD** | **String** | The Hydrologic Unit Code (HUC-12) of the waterbody in which the facility resides, derived based on location data in FRS. | 
**facDerivedWBDHu12Name** | **String** | The Watershed Boundary Dataset name derived from the facility coordinate. | 
**facDerivedWBDHu8** | **String** | Spatially derived HUC based on the facility&#39;s geographic coordinates in FRS. | 
**facDerivedWBDHu8Name** | **String** | The name of the hydrologic unit in which the facility is located within, derived spatially based on the facility&#39;s geographic coordinates in FRS. | 
**facDerivedZip** | **String** | The ZIP Code derived from the facility coordinate. | 
**facEPARegion** | **String** | The EPA region where the facility is located. EPA has 10 regional offices that execute programs within several states and territories | 
**facFIPSCode** | **String** | The 2-digit Federal Information Processing Standards (FIPS) code to identify the county that a facility is located in. | 
**facFederalAgency** | **String** | The facility&#39;s federal agency code. | 
**facFederalAgencyName** | **String** | Indicates the name of the federal agency, as classified in FRS. Federal agencies are installations that are owned and operated by the U.S. government. | 
**facFederalFlg** | **String** | Indicates whether the facility is part of a federal agency. | 
**facFormalActionCount** | **String** | Indicates the total number of enforcement actions taken against the facility within the last five years. NA indicates that this measure is not applicable for facilities with no associated CAA, CWA, or RCRA permits | 
**facImpWaterFlg** | **String** | Indicates whether or not the facility discharges directly into category 4 or 5 impaired water, as designated under section 303(d) of the Clean Water Act. | 
**facIndianCntryFlg** | **String** | Flag showing Y/N whether the facility is located in Indian Country. | 
**facIndianSpatialFlg** | **String** | Returns “Y” if a facility is located within a tribal spatial boundary as defined by the U.S. Census Bureau 2010 tribal boundary layer data for tribes in the lower 48 states and Bureau of Land Management Alaska State Office data for native villages in Alaska. Returns “N” if a facility is not located within a tribal or native Alaskan village area. | 
**facInformalCount** | **String** | Indicates the total number of informal enforcement actions/notices of violations (NOVs) taken against the facility within the last five years | 
**facInspectionCount** | **String** | The number of inspections/compliance evaluations that have occurred at the facility, under the AIR, CWA, and RCRA, within the last five years. The last 5 years will include data from the 20 most recently completed quarters, plus data from the current quarter up until the refresh date. This count only includes inspection types that are counted as inspections in official counts. | 
**facLastPenaltyAmt** | **String** | Indicates the dollar amount of the most recent assessed (or final) penalty taken against the facility. | 
**facLat** | **String** | The latitude of the facility in decimal degrees expressed using the NAD83 horizontal datum. The coordinate comes from the FRS EPA Locational Reference Tables (LRT) file which represents the most accurate value for the facility based on the available spatial metadata. | 
**facLong** | **String** | The longitude of the facility in decimal degrees expressed using the NAD83 horizontal datum. The coordinate comes from the FRS EPA Locational Reference Tables (LRT) file which represents the most accurate value for the facility based on the available spatial metadata. | 
**facMajorFlag** | **String** | Indicates whether the facility is designated as a “major” (usually a large facility). | 
**facMapFlg** | **String** | Graphical indicator denoting whether geographical data required to map a facility are available. | 
**facMapIcon** | **String** | The default map icon image file calculated for the facility by the ECHO program. | 
**facMyrtkUniverse** | **String** | A 3-digit combination of Y/N flags indicating if the facility is considered a Right-to-Know Network (RTKNet) CAA (position 1), NPDES (position 2), or RCRA facility (position 3). | 
**facNAICSCodes** | **String** | The facility&#39;s North American Industry Classification System (NAICS) Codes. | 
**facNaaFlag** | **String** | Indicates whether the facility is located in a nonattainment area of the country, where air pollution levels persistently exceed the national ambient air quality standards. This flag does not indicate whether or not the facility has violated national ambient area quality standards. | 
**facName** | **String** | Name of facility | 
**facPenaltyCount** | **String** | The total number of penalties assessed (or final) taken against the facility within the last five years | 
**facPercentMinority** | **String** | Percent Minority is the percentage of the population of the given area that is considered minority. Statistics are shown for the area within a 3-mile radius of each facility. | 
**facPopDen** | **String** | The number of persons per square mile in the area being profiled. This field is the ratio of total persons (displayed in the Total Persons field) to total land area (displayed in the Land Area field). | 
**facProgramsWithSNC** | **String** | The number of programs (CAA, CWA, SDWA, RCRA) related to the facility that have a current serious violation. | 
**facQtrsWithNC** | **String** | The number of quarters, out of the last twelve quarters, in which the facility is considered in violation. | 
**facReferencePoint** | **String** | A description of the location for the provided facility coordinate. | 
**facSICCodes** | **String** | Indicates the facility’s or permit&#39;s primary Standard Industrial Classification (SIC) Code. The SIC code describes the primary activity of the facility. | 
**facSNCFlg** | **String** | The Significant Non-compliance (SNC) status for the facility during the most recent quarter reflects the time the records were extracted from the program data systems. \&quot;Y\&quot; indicates the facility is in SNC for the permit or site in question and may pose a more severe level of environmental threat. \&quot;N\&quot; indicates the permit or site is not considered in SNC. | 
**facState** | **String** | Facility state | 
**facStdCountyName** | **String** | The standardized  facility county name from EPA&#39;s Facility Registry System | 
**facStreet** | **String** | Street address where facility is located, as maintained by each data system. Certain data systems also maintain mailing address information, which is not used in this report. The street address may differ across EPA databases due to differences in reported information (e.g., use of mailing address), change in ownership, use of parent or subsidiary address, etc. | 
**facTotalPenalties** | **String** | The total dollar amount of either assessed (or final) penalties taken against the facility within the last five years | 
**facUsMexBorderFlg** | **String** | A Y/N flag indicating that the facility is within 100KM of the US-Mexico Border. | 
**facZip** | **String** | Facility ZIP code | 
**fecCaseIDs** | **String** | All Case Numbers of Federal Enforcement Cases relating to the Facility from the ICIS System | 
**fecLastCaseDate** | **String** | The date of the latest Federal Enforcement Case related to this Facility in the ICIS system. | 
**fecNumberOfCases** | **String** | The total number of Federal Enforcement Cases in the last 5 years related to this Facility in the ICIS system. | 
**fecTotalPenalties** | **String** | The total Federal Enforcement Case penalties assessed against this facility in the last 5 years. | 
**fifraInspections5yr** | **String** | From ICIS FE&amp;C, the number of FIFRA inspections at the facility in the past five years. | 
**gHGCO2Releases** | **String** | The sum of total release amounts of all linked Greenhouse Gas IDs reported as \&quot;metric tons of CO2 equivalents\&quot; | 
**gHGFlag** | **String** | Indicates whether the facility has a Greenhouse Gas (GHG) permit. | 
**gHGIDs** | **String** | A unique ID assigned for each facility within EPA’s Greenhouse Gas Reporting Program (GHGRP) Emissions Data Sets. | 
**hasPollRpt** | **String** | ??? | 
**infea5yrFlag** | **String** | Indicates if the facility has an informal enforcement action within the last 5 years. 1 &#x3D; Yes. | 
**insp5yrFlag** | **String** | Indicates if the facility has an inspection within the last 5 years. 1 &#x3D; Yes | 
**lower48** | **String** | Flag showing Y/N whether location is within the contiguous (lower 48) United States. | 
**maxPctileUs** | **String** | The maximum percentile from all individual EJSCREEN indicators. | 
**maxScore** | **String** | A sorting score for internal use. | 
**NC** | **String** | Indicates whether or not the permit or site is considered either in Non-compliance (NC), Significant Non-compliance (SNC) or High Priority violation (HPV) status. | 
**nPDESFlag** | **String** | Indicates whether the facility has a Clean Water Act (CWA) permit. | 
**nPDESIDs** | **String** | Clean Water Act ID from the ICIS-NPDES (Integrated Compliance Information System - National Pollutant Discharge Elimination System) | 
**naaCategories** | **String** | The nonattainment area categories that the facility is in, derived spatially based on the facility&#39;s geographic coordinates in FRS.� | 
**naaPollutants** | **String** | All criteria pollutants that the facility is in nonattainment for. | 
**objectId** | **String** | Sequential number assigned to each facility or cluster returned. | 
**over80CountUs** | **String** | The number of primary EJSCREEN environmental justice (EJ) indexes exceeding the 80th or higher national percentile for the Census block group that the facility is located in. | 
**pctileCancerUs** | **String** | The national percentile of the census block group for the EJSCREEN NATA air toxics cancer risk indicator. | 
**pctileDpmUs** | **String** | The national percentile of the census block group for the EJSCREEN diesel particulate matter indicator. | 
**pctileO3Us** | **String** | The national percentile of the census block group for the EJSCREEN ozone indicator. | 
**pctilePctpre1960Us** | **String** | The national percentile of the census block group for the EJSCREEN Lead paint indicator. | 
**pctilePmUs** | **String** | The national percentile of the census block group for the EJSCREEN particulate matter indicator. | 
**pctileProximityNPDESUs** | **String** | The national percentile of the census block group for the EJSCREEN proximity to major direct water dischargers indicator. | 
**pctileProximityNplUs** | **String** | The national percentile of the census block group for the EJSCREEN proximity to National Priorities List (NPL) sites indicator. | 
**pctileProximityRmpUs** | **String** | The national percentile of the census block group for the EJSCREEN proximity to Risk Management Plan (RMP) sites indicator. | 
**pctileProximityTsdfUs** | **String** | The national percentile of the census block group for the EJSCREEN proximity to Treatment Storage and Disposal Facilities (TSDFs) indicator. | 
**pctileRespUs** | **String** | The national percentile of the census block group for the EJSCREEN NATA respiratory hazard index indicator. | 
**pctileTrafficScoreUs** | **String** | The national percentile of the census block group for the EJSCREEN Traffic proximity and volume indicator. | 
**rCRA3yrComplQtrsHistory** | **String** | The system&#39;s 3-year compliance status history by quarter (3-month period) entered in the RCRA program database. Each character represents a quarter of compliance, going from oldest to most recent. Character values correspond to the following compliance statuses: _ -�No Violation V -�Violation S -�Significant Violation U - Undetermined | 
**rCRAComplianceStatus** | **String** | An indication of the facility&#39;s compliance status under the Resource Conservation and Recovery Act (Significant Violation &#x3D; Significant Noncomplier, Noncompliance, or No Violation). | 
**rCRADateLastFormalAction** | **String** | The effective date of the most recent listed enforcement action entered into the RCRA program database. | 
**rCRADaysLastEvaluation** | **String** | The number of days since a RCRA inspection was completed. | 
**rCRAFlag** | **String** | Indicates whether the facility has a Resource Conservation and Recovery Action (RCRA) permit. | 
**rCRAFormalActionCount** | **String** | Indicates the number of enforcement actions taken against the facility within the last five years under the Resource Conservation and Recovery Act. | 
**rCRAIDs** | **String** | A unique 12-character ID assigned for each record/permit/site/facility within the RCRAInfo database. | 
**rCRAInformalCount** | **String** | Indicates the number of informal enforcement actions/notices of violations (NOVs) taken against the facility within the last five years under the Resource Conservation and Recovery Act. | 
**rCRAInspectionCount** | **String** | The number of inspections/compliance evaluations under the Resource Conservation and Recovery Act, occurring at the facility within the last five years | 
**rCRALastPenaltyAmt** | **String** | The amount of the most recent penalty entered into the RCRA program database. | 
**rCRALastPenaltyDate** | **String** | Indicates the date on which the most recent assessed (or final) penalty was taken against the facility, entered in the RCRAInfo program database. | 
**RCRANAICS** | **String** | The RCRA permit&#39;s primary North American Industry Classification System (NAICS) Code. | 
**rCRAPenalties** | **String** | The total dollar amount of assessed (or final) penalties taken against the facility within the last five years, entered in the RCRAInfo program database. | 
**rCRAPermitTypes** | **String** | RCRA Facility Types include: - TSDF &#x3D; Treatment, Storage and Disposal facility - LQG &#x3D; Large Quantity Generator - SQG &#x3D; Small Quantity Generator - CESQG &#x3D; Conditionally-Exempt Small Quantity Generator - Operating TSDF - Transporters | 
**rCRAQtrsWithNC** | **String** | The number of quarters, out of the last twelve quarters, in which the RCRA permit is considered in violation. | 
**rCRASNCFlag** | **String** | The RCRA Significant Non-compliance (SNC) status for the facility during the most recent quarter reflects the time the records were extracted from the program data systems. \&quot;Y\&quot; indicates the facility is in SNC for the permit or site in question and may pose a more severe level of environmental threat. \&quot;N\&quot; indicates the permit or site is not considered in SNC. | 
**registryID** | **String** | An internal 12-digit Facility Registry Service (FRS) tracking number used to tie all facility data together in EPA regulatory program databases. | 
**rmpIDs** | **String** | A unique ID assigned to each facility submitting a Risk Management Plan to EPA under the Risk Management Plan Rule. | 
**sDWA3yrComplQtrsHistory** | **String** | The system&#39;s 3-year compliance status history by quarter (3-month period). Each character represents a quarter of compliance, going from oldest to most recent. Character values correspond to the following compliance statuses: _ - No Violation Identified V - Noncompliance S - Significant Noncompliance U - Undetermined | 
**sDWAComplianceStatus** | **String** | An indication of the facility&#39;s compliance status under the Safe Drinking Water Act (Serious Violator, Noncompliance, or No Violation). | 
**sDWAFormalActionCount** | **String** | Indicates the number of enforcement actions taken against the facility within the last five years under the Safe Drinking Water Act | 
**sDWAIDs** | **String** | A unique 9-character ID assigned for each public water system within the Safe Drinking Water Information System (SDWIS). | 
**sDWAInformalCount** | **String** | Indicates the number of informal enforcement actions/notices of violations (NOVs) taken against the facility within the last five years under the Safe Drinking Water Act | 
**sDWAInspections5yr** | **String** | The number of SDWA inspections at the facility in the past five years. | 
**sDWAQtrsWithNC** | **String** | The number of quarters, out of the last twelve quarters, in which the SDWA permit is considered in violation. | 
**sDWASNCFlag** | **String** | Indicates whether the Water System has a Serious Violation. | 
**sDWASystemTypes** | **String** | SDWIS System Types | 
**sDWISFlag** | **String** | Indicates whether the facility has a Safe Drinking Water Information System (SDWIS) ID. | 
**score** | **String** |  | 
**semsFlag** | **String** |  | 
**semsIDs** | **String** |  | 
**sourceID** | **String** | Unique Identifier assigned by EPA. | 
**tRIFlag** | **String** | Indicates whether the facility has a Toxics Release Inventory (TRI) permit. | 
**tRIIDs** | **String** | A unique 15-character ID assigned for each facility within the Toxics Release Inventory (TRI) program. The format is ZZZZZNNNNNSSSSS, where ZZZZZ &#x3D; ZIP code, NNNNN &#x3D; the first 5 consonants of the name, and SSSSS &#x3D; the first 5 non-blank non-special characters in the street address. | 
**tRIOffSiteTransfers** | **String** | Total pounds per year transferred off-site. | 
**tRIOnSiteReleases** | **String** | Total pounds per year released for Air Emissions, Surface Water Discharges, Underground Injections and Releases to Land. | 
**tRIReleasesTransfers** | **String** | Total chemical releases, in pounds, as reported to the Toxics Release Inventory (TRI) by the facility for the most recent reporting year | 
**tRIReporter** | **String** | Indicates whether or not the facility reported to the Toxics Release Inventory (TRI) for the most recent reporting year. | 
**tRIReporterInPast** | **String** | A &#39;Y&#39; indicates a TRI Reporter from a prior year. | 
**tRIbalFlag** | **String** | A flag indicating that the facility is within a tribal area. | 
**tscaFlag** | **String** | Flag indicating whether or not a facility has a TSCA ID | 
**tscaIDs** | **String** | Toxic Substances Control Act ID assigned to a facility | 
**tscaInspections5yr** | **String** | From ICIS FE&amp;C, the number of TSCA inspections at the facility in the past five years. | 
**violFlag** | **String** | Indicates if the facility had a violation within the last 3 years. 1 &#x3D; Yes | 
**webDocs** | **String** | Contains flags that identify what web accessible documents are available for the facility. | 


