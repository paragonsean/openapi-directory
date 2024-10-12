

# AdditionalDataTemporaryServices


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enhancedSchemeDataCustomerReference** | **String** | The customer code, if supplied by a customer. * Encoding: ASCII * maxLength: 25 |  [optional] |
|**enhancedSchemeDataEmployeeName** | **String** | The name or ID of the person working in a temporary capacity. * maxLength: 40.   * Must not be all spaces.  *Must not be all zeros. |  [optional] |
|**enhancedSchemeDataJobDescription** | **String** | The job description of the person working in a temporary capacity. * maxLength: 40  * Must not be all spaces.  *Must not be all zeros. |  [optional] |
|**enhancedSchemeDataRegularHoursRate** | **String** | The amount paid for regular hours worked, [minor units](https://docs.adyen.com/development-resources/currency-codes). * maxLength: 7 * Must not be empty * Can be all zeros |  [optional] |
|**enhancedSchemeDataRegularHoursWorked** | **String** | The hours worked. * maxLength: 7 * Must not be empty * Can be all zeros |  [optional] |
|**enhancedSchemeDataRequestName** | **String** | The name of the person requesting temporary services. * maxLength: 40 * Must not be all zeros * Must not be all spaces |  [optional] |
|**enhancedSchemeDataTempStartDate** | **String** | The billing period start date. * Format: ddMMyy * maxLength: 6 |  [optional] |
|**enhancedSchemeDataTempWeekEnding** | **String** | The billing period end date. * Format: ddMMyy * maxLength: 6 |  [optional] |
|**enhancedSchemeDataTotalTaxAmount** | **String** | The total tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes). For example, 2000 means USD 20.00 * maxLength: 12 |  [optional] |



