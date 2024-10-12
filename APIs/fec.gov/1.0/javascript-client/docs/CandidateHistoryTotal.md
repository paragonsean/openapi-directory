# OpenFec.CandidateHistoryTotal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeThrough** | **Number** | Last year a candidate was active. This field is specific to the candidate_id so if the same person runs for another office, there may be a different record for them. | [optional] 
**addressCity** | **String** | City of candidate&#39;s address, as reported on their Form 2. | [optional] 
**addressState** | **String** | State of candidate&#39;s address, as reported on their Form 2. | [optional] 
**addressStreet1** | **String** | Street of candidate&#39;s address, as reported on their Form 2. | [optional] 
**addressStreet2** | **String** | Additional street information of candidate&#39;s address, as reported on their Form 2. | [optional] 
**addressZip** | **String** | Zip code of candidate&#39;s address, as reported on their Form 2. | [optional] 
**candidateElectionYear** | **Number** | The last year of the cycle for this election. | [optional] 
**candidateId** | **String** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | 
**candidateInactive** | **Boolean** |  True indicates that a candidate is inactive.  | [optional] 
**candidateStatus** | **String** | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional] 
**cashOnHandEndPeriod** | **Number** | Ending cash balance on the most recent filing | [optional] 
**coverageEndDate** | **Date** | Ending date of the reporting period | [optional] 
**coverageStartDate** | **Date** | Beginning date of the reporting period | [optional] 
**cycle** | **Number** |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  | 
**cycles** | **[Number]** |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | [optional] 
**debtsOwedByCommittee** | **Number** | Debts owed by the committee | [optional] 
**disbursements** | **Number** |  | [optional] 
**district** | **String** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
**districtNumber** | **Number** | One-letter code explaining if the candidate is:         - C present candidate         - F future candidate         - N not yet a candidate         - P prior candidate  | [optional] 
**electionDistricts** | **[String]** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. | [optional] 
**electionYear** | **Number** | Year of election | [optional] 
**electionYears** | **[Number]** | Years in which a candidate ran for office. | [optional] 
**fecCyclesInElection** | **[Number]** | FEC cycles are included in candidate election years. | [optional] 
**federalFundsFlag** | **Boolean** | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. | [optional] 
**firstFileDate** | **Date** | The day the FEC received the candidate&#39;s first filing. This is a F2 candidate registration. | [optional] 
**flags** | **String** |  | [optional] 
**hasRaisedFunds** | **Boolean** | A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) | [optional] 
**incumbentChallenge** | **String** | One-letter code (&#39;I&#39;, &#39;C&#39;, &#39;O&#39;) explaining if the candidate is an incumbent, a challenger, or if the seat is open. | [optional] 
**incumbentChallengeFull** | **String** | Explains if the candidate is an incumbent, a challenger, or if the seat is open. | [optional] 
**individualItemizedContributions** | **Number** | Individual itemized contributions are from individuals whose aggregate contributions total over $200 per individual per year. Be aware, some filers choose to itemize donations $200 or less. | [optional] 
**isElection** | **Boolean** |  | 
**lastF2Date** | **Date** | The day the FEC received the candidate&#39;s most recent Form 2 | [optional] 
**lastFileDate** | **Date** | The day the FEC received the candidate&#39;s most recent filing | [optional] 
**loadDate** | **Date** | Date the information was loaded into the FEC systems. This can be affected by reseting systems and other factors, refer to receipt_date for the day that the FEC received the paper or electronic document. Keep in mind that paper filings take more time to process and there can be a lag between load_date and receipt_date. This field can be helpful to identify paper records that have been processed recently. | [optional] 
**name** | **String** | Name of candidate running for office | [optional] 
**office** | **String** | Federal office candidate runs for: H, S or P | [optional] 
**officeFull** | **String** | Federal office candidate runs for: House, Senate or presidential | [optional] 
**otherPoliticalCommitteeContributions** | **Number** | Other committees contributions | [optional] 
**party** | **String** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**partyFull** | **String** | Party affiliated with a candidate or committee | [optional] 
**receipts** | **Number** |  | [optional] 
**roundedElectionYears** | **[Number]** | Rounded election years in which a candidate ran for office | [optional] 
**state** | **String** | US state or territory where a candidate runs for office | [optional] 
**stateFull** | **String** | US state or territory where a candidate runs for office | [optional] 
**transfersFromOtherAuthorizedCommittee** | **Number** | Transfers from authorized committees | [optional] 
**twoYearPeriod** | **Number** |  Two-year election cycle in which a candidate runs for office. Calculated from Form 2. The cycle begins with an odd year and is named for its ending, even year. This cycle follows the traditional house election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. To retrieve data for the entire four years of a presidential term or six years of a senatorial term, you will need the &#x60;election_full&#x60; flag.  | 


