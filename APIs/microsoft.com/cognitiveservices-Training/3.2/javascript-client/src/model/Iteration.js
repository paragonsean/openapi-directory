/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Iteration model module.
 * @module model/Iteration
 * @version 3.2
 */
class Iteration {
    /**
     * Constructs a new <code>Iteration</code>.
     * Iteration model to be sent over JSON.
     * @alias module:model/Iteration
     * @param name {String} Gets or sets the name of the iteration.
     */
    constructor(name) { 
        
        Iteration.initialize(this, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name) { 
        obj['name'] = name;
    }

    /**
     * Constructs a <code>Iteration</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Iteration} obj Optional instance to populate.
     * @return {module:model/Iteration} The populated <code>Iteration</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Iteration();

            if (data.hasOwnProperty('classificationType')) {
                obj['classificationType'] = ApiClient.convertToType(data['classificationType'], 'String');
            }
            if (data.hasOwnProperty('created')) {
                obj['created'] = ApiClient.convertToType(data['created'], 'Date');
            }
            if (data.hasOwnProperty('domainId')) {
                obj['domainId'] = ApiClient.convertToType(data['domainId'], 'String');
            }
            if (data.hasOwnProperty('exportable')) {
                obj['exportable'] = ApiClient.convertToType(data['exportable'], 'Boolean');
            }
            if (data.hasOwnProperty('exportableTo')) {
                obj['exportableTo'] = ApiClient.convertToType(data['exportableTo'], ['String']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('lastModified')) {
                obj['lastModified'] = ApiClient.convertToType(data['lastModified'], 'Date');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('originalPublishResourceId')) {
                obj['originalPublishResourceId'] = ApiClient.convertToType(data['originalPublishResourceId'], 'String');
            }
            if (data.hasOwnProperty('projectId')) {
                obj['projectId'] = ApiClient.convertToType(data['projectId'], 'String');
            }
            if (data.hasOwnProperty('publishName')) {
                obj['publishName'] = ApiClient.convertToType(data['publishName'], 'String');
            }
            if (data.hasOwnProperty('reservedBudgetInHours')) {
                obj['reservedBudgetInHours'] = ApiClient.convertToType(data['reservedBudgetInHours'], 'Number');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('trainedAt')) {
                obj['trainedAt'] = ApiClient.convertToType(data['trainedAt'], 'Date');
            }
            if (data.hasOwnProperty('trainingTimeInMinutes')) {
                obj['trainingTimeInMinutes'] = ApiClient.convertToType(data['trainingTimeInMinutes'], 'Number');
            }
            if (data.hasOwnProperty('trainingType')) {
                obj['trainingType'] = ApiClient.convertToType(data['trainingType'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Iteration</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Iteration</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Iteration.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['classificationType'] && !(typeof data['classificationType'] === 'string' || data['classificationType'] instanceof String)) {
            throw new Error("Expected the field `classificationType` to be a primitive type in the JSON string but got " + data['classificationType']);
        }
        // ensure the json data is a string
        if (data['domainId'] && !(typeof data['domainId'] === 'string' || data['domainId'] instanceof String)) {
            throw new Error("Expected the field `domainId` to be a primitive type in the JSON string but got " + data['domainId']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['exportableTo'])) {
            throw new Error("Expected the field `exportableTo` to be an array in the JSON data but got " + data['exportableTo']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['originalPublishResourceId'] && !(typeof data['originalPublishResourceId'] === 'string' || data['originalPublishResourceId'] instanceof String)) {
            throw new Error("Expected the field `originalPublishResourceId` to be a primitive type in the JSON string but got " + data['originalPublishResourceId']);
        }
        // ensure the json data is a string
        if (data['projectId'] && !(typeof data['projectId'] === 'string' || data['projectId'] instanceof String)) {
            throw new Error("Expected the field `projectId` to be a primitive type in the JSON string but got " + data['projectId']);
        }
        // ensure the json data is a string
        if (data['publishName'] && !(typeof data['publishName'] === 'string' || data['publishName'] instanceof String)) {
            throw new Error("Expected the field `publishName` to be a primitive type in the JSON string but got " + data['publishName']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['trainingType'] && !(typeof data['trainingType'] === 'string' || data['trainingType'] instanceof String)) {
            throw new Error("Expected the field `trainingType` to be a primitive type in the JSON string but got " + data['trainingType']);
        }

        return true;
    }


}

Iteration.RequiredProperties = ["name"];

/**
 * Gets the classification type of the project.
 * @member {module:model/Iteration.ClassificationTypeEnum} classificationType
 */
Iteration.prototype['classificationType'] = undefined;

/**
 * Gets the time this iteration was completed.
 * @member {Date} created
 */
Iteration.prototype['created'] = undefined;

/**
 * Get or sets a guid of the domain the iteration has been trained on.
 * @member {String} domainId
 */
Iteration.prototype['domainId'] = undefined;

/**
 * Whether the iteration can be exported to another format for download.
 * @member {Boolean} exportable
 */
Iteration.prototype['exportable'] = undefined;

/**
 * A set of platforms this iteration can export to.
 * @member {Array.<module:model/Iteration.ExportableToEnum>} exportableTo
 */
Iteration.prototype['exportableTo'] = undefined;

/**
 * Gets the id of the iteration.
 * @member {String} id
 */
Iteration.prototype['id'] = undefined;

/**
 * Gets the time this iteration was last modified.
 * @member {Date} lastModified
 */
Iteration.prototype['lastModified'] = undefined;

/**
 * Gets or sets the name of the iteration.
 * @member {String} name
 */
Iteration.prototype['name'] = undefined;

/**
 * Resource Provider Id this iteration was originally published to.
 * @member {String} originalPublishResourceId
 */
Iteration.prototype['originalPublishResourceId'] = undefined;

/**
 * Gets the project id of the iteration.
 * @member {String} projectId
 */
Iteration.prototype['projectId'] = undefined;

/**
 * Name of the published model.
 * @member {String} publishName
 */
Iteration.prototype['publishName'] = undefined;

/**
 * Gets the reserved advanced training budget for the iteration.
 * @member {Number} reservedBudgetInHours
 */
Iteration.prototype['reservedBudgetInHours'] = undefined;

/**
 * Gets the current iteration status.
 * @member {String} status
 */
Iteration.prototype['status'] = undefined;

/**
 * Gets the time this iteration was last modified.
 * @member {Date} trainedAt
 */
Iteration.prototype['trainedAt'] = undefined;

/**
 * Gets the training time for the iteration.
 * @member {Number} trainingTimeInMinutes
 */
Iteration.prototype['trainingTimeInMinutes'] = undefined;

/**
 * Gets the training type of the iteration.
 * @member {module:model/Iteration.TrainingTypeEnum} trainingType
 */
Iteration.prototype['trainingType'] = undefined;





/**
 * Allowed values for the <code>classificationType</code> property.
 * @enum {String}
 * @readonly
 */
Iteration['ClassificationTypeEnum'] = {

    /**
     * value: "Multiclass"
     * @const
     */
    "Multiclass": "Multiclass",

    /**
     * value: "Multilabel"
     * @const
     */
    "Multilabel": "Multilabel"
};


/**
 * Allowed values for the <code>exportableTo</code> property.
 * @enum {String}
 * @readonly
 */
Iteration['ExportableToEnum'] = {

    /**
     * value: "CoreML"
     * @const
     */
    "CoreML": "CoreML",

    /**
     * value: "TensorFlow"
     * @const
     */
    "TensorFlow": "TensorFlow",

    /**
     * value: "DockerFile"
     * @const
     */
    "DockerFile": "DockerFile",

    /**
     * value: "ONNX"
     * @const
     */
    "ONNX": "ONNX",

    /**
     * value: "VAIDK"
     * @const
     */
    "VAIDK": "VAIDK"
};


/**
 * Allowed values for the <code>trainingType</code> property.
 * @enum {String}
 * @readonly
 */
Iteration['TrainingTypeEnum'] = {

    /**
     * value: "Regular"
     * @const
     */
    "Regular": "Regular",

    /**
     * value: "Advanced"
     * @const
     */
    "Advanced": "Advanced"
};



export default Iteration;

