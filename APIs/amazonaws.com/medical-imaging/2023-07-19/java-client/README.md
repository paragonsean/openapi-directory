# openapi-java-client

AWS Health Imaging
- API version: 2023-07-19
  - Build date: 2024-10-12T12:28:55.616958-04:00[America/New_York]
  - Generator version: 7.9.0

<p>This is the <i>AWS HealthImaging API Reference</i>. AWS HealthImaging is an AWS service for storing, accessing, and analyzing medical images. For an introduction to the service, see the <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide\"> <i>AWS HealthImaging Developer Guide</i> </a>.</p> <note> <p>We recommend using one of the AWS Software Development Kits (SDKs) for your programming language, as they take care of request authentication, serialization, and connection management. For more information, see <a href=\"http://aws.amazon.com/developer/tools\">Tools to build on AWS</a>.</p> <p>For information about using AWS HealthImaging API actions in one of the language-specific AWS SDKs, refer to the <i>See Also</i> link at the end of each section that describes an API action or data type.</p> </note> <p>The following sections list AWS HealthImaging API actions categorized according to functionality. Links are provided to actions within this Reference, along with links back to corresponding sections in the <i>AWS HealthImaging Developer Guide</i> so you can view console procedures and CLI/SDK code examples.</p> <p class=\"title\"> <b>Data store actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_CreateDatastore.html\">CreateDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/create-data-store.html\">Creating a data store</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetDatastore.html\">GetDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-data-store.html\">Getting data store properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListDatastores.html\">ListDatastores</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-data-stores.html\">Listing data stores</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_DeleteDatastore.html\">DeleteDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/delete-data-store.html\">Deleting a data store</a>.</p> </li> </ul> <p class=\"title\"> <b>Import job actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_StartDICOMImportJob.html\">StartDICOMImportJob</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/start-dicom-import-job.html\">Starting an import job</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetDICOMImportJob.html\">GetDICOMImportJob</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-dicom-import-job.html\">Getting import job properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListDICOMImportJobs.html\">ListDICOMImportJobs</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-dicom-import-jobs.html\">Listing import jobs</a>.</p> </li> </ul> <p class=\"title\"> <b>Image set access actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_SearchImageSets.html\">SearchImageSets</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/search-image-sets.html\">Searching image sets</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageSet.html\">GetImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-set-properties.html\">Getting image set properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageSetMetadata.html\">GetImageSetMetadata</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-set-metadata.html\">Getting image set metadata</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageFrame.html\">GetImageFrame</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-frame.html\">Getting image set pixel data</a>.</p> </li> </ul> <p class=\"title\"> <b>Image set modification actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListImageSetVersions.html\">ListImageSetVersions</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-image-set-versions.html\">Listing image set versions</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_UpdateImageSetMetadata.html\">UpdateImageSetMetadata</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/update-image-set-metadata.html\">Updating image set metadata</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_CopyImageSet.html\">CopyImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/copy-image-set.html\">Copying an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_DeleteImageSet.html\">DeleteImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/delete-image-set.html\">Deleting an image set</a>.</p> </li> </ul> <p class=\"title\"> <b>Tagging actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_TagResource.html\">TagResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListTagsForResource.html\">ListTagsForResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_UntagResource.html\">UntagResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> </ul>

  For more information, please visit [https://github.com/mermade/aws2openapi](https://github.com/mermade/aws2openapi)

*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>2023-07-19</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:2023-07-19"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-2023-07-19.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://medical-imaging.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String datastoreId = "datastoreId_example"; // String | The data store identifier.
    String sourceImageSetId = "sourceImageSetId_example"; // String | The source image set identifier.
    CopyImageSetRequest copyImageSetRequest = new CopyImageSetRequest(); // CopyImageSetRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CopyImageSetResponse result = apiInstance.copyImageSet(datastoreId, sourceImageSetId, copyImageSetRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#copyImageSet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *http://medical-imaging.us-east-1.amazonaws.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**copyImageSet**](docs/DefaultApi.md#copyImageSet) | **POST** /datastore/{datastoreId}/imageSet/{sourceImageSetId}/copyImageSet | 
*DefaultApi* | [**createDatastore**](docs/DefaultApi.md#createDatastore) | **POST** /datastore | 
*DefaultApi* | [**deleteDatastore**](docs/DefaultApi.md#deleteDatastore) | **DELETE** /datastore/{datastoreId} | 
*DefaultApi* | [**deleteImageSet**](docs/DefaultApi.md#deleteImageSet) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/deleteImageSet | 
*DefaultApi* | [**getDICOMImportJob**](docs/DefaultApi.md#getDICOMImportJob) | **GET** /getDICOMImportJob/datastore/{datastoreId}/job/{jobId} | 
*DefaultApi* | [**getDatastore**](docs/DefaultApi.md#getDatastore) | **GET** /datastore/{datastoreId} | 
*DefaultApi* | [**getImageFrame**](docs/DefaultApi.md#getImageFrame) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/getImageFrame | 
*DefaultApi* | [**getImageSet**](docs/DefaultApi.md#getImageSet) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/getImageSet | 
*DefaultApi* | [**getImageSetMetadata**](docs/DefaultApi.md#getImageSetMetadata) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/getImageSetMetadata | 
*DefaultApi* | [**listDICOMImportJobs**](docs/DefaultApi.md#listDICOMImportJobs) | **GET** /listDICOMImportJobs/datastore/{datastoreId} | 
*DefaultApi* | [**listDatastores**](docs/DefaultApi.md#listDatastores) | **GET** /datastore | 
*DefaultApi* | [**listImageSetVersions**](docs/DefaultApi.md#listImageSetVersions) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/listImageSetVersions | 
*DefaultApi* | [**listTagsForResource**](docs/DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
*DefaultApi* | [**searchImageSets**](docs/DefaultApi.md#searchImageSets) | **POST** /datastore/{datastoreId}/searchImageSets | 
*DefaultApi* | [**startDICOMImportJob**](docs/DefaultApi.md#startDICOMImportJob) | **POST** /startDICOMImportJob/datastore/{datastoreId} | 
*DefaultApi* | [**tagResource**](docs/DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
*DefaultApi* | [**untagResource**](docs/DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
*DefaultApi* | [**updateImageSetMetadata**](docs/DefaultApi.md#updateImageSetMetadata) | **POST** /datastore/{datastoreId}/imageSet/{imageSetId}/updateImageSetMetadata#latestVersion | 


## Documentation for Models

 - [CopyDestinationImageSet](docs/CopyDestinationImageSet.md)
 - [CopyDestinationImageSetProperties](docs/CopyDestinationImageSetProperties.md)
 - [CopyImageSetInformation](docs/CopyImageSetInformation.md)
 - [CopyImageSetRequest](docs/CopyImageSetRequest.md)
 - [CopyImageSetRequestCopyImageSetInformation](docs/CopyImageSetRequestCopyImageSetInformation.md)
 - [CopyImageSetRequestCopyImageSetInformationDestinationImageSet](docs/CopyImageSetRequestCopyImageSetInformationDestinationImageSet.md)
 - [CopyImageSetRequestCopyImageSetInformationSourceImageSet](docs/CopyImageSetRequestCopyImageSetInformationSourceImageSet.md)
 - [CopyImageSetResponse](docs/CopyImageSetResponse.md)
 - [CopyImageSetResponseDestinationImageSetProperties](docs/CopyImageSetResponseDestinationImageSetProperties.md)
 - [CopyImageSetResponseSourceImageSetProperties](docs/CopyImageSetResponseSourceImageSetProperties.md)
 - [CopySourceImageSetInformation](docs/CopySourceImageSetInformation.md)
 - [CopySourceImageSetProperties](docs/CopySourceImageSetProperties.md)
 - [CreateDatastoreRequest](docs/CreateDatastoreRequest.md)
 - [CreateDatastoreResponse](docs/CreateDatastoreResponse.md)
 - [DICOMImportJobProperties](docs/DICOMImportJobProperties.md)
 - [DICOMImportJobSummary](docs/DICOMImportJobSummary.md)
 - [DICOMStudyDateAndTime](docs/DICOMStudyDateAndTime.md)
 - [DICOMTags](docs/DICOMTags.md)
 - [DICOMUpdates](docs/DICOMUpdates.md)
 - [DatastoreProperties](docs/DatastoreProperties.md)
 - [DatastoreStatus](docs/DatastoreStatus.md)
 - [DatastoreSummary](docs/DatastoreSummary.md)
 - [DeleteDatastoreResponse](docs/DeleteDatastoreResponse.md)
 - [DeleteImageSetResponse](docs/DeleteImageSetResponse.md)
 - [GetDICOMImportJobResponse](docs/GetDICOMImportJobResponse.md)
 - [GetDICOMImportJobResponseJobProperties](docs/GetDICOMImportJobResponseJobProperties.md)
 - [GetDatastoreResponse](docs/GetDatastoreResponse.md)
 - [GetDatastoreResponseDatastoreProperties](docs/GetDatastoreResponseDatastoreProperties.md)
 - [GetImageFrameRequest](docs/GetImageFrameRequest.md)
 - [GetImageFrameRequestImageFrameInformation](docs/GetImageFrameRequestImageFrameInformation.md)
 - [GetImageFrameResponse](docs/GetImageFrameResponse.md)
 - [GetImageSetMetadataResponse](docs/GetImageSetMetadataResponse.md)
 - [GetImageSetResponse](docs/GetImageSetResponse.md)
 - [ImageFrameInformation](docs/ImageFrameInformation.md)
 - [ImageSetProperties](docs/ImageSetProperties.md)
 - [ImageSetState](docs/ImageSetState.md)
 - [ImageSetWorkflowStatus](docs/ImageSetWorkflowStatus.md)
 - [ImageSetsMetadataSummary](docs/ImageSetsMetadataSummary.md)
 - [ImageSetsMetadataSummaryDICOMTags](docs/ImageSetsMetadataSummaryDICOMTags.md)
 - [JobStatus](docs/JobStatus.md)
 - [ListDICOMImportJobsResponse](docs/ListDICOMImportJobsResponse.md)
 - [ListDatastoresResponse](docs/ListDatastoresResponse.md)
 - [ListImageSetVersionsResponse](docs/ListImageSetVersionsResponse.md)
 - [ListTagsForResourceResponse](docs/ListTagsForResourceResponse.md)
 - [MetadataUpdates](docs/MetadataUpdates.md)
 - [Operator](docs/Operator.md)
 - [SearchByAttributeValue](docs/SearchByAttributeValue.md)
 - [SearchByAttributeValueDICOMStudyDateAndTime](docs/SearchByAttributeValueDICOMStudyDateAndTime.md)
 - [SearchCriteria](docs/SearchCriteria.md)
 - [SearchFilter](docs/SearchFilter.md)
 - [SearchImageSetsRequest](docs/SearchImageSetsRequest.md)
 - [SearchImageSetsRequestSearchCriteria](docs/SearchImageSetsRequestSearchCriteria.md)
 - [SearchImageSetsResponse](docs/SearchImageSetsResponse.md)
 - [StartDICOMImportJobRequest](docs/StartDICOMImportJobRequest.md)
 - [StartDICOMImportJobResponse](docs/StartDICOMImportJobResponse.md)
 - [TagResourceRequest](docs/TagResourceRequest.md)
 - [UpdateImageSetMetadataRequest](docs/UpdateImageSetMetadataRequest.md)
 - [UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdates](docs/UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdates.md)
 - [UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdatesDICOMUpdates](docs/UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdatesDICOMUpdates.md)
 - [UpdateImageSetMetadataResponse](docs/UpdateImageSetMetadataResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="hmac"></a>
### hmac

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

mike.ralphson@gmail.com

