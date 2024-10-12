

# Project


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**closedDate** | **OffsetDateTime** | The date when the project was closed and booked.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**contactPersonId** | **Integer** | The number of the contact person. Has to be from the same customer as the one defined in the project.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**costPrice** | **Double** | Sum of registrations based on cost price for the project&lt;p class&#x3D;&#39;filter&#39;&gt;Read-only: true&lt;/p&gt;&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] [readonly] |
|**customerNumber** | **Integer** | Number of customer this project is for. Required if project type is not Internal.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**deliveryDate** | **OffsetDateTime** | The project delivery date.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**deliveryLocationNumber** | **Integer** | The location number used to deliver the project.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**departmentNumber** | **Integer** | Only relevant if the user uses addon dimensions&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**description** | **String** | Text describing the project.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: not filterable&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**fixedPrice** | **Double** | If a fixed price is agreed upon with a customer, this can be utilized. It is not retrieved when invoicing, however, so it is only used for reporting.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**invoicedTotal** | **Double** | Sum of invoiced amount for the project&lt;p class&#x3D;&#39;filter&#39;&gt;Read-only: true&lt;/p&gt;&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] [readonly] |
|**isBarred** | **Boolean** | Barred projects cannot retrieve registrations&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**isClosed** | **Boolean** | Shows if the project is closed. Closed project can&#39;t accept more entries.&lt;p class&#x3D;&#39;filter&#39;&gt;Read-only: true&lt;/p&gt;&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] [readonly] |
|**isMainProject** | **Boolean** | Decides whether the project is a main-project or sub-project. If false, it is a sub-project. If true, it is a main-project. Main-projects are grouping of projects. Main-project can&#39;t have entries, only sub-projects can.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**isMileageInvoiced** | **Boolean** | Determines whether mileage should be included on sales invoices of the project&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**lastUpdated** | **OffsetDateTime** | The date and time when this project was last updated. Use it in the filter to retrieve only updated projects.&lt;p class&#x3D;&#39;filter&#39;&gt;Read-only: true&lt;/p&gt;&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] [readonly] |
|**mainProjectNumber** | **Integer** | The number of the main project, if this is a sub project linked to a main project. It can be null for both main and sub projects (sub project can exist not linked to any main project, like standalone project).&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**mileage** | **Double** | Default amount of mileage for the project&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**name** | **String** | Name of the project.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin, like&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  |
|**number** | **Integer** | The unique number of the project. If it&#39;s not provided in the POST requests, it&#39;s auto-generated.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: true&lt;/p&gt; |  [optional] |
|**objectVersion** | **String** | The object version, required for PUT requests.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: not filterable&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**otherResponsibleEmployeeNumber** | **Integer** | Second employee number that is responsible for the project.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**projectGroupNumber** | **Integer** | The number of the project group that this project belongs.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  |
|**responsibleEmployeeNumber** | **Integer** | The employee number that is responsible for the project.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**salesPrice** | **Double** | Sum of registrations based on sales price for the project&lt;p class&#x3D;&#39;filter&#39;&gt;Read-only: true&lt;/p&gt;&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] [readonly] |
|**status** | **Integer** | The number of the project status. Project status is a separate manageable resource.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |



