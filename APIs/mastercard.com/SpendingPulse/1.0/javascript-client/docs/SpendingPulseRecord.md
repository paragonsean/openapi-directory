# SpendingPulse.SpendingPulseRecord

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **String** | Country Code. | [optional] 
**currencyOfForSalesValue** | **String** | A value to indicate the currency in which the sales value is being reported. For sales index values, this field is not used. | [optional] 
**ecomm** | **String** | Ecommerce indicator. \&quot;yes\&quot; or \&quot;no\&quot; are the options. | [optional] 
**impliedDeflatorMonthOverMonthChange** | **String** | Percent change from one month ago in the implied deflator (the deflator is used in seasonal adjustment calculation). | [optional] 
**impliedDeflatorYearOverYearChange** | **String** | Percent change from one year ago in the implied deflator (the deflator is used in seasonal adjustment calculation). | [optional] 
**nonGregorianReportingPeriod** | **String** | For only those data reported by a non-Gregorian calendar (e.g. US Sectors which are reported based on the National Retail Federation 4-5-4 calendar) this value designates the retail period being reported. As an example, for the US apparel sector, for Period Date &#x3D; February 2015, the reporting period is 2015-01 (February is the first month of US retail year 2015). | [optional] 
**period** | **String** | Indicates the period covered by the data with possible values of - day, week, month, quarter, annual | [optional] 
**periodEndDate** | **String** | Date indicating the end of the period covered by ensuing data. | [optional] 
**periodStartDate** | **String** | Date indicating the beginning of the period covered by ensuing data. | [optional] 
**priceAdjustmentFlag** | **String** | Price adjustment indicator. | [optional] 
**priceIndex3MonthMovingAverageChange** | **String** | Percent change from one year ago in the three-month moving PriceIndexValue average. | [optional] 
**priceIndexMonthOverMonthChange** | **String** | Percent change from one month ago in the PriceIndexValue. | [optional] 
**priceIndexValue** | **String** | Published price index value for the period being reported. Not a currency value - a decimal index value. The price index takes into account both the average ticket value and the size of the basket. Changes in either will be reflected in the price index changes. | [optional] 
**priceIndexYearOverYearChange** | **String** | Percent change from one year ago in the PriceIndexValue. | [optional] 
**productLine** | **String** | Product line, either for this resource it will be ?US Executive\&quot;. | [optional] 
**publicationCoveragePeriod** | **String** | Publication Coverage Period indicates what period is to be covered, often the current report will include the month prior. | [optional] 
**reportType** | **String** | Report type name, today the only report supported is \&quot;monitor\&quot;. | [optional] 
**reportingCalender** | **String** | Value indicates calendar used for periodic aggregation (e.g. \&quot;G\&quot; &#x3D; Gregorian, \&quot;454\&quot; &#x3D; US Retail, \&quot;445\&quot; &#x3D; UK ONS, etc.) Please note that some data are reported under more than one calendar. As a result, in order to uniquely identify the data being reported, the reporting calendar must be included. | [optional] 
**sales3MonthMovingAverageChange** | **String** | Percent change from one year ago in the three-month moving SalesIndexValue average. | [optional] 
**salesMonthOverMonthChange** | **String** | Percent change from one month ago in the SalesValueIndex. | [optional] 
**salesValueIndex** | **String** | Aggregated/computed value of sales for the period being reported. This may be an index value (not a currency value - just a decimal value) or it may be a currency value that would typically be in local currency (dollar, pound, yen, etc.) | [optional] 
**salesYearOverYearChange** | **String** | Percent change from one year ago in the SalesValueIndex. | [optional] 
**salesYearToDateChange** | **String** | Percent change from year ago. | [optional] 
**sameStoreSalesIndex3MonthMovingAverageChange** | **String** | Percent change from one month ago in the SameStoreSalesIndex. | [optional] 
**sameStoreSalesIndexYearOverYearChange** | **String** | Percent change from one year ago in the SameStoreSalesIndex. | [optional] 
**seasonalAdjustmentFlag** | **String** | Seasonal data adjustment indicator. | [optional] 
**sector** | **String** | Sector name/id. | [optional] 
**segment** | **String** | Sub unit within a sector e.g. Sector &#x3D; restaurant; SubSector &#x3D; Full Service; Segment &#x3D; Fine Dining. | [optional] 
**subGeographyValue** | **String** | For those data reported by sub-geographies (e.g. regions, states, etc.) the sub-geography being reported. | [optional] 
**subSector** | **String** | Sub unit within a sector e.g. Sector &#x3D; Electronics &amp; Appliances; SubSector &#x3D; Electronics. | [optional] 
**transactionIndex3MonthMovingAverageChange** | **String** | Percent change from one year ago in the three-month moving TransactionIndexValue average. | [optional] 
**transactionIndexMonthOverMonthChange** | **String** | Percent change from one month ago in the TransactionIndexValue. | [optional] 
**transactionIndexValue** | **String** | Published transaction index value for the period being reported. Not a currency value - a decimal index value. The transaction index is a relative indication of transactions volume in the sector/sub-sector/segment being reported. | [optional] 
**transactionIndexYearOverYearChange** | **String** | Percent change from one year ago in the TransactionIndexValue. | [optional] 


