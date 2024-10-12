# OpenFec.PresidentialSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidateContributionsLessRepayments** | **Number** |  candidate contributions less repayments  | [optional] 
**candidateId** | **String** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.   -P00000001    All candidates   -P00000002    Democrasts   -P00000003    Republicans  | [optional] 
**candidateLastName** | **String** |  Candidate last name  | [optional] 
**candidateName** | **String** | Name of candidate running for office | [optional] 
**candidatePartyAffiliation** | **String** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. | [optional] 
**cashOnHandEnd** | **Number** | Ending cash balance on the most recent filing | [optional] 
**committeeDesignation** | **String** | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
**committeeId** | **String** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
**committeeName** | **String** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. | [optional] 
**committeeType** | **String** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
**debtsOwedByCommittee** | **Number** | Debts owed by the committee | [optional] 
**disbursementsLessOffsets** | **Number** |  disbursements less offsets  | [optional] 
**electionYear** | **Number** | Year of election | [optional] 
**exemptLegalAccountingDisbursement** | **Number** |  exempt legal accounting disbursement  | [optional] 
**federalFunds** | **Number** | Federal funds: Public funding of presidential elections means that qualified presidential candidates                 receive federal government funds to pay for the valid expenses of their political campaigns                 in both the primary and general elections. | [optional] 
**fundraisingDisbursements** | **Number** |  fundraising disbursements  | [optional] 
**individualContributionsLessRefunds** | **Number** |  individual contributions less refunds  | [optional] 
**netReceipts** | **Number** |  Contributions received  | [optional] 
**offsetsToOperatingExpenditures** | **Number** | Offsets to operating expenditures | [optional] 
**operatingExpenditures** | **Number** | Total operating expenditures | [optional] 
**otherDisbursements** | **Number** | Other disbursements | [optional] 
**pacContributionsLessRefunds** | **Number** |  pac contributions less refunds  | [optional] 
**partyContributionsLessRefunds** | **Number** |  party contributions less refunds  | [optional] 
**repaymentsLoansMadeByCandidate** | **Number** |  repayments loans made by candidate  | [optional] 
**repaymentsOtherLoans** | **Number** |  repayments other loans  | [optional] 
**roundedNetReceipts** | **Number** |  Net receipts, in millions  | [optional] 
**totalContributionRefunds** | **Number** |  total contribution refunds  | [optional] 
**totalLoanRepaymentsMade** | **Number** |  total loan repayments made  | [optional] 
**transfersFromAffiliatedCommittees** | **Number** |  transfers from affiliated committees  | [optional] 
**transfersToOtherAuthorizedCommittees** | **Number** |  transfers to other authorized committees  | [optional] 


