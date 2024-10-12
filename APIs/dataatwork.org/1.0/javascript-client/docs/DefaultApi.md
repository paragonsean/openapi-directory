# OpenSkillsApi.DefaultApi

All URIs are relative to *http://api.dataatwork.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobsAutocompleteGet**](DefaultApi.md#jobsAutocompleteGet) | **GET** /jobs/autocomplete | Job Title Autocomplete
[**jobsGet**](DefaultApi.md#jobsGet) | **GET** /jobs | Job Titles and Descriptions
[**jobsIdGet**](DefaultApi.md#jobsIdGet) | **GET** /jobs/{id} | Job Title and Description
[**jobsIdRelatedJobsGet**](DefaultApi.md#jobsIdRelatedJobsGet) | **GET** /jobs/{id}/related_jobs | Jobs Associated with a Job
[**jobsIdRelatedSkillsGet**](DefaultApi.md#jobsIdRelatedSkillsGet) | **GET** /jobs/{id}/related_skills | Skills Associated with a Job
[**jobsNormalizeGet**](DefaultApi.md#jobsNormalizeGet) | **GET** /jobs/normalize | Job Title Normalization
[**jobsUnusualTitlesGet**](DefaultApi.md#jobsUnusualTitlesGet) | **GET** /jobs/unusual_titles | Unusual Job Titles
[**skillsAutocompleteGet**](DefaultApi.md#skillsAutocompleteGet) | **GET** /skills/autocomplete | Skill Name Autocomplete
[**skillsGet**](DefaultApi.md#skillsGet) | **GET** /skills | Skill Names and Descriptions
[**skillsIdGet**](DefaultApi.md#skillsIdGet) | **GET** /skills/{id} | Skill Name and Description
[**skillsIdRelatedJobsGet**](DefaultApi.md#skillsIdRelatedJobsGet) | **GET** /skills/{id}/related_jobs | Jobs Associated with a Skill
[**skillsIdRelatedSkillsGet**](DefaultApi.md#skillsIdRelatedSkillsGet) | **GET** /skills/{id}/related_skills | Skills Associated with a Skill
[**skillsNormalizeGet**](DefaultApi.md#skillsNormalizeGet) | **GET** /skills/normalize | Skill Name Normalization



## jobsAutocompleteGet

> [Job] jobsAutocompleteGet(opts)

Job Title Autocomplete

Retrieves the names, descriptions, and UUIDs of all job titles matching a given search criteria.

### Example

```javascript
import OpenSkillsApi from 'open_skills_api';

let apiInstance = new OpenSkillsApi.DefaultApi();
let opts = {
  'beginsWith': "beginsWith_example", // String | Find job titles beginning with the given text fragment
  'contains': "contains_example", // String | Find job titles containing the given text fragment
  'endsWith': "endsWith_example" // String | Find job titles ending with the given text fragment
};
apiInstance.jobsAutocompleteGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beginsWith** | **String**| Find job titles beginning with the given text fragment | [optional] 
 **contains** | **String**| Find job titles containing the given text fragment | [optional] 
 **endsWith** | **String**| Find job titles ending with the given text fragment | [optional] 

### Return type

[**[Job]**](Job.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsGet

> [Job] jobsGet(opts)

Job Titles and Descriptions

Retrieves the names, descriptions, and UUIDs of all job titles.

### Example

```javascript
import OpenSkillsApi from 'open_skills_api';

let apiInstance = new OpenSkillsApi.DefaultApi();
let opts = {
  'offset': 56, // Number | Pagination offset. Default is 0.
  'limit': 56 // Number | Maximum number of items per page. Default is 20 and cannot exceed 500.
};
apiInstance.jobsGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **Number**| Pagination offset. Default is 0. | [optional] 
 **limit** | **Number**| Maximum number of items per page. Default is 20 and cannot exceed 500. | [optional] 

### Return type

[**[Job]**](Job.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsIdGet

> Job jobsIdGet(id, opts)

Job Title and Description

Retrieves the name, description, and UUID of a job by specifying its O*NET SOC Code or UUID.

### Example

```javascript
import OpenSkillsApi from 'open_skills_api';

let apiInstance = new OpenSkillsApi.DefaultApi();
let id = "id_example"; // String | The O*NET SOC Code or UUID of the job title to retrieve
let opts = {
  'fips': "fips_example" // String | The FIPS Code of a Core-Based Statistical Area. Only return the job if present in this area
};
apiInstance.jobsIdGet(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The O*NET SOC Code or UUID of the job title to retrieve | 
 **fips** | **String**| The FIPS Code of a Core-Based Statistical Area. Only return the job if present in this area | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsIdRelatedJobsGet

> JobRelatedJobs jobsIdRelatedJobsGet(id)

Jobs Associated with a Job

Retrieves a collection of jobs associated with a specified job.

### Example

```javascript
import OpenSkillsApi from 'open_skills_api';

let apiInstance = new OpenSkillsApi.DefaultApi();
let id = "id_example"; // String | The UUID of the job to retrieve related jobs for
apiInstance.jobsIdRelatedJobsGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The UUID of the job to retrieve related jobs for | 

### Return type

[**JobRelatedJobs**](JobRelatedJobs.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsIdRelatedSkillsGet

> JobSkills jobsIdRelatedSkillsGet(id)

Skills Associated with a Job

Retrieves a collection of skills associated with a specified job.

### Example

```javascript
import OpenSkillsApi from 'open_skills_api';

let apiInstance = new OpenSkillsApi.DefaultApi();
let id = "id_example"; // String | The UUID of the job to retrieve skills for
apiInstance.jobsIdRelatedSkillsGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The UUID of the job to retrieve skills for | 

### Return type

[**JobSkills**](JobSkills.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsNormalizeGet

> [NormalizedJob] jobsNormalizeGet(jobTitle, opts)

Job Title Normalization

Retrieves the canonical job title for a synonymous job title

### Example

```javascript
import OpenSkillsApi from 'open_skills_api';

let apiInstance = new OpenSkillsApi.DefaultApi();
let jobTitle = "jobTitle_example"; // String | Find the canonical job title(s) for jobs matching the given text fragment
let opts = {
  'limit': 56 // Number | Maximumn number of job title synonyms to return. Default is 1 and cannot exceed 10.
};
apiInstance.jobsNormalizeGet(jobTitle, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobTitle** | **String**| Find the canonical job title(s) for jobs matching the given text fragment | 
 **limit** | **Number**| Maximumn number of job title synonyms to return. Default is 1 and cannot exceed 10. | [optional] 

### Return type

[**[NormalizedJob]**](NormalizedJob.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobsUnusualTitlesGet

> [NormalizedJob] jobsUnusualTitlesGet()

Unusual Job Titles

Retrieves a list of unusual job titles and the UUIDs of their canonical jobs.

### Example

```javascript
import OpenSkillsApi from 'open_skills_api';

let apiInstance = new OpenSkillsApi.DefaultApi();
apiInstance.jobsUnusualTitlesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[NormalizedJob]**](NormalizedJob.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## skillsAutocompleteGet

> SkillJobs skillsAutocompleteGet(opts)

Skill Name Autocomplete

Retrieves the names, descriptions, and UUIDs of all skills matching a given search criteria.

### Example

```javascript
import OpenSkillsApi from 'open_skills_api';

let apiInstance = new OpenSkillsApi.DefaultApi();
let opts = {
  'beginsWith': "beginsWith_example", // String | Find skill names beginning with the given text fragment
  'contains': "contains_example", // String | Find skill names containing the given text fragment
  'endsWith': "endsWith_example" // String | Find skill names ending with the given text fragment
};
apiInstance.skillsAutocompleteGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beginsWith** | **String**| Find skill names beginning with the given text fragment | [optional] 
 **contains** | **String**| Find skill names containing the given text fragment | [optional] 
 **endsWith** | **String**| Find skill names ending with the given text fragment | [optional] 

### Return type

[**SkillJobs**](SkillJobs.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## skillsGet

> [Skill] skillsGet(opts)

Skill Names and Descriptions

Retrieve the names, descriptions, and UUIDs of all skills.

### Example

```javascript
import OpenSkillsApi from 'open_skills_api';

let apiInstance = new OpenSkillsApi.DefaultApi();
let opts = {
  'offset': 56, // Number | Pagination offset. Default is 0.
  'limit': 56 // Number | Maximum number of items per page. Default is 20 and cannot exceed 500.
};
apiInstance.skillsGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **Number**| Pagination offset. Default is 0. | [optional] 
 **limit** | **Number**| Maximum number of items per page. Default is 20 and cannot exceed 500. | [optional] 

### Return type

[**[Skill]**](Skill.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## skillsIdGet

> Skill skillsIdGet(id)

Skill Name and Description

Retrieves the name, description, and UUID of a job by specifying its UUID.

### Example

```javascript
import OpenSkillsApi from 'open_skills_api';

let apiInstance = new OpenSkillsApi.DefaultApi();
let id = "id_example"; // String | The UUID of the skill name to retrieve
apiInstance.skillsIdGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The UUID of the skill name to retrieve | 

### Return type

[**Skill**](Skill.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## skillsIdRelatedJobsGet

> SkillJobs skillsIdRelatedJobsGet(id)

Jobs Associated with a Skill

Retrieves a collection of jobs associated with a specified skill.

### Example

```javascript
import OpenSkillsApi from 'open_skills_api';

let apiInstance = new OpenSkillsApi.DefaultApi();
let id = "id_example"; // String | The UUID of the skill to retrieve jobs for
apiInstance.skillsIdRelatedJobsGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The UUID of the skill to retrieve jobs for | 

### Return type

[**SkillJobs**](SkillJobs.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## skillsIdRelatedSkillsGet

> SkillRelatedSkills skillsIdRelatedSkillsGet(id)

Skills Associated with a Skill

Retrieves a collection of skills associated with a specified skill.

### Example

```javascript
import OpenSkillsApi from 'open_skills_api';

let apiInstance = new OpenSkillsApi.DefaultApi();
let id = "id_example"; // String | The UUID of the skill to retrieve related skills for
apiInstance.skillsIdRelatedSkillsGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The UUID of the skill to retrieve related skills for | 

### Return type

[**SkillRelatedSkills**](SkillRelatedSkills.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## skillsNormalizeGet

> [NormalizedSkill] skillsNormalizeGet(skillName)

Skill Name Normalization

Retrieves the canonical skill name for a synonymous skill name

### Example

```javascript
import OpenSkillsApi from 'open_skills_api';

let apiInstance = new OpenSkillsApi.DefaultApi();
let skillName = "skillName_example"; // String | Find the canonical skill name(s) for skills matching the given text fragment
apiInstance.skillsNormalizeGet(skillName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skillName** | **String**| Find the canonical skill name(s) for skills matching the given text fragment | 

### Return type

[**[NormalizedSkill]**](NormalizedSkill.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

