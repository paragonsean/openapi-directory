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

/**
 * The REPERTOIREmodifreponseEtatEtat model module.
 * @module model/REPERTOIREmodifreponseEtatEtat
 * @version 1.1.1
 */
class REPERTOIREmodifreponseEtatEtat {
    /**
     * Constructs a new <code>REPERTOIREmodifreponseEtatEtat</code>.
     * Tableau de code retour. Si succès, un code retour distinct par numéro soumis.
     * @alias module:model/REPERTOIREmodifreponseEtatEtat
     * @param code {String} Code retour. Voir \"tableau des code retour\" dans l'annexe de la documentation
     */
    constructor(code) { 
        
        REPERTOIREmodifreponseEtatEtat.initialize(this, code);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, code) { 
        obj['code'] = code;
    }

    /**
     * Constructs a <code>REPERTOIREmodifreponseEtatEtat</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/REPERTOIREmodifreponseEtatEtat} obj Optional instance to populate.
     * @return {module:model/REPERTOIREmodifreponseEtatEtat} The populated <code>REPERTOIREmodifreponseEtatEtat</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new REPERTOIREmodifreponseEtatEtat();

            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'String');
            }
            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
            if (data.hasOwnProperty('repertoireId')) {
                obj['repertoireId'] = ApiClient.convertToType(data['repertoireId'], 'String');
            }
            if (data.hasOwnProperty('tel')) {
                obj['tel'] = ApiClient.convertToType(data['tel'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>REPERTOIREmodifreponseEtatEtat</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>REPERTOIREmodifreponseEtatEtat</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of REPERTOIREmodifreponseEtatEtat.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['code'] && !(typeof data['code'] === 'string' || data['code'] instanceof String)) {
            throw new Error("Expected the field `code` to be a primitive type in the JSON string but got " + data['code']);
        }
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }
        // ensure the json data is a string
        if (data['repertoireId'] && !(typeof data['repertoireId'] === 'string' || data['repertoireId'] instanceof String)) {
            throw new Error("Expected the field `repertoireId` to be a primitive type in the JSON string but got " + data['repertoireId']);
        }
        // ensure the json data is a string
        if (data['tel'] && !(typeof data['tel'] === 'string' || data['tel'] instanceof String)) {
            throw new Error("Expected the field `tel` to be a primitive type in the JSON string but got " + data['tel']);
        }

        return true;
    }


}

REPERTOIREmodifreponseEtatEtat.RequiredProperties = ["code"];

/**
 * Code retour. Voir \"tableau des code retour\" dans l'annexe de la documentation
 * @member {String} code
 */
REPERTOIREmodifreponseEtatEtat.prototype['code'] = undefined;

/**
 * Libellé associé au code retour.
 * @member {String} message
 */
REPERTOIREmodifreponseEtatEtat.prototype['message'] = undefined;

/**
 * repertoireId passé en argument lors de l'appel
 * @member {String} repertoireId
 */
REPERTOIREmodifreponseEtatEtat.prototype['repertoireId'] = undefined;

/**
 * Numéro de téléphone
 * @member {String} tel
 */
REPERTOIREmodifreponseEtatEtat.prototype['tel'] = undefined;






export default REPERTOIREmodifreponseEtatEtat;

