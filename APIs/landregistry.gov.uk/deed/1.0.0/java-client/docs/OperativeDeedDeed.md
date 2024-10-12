

# OperativeDeedDeed

Unique deed, consisting of property, borrower and charge information as well as clauses for the deed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalProvisions** | [**List&lt;AdditionalProvisionsInner&gt;**](AdditionalProvisionsInner.md) |  |  [optional] |
|**borrowers** | [**List&lt;Borrower&gt;**](Borrower.md) |  |  [optional] |
|**chargeClause** | [**ChargeClause**](ChargeClause.md) |  |  [optional] |
|**deedStatus** | **String** | Current state of the deed |  [optional] |
|**effectiveClause** | **String** | Text to display the make effective clause |  [optional] |
|**lender** | [**Lender**](Lender.md) |  |  [optional] |
|**mdRef** | **String** | Land Registry assigned number for a Mortgage Deed (MD). If you wish to use an existing MD reference please prefix it with e- to comply with our system (eg e-MD12345) |  [optional] |
|**propertyAddress** | **String** | The address of property that the deed relates. This should be supplied in a comma separated format e.g. 30 wakefield rd, plymouth, PL6 3WA |  [optional] |
|**titleNumber** | **String** | Unique Land Registry identifier for the registered estate. |  [optional] |



