# GoogleApi.PlusAclentryResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | A descriptive name for this entry. Suitable for display. | [optional] 
**id** | **String** | The ID of the entry. For entries of type \&quot;person\&quot; or \&quot;circle\&quot;, this is the ID of the resource. For other types, this property is not set. | [optional] 
**type** | **String** | The type of entry describing to whom access is granted. Possible values are:   - \&quot;person\&quot; - Access to an individual.  - \&quot;circle\&quot; - Access to members of a circle.  - \&quot;myCircles\&quot; - Access to members of all the person&#39;s circles.  - \&quot;extendedCircles\&quot; - Access to members of all the person&#39;s circles, plus all of the people in their circles.  - \&quot;domain\&quot; - Access to members of the person&#39;s Google Apps domain.  - \&quot;public\&quot; - Access to anyone on the web. | [optional] 


