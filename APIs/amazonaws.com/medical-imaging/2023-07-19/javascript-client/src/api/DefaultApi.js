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


import ApiClient from "../ApiClient";
import CopyImageSetRequest from '../model/CopyImageSetRequest';
import CopyImageSetResponse from '../model/CopyImageSetResponse';
import CreateDatastoreRequest from '../model/CreateDatastoreRequest';
import CreateDatastoreResponse from '../model/CreateDatastoreResponse';
import DeleteDatastoreResponse from '../model/DeleteDatastoreResponse';
import DeleteImageSetResponse from '../model/DeleteImageSetResponse';
import GetDICOMImportJobResponse from '../model/GetDICOMImportJobResponse';
import GetDatastoreResponse from '../model/GetDatastoreResponse';
import GetImageFrameRequest from '../model/GetImageFrameRequest';
import GetImageFrameResponse from '../model/GetImageFrameResponse';
import GetImageSetMetadataResponse from '../model/GetImageSetMetadataResponse';
import GetImageSetResponse from '../model/GetImageSetResponse';
import ListDICOMImportJobsResponse from '../model/ListDICOMImportJobsResponse';
import ListDatastoresResponse from '../model/ListDatastoresResponse';
import ListImageSetVersionsResponse from '../model/ListImageSetVersionsResponse';
import ListTagsForResourceResponse from '../model/ListTagsForResourceResponse';
import SearchImageSetsRequest from '../model/SearchImageSetsRequest';
import SearchImageSetsResponse from '../model/SearchImageSetsResponse';
import StartDICOMImportJobRequest from '../model/StartDICOMImportJobRequest';
import StartDICOMImportJobResponse from '../model/StartDICOMImportJobResponse';
import TagResourceRequest from '../model/TagResourceRequest';
import UpdateImageSetMetadataRequest from '../model/UpdateImageSetMetadataRequest';
import UpdateImageSetMetadataResponse from '../model/UpdateImageSetMetadataResponse';

/**
* Default service.
* @module api/DefaultApi
* @version 2023-07-19
*/
export default class DefaultApi {

    /**
    * Constructs a new DefaultApi. 
    * @alias module:api/DefaultApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the copyImageSet operation.
     * @callback module:api/DefaultApi~copyImageSetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CopyImageSetResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Copy an image set.
     * @param {String} datastoreId The data store identifier.
     * @param {String} sourceImageSetId The source image set identifier.
     * @param {module:model/CopyImageSetRequest} copyImageSetRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~copyImageSetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CopyImageSetResponse}
     */
    copyImageSet(datastoreId, sourceImageSetId, copyImageSetRequest, opts, callback) {
      opts = opts || {};
      let postBody = copyImageSetRequest;
      // verify the required parameter 'datastoreId' is set
      if (datastoreId === undefined || datastoreId === null) {
        throw new Error("Missing the required parameter 'datastoreId' when calling copyImageSet");
      }
      // verify the required parameter 'sourceImageSetId' is set
      if (sourceImageSetId === undefined || sourceImageSetId === null) {
        throw new Error("Missing the required parameter 'sourceImageSetId' when calling copyImageSet");
      }
      // verify the required parameter 'copyImageSetRequest' is set
      if (copyImageSetRequest === undefined || copyImageSetRequest === null) {
        throw new Error("Missing the required parameter 'copyImageSetRequest' when calling copyImageSet");
      }

      let pathParams = {
        'datastoreId': datastoreId,
        'sourceImageSetId': sourceImageSetId
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CopyImageSetResponse;
      return this.apiClient.callApi(
        '/datastore/{datastoreId}/imageSet/{sourceImageSetId}/copyImageSet', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createDatastore operation.
     * @callback module:api/DefaultApi~createDatastoreCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateDatastoreResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a data store.
     * @param {module:model/CreateDatastoreRequest} createDatastoreRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createDatastoreCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateDatastoreResponse}
     */
    createDatastore(createDatastoreRequest, opts, callback) {
      opts = opts || {};
      let postBody = createDatastoreRequest;
      // verify the required parameter 'createDatastoreRequest' is set
      if (createDatastoreRequest === undefined || createDatastoreRequest === null) {
        throw new Error("Missing the required parameter 'createDatastoreRequest' when calling createDatastore");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateDatastoreResponse;
      return this.apiClient.callApi(
        '/datastore', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteDatastore operation.
     * @callback module:api/DefaultApi~deleteDatastoreCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteDatastoreResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Delete a data store.</p> <note> <p>Before a data store can be deleted, you must first delete all image sets within it.</p> </note>
     * @param {String} datastoreId The data store identifier.
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteDatastoreCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteDatastoreResponse}
     */
    deleteDatastore(datastoreId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'datastoreId' is set
      if (datastoreId === undefined || datastoreId === null) {
        throw new Error("Missing the required parameter 'datastoreId' when calling deleteDatastore");
      }

      let pathParams = {
        'datastoreId': datastoreId
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DeleteDatastoreResponse;
      return this.apiClient.callApi(
        '/datastore/{datastoreId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteImageSet operation.
     * @callback module:api/DefaultApi~deleteImageSetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteImageSetResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an image set.
     * @param {String} datastoreId The data store identifier.
     * @param {String} imageSetId The image set identifier.
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteImageSetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteImageSetResponse}
     */
    deleteImageSet(datastoreId, imageSetId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'datastoreId' is set
      if (datastoreId === undefined || datastoreId === null) {
        throw new Error("Missing the required parameter 'datastoreId' when calling deleteImageSet");
      }
      // verify the required parameter 'imageSetId' is set
      if (imageSetId === undefined || imageSetId === null) {
        throw new Error("Missing the required parameter 'imageSetId' when calling deleteImageSet");
      }

      let pathParams = {
        'datastoreId': datastoreId,
        'imageSetId': imageSetId
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DeleteImageSetResponse;
      return this.apiClient.callApi(
        '/datastore/{datastoreId}/imageSet/{imageSetId}/deleteImageSet', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDICOMImportJob operation.
     * @callback module:api/DefaultApi~getDICOMImportJobCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDICOMImportJobResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the import job properties to learn more about the job or job progress.
     * @param {String} datastoreId The data store identifier.
     * @param {String} jobId The import job identifier.
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getDICOMImportJobCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDICOMImportJobResponse}
     */
    getDICOMImportJob(datastoreId, jobId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'datastoreId' is set
      if (datastoreId === undefined || datastoreId === null) {
        throw new Error("Missing the required parameter 'datastoreId' when calling getDICOMImportJob");
      }
      // verify the required parameter 'jobId' is set
      if (jobId === undefined || jobId === null) {
        throw new Error("Missing the required parameter 'jobId' when calling getDICOMImportJob");
      }

      let pathParams = {
        'datastoreId': datastoreId,
        'jobId': jobId
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetDICOMImportJobResponse;
      return this.apiClient.callApi(
        '/getDICOMImportJob/datastore/{datastoreId}/job/{jobId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDatastore operation.
     * @callback module:api/DefaultApi~getDatastoreCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDatastoreResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get data store properties.
     * @param {String} datastoreId The data store identifier.
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getDatastoreCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDatastoreResponse}
     */
    getDatastore(datastoreId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'datastoreId' is set
      if (datastoreId === undefined || datastoreId === null) {
        throw new Error("Missing the required parameter 'datastoreId' when calling getDatastore");
      }

      let pathParams = {
        'datastoreId': datastoreId
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetDatastoreResponse;
      return this.apiClient.callApi(
        '/datastore/{datastoreId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getImageFrame operation.
     * @callback module:api/DefaultApi~getImageFrameCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetImageFrameResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get an image frame (pixel data) for an image set.
     * @param {String} datastoreId The data store identifier.
     * @param {String} imageSetId The image set identifier.
     * @param {module:model/GetImageFrameRequest} getImageFrameRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getImageFrameCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetImageFrameResponse}
     */
    getImageFrame(datastoreId, imageSetId, getImageFrameRequest, opts, callback) {
      opts = opts || {};
      let postBody = getImageFrameRequest;
      // verify the required parameter 'datastoreId' is set
      if (datastoreId === undefined || datastoreId === null) {
        throw new Error("Missing the required parameter 'datastoreId' when calling getImageFrame");
      }
      // verify the required parameter 'imageSetId' is set
      if (imageSetId === undefined || imageSetId === null) {
        throw new Error("Missing the required parameter 'imageSetId' when calling getImageFrame");
      }
      // verify the required parameter 'getImageFrameRequest' is set
      if (getImageFrameRequest === undefined || getImageFrameRequest === null) {
        throw new Error("Missing the required parameter 'getImageFrameRequest' when calling getImageFrame");
      }

      let pathParams = {
        'datastoreId': datastoreId,
        'imageSetId': imageSetId
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetImageFrameResponse;
      return this.apiClient.callApi(
        '/datastore/{datastoreId}/imageSet/{imageSetId}/getImageFrame', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getImageSet operation.
     * @callback module:api/DefaultApi~getImageSetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetImageSetResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get image set properties.
     * @param {String} datastoreId The data store identifier.
     * @param {String} imageSetId The image set identifier.
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [version] The image set version identifier.
     * @param {module:api/DefaultApi~getImageSetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetImageSetResponse}
     */
    getImageSet(datastoreId, imageSetId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'datastoreId' is set
      if (datastoreId === undefined || datastoreId === null) {
        throw new Error("Missing the required parameter 'datastoreId' when calling getImageSet");
      }
      // verify the required parameter 'imageSetId' is set
      if (imageSetId === undefined || imageSetId === null) {
        throw new Error("Missing the required parameter 'imageSetId' when calling getImageSet");
      }

      let pathParams = {
        'datastoreId': datastoreId,
        'imageSetId': imageSetId
      };
      let queryParams = {
        'version': opts['version']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetImageSetResponse;
      return this.apiClient.callApi(
        '/datastore/{datastoreId}/imageSet/{imageSetId}/getImageSet', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getImageSetMetadata operation.
     * @callback module:api/DefaultApi~getImageSetMetadataCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetImageSetMetadataResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get metadata attributes for an image set.
     * @param {String} datastoreId The data store identifier.
     * @param {String} imageSetId The image set identifier.
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [version] The image set version identifier.
     * @param {module:api/DefaultApi~getImageSetMetadataCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetImageSetMetadataResponse}
     */
    getImageSetMetadata(datastoreId, imageSetId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'datastoreId' is set
      if (datastoreId === undefined || datastoreId === null) {
        throw new Error("Missing the required parameter 'datastoreId' when calling getImageSetMetadata");
      }
      // verify the required parameter 'imageSetId' is set
      if (imageSetId === undefined || imageSetId === null) {
        throw new Error("Missing the required parameter 'imageSetId' when calling getImageSetMetadata");
      }

      let pathParams = {
        'datastoreId': datastoreId,
        'imageSetId': imageSetId
      };
      let queryParams = {
        'version': opts['version']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetImageSetMetadataResponse;
      return this.apiClient.callApi(
        '/datastore/{datastoreId}/imageSet/{imageSetId}/getImageSetMetadata', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listDICOMImportJobs operation.
     * @callback module:api/DefaultApi~listDICOMImportJobsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListDICOMImportJobsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List import jobs created by this AWS account for a specific data store.
     * @param {String} datastoreId The data store identifier.
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:model/String} [jobStatus] The filters for listing import jobs based on status.
     * @param {String} [nextToken] The pagination token used to request the list of import jobs on the next page.
     * @param {Number} [maxResults] The max results count. The upper bound is determined by load testing.
     * @param {module:api/DefaultApi~listDICOMImportJobsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListDICOMImportJobsResponse}
     */
    listDICOMImportJobs(datastoreId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'datastoreId' is set
      if (datastoreId === undefined || datastoreId === null) {
        throw new Error("Missing the required parameter 'datastoreId' when calling listDICOMImportJobs");
      }

      let pathParams = {
        'datastoreId': datastoreId
      };
      let queryParams = {
        'jobStatus': opts['jobStatus'],
        'nextToken': opts['nextToken'],
        'maxResults': opts['maxResults']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ListDICOMImportJobsResponse;
      return this.apiClient.callApi(
        '/listDICOMImportJobs/datastore/{datastoreId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listDatastores operation.
     * @callback module:api/DefaultApi~listDatastoresCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListDatastoresResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List data stores created by this AWS account.
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:model/String} [datastoreStatus] The data store status.
     * @param {String} [nextToken] The pagination token used to request the list of data stores on the next page.
     * @param {Number} [maxResults] Valid Range: Minimum value of 1. Maximum value of 50.
     * @param {module:api/DefaultApi~listDatastoresCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListDatastoresResponse}
     */
    listDatastores(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'datastoreStatus': opts['datastoreStatus'],
        'nextToken': opts['nextToken'],
        'maxResults': opts['maxResults']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ListDatastoresResponse;
      return this.apiClient.callApi(
        '/datastore', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listImageSetVersions operation.
     * @callback module:api/DefaultApi~listImageSetVersionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListImageSetVersionsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List image set versions.
     * @param {String} datastoreId The data store identifier.
     * @param {String} imageSetId The image set identifier.
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [nextToken] The pagination token used to request the list of image set versions on the next page.
     * @param {Number} [maxResults] The max results count.
     * @param {module:api/DefaultApi~listImageSetVersionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListImageSetVersionsResponse}
     */
    listImageSetVersions(datastoreId, imageSetId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'datastoreId' is set
      if (datastoreId === undefined || datastoreId === null) {
        throw new Error("Missing the required parameter 'datastoreId' when calling listImageSetVersions");
      }
      // verify the required parameter 'imageSetId' is set
      if (imageSetId === undefined || imageSetId === null) {
        throw new Error("Missing the required parameter 'imageSetId' when calling listImageSetVersions");
      }

      let pathParams = {
        'datastoreId': datastoreId,
        'imageSetId': imageSetId
      };
      let queryParams = {
        'nextToken': opts['nextToken'],
        'maxResults': opts['maxResults']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ListImageSetVersionsResponse;
      return this.apiClient.callApi(
        '/datastore/{datastoreId}/imageSet/{imageSetId}/listImageSetVersions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listTagsForResource operation.
     * @callback module:api/DefaultApi~listTagsForResourceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListTagsForResourceResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists all tags associated with a medical imaging resource.
     * @param {String} resourceArn The Amazon Resource Name (ARN) of the medical imaging resource to list tags for.
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~listTagsForResourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListTagsForResourceResponse}
     */
    listTagsForResource(resourceArn, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'resourceArn' is set
      if (resourceArn === undefined || resourceArn === null) {
        throw new Error("Missing the required parameter 'resourceArn' when calling listTagsForResource");
      }

      let pathParams = {
        'resourceArn': resourceArn
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ListTagsForResourceResponse;
      return this.apiClient.callApi(
        '/tags/{resourceArn}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the searchImageSets operation.
     * @callback module:api/DefaultApi~searchImageSetsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SearchImageSetsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Search image sets based on defined input attributes.
     * @param {String} datastoreId The identifier of the data store where the image sets reside.
     * @param {module:model/SearchImageSetsRequest} searchImageSetsRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {Number} [maxResults] The maximum number of results that can be returned in a search.
     * @param {String} [nextToken] The token used for pagination of results returned in the response. Use the token returned from the previous request to continue results where the previous request ended.
     * @param {module:api/DefaultApi~searchImageSetsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SearchImageSetsResponse}
     */
    searchImageSets(datastoreId, searchImageSetsRequest, opts, callback) {
      opts = opts || {};
      let postBody = searchImageSetsRequest;
      // verify the required parameter 'datastoreId' is set
      if (datastoreId === undefined || datastoreId === null) {
        throw new Error("Missing the required parameter 'datastoreId' when calling searchImageSets");
      }
      // verify the required parameter 'searchImageSetsRequest' is set
      if (searchImageSetsRequest === undefined || searchImageSetsRequest === null) {
        throw new Error("Missing the required parameter 'searchImageSetsRequest' when calling searchImageSets");
      }

      let pathParams = {
        'datastoreId': datastoreId
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = SearchImageSetsResponse;
      return this.apiClient.callApi(
        '/datastore/{datastoreId}/searchImageSets', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the startDICOMImportJob operation.
     * @callback module:api/DefaultApi~startDICOMImportJobCallback
     * @param {String} error Error message, if any.
     * @param {module:model/StartDICOMImportJobResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Start importing bulk data into an <code>ACTIVE</code> data store. The import job imports DICOM P10 files found in the S3 prefix specified by the <code>inputS3Uri</code> parameter. The import job stores processing results in the file specified by the <code>outputS3Uri</code> parameter.
     * @param {String} datastoreId The data store identifier.
     * @param {module:model/StartDICOMImportJobRequest} startDICOMImportJobRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~startDICOMImportJobCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/StartDICOMImportJobResponse}
     */
    startDICOMImportJob(datastoreId, startDICOMImportJobRequest, opts, callback) {
      opts = opts || {};
      let postBody = startDICOMImportJobRequest;
      // verify the required parameter 'datastoreId' is set
      if (datastoreId === undefined || datastoreId === null) {
        throw new Error("Missing the required parameter 'datastoreId' when calling startDICOMImportJob");
      }
      // verify the required parameter 'startDICOMImportJobRequest' is set
      if (startDICOMImportJobRequest === undefined || startDICOMImportJobRequest === null) {
        throw new Error("Missing the required parameter 'startDICOMImportJobRequest' when calling startDICOMImportJob");
      }

      let pathParams = {
        'datastoreId': datastoreId
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = StartDICOMImportJobResponse;
      return this.apiClient.callApi(
        '/startDICOMImportJob/datastore/{datastoreId}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the tagResource operation.
     * @callback module:api/DefaultApi~tagResourceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Adds a user-specifed key and value tag to a medical imaging resource.
     * @param {String} resourceArn The Amazon Resource Name (ARN) of the medical imaging resource that tags are being added to.
     * @param {module:model/TagResourceRequest} tagResourceRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~tagResourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    tagResource(resourceArn, tagResourceRequest, opts, callback) {
      opts = opts || {};
      let postBody = tagResourceRequest;
      // verify the required parameter 'resourceArn' is set
      if (resourceArn === undefined || resourceArn === null) {
        throw new Error("Missing the required parameter 'resourceArn' when calling tagResource");
      }
      // verify the required parameter 'tagResourceRequest' is set
      if (tagResourceRequest === undefined || tagResourceRequest === null) {
        throw new Error("Missing the required parameter 'tagResourceRequest' when calling tagResource");
      }

      let pathParams = {
        'resourceArn': resourceArn
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/tags/{resourceArn}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the untagResource operation.
     * @callback module:api/DefaultApi~untagResourceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Removes tags from a medical imaging resource.
     * @param {String} resourceArn The Amazon Resource Name (ARN) of the medical imaging resource that tags are being removed from.
     * @param {Array.<String>} tagKeys The keys for the tags to be removed from the medical imaging resource.
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~untagResourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    untagResource(resourceArn, tagKeys, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'resourceArn' is set
      if (resourceArn === undefined || resourceArn === null) {
        throw new Error("Missing the required parameter 'resourceArn' when calling untagResource");
      }
      // verify the required parameter 'tagKeys' is set
      if (tagKeys === undefined || tagKeys === null) {
        throw new Error("Missing the required parameter 'tagKeys' when calling untagResource");
      }

      let pathParams = {
        'resourceArn': resourceArn
      };
      let queryParams = {
        'tagKeys': this.apiClient.buildCollectionParam(tagKeys, 'multi')
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/tags/{resourceArn}#tagKeys', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateImageSetMetadata operation.
     * @callback module:api/DefaultApi~updateImageSetMetadataCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateImageSetMetadataResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update image set metadata attributes.
     * @param {String} datastoreId The data store identifier.
     * @param {String} imageSetId The image set identifier.
     * @param {String} latestVersion The latest image set version identifier.
     * @param {module:model/UpdateImageSetMetadataRequest} updateImageSetMetadataRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateImageSetMetadataCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateImageSetMetadataResponse}
     */
    updateImageSetMetadata(datastoreId, imageSetId, latestVersion, updateImageSetMetadataRequest, opts, callback) {
      opts = opts || {};
      let postBody = updateImageSetMetadataRequest;
      // verify the required parameter 'datastoreId' is set
      if (datastoreId === undefined || datastoreId === null) {
        throw new Error("Missing the required parameter 'datastoreId' when calling updateImageSetMetadata");
      }
      // verify the required parameter 'imageSetId' is set
      if (imageSetId === undefined || imageSetId === null) {
        throw new Error("Missing the required parameter 'imageSetId' when calling updateImageSetMetadata");
      }
      // verify the required parameter 'latestVersion' is set
      if (latestVersion === undefined || latestVersion === null) {
        throw new Error("Missing the required parameter 'latestVersion' when calling updateImageSetMetadata");
      }
      // verify the required parameter 'updateImageSetMetadataRequest' is set
      if (updateImageSetMetadataRequest === undefined || updateImageSetMetadataRequest === null) {
        throw new Error("Missing the required parameter 'updateImageSetMetadataRequest' when calling updateImageSetMetadata");
      }

      let pathParams = {
        'datastoreId': datastoreId,
        'imageSetId': imageSetId
      };
      let queryParams = {
        'latestVersion': latestVersion
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateImageSetMetadataResponse;
      return this.apiClient.callApi(
        '/datastore/{datastoreId}/imageSet/{imageSetId}/updateImageSetMetadata#latestVersion', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
