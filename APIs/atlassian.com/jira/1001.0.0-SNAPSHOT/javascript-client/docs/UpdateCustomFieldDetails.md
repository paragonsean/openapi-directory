# TheJiraCloudPlatformRestApi.UpdateCustomFieldDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description of the custom field. The maximum length is 40000 characters. | [optional] 
**name** | **String** | The name of the custom field. It doesn&#39;t have to be unique. The maximum length is 255 characters. | [optional] 
**searcherKey** | **String** | The searcher that defines the way the field is searched in Jira. It can be set to &#x60;null&#x60;, otherwise you must specify the valid searcher for the field type, as listed below (abbreviated values shown):   *  &#x60;cascadingselect&#x60;: &#x60;cascadingselectsearcher&#x60;  *  &#x60;datepicker&#x60;: &#x60;daterange&#x60;  *  &#x60;datetime&#x60;: &#x60;datetimerange&#x60;  *  &#x60;float&#x60;: &#x60;exactnumber&#x60; or &#x60;numberrange&#x60;  *  &#x60;grouppicker&#x60;: &#x60;grouppickersearcher&#x60;  *  &#x60;importid&#x60;: &#x60;exactnumber&#x60; or &#x60;numberrange&#x60;  *  &#x60;labels&#x60;: &#x60;labelsearcher&#x60;  *  &#x60;multicheckboxes&#x60;: &#x60;multiselectsearcher&#x60;  *  &#x60;multigrouppicker&#x60;: &#x60;multiselectsearcher&#x60;  *  &#x60;multiselect&#x60;: &#x60;multiselectsearcher&#x60;  *  &#x60;multiuserpicker&#x60;: &#x60;userpickergroupsearcher&#x60;  *  &#x60;multiversion&#x60;: &#x60;versionsearcher&#x60;  *  &#x60;project&#x60;: &#x60;projectsearcher&#x60;  *  &#x60;radiobuttons&#x60;: &#x60;multiselectsearcher&#x60;  *  &#x60;readonlyfield&#x60;: &#x60;textsearcher&#x60;  *  &#x60;select&#x60;: &#x60;multiselectsearcher&#x60;  *  &#x60;textarea&#x60;: &#x60;textsearcher&#x60;  *  &#x60;textfield&#x60;: &#x60;textsearcher&#x60;  *  &#x60;url&#x60;: &#x60;exacttextsearcher&#x60;  *  &#x60;userpicker&#x60;: &#x60;userpickergroupsearcher&#x60;  *  &#x60;version&#x60;: &#x60;versionsearcher&#x60; | [optional] 



## Enum: SearcherKeyEnum


* `cascadingselectsearcher` (value: `"com.atlassian.jira.plugin.system.customfieldtypes:cascadingselectsearcher"`)

* `daterange` (value: `"com.atlassian.jira.plugin.system.customfieldtypes:daterange"`)

* `datetimerange` (value: `"com.atlassian.jira.plugin.system.customfieldtypes:datetimerange"`)

* `exactnumber` (value: `"com.atlassian.jira.plugin.system.customfieldtypes:exactnumber"`)

* `exacttextsearcher` (value: `"com.atlassian.jira.plugin.system.customfieldtypes:exacttextsearcher"`)

* `grouppickersearcher` (value: `"com.atlassian.jira.plugin.system.customfieldtypes:grouppickersearcher"`)

* `labelsearcher` (value: `"com.atlassian.jira.plugin.system.customfieldtypes:labelsearcher"`)

* `multiselectsearcher` (value: `"com.atlassian.jira.plugin.system.customfieldtypes:multiselectsearcher"`)

* `numberrange` (value: `"com.atlassian.jira.plugin.system.customfieldtypes:numberrange"`)

* `projectsearcher` (value: `"com.atlassian.jira.plugin.system.customfieldtypes:projectsearcher"`)

* `textsearcher` (value: `"com.atlassian.jira.plugin.system.customfieldtypes:textsearcher"`)

* `userpickergroupsearcher` (value: `"com.atlassian.jira.plugin.system.customfieldtypes:userpickergroupsearcher"`)

* `versionsearcher` (value: `"com.atlassian.jira.plugin.system.customfieldtypes:versionsearcher"`)




