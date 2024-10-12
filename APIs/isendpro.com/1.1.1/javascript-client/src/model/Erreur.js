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
import ErreurEtat from './ErreurEtat';

/**
 * The Erreur model module.
 * @module model/Erreur
 * @version 1.1.1
 */
class Erreur {
    /**
     * Constructs a new <code>Erreur</code>.
     * @alias module:model/Erreur
     */
    constructor() { 
        
        Erreur.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Erreur</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Erreur} obj Optional instance to populate.
     * @return {module:model/Erreur} The populated <code>Erreur</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Erreur();

            if (data.hasOwnProperty('etat')) {
                obj['etat'] = ErreurEtat.constructFromObject(data['etat']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Erreur</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Erreur</code>.
     */
    static validateJSON(data) {
        // validate the optional field `etat`
        if (data['etat']) { // data not null
          ErreurEtat.validateJSON(data['etat']);
        }

        return true;
    }


}



/**
 * @member {module:model/ErreurEtat} etat
 */
Erreur.prototype['etat'] = undefined;






export default Erreur;

