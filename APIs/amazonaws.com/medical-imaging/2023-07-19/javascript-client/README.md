# aws_health_imaging

AwsHealthImaging - JavaScript client for aws_health_imaging
<p>This is the <i>AWS HealthImaging API Reference</i>. AWS HealthImaging is an AWS service for storing, accessing, and analyzing medical images. For an introduction to the service, see the <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide\"> <i>AWS HealthImaging Developer Guide</i> </a>.</p> <note> <p>We recommend using one of the AWS Software Development Kits (SDKs) for your programming language, as they take care of request authentication, serialization, and connection management. For more information, see <a href=\"http://aws.amazon.com/developer/tools\">Tools to build on AWS</a>.</p> <p>For information about using AWS HealthImaging API actions in one of the language-specific AWS SDKs, refer to the <i>See Also</i> link at the end of each section that describes an API action or data type.</p> </note> <p>The following sections list AWS HealthImaging API actions categorized according to functionality. Links are provided to actions within this Reference, along with links back to corresponding sections in the <i>AWS HealthImaging Developer Guide</i> so you can view console procedures and CLI/SDK code examples.</p> <p class=\"title\"> <b>Data store actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_CreateDatastore.html\">CreateDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/create-data-store.html\">Creating a data store</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetDatastore.html\">GetDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-data-store.html\">Getting data store properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListDatastores.html\">ListDatastores</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-data-stores.html\">Listing data stores</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_DeleteDatastore.html\">DeleteDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/delete-data-store.html\">Deleting a data store</a>.</p> </li> </ul> <p class=\"title\"> <b>Import job actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_StartDICOMImportJob.html\">StartDICOMImportJob</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/start-dicom-import-job.html\">Starting an import job</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetDICOMImportJob.html\">GetDICOMImportJob</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-dicom-import-job.html\">Getting import job properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListDICOMImportJobs.html\">ListDICOMImportJobs</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-dicom-import-jobs.html\">Listing import jobs</a>.</p> </li> </ul> <p class=\"title\"> <b>Image set access actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_SearchImageSets.html\">SearchImageSets</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/search-image-sets.html\">Searching image sets</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageSet.html\">GetImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-set-properties.html\">Getting image set properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageSetMetadata.html\">GetImageSetMetadata</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-set-metadata.html\">Getting image set metadata</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageFrame.html\">GetImageFrame</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-frame.html\">Getting image set pixel data</a>.</p> </li> </ul> <p class=\"title\"> <b>Image set modification actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListImageSetVersions.html\">ListImageSetVersions</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-image-set-versions.html\">Listing image set versions</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_UpdateImageSetMetadata.html\">UpdateImageSetMetadata</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/update-image-set-metadata.html\">Updating image set metadata</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_CopyImageSet.html\">CopyImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/copy-image-set.html\">Copying an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_DeleteImageSet.html\">DeleteImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/delete-image-set.html\">Deleting an image set</a>.</p> </li> </ul> <p class=\"title\"> <b>Tagging actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_TagResource.html\">TagResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListTagsForResource.html\">ListTagsForResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_UntagResource.html\">UntagResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> </ul>
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2023-07-19
- Package version: 2023-07-19
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://github.com/mermade/aws2openapi](https://github.com/mermade/aws2openapi)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install aws_health_imaging --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your aws_health_imaging from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var AwsHealthImaging = require('aws_health_imaging');

var defaultClient = AwsHealthImaging.ApiClient.instance;
// Configure API key authorization: hmac
var hmac = defaultClient.authentications['hmac'];
hmac.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix['Authorization'] = "Token"

var api = new AwsHealthImaging.DefaultApi()
var datastoreId = "datastoreId_example"; // {String} The data store identifier.
var sourceImageSetId = "sourceImageSetId_example"; // {String} The source image set identifier.
var copyImageSetRequest = new AwsHealthImaging.CopyImageSetRequest(); // {CopyImageSetRequest} 
var opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // {String} 
  'xAmzDate': "xAmzDate_example", // {String} 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // {String} 
  'xAmzCredential': "xAmzCredential_example", // {String} 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // {String} 
  'xAmzSignature': "xAmzSignature_example", // {String} 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // {String} 
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.copyImageSet(datastoreId, sourceImageSetId, copyImageSetRequest, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *http://medical-imaging.us-east-1.amazonaws.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AwsHealthImaging.DefaultApi* | [**copyImageSet**](docs/DefaultApi.md#copyImageSet) | **POST** /datastore/{datastoreId}/imageSet/{sourceImageSetId}/copyImageSet | 
*AwsHealthImaging.DefaultApi* | [**createDatastore**](docs/DefaultApi.md#createDatastore) | **POST** /datastore | 
*AwsHealthImaging.DefaultApi* | [**deleteDatastore**](docs/DefaultApi.md#deleteDatastore) | **DELETE** /datastore/{datastoreId} | 
*AwsHealthImaging.DefaultApi* | [**deleteImageSet**](docs/DefaultApi.md#deleteImageSet) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/deleteImageSet | 
*AwsHealthImaging.DefaultApi* | [**getDICOMImportJob**](docs/DefaultApi.md#getDICOMImportJob) | **GET** /getDICOMImportJob/datastore/{datastoreId}/job/{jobId} | 
*AwsHealthImaging.DefaultApi* | [**getDatastore**](docs/DefaultApi.md#getDatastore) | **GET** /datastore/{datastoreId} | 
*AwsHealthImaging.DefaultApi* | [**getImageFrame**](docs/DefaultApi.md#getImageFrame) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/getImageFrame | 
*AwsHealthImaging.DefaultApi* | [**getImageSet**](docs/DefaultApi.md#getImageSet) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/getImageSet | 
*AwsHealthImaging.DefaultApi* | [**getImageSetMetadata**](docs/DefaultApi.md#getImageSetMetadata) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/getImageSetMetadata | 
*AwsHealthImaging.DefaultApi* | [**listDICOMImportJobs**](docs/DefaultApi.md#listDICOMImportJobs) | **GET** /listDICOMImportJobs/datastore/{datastoreId} | 
*AwsHealthImaging.DefaultApi* | [**listDatastores**](docs/DefaultApi.md#listDatastores) | **GET** /datastore | 
*AwsHealthImaging.DefaultApi* | [**listImageSetVersions**](docs/DefaultApi.md#listImageSetVersions) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/listImageSetVersions | 
*AwsHealthImaging.DefaultApi* | [**listTagsForResource**](docs/DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
*AwsHealthImaging.DefaultApi* | [**searchImageSets**](docs/DefaultApi.md#searchImageSets) | **POST** /datastore/{datastoreId}/searchImageSets | 
*AwsHealthImaging.DefaultApi* | [**startDICOMImportJob**](docs/DefaultApi.md#startDICOMImportJob) | **POST** /startDICOMImportJob/datastore/{datastoreId} | 
*AwsHealthImaging.DefaultApi* | [**tagResource**](docs/DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
*AwsHealthImaging.DefaultApi* | [**untagResource**](docs/DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
*AwsHealthImaging.DefaultApi* | [**updateImageSetMetadata**](docs/DefaultApi.md#updateImageSetMetadata) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/updateImageSetMetadata#latestVersion | 


## Documentation for Models

 - [AwsHealthImaging.CopyDestinationImageSet](docs/CopyDestinationImageSet.md)
 - [AwsHealthImaging.CopyDestinationImageSetProperties](docs/CopyDestinationImageSetProperties.md)
 - [AwsHealthImaging.CopyImageSetInformation](docs/CopyImageSetInformation.md)
 - [AwsHealthImaging.CopyImageSetRequest](docs/CopyImageSetRequest.md)
 - [AwsHealthImaging.CopyImageSetRequestCopyImageSetInformation](docs/CopyImageSetRequestCopyImageSetInformation.md)
 - [AwsHealthImaging.CopyImageSetRequestCopyImageSetInformationDestinationImageSet](docs/CopyImageSetRequestCopyImageSetInformationDestinationImageSet.md)
 - [AwsHealthImaging.CopyImageSetRequestCopyImageSetInformationSourceImageSet](docs/CopyImageSetRequestCopyImageSetInformationSourceImageSet.md)
 - [AwsHealthImaging.CopyImageSetResponse](docs/CopyImageSetResponse.md)
 - [AwsHealthImaging.CopyImageSetResponseDestinationImageSetProperties](docs/CopyImageSetResponseDestinationImageSetProperties.md)
 - [AwsHealthImaging.CopyImageSetResponseSourceImageSetProperties](docs/CopyImageSetResponseSourceImageSetProperties.md)
 - [AwsHealthImaging.CopySourceImageSetInformation](docs/CopySourceImageSetInformation.md)
 - [AwsHealthImaging.CopySourceImageSetProperties](docs/CopySourceImageSetProperties.md)
 - [AwsHealthImaging.CreateDatastoreRequest](docs/CreateDatastoreRequest.md)
 - [AwsHealthImaging.CreateDatastoreResponse](docs/CreateDatastoreResponse.md)
 - [AwsHealthImaging.DICOMImportJobProperties](docs/DICOMImportJobProperties.md)
 - [AwsHealthImaging.DICOMImportJobSummary](docs/DICOMImportJobSummary.md)
 - [AwsHealthImaging.DICOMStudyDateAndTime](docs/DICOMStudyDateAndTime.md)
 - [AwsHealthImaging.DICOMTags](docs/DICOMTags.md)
 - [AwsHealthImaging.DICOMUpdates](docs/DICOMUpdates.md)
 - [AwsHealthImaging.DatastoreProperties](docs/DatastoreProperties.md)
 - [AwsHealthImaging.DatastoreStatus](docs/DatastoreStatus.md)
 - [AwsHealthImaging.DatastoreSummary](docs/DatastoreSummary.md)
 - [AwsHealthImaging.DeleteDatastoreResponse](docs/DeleteDatastoreResponse.md)
 - [AwsHealthImaging.DeleteImageSetResponse](docs/DeleteImageSetResponse.md)
 - [AwsHealthImaging.GetDICOMImportJobResponse](docs/GetDICOMImportJobResponse.md)
 - [AwsHealthImaging.GetDICOMImportJobResponseJobProperties](docs/GetDICOMImportJobResponseJobProperties.md)
 - [AwsHealthImaging.GetDatastoreResponse](docs/GetDatastoreResponse.md)
 - [AwsHealthImaging.GetDatastoreResponseDatastoreProperties](docs/GetDatastoreResponseDatastoreProperties.md)
 - [AwsHealthImaging.GetImageFrameRequest](docs/GetImageFrameRequest.md)
 - [AwsHealthImaging.GetImageFrameRequestImageFrameInformation](docs/GetImageFrameRequestImageFrameInformation.md)
 - [AwsHealthImaging.GetImageFrameResponse](docs/GetImageFrameResponse.md)
 - [AwsHealthImaging.GetImageSetMetadataResponse](docs/GetImageSetMetadataResponse.md)
 - [AwsHealthImaging.GetImageSetResponse](docs/GetImageSetResponse.md)
 - [AwsHealthImaging.ImageFrameInformation](docs/ImageFrameInformation.md)
 - [AwsHealthImaging.ImageSetProperties](docs/ImageSetProperties.md)
 - [AwsHealthImaging.ImageSetState](docs/ImageSetState.md)
 - [AwsHealthImaging.ImageSetWorkflowStatus](docs/ImageSetWorkflowStatus.md)
 - [AwsHealthImaging.ImageSetsMetadataSummary](docs/ImageSetsMetadataSummary.md)
 - [AwsHealthImaging.ImageSetsMetadataSummaryDICOMTags](docs/ImageSetsMetadataSummaryDICOMTags.md)
 - [AwsHealthImaging.JobStatus](docs/JobStatus.md)
 - [AwsHealthImaging.ListDICOMImportJobsResponse](docs/ListDICOMImportJobsResponse.md)
 - [AwsHealthImaging.ListDatastoresResponse](docs/ListDatastoresResponse.md)
 - [AwsHealthImaging.ListImageSetVersionsResponse](docs/ListImageSetVersionsResponse.md)
 - [AwsHealthImaging.ListTagsForResourceResponse](docs/ListTagsForResourceResponse.md)
 - [AwsHealthImaging.MetadataUpdates](docs/MetadataUpdates.md)
 - [AwsHealthImaging.Operator](docs/Operator.md)
 - [AwsHealthImaging.SearchByAttributeValue](docs/SearchByAttributeValue.md)
 - [AwsHealthImaging.SearchByAttributeValueDICOMStudyDateAndTime](docs/SearchByAttributeValueDICOMStudyDateAndTime.md)
 - [AwsHealthImaging.SearchCriteria](docs/SearchCriteria.md)
 - [AwsHealthImaging.SearchFilter](docs/SearchFilter.md)
 - [AwsHealthImaging.SearchImageSetsRequest](docs/SearchImageSetsRequest.md)
 - [AwsHealthImaging.SearchImageSetsRequestSearchCriteria](docs/SearchImageSetsRequestSearchCriteria.md)
 - [AwsHealthImaging.SearchImageSetsResponse](docs/SearchImageSetsResponse.md)
 - [AwsHealthImaging.StartDICOMImportJobRequest](docs/StartDICOMImportJobRequest.md)
 - [AwsHealthImaging.StartDICOMImportJobResponse](docs/StartDICOMImportJobResponse.md)
 - [AwsHealthImaging.TagResourceRequest](docs/TagResourceRequest.md)
 - [AwsHealthImaging.UpdateImageSetMetadataRequest](docs/UpdateImageSetMetadataRequest.md)
 - [AwsHealthImaging.UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdates](docs/UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdates.md)
 - [AwsHealthImaging.UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdatesDICOMUpdates](docs/UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdatesDICOMUpdates.md)
 - [AwsHealthImaging.UpdateImageSetMetadataResponse](docs/UpdateImageSetMetadataResponse.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### hmac


- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

