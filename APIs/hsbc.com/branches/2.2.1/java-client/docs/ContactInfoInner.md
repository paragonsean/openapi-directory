

# ContactInfoInner

Communication device number or electronic address used for communication.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contactContent** | **String** | Collection of information that identifies a phone/Fax number/ email, as defined by telecom services. |  |
|**contactDescription** | **String** | Description of contact such as main phone number, alternate phone number, Fax number, alternate fax number, email and alternate email |  [optional] |
|**contactType** | [**ContactTypeEnum**](#ContactTypeEnum) | Contact type such Phone, Fax and email |  |
|**otherContactType** | **Object** | Other contact type which is not in the standard code list |  [optional] |



## Enum: ContactTypeEnum

| Name | Value |
|---- | -----|
| ALTERNATE_EMAIL | &quot;AlternateEmail&quot; |
| ALTERNATE_FAX | &quot;AlternateFax&quot; |
| ALTERNATE_PHONE | &quot;AlternatePhone&quot; |
| EMAIL | &quot;Email&quot; |
| FAX | &quot;Fax&quot; |
| OTHER | &quot;Other&quot; |
| PHONE | &quot;Phone&quot; |



