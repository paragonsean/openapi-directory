# CloudTalentSolutionApi.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **[String]** | Strongly recommended for the best service experience. Location(s) where the employer is looking to hire for this job posting. Specifying the full street address(es) of the hiring location enables better API results, especially job searches by commute time. At most 50 locations are allowed for best search performance. If a job has more locations, it is suggested to split it into multiple jobs with unique requisition_ids (e.g. &#39;ReqA&#39; becomes &#39;ReqA-1&#39;, &#39;ReqA-2&#39;, and so on.) as multiple jobs with the same company, language_code and requisition_id are not allowed. If the original requisition_id must be preserved, a custom field should be used for storage. It is also suggested to group the locations that close to each other in the same job for better search experience. Jobs with multiple addresses must have their addresses with the same LocationType to allow location filtering to work properly. (For example, a Job with addresses \&quot;1600 Amphitheatre Parkway, Mountain View, CA, USA\&quot; and \&quot;London, UK\&quot; may not have location filters applied correctly at search time since the first is a LocationType.STREET_ADDRESS and the second is a LocationType.LOCALITY.) If a job needs to have multiple addresses, it is suggested to split it into multiple jobs with same LocationTypes. The maximum number of allowed characters is 500. | [optional] 
**applicationInfo** | [**ApplicationInfo**](ApplicationInfo.md) |  | [optional] 
**company** | **String** | Required. The resource name of the company listing the job. The format is \&quot;projects/{project_id}/tenants/{tenant_id}/companies/{company_id}\&quot;. For example, \&quot;projects/foo/tenants/bar/companies/baz\&quot;. | [optional] 
**companyDisplayName** | **String** | Output only. Display name of the company listing the job. | [optional] [readonly] 
**compensationInfo** | [**CompensationInfo**](CompensationInfo.md) |  | [optional] 
**customAttributes** | [**{String: CustomAttribute}**](CustomAttribute.md) | A map of fields to hold both filterable and non-filterable custom job attributes that are not covered by the provided structured fields. The keys of the map are strings up to 64 bytes and must match the pattern: &#x60;a-zA-Z*&#x60;. For example, key0LikeThis or KEY_1_LIKE_THIS. At most 100 filterable and at most 100 unfilterable keys are supported. For filterable &#x60;string_values&#x60;, across all keys at most 200 values are allowed, with each string no more than 255 characters. For unfilterable &#x60;string_values&#x60;, the maximum total size of &#x60;string_values&#x60; across all keys is 50KB. | [optional] 
**degreeTypes** | **[String]** | The desired education degrees for the job, such as Bachelors, Masters. | [optional] 
**department** | **String** | The department or functional area within the company with the open position. The maximum number of allowed characters is 255. | [optional] 
**derivedInfo** | [**JobDerivedInfo**](JobDerivedInfo.md) |  | [optional] 
**description** | **String** | Required. The description of the job, which typically includes a multi-paragraph description of the company and related information. Separate fields are provided on the job object for responsibilities, qualifications, and other job characteristics. Use of these separate job fields is recommended. This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags. The maximum number of allowed characters is 100,000. | [optional] 
**employmentTypes** | **[String]** | The employment type(s) of a job, for example, full time or part time. | [optional] 
**incentives** | **String** | A description of bonus, commission, and other compensation incentives associated with the job not including salary or pay. The maximum number of allowed characters is 10,000. | [optional] 
**jobBenefits** | **[String]** | The benefits included with the job. | [optional] 
**jobEndTime** | **String** | The end timestamp of the job. Typically this field is used for contracting engagements. Invalid timestamps are ignored. | [optional] 
**jobLevel** | **String** | The experience level associated with the job, such as \&quot;Entry Level\&quot;. | [optional] 
**jobStartTime** | **String** | The start timestamp of the job in UTC time zone. Typically this field is used for contracting engagements. Invalid timestamps are ignored. | [optional] 
**languageCode** | **String** | The language of the posting. This field is distinct from any requirements for fluency that are associated with the job. Language codes must be in BCP-47 format, such as \&quot;en-US\&quot; or \&quot;sr-Latn\&quot;. For more information, see [Tags for Identifying Languages](https://tools.ietf.org/html/bcp47){: class&#x3D;\&quot;external\&quot; target&#x3D;\&quot;_blank\&quot; }. If this field is unspecified and Job.description is present, detected language code based on Job.description is assigned, otherwise defaults to &#39;en_US&#39;. | [optional] 
**name** | **String** | Required during job update. The resource name for the job. This is generated by the service when a job is created. The format is \&quot;projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}\&quot;. For example, \&quot;projects/foo/tenants/bar/jobs/baz\&quot;. Use of this field in job queries and API calls is preferred over the use of requisition_id since this value is unique. | [optional] 
**postingCreateTime** | **String** | Output only. The timestamp when this job posting was created. | [optional] [readonly] 
**postingExpireTime** | **String** | Strongly recommended for the best service experience. The expiration timestamp of the job. After this timestamp, the job is marked as expired, and it no longer appears in search results. The expired job can&#39;t be listed by the ListJobs API, but it can be retrieved with the GetJob API or updated with the UpdateJob API or deleted with the DeleteJob API. An expired job can be updated and opened again by using a future expiration timestamp. Updating an expired job fails if there is another existing open job with same company, language_code and requisition_id. The expired jobs are retained in our system for 90 days. However, the overall expired job count cannot exceed 3 times the maximum number of open jobs over previous 7 days. If this threshold is exceeded, expired jobs are cleaned out in order of earliest expire time. Expired jobs are no longer accessible after they are cleaned out. Invalid timestamps are ignored, and treated as expire time not provided. If the timestamp is before the instant request is made, the job is treated as expired immediately on creation. This kind of job can not be updated. And when creating a job with past timestamp, the posting_publish_time must be set before posting_expire_time. The purpose of this feature is to allow other objects, such as Application, to refer a job that didn&#39;t exist in the system prior to becoming expired. If you want to modify a job that was expired on creation, delete it and create a new one. If this value isn&#39;t provided at the time of job creation or is invalid, the job posting expires after 30 days from the job&#39;s creation time. For example, if the job was created on 2017/01/01 13:00AM UTC with an unspecified expiration date, the job expires after 2017/01/31 13:00AM UTC. If this value isn&#39;t provided on job update, it depends on the field masks set by UpdateJobRequest.update_mask. If the field masks include job_end_time, or the masks are empty meaning that every field is updated, the job posting expires after 30 days from the job&#39;s last update time. Otherwise the expiration date isn&#39;t updated. | [optional] 
**postingPublishTime** | **String** | The timestamp this job posting was most recently published. The default value is the time the request arrives at the server. Invalid timestamps are ignored. | [optional] 
**postingRegion** | **String** | The job PostingRegion (for example, state, country) throughout which the job is available. If this field is set, a LocationFilter in a search query within the job region finds this job posting if an exact location match isn&#39;t specified. If this field is set to PostingRegion.NATION or PostingRegion.ADMINISTRATIVE_AREA, setting job Job.addresses to the same location level as this field is strongly recommended. | [optional] 
**postingUpdateTime** | **String** | Output only. The timestamp when this job posting was last updated. | [optional] [readonly] 
**processingOptions** | [**ProcessingOptions**](ProcessingOptions.md) |  | [optional] 
**promotionValue** | **Number** | A promotion value of the job, as determined by the client. The value determines the sort order of the jobs returned when searching for jobs using the featured jobs search call, with higher promotional values being returned first and ties being resolved by relevance sort. Only the jobs with a promotionValue &gt;0 are returned in a FEATURED_JOB_SEARCH. Default value is 0, and negative values are treated as 0. | [optional] 
**qualifications** | **String** | A description of the qualifications required to perform the job. The use of this field is recommended as an alternative to using the more general description field. This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags. The maximum number of allowed characters is 10,000. | [optional] 
**requisitionId** | **String** | Required. The requisition ID, also referred to as the posting ID, is assigned by the client to identify a job. This field is intended to be used by clients for client identification and tracking of postings. A job isn&#39;t allowed to be created if there is another job with the same company, language_code and requisition_id. The maximum number of allowed characters is 255. | [optional] 
**responsibilities** | **String** | A description of job responsibilities. The use of this field is recommended as an alternative to using the more general description field. This field accepts and sanitizes HTML input, and also accepts bold, italic, ordered list, and unordered list markup tags. The maximum number of allowed characters is 10,000. | [optional] 
**title** | **String** | Required. The title of the job, such as \&quot;Software Engineer\&quot; The maximum number of allowed characters is 500. | [optional] 
**visibility** | **String** | Deprecated. The job is only visible to the owner. The visibility of the job. Defaults to Visibility.ACCOUNT_ONLY if not specified. | [optional] 



## Enum: [DegreeTypesEnum]


* `DEGREE_TYPE_UNSPECIFIED` (value: `"DEGREE_TYPE_UNSPECIFIED"`)

* `PRIMARY_EDUCATION` (value: `"PRIMARY_EDUCATION"`)

* `LOWER_SECONDARY_EDUCATION` (value: `"LOWER_SECONDARY_EDUCATION"`)

* `UPPER_SECONDARY_EDUCATION` (value: `"UPPER_SECONDARY_EDUCATION"`)

* `ADULT_REMEDIAL_EDUCATION` (value: `"ADULT_REMEDIAL_EDUCATION"`)

* `ASSOCIATES_OR_EQUIVALENT` (value: `"ASSOCIATES_OR_EQUIVALENT"`)

* `BACHELORS_OR_EQUIVALENT` (value: `"BACHELORS_OR_EQUIVALENT"`)

* `MASTERS_OR_EQUIVALENT` (value: `"MASTERS_OR_EQUIVALENT"`)

* `DOCTORAL_OR_EQUIVALENT` (value: `"DOCTORAL_OR_EQUIVALENT"`)





## Enum: [EmploymentTypesEnum]


* `EMPLOYMENT_TYPE_UNSPECIFIED` (value: `"EMPLOYMENT_TYPE_UNSPECIFIED"`)

* `FULL_TIME` (value: `"FULL_TIME"`)

* `PART_TIME` (value: `"PART_TIME"`)

* `CONTRACTOR` (value: `"CONTRACTOR"`)

* `CONTRACT_TO_HIRE` (value: `"CONTRACT_TO_HIRE"`)

* `TEMPORARY` (value: `"TEMPORARY"`)

* `INTERN` (value: `"INTERN"`)

* `VOLUNTEER` (value: `"VOLUNTEER"`)

* `PER_DIEM` (value: `"PER_DIEM"`)

* `FLY_IN_FLY_OUT` (value: `"FLY_IN_FLY_OUT"`)

* `OTHER_EMPLOYMENT_TYPE` (value: `"OTHER_EMPLOYMENT_TYPE"`)





## Enum: [JobBenefitsEnum]


* `JOB_BENEFIT_UNSPECIFIED` (value: `"JOB_BENEFIT_UNSPECIFIED"`)

* `CHILD_CARE` (value: `"CHILD_CARE"`)

* `DENTAL` (value: `"DENTAL"`)

* `DOMESTIC_PARTNER` (value: `"DOMESTIC_PARTNER"`)

* `FLEXIBLE_HOURS` (value: `"FLEXIBLE_HOURS"`)

* `MEDICAL` (value: `"MEDICAL"`)

* `LIFE_INSURANCE` (value: `"LIFE_INSURANCE"`)

* `PARENTAL_LEAVE` (value: `"PARENTAL_LEAVE"`)

* `RETIREMENT_PLAN` (value: `"RETIREMENT_PLAN"`)

* `SICK_DAYS` (value: `"SICK_DAYS"`)

* `VACATION` (value: `"VACATION"`)

* `VISION` (value: `"VISION"`)





## Enum: JobLevelEnum


* `JOB_LEVEL_UNSPECIFIED` (value: `"JOB_LEVEL_UNSPECIFIED"`)

* `ENTRY_LEVEL` (value: `"ENTRY_LEVEL"`)

* `EXPERIENCED` (value: `"EXPERIENCED"`)

* `MANAGER` (value: `"MANAGER"`)

* `DIRECTOR` (value: `"DIRECTOR"`)

* `EXECUTIVE` (value: `"EXECUTIVE"`)





## Enum: PostingRegionEnum


* `POSTING_REGION_UNSPECIFIED` (value: `"POSTING_REGION_UNSPECIFIED"`)

* `ADMINISTRATIVE_AREA` (value: `"ADMINISTRATIVE_AREA"`)

* `NATION` (value: `"NATION"`)

* `TELECOMMUTE` (value: `"TELECOMMUTE"`)





## Enum: VisibilityEnum


* `VISIBILITY_UNSPECIFIED` (value: `"VISIBILITY_UNSPECIFIED"`)

* `ACCOUNT_ONLY` (value: `"ACCOUNT_ONLY"`)

* `SHARED_WITH_GOOGLE` (value: `"SHARED_WITH_GOOGLE"`)

* `SHARED_WITH_PUBLIC` (value: `"SHARED_WITH_PUBLIC"`)




