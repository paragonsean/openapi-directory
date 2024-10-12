# HetrasBookingApiVersion0.LinkObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecation** | **String** | &lt;para&gt;The \&quot;deprecation\&quot; property is OPTIONAL.&lt;/para&gt;  &lt;para&gt; &lt;/para&gt;  &lt;para&gt;Its presence indicates that the link is to be deprecated (i.e.              removed) at a future date.  Its value is a URL that SHOULD provide              further information about the deprecation.              A client SHOULD provide some notification (for example, by logging a              warning message) whenever it traverses over a link that has this              property.  The notification SHOULD include the deprecation property&#39;s              value so that a client maintainer can easily find information about              the deprecation.&lt;/para&gt; | [optional] 
**href** | **String** | &lt;para&gt;The \&quot;href\&quot; property is REQUIRED.&lt;/para&gt;  &lt;para&gt; &lt;/para&gt;  &lt;para&gt;Its value is either a URI [RFC3986] or a URI Template [RFC6570].              If the value is a URI Template then the Link Object SHOULD have a              \&quot;templated\&quot; attribute whose value is true.&lt;/para&gt; | 
**hreflang** | **String** | &lt;para&gt;The \&quot;hreflang\&quot; property is OPTIONAL.&lt;/para&gt;  &lt;para&gt; &lt;/para&gt;  &lt;para&gt;Its value is a string and is intended for indicating the language of              the target resource (as defined by [RFC5988]).&lt;/para&gt; | [optional] 
**name** | **String** | &lt;para&gt;The \&quot;name\&quot; property is OPTIONAL.&lt;/para&gt;  &lt;para&gt; &lt;/para&gt;  &lt;para&gt;Its value MAY be used as a secondary key for selecting Link Objects              which share the same relation type.&lt;/para&gt; | [optional] 
**profile** | **String** | &lt;para&gt;The \&quot;profile\&quot; property is OPTIONAL.&lt;/para&gt;  &lt;para&gt; &lt;/para&gt;  &lt;para&gt;Its value is a string which is a URI that hints about the profile.&lt;/para&gt; | [optional] 
**templated** | **Boolean** | &lt;para&gt;The \&quot;templated\&quot; property is OPTIONAL.&lt;/para&gt;  &lt;para&gt; &lt;/para&gt;  &lt;para&gt;Its value is boolean and SHOULD be true when the Link Object&#39;s \&quot;href\&quot;              property is a URI Template.              Its value SHOULD be considered false if it is undefined or any other              value than true.&lt;/para&gt; | [optional] 
**title** | **String** | &lt;para&gt;The \&quot;title\&quot; property is OPTIONAL.&lt;/para&gt;  &lt;para&gt; &lt;/para&gt;  &lt;para&gt;Its value is a string and is intended for labelling the link with a              human-readable identifier (as defined by [RFC5988]).&lt;/para&gt; | [optional] 
**type** | **String** | &lt;para&gt;The \&quot;type\&quot; property is OPTIONAL.&lt;/para&gt;  &lt;para&gt; &lt;/para&gt;  &lt;para&gt;Its value is a string used as a hint to indicate the media type              expected when dereferencing the target resource.&lt;/para&gt; | [optional] 


