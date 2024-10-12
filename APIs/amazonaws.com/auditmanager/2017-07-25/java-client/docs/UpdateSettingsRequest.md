

# UpdateSettingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**snsTopic** | **String** |  The Amazon Simple Notification Service (Amazon SNS) topic that Audit Manager sends notifications to.  |  [optional] |
|**defaultAssessmentReportsDestination** | [**CreateAssessmentRequestAssessmentReportsDestination**](CreateAssessmentRequestAssessmentReportsDestination.md) |  |  [optional] |
|**defaultProcessOwners** | [**List&lt;Role&gt;**](Role.md) |  A list of the default audit owners.  |  [optional] |
|**kmsKey** | **String** |  The KMS key details.  |  [optional] |
|**evidenceFinderEnabled** | **Boolean** | &lt;p&gt;Specifies whether the evidence finder feature is enabled. Change this attribute to enable or disable evidence finder.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When you use this attribute to disable evidence finder, Audit Manager deletes the event data store that’s used to query your evidence data. As a result, you can’t re-enable evidence finder and use the feature again. Your only alternative is to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeregisterAccount.html\&quot;&gt;deregister&lt;/a&gt; and then &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_RegisterAccount.html\&quot;&gt;re-register&lt;/a&gt; Audit Manager. &lt;/p&gt; &lt;/important&gt; |  [optional] |
|**deregistrationPolicy** | [**UpdateSettingsRequestDeregistrationPolicy**](UpdateSettingsRequestDeregistrationPolicy.md) |  |  [optional] |
|**defaultExportDestination** | [**UpdateSettingsRequestDefaultExportDestination**](UpdateSettingsRequestDefaultExportDestination.md) |  |  [optional] |



