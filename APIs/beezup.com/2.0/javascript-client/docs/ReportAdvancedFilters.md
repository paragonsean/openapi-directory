# BeezUpMerchantApi.ReportAdvancedFilters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**globalMarginPercent** | **Number** | If the margin type is &#39;Global&#39;, indicate the percentage of sale price. | [optional] 
**linkClickToOrderMaxDay** | **Number** | If the linkOrderType is OnClickDate, indicate the max day to search the click from the order | [optional] 
**linkClickToOrderType** | [**LinkClickToOrderType**](LinkClickToOrderType.md) |  | 
**marginType** | [**MarginType**](MarginType.md) |  | 
**onlyDirectSales** | **Boolean** | If true, you will get only direct sales. Otherwise the indirect sales will be included. | [default to false]
**onlyPaymentValidatedOrders** | **Boolean** | If true, you will get the only the orders with payment validated. Otherwise, you will get all orders validated or not. | [default to false]
**performanceIndicatorFormula** | [**PerformanceIndicatorFormula**](PerformanceIndicatorFormula.md) |  | 


