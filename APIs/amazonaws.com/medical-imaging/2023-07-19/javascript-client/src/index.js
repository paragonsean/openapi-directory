/**
 * AWS Health Imaging
 * <p>This is the <i>AWS HealthImaging API Reference</i>. AWS HealthImaging is an AWS service for storing, accessing, and analyzing medical images. For an introduction to the service, see the <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide\"> <i>AWS HealthImaging Developer Guide</i> </a>.</p> <note> <p>We recommend using one of the AWS Software Development Kits (SDKs) for your programming language, as they take care of request authentication, serialization, and connection management. For more information, see <a href=\"http://aws.amazon.com/developer/tools\">Tools to build on AWS</a>.</p> <p>For information about using AWS HealthImaging API actions in one of the language-specific AWS SDKs, refer to the <i>See Also</i> link at the end of each section that describes an API action or data type.</p> </note> <p>The following sections list AWS HealthImaging API actions categorized according to functionality. Links are provided to actions within this Reference, along with links back to corresponding sections in the <i>AWS HealthImaging Developer Guide</i> so you can view console procedures and CLI/SDK code examples.</p> <p class=\"title\"> <b>Data store actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_CreateDatastore.html\">CreateDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/create-data-store.html\">Creating a data store</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetDatastore.html\">GetDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-data-store.html\">Getting data store properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListDatastores.html\">ListDatastores</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-data-stores.html\">Listing data stores</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_DeleteDatastore.html\">DeleteDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/delete-data-store.html\">Deleting a data store</a>.</p> </li> </ul> <p class=\"title\"> <b>Import job actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_StartDICOMImportJob.html\">StartDICOMImportJob</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/start-dicom-import-job.html\">Starting an import job</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetDICOMImportJob.html\">GetDICOMImportJob</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-dicom-import-job.html\">Getting import job properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListDICOMImportJobs.html\">ListDICOMImportJobs</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-dicom-import-jobs.html\">Listing import jobs</a>.</p> </li> </ul> <p class=\"title\"> <b>Image set access actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_SearchImageSets.html\">SearchImageSets</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/search-image-sets.html\">Searching image sets</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageSet.html\">GetImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-set-properties.html\">Getting image set properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageSetMetadata.html\">GetImageSetMetadata</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-set-metadata.html\">Getting image set metadata</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageFrame.html\">GetImageFrame</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-frame.html\">Getting image set pixel data</a>.</p> </li> </ul> <p class=\"title\"> <b>Image set modification actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListImageSetVersions.html\">ListImageSetVersions</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-image-set-versions.html\">Listing image set versions</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_UpdateImageSetMetadata.html\">UpdateImageSetMetadata</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/update-image-set-metadata.html\">Updating image set metadata</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_CopyImageSet.html\">CopyImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/copy-image-set.html\">Copying an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_DeleteImageSet.html\">DeleteImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/delete-image-set.html\">Deleting an image set</a>.</p> </li> </ul> <p class=\"title\"> <b>Tagging actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_TagResource.html\">TagResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListTagsForResource.html\">ListTagsForResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_UntagResource.html\">UntagResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2023-07-19
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import CopyDestinationImageSet from './model/CopyDestinationImageSet';
import CopyDestinationImageSetProperties from './model/CopyDestinationImageSetProperties';
import CopyImageSetInformation from './model/CopyImageSetInformation';
import CopyImageSetRequest from './model/CopyImageSetRequest';
import CopyImageSetRequestCopyImageSetInformation from './model/CopyImageSetRequestCopyImageSetInformation';
import CopyImageSetRequestCopyImageSetInformationDestinationImageSet from './model/CopyImageSetRequestCopyImageSetInformationDestinationImageSet';
import CopyImageSetRequestCopyImageSetInformationSourceImageSet from './model/CopyImageSetRequestCopyImageSetInformationSourceImageSet';
import CopyImageSetResponse from './model/CopyImageSetResponse';
import CopyImageSetResponseDestinationImageSetProperties from './model/CopyImageSetResponseDestinationImageSetProperties';
import CopyImageSetResponseSourceImageSetProperties from './model/CopyImageSetResponseSourceImageSetProperties';
import CopySourceImageSetInformation from './model/CopySourceImageSetInformation';
import CopySourceImageSetProperties from './model/CopySourceImageSetProperties';
import CreateDatastoreRequest from './model/CreateDatastoreRequest';
import CreateDatastoreResponse from './model/CreateDatastoreResponse';
import DICOMImportJobProperties from './model/DICOMImportJobProperties';
import DICOMImportJobSummary from './model/DICOMImportJobSummary';
import DICOMStudyDateAndTime from './model/DICOMStudyDateAndTime';
import DICOMTags from './model/DICOMTags';
import DICOMUpdates from './model/DICOMUpdates';
import DatastoreProperties from './model/DatastoreProperties';
import DatastoreStatus from './model/DatastoreStatus';
import DatastoreSummary from './model/DatastoreSummary';
import DeleteDatastoreResponse from './model/DeleteDatastoreResponse';
import DeleteImageSetResponse from './model/DeleteImageSetResponse';
import GetDICOMImportJobResponse from './model/GetDICOMImportJobResponse';
import GetDICOMImportJobResponseJobProperties from './model/GetDICOMImportJobResponseJobProperties';
import GetDatastoreResponse from './model/GetDatastoreResponse';
import GetDatastoreResponseDatastoreProperties from './model/GetDatastoreResponseDatastoreProperties';
import GetImageFrameRequest from './model/GetImageFrameRequest';
import GetImageFrameRequestImageFrameInformation from './model/GetImageFrameRequestImageFrameInformation';
import GetImageFrameResponse from './model/GetImageFrameResponse';
import GetImageSetMetadataResponse from './model/GetImageSetMetadataResponse';
import GetImageSetResponse from './model/GetImageSetResponse';
import ImageFrameInformation from './model/ImageFrameInformation';
import ImageSetProperties from './model/ImageSetProperties';
import ImageSetState from './model/ImageSetState';
import ImageSetWorkflowStatus from './model/ImageSetWorkflowStatus';
import ImageSetsMetadataSummary from './model/ImageSetsMetadataSummary';
import ImageSetsMetadataSummaryDICOMTags from './model/ImageSetsMetadataSummaryDICOMTags';
import JobStatus from './model/JobStatus';
import ListDICOMImportJobsResponse from './model/ListDICOMImportJobsResponse';
import ListDatastoresResponse from './model/ListDatastoresResponse';
import ListImageSetVersionsResponse from './model/ListImageSetVersionsResponse';
import ListTagsForResourceResponse from './model/ListTagsForResourceResponse';
import MetadataUpdates from './model/MetadataUpdates';
import Operator from './model/Operator';
import SearchByAttributeValue from './model/SearchByAttributeValue';
import SearchByAttributeValueDICOMStudyDateAndTime from './model/SearchByAttributeValueDICOMStudyDateAndTime';
import SearchCriteria from './model/SearchCriteria';
import SearchFilter from './model/SearchFilter';
import SearchImageSetsRequest from './model/SearchImageSetsRequest';
import SearchImageSetsRequestSearchCriteria from './model/SearchImageSetsRequestSearchCriteria';
import SearchImageSetsResponse from './model/SearchImageSetsResponse';
import StartDICOMImportJobRequest from './model/StartDICOMImportJobRequest';
import StartDICOMImportJobResponse from './model/StartDICOMImportJobResponse';
import TagResourceRequest from './model/TagResourceRequest';
import UpdateImageSetMetadataRequest from './model/UpdateImageSetMetadataRequest';
import UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdates from './model/UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdates';
import UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdatesDICOMUpdates from './model/UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdatesDICOMUpdates';
import UpdateImageSetMetadataResponse from './model/UpdateImageSetMetadataResponse';
import DefaultApi from './api/DefaultApi';


/**
* &lt;p&gt;This is the &lt;i&gt;AWS HealthImaging API Reference&lt;/i&gt;. AWS HealthImaging is an AWS service for storing, accessing, and analyzing medical images. For an introduction to the service, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide\&quot;&gt; &lt;i&gt;AWS HealthImaging Developer Guide&lt;/i&gt; &lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;We recommend using one of the AWS Software Development Kits (SDKs) for your programming language, as they take care of request authentication, serialization, and connection management. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/developer/tools\&quot;&gt;Tools to build on AWS&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For information about using AWS HealthImaging API actions in one of the language-specific AWS SDKs, refer to the &lt;i&gt;See Also&lt;/i&gt; link at the end of each section that describes an API action or data type.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The following sections list AWS HealthImaging API actions categorized according to functionality. Links are provided to actions within this Reference, along with links back to corresponding sections in the &lt;i&gt;AWS HealthImaging Developer Guide&lt;/i&gt; so you can view console procedures and CLI/SDK code examples.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Data store actions&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_CreateDatastore.html\&quot;&gt;CreateDatastore&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/create-data-store.html\&quot;&gt;Creating a data store&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetDatastore.html\&quot;&gt;GetDatastore&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-data-store.html\&quot;&gt;Getting data store properties&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListDatastores.html\&quot;&gt;ListDatastores&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-data-stores.html\&quot;&gt;Listing data stores&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_DeleteDatastore.html\&quot;&gt;DeleteDatastore&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/delete-data-store.html\&quot;&gt;Deleting a data store&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Import job actions&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_StartDICOMImportJob.html\&quot;&gt;StartDICOMImportJob&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/start-dicom-import-job.html\&quot;&gt;Starting an import job&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetDICOMImportJob.html\&quot;&gt;GetDICOMImportJob&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-dicom-import-job.html\&quot;&gt;Getting import job properties&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListDICOMImportJobs.html\&quot;&gt;ListDICOMImportJobs&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-dicom-import-jobs.html\&quot;&gt;Listing import jobs&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Image set access actions&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_SearchImageSets.html\&quot;&gt;SearchImageSets&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/search-image-sets.html\&quot;&gt;Searching image sets&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageSet.html\&quot;&gt;GetImageSet&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-set-properties.html\&quot;&gt;Getting image set properties&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageSetMetadata.html\&quot;&gt;GetImageSetMetadata&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-set-metadata.html\&quot;&gt;Getting image set metadata&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageFrame.html\&quot;&gt;GetImageFrame&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-frame.html\&quot;&gt;Getting image set pixel data&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Image set modification actions&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListImageSetVersions.html\&quot;&gt;ListImageSetVersions&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-image-set-versions.html\&quot;&gt;Listing image set versions&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_UpdateImageSetMetadata.html\&quot;&gt;UpdateImageSetMetadata&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/update-image-set-metadata.html\&quot;&gt;Updating image set metadata&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_CopyImageSet.html\&quot;&gt;CopyImageSet&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/copy-image-set.html\&quot;&gt;Copying an image set&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_DeleteImageSet.html\&quot;&gt;DeleteImageSet&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/delete-image-set.html\&quot;&gt;Deleting an image set&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Tagging actions&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\&quot;&gt;Tagging a data store&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\&quot;&gt;Tagging an image set&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListTagsForResource.html\&quot;&gt;ListTagsForResource&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\&quot;&gt;Tagging a data store&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\&quot;&gt;Tagging an image set&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_UntagResource.html\&quot;&gt;UntagResource&lt;/a&gt; – See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\&quot;&gt;Tagging a data store&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\&quot;&gt;Tagging an image set&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var AwsHealthImaging = require('index'); // See note below*.
* var xxxSvc = new AwsHealthImaging.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new AwsHealthImaging.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new AwsHealthImaging.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new AwsHealthImaging.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2023-07-19
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The CopyDestinationImageSet model constructor.
     * @property {module:model/CopyDestinationImageSet}
     */
    CopyDestinationImageSet,

    /**
     * The CopyDestinationImageSetProperties model constructor.
     * @property {module:model/CopyDestinationImageSetProperties}
     */
    CopyDestinationImageSetProperties,

    /**
     * The CopyImageSetInformation model constructor.
     * @property {module:model/CopyImageSetInformation}
     */
    CopyImageSetInformation,

    /**
     * The CopyImageSetRequest model constructor.
     * @property {module:model/CopyImageSetRequest}
     */
    CopyImageSetRequest,

    /**
     * The CopyImageSetRequestCopyImageSetInformation model constructor.
     * @property {module:model/CopyImageSetRequestCopyImageSetInformation}
     */
    CopyImageSetRequestCopyImageSetInformation,

    /**
     * The CopyImageSetRequestCopyImageSetInformationDestinationImageSet model constructor.
     * @property {module:model/CopyImageSetRequestCopyImageSetInformationDestinationImageSet}
     */
    CopyImageSetRequestCopyImageSetInformationDestinationImageSet,

    /**
     * The CopyImageSetRequestCopyImageSetInformationSourceImageSet model constructor.
     * @property {module:model/CopyImageSetRequestCopyImageSetInformationSourceImageSet}
     */
    CopyImageSetRequestCopyImageSetInformationSourceImageSet,

    /**
     * The CopyImageSetResponse model constructor.
     * @property {module:model/CopyImageSetResponse}
     */
    CopyImageSetResponse,

    /**
     * The CopyImageSetResponseDestinationImageSetProperties model constructor.
     * @property {module:model/CopyImageSetResponseDestinationImageSetProperties}
     */
    CopyImageSetResponseDestinationImageSetProperties,

    /**
     * The CopyImageSetResponseSourceImageSetProperties model constructor.
     * @property {module:model/CopyImageSetResponseSourceImageSetProperties}
     */
    CopyImageSetResponseSourceImageSetProperties,

    /**
     * The CopySourceImageSetInformation model constructor.
     * @property {module:model/CopySourceImageSetInformation}
     */
    CopySourceImageSetInformation,

    /**
     * The CopySourceImageSetProperties model constructor.
     * @property {module:model/CopySourceImageSetProperties}
     */
    CopySourceImageSetProperties,

    /**
     * The CreateDatastoreRequest model constructor.
     * @property {module:model/CreateDatastoreRequest}
     */
    CreateDatastoreRequest,

    /**
     * The CreateDatastoreResponse model constructor.
     * @property {module:model/CreateDatastoreResponse}
     */
    CreateDatastoreResponse,

    /**
     * The DICOMImportJobProperties model constructor.
     * @property {module:model/DICOMImportJobProperties}
     */
    DICOMImportJobProperties,

    /**
     * The DICOMImportJobSummary model constructor.
     * @property {module:model/DICOMImportJobSummary}
     */
    DICOMImportJobSummary,

    /**
     * The DICOMStudyDateAndTime model constructor.
     * @property {module:model/DICOMStudyDateAndTime}
     */
    DICOMStudyDateAndTime,

    /**
     * The DICOMTags model constructor.
     * @property {module:model/DICOMTags}
     */
    DICOMTags,

    /**
     * The DICOMUpdates model constructor.
     * @property {module:model/DICOMUpdates}
     */
    DICOMUpdates,

    /**
     * The DatastoreProperties model constructor.
     * @property {module:model/DatastoreProperties}
     */
    DatastoreProperties,

    /**
     * The DatastoreStatus model constructor.
     * @property {module:model/DatastoreStatus}
     */
    DatastoreStatus,

    /**
     * The DatastoreSummary model constructor.
     * @property {module:model/DatastoreSummary}
     */
    DatastoreSummary,

    /**
     * The DeleteDatastoreResponse model constructor.
     * @property {module:model/DeleteDatastoreResponse}
     */
    DeleteDatastoreResponse,

    /**
     * The DeleteImageSetResponse model constructor.
     * @property {module:model/DeleteImageSetResponse}
     */
    DeleteImageSetResponse,

    /**
     * The GetDICOMImportJobResponse model constructor.
     * @property {module:model/GetDICOMImportJobResponse}
     */
    GetDICOMImportJobResponse,

    /**
     * The GetDICOMImportJobResponseJobProperties model constructor.
     * @property {module:model/GetDICOMImportJobResponseJobProperties}
     */
    GetDICOMImportJobResponseJobProperties,

    /**
     * The GetDatastoreResponse model constructor.
     * @property {module:model/GetDatastoreResponse}
     */
    GetDatastoreResponse,

    /**
     * The GetDatastoreResponseDatastoreProperties model constructor.
     * @property {module:model/GetDatastoreResponseDatastoreProperties}
     */
    GetDatastoreResponseDatastoreProperties,

    /**
     * The GetImageFrameRequest model constructor.
     * @property {module:model/GetImageFrameRequest}
     */
    GetImageFrameRequest,

    /**
     * The GetImageFrameRequestImageFrameInformation model constructor.
     * @property {module:model/GetImageFrameRequestImageFrameInformation}
     */
    GetImageFrameRequestImageFrameInformation,

    /**
     * The GetImageFrameResponse model constructor.
     * @property {module:model/GetImageFrameResponse}
     */
    GetImageFrameResponse,

    /**
     * The GetImageSetMetadataResponse model constructor.
     * @property {module:model/GetImageSetMetadataResponse}
     */
    GetImageSetMetadataResponse,

    /**
     * The GetImageSetResponse model constructor.
     * @property {module:model/GetImageSetResponse}
     */
    GetImageSetResponse,

    /**
     * The ImageFrameInformation model constructor.
     * @property {module:model/ImageFrameInformation}
     */
    ImageFrameInformation,

    /**
     * The ImageSetProperties model constructor.
     * @property {module:model/ImageSetProperties}
     */
    ImageSetProperties,

    /**
     * The ImageSetState model constructor.
     * @property {module:model/ImageSetState}
     */
    ImageSetState,

    /**
     * The ImageSetWorkflowStatus model constructor.
     * @property {module:model/ImageSetWorkflowStatus}
     */
    ImageSetWorkflowStatus,

    /**
     * The ImageSetsMetadataSummary model constructor.
     * @property {module:model/ImageSetsMetadataSummary}
     */
    ImageSetsMetadataSummary,

    /**
     * The ImageSetsMetadataSummaryDICOMTags model constructor.
     * @property {module:model/ImageSetsMetadataSummaryDICOMTags}
     */
    ImageSetsMetadataSummaryDICOMTags,

    /**
     * The JobStatus model constructor.
     * @property {module:model/JobStatus}
     */
    JobStatus,

    /**
     * The ListDICOMImportJobsResponse model constructor.
     * @property {module:model/ListDICOMImportJobsResponse}
     */
    ListDICOMImportJobsResponse,

    /**
     * The ListDatastoresResponse model constructor.
     * @property {module:model/ListDatastoresResponse}
     */
    ListDatastoresResponse,

    /**
     * The ListImageSetVersionsResponse model constructor.
     * @property {module:model/ListImageSetVersionsResponse}
     */
    ListImageSetVersionsResponse,

    /**
     * The ListTagsForResourceResponse model constructor.
     * @property {module:model/ListTagsForResourceResponse}
     */
    ListTagsForResourceResponse,

    /**
     * The MetadataUpdates model constructor.
     * @property {module:model/MetadataUpdates}
     */
    MetadataUpdates,

    /**
     * The Operator model constructor.
     * @property {module:model/Operator}
     */
    Operator,

    /**
     * The SearchByAttributeValue model constructor.
     * @property {module:model/SearchByAttributeValue}
     */
    SearchByAttributeValue,

    /**
     * The SearchByAttributeValueDICOMStudyDateAndTime model constructor.
     * @property {module:model/SearchByAttributeValueDICOMStudyDateAndTime}
     */
    SearchByAttributeValueDICOMStudyDateAndTime,

    /**
     * The SearchCriteria model constructor.
     * @property {module:model/SearchCriteria}
     */
    SearchCriteria,

    /**
     * The SearchFilter model constructor.
     * @property {module:model/SearchFilter}
     */
    SearchFilter,

    /**
     * The SearchImageSetsRequest model constructor.
     * @property {module:model/SearchImageSetsRequest}
     */
    SearchImageSetsRequest,

    /**
     * The SearchImageSetsRequestSearchCriteria model constructor.
     * @property {module:model/SearchImageSetsRequestSearchCriteria}
     */
    SearchImageSetsRequestSearchCriteria,

    /**
     * The SearchImageSetsResponse model constructor.
     * @property {module:model/SearchImageSetsResponse}
     */
    SearchImageSetsResponse,

    /**
     * The StartDICOMImportJobRequest model constructor.
     * @property {module:model/StartDICOMImportJobRequest}
     */
    StartDICOMImportJobRequest,

    /**
     * The StartDICOMImportJobResponse model constructor.
     * @property {module:model/StartDICOMImportJobResponse}
     */
    StartDICOMImportJobResponse,

    /**
     * The TagResourceRequest model constructor.
     * @property {module:model/TagResourceRequest}
     */
    TagResourceRequest,

    /**
     * The UpdateImageSetMetadataRequest model constructor.
     * @property {module:model/UpdateImageSetMetadataRequest}
     */
    UpdateImageSetMetadataRequest,

    /**
     * The UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdates model constructor.
     * @property {module:model/UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdates}
     */
    UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdates,

    /**
     * The UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdatesDICOMUpdates model constructor.
     * @property {module:model/UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdatesDICOMUpdates}
     */
    UpdateImageSetMetadataRequestUpdateImageSetMetadataUpdatesDICOMUpdates,

    /**
     * The UpdateImageSetMetadataResponse model constructor.
     * @property {module:model/UpdateImageSetMetadataResponse}
     */
    UpdateImageSetMetadataResponse,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};
