# AmazonConnectService.ListPhoneNumbersV2Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targetArn** | **String** | The Amazon Resource Name (ARN) for Amazon Connect instances or traffic distribution groups that phone numbers are claimed to. If &lt;code&gt;TargetArn&lt;/code&gt; input is not provided, this API lists numbers claimed to all the Amazon Connect instances belonging to your account in the same Amazon Web Services Region as the request. | [optional] 
**maxResults** | **Number** | The maximum number of results to return per page. | [optional] 
**nextToken** | **String** | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
**phoneNumberCountryCodes** | [**[PhoneNumberCountryCode]**](PhoneNumberCountryCode.md) | The ISO country code. | [optional] 
**phoneNumberTypes** | [**[PhoneNumberType]**](PhoneNumberType.md) | The type of phone number. | [optional] 
**phoneNumberPrefix** | **String** | The prefix of the phone number. If provided, it must contain &lt;code&gt;+&lt;/code&gt; as part of the country code. | [optional] 


