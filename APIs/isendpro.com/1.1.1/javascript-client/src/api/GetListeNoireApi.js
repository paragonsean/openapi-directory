/**
 * API iSendPro
 * [1] Liste des fonctionnalités : - envoi de SMS à un ou plusieurs destinataires, - lookup HLR, - récupération des récapitulatifs de campagne, - gestion des répertoires, - ajout en liste noire. - comptage du nombre de caractères des SMS  [2] Pour utiliser cette API vous devez: - Créer un compte iSendPro sur https://isendpro.com/ - Créditer votre compte      - Remarque: obtention d'un crédit de test possible sous conditions - Noter votre clé de compte (keyid)   - Elle vous sera indispensable à l'utilisation de l'API   - Vous pouvez la trouver dans le rubrique mon \"compte\", sous-rubrique \"mon API\" - Configurer le contrôle IP   - Le contrôle IP est configurable dans le rubrique mon \"compte\", sous-rubrique \"mon API\"   - Il s'agit d'un système de liste blanche, vous devez entrer les IP utilisées pour appeler l'API   - Vous pouvez également désactiver totalement le contrôle IP 
 *
 * The version of the OpenAPI document: 1.1.1
 * Contact: support@isendpro.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Erreur from '../model/Erreur';

/**
* GetListeNoire service.
* @module api/GetListeNoireApi
* @version 1.1.1
*/
export default class GetListeNoireApi {

    /**
    * Constructs a new GetListeNoireApi. 
    * @alias module:api/GetListeNoireApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getListeNoire operation.
     * @callback module:api/GetListeNoireApi~getListeNoireCallback
     * @param {String} error Error message, if any.
     * @param {File} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retourne le liste noire
     * Retourne un fichier csv zippé contenant la liste noire
     * @param {String} keyid Clé API
     * @param {module:model/String} getListeNoire Doit valoir \"1\"
     * @param {module:api/GetListeNoireApi~getListeNoireCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link File}
     */
    getListeNoire(keyid, getListeNoire, callback) {
      let postBody = null;
      // verify the required parameter 'keyid' is set
      if (keyid === undefined || keyid === null) {
        throw new Error("Missing the required parameter 'keyid' when calling getListeNoire");
      }
      // verify the required parameter 'getListeNoire' is set
      if (getListeNoire === undefined || getListeNoire === null) {
        throw new Error("Missing the required parameter 'getListeNoire' when calling getListeNoire");
      }

      let pathParams = {
      };
      let queryParams = {
        'keyid': keyid,
        'getListeNoire': getListeNoire
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = File;
      return this.apiClient.callApi(
        '/getlistenoire', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
