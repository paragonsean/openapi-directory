# NaviPlanApi.IHoldingCompany

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annualDividendYield** | [**Percent**](Percent.md) |  | [optional] 
**ccpc** | [**DescriptiveBoolean**](DescriptiveBoolean.md) |  | [optional] 
**commonSharesOutstanding** | **Number** |  | [optional] [readonly] 
**contributions** | [**IContributions**](IContributions.md) |  | [optional] 
**corporateYearEnd** | [**ModelDate**](ModelDate.md) |  | [optional] 
**description** | **String** |  | [optional] [readonly] 
**dividendType** | **String** |  | [optional] [readonly] 
**dividendTypeFormatted** | **String** |  | [optional] [readonly] 
**estateDetails** | [**IEstateDetails**](IEstateDetails.md) |  | [optional] 
**historicalData** | [**IHistoricalData**](IHistoricalData.md) |  | [optional] 
**id** | **String** |  | [optional] [readonly] 
**investmentAccounts** | [**[IInvestmentAccount]**](IInvestmentAccount.md) |  | [optional] [readonly] 
**liabilities** | [**[ILiability]**](ILiability.md) |  | [optional] [readonly] 
**lifeInsurancePolicies** | [**[ILifeInsurancePolicy]**](ILifeInsurancePolicy.md) |  | [optional] [readonly] 
**marketValue** | [**Currency**](Currency.md) |  | [optional] 
**numPreferredShareClasses** | **Number** |  | [optional] [readonly] 
**otherAssets** | [**[IRealEstateAsset]**](IRealEstateAsset.md) |  | [optional] [readonly] 
**ownershipAsOfDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**ownershipDetails** | [**IOwnershipDetails**](IOwnershipDetails.md) |  | [optional] 
**preferredSharesOutstanding** | **Number** |  | [optional] [readonly] 
**provinceOfIncorporation** | **String** |  | [optional] [readonly] 
**provinceOfTaxation** | **String** |  | [optional] [readonly] 
**realEstateAssets** | [**[ICorporationRealEstateAsset]**](ICorporationRealEstateAsset.md) |  | [optional] [readonly] 
**valueOfAllCommonShares** | [**Currency**](Currency.md) |  | [optional] 
**valueOfAllPreferredShares** | [**Currency**](Currency.md) |  | [optional] 
**withdrawals** | [**IWithdrawals**](IWithdrawals.md) |  | [optional] 



## Enum: DividendTypeEnum


* `Taxable` (value: `"Taxable"`)

* `NonTaxable` (value: `"NonTaxable"`)




