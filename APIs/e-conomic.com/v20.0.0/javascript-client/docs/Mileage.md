# VismaEConomicOpenApi.Mileage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **Date** | The date of the project mileage entry&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; | 
**distance** | **Number** | The distance amount that the mileage registration should contain&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: not filterable&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; | 
**employeeNumber** | **Number** | The employee number of the project mileage entry&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; | 
**from** | **String** | The starting place of the travel which the mileage registration reflects&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: not filterable&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; | [optional] 
**includeApprove** | **Boolean** | By default it is true, so a user with rights will be able to approve.        Once it is approved, field becomes false and it will be impossible to approve ever again.&lt;p class&#x3D;&#39;filter&#39;&gt;Read-only: true&lt;/p&gt;&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; | [optional] [readonly] 
**isApproved** | **Boolean** | Value specifying if the mileage was approved. If it was approved, it can not be updated anymore.&lt;p class&#x3D;&#39;filter&#39;&gt;Read-only: true&lt;/p&gt;&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; | [optional] [readonly] 
**number** | **Number** | The unique number of the project mileage entry&lt;p class&#x3D;&#39;filter&#39;&gt;Read-only: true&lt;/p&gt;&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: true&lt;/p&gt; | [optional] [readonly] 
**objectVersion** | **String** | The object version, required for PUT requests.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: not filterable&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; | [optional] 
**projectNumber** | **Number** | The project number of the project mileage entry&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; | 
**to** | **String** | The destination of the travel which the mileage registration reflects&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: not filterable&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; | [optional] 


