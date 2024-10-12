

# IHoldingCompany


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annualDividendYield** | [**Percent**](Percent.md) |  |  [optional] |
|**ccpc** | [**DescriptiveBoolean**](DescriptiveBoolean.md) |  |  [optional] |
|**commonSharesOutstanding** | **Integer** |  |  [optional] [readonly] |
|**contributions** | [**IContributions**](IContributions.md) |  |  [optional] |
|**corporateYearEnd** | [**Date**](Date.md) |  |  [optional] |
|**description** | **String** |  |  [optional] [readonly] |
|**dividendType** | [**DividendTypeEnum**](#DividendTypeEnum) |  |  [optional] [readonly] |
|**dividendTypeFormatted** | **String** |  |  [optional] [readonly] |
|**estateDetails** | [**IEstateDetails**](IEstateDetails.md) |  |  [optional] |
|**historicalData** | [**IHistoricalData**](IHistoricalData.md) |  |  [optional] |
|**id** | **String** |  |  [optional] [readonly] |
|**investmentAccounts** | [**List&lt;IInvestmentAccount&gt;**](IInvestmentAccount.md) |  |  [optional] [readonly] |
|**liabilities** | [**List&lt;ILiability&gt;**](ILiability.md) |  |  [optional] [readonly] |
|**lifeInsurancePolicies** | [**List&lt;ILifeInsurancePolicy&gt;**](ILifeInsurancePolicy.md) |  |  [optional] [readonly] |
|**marketValue** | [**Currency**](Currency.md) |  |  [optional] |
|**numPreferredShareClasses** | **Integer** |  |  [optional] [readonly] |
|**otherAssets** | [**List&lt;IRealEstateAsset&gt;**](IRealEstateAsset.md) |  |  [optional] [readonly] |
|**ownershipAsOfDate** | [**Date**](Date.md) |  |  [optional] |
|**ownershipDetails** | [**IOwnershipDetails**](IOwnershipDetails.md) |  |  [optional] |
|**preferredSharesOutstanding** | **Integer** |  |  [optional] [readonly] |
|**provinceOfIncorporation** | **String** |  |  [optional] [readonly] |
|**provinceOfTaxation** | **String** |  |  [optional] [readonly] |
|**realEstateAssets** | [**List&lt;ICorporationRealEstateAsset&gt;**](ICorporationRealEstateAsset.md) |  |  [optional] [readonly] |
|**valueOfAllCommonShares** | [**Currency**](Currency.md) |  |  [optional] |
|**valueOfAllPreferredShares** | [**Currency**](Currency.md) |  |  [optional] |
|**withdrawals** | [**IWithdrawals**](IWithdrawals.md) |  |  [optional] |



## Enum: DividendTypeEnum

| Name | Value |
|---- | -----|
| TAXABLE | &quot;Taxable&quot; |
| NON_TAXABLE | &quot;NonTaxable&quot; |



