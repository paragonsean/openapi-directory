/**
 * Hubhopper Partner Integration API(s) - Production
 * This is an interactive document explaining the API(s) that could be used to fetch data from [Hubhopper](https://hubhopper.com). Use the api key provided to authorize `x-api-key` and test the API(s). The output data models are also available for reference.
 *
 * The version of the OpenAPI document: v5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Error from '../model/Error';
import PodcastEpisodeList from '../model/PodcastEpisodeList';
import PodcastList from '../model/PodcastList';
import SinglePodcast from '../model/SinglePodcast';

/**
* Podcast service.
* @module api/PodcastApi
* @version v5
*/
export default class PodcastApi {

    /**
    * Constructs a new PodcastApi. 
    * @alias module:api/PodcastApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the podcastsGet operation.
     * @callback module:api/PodcastApi~podcastsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PodcastList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the list of all podcasts.
     * @param {Object} opts Optional parameters
     * @param {String} [page] Provide the page number to fetch.
     * @param {String} [pageSize] Provide the size of the page to fetch.
     * @param {String} [order] Order the items by 'newest' | 'random'
     * @param {String} [filters] Takes filters like 'lang' in a url encoded json.  Example: 1)Single -> &nbsp;&nbsp;&nbsp;&nbsp; var filterJson = {\"lang\":[\"en\"]}; &nbsp;&nbsp;&nbsp;&nbsp; var url = baseUrl+'?'+filters=enocdeURI(JSON.stringify(filterJson)); 2)Multiple -> &nbsp;&nbsp;&nbsp;&nbsp; var filterJson = {\"lang\":[\"en\",\"hi\"]}; &nbsp;&nbsp;&nbsp;&nbsp; var url = baseUrl+'?'+filters=enocdeURI(JSON.stringify(filterJson));
     * @param {module:api/PodcastApi~podcastsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PodcastList}
     */
    podcastsGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'page': opts['page'],
        'pageSize': opts['pageSize'],
        'order': opts['order'],
        'filters': opts['filters']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['partner_id', 'api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PodcastList;
      return this.apiClient.callApi(
        '/podcasts', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the podcastsPodcastIdEpisodesGet operation.
     * @callback module:api/PodcastApi~podcastsPodcastIdEpisodesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PodcastEpisodeList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a list of all episodes under a podcast.
     * @param {String} podcastId Unique qualifier for a podcast.
     * @param {Object} opts Optional parameters
     * @param {String} [page] Provide the page number to fetch.
     * @param {String} [pageSize] Provide the size of the page to fetch.
     * @param {String} [order] Order the items by 'newest' | 'random'
     * @param {String} [filters] Takes filters like 'lang' in a url encoded json.  Example: 1)Single -> &nbsp;&nbsp;&nbsp;&nbsp; var filterJson = {\"lang\":[\"en\"]}; &nbsp;&nbsp;&nbsp;&nbsp; var url = baseUrl+'?'+filters=enocdeURI(JSON.stringify(filterJson)); 2)Multiple -> &nbsp;&nbsp;&nbsp;&nbsp; var filterJson = {\"lang\":[\"en\",\"hi\"]}; &nbsp;&nbsp;&nbsp;&nbsp; var url = baseUrl+'?'+filters=enocdeURI(JSON.stringify(filterJson));
     * @param {module:api/PodcastApi~podcastsPodcastIdEpisodesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PodcastEpisodeList}
     */
    podcastsPodcastIdEpisodesGet(podcastId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'podcastId' is set
      if (podcastId === undefined || podcastId === null) {
        throw new Error("Missing the required parameter 'podcastId' when calling podcastsPodcastIdEpisodesGet");
      }

      let pathParams = {
        'podcastId': podcastId
      };
      let queryParams = {
        'page': opts['page'],
        'pageSize': opts['pageSize'],
        'order': opts['order'],
        'filters': opts['filters']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['partner_id', 'api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PodcastEpisodeList;
      return this.apiClient.callApi(
        '/podcasts/{podcastId}/episodes', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the podcastsPodcastIdGet operation.
     * @callback module:api/PodcastApi~podcastsPodcastIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SinglePodcast} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a single Podcast.
     * @param {String} podcastId Unique qualifier for a podcast.
     * @param {module:api/PodcastApi~podcastsPodcastIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SinglePodcast}
     */
    podcastsPodcastIdGet(podcastId, callback) {
      let postBody = null;
      // verify the required parameter 'podcastId' is set
      if (podcastId === undefined || podcastId === null) {
        throw new Error("Missing the required parameter 'podcastId' when calling podcastsPodcastIdGet");
      }

      let pathParams = {
        'podcastId': podcastId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['partner_id', 'api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = SinglePodcast;
      return this.apiClient.callApi(
        '/podcasts/{podcastId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
