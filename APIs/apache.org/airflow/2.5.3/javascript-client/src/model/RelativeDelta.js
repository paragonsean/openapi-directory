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

/**
 * The RelativeDelta model module.
 * @module model/RelativeDelta
 * @version 2.5.3
 */
class RelativeDelta {
    /**
     * Constructs a new <code>RelativeDelta</code>.
     * Relative delta
     * @alias module:model/RelativeDelta
     * @param type {String} 
     * @param day {Number} 
     * @param days {Number} 
     * @param hour {Number} 
     * @param hours {Number} 
     * @param leapdays {Number} 
     * @param microsecond {Number} 
     * @param microseconds {Number} 
     * @param minute {Number} 
     * @param minutes {Number} 
     * @param month {Number} 
     * @param months {Number} 
     * @param second {Number} 
     * @param seconds {Number} 
     * @param year {Number} 
     * @param years {Number} 
     */
    constructor(type, day, days, hour, hours, leapdays, microsecond, microseconds, minute, minutes, month, months, second, seconds, year, years) { 
        
        RelativeDelta.initialize(this, type, day, days, hour, hours, leapdays, microsecond, microseconds, minute, minutes, month, months, second, seconds, year, years);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, type, day, days, hour, hours, leapdays, microsecond, microseconds, minute, minutes, month, months, second, seconds, year, years) { 
        obj['__type'] = type;
        obj['day'] = day;
        obj['days'] = days;
        obj['hour'] = hour;
        obj['hours'] = hours;
        obj['leapdays'] = leapdays;
        obj['microsecond'] = microsecond;
        obj['microseconds'] = microseconds;
        obj['minute'] = minute;
        obj['minutes'] = minutes;
        obj['month'] = month;
        obj['months'] = months;
        obj['second'] = second;
        obj['seconds'] = seconds;
        obj['year'] = year;
        obj['years'] = years;
    }

    /**
     * Constructs a <code>RelativeDelta</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RelativeDelta} obj Optional instance to populate.
     * @return {module:model/RelativeDelta} The populated <code>RelativeDelta</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RelativeDelta();

            if (data.hasOwnProperty('__type')) {
                obj['__type'] = ApiClient.convertToType(data['__type'], 'String');
            }
            if (data.hasOwnProperty('day')) {
                obj['day'] = ApiClient.convertToType(data['day'], 'Number');
            }
            if (data.hasOwnProperty('days')) {
                obj['days'] = ApiClient.convertToType(data['days'], 'Number');
            }
            if (data.hasOwnProperty('hour')) {
                obj['hour'] = ApiClient.convertToType(data['hour'], 'Number');
            }
            if (data.hasOwnProperty('hours')) {
                obj['hours'] = ApiClient.convertToType(data['hours'], 'Number');
            }
            if (data.hasOwnProperty('leapdays')) {
                obj['leapdays'] = ApiClient.convertToType(data['leapdays'], 'Number');
            }
            if (data.hasOwnProperty('microsecond')) {
                obj['microsecond'] = ApiClient.convertToType(data['microsecond'], 'Number');
            }
            if (data.hasOwnProperty('microseconds')) {
                obj['microseconds'] = ApiClient.convertToType(data['microseconds'], 'Number');
            }
            if (data.hasOwnProperty('minute')) {
                obj['minute'] = ApiClient.convertToType(data['minute'], 'Number');
            }
            if (data.hasOwnProperty('minutes')) {
                obj['minutes'] = ApiClient.convertToType(data['minutes'], 'Number');
            }
            if (data.hasOwnProperty('month')) {
                obj['month'] = ApiClient.convertToType(data['month'], 'Number');
            }
            if (data.hasOwnProperty('months')) {
                obj['months'] = ApiClient.convertToType(data['months'], 'Number');
            }
            if (data.hasOwnProperty('second')) {
                obj['second'] = ApiClient.convertToType(data['second'], 'Number');
            }
            if (data.hasOwnProperty('seconds')) {
                obj['seconds'] = ApiClient.convertToType(data['seconds'], 'Number');
            }
            if (data.hasOwnProperty('year')) {
                obj['year'] = ApiClient.convertToType(data['year'], 'Number');
            }
            if (data.hasOwnProperty('years')) {
                obj['years'] = ApiClient.convertToType(data['years'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RelativeDelta</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RelativeDelta</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of RelativeDelta.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['__type'] && !(typeof data['__type'] === 'string' || data['__type'] instanceof String)) {
            throw new Error("Expected the field `__type` to be a primitive type in the JSON string but got " + data['__type']);
        }

        return true;
    }


}

RelativeDelta.RequiredProperties = ["__type", "day", "days", "hour", "hours", "leapdays", "microsecond", "microseconds", "minute", "minutes", "month", "months", "second", "seconds", "year", "years"];

/**
 * @member {String} __type
 */
RelativeDelta.prototype['__type'] = undefined;

/**
 * @member {Number} day
 */
RelativeDelta.prototype['day'] = undefined;

/**
 * @member {Number} days
 */
RelativeDelta.prototype['days'] = undefined;

/**
 * @member {Number} hour
 */
RelativeDelta.prototype['hour'] = undefined;

/**
 * @member {Number} hours
 */
RelativeDelta.prototype['hours'] = undefined;

/**
 * @member {Number} leapdays
 */
RelativeDelta.prototype['leapdays'] = undefined;

/**
 * @member {Number} microsecond
 */
RelativeDelta.prototype['microsecond'] = undefined;

/**
 * @member {Number} microseconds
 */
RelativeDelta.prototype['microseconds'] = undefined;

/**
 * @member {Number} minute
 */
RelativeDelta.prototype['minute'] = undefined;

/**
 * @member {Number} minutes
 */
RelativeDelta.prototype['minutes'] = undefined;

/**
 * @member {Number} month
 */
RelativeDelta.prototype['month'] = undefined;

/**
 * @member {Number} months
 */
RelativeDelta.prototype['months'] = undefined;

/**
 * @member {Number} second
 */
RelativeDelta.prototype['second'] = undefined;

/**
 * @member {Number} seconds
 */
RelativeDelta.prototype['seconds'] = undefined;

/**
 * @member {Number} year
 */
RelativeDelta.prototype['year'] = undefined;

/**
 * @member {Number} years
 */
RelativeDelta.prototype['years'] = undefined;






export default RelativeDelta;

