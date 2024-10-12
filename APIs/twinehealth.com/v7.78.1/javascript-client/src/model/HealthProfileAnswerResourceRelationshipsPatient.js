/**
 * Fitbit Plus API
 * # Overview The Fitbit Plus API is a RESTful API. The requests and responses are formated according to the [JSON API](http://jsonapi.org/format/1.0/) specification.  In addition to this documentation, we also provide an [OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) \"yaml\" file describing the API: [Fitbit Plus API Specification](swagger.yaml).  # Authentication Authentication for the Fitbit Plus API is based on the [OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749). Fitbit Plus currently supports grant types of **client_credentials** and **refresh_token**.  See [POST /oauth/token](#operation/createToken) for details on the request and response formats. <!-- ReDoc-Inject: <security-definitions> -->  ## Building Integrations We will provide customers with unique client credentials for each application/integration they build, allowing us to enforce appropriate access controls and monitor API usage. The client credentials will be scoped to the organization, and allow full access to all patients and related data within that organization.  These credentials are appropriate for creating an integration that does one of the following:  - background reporting/analysis  - synchronizing data with another system (such as an EMR)  The API credentials and oauth flows we currently support are **not** well suited for creating a user-facing application that allows a user (patient, coach, or admin) to login and have access to data which is appropriate to that specific user. It is possible to build such an application, but it is not possible to use Fitbit Plus as a federated identity provider. You would need to have a separate means of verifying a user's identity. We do not currently support the required password-based oauth flow to make this possible.  # Paging The Fitbit Plus API supports two different pagination strategies for GET collection endpoints.  #### Skip-based paging  Skip-based paging uses the query parameters `page[size]` and `page[number]` to specify the max number of resources returned and the page number. We default to skip-based paging if there are no page parameters. The response will include a `links` object containing links to the first, last, prev, and next pages of data.  If the contents of the collection change while you are iterating through the collection, you will see duplicate or missing documents. For example, if you are iterating through the `calender_event` resource via `GET /pub/calendar_event?sort=start_at&page[size]=50&page[number]=1`, and a new `calendar_event` is created that has a `start_at` value before the first `calendar_event`, when you fetch the next page at `GET /pub/calendar_event?sort=start_at&page[size]=50&page[number]=2`, the first entry in the second response will be a duplicate of the last entry in the first response.  #### Cursor-based paging Cursor-based paging uses the query parameters `page[limit]` and `page[after]` to specify the max number of entries returned and identify where to begin the next page. Add `page[limit]` to the parameters to use cursor-based paging. The response will include a `links` object containing a link to the next page of data, if the next page exists.  Cursor-based paging is not subject to duplication if new resources are added to the collection. For example, if you are iterating through the `calender_event` resource via `GET /pub/calendar_event?sort=start_at&page[limit]=50`, and a new `calendar_event` is created that has a `start_at` value before the first `calendar_event`, you will not see a duplicate entry when you fetch the next page at `GET /pub/calendar_event?sort=start_at&page[limit]=50&page[after]=<cursor>`.  We encourage the use of cursor-based paging for performance reasons.  In either form of paging, you can determine whether any resources were missed by comparing the number of fetched resources against `meta.count`. Set `page[size]` or `page[limit]` to 0 to get only the count.  It is not valid to mix the two strategies. 
 *
 * The version of the OpenAPI document: v7.78.1
 * Contact: apiteam@twinehealth.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ActionResourceRelationshipsPlanData from './ActionResourceRelationshipsPlanData';
import HealthProfileAnswerResourceRelationshipsPatientLinks from './HealthProfileAnswerResourceRelationshipsPatientLinks';

/**
 * The HealthProfileAnswerResourceRelationshipsPatient model module.
 * @module model/HealthProfileAnswerResourceRelationshipsPatient
 * @version v7.78.1
 */
class HealthProfileAnswerResourceRelationshipsPatient {
    /**
     * Constructs a new <code>HealthProfileAnswerResourceRelationshipsPatient</code>.
     * @alias module:model/HealthProfileAnswerResourceRelationshipsPatient
     */
    constructor() { 
        
        HealthProfileAnswerResourceRelationshipsPatient.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>HealthProfileAnswerResourceRelationshipsPatient</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HealthProfileAnswerResourceRelationshipsPatient} obj Optional instance to populate.
     * @return {module:model/HealthProfileAnswerResourceRelationshipsPatient} The populated <code>HealthProfileAnswerResourceRelationshipsPatient</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HealthProfileAnswerResourceRelationshipsPatient();

            if (data.hasOwnProperty('data')) {
                obj['data'] = ActionResourceRelationshipsPlanData.constructFromObject(data['data']);
            }
            if (data.hasOwnProperty('links')) {
                obj['links'] = HealthProfileAnswerResourceRelationshipsPatientLinks.constructFromObject(data['links']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HealthProfileAnswerResourceRelationshipsPatient</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HealthProfileAnswerResourceRelationshipsPatient</code>.
     */
    static validateJSON(data) {
        // validate the optional field `data`
        if (data['data']) { // data not null
          ActionResourceRelationshipsPlanData.validateJSON(data['data']);
        }
        // validate the optional field `links`
        if (data['links']) { // data not null
          HealthProfileAnswerResourceRelationshipsPatientLinks.validateJSON(data['links']);
        }

        return true;
    }


}



/**
 * @member {module:model/ActionResourceRelationshipsPlanData} data
 */
HealthProfileAnswerResourceRelationshipsPatient.prototype['data'] = undefined;

/**
 * @member {module:model/HealthProfileAnswerResourceRelationshipsPatientLinks} links
 */
HealthProfileAnswerResourceRelationshipsPatient.prototype['links'] = undefined;






export default HealthProfileAnswerResourceRelationshipsPatient;

