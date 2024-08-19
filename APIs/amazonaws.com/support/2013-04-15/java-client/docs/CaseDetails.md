

# CaseDetails

<p>A JSON-formatted object that contains the metadata for a support case. It is contained in the response from a <a>DescribeCases</a> request. <b>CaseDetails</b> contains the following fields:</p> <ul> <li> <p> <b>caseId</b> - The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-<i>12345678910-2013-c4c1d2bf33c5cf47</i>.</p> </li> <li> <p> <b>categoryCode</b> - The category of problem for the support case. Corresponds to the <code>CategoryCode</code> values returned by a call to <a>DescribeServices</a>.</p> </li> <li> <p> <b>displayId</b> - The identifier for the case on pages in the Amazon Web Services Support Center.</p> </li> <li> <p> <b>language</b> - The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English (\"en\"), Japanese (\"ja\") and Korean (“ko”). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p> </li> <li> <p> <b>nextToken</b> - A resumption point for pagination.</p> </li> <li> <p> <b>recentCommunications</b> - One or more <a>Communication</a> objects. Fields of these objects are <code>attachments</code>, <code>body</code>, <code>caseId</code>, <code>submittedBy</code>, and <code>timeCreated</code>.</p> </li> <li> <p> <b>serviceCode</b> - The identifier for the Amazon Web Services service that corresponds to the service code defined in the call to <a>DescribeServices</a>.</p> </li> <li> <p> <b>severityCode</b> - The severity code assigned to the case. Contains one of the values returned by the call to <a>DescribeSeverityLevels</a>. The possible values are: <code>low</code>, <code>normal</code>, <code>high</code>, <code>urgent</code>, and <code>critical</code>.</p> </li> <li> <p> <b>status</b> - The status of the case in the Amazon Web Services Support Center. Valid values:</p> <ul> <li> <p> <code>opened</code> </p> </li> <li> <p> <code>pending-customer-action</code> </p> </li> <li> <p> <code>reopened</code> </p> </li> <li> <p> <code>resolved</code> </p> </li> <li> <p> <code>unassigned</code> </p> </li> <li> <p> <code>work-in-progress</code> </p> </li> </ul> </li> <li> <p> <b>subject</b> - The subject line of the case.</p> </li> <li> <p> <b>submittedBy</b> - The email address of the account that submitted the case.</p> </li> <li> <p> <b>timeCreated</b> - The time the case was created, in ISO-8601 format.</p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caseId** | [**String**](String.md) |  |  [optional] |
|**displayId** | [**String**](String.md) |  |  [optional] |
|**subject** | [**String**](String.md) |  |  [optional] |
|**status** | [**String**](String.md) |  |  [optional] |
|**serviceCode** | [**String**](String.md) |  |  [optional] |
|**categoryCode** | [**String**](String.md) |  |  [optional] |
|**severityCode** | [**String**](String.md) |  |  [optional] |
|**submittedBy** | [**String**](String.md) |  |  [optional] |
|**timeCreated** | [**String**](String.md) |  |  [optional] |
|**recentCommunications** | [**CaseDetailsRecentCommunications**](CaseDetailsRecentCommunications.md) |  |  [optional] |
|**ccEmailAddresses** | [**List**](List.md) |  |  [optional] |
|**language** | [**String**](String.md) |  |  [optional] |



