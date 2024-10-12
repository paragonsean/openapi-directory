/**
 * LoL v3 Stats
 * LoL v3 Stats
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Champion model module.
 * @module model/Champion
 * @version 1.0
 */
class Champion {
    /**
     * Constructs a new <code>Champion</code>.
     * @alias module:model/Champion
     */
    constructor() { 
        
        Champion.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Champion</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Champion} obj Optional instance to populate.
     * @return {module:model/Champion} The populated <code>Champion</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Champion();

            if (data.hasOwnProperty('Armor')) {
                obj['Armor'] = ApiClient.convertToType(data['Armor'], 'Number');
            }
            if (data.hasOwnProperty('ArmorPerLevel')) {
                obj['ArmorPerLevel'] = ApiClient.convertToType(data['ArmorPerLevel'], 'Number');
            }
            if (data.hasOwnProperty('Attack')) {
                obj['Attack'] = ApiClient.convertToType(data['Attack'], 'Number');
            }
            if (data.hasOwnProperty('AttackDamage')) {
                obj['AttackDamage'] = ApiClient.convertToType(data['AttackDamage'], 'Number');
            }
            if (data.hasOwnProperty('AttackDamagePerLevel')) {
                obj['AttackDamagePerLevel'] = ApiClient.convertToType(data['AttackDamagePerLevel'], 'Number');
            }
            if (data.hasOwnProperty('AttackRange')) {
                obj['AttackRange'] = ApiClient.convertToType(data['AttackRange'], 'Number');
            }
            if (data.hasOwnProperty('AttackSpeedOffset')) {
                obj['AttackSpeedOffset'] = ApiClient.convertToType(data['AttackSpeedOffset'], 'Number');
            }
            if (data.hasOwnProperty('ChampionId')) {
                obj['ChampionId'] = ApiClient.convertToType(data['ChampionId'], 'Number');
            }
            if (data.hasOwnProperty('Defense')) {
                obj['Defense'] = ApiClient.convertToType(data['Defense'], 'Number');
            }
            if (data.hasOwnProperty('Difficulty')) {
                obj['Difficulty'] = ApiClient.convertToType(data['Difficulty'], 'Number');
            }
            if (data.hasOwnProperty('Hp')) {
                obj['Hp'] = ApiClient.convertToType(data['Hp'], 'Number');
            }
            if (data.hasOwnProperty('HpRegen')) {
                obj['HpRegen'] = ApiClient.convertToType(data['HpRegen'], 'Number');
            }
            if (data.hasOwnProperty('HpRegenPerLevel')) {
                obj['HpRegenPerLevel'] = ApiClient.convertToType(data['HpRegenPerLevel'], 'Number');
            }
            if (data.hasOwnProperty('HpUpPerLevel')) {
                obj['HpUpPerLevel'] = ApiClient.convertToType(data['HpUpPerLevel'], 'Number');
            }
            if (data.hasOwnProperty('Magic')) {
                obj['Magic'] = ApiClient.convertToType(data['Magic'], 'Number');
            }
            if (data.hasOwnProperty('MoveSpeed')) {
                obj['MoveSpeed'] = ApiClient.convertToType(data['MoveSpeed'], 'Number');
            }
            if (data.hasOwnProperty('Mp')) {
                obj['Mp'] = ApiClient.convertToType(data['Mp'], 'Number');
            }
            if (data.hasOwnProperty('MpRegen')) {
                obj['MpRegen'] = ApiClient.convertToType(data['MpRegen'], 'Number');
            }
            if (data.hasOwnProperty('MpRegenPerLevel')) {
                obj['MpRegenPerLevel'] = ApiClient.convertToType(data['MpRegenPerLevel'], 'Number');
            }
            if (data.hasOwnProperty('MpUpPerLevel')) {
                obj['MpUpPerLevel'] = ApiClient.convertToType(data['MpUpPerLevel'], 'Number');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('SpellBlock')) {
                obj['SpellBlock'] = ApiClient.convertToType(data['SpellBlock'], 'Number');
            }
            if (data.hasOwnProperty('SpellBlockPerLevel')) {
                obj['SpellBlockPerLevel'] = ApiClient.convertToType(data['SpellBlockPerLevel'], 'Number');
            }
            if (data.hasOwnProperty('Title')) {
                obj['Title'] = ApiClient.convertToType(data['Title'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Champion</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Champion</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['Title'] && !(typeof data['Title'] === 'string' || data['Title'] instanceof String)) {
            throw new Error("Expected the field `Title` to be a primitive type in the JSON string but got " + data['Title']);
        }

        return true;
    }


}



/**
 * @member {Number} Armor
 */
Champion.prototype['Armor'] = undefined;

/**
 * @member {Number} ArmorPerLevel
 */
Champion.prototype['ArmorPerLevel'] = undefined;

/**
 * @member {Number} Attack
 */
Champion.prototype['Attack'] = undefined;

/**
 * @member {Number} AttackDamage
 */
Champion.prototype['AttackDamage'] = undefined;

/**
 * @member {Number} AttackDamagePerLevel
 */
Champion.prototype['AttackDamagePerLevel'] = undefined;

/**
 * @member {Number} AttackRange
 */
Champion.prototype['AttackRange'] = undefined;

/**
 * @member {Number} AttackSpeedOffset
 */
Champion.prototype['AttackSpeedOffset'] = undefined;

/**
 * @member {Number} ChampionId
 */
Champion.prototype['ChampionId'] = undefined;

/**
 * @member {Number} Defense
 */
Champion.prototype['Defense'] = undefined;

/**
 * @member {Number} Difficulty
 */
Champion.prototype['Difficulty'] = undefined;

/**
 * @member {Number} Hp
 */
Champion.prototype['Hp'] = undefined;

/**
 * @member {Number} HpRegen
 */
Champion.prototype['HpRegen'] = undefined;

/**
 * @member {Number} HpRegenPerLevel
 */
Champion.prototype['HpRegenPerLevel'] = undefined;

/**
 * @member {Number} HpUpPerLevel
 */
Champion.prototype['HpUpPerLevel'] = undefined;

/**
 * @member {Number} Magic
 */
Champion.prototype['Magic'] = undefined;

/**
 * @member {Number} MoveSpeed
 */
Champion.prototype['MoveSpeed'] = undefined;

/**
 * @member {Number} Mp
 */
Champion.prototype['Mp'] = undefined;

/**
 * @member {Number} MpRegen
 */
Champion.prototype['MpRegen'] = undefined;

/**
 * @member {Number} MpRegenPerLevel
 */
Champion.prototype['MpRegenPerLevel'] = undefined;

/**
 * @member {Number} MpUpPerLevel
 */
Champion.prototype['MpUpPerLevel'] = undefined;

/**
 * @member {String} Name
 */
Champion.prototype['Name'] = undefined;

/**
 * @member {Number} SpellBlock
 */
Champion.prototype['SpellBlock'] = undefined;

/**
 * @member {Number} SpellBlockPerLevel
 */
Champion.prototype['SpellBlockPerLevel'] = undefined;

/**
 * @member {String} Title
 */
Champion.prototype['Title'] = undefined;






export default Champion;

