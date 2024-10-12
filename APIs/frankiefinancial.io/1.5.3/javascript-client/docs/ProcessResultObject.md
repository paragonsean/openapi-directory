# FrankieFinancialApi.ProcessResultObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkDate** | **Date** | The date and time the item was checked to provide this result. | [optional] 
**checkId** | **String** | Unique identifier for every check/comparison/verification. Make sure you reference this ID whenever updating check details. This ID will also be used when pushing check results back to you. | [optional] 
**checkPerformedBy** | **String** | Service provider that performed the check. Basically the name of the connector, without the leading con_  | [optional] 
**checkSource** | **String** | Code that can be used to determine the underlying nature or data source of the checks performed. This may or may not be known by the connector, or may be a provider specific type (e.g. type \&quot;O\&quot;)  Note, this will actually be normalised by the core service into a standfardised result so that we&#39;re not accidentally counting sources twice. Original source will then be copied into the KVPs  | [optional] 
**checkType** | **String** | Short indication of the type of check that was done.   When used as a summary, it will the the checkType that was requested  For granular results, it will be the individual check performed.  | [optional] 
**confidenceLevel** | **Number** | Confidence in the result on a scale of 0 (no match) to 100 (strong/identical match). Whole integers only.  Negative values are used to indicate untrusted results.  | [optional] 
**providerCheckID** | **String** | The service provider will give us a receipt, transaction id, check number, or some such that gives us a unique id on their side that we can reconcile with  | [optional] 
**resultNotes** | [**[KeyValuePairObject]**](KeyValuePairObject.md) | Any additional notes that may relate to the state. These are returned as typed KVPs | [optional] 
**resultState** | [**EnumCheckResultState**](EnumCheckResultState.md) |  | [optional] 
**riskLevel** | **Number** | Only supplied in a summary result. Used to indicate the ovall risk score for the entity at this point in time, based on configurable rules.  Some examples might include:    * Current level of ID checks passed   * Device ID scores   * Current PEP/Sanctions/etc checks   * Jurisdictional risk based on addresses, documents and other KVPs   * Fraud check results    In this case a higher score is a bad thing. General rule of thumb:    * 0 - 30 &#x3D; Low Risk   * 31 - 50 &#x3D; Medium Risk   * 50 - 75 &#x3D; High Risk   * 75+ &#x3D; Unacceptable  | [optional] 


