# SalesLoftPlatform.User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privateFields** | **Object** | For internal use only. This field does not comply with our backwards compatability policies. | [optional] 
**active** | **Boolean** | Whether an user is currently active in SalesLoft | [optional] 
**bccEmailAddress** | **String** | Address that will be BBC&#39;d on all emails from this user | [optional] 
**clickToCallEnabled** | **Boolean** | Whether this user has click to call enabled | [optional] 
**createdAt** | **Date** | Datetime of when the user was created | [optional] 
**crmConnected** | **Boolean** | Whether the user has a crm connected | [optional] 
**email** | **String** | Email address provided to accounts.salesloft.com | [optional] 
**emailClientConfigured** | **Boolean** | Whether this user has a email client configured | [optional] 
**emailClientEmailAddress** | **String** | Email address associated with the email client of the user | [optional] 
**emailSignature** | **String** | Email signature | [optional] 
**emailSignatureClickTrackingDisabled** | **Boolean** | Whether this user has click tracking disabled in email signature | [optional] 
**emailSignatureType** | **String** | Email signature type | [optional] 
**externalFeatureFlags** | **Object** | Feature flags that are for this user. New flags may appear or disappear at any time | [optional] 
**firstName** | **String** | First name of user | [optional] 
**fromAddress** | **String** | The from address of this user | [optional] 
**fullEmailAddress** | **String** | RFC 5322 compliant email address | [optional] 
**group** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**guid** | **String** | Globally unique user ID. New endpoints will explicitly accept this over id | [optional] 
**id** | **Number** | User ID | [optional] 
**jobRole** | **String** | Job role of user | [optional] 
**lastName** | **String** | Last name of user | [optional] 
**localDialEnabled** | **Boolean** | Whether this user has Local Dial enabled | [optional] 
**name** | **String** | Display name of user | [optional] 
**phoneClient** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**phoneNumberAssignment** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**role** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**sendingEmailAddress** | **String** | The email address that email of the user will be sent from, resolved in the following resolution order: from_user, email_client_email_address, email | [optional] 
**slackUsername** | **String** | Slack username | [optional] 
**team** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**teamAdmin** | **Boolean** | Team Admin | [optional] 
**timeZone** | **String** | User Time Zone | [optional] 
**twitterHandle** | **String** | Twitter handle | [optional] 
**updatedAt** | **Date** | Datetime of when the user was last updated | [optional] 
**workCountry** | **String** | Work Country | [optional] 


