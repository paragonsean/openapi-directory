# AwsAuditManager.CreateAssessmentReportRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** |  The name of the new assessment report.  | 
**description** | **String** |  The description of the assessment report.  | [optional] 
**queryStatement** | **String** | &lt;p&gt;A SQL statement that represents an evidence finder query.&lt;/p&gt; &lt;p&gt;Provide this parameter when you want to generate an assessment report from the results of an evidence finder search query. When you use this parameter, Audit Manager generates a one-time report using only the evidence from the query output. This report does not include any assessment evidence that was manually &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/generate-assessment-report.html#generate-assessment-report-include-evidence\&quot;&gt;added to a report using the console&lt;/a&gt;, or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchAssociateAssessmentReportEvidence.html\&quot;&gt;associated with a report using the API&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;To use this parameter, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_EvidenceFinderEnablement.html#auditmanager-Type-EvidenceFinderEnablement-enablementStatus\&quot;&gt;enablementStatus&lt;/a&gt; of evidence finder must be &lt;code&gt;ENABLED&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; For examples and help resolving &lt;code&gt;queryStatement&lt;/code&gt; validation exceptions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-finder-issues.html#querystatement-exceptions\&quot;&gt;Troubleshooting evidence finder issues&lt;/a&gt; in the &lt;i&gt;Audit Manager User Guide.&lt;/i&gt; &lt;/p&gt; | [optional] 


