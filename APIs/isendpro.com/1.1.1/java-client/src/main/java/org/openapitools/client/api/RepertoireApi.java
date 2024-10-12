/*
 * API iSendPro
 * [1] Liste des fonctionnalités : - envoi de SMS à un ou plusieurs destinataires, - lookup HLR, - récupération des récapitulatifs de campagne, - gestion des répertoires, - ajout en liste noire. - comptage du nombre de caractères des SMS  [2] Pour utiliser cette API vous devez: - Créer un compte iSendPro sur https://isendpro.com/ - Créditer votre compte      - Remarque: obtention d'un crédit de test possible sous conditions - Noter votre clé de compte (keyid)   - Elle vous sera indispensable à l'utilisation de l'API   - Vous pouvez la trouver dans le rubrique mon \"compte\", sous-rubrique \"mon API\" - Configurer le contrôle IP   - Le contrôle IP est configurable dans le rubrique mon \"compte\", sous-rubrique \"mon API\"   - Il s'agit d'un système de liste blanche, vous devez entrer les IP utilisées pour appeler l'API   - Vous pouvez également désactiver totalement le contrôle IP 
 *
 * The version of the OpenAPI document: 1.1.1
 * Contact: support@isendpro.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import org.openapitools.client.model.Erreur;
import org.openapitools.client.model.REPERTOIREcreatereponse;
import org.openapitools.client.model.REPERTOIREcreaterequest;
import org.openapitools.client.model.REPERTOIREmodifreponse;
import org.openapitools.client.model.REPERTOIREmodifrequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class RepertoireApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public RepertoireApi() {
        this(Configuration.getDefaultApiClient());
    }

    public RepertoireApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for repertoire
     * @param rePERTOIREmodifrequest Requête de creation repertoire (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful response </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Erreur </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call repertoireCall(REPERTOIREmodifrequest rePERTOIREmodifrequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = rePERTOIREmodifrequest;

        // create path and map variables
        String localVarPath = "/repertoire";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call repertoireValidateBeforeCall(REPERTOIREmodifrequest rePERTOIREmodifrequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'rePERTOIREmodifrequest' is set
        if (rePERTOIREmodifrequest == null) {
            throw new ApiException("Missing the required parameter 'rePERTOIREmodifrequest' when calling repertoire(Async)");
        }

        return repertoireCall(rePERTOIREmodifrequest, _callback);

    }

    /**
     * Gestion repertoire (modification)
     * Ajoute ou supprime une liste de numéros à un répertoire existant.
     * @param rePERTOIREmodifrequest Requête de creation repertoire (required)
     * @return REPERTOIREmodifreponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful response </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Erreur </td><td>  -  </td></tr>
     </table>
     */
    public REPERTOIREmodifreponse repertoire(REPERTOIREmodifrequest rePERTOIREmodifrequest) throws ApiException {
        ApiResponse<REPERTOIREmodifreponse> localVarResp = repertoireWithHttpInfo(rePERTOIREmodifrequest);
        return localVarResp.getData();
    }

    /**
     * Gestion repertoire (modification)
     * Ajoute ou supprime une liste de numéros à un répertoire existant.
     * @param rePERTOIREmodifrequest Requête de creation repertoire (required)
     * @return ApiResponse&lt;REPERTOIREmodifreponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful response </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Erreur </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<REPERTOIREmodifreponse> repertoireWithHttpInfo(REPERTOIREmodifrequest rePERTOIREmodifrequest) throws ApiException {
        okhttp3.Call localVarCall = repertoireValidateBeforeCall(rePERTOIREmodifrequest, null);
        Type localVarReturnType = new TypeToken<REPERTOIREmodifreponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Gestion repertoire (modification) (asynchronously)
     * Ajoute ou supprime une liste de numéros à un répertoire existant.
     * @param rePERTOIREmodifrequest Requête de creation repertoire (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful response </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Erreur </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call repertoireAsync(REPERTOIREmodifrequest rePERTOIREmodifrequest, final ApiCallback<REPERTOIREmodifreponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = repertoireValidateBeforeCall(rePERTOIREmodifrequest, _callback);
        Type localVarReturnType = new TypeToken<REPERTOIREmodifreponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for repertoireCrea
     * @param rePERTOIREcreaterequest Creation repertoire (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful response </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Erreur </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call repertoireCreaCall(REPERTOIREcreaterequest rePERTOIREcreaterequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = rePERTOIREcreaterequest;

        // create path and map variables
        String localVarPath = "/repertoire";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call repertoireCreaValidateBeforeCall(REPERTOIREcreaterequest rePERTOIREcreaterequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'rePERTOIREcreaterequest' is set
        if (rePERTOIREcreaterequest == null) {
            throw new ApiException("Missing the required parameter 'rePERTOIREcreaterequest' when calling repertoireCrea(Async)");
        }

        return repertoireCreaCall(rePERTOIREcreaterequest, _callback);

    }

    /**
     * Gestion repertoire (creation)
     * Cree un nouveau répertoire et retourne son identifiant. Cet identifiant pourra être utilisé pour ajouter ou supprimer des numéros via l&#39;API.
     * @param rePERTOIREcreaterequest Creation repertoire (required)
     * @return REPERTOIREcreatereponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful response </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Erreur </td><td>  -  </td></tr>
     </table>
     */
    public REPERTOIREcreatereponse repertoireCrea(REPERTOIREcreaterequest rePERTOIREcreaterequest) throws ApiException {
        ApiResponse<REPERTOIREcreatereponse> localVarResp = repertoireCreaWithHttpInfo(rePERTOIREcreaterequest);
        return localVarResp.getData();
    }

    /**
     * Gestion repertoire (creation)
     * Cree un nouveau répertoire et retourne son identifiant. Cet identifiant pourra être utilisé pour ajouter ou supprimer des numéros via l&#39;API.
     * @param rePERTOIREcreaterequest Creation repertoire (required)
     * @return ApiResponse&lt;REPERTOIREcreatereponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful response </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Erreur </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<REPERTOIREcreatereponse> repertoireCreaWithHttpInfo(REPERTOIREcreaterequest rePERTOIREcreaterequest) throws ApiException {
        okhttp3.Call localVarCall = repertoireCreaValidateBeforeCall(rePERTOIREcreaterequest, null);
        Type localVarReturnType = new TypeToken<REPERTOIREcreatereponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Gestion repertoire (creation) (asynchronously)
     * Cree un nouveau répertoire et retourne son identifiant. Cet identifiant pourra être utilisé pour ajouter ou supprimer des numéros via l&#39;API.
     * @param rePERTOIREcreaterequest Creation repertoire (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful response </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Erreur </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call repertoireCreaAsync(REPERTOIREcreaterequest rePERTOIREcreaterequest, final ApiCallback<REPERTOIREcreatereponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = repertoireCreaValidateBeforeCall(rePERTOIREcreaterequest, _callback);
        Type localVarReturnType = new TypeToken<REPERTOIREcreatereponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
