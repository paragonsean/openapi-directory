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

import ApiClient from '../ApiClient';
import LISTENOIREReponseEtatEtat from './LISTENOIREReponseEtatEtat';

/**
 * The LISTENOIREReponseEtat model module.
 * @module model/LISTENOIREReponseEtat
 * @version 1.1.1
 */
class LISTENOIREReponseEtat {
    /**
     * Constructs a new <code>LISTENOIREReponseEtat</code>.
     * @alias module:model/LISTENOIREReponseEtat
     * @param etat {Array.<module:model/LISTENOIREReponseEtatEtat>} 
     */
    constructor(etat) { 
        
        LISTENOIREReponseEtat.initialize(this, etat);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, etat) { 
        obj['etat'] = etat;
    }

    /**
     * Constructs a <code>LISTENOIREReponseEtat</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LISTENOIREReponseEtat} obj Optional instance to populate.
     * @return {module:model/LISTENOIREReponseEtat} The populated <code>LISTENOIREReponseEtat</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LISTENOIREReponseEtat();

            if (data.hasOwnProperty('etat')) {
                obj['etat'] = ApiClient.convertToType(data['etat'], [LISTENOIREReponseEtatEtat]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LISTENOIREReponseEtat</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LISTENOIREReponseEtat</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of LISTENOIREReponseEtat.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['etat']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['etat'])) {
                throw new Error("Expected the field `etat` to be an array in the JSON data but got " + data['etat']);
            }
            // validate the optional field `etat` (array)
            for (const item of data['etat']) {
                LISTENOIREReponseEtatEtat.validateJSON(item);
            };
        }

        return true;
    }


}

LISTENOIREReponseEtat.RequiredProperties = ["etat"];

/**
 * @member {Array.<module:model/LISTENOIREReponseEtatEtat>} etat
 */
LISTENOIREReponseEtat.prototype['etat'] = undefined;






export default LISTENOIREReponseEtat;

