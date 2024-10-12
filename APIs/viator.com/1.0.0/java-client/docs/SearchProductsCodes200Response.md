

# SearchProductsCodes200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateStamp** | **String** | **timestamp** of *this* response |  [optional] |
|**errorCodes** | **List&lt;String&gt;** | **array** of error codes pertaining to *this* error - See: [Viator API error codes](#section/Appendices/Viator-API-error-codes) for a list of possible error codes  |  [optional] |
|**errorMessage** | **List&lt;Object&gt;** | **array** of error message strings |  [optional] |
|**errorMessageText** | **String** | **array** of error message strings in plain text |  [optional] |
|**errorName** | **String** | **name** of *this* type of error |  [optional] |
|**errorReference** | **String** | **reference number** of *this* error |  [optional] |
|**errorType** | **String** | **code** specifying the type of error |  [optional] |
|**extraInfo** | **Object** | ignore (Viator only) |  [optional] |
|**extraObject** | **Object** | ignore (Viator only) |  [optional] |
|**success** | **Boolean** | **boolean indicator** of *this* request&#39;s outcome - &#x60;true&#x60;: the request was successful with no errors - &#x60;false&#x60;: an error was encountered  |  [optional] |
|**totalCount** | **Integer** | **number** of results available for *this* service  |  [optional] |
|**vmid** | **String** | **unique numeric id** of the server that processed *this* request |  [optional] |
|**data** | [**List&lt;SearchProductsCodes200ResponseAllOfDataInner&gt;**](SearchProductsCodes200ResponseAllOfDataInner.md) | **array** of product objects |  [optional] |



