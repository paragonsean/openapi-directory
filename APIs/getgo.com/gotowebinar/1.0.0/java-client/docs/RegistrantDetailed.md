

# RegistrantDetailed

Detailed description of a webinar registrant with all registration fields.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | The registrant&#39;s address |  [optional] |
|**city** | **String** | The registrant&#39;s city |  [optional] |
|**country** | **String** | The registrant&#39;s country |  [optional] |
|**email** | **String** | The registrant&#39;s email address |  |
|**employeeCount** | **String** | The size in employees of the registrant&#39;s organization |  [optional] |
|**firstName** | **String** | The registrant&#39;s first name |  |
|**implementationTimeFrame** | **String** | The time frame within which the product will be purchased |  [optional] |
|**industry** | **String** | The type of industry the registrant&#39;s organization belongs to |  [optional] |
|**jobTitle** | **String** | The registrant&#39;s job title |  [optional] |
|**joinUrl** | **String** | The URL the registrant will use to join the webinar |  |
|**lastName** | **String** | The registrant&#39;s last name |  |
|**numberOfEmployees** | **String** | The size in employees of the registrant&#39;s organization |  [optional] |
|**organization** | **String** | The registrant&#39;s organization |  [optional] |
|**phone** | **String** | The registrant&#39;s phone |  [optional] |
|**purchasingRole** | **String** | The registrant&#39;s role in purchasing the product |  [optional] |
|**purchasingTimeFrame** | **String** | The time frame within which the product will be purchased |  [optional] |
|**questionsAndComments** | **String** | Any questions or comments the registrant made at the time of registration |  [optional] |
|**registrantKey** | **Long** | The registrant&#39;s key |  |
|**registrationDate** | **OffsetDateTime** | The registration date and time |  |
|**responses** | [**List&lt;CustomAnswers&gt;**](CustomAnswers.md) | Responses to custom questions |  [optional] |
|**source** | **String** | The source that led to the registration. This can be any string like &#39;Newsletter 123&#39; or &#39;Marketing campaign ABC&#39; |  [optional] |
|**state** | **String** | The registrant&#39;s state (US only) |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The registration status |  |
|**timeZone** | **String** | The time zone where the webinar will take place |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type is REGULAR for &#39;One session&#39; and &#39;Sequence&#39; webinars. For webinar series this parameter is not passed |  [optional] |
|**unsubscribed** | **Boolean** | Indicates whether the registrant opted-out from receiving other emails from this webinar&#39;s organizer |  [optional] |
|**zipCode** | **String** | The registrant&#39;s zip (post) code |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| APPROVED | &quot;APPROVED&quot; |
| DENIED | &quot;DENIED&quot; |
| WAITING | &quot;WAITING&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| REGULAR | &quot;REGULAR&quot; |



