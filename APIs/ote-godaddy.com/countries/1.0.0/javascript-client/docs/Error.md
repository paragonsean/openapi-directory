# OpenapiJsClient.Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | Short identifier for the error, suitable for indicating the specific error within client code | 
**fields** | [**[ErrorField]**](ErrorField.md) | List of the specific fields, and the errors found with their contents | [optional] 
**message** | **String** | Human-readable, English description of the error | [optional] 
**stack** | **[String]** | Stack trace indicating where the error occurred.&lt;br/&gt; NOTE: This attribute &lt;strong&gt;MAY&lt;/strong&gt; be included for Development and Test environments. However, it &lt;strong&gt;MUST NOT&lt;/strong&gt; be exposed from OTE nor Production systems | [optional] 


