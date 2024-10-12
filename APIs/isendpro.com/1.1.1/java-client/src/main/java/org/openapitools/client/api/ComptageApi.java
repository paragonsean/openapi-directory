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


import org.openapitools.client.model.ComptageReponse;
import org.openapitools.client.model.ComptageRequest;
import org.openapitools.client.model.Erreur;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ComptageApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ComptageApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ComptageApi(ApiClient apiClient) {
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
     * Build call for comptage
     * @param comptageRequest sms request (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Reponse OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Dysfonctionnement </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call comptageCall(ComptageRequest comptageRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = comptageRequest;

        // create path and map variables
        String localVarPath = "/comptage";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json",
            "etat"
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
    private okhttp3.Call comptageValidateBeforeCall(ComptageRequest comptageRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'comptageRequest' is set
        if (comptageRequest == null) {
            throw new ApiException("Missing the required parameter 'comptageRequest' when calling comptage(Async)");
        }

        return comptageCall(comptageRequest, _callback);

    }

    /**
     * Compter le nombre de caractère 
     * Compte le nombre de SMS necessaire à un envoi
     * @param comptageRequest sms request (required)
     * @return ComptageReponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Reponse OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Dysfonctionnement </td><td>  -  </td></tr>
     </table>
     */
    public ComptageReponse comptage(ComptageRequest comptageRequest) throws ApiException {
        ApiResponse<ComptageReponse> localVarResp = comptageWithHttpInfo(comptageRequest);
        return localVarResp.getData();
    }

    /**
     * Compter le nombre de caractère 
     * Compte le nombre de SMS necessaire à un envoi
     * @param comptageRequest sms request (required)
     * @return ApiResponse&lt;ComptageReponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Reponse OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Dysfonctionnement </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ComptageReponse> comptageWithHttpInfo(ComptageRequest comptageRequest) throws ApiException {
        okhttp3.Call localVarCall = comptageValidateBeforeCall(comptageRequest, null);
        Type localVarReturnType = new TypeToken<ComptageReponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Compter le nombre de caractère  (asynchronously)
     * Compte le nombre de SMS necessaire à un envoi
     * @param comptageRequest sms request (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Reponse OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Dysfonctionnement </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call comptageAsync(ComptageRequest comptageRequest, final ApiCallback<ComptageReponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = comptageValidateBeforeCall(comptageRequest, _callback);
        Type localVarReturnType = new TypeToken<ComptageReponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
