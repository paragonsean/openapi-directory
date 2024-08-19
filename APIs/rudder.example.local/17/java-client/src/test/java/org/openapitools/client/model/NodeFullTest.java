/*
 * Rudder API
 * Download OpenAPI specification: [openapi.yml](openapi.yml)  # Introduction  Rudder exposes a REST API, enabling the user to interact with Rudder without using the webapp, for example in scripts or cronjobs.  ## Versioning  Each time the API is extended with new features (new functions, new parameters, new responses, ...), it will be assigned a new version number. This will allow you to keep your existing scripts (based on previous behavior). Versions will always be integers (no 2.1 or 3.3, just 2, 3, 4, ...) or `latest`.  You can change the version of the API used by setting it either within the url or in a header:  * the URL: each URL is prefixed by its version id, like `/api/version/function`.  ```bash # Version 10 curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/10/rules # Latest curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/latest/rules # Wrong (not an integer) => 404 not found curl -X GET -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/3.14/rules ```  * the HTTP headers. You can add the **X-API-Version** header to your request. The value needs to be an integer or `latest`.  ```bash # Version 10 curl -X GET -H \"X-API-Token: yourToken\" -H \"X-API-Version: 10\" https://rudder.example.com/rudder/api/rules # Wrong => Error response indicating which versions are available curl -X GET -H \"X-API-Token: yourToken\" -H \"X-API-Version: 3.14\" https://rudder.example.com/rudder/api/rules ```  In the future, we may declare some versions as deprecated, in order to remove them in a later version of Rudder, but we will never remove any versions without warning, or without a safe period of time to allow migration from previous versions.   <h4>Existing versions</h4> <table>   <thead>     <tr>       <th style=\"width: 20%\">Version</th>       <th style=\"width: 20%\">Rudder versions it appeared in</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">1</td>       <td class=\"code\">Never released (for internal use only)</td>       <td>Experimental version</td>     </tr>     <tr>       <td class=\"code\">2 to 10 (deprecated)</td>       <td class=\"code\">4.3 and before</td>       <td>These versions provided the core set of API features for rules, directives, nodes global parameters, change requests and compliance, rudder settings and system API</td>     </tr>     <tr>       <td class=\"code\">11</td>       <td class=\"code\">5.0</td>       <td>New system API (replacing old localhost v1 api): status, maintenance operations and server behavior</td>     </tr>     <tr>       <td class=\"code\">12</td>       <td class=\"code\">6.0 and 6.1</td>       <td>Node key management</td>     </tr>     <tr>       <td class=\"code\">13</td>       <td class=\"code\">6.2</td>       <td><ul>         <li>Node status endpoint</li>         <li>System health check</li>         <li>System maintenance job to purge software [that endpoint was back-ported in 6.1]</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">14</td>       <td class=\"code\">7.0</td>       <td><ul>         <li>Secret management</li>         <li>Directive tree</li>         <li>Improve techniques management</li>         <li>Demote a relay</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">15</td>       <td class=\"code\">7.1</td>       <td><ul>         <li>Package updates in nodes</li>       </ul></td>     </tr>     <tr>       <td class=\"code\">16</td>       <td class=\"code\">7.2</td>       <td><ul>         <li>Create node API included from plugin</li>         <li>Configuration archive import/export</li>       </ul></td>     </tr>   </tbody> </table>   ## Response format  All responses from the API are in the JSON format.  ```json {   \"action\": \"The name of the called function\",   \"id\": \"The ID of the element you want, if relevant\",   \"result\": \"The result of your action: success or error\",   \"data\": \"Only present if this is a success and depends on the function, it's usually a JSON object\",   \"errorDetails\": \"Only present if this is an error, it contains the error message\" } ```   * __Success__ responses are sent with the 200 HTTP (Success) code  * __Error__ responses are sent with a HTTP error code (mostly 5xx...)   ## HTTP method  Rudder's REST API is based on the usage of [HTTP methods](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html). We use them to indicate what action will be done by the request. Currently, we use four of them:   * **GET**: search or retrieve information (get rule details, get a group, ...)  * **PUT**: add new objects (create a directive, clone a Rule, ...)  * **DELETE**: remove objects (delete a node, delete a parameter, ...)  * **POST**: update existing objects (update a directive, reload a group, ...)   ## Parameters  ### General parameters  Some parameters are available for almost all API functions. They will be described in this section. They must be part of the query and can't be submitted in a JSON form.  #### Available for all requests  <table>   <thead>     <tr>       <th style=\"width: 30%\">Field</th>       <th style=\"width: 10%\">Type</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">prettify</td>       <td><b>boolean</b><br><i>optional</i></td>       <td>         Determine if the answer should be prettified (human friendly) or not. We recommend using this for debugging purposes, but not for general script usage as this does add some unnecessary load on the server side.         <p class=\"default-value\">Default value: <code>false</code></p>       </td>     </tr>   </tbody> </table>   #### Available for modification requests (PUT/POST/DELETE)  <table>   <thead>     <tr>       <th style=\"width: 25%\">Field</th>       <th style=\"width: 12%\">Type</th>       <th style=\"width: 70%\">Description</th>     </tr>   </thead>   <tbody>     <tr>       <td class=\"code\">reason</td>       <td><b>string</b><br><i>optional</i> or <i>required</i></td>       <td>         Set a message to explain the change. If you set the reason messages to be mandatory in the web interface, failing to supply this value will lead to an error.         <p class=\"default-value\">Default value: <code>\"\"</code></p>       </td>     </tr>     <tr>       <td class=\"code\">changeRequestName</td>       <td><b>string</b><br><i>optional</i></td>       <td>         Set the change request name, is used only if workflows are enabled. The default value depends on the function called         <p class=\"default-value\">Default value: <code>A default string for each function</code></p>       </td>     </tr>     <tr>       <td class=\"code\">changeRequestDescription</td>       <td><b>string</b><br><i>optional</i></td>       <td>         Set the change request description, is used only if workflows are enabled.         <p class=\"default-value\">Default value: <code>\"\"</code></p>       </td>     </tr>   </tbody> </table>   ### Passing parameters  Parameters to the API can be sent:  * As part of the URL for resource identification  * As data for POST/PUT requests    * Directly in JSON format    * As request arguments  #### As part of the URL for resource identification  Parameters in URLs are used to indicate which resource you want to interact with. The function will not work if this resource is missing.  ```bash # Get the Rule of ID \"id\" curl -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/latest/rules/id ```    CAUTION: To avoid surprising behavior, do not put a '/' at the end of an URL: it would be interpreted as '/[empty string parameter]' and redirected to '/index', likely not what you wanted to do.   #### Sending data for POST/PUT requests  ##### Directly in JSON format  JSON format is the preferred way to interact with Rudder API for creating or updating resources. You'll also have to set the *Content-Type* header to **application/json** (without it the JSON content would be ignored). In a `curl` `POST` request, that header can be provided with the `-H` parameter:  ```bash curl -X POST -H \"Content-Type: application/json\" ... ```  The supplied file must contain a valid JSON: strings need quotes, booleans and integers don't, etc.  The (human readable) format is:  ```json {   \"key1\": \"value1\",   \"key2\": false,   \"key3\": 42 } ```   Here is an example with inlined data:  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\" -H  \"Content-Type: application/json\" https://rudder.example.com/rudder/api/rules/latest/{id}   -d '{ \"displayName\": \"new name\", \"enabled\": false, \"directives\": \"directiveId\"}' ```  You can also pass a supply the JSON in a file:  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\" -H \"Content-Type: application/json\" https://rudder.example.com/rudder/api/rules/latest/{id} -d @jsonParam ```  Note that the general parameters view in the previous chapter cannot be passed in a JSON, and you will need to pass them a URL parameters if you want them to be taken into account (you can't mix JSON and request parameters):  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive with reason message \"Reason used\" curl -X POST -H \"X-API-Token: yourToken\" -H \"Content-Type: application/json\" \"https://rudder.example.com/rudder/api/rules/latest/{id}?reason=Reason used\" -d @jsonParam -d \"reason=Reason ignored\" ```  ##### Request parameters  In some cases, when you have little, simple data to update, JSON can feel bloated. In such cases, you can use request parameters. You will need to pass one parameter for each data you want to change.  Parameters follow the following schema:  ``` key=value ```  You can pass parameters by two means:  * As query parameters: At the end of your url, put a **?** then your first parameter and then a **&** before next parameters. In that case, parameters need to be https://en.wikipedia.org/wiki/Percent-encoding[URL encoded]  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive curl -X POST -H \"X-API-Token: yourToken\"  https://rudder.example.com/rudder/api/rules/latest/{id}?\"displayName=my new name\"&\"enabled=false\"&\"directives=aDirectiveId\" ```  * As request data: You can pass those parameters in the request data, they won't figure in the URL, making it lighter to read, You can pass a file that contains data.  ```bash # Update the Rule 'id' with a new name, disabled, and setting it one directive (in file directive-info.json) curl -X POST -H \"X-API-Token: yourToken\" https://rudder.example.com/rudder/api/rules/latest/{id} -d \"displayName=my new name\" -d \"enabled=false\" -d @directive-info.json ``` 
 *
 * The version of the OpenAPI document: 17
 * Contact: dev@rudder.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.NodeAddInnerPropertiesInner;
import org.openapitools.client.model.NodeFullBios;
import org.openapitools.client.model.NodeFullControllersInner;
import org.openapitools.client.model.NodeFullEnvironmentVariablesInner;
import org.openapitools.client.model.NodeFullFileSystemsInner;
import org.openapitools.client.model.NodeFullMachine;
import org.openapitools.client.model.NodeFullManagementTechnologyDetails;
import org.openapitools.client.model.NodeFullManagementTechnologyInner;
import org.openapitools.client.model.NodeFullMemoriesInner;
import org.openapitools.client.model.NodeFullNetworkInterfacesInner;
import org.openapitools.client.model.NodeFullOs;
import org.openapitools.client.model.NodeFullPortsInner;
import org.openapitools.client.model.NodeFullProcessesInner;
import org.openapitools.client.model.NodeFullProcessorsInner;
import org.openapitools.client.model.NodeFullSlotsInner;
import org.openapitools.client.model.NodeFullSoftwareInner;
import org.openapitools.client.model.NodeFullSoftwareUpdateInner;
import org.openapitools.client.model.NodeFullSoundInner;
import org.openapitools.client.model.NodeFullStorageInner;
import org.openapitools.client.model.NodeFullTimezone;
import org.openapitools.client.model.NodeFullVideosInner;
import org.openapitools.client.model.NodeFullVirtualMachinesInner;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for NodeFull
 */
public class NodeFullTest {
    private final NodeFull model = new NodeFull();

    /**
     * Model tests for NodeFull
     */
    @Test
    public void testNodeFull() {
        // TODO: test NodeFull
    }

    /**
     * Test the property 'accounts'
     */
    @Test
    public void accountsTest() {
        // TODO: test accounts
    }

    /**
     * Test the property 'architectureDescription'
     */
    @Test
    public void architectureDescriptionTest() {
        // TODO: test architectureDescription
    }

    /**
     * Test the property 'bios'
     */
    @Test
    public void biosTest() {
        // TODO: test bios
    }

    /**
     * Test the property 'controllers'
     */
    @Test
    public void controllersTest() {
        // TODO: test controllers
    }

    /**
     * Test the property 'description'
     */
    @Test
    public void descriptionTest() {
        // TODO: test description
    }

    /**
     * Test the property 'environmentVariables'
     */
    @Test
    public void environmentVariablesTest() {
        // TODO: test environmentVariables
    }

    /**
     * Test the property 'fileSystems'
     */
    @Test
    public void fileSystemsTest() {
        // TODO: test fileSystems
    }

    /**
     * Test the property 'hostname'
     */
    @Test
    public void hostnameTest() {
        // TODO: test hostname
    }

    /**
     * Test the property 'id'
     */
    @Test
    public void idTest() {
        // TODO: test id
    }

    /**
     * Test the property 'ipAddresses'
     */
    @Test
    public void ipAddressesTest() {
        // TODO: test ipAddresses
    }

    /**
     * Test the property 'lastInventoryDate'
     */
    @Test
    public void lastInventoryDateTest() {
        // TODO: test lastInventoryDate
    }

    /**
     * Test the property 'lastRunDate'
     */
    @Test
    public void lastRunDateTest() {
        // TODO: test lastRunDate
    }

    /**
     * Test the property 'machine'
     */
    @Test
    public void machineTest() {
        // TODO: test machine
    }

    /**
     * Test the property 'managementTechnology'
     */
    @Test
    public void managementTechnologyTest() {
        // TODO: test managementTechnology
    }

    /**
     * Test the property 'managementTechnologyDetails'
     */
    @Test
    public void managementTechnologyDetailsTest() {
        // TODO: test managementTechnologyDetails
    }

    /**
     * Test the property 'memories'
     */
    @Test
    public void memoriesTest() {
        // TODO: test memories
    }

    /**
     * Test the property 'networkInterfaces'
     */
    @Test
    public void networkInterfacesTest() {
        // TODO: test networkInterfaces
    }

    /**
     * Test the property 'os'
     */
    @Test
    public void osTest() {
        // TODO: test os
    }

    /**
     * Test the property 'policyMode'
     */
    @Test
    public void policyModeTest() {
        // TODO: test policyMode
    }

    /**
     * Test the property 'policyServerId'
     */
    @Test
    public void policyServerIdTest() {
        // TODO: test policyServerId
    }

    /**
     * Test the property 'ports'
     */
    @Test
    public void portsTest() {
        // TODO: test ports
    }

    /**
     * Test the property 'processes'
     */
    @Test
    public void processesTest() {
        // TODO: test processes
    }

    /**
     * Test the property 'processors'
     */
    @Test
    public void processorsTest() {
        // TODO: test processors
    }

    /**
     * Test the property 'properties'
     */
    @Test
    public void propertiesTest() {
        // TODO: test properties
    }

    /**
     * Test the property 'ram'
     */
    @Test
    public void ramTest() {
        // TODO: test ram
    }

    /**
     * Test the property 'slots'
     */
    @Test
    public void slotsTest() {
        // TODO: test slots
    }

    /**
     * Test the property 'software'
     */
    @Test
    public void softwareTest() {
        // TODO: test software
    }

    /**
     * Test the property 'softwareUpdate'
     */
    @Test
    public void softwareUpdateTest() {
        // TODO: test softwareUpdate
    }

    /**
     * Test the property 'sound'
     */
    @Test
    public void soundTest() {
        // TODO: test sound
    }

    /**
     * Test the property 'status'
     */
    @Test
    public void statusTest() {
        // TODO: test status
    }

    /**
     * Test the property 'storage'
     */
    @Test
    public void storageTest() {
        // TODO: test storage
    }

    /**
     * Test the property 'timezone'
     */
    @Test
    public void timezoneTest() {
        // TODO: test timezone
    }

    /**
     * Test the property 'videos'
     */
    @Test
    public void videosTest() {
        // TODO: test videos
    }

    /**
     * Test the property 'virtualMachines'
     */
    @Test
    public void virtualMachinesTest() {
        // TODO: test virtualMachines
    }

}
