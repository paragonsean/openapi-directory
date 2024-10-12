/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ArticleComplete from './ArticleComplete';
import Curation from './Curation';

/**
 * The CurationDetail model module.
 * @module model/CurationDetail
 * @version 2.0.0
 */
class CurationDetail {
    /**
     * Constructs a new <code>CurationDetail</code>.
     * @alias module:model/CurationDetail
     * @implements module:model/Curation
     * @param accountId {Number} The ID of the account of the owner of the article of this review.
     * @param articleId {Number} The ID of the article of this review.
     * @param assignedTo {Number} The ID of the account to which this review is assigned.
     * @param commentsCount {Number} The number of comments in the review.
     * @param createdDate {String} The creation date of the review.
     * @param groupId {Number} The group in which the article is present.
     * @param id {Number} The review id
     * @param modifiedDate {String} The date the review has been modified.
     * @param reviewDate {String} The last time a comment has been added to the review.
     * @param status {module:model/CurationDetail.StatusEnum} The status of the review.
     * @param version {Number} The Version number of the article in review.
     */
    constructor(accountId, articleId, assignedTo, commentsCount, createdDate, groupId, id, modifiedDate, reviewDate, status, version) { 
        Curation.initialize(this, accountId, articleId, assignedTo, commentsCount, createdDate, groupId, id, modifiedDate, reviewDate, status, version);
        CurationDetail.initialize(this, accountId, articleId, assignedTo, commentsCount, createdDate, groupId, id, modifiedDate, reviewDate, status, version);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, accountId, articleId, assignedTo, commentsCount, createdDate, groupId, id, modifiedDate, reviewDate, status, version) { 
        obj['item'] = item;
        obj['account_id'] = accountId;
        obj['article_id'] = articleId;
        obj['assigned_to'] = assignedTo;
        obj['comments_count'] = commentsCount;
        obj['created_date'] = createdDate;
        obj['group_id'] = groupId;
        obj['id'] = id;
        obj['modified_date'] = modifiedDate;
        obj['review_date'] = reviewDate;
        obj['status'] = status;
        obj['version'] = version;
    }

    /**
     * Constructs a <code>CurationDetail</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CurationDetail} obj Optional instance to populate.
     * @return {module:model/CurationDetail} The populated <code>CurationDetail</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CurationDetail();
            Curation.constructFromObject(data, obj);

            if (data.hasOwnProperty('item')) {
                obj['item'] = ArticleComplete.constructFromObject(data['item']);
            }
            if (data.hasOwnProperty('account_id')) {
                obj['account_id'] = ApiClient.convertToType(data['account_id'], 'Number');
            }
            if (data.hasOwnProperty('article_id')) {
                obj['article_id'] = ApiClient.convertToType(data['article_id'], 'Number');
            }
            if (data.hasOwnProperty('assigned_to')) {
                obj['assigned_to'] = ApiClient.convertToType(data['assigned_to'], 'Number');
            }
            if (data.hasOwnProperty('comments_count')) {
                obj['comments_count'] = ApiClient.convertToType(data['comments_count'], 'Number');
            }
            if (data.hasOwnProperty('created_date')) {
                obj['created_date'] = ApiClient.convertToType(data['created_date'], 'String');
            }
            if (data.hasOwnProperty('group_id')) {
                obj['group_id'] = ApiClient.convertToType(data['group_id'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('modified_date')) {
                obj['modified_date'] = ApiClient.convertToType(data['modified_date'], 'String');
            }
            if (data.hasOwnProperty('review_date')) {
                obj['review_date'] = ApiClient.convertToType(data['review_date'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('version')) {
                obj['version'] = ApiClient.convertToType(data['version'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CurationDetail</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CurationDetail</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CurationDetail.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `item`
        if (data['item']) { // data not null
          ArticleComplete.validateJSON(data['item']);
        }
        // ensure the json data is a string
        if (data['created_date'] && !(typeof data['created_date'] === 'string' || data['created_date'] instanceof String)) {
            throw new Error("Expected the field `created_date` to be a primitive type in the JSON string but got " + data['created_date']);
        }
        // ensure the json data is a string
        if (data['modified_date'] && !(typeof data['modified_date'] === 'string' || data['modified_date'] instanceof String)) {
            throw new Error("Expected the field `modified_date` to be a primitive type in the JSON string but got " + data['modified_date']);
        }
        // ensure the json data is a string
        if (data['review_date'] && !(typeof data['review_date'] === 'string' || data['review_date'] instanceof String)) {
            throw new Error("Expected the field `review_date` to be a primitive type in the JSON string but got " + data['review_date']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}

CurationDetail.RequiredProperties = ["item", "account_id", "article_id", "assigned_to", "comments_count", "created_date", "group_id", "id", "modified_date", "review_date", "status", "version"];

/**
 * @member {module:model/ArticleComplete} item
 */
CurationDetail.prototype['item'] = undefined;

/**
 * The ID of the account of the owner of the article of this review.
 * @member {Number} account_id
 */
CurationDetail.prototype['account_id'] = undefined;

/**
 * The ID of the article of this review.
 * @member {Number} article_id
 */
CurationDetail.prototype['article_id'] = undefined;

/**
 * The ID of the account to which this review is assigned.
 * @member {Number} assigned_to
 */
CurationDetail.prototype['assigned_to'] = undefined;

/**
 * The number of comments in the review.
 * @member {Number} comments_count
 */
CurationDetail.prototype['comments_count'] = undefined;

/**
 * The creation date of the review.
 * @member {String} created_date
 */
CurationDetail.prototype['created_date'] = undefined;

/**
 * The group in which the article is present.
 * @member {Number} group_id
 */
CurationDetail.prototype['group_id'] = undefined;

/**
 * The review id
 * @member {Number} id
 */
CurationDetail.prototype['id'] = undefined;

/**
 * The date the review has been modified.
 * @member {String} modified_date
 */
CurationDetail.prototype['modified_date'] = undefined;

/**
 * The last time a comment has been added to the review.
 * @member {String} review_date
 */
CurationDetail.prototype['review_date'] = undefined;

/**
 * The status of the review.
 * @member {module:model/CurationDetail.StatusEnum} status
 */
CurationDetail.prototype['status'] = undefined;

/**
 * The Version number of the article in review.
 * @member {Number} version
 */
CurationDetail.prototype['version'] = undefined;


// Implement Curation interface:
/**
 * The ID of the account of the owner of the article of this review.
 * @member {Number} account_id
 */
Curation.prototype['account_id'] = undefined;
/**
 * The ID of the article of this review.
 * @member {Number} article_id
 */
Curation.prototype['article_id'] = undefined;
/**
 * The ID of the account to which this review is assigned.
 * @member {Number} assigned_to
 */
Curation.prototype['assigned_to'] = undefined;
/**
 * The number of comments in the review.
 * @member {Number} comments_count
 */
Curation.prototype['comments_count'] = undefined;
/**
 * The creation date of the review.
 * @member {String} created_date
 */
Curation.prototype['created_date'] = undefined;
/**
 * The group in which the article is present.
 * @member {Number} group_id
 */
Curation.prototype['group_id'] = undefined;
/**
 * The review id
 * @member {Number} id
 */
Curation.prototype['id'] = undefined;
/**
 * The date the review has been modified.
 * @member {String} modified_date
 */
Curation.prototype['modified_date'] = undefined;
/**
 * The last time a comment has been added to the review.
 * @member {String} review_date
 */
Curation.prototype['review_date'] = undefined;
/**
 * The status of the review.
 * @member {module:model/Curation.StatusEnum} status
 */
Curation.prototype['status'] = undefined;
/**
 * The Version number of the article in review.
 * @member {Number} version
 */
Curation.prototype['version'] = undefined;



/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
CurationDetail['StatusEnum'] = {

    /**
     * value: "pending"
     * @const
     */
    "pending": "pending",

    /**
     * value: "approved"
     * @const
     */
    "approved": "approved",

    /**
     * value: "rejected"
     * @const
     */
    "rejected": "rejected",

    /**
     * value: "closed"
     * @const
     */
    "closed": "closed"
};



export default CurationDetail;

