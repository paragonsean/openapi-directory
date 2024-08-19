# ThePlaidApi.CustomerInitiatedReturnRisk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**riskTier** | **Number** | A tier corresponding to the projected likelihood that the transaction, if initiated, will be subject to a return.  In the &#x60;customer_initiated_return_risk&#x60; object, there are five risk tiers corresponding to the scores:   1: Predicted customer-initiated return incidence rate between 0.00% - 0.02%   2: Predicted customer-initiated return incidence rate between 0.02% - 0.05%   3: Predicted customer-initiated return incidence rate between 0.05% - 0.1%   4: Predicted customer-initiated return incidence rate between 0.1% - 0.5%   5: Predicted customer-initiated return incidence rate greater than 0.5%  | 
**score** | **Number** | A score from 1-99 that indicates the transaction return risk: a higher risk score suggests a higher return likelihood. | 


