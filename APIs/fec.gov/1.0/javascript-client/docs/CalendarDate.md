# OpenFec.CalendarDate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allDay** | **Boolean** |  | [optional] 
**calendarCategoryId** | **Number** |  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  | [optional] 
**category** | **String** |  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  | [optional] 
**description** | **String** |  | [optional] 
**endDate** | **String** |  | [optional] 
**eventId** | **Number** | An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. | [optional] 
**location** | **String** |  Can be state address or room.  | [optional] 
**startDate** | **String** |  | [optional] 
**state** | **[String]** | The state field only applies to election dates and reporting deadlines, reporting periods and all other dates do not have the array of states to filter on | [optional] 
**summary** | **String** |  | [optional] 
**url** | **String** |  A url for that event  | [optional] 


