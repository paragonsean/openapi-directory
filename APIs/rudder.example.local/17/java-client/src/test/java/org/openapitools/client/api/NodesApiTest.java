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


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ApplyPolicyAllNodes200Response;
import org.openapitools.client.model.ChangePendingNodeStatus200Response;
import org.openapitools.client.model.ChangePendingNodeStatusRequest;
import org.openapitools.client.model.CreateNodes200Response;
import org.openapitools.client.model.DeleteNode200Response;
import org.openapitools.client.model.GetNodesStatus200Response;
import org.openapitools.client.model.ListAcceptedNodes200Response;
import org.openapitools.client.model.ListPendingNodes200Response;
import org.openapitools.client.model.NodeAddInner;
import org.openapitools.client.model.NodeDetails200Response;
import org.openapitools.client.model.NodeInheritedProperties200Response;
import org.openapitools.client.model.NodeSettings;
import org.openapitools.client.model.UpdateNode200Response;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for NodesApi
 */
@Disabled
public class NodesApiTest {

    private final NodesApi api = new NodesApi();

    /**
     * Trigger an agent run
     *
     * This API allows to trigger an agent run on the target node. Response is a stream of the actual agent run on the node.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void applyPolicyTest() throws ApiException {
        String nodeId = null;
        String response = api.applyPolicy(nodeId);
        // TODO: test validations
    }

    /**
     * Trigger an agent run on all nodes
     *
     * This API allows to trigger an agent run on all nodes. Response contains a json stating if agent could be started on each node, but not if the run went fine and do not display any output from it. You can see the result of the run in Rudder web interface or in the each agent logs.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void applyPolicyAllNodesTest() throws ApiException {
        ApplyPolicyAllNodes200Response response = api.applyPolicyAllNodes();
        // TODO: test validations
    }

    /**
     * Update pending Node status
     *
     * Accept or refuse a pending node
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void changePendingNodeStatusTest() throws ApiException {
        String nodeId = null;
        ChangePendingNodeStatusRequest changePendingNodeStatusRequest = null;
        ChangePendingNodeStatus200Response response = api.changePendingNodeStatus(nodeId, changePendingNodeStatusRequest);
        // TODO: test validations
    }

    /**
     * Create one or several new nodes
     *
     * Use the provided array of node information to create new nodes
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createNodesTest() throws ApiException {
        List<NodeAddInner> nodeAddInner = null;
        CreateNodes200Response response = api.createNodes(nodeAddInner);
        // TODO: test validations
    }

    /**
     * Delete a node
     *
     * Remove a node from the Rudder server. It won&#39;t be managed anymore.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteNodeTest() throws ApiException {
        String nodeId = null;
        String mode = null;
        DeleteNode200Response response = api.deleteNode(nodeId, mode);
        // TODO: test validations
    }

    /**
     * Get nodes acceptation status
     *
     * Get acceptation status (pending, accepted, deleted, unknown) of a list of nodes
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNodesStatusTest() throws ApiException {
        String ids = null;
        GetNodesStatus200Response response = api.getNodesStatus(ids);
        // TODO: test validations
    }

    /**
     * List managed nodes
     *
     * Get information about the nodes managed by the target server
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listAcceptedNodesTest() throws ApiException {
        String include = null;
        Object query = null;
        List<Object> where = null;
        String composition = null;
        String select = null;
        ListAcceptedNodes200Response response = api.listAcceptedNodes(include, query, where, composition, select);
        // TODO: test validations
    }

    /**
     * List pending nodes
     *
     * Get information about the nodes pending acceptation
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listPendingNodesTest() throws ApiException {
        String include = null;
        Object query = null;
        List<Object> where = null;
        String composition = null;
        String select = null;
        ListPendingNodes200Response response = api.listPendingNodes(include, query, where, composition, select);
        // TODO: test validations
    }

    /**
     * Get information about a node
     *
     * Get details about a given node
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void nodeDetailsTest() throws ApiException {
        String nodeId = null;
        String include = null;
        NodeDetails200Response response = api.nodeDetails(nodeId, include);
        // TODO: test validations
    }

    /**
     * Get inherited node properties for a node
     *
     * This API returns all node properties for a node, including group inherited ones.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void nodeInheritedPropertiesTest() throws ApiException {
        String nodeId = null;
        NodeInheritedProperties200Response response = api.nodeInheritedProperties(nodeId);
        // TODO: test validations
    }

    /**
     * Update node settings and properties
     *
     * Update node settings and properties
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateNodeTest() throws ApiException {
        String nodeId = null;
        NodeSettings nodeSettings = null;
        UpdateNode200Response response = api.updateNode(nodeId, nodeSettings);
        // TODO: test validations
    }

}
