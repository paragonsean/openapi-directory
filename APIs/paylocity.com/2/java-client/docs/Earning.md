

# Earning

The employee earning model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agency** | **String** | Third-party agency associated with earning. Must match Company setup.&lt;br  /&gt;Max length: 10 |  [optional] |
|**amount** | **BigDecimal** | Value that matches CalculationCode to add to gross wages. For percentage (%), enter whole number (10 &#x3D; 10%).  &lt;br  /&gt;Decimal(12,2) |  [optional] |
|**annualMaximum** | **BigDecimal** | Year to Date dollar amount not to be exceeded for an earning in the calendar year. Used only with company driven maximums. &lt;br  /&gt;Decimal(12,2) |  [optional] |
|**calculationCode** | **String** | Defines how earnings are calculated. Common values are *% (percentage of gross), flat (flat dollar amount)*. Defaulted to the Company setup calcCode for earning. &lt;br  /&gt;Max length: 20 |  [optional] |
|**costCenter1** | **String** | Cost Center associated with earning. Must match Company setup.&lt;br  /&gt; Max length: 10 |  [optional] |
|**costCenter2** | **String** | Cost Center associated with earning. Must match Company setup.&lt;br  /&gt; Max length: 10 |  [optional] |
|**costCenter3** | **String** | Cost Center associated with earning. Must match Company setup.&lt;br  /&gt; Max length: 10 |  [optional] |
|**earningCode** | **String** | Earning code. Must match Company setup. &lt;br  /&gt;Max length: 10 |  |
|**effectiveDate** | **String** | Date earning is active. Defaulted to run date or check date based on Company setup. Common formats are MM-DD-CCYY, CCYY-MM-DD. |  [optional] |
|**endDate** | **String** | Stop date of an earning. Common formats are MM-DD-CCYY, CCYY-MM-DD. |  [optional] |
|**frequency** | **String** | Needed if earning is applied differently from the payroll frequency (one time earning for example).&lt;br  /&gt; Max length: 5 |  [optional] |
|**goal** | **BigDecimal** | Dollar amount. The employee earning will stop when the goal amount is reached.&lt;br  /&gt; Decimal(12,2) |  [optional] |
|**hoursOrUnits** | **BigDecimal** | The value is used in conjunction with the Rate field. When entering Group Term Life Insurance (GTL), it should contain the full amount of the group term life insurance policy. &lt;br  /&gt; Decimal(12,2) |  [optional] |
|**isSelfInsured** | **Boolean** | Used for ACA. If not entered, defaulted to Company earning setup. |  [optional] |
|**jobCode** | **String** | Job code associated with earnings. Must match Company setup.&lt;br  /&gt; Max length: 20 |  [optional] |
|**miscellaneousInfo** | **String** | Information to print on the check stub if agency is set up for this earning. &lt;br  /&gt;Max length: 50 |  [optional] |
|**paidTowardsGoal** | **BigDecimal** | Amount already paid to employee toward goal. &lt;br  /&gt; Decimal(12,2) |  [optional] |
|**payPeriodMaximum** | **BigDecimal** | Maximum amount of the earning on a single paycheck. &lt;br  /&gt; Decimal(12,2) |  [optional] |
|**payPeriodMinimum** | **BigDecimal** | Minimum amount of the earning on a single paycheck. &lt;br  /&gt; Decimal(12,2) |  [optional] |
|**rate** | **BigDecimal** | Rate is used in conjunction with the hoursOrUnits field. &lt;br  /&gt; Decimal(12,2) |  [optional] |
|**rateCode** | **String** | Rate Code applies to additional pay rates entered for an employee. Must match Company setup. &lt;br  /&gt; Max length: 10 |  [optional] |
|**startDate** | **String** | Start date of an earning based on payroll calendar. Common formats are MM-DD-CCYY, CCYY-MM-DD. |  |



