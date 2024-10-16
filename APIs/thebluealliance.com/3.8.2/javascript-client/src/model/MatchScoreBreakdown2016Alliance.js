/**
 * The Blue Alliance API v3
 * # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).
 *
 * The version of the OpenAPI document: 3.8.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The MatchScoreBreakdown2016Alliance model module.
 * @module model/MatchScoreBreakdown2016Alliance
 * @version 3.8.2
 */
class MatchScoreBreakdown2016Alliance {
    /**
     * Constructs a new <code>MatchScoreBreakdown2016Alliance</code>.
     * @alias module:model/MatchScoreBreakdown2016Alliance
     */
    constructor() { 
        
        MatchScoreBreakdown2016Alliance.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>MatchScoreBreakdown2016Alliance</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MatchScoreBreakdown2016Alliance} obj Optional instance to populate.
     * @return {module:model/MatchScoreBreakdown2016Alliance} The populated <code>MatchScoreBreakdown2016Alliance</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MatchScoreBreakdown2016Alliance();

            if (data.hasOwnProperty('adjustPoints')) {
                obj['adjustPoints'] = ApiClient.convertToType(data['adjustPoints'], 'Number');
            }
            if (data.hasOwnProperty('autoBoulderPoints')) {
                obj['autoBoulderPoints'] = ApiClient.convertToType(data['autoBoulderPoints'], 'Number');
            }
            if (data.hasOwnProperty('autoBouldersHigh')) {
                obj['autoBouldersHigh'] = ApiClient.convertToType(data['autoBouldersHigh'], 'Number');
            }
            if (data.hasOwnProperty('autoBouldersLow')) {
                obj['autoBouldersLow'] = ApiClient.convertToType(data['autoBouldersLow'], 'Number');
            }
            if (data.hasOwnProperty('autoCrossingPoints')) {
                obj['autoCrossingPoints'] = ApiClient.convertToType(data['autoCrossingPoints'], 'Number');
            }
            if (data.hasOwnProperty('autoPoints')) {
                obj['autoPoints'] = ApiClient.convertToType(data['autoPoints'], 'Number');
            }
            if (data.hasOwnProperty('autoReachPoints')) {
                obj['autoReachPoints'] = ApiClient.convertToType(data['autoReachPoints'], 'Number');
            }
            if (data.hasOwnProperty('breachPoints')) {
                obj['breachPoints'] = ApiClient.convertToType(data['breachPoints'], 'Number');
            }
            if (data.hasOwnProperty('capturePoints')) {
                obj['capturePoints'] = ApiClient.convertToType(data['capturePoints'], 'Number');
            }
            if (data.hasOwnProperty('foulCount')) {
                obj['foulCount'] = ApiClient.convertToType(data['foulCount'], 'Number');
            }
            if (data.hasOwnProperty('foulPoints')) {
                obj['foulPoints'] = ApiClient.convertToType(data['foulPoints'], 'Number');
            }
            if (data.hasOwnProperty('position1crossings')) {
                obj['position1crossings'] = ApiClient.convertToType(data['position1crossings'], 'Number');
            }
            if (data.hasOwnProperty('position2')) {
                obj['position2'] = ApiClient.convertToType(data['position2'], 'String');
            }
            if (data.hasOwnProperty('position2crossings')) {
                obj['position2crossings'] = ApiClient.convertToType(data['position2crossings'], 'Number');
            }
            if (data.hasOwnProperty('position3')) {
                obj['position3'] = ApiClient.convertToType(data['position3'], 'String');
            }
            if (data.hasOwnProperty('position3crossings')) {
                obj['position3crossings'] = ApiClient.convertToType(data['position3crossings'], 'Number');
            }
            if (data.hasOwnProperty('position4')) {
                obj['position4'] = ApiClient.convertToType(data['position4'], 'String');
            }
            if (data.hasOwnProperty('position4crossings')) {
                obj['position4crossings'] = ApiClient.convertToType(data['position4crossings'], 'Number');
            }
            if (data.hasOwnProperty('position5')) {
                obj['position5'] = ApiClient.convertToType(data['position5'], 'String');
            }
            if (data.hasOwnProperty('position5crossings')) {
                obj['position5crossings'] = ApiClient.convertToType(data['position5crossings'], 'Number');
            }
            if (data.hasOwnProperty('robot1Auto')) {
                obj['robot1Auto'] = ApiClient.convertToType(data['robot1Auto'], 'String');
            }
            if (data.hasOwnProperty('robot2Auto')) {
                obj['robot2Auto'] = ApiClient.convertToType(data['robot2Auto'], 'String');
            }
            if (data.hasOwnProperty('robot3Auto')) {
                obj['robot3Auto'] = ApiClient.convertToType(data['robot3Auto'], 'String');
            }
            if (data.hasOwnProperty('techFoulCount')) {
                obj['techFoulCount'] = ApiClient.convertToType(data['techFoulCount'], 'Number');
            }
            if (data.hasOwnProperty('teleopBoulderPoints')) {
                obj['teleopBoulderPoints'] = ApiClient.convertToType(data['teleopBoulderPoints'], 'Number');
            }
            if (data.hasOwnProperty('teleopBouldersHigh')) {
                obj['teleopBouldersHigh'] = ApiClient.convertToType(data['teleopBouldersHigh'], 'Number');
            }
            if (data.hasOwnProperty('teleopBouldersLow')) {
                obj['teleopBouldersLow'] = ApiClient.convertToType(data['teleopBouldersLow'], 'Number');
            }
            if (data.hasOwnProperty('teleopChallengePoints')) {
                obj['teleopChallengePoints'] = ApiClient.convertToType(data['teleopChallengePoints'], 'Number');
            }
            if (data.hasOwnProperty('teleopCrossingPoints')) {
                obj['teleopCrossingPoints'] = ApiClient.convertToType(data['teleopCrossingPoints'], 'Number');
            }
            if (data.hasOwnProperty('teleopDefensesBreached')) {
                obj['teleopDefensesBreached'] = ApiClient.convertToType(data['teleopDefensesBreached'], 'Boolean');
            }
            if (data.hasOwnProperty('teleopPoints')) {
                obj['teleopPoints'] = ApiClient.convertToType(data['teleopPoints'], 'Number');
            }
            if (data.hasOwnProperty('teleopScalePoints')) {
                obj['teleopScalePoints'] = ApiClient.convertToType(data['teleopScalePoints'], 'Number');
            }
            if (data.hasOwnProperty('teleopTowerCaptured')) {
                obj['teleopTowerCaptured'] = ApiClient.convertToType(data['teleopTowerCaptured'], 'Number');
            }
            if (data.hasOwnProperty('totalPoints')) {
                obj['totalPoints'] = ApiClient.convertToType(data['totalPoints'], 'Number');
            }
            if (data.hasOwnProperty('towerEndStrength')) {
                obj['towerEndStrength'] = ApiClient.convertToType(data['towerEndStrength'], 'Number');
            }
            if (data.hasOwnProperty('towerFaceA')) {
                obj['towerFaceA'] = ApiClient.convertToType(data['towerFaceA'], 'String');
            }
            if (data.hasOwnProperty('towerFaceB')) {
                obj['towerFaceB'] = ApiClient.convertToType(data['towerFaceB'], 'String');
            }
            if (data.hasOwnProperty('towerFaceC')) {
                obj['towerFaceC'] = ApiClient.convertToType(data['towerFaceC'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MatchScoreBreakdown2016Alliance</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MatchScoreBreakdown2016Alliance</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['position2'] && !(typeof data['position2'] === 'string' || data['position2'] instanceof String)) {
            throw new Error("Expected the field `position2` to be a primitive type in the JSON string but got " + data['position2']);
        }
        // ensure the json data is a string
        if (data['position3'] && !(typeof data['position3'] === 'string' || data['position3'] instanceof String)) {
            throw new Error("Expected the field `position3` to be a primitive type in the JSON string but got " + data['position3']);
        }
        // ensure the json data is a string
        if (data['position4'] && !(typeof data['position4'] === 'string' || data['position4'] instanceof String)) {
            throw new Error("Expected the field `position4` to be a primitive type in the JSON string but got " + data['position4']);
        }
        // ensure the json data is a string
        if (data['position5'] && !(typeof data['position5'] === 'string' || data['position5'] instanceof String)) {
            throw new Error("Expected the field `position5` to be a primitive type in the JSON string but got " + data['position5']);
        }
        // ensure the json data is a string
        if (data['robot1Auto'] && !(typeof data['robot1Auto'] === 'string' || data['robot1Auto'] instanceof String)) {
            throw new Error("Expected the field `robot1Auto` to be a primitive type in the JSON string but got " + data['robot1Auto']);
        }
        // ensure the json data is a string
        if (data['robot2Auto'] && !(typeof data['robot2Auto'] === 'string' || data['robot2Auto'] instanceof String)) {
            throw new Error("Expected the field `robot2Auto` to be a primitive type in the JSON string but got " + data['robot2Auto']);
        }
        // ensure the json data is a string
        if (data['robot3Auto'] && !(typeof data['robot3Auto'] === 'string' || data['robot3Auto'] instanceof String)) {
            throw new Error("Expected the field `robot3Auto` to be a primitive type in the JSON string but got " + data['robot3Auto']);
        }
        // ensure the json data is a string
        if (data['towerFaceA'] && !(typeof data['towerFaceA'] === 'string' || data['towerFaceA'] instanceof String)) {
            throw new Error("Expected the field `towerFaceA` to be a primitive type in the JSON string but got " + data['towerFaceA']);
        }
        // ensure the json data is a string
        if (data['towerFaceB'] && !(typeof data['towerFaceB'] === 'string' || data['towerFaceB'] instanceof String)) {
            throw new Error("Expected the field `towerFaceB` to be a primitive type in the JSON string but got " + data['towerFaceB']);
        }
        // ensure the json data is a string
        if (data['towerFaceC'] && !(typeof data['towerFaceC'] === 'string' || data['towerFaceC'] instanceof String)) {
            throw new Error("Expected the field `towerFaceC` to be a primitive type in the JSON string but got " + data['towerFaceC']);
        }

        return true;
    }


}



/**
 * @member {Number} adjustPoints
 */
MatchScoreBreakdown2016Alliance.prototype['adjustPoints'] = undefined;

/**
 * @member {Number} autoBoulderPoints
 */
MatchScoreBreakdown2016Alliance.prototype['autoBoulderPoints'] = undefined;

/**
 * @member {Number} autoBouldersHigh
 */
MatchScoreBreakdown2016Alliance.prototype['autoBouldersHigh'] = undefined;

/**
 * @member {Number} autoBouldersLow
 */
MatchScoreBreakdown2016Alliance.prototype['autoBouldersLow'] = undefined;

/**
 * @member {Number} autoCrossingPoints
 */
MatchScoreBreakdown2016Alliance.prototype['autoCrossingPoints'] = undefined;

/**
 * @member {Number} autoPoints
 */
MatchScoreBreakdown2016Alliance.prototype['autoPoints'] = undefined;

/**
 * @member {Number} autoReachPoints
 */
MatchScoreBreakdown2016Alliance.prototype['autoReachPoints'] = undefined;

/**
 * @member {Number} breachPoints
 */
MatchScoreBreakdown2016Alliance.prototype['breachPoints'] = undefined;

/**
 * @member {Number} capturePoints
 */
MatchScoreBreakdown2016Alliance.prototype['capturePoints'] = undefined;

/**
 * @member {Number} foulCount
 */
MatchScoreBreakdown2016Alliance.prototype['foulCount'] = undefined;

/**
 * @member {Number} foulPoints
 */
MatchScoreBreakdown2016Alliance.prototype['foulPoints'] = undefined;

/**
 * @member {Number} position1crossings
 */
MatchScoreBreakdown2016Alliance.prototype['position1crossings'] = undefined;

/**
 * @member {String} position2
 */
MatchScoreBreakdown2016Alliance.prototype['position2'] = undefined;

/**
 * @member {Number} position2crossings
 */
MatchScoreBreakdown2016Alliance.prototype['position2crossings'] = undefined;

/**
 * @member {String} position3
 */
MatchScoreBreakdown2016Alliance.prototype['position3'] = undefined;

/**
 * @member {Number} position3crossings
 */
MatchScoreBreakdown2016Alliance.prototype['position3crossings'] = undefined;

/**
 * @member {String} position4
 */
MatchScoreBreakdown2016Alliance.prototype['position4'] = undefined;

/**
 * @member {Number} position4crossings
 */
MatchScoreBreakdown2016Alliance.prototype['position4crossings'] = undefined;

/**
 * @member {String} position5
 */
MatchScoreBreakdown2016Alliance.prototype['position5'] = undefined;

/**
 * @member {Number} position5crossings
 */
MatchScoreBreakdown2016Alliance.prototype['position5crossings'] = undefined;

/**
 * @member {module:model/MatchScoreBreakdown2016Alliance.Robot1AutoEnum} robot1Auto
 */
MatchScoreBreakdown2016Alliance.prototype['robot1Auto'] = undefined;

/**
 * @member {module:model/MatchScoreBreakdown2016Alliance.Robot2AutoEnum} robot2Auto
 */
MatchScoreBreakdown2016Alliance.prototype['robot2Auto'] = undefined;

/**
 * @member {module:model/MatchScoreBreakdown2016Alliance.Robot3AutoEnum} robot3Auto
 */
MatchScoreBreakdown2016Alliance.prototype['robot3Auto'] = undefined;

/**
 * @member {Number} techFoulCount
 */
MatchScoreBreakdown2016Alliance.prototype['techFoulCount'] = undefined;

/**
 * @member {Number} teleopBoulderPoints
 */
MatchScoreBreakdown2016Alliance.prototype['teleopBoulderPoints'] = undefined;

/**
 * @member {Number} teleopBouldersHigh
 */
MatchScoreBreakdown2016Alliance.prototype['teleopBouldersHigh'] = undefined;

/**
 * @member {Number} teleopBouldersLow
 */
MatchScoreBreakdown2016Alliance.prototype['teleopBouldersLow'] = undefined;

/**
 * @member {Number} teleopChallengePoints
 */
MatchScoreBreakdown2016Alliance.prototype['teleopChallengePoints'] = undefined;

/**
 * @member {Number} teleopCrossingPoints
 */
MatchScoreBreakdown2016Alliance.prototype['teleopCrossingPoints'] = undefined;

/**
 * @member {Boolean} teleopDefensesBreached
 */
MatchScoreBreakdown2016Alliance.prototype['teleopDefensesBreached'] = undefined;

/**
 * @member {Number} teleopPoints
 */
MatchScoreBreakdown2016Alliance.prototype['teleopPoints'] = undefined;

/**
 * @member {Number} teleopScalePoints
 */
MatchScoreBreakdown2016Alliance.prototype['teleopScalePoints'] = undefined;

/**
 * @member {Number} teleopTowerCaptured
 */
MatchScoreBreakdown2016Alliance.prototype['teleopTowerCaptured'] = undefined;

/**
 * @member {Number} totalPoints
 */
MatchScoreBreakdown2016Alliance.prototype['totalPoints'] = undefined;

/**
 * @member {Number} towerEndStrength
 */
MatchScoreBreakdown2016Alliance.prototype['towerEndStrength'] = undefined;

/**
 * @member {String} towerFaceA
 */
MatchScoreBreakdown2016Alliance.prototype['towerFaceA'] = undefined;

/**
 * @member {String} towerFaceB
 */
MatchScoreBreakdown2016Alliance.prototype['towerFaceB'] = undefined;

/**
 * @member {String} towerFaceC
 */
MatchScoreBreakdown2016Alliance.prototype['towerFaceC'] = undefined;





/**
 * Allowed values for the <code>robot1Auto</code> property.
 * @enum {String}
 * @readonly
 */
MatchScoreBreakdown2016Alliance['Robot1AutoEnum'] = {

    /**
     * value: "Crossed"
     * @const
     */
    "Crossed": "Crossed",

    /**
     * value: "Reached"
     * @const
     */
    "Reached": "Reached",

    /**
     * value: "None"
     * @const
     */
    "None": "None"
};


/**
 * Allowed values for the <code>robot2Auto</code> property.
 * @enum {String}
 * @readonly
 */
MatchScoreBreakdown2016Alliance['Robot2AutoEnum'] = {

    /**
     * value: "Crossed"
     * @const
     */
    "Crossed": "Crossed",

    /**
     * value: "Reached"
     * @const
     */
    "Reached": "Reached",

    /**
     * value: "None"
     * @const
     */
    "None": "None"
};


/**
 * Allowed values for the <code>robot3Auto</code> property.
 * @enum {String}
 * @readonly
 */
MatchScoreBreakdown2016Alliance['Robot3AutoEnum'] = {

    /**
     * value: "Crossed"
     * @const
     */
    "Crossed": "Crossed",

    /**
     * value: "Reached"
     * @const
     */
    "Reached": "Reached",

    /**
     * value: "None"
     * @const
     */
    "None": "None"
};



export default MatchScoreBreakdown2016Alliance;

