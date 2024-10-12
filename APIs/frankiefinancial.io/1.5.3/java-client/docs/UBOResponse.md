

# UBOResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**asicSearchTimestamp** | **OffsetDateTime** | If an ASIC search was conducted, what was the date/time in RFC-3339 format  |  [optional] |
|**businessDetails** | [**BusinessDetails**](BusinessDetails.md) |  |  [optional] |
|**businessScreeningResult** | [**ScreeningResult**](ScreeningResult.md) |  |  [optional] |
|**errorMessage** | **String** | Only populated if there was an error whilst trying to initiate the UBO check.  Signifies that no other result data will be supplied  |  [optional] |
|**issuesList** | [**List&lt;IssueListItems&gt;**](IssueListItems.md) | A list of issues encountered whilst processing the UBO request and subsequent KYC/AML checks.  |  [optional] |
|**nonIndividualBeneficialOwners** | [**List&lt;NonIndividualBeneficialOwner&gt;**](NonIndividualBeneficialOwner.md) | A list of organisations who have been determined to own a (potentially) beneficial interest the company.  The presence of non_individual_beneficial_owners indicates that not all individual ultimate beneficial owners could be determined.  Examples may include public companies, listed companies, foreign companies, corporate trusts or other entities whose beneficial owners are not readily available.  |  [optional] |
|**officeholders** | [**List&lt;IndividualData&gt;**](IndividualData.md) | A list of individuals who serve as current office holders the company  |  [optional] |
|**suppliedData** | [**SuppliedData**](SuppliedData.md) |  |  |
|**suppliedDataMatches** | [**SuppliedDataMatches**](SuppliedDataMatches.md) |  |  [optional] |
|**uboReport** | **String** | The full URI of the UBO report PDF created as a part of this process (if requested)  |  [optional] |
|**ultimateBeneficialOwners** | [**List&lt;IndividualData&gt;**](IndividualData.md) | A list of individuals who have been determined to own, either directly or indirectly, 25% or more of the company  |  [optional] |



