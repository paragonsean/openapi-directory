/**
 * Airflow API (Stable)
 * # Overview  To facilitate management, Apache Airflow supports a range of REST API endpoints across its objects. This section provides an overview of the API design, methods, and supported use cases.  Most of the endpoints accept `JSON` as input and return `JSON` responses. This means that you must usually add the following headers to your request: ``` Content-type: application/json Accept: application/json ```  ## Resources  The term `resource` refers to a single type of object in the Airflow metadata. An API is broken up by its endpoint's corresponding resource. The name of a resource is typically plural and expressed in camelCase. Example: `dagRuns`.  Resource names are used as part of endpoint URLs, as well as in API parameters and responses.  ## CRUD Operations  The platform supports **C**reate, **R**ead, **U**pdate, and **D**elete operations on most resources. You can review the standards for these operations and their standard parameters below.  Some endpoints have special behavior as exceptions.  ### Create  To create a resource, you typically submit an HTTP `POST` request with the resource's required metadata in the request body. The response returns a `201 Created` response code upon success with the resource's metadata, including its internal `id`, in the response body.  ### Read  The HTTP `GET` request can be used to read a resource or to list a number of resources.  A resource's `id` can be submitted in the request parameters to read a specific resource. The response usually returns a `200 OK` response code upon success, with the resource's metadata in the response body.  If a `GET` request does not include a specific resource `id`, it is treated as a list request. The response usually returns a `200 OK` response code upon success, with an object containing a list of resources' metadata in the response body.  When reading resources, some common query parameters are usually available. e.g.: ``` v1/connections?limit=25&offset=25 ```  |Query Parameter|Type|Description| |---------------|----|-----------| |limit|integer|Maximum number of objects to fetch. Usually 25 by default| |offset|integer|Offset after which to start returning objects. For use with limit query parameter.|  ### Update  Updating a resource requires the resource `id`, and is typically done using an HTTP `PATCH` request, with the fields to modify in the request body. The response usually returns a `200 OK` response code upon success, with information about the modified resource in the response body.  ### Delete  Deleting a resource requires the resource `id` and is typically executing via an HTTP `DELETE` request. The response usually returns a `204 No Content` response code upon success.  ## Conventions  - Resource names are plural and expressed in camelCase. - Names are consistent between URL parameter name and field name.  - Field names are in snake_case. ```json {     \"name\": \"string\",     \"slots\": 0,     \"occupied_slots\": 0,     \"used_slots\": 0,     \"queued_slots\": 0,     \"open_slots\": 0 } ```  ### Update Mask  Update mask is available as a query parameter in patch endpoints. It is used to notify the API which fields you want to update. Using `update_mask` makes it easier to update objects by helping the server know which fields to update in an object instead of updating all fields. The update request ignores any fields that aren't specified in the field mask, leaving them with their current values.  Example: ```   resource = request.get('/resource/my-id').json()   resource['my_field'] = 'new-value'   request.patch('/resource/my-id?update_mask=my_field', data=json.dumps(resource)) ```  ## Versioning and Endpoint Lifecycle  - API versioning is not synchronized to specific releases of the Apache Airflow. - APIs are designed to be backward compatible. - Any changes to the API will first go through a deprecation phase.  # Trying the API  You can use a third party client, such as [curl](https://curl.haxx.se/), [HTTPie](https://httpie.org/), [Postman](https://www.postman.com/) or [the Insomnia rest client](https://insomnia.rest/) to test the Apache Airflow API.  Note that you will need to pass credentials data.  For e.g., here is how to pause a DAG with [curl](https://curl.haxx.se/), when basic authorization is used: ```bash curl -X PATCH 'https://example.com/api/v1/dags/{dag_id}?update_mask=is_paused' \\ -H 'Content-Type: application/json' \\ --user \"username:password\" \\ -d '{     \"is_paused\": true }' ```  Using a graphical tool such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/), it is possible to import the API specifications directly:  1. Download the API specification by clicking the **Download** button at top of this document 2. Import the JSON specification in the graphical tool of your choice.   - In *Postman*, you can click the **import** button at the top   - With *Insomnia*, you can just drag-and-drop the file on the UI  Note that with *Postman*, you can also generate code snippets by selecting a request and clicking on the **Code** button.  ## Enabling CORS  [Cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a browser security feature that restricts HTTP requests that are initiated from scripts running in the browser.  For details on enabling/configuring CORS, see [Enabling CORS](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Authentication  To be able to meet the requirements of many organizations, Airflow supports many authentication methods, and it is even possible to add your own method.  If you want to check which auth backend is currently set, you can use `airflow config get-value api auth_backends` command as in the example below. ```bash $ airflow config get-value api auth_backends airflow.api.auth.backend.basic_auth ``` The default is to deny all requests.  For details on configuring the authentication, see [API Authorization](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Errors  We follow the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs. As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Unauthenticated  This indicates that the request has not been applied because it lacks valid authentication credentials for the target resource. Please check that you have valid credentials.  ## PermissionDenied  This response means that the server understood the request but refuses to authorize it because it lacks sufficient rights to the resource. It happens when you do not have the necessary permission to execute the action you performed. You need to get the appropriate permissions in other to resolve this error.  ## BadRequest  This response means that the server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). To resolve this, please ensure that your syntax is correct.  ## NotFound  This client error response indicates that the server cannot find the requested resource.  ## MethodNotAllowed  Indicates that the request method is known by the server but is not supported by the target resource.  ## NotAcceptable  The target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.  ## AlreadyExists  The request could not be completed due to a conflict with the current state of the target resource, e.g. the resource it tries to create already exists.  ## Unknown  This means that the server encountered an unexpected condition that prevented it from fulfilling the request. 
 *
 * The version of the OpenAPI document: 2.5.3
 * Contact: dev@airflow.apache.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import UserCollectionItem from './UserCollectionItem';
import UserCollectionItemRolesInner from './UserCollectionItemRolesInner';

/**
 * The User model module.
 * @module model/User
 * @version 2.5.3
 */
class User {
    /**
     * Constructs a new <code>User</code>.
     * A user object with sensitive data.  *New in version 2.1.0* 
     * @alias module:model/User
     * @implements module:model/UserCollectionItem
     */
    constructor() { 
        UserCollectionItem.initialize(this);
        User.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>User</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/User} obj Optional instance to populate.
     * @return {module:model/User} The populated <code>User</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new User();
            UserCollectionItem.constructFromObject(data, obj);

            if (data.hasOwnProperty('active')) {
                obj['active'] = ApiClient.convertToType(data['active'], 'Boolean');
            }
            if (data.hasOwnProperty('changed_on')) {
                obj['changed_on'] = ApiClient.convertToType(data['changed_on'], 'String');
            }
            if (data.hasOwnProperty('created_on')) {
                obj['created_on'] = ApiClient.convertToType(data['created_on'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('failed_login_count')) {
                obj['failed_login_count'] = ApiClient.convertToType(data['failed_login_count'], 'Number');
            }
            if (data.hasOwnProperty('first_name')) {
                obj['first_name'] = ApiClient.convertToType(data['first_name'], 'String');
            }
            if (data.hasOwnProperty('last_login')) {
                obj['last_login'] = ApiClient.convertToType(data['last_login'], 'String');
            }
            if (data.hasOwnProperty('last_name')) {
                obj['last_name'] = ApiClient.convertToType(data['last_name'], 'String');
            }
            if (data.hasOwnProperty('login_count')) {
                obj['login_count'] = ApiClient.convertToType(data['login_count'], 'Number');
            }
            if (data.hasOwnProperty('roles')) {
                obj['roles'] = ApiClient.convertToType(data['roles'], [UserCollectionItemRolesInner]);
            }
            if (data.hasOwnProperty('username')) {
                obj['username'] = ApiClient.convertToType(data['username'], 'String');
            }
            if (data.hasOwnProperty('password')) {
                obj['password'] = ApiClient.convertToType(data['password'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>User</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>User</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['changed_on'] && !(typeof data['changed_on'] === 'string' || data['changed_on'] instanceof String)) {
            throw new Error("Expected the field `changed_on` to be a primitive type in the JSON string but got " + data['changed_on']);
        }
        // ensure the json data is a string
        if (data['created_on'] && !(typeof data['created_on'] === 'string' || data['created_on'] instanceof String)) {
            throw new Error("Expected the field `created_on` to be a primitive type in the JSON string but got " + data['created_on']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['first_name'] && !(typeof data['first_name'] === 'string' || data['first_name'] instanceof String)) {
            throw new Error("Expected the field `first_name` to be a primitive type in the JSON string but got " + data['first_name']);
        }
        // ensure the json data is a string
        if (data['last_login'] && !(typeof data['last_login'] === 'string' || data['last_login'] instanceof String)) {
            throw new Error("Expected the field `last_login` to be a primitive type in the JSON string but got " + data['last_login']);
        }
        // ensure the json data is a string
        if (data['last_name'] && !(typeof data['last_name'] === 'string' || data['last_name'] instanceof String)) {
            throw new Error("Expected the field `last_name` to be a primitive type in the JSON string but got " + data['last_name']);
        }
        if (data['roles']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['roles'])) {
                throw new Error("Expected the field `roles` to be an array in the JSON data but got " + data['roles']);
            }
            // validate the optional field `roles` (array)
            for (const item of data['roles']) {
                UserCollectionItemRolesInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['username'] && !(typeof data['username'] === 'string' || data['username'] instanceof String)) {
            throw new Error("Expected the field `username` to be a primitive type in the JSON string but got " + data['username']);
        }
        // ensure the json data is a string
        if (data['password'] && !(typeof data['password'] === 'string' || data['password'] instanceof String)) {
            throw new Error("Expected the field `password` to be a primitive type in the JSON string but got " + data['password']);
        }

        return true;
    }


}



/**
 * Whether the user is active
 * @member {Boolean} active
 */
User.prototype['active'] = undefined;

/**
 * The date user was changed
 * @member {String} changed_on
 */
User.prototype['changed_on'] = undefined;

/**
 * The date user was created
 * @member {String} created_on
 */
User.prototype['created_on'] = undefined;

/**
 * The user's email.  *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added. 
 * @member {String} email
 */
User.prototype['email'] = undefined;

/**
 * The number of times the login failed
 * @member {Number} failed_login_count
 */
User.prototype['failed_login_count'] = undefined;

/**
 * The user's first name.  *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed. 
 * @member {String} first_name
 */
User.prototype['first_name'] = undefined;

/**
 * The last user login
 * @member {String} last_login
 */
User.prototype['last_login'] = undefined;

/**
 * The user's last name.  *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed. 
 * @member {String} last_name
 */
User.prototype['last_name'] = undefined;

/**
 * The login count
 * @member {Number} login_count
 */
User.prototype['login_count'] = undefined;

/**
 * User roles.  *Changed in version 2.2.0*&#58; Field is no longer read-only. 
 * @member {Array.<module:model/UserCollectionItemRolesInner>} roles
 */
User.prototype['roles'] = undefined;

/**
 * The username.  *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added. 
 * @member {String} username
 */
User.prototype['username'] = undefined;

/**
 * @member {String} password
 */
User.prototype['password'] = undefined;


// Implement UserCollectionItem interface:
/**
 * Whether the user is active
 * @member {Boolean} active
 */
UserCollectionItem.prototype['active'] = undefined;
/**
 * The date user was changed
 * @member {String} changed_on
 */
UserCollectionItem.prototype['changed_on'] = undefined;
/**
 * The date user was created
 * @member {String} created_on
 */
UserCollectionItem.prototype['created_on'] = undefined;
/**
 * The user's email.  *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added. 
 * @member {String} email
 */
UserCollectionItem.prototype['email'] = undefined;
/**
 * The number of times the login failed
 * @member {Number} failed_login_count
 */
UserCollectionItem.prototype['failed_login_count'] = undefined;
/**
 * The user's first name.  *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed. 
 * @member {String} first_name
 */
UserCollectionItem.prototype['first_name'] = undefined;
/**
 * The last user login
 * @member {String} last_login
 */
UserCollectionItem.prototype['last_login'] = undefined;
/**
 * The user's last name.  *Changed in version 2.4.0*&#58; The requirement for this to be non-empty was removed. 
 * @member {String} last_name
 */
UserCollectionItem.prototype['last_name'] = undefined;
/**
 * The login count
 * @member {Number} login_count
 */
UserCollectionItem.prototype['login_count'] = undefined;
/**
 * User roles.  *Changed in version 2.2.0*&#58; Field is no longer read-only. 
 * @member {Array.<module:model/UserCollectionItemRolesInner>} roles
 */
UserCollectionItem.prototype['roles'] = undefined;
/**
 * The username.  *Changed in version 2.2.0*&#58; A minimum character length requirement ('minLength') is added. 
 * @member {String} username
 */
UserCollectionItem.prototype['username'] = undefined;




export default User;

