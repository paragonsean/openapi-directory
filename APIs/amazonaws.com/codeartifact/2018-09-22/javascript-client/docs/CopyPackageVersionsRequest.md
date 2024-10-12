# CodeArtifact.CopyPackageVersionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | **[String]** | &lt;p&gt; The versions of the package to be copied. &lt;/p&gt; &lt;note&gt; &lt;p&gt; You must specify &lt;code&gt;versions&lt;/code&gt; or &lt;code&gt;versionRevisions&lt;/code&gt;. You cannot specify both. &lt;/p&gt; &lt;/note&gt; | [optional] 
**versionRevisions** | **{String: String}** | &lt;p&gt; A list of key-value pairs. The keys are package versions and the values are package version revisions. A &lt;code&gt;CopyPackageVersion&lt;/code&gt; operation succeeds if the specified versions in the source repository match the specified package version revision. &lt;/p&gt; &lt;note&gt; &lt;p&gt; You must specify &lt;code&gt;versions&lt;/code&gt; or &lt;code&gt;versionRevisions&lt;/code&gt;. You cannot specify both. &lt;/p&gt; &lt;/note&gt; | [optional] 
**allowOverwrite** | **Boolean** |  Set to true to overwrite a package version that already exists in the destination repository. If set to false and the package version already exists in the destination repository, the package version is returned in the &lt;code&gt;failedVersions&lt;/code&gt; field of the response with an &lt;code&gt;ALREADY_EXISTS&lt;/code&gt; error code.  | [optional] 
**includeFromUpstream** | **Boolean** |  Set to true to copy packages from repositories that are upstream from the source repository to the destination repository. The default setting is false. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html\&quot;&gt;Working with upstream repositories&lt;/a&gt;.  | [optional] 


