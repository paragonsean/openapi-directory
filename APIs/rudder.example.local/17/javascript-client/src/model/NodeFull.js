/**
 * Rudder API
 * Download OpenAPI specification: [openapi.yml](openapi.yml)  # Introduction  Rudder exposes a REST API, enabling the user to interact with Rudder without using the webapp, for example in scripts or cronjobs.  ## Versioning  Each time the API is extended with new features (new functions, new parameters, new responses, ...), it will be assigned a new version number. This will allow you to keep your existing scripts (based on previous behavior). Versions will always be integers (no 2.1 or 3.3, just 2, 3, 4, ...) or `latest`.  You can change the version of the API used by setting it either within the url or in a header:  * the URL: each URL is prefixed by its version id, like `/api/version/function`.  ```bash # Version 10 curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/10/rules # Latest curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/latest/rules # Wrong (not an integer) => 404 not found curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/3.14/rules ```  * the HTTP headers. You can add the **X-API-Version** header to your request. The value needs to be an integer or `latest`.  ```bash # Version 10 curl -X GET -H \"X-API-Token: yourToken\" -H \"X-API-Version: 10\" https://rudder.example.com/rudder/api/rules # Wrong => Error response indicating which versions are available curl -X GET -H \"X-API-Token: yourToken\" -H \"X-API-Version: 3.14\" https://rudder.example.com/rudder/api/rules ```  In the future, we may declare some versions as deprecated, in order to remove them in a later version of Rudder, but we will never remove any versions without warning, or without a safe period of time to allow migration from previous versions.   <h4>Existing versions</h4> <table>   <thead>     <tr>       <th style=\"width: 20%\">Version</th>       <th style=\"width: 20%\">Rudder versions it appeared in</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">1</td>       <td class=\"code\">Never released (for internal use only)</td>       <td>Experimental version</td>     </tr>     <tr>       <td class=\"code\">2 to 10 (deprecated)</td>       <td class=\"code\">4.3 and before</td>       <td>These versions provided the core set of API features for rules, directives, nodes global parameters, change requests and compliance, rudder settings and system API</td>     </tr>     <tr>       <td class=\"code\">11</td>       <td class=\"code\">5.0</td>       <td>New system API (replacing old localhost v1 api): status, maintenance operations and server behavior</td>     </tr>     <tr>       <td class=\"code\">12</td>       <td class=\"code\">6.0 and 6.1</td>       <td>Node key management</td>     </tr>     <tr>       <td class=\"code\">13</td>       <td class=\"code\">6.2</td>       <td><ul>         <li>Node status endpoint</li>         <li>System health check</li>         <li>System maintenance job to purge software [that endpoint was back-ported in 6.1]</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">14</td>       <td class=\"code\">7.0</td>       <td><ul>         <li>Secret management</li>         <li>Directive tree</li>         <li>Improve techniques management</li>         <li>Demote a relay</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">15</td>       <td class=\"code\">7.1</td>       <td><ul>         <li>Package updates in nodes</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">16</td>       <td class=\"code\">7.2</td>       <td><ul>         <li>Create node API included from plugin</li>         <li>Configuration archive import/export</li>       </ul></td>     </tr>   </tbody> </table>   ## Response format  All responses from the API are in the JSON format.  ```json {   \"action\": \"The name of the called function\",   \"id\": \"The ID of the element you want, if relevant\",   \"result\": \"The result of your action: success or error\",   \"data\": \"Only present if this is a success and depends on the function, it's usually a JSON object\",   \"errorDetails\": \"Only present if this is an error, it contains the error message\" } ```   * __Success__ responses are sent with the 200 HTTP (Success) code  * __Error__ responses are sent with a HTTP error code (mostly 5xx...)   ## HTTP method  Rudder's REST API is based on the usage of [HTTP methods](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html). We use them to indicate what action will be done by the request. Currently, we use four of them:   * **GET**: search or retrieve information (get rule details, get a group, ...)  * **PUT**: add new objects (create a directive, clone a Rule, ...)  * **DELETE**: remove objects (delete a node, delete a parameter, ...)  * **POST**: update existing objects (update a directive, reload a group, ...)   ## Parameters  ### General parameters  Some parameters are available for almost all API functions. They will be described in this section. They must be part of the query and can't be submitted in a JSON form.  #### Available for all requests  <table>   <thead>     <tr>       <th style=\"width: 30%\">Field</th>       <th style=\"width: 10%\">Type</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">prettify</td>       <td><b>boolean</b><br><i>optional</i></td>       <td>         Determine if the answer should be prettified (human friendly) or not. We recommend using this for debugging purposes, but not for general script usage as this does add some unnecessary load on the server side.         <p class=\"default-value\">Default value: <code>false</code></p>       </td>     </tr>   </tbody> </table>   #### Available for modification requests (PUT/POST/DELETE)  <table>   <thead>     <tr>       <th style=\"width: 25%\">Field</th>       <th style=\"width: 12%\">Type</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">reason</td>       <td><b>string</b><br><i>optional</i> or <i>required</i></td>       <td>         Set a message to explain the change. If you set the reason messages to be mandatory in the web interface, failing to supply this value will lead to an error.         <p class=\"default-value\">Default value: <code>\"\"</code></p>       </td>     </tr>     <tr>       <td class=\"code\">changeRequestName</td>       <td><b>string</b><br><i>optional</i></td>       <td>         Set the change request name, is used only if workflows are enabled. The default value depends on the function called         <p class=\"default-value\">Default value: <code>A default string for each function</code></p>       </td>     </tr>     <tr>       <td class=\"code\">changeRequestDescription</td>       <td><b>string</b><br><i>optional</i></td>       <td>         Set the change request description, is used only if workflows are enabled.         <p class=\"default-value\">Default value: <code>\"\"</code></p>       </td>     </tr>   </tbody> </table>   ### Passing parameters  Parameters to the API can be sent:  * As part of the URL for resource identification  * As data for POST/PUT requests    * Directly in JSON format    * As request arguments  #### As part of the URL for resource identification  Parameters in URLs are used to indicate which resource you want to interact with. The function will not work if this resource is missing.  ```bash # Get the Rule of ID \"id\" curl -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/latest/rules/id ```    CAUTION: To avoid surprising behavior, do not put a '/' at the end of an URL: it would be interpreted as '/[empty string parameter]' and redirected to '/index', likely not what you wanted to do.   #### Sending data for POST/PUT requests  ##### Directly in JSON format  JSON format is the preferred way to interact with Rudder API for creating or updating resources. You'll also have to set the *Content-Type* header to **application/json** (without it the JSON content would be ignored). In a `curl` `POST` request, that header can be provided with the `-H` parameter:  ```bash curl -X POST -H \"Content-Type: application/json\" ... ```  The supplied file must contain a valid JSON: strings need quotes, booleans and integers don't, etc.  The (human readable) format is:  ```json {   \"key1\": \"value1\",   \"key2\": false,   \"key3\": 42 } ```   Here is an example with inlined data:  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\" -H  \"Content-Type: application/json\" https://rudder.example.com/rudder/api/rules/latest/{id}   -d '{ \"displayName\": \"new name\", \"enabled\": false, \"directives\": \"directiveId\"}' ```  You can also pass a supply the JSON in a file:  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\" -H \"Content-Type: application/json\" https://rudder.example.com/rudder/api/rules/latest/{id} -d @jsonParam ```  Note that the general parameters view in the previous chapter cannot be passed in a JSON, and you will need to pass them a URL parameters if you want them to be taken into account (you can't mix JSON and request parameters):  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive with reason message \"Reason used\" curl -X POST -H \"X-API-Token: yourToken\" -H \"Content-Type: application/json\" \"https://rudder.example.com/rudder/api/rules/latest/{id}?reason=Reason used\" -d @jsonParam -d \"reason=Reason ignored\" ```  ##### Request parameters  In some cases, when you have little, simple data to update, JSON can feel bloated. In such cases, you can use request parameters. You will need to pass one parameter for each data you want to change.  Parameters follow the following schema:  ``` key=value ```  You can pass parameters by two means:  * As query parameters: At the end of your url, put a **?** then your first parameter and then a **&** before next parameters. In that case, parameters need to be https://en.wikipedia.org/wiki/Percent-encoding[URL encoded]  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\"  https://rudder.example.com/rudder/api/rules/latest/{id}?\"displayName=my new name\"&\"enabled=false\"&\"directives=aDirectiveId\" ```  * As request data: You can pass those parameters in the request data, they won't figure in the URL, making it lighter to read, You can pass a file that contains data.  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive (in file directive-info.json) curl -X POST -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/rules/latest/{id} -d \"displayName=my new name\" -d \"enabled=false\" -d @directive-info.json ``` 
 *
 * The version of the OpenAPI document: 17
 * Contact: dev@rudder.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import NodeAddInnerPropertiesInner from './NodeAddInnerPropertiesInner';
import NodeFullBios from './NodeFullBios';
import NodeFullControllersInner from './NodeFullControllersInner';
import NodeFullEnvironmentVariablesInner from './NodeFullEnvironmentVariablesInner';
import NodeFullFileSystemsInner from './NodeFullFileSystemsInner';
import NodeFullMachine from './NodeFullMachine';
import NodeFullManagementTechnologyDetails from './NodeFullManagementTechnologyDetails';
import NodeFullManagementTechnologyInner from './NodeFullManagementTechnologyInner';
import NodeFullMemoriesInner from './NodeFullMemoriesInner';
import NodeFullNetworkInterfacesInner from './NodeFullNetworkInterfacesInner';
import NodeFullOs from './NodeFullOs';
import NodeFullPortsInner from './NodeFullPortsInner';
import NodeFullProcessesInner from './NodeFullProcessesInner';
import NodeFullProcessorsInner from './NodeFullProcessorsInner';
import NodeFullSlotsInner from './NodeFullSlotsInner';
import NodeFullSoftwareInner from './NodeFullSoftwareInner';
import NodeFullSoftwareUpdateInner from './NodeFullSoftwareUpdateInner';
import NodeFullSoundInner from './NodeFullSoundInner';
import NodeFullStorageInner from './NodeFullStorageInner';
import NodeFullTimezone from './NodeFullTimezone';
import NodeFullVideosInner from './NodeFullVideosInner';
import NodeFullVirtualMachinesInner from './NodeFullVirtualMachinesInner';

/**
 * The NodeFull model module.
 * @module model/NodeFull
 * @version 17
 */
class NodeFull {
    /**
     * Constructs a new <code>NodeFull</code>.
     * @alias module:model/NodeFull
     * @param hostname {String} Fully qualified name of the node
     * @param id {String} Unique id of the node
     * @param ipAddresses {Array.<String>} IP addresses of the node (IPv4 and IPv6)
     * @param managementTechnology {Array.<module:model/NodeFullManagementTechnologyInner>} Management agents running on the node
     * @param policyServerId {String} Rudder policy server managing the node
     * @param properties {Array.<module:model/NodeAddInnerPropertiesInner>} Node properties (either set by user or filled by third party sources)
     * @param status {module:model/NodeFull.StatusEnum} Status of the node
     */
    constructor(hostname, id, ipAddresses, managementTechnology, policyServerId, properties, status) { 
        
        NodeFull.initialize(this, hostname, id, ipAddresses, managementTechnology, policyServerId, properties, status);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, hostname, id, ipAddresses, managementTechnology, policyServerId, properties, status) { 
        obj['hostname'] = hostname;
        obj['id'] = id;
        obj['ipAddresses'] = ipAddresses;
        obj['managementTechnology'] = managementTechnology;
        obj['policyServerId'] = policyServerId;
        obj['properties'] = properties;
        obj['status'] = status;
    }

    /**
     * Constructs a <code>NodeFull</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NodeFull} obj Optional instance to populate.
     * @return {module:model/NodeFull} The populated <code>NodeFull</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NodeFull();

            if (data.hasOwnProperty('accounts')) {
                obj['accounts'] = ApiClient.convertToType(data['accounts'], ['String']);
            }
            if (data.hasOwnProperty('architectureDescription')) {
                obj['architectureDescription'] = ApiClient.convertToType(data['architectureDescription'], 'String');
            }
            if (data.hasOwnProperty('bios')) {
                obj['bios'] = NodeFullBios.constructFromObject(data['bios']);
            }
            if (data.hasOwnProperty('controllers')) {
                obj['controllers'] = ApiClient.convertToType(data['controllers'], [NodeFullControllersInner]);
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('environmentVariables')) {
                obj['environmentVariables'] = ApiClient.convertToType(data['environmentVariables'], [NodeFullEnvironmentVariablesInner]);
            }
            if (data.hasOwnProperty('fileSystems')) {
                obj['fileSystems'] = ApiClient.convertToType(data['fileSystems'], [NodeFullFileSystemsInner]);
            }
            if (data.hasOwnProperty('hostname')) {
                obj['hostname'] = ApiClient.convertToType(data['hostname'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('ipAddresses')) {
                obj['ipAddresses'] = ApiClient.convertToType(data['ipAddresses'], ['String']);
            }
            if (data.hasOwnProperty('lastInventoryDate')) {
                obj['lastInventoryDate'] = ApiClient.convertToType(data['lastInventoryDate'], 'Date');
            }
            if (data.hasOwnProperty('lastRunDate')) {
                obj['lastRunDate'] = ApiClient.convertToType(data['lastRunDate'], 'Date');
            }
            if (data.hasOwnProperty('machine')) {
                obj['machine'] = NodeFullMachine.constructFromObject(data['machine']);
            }
            if (data.hasOwnProperty('managementTechnology')) {
                obj['managementTechnology'] = ApiClient.convertToType(data['managementTechnology'], [NodeFullManagementTechnologyInner]);
            }
            if (data.hasOwnProperty('managementTechnologyDetails')) {
                obj['managementTechnologyDetails'] = NodeFullManagementTechnologyDetails.constructFromObject(data['managementTechnologyDetails']);
            }
            if (data.hasOwnProperty('memories')) {
                obj['memories'] = ApiClient.convertToType(data['memories'], [NodeFullMemoriesInner]);
            }
            if (data.hasOwnProperty('networkInterfaces')) {
                obj['networkInterfaces'] = ApiClient.convertToType(data['networkInterfaces'], [NodeFullNetworkInterfacesInner]);
            }
            if (data.hasOwnProperty('os')) {
                obj['os'] = NodeFullOs.constructFromObject(data['os']);
            }
            if (data.hasOwnProperty('policyMode')) {
                obj['policyMode'] = ApiClient.convertToType(data['policyMode'], 'String');
            }
            if (data.hasOwnProperty('policyServerId')) {
                obj['policyServerId'] = ApiClient.convertToType(data['policyServerId'], 'String');
            }
            if (data.hasOwnProperty('ports')) {
                obj['ports'] = ApiClient.convertToType(data['ports'], [NodeFullPortsInner]);
            }
            if (data.hasOwnProperty('processes')) {
                obj['processes'] = ApiClient.convertToType(data['processes'], [NodeFullProcessesInner]);
            }
            if (data.hasOwnProperty('processors')) {
                obj['processors'] = ApiClient.convertToType(data['processors'], [NodeFullProcessorsInner]);
            }
            if (data.hasOwnProperty('properties')) {
                obj['properties'] = ApiClient.convertToType(data['properties'], [NodeAddInnerPropertiesInner]);
            }
            if (data.hasOwnProperty('ram')) {
                obj['ram'] = ApiClient.convertToType(data['ram'], 'Number');
            }
            if (data.hasOwnProperty('slots')) {
                obj['slots'] = ApiClient.convertToType(data['slots'], [NodeFullSlotsInner]);
            }
            if (data.hasOwnProperty('software')) {
                obj['software'] = ApiClient.convertToType(data['software'], [NodeFullSoftwareInner]);
            }
            if (data.hasOwnProperty('softwareUpdate')) {
                obj['softwareUpdate'] = ApiClient.convertToType(data['softwareUpdate'], [NodeFullSoftwareUpdateInner]);
            }
            if (data.hasOwnProperty('sound')) {
                obj['sound'] = ApiClient.convertToType(data['sound'], [NodeFullSoundInner]);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('storage')) {
                obj['storage'] = ApiClient.convertToType(data['storage'], [NodeFullStorageInner]);
            }
            if (data.hasOwnProperty('timezone')) {
                obj['timezone'] = NodeFullTimezone.constructFromObject(data['timezone']);
            }
            if (data.hasOwnProperty('videos')) {
                obj['videos'] = ApiClient.convertToType(data['videos'], [NodeFullVideosInner]);
            }
            if (data.hasOwnProperty('virtualMachines')) {
                obj['virtualMachines'] = ApiClient.convertToType(data['virtualMachines'], [NodeFullVirtualMachinesInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NodeFull</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NodeFull</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of NodeFull.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['accounts'])) {
            throw new Error("Expected the field `accounts` to be an array in the JSON data but got " + data['accounts']);
        }
        // ensure the json data is a string
        if (data['architectureDescription'] && !(typeof data['architectureDescription'] === 'string' || data['architectureDescription'] instanceof String)) {
            throw new Error("Expected the field `architectureDescription` to be a primitive type in the JSON string but got " + data['architectureDescription']);
        }
        // validate the optional field `bios`
        if (data['bios']) { // data not null
          NodeFullBios.validateJSON(data['bios']);
        }
        if (data['controllers']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['controllers'])) {
                throw new Error("Expected the field `controllers` to be an array in the JSON data but got " + data['controllers']);
            }
            // validate the optional field `controllers` (array)
            for (const item of data['controllers']) {
                NodeFullControllersInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        if (data['environmentVariables']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['environmentVariables'])) {
                throw new Error("Expected the field `environmentVariables` to be an array in the JSON data but got " + data['environmentVariables']);
            }
            // validate the optional field `environmentVariables` (array)
            for (const item of data['environmentVariables']) {
                NodeFullEnvironmentVariablesInner.validateJSON(item);
            };
        }
        if (data['fileSystems']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['fileSystems'])) {
                throw new Error("Expected the field `fileSystems` to be an array in the JSON data but got " + data['fileSystems']);
            }
            // validate the optional field `fileSystems` (array)
            for (const item of data['fileSystems']) {
                NodeFullFileSystemsInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['hostname'] && !(typeof data['hostname'] === 'string' || data['hostname'] instanceof String)) {
            throw new Error("Expected the field `hostname` to be a primitive type in the JSON string but got " + data['hostname']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['ipAddresses'])) {
            throw new Error("Expected the field `ipAddresses` to be an array in the JSON data but got " + data['ipAddresses']);
        }
        // validate the optional field `machine`
        if (data['machine']) { // data not null
          NodeFullMachine.validateJSON(data['machine']);
        }
        if (data['managementTechnology']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['managementTechnology'])) {
                throw new Error("Expected the field `managementTechnology` to be an array in the JSON data but got " + data['managementTechnology']);
            }
            // validate the optional field `managementTechnology` (array)
            for (const item of data['managementTechnology']) {
                NodeFullManagementTechnologyInner.validateJSON(item);
            };
        }
        // validate the optional field `managementTechnologyDetails`
        if (data['managementTechnologyDetails']) { // data not null
          NodeFullManagementTechnologyDetails.validateJSON(data['managementTechnologyDetails']);
        }
        if (data['memories']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['memories'])) {
                throw new Error("Expected the field `memories` to be an array in the JSON data but got " + data['memories']);
            }
            // validate the optional field `memories` (array)
            for (const item of data['memories']) {
                NodeFullMemoriesInner.validateJSON(item);
            };
        }
        if (data['networkInterfaces']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['networkInterfaces'])) {
                throw new Error("Expected the field `networkInterfaces` to be an array in the JSON data but got " + data['networkInterfaces']);
            }
            // validate the optional field `networkInterfaces` (array)
            for (const item of data['networkInterfaces']) {
                NodeFullNetworkInterfacesInner.validateJSON(item);
            };
        }
        // validate the optional field `os`
        if (data['os']) { // data not null
          NodeFullOs.validateJSON(data['os']);
        }
        // ensure the json data is a string
        if (data['policyMode'] && !(typeof data['policyMode'] === 'string' || data['policyMode'] instanceof String)) {
            throw new Error("Expected the field `policyMode` to be a primitive type in the JSON string but got " + data['policyMode']);
        }
        // ensure the json data is a string
        if (data['policyServerId'] && !(typeof data['policyServerId'] === 'string' || data['policyServerId'] instanceof String)) {
            throw new Error("Expected the field `policyServerId` to be a primitive type in the JSON string but got " + data['policyServerId']);
        }
        if (data['ports']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['ports'])) {
                throw new Error("Expected the field `ports` to be an array in the JSON data but got " + data['ports']);
            }
            // validate the optional field `ports` (array)
            for (const item of data['ports']) {
                NodeFullPortsInner.validateJSON(item);
            };
        }
        if (data['processes']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['processes'])) {
                throw new Error("Expected the field `processes` to be an array in the JSON data but got " + data['processes']);
            }
            // validate the optional field `processes` (array)
            for (const item of data['processes']) {
                NodeFullProcessesInner.validateJSON(item);
            };
        }
        if (data['processors']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['processors'])) {
                throw new Error("Expected the field `processors` to be an array in the JSON data but got " + data['processors']);
            }
            // validate the optional field `processors` (array)
            for (const item of data['processors']) {
                NodeFullProcessorsInner.validateJSON(item);
            };
        }
        if (data['properties']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['properties'])) {
                throw new Error("Expected the field `properties` to be an array in the JSON data but got " + data['properties']);
            }
            // validate the optional field `properties` (array)
            for (const item of data['properties']) {
                NodeAddInnerPropertiesInner.validateJSON(item);
            };
        }
        if (data['slots']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['slots'])) {
                throw new Error("Expected the field `slots` to be an array in the JSON data but got " + data['slots']);
            }
            // validate the optional field `slots` (array)
            for (const item of data['slots']) {
                NodeFullSlotsInner.validateJSON(item);
            };
        }
        if (data['software']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['software'])) {
                throw new Error("Expected the field `software` to be an array in the JSON data but got " + data['software']);
            }
            // validate the optional field `software` (array)
            for (const item of data['software']) {
                NodeFullSoftwareInner.validateJSON(item);
            };
        }
        if (data['softwareUpdate']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['softwareUpdate'])) {
                throw new Error("Expected the field `softwareUpdate` to be an array in the JSON data but got " + data['softwareUpdate']);
            }
            // validate the optional field `softwareUpdate` (array)
            for (const item of data['softwareUpdate']) {
                NodeFullSoftwareUpdateInner.validateJSON(item);
            };
        }
        if (data['sound']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['sound'])) {
                throw new Error("Expected the field `sound` to be an array in the JSON data but got " + data['sound']);
            }
            // validate the optional field `sound` (array)
            for (const item of data['sound']) {
                NodeFullSoundInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        if (data['storage']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['storage'])) {
                throw new Error("Expected the field `storage` to be an array in the JSON data but got " + data['storage']);
            }
            // validate the optional field `storage` (array)
            for (const item of data['storage']) {
                NodeFullStorageInner.validateJSON(item);
            };
        }
        // validate the optional field `timezone`
        if (data['timezone']) { // data not null
          NodeFullTimezone.validateJSON(data['timezone']);
        }
        if (data['videos']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['videos'])) {
                throw new Error("Expected the field `videos` to be an array in the JSON data but got " + data['videos']);
            }
            // validate the optional field `videos` (array)
            for (const item of data['videos']) {
                NodeFullVideosInner.validateJSON(item);
            };
        }
        if (data['virtualMachines']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['virtualMachines'])) {
                throw new Error("Expected the field `virtualMachines` to be an array in the JSON data but got " + data['virtualMachines']);
            }
            // validate the optional field `virtualMachines` (array)
            for (const item of data['virtualMachines']) {
                NodeFullVirtualMachinesInner.validateJSON(item);
            };
        }

        return true;
    }


}

NodeFull.RequiredProperties = ["hostname", "id", "ipAddresses", "managementTechnology", "policyServerId", "properties", "status"];

/**
 * User accounts declared in the node
 * @member {Array.<String>} accounts
 */
NodeFull.prototype['accounts'] = undefined;

/**
 * Information about CPU architecture (32/64 bits)
 * @member {String} architectureDescription
 */
NodeFull.prototype['architectureDescription'] = undefined;

/**
 * @member {module:model/NodeFullBios} bios
 */
NodeFull.prototype['bios'] = undefined;

/**
 * Physical controller information
 * @member {Array.<module:model/NodeFullControllersInner>} controllers
 */
NodeFull.prototype['controllers'] = undefined;

/**
 * A human intended description of the node (not used)
 * @member {String} description
 */
NodeFull.prototype['description'] = undefined;

/**
 * Environment variables defined on the node in the context of the agent
 * @member {Array.<module:model/NodeFullEnvironmentVariablesInner>} environmentVariables
 */
NodeFull.prototype['environmentVariables'] = undefined;

/**
 * File system declared on the node
 * @member {Array.<module:model/NodeFullFileSystemsInner>} fileSystems
 */
NodeFull.prototype['fileSystems'] = undefined;

/**
 * Fully qualified name of the node
 * @member {String} hostname
 */
NodeFull.prototype['hostname'] = undefined;

/**
 * Unique id of the node
 * @member {String} id
 */
NodeFull.prototype['id'] = undefined;

/**
 * IP addresses of the node (IPv4 and IPv6)
 * @member {Array.<String>} ipAddresses
 */
NodeFull.prototype['ipAddresses'] = undefined;

/**
 * Date and time of the latest generated inventory, if one is available (node time). Up to API v11, format was: \"YYYY-MM-dd HH:mm\"
 * @member {Date} lastInventoryDate
 */
NodeFull.prototype['lastInventoryDate'] = undefined;

/**
 * Date and time of the latest run, if one is available (node time). Up to API v11, format was: \"YYYY-MM-dd HH:mm\"
 * @member {Date} lastRunDate
 */
NodeFull.prototype['lastRunDate'] = undefined;

/**
 * @member {module:model/NodeFullMachine} machine
 */
NodeFull.prototype['machine'] = undefined;

/**
 * Management agents running on the node
 * @member {Array.<module:model/NodeFullManagementTechnologyInner>} managementTechnology
 */
NodeFull.prototype['managementTechnology'] = undefined;

/**
 * @member {module:model/NodeFullManagementTechnologyDetails} managementTechnologyDetails
 */
NodeFull.prototype['managementTechnologyDetails'] = undefined;

/**
 * Memory slots
 * @member {Array.<module:model/NodeFullMemoriesInner>} memories
 */
NodeFull.prototype['memories'] = undefined;

/**
 * Detailed information about registered network interfaces on the node
 * @member {Array.<module:model/NodeFullNetworkInterfacesInner>} networkInterfaces
 */
NodeFull.prototype['networkInterfaces'] = undefined;

/**
 * @member {module:model/NodeFullOs} os
 */
NodeFull.prototype['os'] = undefined;

/**
 * Rudder policy mode for the node (`default` follows the global configuration)
 * @member {module:model/NodeFull.PolicyModeEnum} policyMode
 */
NodeFull.prototype['policyMode'] = undefined;

/**
 * Rudder policy server managing the node
 * @member {String} policyServerId
 */
NodeFull.prototype['policyServerId'] = undefined;

/**
 * Physical port information objects
 * @member {Array.<module:model/NodeFullPortsInner>} ports
 */
NodeFull.prototype['ports'] = undefined;

/**
 * Process running (at inventory time)
 * @member {Array.<module:model/NodeFullProcessesInner>} processes
 */
NodeFull.prototype['processes'] = undefined;

/**
 * CPU information
 * @member {Array.<module:model/NodeFullProcessorsInner>} processors
 */
NodeFull.prototype['processors'] = undefined;

/**
 * Node properties (either set by user or filled by third party sources)
 * @member {Array.<module:model/NodeAddInnerPropertiesInner>} properties
 */
NodeFull.prototype['properties'] = undefined;

/**
 * Size of RAM in MB
 * @member {Number} ram
 */
NodeFull.prototype['ram'] = undefined;

/**
 * Physical extension slot information
 * @member {Array.<module:model/NodeFullSlotsInner>} slots
 */
NodeFull.prototype['slots'] = undefined;

/**
 * Software installed on the node (can have thousands items)
 * @member {Array.<module:model/NodeFullSoftwareInner>} software
 */
NodeFull.prototype['software'] = undefined;

/**
 * Software that can be updated on that machine
 * @member {Array.<module:model/NodeFullSoftwareUpdateInner>} softwareUpdate
 */
NodeFull.prototype['softwareUpdate'] = undefined;

/**
 * Sound card information
 * @member {Array.<module:model/NodeFullSoundInner>} sound
 */
NodeFull.prototype['sound'] = undefined;

/**
 * Status of the node
 * @member {module:model/NodeFull.StatusEnum} status
 */
NodeFull.prototype['status'] = undefined;

/**
 * Storage (disks) information objects
 * @member {Array.<module:model/NodeFullStorageInner>} storage
 */
NodeFull.prototype['storage'] = undefined;

/**
 * @member {module:model/NodeFullTimezone} timezone
 */
NodeFull.prototype['timezone'] = undefined;

/**
 * Video card information
 * @member {Array.<module:model/NodeFullVideosInner>} videos
 */
NodeFull.prototype['videos'] = undefined;

/**
 * Hosted virtual machine information
 * @member {Array.<module:model/NodeFullVirtualMachinesInner>} virtualMachines
 */
NodeFull.prototype['virtualMachines'] = undefined;





/**
 * Allowed values for the <code>policyMode</code> property.
 * @enum {String}
 * @readonly
 */
NodeFull['PolicyModeEnum'] = {

    /**
     * value: "enforce"
     * @const
     */
    "enforce": "enforce",

    /**
     * value: "audit"
     * @const
     */
    "audit": "audit",

    /**
     * value: "default"
     * @const
     */
    "default": "default"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
NodeFull['StatusEnum'] = {

    /**
     * value: "pending"
     * @const
     */
    "pending": "pending",

    /**
     * value: "accepted"
     * @const
     */
    "accepted": "accepted",

    /**
     * value: "deleted"
     * @const
     */
    "deleted": "deleted"
};



export default NodeFull;

