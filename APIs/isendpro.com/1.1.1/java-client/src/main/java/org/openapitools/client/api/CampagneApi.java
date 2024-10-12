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
import java.io.File;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CampagneApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CampagneApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CampagneApi(ApiClient apiClient) {
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
     * Build call for getCampagne
     * @param keyid Clé API (required)
     * @param rapportCampagne Doit valoir \&quot;1\&quot; (required)
     * @param dateDeb date de debut au format YYYY-MM-DD hh:mm (required)
     * @param dateFin date de fin au format YYYY-MM-DD hh:mm (required)
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
    public okhttp3.Call getCampagneCall(String keyid, String rapportCampagne, String dateDeb, String dateFin, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/campagne";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (keyid != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("keyid", keyid));
        }

        if (rapportCampagne != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("rapportCampagne", rapportCampagne));
        }

        if (dateDeb != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_deb", dateDeb));
        }

        if (dateFin != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date_fin", dateFin));
        }

        final String[] localVarAccepts = {
            "application/json",
            "file"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getCampagneValidateBeforeCall(String keyid, String rapportCampagne, String dateDeb, String dateFin, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'keyid' is set
        if (keyid == null) {
            throw new ApiException("Missing the required parameter 'keyid' when calling getCampagne(Async)");
        }

        // verify the required parameter 'rapportCampagne' is set
        if (rapportCampagne == null) {
            throw new ApiException("Missing the required parameter 'rapportCampagne' when calling getCampagne(Async)");
        }

        // verify the required parameter 'dateDeb' is set
        if (dateDeb == null) {
            throw new ApiException("Missing the required parameter 'dateDeb' when calling getCampagne(Async)");
        }

        // verify the required parameter 'dateFin' is set
        if (dateFin == null) {
            throw new ApiException("Missing the required parameter 'dateFin' when calling getCampagne(Async)");
        }

        return getCampagneCall(keyid, rapportCampagne, dateDeb, dateFin, _callback);

    }

    /**
     * Retourne les SMS envoyés sur une période donnée
     * Retourne les SMS envoyés sur une période donnée en fonction d&#39;une date de début et d&#39;une date de fin.   Les dates sont au format YYYY-MM-DD hh:mm.   Le fichier rapport de campagne est sous la forme d&#39;un fichier zip + contenant un fichier csv contenant le détail des envois. 
     * @param keyid Clé API (required)
     * @param rapportCampagne Doit valoir \&quot;1\&quot; (required)
     * @param dateDeb date de debut au format YYYY-MM-DD hh:mm (required)
     * @param dateFin date de fin au format YYYY-MM-DD hh:mm (required)
     * @return File
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful response </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Erreur </td><td>  -  </td></tr>
     </table>
     */
    public File getCampagne(String keyid, String rapportCampagne, String dateDeb, String dateFin) throws ApiException {
        ApiResponse<File> localVarResp = getCampagneWithHttpInfo(keyid, rapportCampagne, dateDeb, dateFin);
        return localVarResp.getData();
    }

    /**
     * Retourne les SMS envoyés sur une période donnée
     * Retourne les SMS envoyés sur une période donnée en fonction d&#39;une date de début et d&#39;une date de fin.   Les dates sont au format YYYY-MM-DD hh:mm.   Le fichier rapport de campagne est sous la forme d&#39;un fichier zip + contenant un fichier csv contenant le détail des envois. 
     * @param keyid Clé API (required)
     * @param rapportCampagne Doit valoir \&quot;1\&quot; (required)
     * @param dateDeb date de debut au format YYYY-MM-DD hh:mm (required)
     * @param dateFin date de fin au format YYYY-MM-DD hh:mm (required)
     * @return ApiResponse&lt;File&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful response </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Erreur </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<File> getCampagneWithHttpInfo(String keyid, String rapportCampagne, String dateDeb, String dateFin) throws ApiException {
        okhttp3.Call localVarCall = getCampagneValidateBeforeCall(keyid, rapportCampagne, dateDeb, dateFin, null);
        Type localVarReturnType = new TypeToken<File>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retourne les SMS envoyés sur une période donnée (asynchronously)
     * Retourne les SMS envoyés sur une période donnée en fonction d&#39;une date de début et d&#39;une date de fin.   Les dates sont au format YYYY-MM-DD hh:mm.   Le fichier rapport de campagne est sous la forme d&#39;un fichier zip + contenant un fichier csv contenant le détail des envois. 
     * @param keyid Clé API (required)
     * @param rapportCampagne Doit valoir \&quot;1\&quot; (required)
     * @param dateDeb date de debut au format YYYY-MM-DD hh:mm (required)
     * @param dateFin date de fin au format YYYY-MM-DD hh:mm (required)
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
    public okhttp3.Call getCampagneAsync(String keyid, String rapportCampagne, String dateDeb, String dateFin, final ApiCallback<File> _callback) throws ApiException {

        okhttp3.Call localVarCall = getCampagneValidateBeforeCall(keyid, rapportCampagne, dateDeb, dateFin, _callback);
        Type localVarReturnType = new TypeToken<File>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
