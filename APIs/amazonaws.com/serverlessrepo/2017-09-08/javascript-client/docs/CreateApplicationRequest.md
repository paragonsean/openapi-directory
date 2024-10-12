# AwsServerlessApplicationRepository.CreateApplicationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **String** | &lt;p&gt;The name of the author publishing the app.&lt;/p&gt;&lt;p&gt;Minimum length&#x3D;1. Maximum length&#x3D;127.&lt;/p&gt;&lt;p&gt;Pattern \&quot;^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$\&quot;;&lt;/p&gt; | 
**description** | **String** | &lt;p&gt;The description of the application.&lt;/p&gt;&lt;p&gt;Minimum length&#x3D;1. Maximum length&#x3D;256&lt;/p&gt; | 
**homePageUrl** | **String** | A URL with more information about the application, for example the location of your GitHub repository for the application. | [optional] 
**labels** | **[String]** | &lt;p&gt;Labels to improve discovery of apps in search results.&lt;/p&gt;&lt;p&gt;Minimum length&#x3D;1. Maximum length&#x3D;127. Maximum number of labels: 10&lt;/p&gt;&lt;p&gt;Pattern: \&quot;^[a-zA-Z0-9+\\\\-_:\\/@]+$\&quot;;&lt;/p&gt; | [optional] 
**licenseBody** | **String** | &lt;p&gt;A local text file that contains the license of the app that matches the spdxLicenseID value of your application.  The file has the format file://&amp;lt;path&gt;/&amp;lt;filename&gt;.&lt;/p&gt;&lt;p&gt;Maximum size 5 MB&lt;/p&gt;&lt;p&gt;You can specify only one of licenseBody and licenseUrl; otherwise, an error results.&lt;/p&gt; | [optional] 
**licenseUrl** | **String** | &lt;p&gt;A link to the S3 object that contains the license of the app that matches the spdxLicenseID value of your application.&lt;/p&gt;&lt;p&gt;Maximum size 5 MB&lt;/p&gt;&lt;p&gt;You can specify only one of licenseBody and licenseUrl; otherwise, an error results.&lt;/p&gt; | [optional] 
**name** | **String** | &lt;p&gt;The name of the application that you want to publish.&lt;/p&gt;&lt;p&gt;Minimum length&#x3D;1. Maximum length&#x3D;140&lt;/p&gt;&lt;p&gt;Pattern: \&quot;[a-zA-Z0-9\\\\-]+\&quot;;&lt;/p&gt; | 
**readmeBody** | **String** | &lt;p&gt;A local text readme file in Markdown language that contains a more detailed description of the application and how it works.  The file has the format file://&amp;lt;path&gt;/&amp;lt;filename&gt;.&lt;/p&gt;&lt;p&gt;Maximum size 5 MB&lt;/p&gt;&lt;p&gt;You can specify only one of readmeBody and readmeUrl; otherwise, an error results.&lt;/p&gt; | [optional] 
**readmeUrl** | **String** | &lt;p&gt;A link to the S3 object in Markdown language that contains a more detailed description of the application and how it works.&lt;/p&gt;&lt;p&gt;Maximum size 5 MB&lt;/p&gt;&lt;p&gt;You can specify only one of readmeBody and readmeUrl; otherwise, an error results.&lt;/p&gt; | [optional] 
**semanticVersion** | **String** | &lt;p&gt;The semantic version of the application:&lt;/p&gt;&lt;p&gt;  &lt;a href&#x3D;\&quot;https://semver.org/\&quot;&gt;https://semver.org/&lt;/a&gt;  &lt;/p&gt; | [optional] 
**sourceCodeArchiveUrl** | **String** | &lt;p&gt;A link to the S3 object that contains the ZIP archive of the source code for this version of your application.&lt;/p&gt;&lt;p&gt;Maximum size 50 MB&lt;/p&gt; | [optional] 
**sourceCodeUrl** | **String** | A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit. | [optional] 
**spdxLicenseId** | **String** | A valid identifier from &lt;a href&#x3D;\&quot;https://spdx.org/licenses/\&quot;&gt;https://spdx.org/licenses/&lt;/a&gt;. | [optional] 
**templateBody** | **String** | &lt;p&gt;The local raw packaged AWS SAM template file of your application.  The file has the format file://&amp;lt;path&gt;/&amp;lt;filename&gt;.&lt;/p&gt;&lt;p&gt;You can specify only one of templateBody and templateUrl; otherwise an error results.&lt;/p&gt; | [optional] 
**templateUrl** | **String** | &lt;p&gt;A link to the S3 object containing the packaged AWS SAM template of your application.&lt;/p&gt;&lt;p&gt;You can specify only one of templateBody and templateUrl; otherwise an error results.&lt;/p&gt; | [optional] 


