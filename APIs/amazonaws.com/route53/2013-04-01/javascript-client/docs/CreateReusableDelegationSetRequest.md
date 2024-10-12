# AmazonRoute53.CreateReusableDelegationSetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callerReference** | **String** | A unique string that identifies the request, and that allows you to retry failed &lt;code&gt;CreateReusableDelegationSet&lt;/code&gt; requests without the risk of executing the operation twice. You must use a unique &lt;code&gt;CallerReference&lt;/code&gt; string every time you submit a &lt;code&gt;CreateReusableDelegationSet&lt;/code&gt; request. &lt;code&gt;CallerReference&lt;/code&gt; can be any unique string, for example a date/time stamp. | 
**hostedZoneId** | **String** | If you want to mark the delegation set for an existing hosted zone as reusable, the ID for that hosted zone. | [optional] 


