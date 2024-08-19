

# Rcra07

Facilities Object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aiRIDs** | **String** | Air Facility System (AFS) ID. |  |
|**activeLower48** | **String** | A Y/N indicator indicating that the facility is active and located within the lower 48 contiguous US States. |  |
|**cwAIDs** | **String** | A unique  ID assigned for each record/permit/site/facility within ICIS-NPDES. These identifiers are for used tracking purposes in the individual data systems. |  |
|**calculatedAccuracyMeters** | **String** | The estimated accuracy in Meters for the facility&#39;s geospatial coordinate. |  |
|**censusBlockGroup** | **String** | A geographic unit used by the United States Census Bureau, generally defined to contain between 600 and 3,000 people. |  |
|**chemNamesRelLand** | **String** | It is an aggregated field containing all the names found for the current reporting year (2017). |  |
|**chesapeakeBayFlag** | **String** | Displays \&quot;Y\&quot; if the facility is located within the Chesapeake Bay watershed. |  |
|**cleanupActionFlag** | **String** |  |  |
|**collectionMethod** | **String** | ?? |  |
|**currSvFlag** | **String** | Indicates if the facility has a current significant violation. 1 &#x3D; Yes |  |
|**currVioFlag** | **String** | Indicates if the facility has a current violation. 1 &#x3D; Yes |  |
|**currentVioCnt** | **String** |  |  |
|**dateLastRecordReview** | **String** |  |  |
|**epASystem** | **String** | The EPA data system in which permit and facility records are kept. EPA&#39;s Facility Registry System (FRS) links all program database records (such as permit IDs and IDs facilities use in reporting to EPA) together. The following list describes the individual data systems that are linked to from the detailed facility report:   - AFS: Air Facility System for Clean Air Act stationary source programs. - ICP: Integrated Compliance Information System for Clean Water Act programs monitoring National Pollutant Discharge Elimination System (NPDES) permits. - RCR: Resource Conservation and Recovery Act Information System (RCRAInfo) for tracking the Resource Conservation and Recovery Act (RCRA) programs. - NCDB: National Compliance Database System for monitoring national performance of the Toxic Substance Control Act (TSCA); the Emergency Planning and Right-to-Know Act, Section 313 (EPCRA); the Asbestos Hazard Emergency Response (AHERA); and the Federal Insecticide, Fungicide, and Rodenticide Act (FIFRA). - TRI: Toxics Release Inventory for Emergency Planning and Community Right-to-Know Act, Section 313 submissions. - NEI: National Emissions Inventory database contains information on stationary and mobile sources that emit criteria air pollutants and their precursors, as well as hazardous air pollutants (HAPs). The database includes estimates of annual emissions, by source, of air pollutants in each area of the country, on an annual basis. - TSCA: Toxic Substances Control Act addressing the production, importation, use, and disposal of specific chemicals. |  |
|**ea5yrFlag** | **String** | Indicates if the facility has a formal enforcement action within the last 5 years. 1 &#x3D; Yes |  |
|**ejscreenFlag** | **String** | A Y/N indicator identifying whether or not the facility is within an Environmental Justice area. |  |
|**ejscreenFlagUs** | **String** | A Y/N indicator identifying whether or not the facility is within an Environmental Justice area. |  |
|**facCountyName** | **String** | The facility county name from EPA&#39;s Facility Registry System |  |
|**facDerivedHuc** | **String** | The 8-digit Hydrologic Unit Code (HUC) of the watershed in which the facility resides. A HUC number is assigned to every watershed in the nation and uniquely identifies the watershed. |  |
|**facDerivedTRIbes** | **String** | The tribes or tribal territories located within 25 miles of the facility&#39;s location. |  |
|**facDerivedWBD** | **String** | The Hydrologic Unit Code (HUC-12) of the waterbody in which the facility resides, derived based on location data in FRS. |  |
|**facDerivedWBDName** | **String** | The 12 digit Watershed Boundary Dataset Name derived from the FRS Best Pick Coordinate |  |
|**facFIPSCode** | **String** | The 2-digit Federal Information Processing Standards (FIPS) code to identify the county that a facility is located in. |  |
|**facFederalAgencyCode** | **String** | Indicates the federal agency, as classified in FRS. Federal agencies are installations that are owned and operated by the U.S. government. The five-character code consists of a letter followed by four numbers. There are four possible letters that can occupy the first character position: C &#x3D; Civilian Federal Agency; D &#x3D; Department of Defense; E &#x3D; Department of Energy; X &#x3D; Unknown. The second and third characters represent the agency code, while the fourth and fifth characters represent the bureau code. |  |
|**facFederalAgencyName** | **String** | Indicates the name of the federal agency, as classified in FRS. Federal agencies are installations that are owned and operated by the U.S. government. |  |
|**facIndianCntryFlg** | **String** | Flag showing Y/N whether the facility is located in Indian Country. |  |
|**facIndianSpatialFlg** | **String** | Returns “Y” if a facility is located within a tribal spatial boundary as defined by the U.S. Census Bureau 2010 tribal boundary layer data for tribes in the lower 48 states and Bureau of Land Management Alaska State Office data for native villages in Alaska. Returns “N” if a facility is not located within a tribal or native Alaskan village area. |  |
|**facLat** | **String** | The latitude of the facility in decimal degrees expressed using the NAD83 horizontal datum. The coordinate comes from the FRS EPA Locational Reference Tables (LRT) file which represents the most accurate value for the facility based on the available spatial metadata. |  |
|**facLong** | **String** | The longitude of the facility in decimal degrees expressed using the NAD83 horizontal datum. The coordinate comes from the FRS EPA Locational Reference Tables (LRT) file which represents the most accurate value for the facility based on the available spatial metadata. |  |
|**facMapFlg** | **String** | Graphical indicator denoting whether geographical data required to map a facility are available. |  |
|**facMapIcon** | **String** | The default map icon image file calculated for the facility by the ECHO program. |  |
|**facPercentMinority** | **String** | Percent Minority is the percentage of the population of the given area that is considered minority. Statistics are shown for the area within a 3-mile radius of each facility. |  |
|**facPopulationDensity** | **String** | The number of persons per square mile in the profiled area. |  |
|**facSICCodes** | **String** | Indicates the facility’s or permit&#39;s primary Standard Industrial Classification (SIC) Code. The SIC code describes the primary activity of the facility. |  |
|**facStdCountyName** | **String** | The standardized  facility county name from EPA&#39;s Facility Registry System |  |
|**facTRILandReleases** | **String** |  |  |
|**facTRIOffSiteTransfers** | **String** |  |  |
|**facTRIOnSiteReleases** | **String** |  |  |
|**facTRIReporter** | **String** | Indicates whether facility reported to the Toxics Release Inventory (TRI) for the most recent reporting year. |  |
|**facUsMexBorderFlg** | **String** | A Y/N flag indicating that the facility is within 100KM of the US-Mexico Border. |  |
|**infea5yrFlag** | **String** | Indicates if the facility has an informal enforcement action within the last 5 years. 1 &#x3D; Yes. |  |
|**insp5yrFlag** | **String** | Indicates if the facility has an inspection within the last 5 years. 1 &#x3D; Yes |  |
|**lastViolationDate** | **String** |  |  |
|**lower48** | **String** | Flag showing Y/N whether location is within the contiguous (lower 48) United States. |  |
|**map** | **String** | No Longer Used. |  |
|**maxPctileUs** | **String** | The maximum percentile from all individual EJSCREEN indicators. |  |
|**maxScore** | **String** | A sorting score for internal use. |  |
|**objectId** | **String** | Sequential number assigned to each facility or cluster returned. |  |
|**operatorCode** | **String** |  |  |
|**operatorDesc** | **String** |  |  |
|**over80CountUs** | **String** | The number of primary EJSCREEN environmental justice (EJ) indexes exceeding the 80th or higher national percentile for the Census block group that the facility is located in. |  |
|**ownerCode** | **String** |  |  |
|**ownerDesc** | **String** | Description of Owner code |  |
|**pctileCancerUs** | **String** | The national percentile of the census block group for the EJSCREEN NATA air toxics cancer risk indicator. |  |
|**pctileDpmUs** | **String** | The national percentile of the census block group for the EJSCREEN diesel particulate matter indicator. |  |
|**pctileO3Us** | **String** | The national percentile of the census block group for the EJSCREEN ozone indicator. |  |
|**pctilePctpre1960Us** | **String** | The national percentile of the census block group for the EJSCREEN Lead paint indicator. |  |
|**pctilePmUs** | **String** | The national percentile of the census block group for the EJSCREEN particulate matter indicator. |  |
|**pctileProximityNPDESUs** | **String** | The national percentile of the census block group for the EJSCREEN proximity to major direct water dischargers indicator. |  |
|**pctileProximityNplUs** | **String** | The national percentile of the census block group for the EJSCREEN proximity to National Priorities List (NPL) sites indicator. |  |
|**pctileProximityRmpUs** | **String** | The national percentile of the census block group for the EJSCREEN proximity to Risk Management Plan (RMP) sites indicator. |  |
|**pctileProximityTsdfUs** | **String** | The national percentile of the census block group for the EJSCREEN proximity to Treatment Storage and Disposal Facilities (TSDFs) indicator. |  |
|**pctileRespUs** | **String** | The national percentile of the census block group for the EJSCREEN NATA respiratory hazard index indicator. |  |
|**pctileTrafficScoreUs** | **String** | The national percentile of the census block group for the EJSCREEN Traffic proximity and volume indicator. |  |
|**rcRA3yrComplQtrsHistory** | **String** | The system&#39;s 3-year compliance status history by quarter (3-month period) entered in the RCRA program database. Each character represents a quarter of compliance, going from oldest to most recent. Character values correspond to the following compliance statuses: _ -�No Violation V -�Violation S -�Significant Violation U - Undetermined |  |
|**rcRACaseIDs** | **String** |  |  |
|**rcRACity** | **String** |  |  |
|**rcRAComplStatus** | **String** |  |  |
|**rcRACounty** | **String** |  |  |
|**rcRADaysLastInspection** | **String** |  |  |
|**rcRAEPARegion** | **String** |  |  |
|**rcRAFIPSCode** | **String** |  |  |
|**rcRAFeaCnt** | **String** |  |  |
|**rcRAIDs** | **String** | A unique 12-character ID assigned for each record/permit/site/facility within the RCRAInfo database. |  |
|**rcRAIeaCnt** | **String** |  |  |
|**rcRAImpWaterFlg** | **String** |  |  |
|**rcRAIndianCntryFlg** | **String** |  |  |
|**rcRAInspCnt** | **String** |  |  |
|**rcRALandTypeCode** | **String** |  |  |
|**rcRALastFeaDate** | **String** |  |  |
|**rcRALastFeaDateEPA** | **String** |  |  |
|**rcRALastFeaDateState** | **String** |  |  |
|**rcRALastIeaDate** | **String** |  |  |
|**rcRALastIeaDateEPA** | **String** |  |  |
|**rcRALastIeaDateState** | **String** |  |  |
|**rcRALastInspDateEPA** | **String** |  |  |
|**rcRALastInspDateState** | **String** |  |  |
|**rcRALastInspectionDate** | **String** |  |  |
|**rcRALastPenaltyDate** | **String** | Indicates the date on which the most recent assessed (or final) penalty was taken against the facility, entered in the RCRAInfo program database. |  |
|**rcRAMapIcon** | **String** |  |  |
|**RCRANAICS** | **String** | The RCRA permit&#39;s primary North American Industry Classification System (NAICS) Code. |  |
|**rcRAName** | **String** |  |  |
|**rcRAOldestOpenVioDate** | **String** |  |  |
|**rcRAPenalties** | **String** | The total dollar amount of assessed (or final) penalties taken against the facility within the last five years, entered in the RCRAInfo program database. |  |
|**rcRAQtrsWithNC** | **String** | The number of quarters, out of the last twelve quarters, in which the RCRA permit is considered in violation. |  |
|**rcRAQtrsWithSNC** | **String** |  |  |
|**RCRASNC** | **String** |  |  |
|**rcRAState** | **String** |  |  |
|**rcRAStateDistrict** | **String** |  |  |
|**rcRAStatus** | **String** |  |  |
|**rcRAStreet** | **String** |  |  |
|**rcRATRIbalLandCode** | **String** |  |  |
|**rcRAUniverse** | **String** |  |  |
|**rcRAViolationTypes** | **String** |  |  |
|**rcRAZip** | **String** |  |  |
|**rcRAinfoLandTypeCode** | **String** |  |  |
|**rcRAinfoLandTypeDesc** | **String** |  |  |
|**referencePoint** | **String** | ?? |  |
|**registryID** | **String** | An internal 12-digit Facility Registry Service (FRS) tracking number used to tie all facility data together in EPA regulatory program databases. |  |
|**rmpIDs** | **String** | A unique ID assigned to each facility submitting a Risk Management Plan to EPA under the Risk Management Plan Rule. |  |
|**sdWAIDs** | **String** | A unique 9-character ID assigned for each public water system within the Safe Drinking Water Information System (SDWIS). |  |
|**score** | **String** |  |  |
|**semsIDs** | **String** |  |  |
|**sourceID** | **String** | Unique Identifier assigned by EPA. |  |
|**statute** | **String** | The name of the statute associated with each of the permits and identifiers linked to the facility:  - CAA &#x3D; the Clean Air Act - CWA &#x3D; the Clean Water Act - RCRA &#x3D; the Resource Conservation and Recovery Act - EP313 &#x3D; the Emergency Planning and Community Right-to-Know Act, Section 313 (also known as the Toxics Release Inventory Program) - TSCA &#x3D; the Toxic Substances Control Act - SDWA &#x3D; the Safe Drinking Water Act |  |
|**trIIDs** | **String** | A unique 15-character ID assigned for each facility within the Toxics Release Inventory (TRI) program. The format is ZZZZZNNNNNSSSSS, where ZZZZZ &#x3D; ZIP code, NNNNN &#x3D; the first 5 consonants of the name, and SSSSS &#x3D; the first 5 non-blank non-special characters in the street address. |  |
|**trIbalFlag** | **String** | A flag indicating that the facility is within a tribal area. |  |
|**tsdf** | **String** |  |  |
|**violFlag** | **String** | Indicates if the facility had a violation within the last 3 years. 1 &#x3D; Yes |  |
|**webDocs** | **String** | Contains flags that identify what web accessible documents are available for the facility. |  |



