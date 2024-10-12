

# PresidentialByCandidate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**candidateId** | **String** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.   -P00000001    All candidates   -P00000002    Democrasts   -P00000003    Republicans  |  [optional] |
|**candidateLastName** | **String** |  Candidate last name  |  [optional] |
|**candidatePartyAffiliation** | **String** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. |  [optional] |
|**contributorState** | **String** | State of contributor |  [optional] |
|**electionYear** | **Integer** | Year of election |  [optional] |
|**netReceipts** | **BigDecimal** | Net contributions |  [optional] |
|**roundedNetReceipts** | **BigDecimal** |  Net receipts, in millions  |  [optional] |



