# SmartMe.VirtualMeterCalculateFormulaApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualMeterCalculateFormulaGet**](VirtualMeterCalculateFormulaApi.md#virtualMeterCalculateFormulaGet) | **GET** /api/VirtualMeterCalculateFormula | Calculates a virtual meter from a formula.               A meter is coded as ID(\&quot;METERID\&quot;)



## virtualMeterCalculateFormulaGet

> Device virtualMeterCalculateFormulaGet(formula)

Calculates a virtual meter from a formula.               A meter is coded as ID(\&quot;METERID\&quot;)

Calculates a virtual meter from a formula.                            A meter is coded as ID(\&quot;METERID\&quot;)              Ariphmetical operators:               ()  parentheses;                 +   plus (a + b);                -  minus (a - b);                *  multiplycation symbol (a * b);                /  divide symbol (a / b);               Example: (ID(\&quot;63ac09cb-4e5f-4f3e-bd27-ad8c30bdfc0c\&quot;) + ID(\&quot;0209555e-9dc4-4e84-a166-a864488b4b12\&quot;)) * 2

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.VirtualMeterCalculateFormulaApi();
let formula = "formula_example"; // String | 
apiInstance.virtualMeterCalculateFormulaGet(formula, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **formula** | **String**|  | 

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

