# MotaWordApi.ContinuousProject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyticsEnabled** | **Boolean** | Should we collect analytics data from Active for this continuous project? | [optional] 
**autoStartPostedit** | **Boolean** | Immediately start post-editing project for translation requests that are applied MT. | [optional] 
**createdAt** | **Date** | the date-time notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z | [optional] 
**id** | **Number** |  | [optional] 
**isEnabled** | **Boolean** |  | [optional] 
**lastActivityAt** | **Date** | the date-time notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z | [optional] 
**links** | [**ContinuousProjectLinks**](ContinuousProjectLinks.md) |  | [optional] 
**mtEnabled** | **Boolean** | Immediately apply MT on translation requests if they are missing from TM. | [optional] 
**mtEngine** | **String** | One of \&quot;MOTAWORD\&quot;, \&quot;GOOGLE\&quot;, \&quot;AMAZON\&quot;, \&quot;MS\&quot;. Default is \&quot;MOTAWORD\&quot;. | [optional] 
**name** | **String** |  | [optional] 
**posteditEnabled** | **Boolean** | Get an instant quote for translation requests that are applied MT. | [optional] 
**sourceLanguage** | **String** |  | [optional] 
**status** | **String** | One of \&quot;a &#x3D;&gt; ACTIVE\&quot;, \&quot;i &#x3D;&gt; INACTIVE\&quot;, \&quot;d &#x3D;&gt; DELETED\&quot;, \&quot;c &#x3D;&gt; SCHEDULED CANCELLATION\&quot;, \&quot;p &#x3D;&gt; SCHEDULED CHANGE\&quot; | [optional] 
**subscription** | [**Subscription**](Subscription.md) |  | [optional] 
**targetLanguages** | **[String]** |  | [optional] 
**type** | **String** | Continuous project type. We currently have only 2 types, NULL and \&quot;active\&quot;. | [optional] 
**wordCount** | **Number** |  | [optional] 


