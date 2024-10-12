# SalesLoftPlatform.Team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privateFields** | **Object** | For internal use only. This field does not comply with our backwards compatability policies. | [optional] 
**allowAutomatedEmailSteps** | **Boolean** | Whether team members are allowed to have automated email steps | [optional] 
**callRecordingDisabled** | **Boolean** | Whether all call recording is disabled | [optional] 
**clickTrackingDefault** | **Boolean** | The team default for click tracking when composing emails | [optional] 
**createdAt** | **Date** | Datetime of when the team was created | [optional] 
**customTrackingDomain** | **String** | The domain click and open tracking will be proxied through | [optional] 
**deactivated** | **Boolean** | Indicates if the team has been deactivated | [optional] 
**dispositionsRequired** | **Boolean** | Whether team members are required to mark disposition at the end of calls | [optional] 
**emailDailyLimit** | **Number** | Daily email limit for each member on the team | [optional] 
**groupPrivacySetting** | **String** | Visibility setting for resources across the team. Possible values are: group_public, all_public. When the value is group_public, certain resources will only be visible to members of the same group. When the value is all_public, all resources are visible to all users on this team.  | [optional] 
**id** | **Number** | Team ID | [optional] 
**licenseLimit** | **Number** | Count of seats that this team has licensed | [optional] 
**localDialEnabled** | **Boolean** | Whether this team has local dial enabled | [optional] 
**name** | **String** | Team name | [optional] 
**plan** | **String** | Plan type of the team, Possible values are: group, professional, enterprise | [optional] 
**planFeatures** | **Object** | Add on features for this team | [optional] 
**recordByDefault** | **Boolean** | Whether calls will record by default | [optional] 
**sentimentsRequired** | **Boolean** | Whether team members are required to log sentiments | [optional] 
**teamVisibilityDefault** | **String** | The default visibility of resources on the team, in the UI only. The API does not utilize this default. Possible values are: public, private.  | [optional] 
**updatedAt** | **Date** | Datetime of when the team was last updated | [optional] 


