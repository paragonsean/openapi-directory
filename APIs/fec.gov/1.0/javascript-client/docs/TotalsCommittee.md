# OpenFec.TotalsCommittee

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliatedCommitteeName** | **String** |  Affiliated committee or connected organization  | [optional] 
**candidateIds** | **[String]** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
**cashOnHandEndPeriod** | **Number** |  | [optional] 
**city** | **String** |  City of committee as reported on the Form 1  | [optional] 
**committeeId** | **String** |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | 
**committeeType** | **String** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**committeeTypeFull** | **String** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**cycle** | **Number** |  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | 
**cycles** | **[Number]** |  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1s) The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
**cyclesHasActivity** | **[Number]** |  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1), and the committee has filling activity during the cycle  | [optional] 
**cyclesHasFinancial** | **[Number]** |  A two year election cycle that the committee was active- (after original registration date but before expiration date in Form 1s), and the committee files the financial reports (&#39;F3&#39;, &#39;F3X&#39;, &#39;F3P&#39;, &#39;F3L&#39;, &#39;F4&#39;, &#39;F5&#39;, &#39;F7&#39;, &#39;F13&#39;) during this cycle.  | [optional] 
**debtsOwedByCommittee** | **Number** |  | [optional] 
**designation** | **String** | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
**designationFull** | **String** | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
**disbursements** | **Number** |  | [optional] 
**filingFrequency** | **String** | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  | [optional] 
**firstF1Date** | **Date** | The day the FEC received the committee&#39;s first Form 1 | [optional] 
**firstFileDate** | **Date** | The day the FEC received the committee&#39;s first filing. This is usually a Form 1 committee registration. | [optional] 
**independentExpenditures** | **Number** |  | [optional] 
**isActive** | **Boolean** |  True indicates that a committee is active.  | [optional] 
**jfcCommittee** | [**[CommitteeDetailJfcCommitteeInner]**](CommitteeDetailJfcCommitteeInner.md) |  | [optional] 
**lastCycleHasActivity** | **Number** |  The latest two year election cycle that the committee has filings  | [optional] 
**lastCycleHasFinancial** | **Number** |  The latest two year election cycle that the committee files the financial reports (&#39;F3&#39;, &#39;F3X&#39;, &#39;F3P&#39;, &#39;F3L&#39;, &#39;F4&#39;, &#39;F5&#39;, &#39;F7&#39;, &#39;F13&#39;).  | [optional] 
**lastF1Date** | **Date** | The day the FEC received the committee&#39;s most recent Form 1 | [optional] 
**lastFileDate** | **Date** | The day the FEC received the committee&#39;s most recent filing | [optional] 
**name** | **String** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**organizationType** | **String** | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
**organizationTypeFull** | **String** | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
**party** | **String** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**partyFull** | **String** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**receipts** | **Number** |  | [optional] 
**state** | **String** |  State of the committee&#39;s address as filed on the Form 1  | [optional] 
**stateFull** | **String** |  State of committee as reported on the Form 1  | [optional] 
**street1** | **String** |  Street address of committee as reported on the Form 1  | [optional] 
**street2** | **String** |  Second line of street address of committee as reported on the Form 1  | [optional] 
**treasurerName** | **String** | Name of the Committee&#39;s treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown. | [optional] 
**zip** | **String** |  Zip code of committee as reported on the Form 1  | [optional] 


