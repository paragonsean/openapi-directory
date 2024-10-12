# CloudSearchApi.PersonCore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressMeAs** | **String** | Instructions for how to address this person (e.g. custom pronouns). For google.com this is a set of pronouns from a defined list of options. | [optional] 
**adminTo** | [**[PersonCore]**](PersonCore.md) | People the profile owner is an admin to. Note that not all fields of these PersonCores will be set, in particular, relationships will be empty. | [optional] 
**admins** | [**[PersonCore]**](PersonCore.md) | The profile owner&#39;s admins in no particular order. Note that not all fields of these PersonCores will be set, in particular, relationships will be empty. | [optional] 
**availabilityStatus** | **String** |  | [optional] 
**birthday** | [**ModelDate**](ModelDate.md) |  | [optional] 
**calendarUrl** | [**SafeUrlProto**](SafeUrlProto.md) |  | [optional] 
**chatUrl** | [**SafeUrlProto**](SafeUrlProto.md) |  | [optional] 
**costCenter** | **String** | Person&#39;s cost center as a string, e.g. \&quot;926: Googler Apps\&quot;. | [optional] 
**department** | **String** | The person&#39;s Organization department, e.g. \&quot;People Operations\&quot;. For google.com this is usually called \&quot;area\&quot;. | [optional] 
**directReports** | [**[PersonCore]**](PersonCore.md) | A subset of the profile owner&#39;s direct reports. The number of entities here may be less than total_direct_reports_count, because typically ProfileResponse does not include all the person&#39;s reports, if there are too many to retrieve efficiently. Note that not all fields of these PersonCores will be set, in particular, relationships will be empty. | [optional] 
**dottedLineManagers** | [**[PersonCore]**](PersonCore.md) | The profile owner&#39;s direct dotted line managers in no particular order. Note that not all fields of these PersonCores will be set, in particular, relationships will be empty. | [optional] 
**dottedLineReports** | [**[PersonCore]**](PersonCore.md) | A subset of the profile owner&#39;s dotted-line reports. The number of entities here may be less than total_dlr_count. Note that not all fields of these PersonCores will be set, in particular, relationships will be empty. | [optional] 
**emails** | **[String]** | E-mail addresses of the person. The primary or preferred email should be first. | [optional] 
**employeeId** | **String** | Person&#39;s employee number (external ID of type \&quot;organization\&quot;) For google.com this is the badge number (e.g. 2 for Larry Page). | [optional] 
**fingerprint** | **String** | A fingerprint used by PAPI to reliably determine if a resource has changed Externally it is used as part of the etag. | [optional] 
**ftePermille** | **String** | Full-time equivalent (in ‰) (e.g. 800 for a person who&#39;s working 80%). | [optional] 
**geoLocation** | [**MapInfo**](MapInfo.md) |  | [optional] 
**gmailUrl** | **String** |  | [optional] 
**jobTitle** | **String** | Profile owner&#39;s job title (e.g. \&quot;Software Engineer\&quot;). For google.com this is the Workday preferred job title. | [optional] 
**keywordTypes** | **[String]** | List of keys to use from the map &#39;keywords&#39;. | [optional] 
**keywords** | **{String: String}** | Custom keywords the domain admin has added. | [optional] 
**links** | [**[EnterpriseTopazFrontendTeamsLink]**](EnterpriseTopazFrontendTeamsLink.md) | Custom links the profile owner has added. | [optional] 
**location** | **String** | Detailed desk location within the company. For google.com this is the desk location code (e.g. \&quot;DE-MUC-ARP-6T2-6T2C0C\&quot;) if the person has a desk. | [optional] 
**managers** | [**[PersonCore]**](PersonCore.md) | The profile owner&#39;s management chain from top to bottom, where managers[0] is the CEO, manager[N-2] is the person&#39;s manager&#39;s manager and managers[N-1] is the person&#39;s direct manager. Note that not all fields of these PersonCores will be set, in particular, relationships will be empty. | [optional] 
**mission** | **String** | Custom mission statement the profile owner has added. | [optional] 
**name** | **String** | Human-readable Unicode display name. | [optional] 
**officeLocation** | **String** | Office/building identifier within the company. For google.com this is the office code (e.g. \&quot;DE-MUC-ARP\&quot;). | [optional] 
**personId** | **String** | The person&#39;s obfuscated Gaia ID. | [optional] 
**phoneNumbers** | [**[EnterpriseTopazFrontendTeamsPersonCorePhoneNumber]**](EnterpriseTopazFrontendTeamsPersonCorePhoneNumber.md) |  | [optional] 
**photoUrl** | [**SafeUrlProto**](SafeUrlProto.md) |  | [optional] 
**postalAddress** | **String** | Postal address of office/building. | [optional] 
**totalDirectReportsCount** | **Number** | Total count of the profile owner&#39;s direct reports. | [optional] 
**totalDlrCount** | **Number** | Total count of the profile owner&#39;s dotted-line reports. | [optional] 
**totalFteCount** | **String** | The sum of all profile owner&#39;s reports and their own full-time-equivalents in ‰ (e.g. 1800 if one report is working 80% and profile owner 100%). | [optional] 
**username** | **String** | External ID of type \&quot;login_id\&quot; for the profile. For google.com this is the username/LDAP. | [optional] 
**waldoComeBackTime** | **String** |  | [optional] 



## Enum: AvailabilityStatusEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `OUT_OF_OFFICE` (value: `"OUT_OF_OFFICE"`)

* `OUTSIDE_WORKING_HOURS` (value: `"OUTSIDE_WORKING_HOURS"`)

* `AVAILABLE` (value: `"AVAILABLE"`)




