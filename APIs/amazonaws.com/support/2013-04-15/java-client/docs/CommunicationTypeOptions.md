

# CommunicationTypeOptions

<p>A JSON-formatted object that contains the CommunicationTypeOptions for creating a case for a certain communication channel. It is contained in the response from a <a>DescribeCreateCaseOptions</a> request. <b>CommunicationTypeOptions</b> contains the following fields:</p> <ul> <li> <p> <b>datesWithoutSupport</b> - A JSON-formatted list containing date and time ranges for periods without support in UTC time. Date and time format is RFC 3339 : 'yyyy-MM-dd'T'HH:mm:ss.SSSZZ'. </p> </li> <li> <p> <b>supportedHours</b> - A JSON-formatted list containing time ranges when support are available. Time format is RFC 3339 : 'HH:mm:ss.SSS'. </p> </li> <li> <p> <b>type</b> - A string value indicating the communication type that the aforementioned rules apply to. At the moment the type value can assume one of 3 values at the moment <code>chat</code>, <code>web</code> and <code>call</code>. </p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**String**](String.md) |  |  [optional] |
|**supportedHours** | [**List**](List.md) |  |  [optional] |
|**datesWithoutSupport** | [**List**](List.md) |  |  [optional] |



