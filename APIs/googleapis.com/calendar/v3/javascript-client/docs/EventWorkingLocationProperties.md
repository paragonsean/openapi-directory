# CalendarApi.EventWorkingLocationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customLocation** | [**EventWorkingLocationPropertiesCustomLocation**](EventWorkingLocationPropertiesCustomLocation.md) |  | [optional] 
**homeOffice** | **Object** | If present, specifies that the user is working at home. | [optional] 
**officeLocation** | [**EventWorkingLocationPropertiesOfficeLocation**](EventWorkingLocationPropertiesOfficeLocation.md) |  | [optional] 
**type** | **String** | Type of the working location. Possible values are:   - \&quot;homeOffice\&quot; - The user is working at home.  - \&quot;officeLocation\&quot; - The user is working from an office.  - \&quot;customLocation\&quot; - The user is working from a custom location.  Any details are specified in a sub-field of the specified name, but this field may be missing if empty. Any other fields are ignored. Required when adding working location properties. | [optional] 


