/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ChildObjects from '../model/ChildObjects';
import OoxmlDTO from '../model/OoxmlDTO';
import ProblemDetails from '../model/ProblemDetails';
import SlideShapes from '../model/SlideShapes';
import SlideShapesDetails from '../model/SlideShapesDetails';

/**
* Shapes service.
* @module api/ShapesApi
* @version 0.1.0
*/
export default class ShapesApi {

    /**
    * Constructs a new ShapesApi. 
    * @alias module:api/ShapesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the slidesShapesChildobjectsGetId operation.
     * @callback module:api/ShapesApi~slidesShapesChildobjectsGetIdCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/ChildObjects>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Slides: Get Dependent Objects Tree
     * This endpoint is helpful for helping users and bots identify dependent objects to this Slide and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.
     * @param {String} id 
     * @param {module:api/ShapesApi~slidesShapesChildobjectsGetIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/ChildObjects>}
     */
    slidesShapesChildobjectsGetId(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling slidesShapesChildobjectsGetId");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [ChildObjects];
      return this.apiClient.callApi(
        '/Shapes/ChildObjects/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the slidesShapesDetailsGetId operation.
     * @callback module:api/ShapesApi~slidesShapesDetailsGetIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SlideShapesDetails} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Slides: Get Details
     * Returns object metadata and information about relative dependent objects 
     * @param {String} id 
     * @param {module:api/ShapesApi~slidesShapesDetailsGetIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SlideShapesDetails}
     */
    slidesShapesDetailsGetId(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling slidesShapesDetailsGetId");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = SlideShapesDetails;
      return this.apiClient.callApi(
        '/Shapes/Details/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the slidesShapesGetId operation.
     * @callback module:api/ShapesApi~slidesShapesGetIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SlideShapes} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Shapes: Get by Id
     * Get by Id: Use this method to retrieve a Shapes object by its primary key (id)
     * @param {String} id An Id of the respository DTO elemennt
     * @param {module:api/ShapesApi~slidesShapesGetIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SlideShapes}
     */
    slidesShapesGetId(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling slidesShapesGetId");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = SlideShapes;
      return this.apiClient.callApi(
        '/Shapes/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the slidesShapesOpenofficexmlGetIdUpdated operation.
     * @callback module:api/ShapesApi~slidesShapesOpenofficexmlGetIdUpdatedCallback
     * @param {String} error Error message, if any.
     * @param {module:model/OoxmlDTO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Slides: Get Underlying Xml
     * Return the subset of the xml content from within the latest edited version of the OpenXmlDocument from this Slide object.  The returned xml data conforms to the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm).  Use this endpoint a starting point for building client-side extensions that modify Presalytics widgets containing Slide objects.
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Boolean} [updated = true)] Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default)
     * @param {module:api/ShapesApi~slidesShapesOpenofficexmlGetIdUpdatedCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/OoxmlDTO}
     */
    slidesShapesOpenofficexmlGetIdUpdated(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling slidesShapesOpenofficexmlGetIdUpdated");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'updated': opts['updated']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = OoxmlDTO;
      return this.apiClient.callApi(
        '/Shapes/OpenOfficeXml/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the slidesShapesOpenofficexmlPutId operation.
     * @callback module:api/ShapesApi~slidesShapesOpenofficexmlPutIdCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Slides: Modify Underlying Xml
     * Directly eidt the underlying xml of a Slide object within an OpenOpenXml (e.g. Excel, Powerpoint) document. This endpoint will validatate the submitted xml against the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm) prior to saving modification.  Invalid xml will rejected by this endpoint and a (hopefully) helpful error message will be returned.  Use this endpoint for client-side automation of modifications ot Slide objects.
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {module:model/OoxmlDTO} [ooxmlDTO] 
     * @param {module:api/ShapesApi~slidesShapesOpenofficexmlPutIdCallback} callback The callback function, accepting three arguments: error, data, response
     */
    slidesShapesOpenofficexmlPutId(id, opts, callback) {
      opts = opts || {};
      let postBody = opts['ooxmlDTO'];
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling slidesShapesOpenofficexmlPutId");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/*+json', 'application/json', 'application/json-patch+json', 'text/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/Shapes/OpenOfficeXml/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the slidesShapesSvgGetIdUseCache operation.
     * @callback module:api/ShapesApi~slidesShapesSvgGetIdUseCacheCallback
     * @param {String} error Error message, if any.
     * @param {File} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Slides: Get Svg file
     * This endpoint is helpful for rending this Slide as an svg or image object that can then be rendered in a story, dashboard or website.
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Boolean} [useCache = false)] Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false)
     * @param {module:api/ShapesApi~slidesShapesSvgGetIdUseCacheCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link File}
     */
    slidesShapesSvgGetIdUseCache(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling slidesShapesSvgGetIdUseCache");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'use_cache': opts['useCache']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['image/svg+xml', 'application/json'];
      let returnType = File;
      return this.apiClient.callApi(
        '/Shapes/Svg/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
