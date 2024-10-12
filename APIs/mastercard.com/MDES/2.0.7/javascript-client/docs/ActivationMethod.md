# MdesCustomerService.ActivationMethod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activationMethodId** | **String** | Unique identifier of the activation method. | [optional] 
**activationMethodType** | **String** | Type of activation method. Valid values:&lt;br /&gt;    \&quot;SMS\&quot; ? Activation code sent in text message to masked mobile phone number&lt;br /&gt;    \&quot;EMA\&quot; ? Activation code sent in email to masked email address&lt;br /&gt;    \&quot;ACC\&quot; ? Cardholder to call automated call center phone number&lt;br /&gt;    \&quot;CLC\&quot; ? Cardholder to call Call Center phone number&lt;br /&gt;    \&quot;WEB\&quot; ? Website&lt;br /&gt;    \&quot;BAP\&quot; ? Mobile application&lt;br /&gt;    \&quot;OBC\&quot; ? Activation code spoken via call to cardholder on masked voice call phone number. | [optional] 
**activationMethodValue** | **String** | Activation method details value. | [optional] 
**resendIndicator** | **String** | Whether the activation method can be used to re-send an activation code. Valid values are TRUE and FALSE. | [optional] 


