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

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Erreur;
import org.openapitools.client.model.REPERTOIREcreatereponse;
import org.openapitools.client.model.REPERTOIREcreaterequest;
import org.openapitools.client.model.REPERTOIREmodifreponse;
import org.openapitools.client.model.REPERTOIREmodifrequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for RepertoireApi
 */
@Disabled
public class RepertoireApiTest {

    private final RepertoireApi api = new RepertoireApi();

    /**
     * Gestion repertoire (modification)
     *
     * Ajoute ou supprime une liste de numéros à un répertoire existant.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void repertoireTest() throws ApiException {
        REPERTOIREmodifrequest rePERTOIREmodifrequest = null;
        REPERTOIREmodifreponse response = api.repertoire(rePERTOIREmodifrequest);
        // TODO: test validations
    }

    /**
     * Gestion repertoire (creation)
     *
     * Cree un nouveau répertoire et retourne son identifiant. Cet identifiant pourra être utilisé pour ajouter ou supprimer des numéros via l&#39;API.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void repertoireCreaTest() throws ApiException {
        REPERTOIREcreaterequest rePERTOIREcreaterequest = null;
        REPERTOIREcreatereponse response = api.repertoireCrea(rePERTOIREcreaterequest);
        // TODO: test validations
    }

}
