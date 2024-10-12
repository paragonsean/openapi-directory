/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import CustomVisionError from '../model/CustomVisionError';
import Image from '../model/Image';
import ImageCreateSummary from '../model/ImageCreateSummary';
import ImageFileCreateBatch from '../model/ImageFileCreateBatch';
import ImageIdCreateBatch from '../model/ImageIdCreateBatch';
import ImageRegionCreateBatch from '../model/ImageRegionCreateBatch';
import ImageRegionCreateSummary from '../model/ImageRegionCreateSummary';
import ImageTagCreateBatch from '../model/ImageTagCreateBatch';
import ImageTagCreateSummary from '../model/ImageTagCreateSummary';
import ImageUrlCreateBatch from '../model/ImageUrlCreateBatch';

/**
* ImageApi service.
* @module api/ImageApiApi
* @version 3.0
*/
export default class ImageApiApi {

    /**
    * Constructs a new ImageApiApi. 
    * @alias module:api/ImageApiApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createImageRegions operation.
     * @callback module:api/ImageApiApi~createImageRegionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ImageRegionCreateSummary} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a set of image regions.
     * This API accepts a batch of image regions, and optionally tags, to update existing images with region information.  There is a limit of 64 entries in the batch.
     * @param {String} projectId The project id.
     * @param {String} trainingKey API key.
     * @param {module:model/ImageRegionCreateBatch} imageRegionCreateBatch Batch of image regions which include a tag and bounding box. Limited to 64.
     * @param {module:api/ImageApiApi~createImageRegionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ImageRegionCreateSummary}
     */
    createImageRegions(projectId, trainingKey, imageRegionCreateBatch, callback) {
      let postBody = imageRegionCreateBatch;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling createImageRegions");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling createImageRegions");
      }
      // verify the required parameter 'imageRegionCreateBatch' is set
      if (imageRegionCreateBatch === undefined || imageRegionCreateBatch === null) {
        throw new Error("Missing the required parameter 'imageRegionCreateBatch' when calling createImageRegions");
      }

      let pathParams = {
        'projectId': projectId
      };
      let queryParams = {
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'];
      let accepts = ['application/json', 'application/xml', 'text/xml'];
      let returnType = ImageRegionCreateSummary;
      return this.apiClient.callApi(
        '/projects/{projectId}/images/regions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createImageTags operation.
     * @callback module:api/ImageApiApi~createImageTagsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ImageTagCreateSummary} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Associate a set of images with a set of tags.
     * @param {String} projectId The project id.
     * @param {String} trainingKey API key.
     * @param {module:model/ImageTagCreateBatch} imageTagCreateBatch Batch of image tags. Limited to 128 tags per batch.
     * @param {module:api/ImageApiApi~createImageTagsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ImageTagCreateSummary}
     */
    createImageTags(projectId, trainingKey, imageTagCreateBatch, callback) {
      let postBody = imageTagCreateBatch;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling createImageTags");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling createImageTags");
      }
      // verify the required parameter 'imageTagCreateBatch' is set
      if (imageTagCreateBatch === undefined || imageTagCreateBatch === null) {
        throw new Error("Missing the required parameter 'imageTagCreateBatch' when calling createImageTags");
      }

      let pathParams = {
        'projectId': projectId
      };
      let queryParams = {
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'];
      let accepts = ['application/json', 'application/xml', 'text/xml'];
      let returnType = ImageTagCreateSummary;
      return this.apiClient.callApi(
        '/projects/{projectId}/images/tags', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createImagesFromData operation.
     * @callback module:api/ImageApiApi~createImagesFromDataCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ImageCreateSummary} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add the provided images to the set of training images.
     * This API accepts body content as multipart/form-data and application/octet-stream. When using multipart  multiple image files can be sent at once, with a maximum of 64 files
     * @param {String} projectId The project id.
     * @param {String} trainingKey API key.
     * @param {File} imageData Binary image data. Supported formats are JPEG, GIF, PNG, and BMP. Supports images up to 6MB.
     * @param {Object} opts Optional parameters
     * @param {Array.<String>} [tagIds] The tags ids with which to tag each image. Limited to 20.
     * @param {module:api/ImageApiApi~createImagesFromDataCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ImageCreateSummary}
     */
    createImagesFromData(projectId, trainingKey, imageData, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling createImagesFromData");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling createImagesFromData");
      }
      // verify the required parameter 'imageData' is set
      if (imageData === undefined || imageData === null) {
        throw new Error("Missing the required parameter 'imageData' when calling createImagesFromData");
      }

      let pathParams = {
        'projectId': projectId
      };
      let queryParams = {
        'tagIds': this.apiClient.buildCollectionParam(opts['tagIds'], 'csv')
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
        'imageData': imageData
      };

      let authNames = [];
      let contentTypes = ['multipart/form-data'];
      let accepts = ['application/json', 'application/xml', 'text/xml'];
      let returnType = ImageCreateSummary;
      return this.apiClient.callApi(
        '/projects/{projectId}/images', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createImagesFromFiles operation.
     * @callback module:api/ImageApiApi~createImagesFromFilesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ImageCreateSummary} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add the provided batch of images to the set of training images.
     * This API accepts a batch of files, and optionally tags, to create images. There is a limit of 64 images and 20 tags.
     * @param {String} projectId The project id.
     * @param {String} trainingKey API key.
     * @param {module:model/ImageFileCreateBatch} imageFileCreateBatch The batch of image files to add. Limited to 64 images and 20 tags per batch.
     * @param {module:api/ImageApiApi~createImagesFromFilesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ImageCreateSummary}
     */
    createImagesFromFiles(projectId, trainingKey, imageFileCreateBatch, callback) {
      let postBody = imageFileCreateBatch;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling createImagesFromFiles");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling createImagesFromFiles");
      }
      // verify the required parameter 'imageFileCreateBatch' is set
      if (imageFileCreateBatch === undefined || imageFileCreateBatch === null) {
        throw new Error("Missing the required parameter 'imageFileCreateBatch' when calling createImagesFromFiles");
      }

      let pathParams = {
        'projectId': projectId
      };
      let queryParams = {
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'];
      let accepts = ['application/json', 'application/xml', 'text/xml'];
      let returnType = ImageCreateSummary;
      return this.apiClient.callApi(
        '/projects/{projectId}/images/files', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createImagesFromPredictions operation.
     * @callback module:api/ImageApiApi~createImagesFromPredictionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ImageCreateSummary} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add the specified predicted images to the set of training images.
     * This API creates a batch of images from predicted images specified. There is a limit of 64 images and 20 tags.
     * @param {String} projectId The project id.
     * @param {String} trainingKey API key.
     * @param {module:model/ImageIdCreateBatch} imageIdCreateBatch Image and tag ids. Limited to 64 images and 20 tags per batch.
     * @param {module:api/ImageApiApi~createImagesFromPredictionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ImageCreateSummary}
     */
    createImagesFromPredictions(projectId, trainingKey, imageIdCreateBatch, callback) {
      let postBody = imageIdCreateBatch;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling createImagesFromPredictions");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling createImagesFromPredictions");
      }
      // verify the required parameter 'imageIdCreateBatch' is set
      if (imageIdCreateBatch === undefined || imageIdCreateBatch === null) {
        throw new Error("Missing the required parameter 'imageIdCreateBatch' when calling createImagesFromPredictions");
      }

      let pathParams = {
        'projectId': projectId
      };
      let queryParams = {
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'];
      let accepts = ['application/json', 'application/xml', 'text/xml'];
      let returnType = ImageCreateSummary;
      return this.apiClient.callApi(
        '/projects/{projectId}/images/predictions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createImagesFromUrls operation.
     * @callback module:api/ImageApiApi~createImagesFromUrlsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ImageCreateSummary} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add the provided images urls to the set of training images.
     * This API accepts a batch of urls, and optionally tags, to create images. There is a limit of 64 images and 20 tags.
     * @param {String} projectId The project id.
     * @param {String} trainingKey API key.
     * @param {module:model/ImageUrlCreateBatch} imageUrlCreateBatch Image urls and tag ids. Limited to 64 images and 20 tags per batch.
     * @param {module:api/ImageApiApi~createImagesFromUrlsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ImageCreateSummary}
     */
    createImagesFromUrls(projectId, trainingKey, imageUrlCreateBatch, callback) {
      let postBody = imageUrlCreateBatch;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling createImagesFromUrls");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling createImagesFromUrls");
      }
      // verify the required parameter 'imageUrlCreateBatch' is set
      if (imageUrlCreateBatch === undefined || imageUrlCreateBatch === null) {
        throw new Error("Missing the required parameter 'imageUrlCreateBatch' when calling createImagesFromUrls");
      }

      let pathParams = {
        'projectId': projectId
      };
      let queryParams = {
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/xml'];
      let accepts = ['application/json', 'application/xml', 'text/xml'];
      let returnType = ImageCreateSummary;
      return this.apiClient.callApi(
        '/projects/{projectId}/images/urls', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteImageRegions operation.
     * @callback module:api/ImageApiApi~deleteImageRegionsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a set of image regions.
     * @param {String} projectId The project id.
     * @param {Array.<String>} regionIds Regions to delete. Limited to 64.
     * @param {String} trainingKey API key.
     * @param {module:api/ImageApiApi~deleteImageRegionsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteImageRegions(projectId, regionIds, trainingKey, callback) {
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling deleteImageRegions");
      }
      // verify the required parameter 'regionIds' is set
      if (regionIds === undefined || regionIds === null) {
        throw new Error("Missing the required parameter 'regionIds' when calling deleteImageRegions");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling deleteImageRegions");
      }

      let pathParams = {
        'projectId': projectId
      };
      let queryParams = {
        'regionIds': this.apiClient.buildCollectionParam(regionIds, 'csv')
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = null;
      return this.apiClient.callApi(
        '/projects/{projectId}/images/regions', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteImageTags operation.
     * @callback module:api/ImageApiApi~deleteImageTagsCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove a set of tags from a set of images.
     * @param {String} projectId The project id.
     * @param {Array.<String>} imageIds Image ids. Limited to 64 images.
     * @param {Array.<String>} tagIds Tags to be deleted from the specified images. Limited to 20 tags.
     * @param {String} trainingKey API key.
     * @param {module:api/ImageApiApi~deleteImageTagsCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteImageTags(projectId, imageIds, tagIds, trainingKey, callback) {
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling deleteImageTags");
      }
      // verify the required parameter 'imageIds' is set
      if (imageIds === undefined || imageIds === null) {
        throw new Error("Missing the required parameter 'imageIds' when calling deleteImageTags");
      }
      // verify the required parameter 'tagIds' is set
      if (tagIds === undefined || tagIds === null) {
        throw new Error("Missing the required parameter 'tagIds' when calling deleteImageTags");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling deleteImageTags");
      }

      let pathParams = {
        'projectId': projectId
      };
      let queryParams = {
        'imageIds': this.apiClient.buildCollectionParam(imageIds, 'csv'),
        'tagIds': this.apiClient.buildCollectionParam(tagIds, 'csv')
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = null;
      return this.apiClient.callApi(
        '/projects/{projectId}/images/tags', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteImages operation.
     * @callback module:api/ImageApiApi~deleteImagesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete images from the set of training images.
     * @param {String} projectId The project id.
     * @param {Array.<String>} imageIds Ids of the images to be deleted. Limited to 256 images per batch.
     * @param {String} trainingKey API key.
     * @param {module:api/ImageApiApi~deleteImagesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteImages(projectId, imageIds, trainingKey, callback) {
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling deleteImages");
      }
      // verify the required parameter 'imageIds' is set
      if (imageIds === undefined || imageIds === null) {
        throw new Error("Missing the required parameter 'imageIds' when calling deleteImages");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling deleteImages");
      }

      let pathParams = {
        'projectId': projectId
      };
      let queryParams = {
        'imageIds': this.apiClient.buildCollectionParam(imageIds, 'csv')
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = null;
      return this.apiClient.callApi(
        '/projects/{projectId}/images', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getImagesByIds operation.
     * @callback module:api/ImageApiApi~getImagesByIdsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Image>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get images by id for a given project iteration.
     * This API will return a set of Images for the specified tags and optionally iteration. If no iteration is specified the  current workspace is used.
     * @param {String} projectId The project id.
     * @param {String} trainingKey API key.
     * @param {Object} opts Optional parameters
     * @param {Array.<String>} [imageIds] The list of image ids to retrieve. Limited to 256.
     * @param {String} [iterationId] The iteration id. Defaults to workspace.
     * @param {module:api/ImageApiApi~getImagesByIdsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Image>}
     */
    getImagesByIds(projectId, trainingKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling getImagesByIds");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling getImagesByIds");
      }

      let pathParams = {
        'projectId': projectId
      };
      let queryParams = {
        'imageIds': this.apiClient.buildCollectionParam(opts['imageIds'], 'csv'),
        'iterationId': opts['iterationId']
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/xml'];
      let returnType = [Image];
      return this.apiClient.callApi(
        '/projects/{projectId}/images/id', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTaggedImageCount operation.
     * @callback module:api/ImageApiApi~getTaggedImageCountCallback
     * @param {String} error Error message, if any.
     * @param {Number} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets the number of images tagged with the provided {tagIds}.
     * The filtering is on an and/or relationship. For example, if the provided tag ids are for the \"Dog\" and  \"Cat\" tags, then only images tagged with Dog and/or Cat will be returned
     * @param {String} projectId The project id.
     * @param {String} trainingKey API key.
     * @param {Object} opts Optional parameters
     * @param {String} [iterationId] The iteration id. Defaults to workspace.
     * @param {Array.<String>} [tagIds] A list of tags ids to filter the images to count. Defaults to all tags when null.
     * @param {module:api/ImageApiApi~getTaggedImageCountCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Number}
     */
    getTaggedImageCount(projectId, trainingKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling getTaggedImageCount");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling getTaggedImageCount");
      }

      let pathParams = {
        'projectId': projectId
      };
      let queryParams = {
        'iterationId': opts['iterationId'],
        'tagIds': this.apiClient.buildCollectionParam(opts['tagIds'], 'csv')
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/xml'];
      let returnType = 'Number';
      return this.apiClient.callApi(
        '/projects/{projectId}/images/tagged/count', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTaggedImages operation.
     * @callback module:api/ImageApiApi~getTaggedImagesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Image>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get tagged images for a given project iteration.
     * This API supports batching and range selection. By default it will only return first 50 images matching images.  Use the {take} and {skip} parameters to control how many images to return in a given batch.  The filtering is on an and/or relationship. For example, if the provided tag ids are for the \"Dog\" and  \"Cat\" tags, then only images tagged with Dog and/or Cat will be returned
     * @param {String} projectId The project id.
     * @param {String} trainingKey API key.
     * @param {Object} opts Optional parameters
     * @param {String} [iterationId] The iteration id. Defaults to workspace.
     * @param {Array.<String>} [tagIds] A list of tags ids to filter the images. Defaults to all tagged images when null. Limited to 20.
     * @param {module:model/String} [orderBy] The ordering. Defaults to newest.
     * @param {Number} [take = 50)] Maximum number of images to return. Defaults to 50, limited to 256.
     * @param {Number} [skip = 0)] Number of images to skip before beginning the image batch. Defaults to 0.
     * @param {module:api/ImageApiApi~getTaggedImagesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Image>}
     */
    getTaggedImages(projectId, trainingKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling getTaggedImages");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling getTaggedImages");
      }

      let pathParams = {
        'projectId': projectId
      };
      let queryParams = {
        'iterationId': opts['iterationId'],
        'tagIds': this.apiClient.buildCollectionParam(opts['tagIds'], 'csv'),
        'orderBy': opts['orderBy'],
        'take': opts['take'],
        'skip': opts['skip']
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/xml'];
      let returnType = [Image];
      return this.apiClient.callApi(
        '/projects/{projectId}/images/tagged', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getUntaggedImageCount operation.
     * @callback module:api/ImageApiApi~getUntaggedImageCountCallback
     * @param {String} error Error message, if any.
     * @param {Number} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets the number of untagged images.
     * This API returns the images which have no tags for a given project and optionally an iteration. If no iteration is specified the  current workspace is used.
     * @param {String} projectId The project id.
     * @param {String} trainingKey API key.
     * @param {Object} opts Optional parameters
     * @param {String} [iterationId] The iteration id. Defaults to workspace.
     * @param {module:api/ImageApiApi~getUntaggedImageCountCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Number}
     */
    getUntaggedImageCount(projectId, trainingKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling getUntaggedImageCount");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling getUntaggedImageCount");
      }

      let pathParams = {
        'projectId': projectId
      };
      let queryParams = {
        'iterationId': opts['iterationId']
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/xml'];
      let returnType = 'Number';
      return this.apiClient.callApi(
        '/projects/{projectId}/images/untagged/count', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getUntaggedImages operation.
     * @callback module:api/ImageApiApi~getUntaggedImagesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Image>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get untagged images for a given project iteration.
     * This API supports batching and range selection. By default it will only return first 50 images matching images.  Use the {take} and {skip} parameters to control how many images to return in a given batch.
     * @param {String} projectId The project id.
     * @param {String} trainingKey API key.
     * @param {Object} opts Optional parameters
     * @param {String} [iterationId] The iteration id. Defaults to workspace.
     * @param {module:model/String} [orderBy] The ordering. Defaults to newest.
     * @param {Number} [take = 50)] Maximum number of images to return. Defaults to 50, limited to 256.
     * @param {Number} [skip = 0)] Number of images to skip before beginning the image batch. Defaults to 0.
     * @param {module:api/ImageApiApi~getUntaggedImagesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Image>}
     */
    getUntaggedImages(projectId, trainingKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling getUntaggedImages");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling getUntaggedImages");
      }

      let pathParams = {
        'projectId': projectId
      };
      let queryParams = {
        'iterationId': opts['iterationId'],
        'orderBy': opts['orderBy'],
        'take': opts['take'],
        'skip': opts['skip']
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/xml'];
      let returnType = [Image];
      return this.apiClient.callApi(
        '/projects/{projectId}/images/untagged', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
